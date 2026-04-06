# app/modules/auth/auth_service.py
# 🔐 Servicio de autenticación

from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.identities.identity_model import Identity
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify_password
)
from app.core.authorization.permissions import get_user_permissions


# =========================================================
# 🔄 REFRESH TOKEN → ACCESS TOKEN
# =========================================================
def refresh_access_token(payload: dict) -> str:
    """
    Genera un nuevo access token a partir de un refresh token válido.
    """

    # 🔒 Validar tipo de token
    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=401,
            detail="Refresh token inválido"
        )

    # 🔁 Generar nuevo access token
    return create_access_token({
        "sub": payload.get("sub"),
        "roles": payload.get("roles", []),
        "permissions": payload.get("permissions", []),
        "username": payload.get("username"),
        "type": "access",
        "iat": datetime.now(timezone.utc).timestamp()
    })


# =========================================================
# 🔐 LOGIN (email + password)
# =========================================================
def authenticate_user(
    db: Session,
    email: str,
    password: str
) -> dict:
    """
    Autentica un usuario y genera tokens JWT.

    Flujo:
    1. Buscar identidad por email
    2. Validar password
    3. Validar estado usuario
    4. Obtener roles y permisos
    5. Generar tokens
    """

    # =========================================================
    # 🔎 1. BUSCAR IDENTIDAD
    # =========================================================
    identity = db.query(Identity).filter(
        Identity.email == email
    ).first()

    if not identity:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    # =========================================================
    # 🔐 2. VALIDAR PASSWORD
    # =========================================================
    if not identity.password_hash:
        raise HTTPException(
            status_code=401,
            detail="Login no permitido para este proveedor"
        )

    if not verify_password(password, identity.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    # =========================================================
    # 👤 3. VALIDAR USUARIO
    # =========================================================
    user = identity.usuario

    if not user or not user.activo:
        raise HTTPException(
            status_code=403,
            detail="Usuario desactivado o inválido"
        )

    # =========================================================
    # 🎭 4. ROLES EFECTIVOS
    # =========================================================
    # ⚠️ prioridad: identity.rol (legacy) → user.roles (RBAC)
    if identity.rol:
        roles = [identity.rol.nombre.lower()]
    else:
        roles = [role.nombre.lower() for role in user.roles]

    # =========================================================
    # 🔑 5. PERMISOS EFECTIVOS
    # =========================================================
    permissions = get_user_permissions(user)

    # =========================================================
    # 🪪 6. PAYLOAD BASE
    # =========================================================
    base_payload = {
        "sub": str(user.id_usuario),
        "roles": roles,
        "permissions": permissions,
        "username": user.nombre,
        "iat": datetime.now(timezone.utc).timestamp()
    }

    # =========================================================
    # 🔥 7. TOKENS
    # =========================================================
    access_token = create_access_token({
        **base_payload,
        "type": "access"
    })

    refresh_token = create_refresh_token({
        **base_payload,
        "type": "refresh"
    })

    # =========================================================
    # 📦 8. RESPONSE
    # =========================================================
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": user
    }