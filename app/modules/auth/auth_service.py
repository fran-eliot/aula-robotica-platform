# app/services/auth_service.py

import datetime

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.authorization.permissions import get_permissions_from_roles
from app.core.authorization.role_permissions import ROLE_PERMISSIONS
from app.modules.users.identity_model import Identity
from app.core.security import create_refresh_token, verify_password, create_access_token


def refresh_access_token(payload: dict) -> str:

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Refresh token inválido")

    return create_access_token({
        "sub": payload.get("sub"),
        "roles": payload.get("roles", []),
        "permissions": payload.get("permissions", []),
        "username": payload.get("username"),
        "type": "access"
    })


def authenticate_user(db: Session, email: str, password: str):

    identity = db.query(Identity).filter(
        Identity.email == email
    ).first()

    if not identity:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    if not identity.password_hash:
        raise HTTPException(status_code=401, detail="Login no permitido para este proveedor")

    if not verify_password(password, identity.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    user = identity.usuario

    if not user.activo:
        raise HTTPException(status_code=403, detail="Usuario desactivado")

    # 🔥 roles efectivos
    roles = (
        [identity.rol.nombre]
        if identity.rol
        else [role.nombre for role in user.roles]
    )
    roles = [r.lower() for r in roles]

    # 🔥 permisos
    permissions = get_permissions_from_roles(roles)

    # 🔥 tokens
    access_token = create_access_token({
        "sub": str(user.id_usuario),
        "roles": roles,
        "permissions": permissions,
        "username": user.nombre,
        "type": "access",
        "iat": datetime.utcnow().timestamp()
    })

    refresh_token = create_refresh_token({
        "sub": str(user.id_usuario),
        "roles": roles,
        "permissions": permissions,
        "username": user.nombre,
        "type": "refresh",
        "iat": datetime.utcnow().timestamp()
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": user
    }

