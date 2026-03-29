# app/services/auth_service.py

from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.modules.users.identity_model import Identity
from app.modules.users.user_model import User
from app.core.security import validate_refresh_token, verify_password, create_access_token
from app.core.constants.audit_actions import AuditAction

def refresh_access_token(refresh_token: str) -> dict:
    payload = validate_refresh_token(refresh_token)

    if payload.get("type") != "refresh":
        raise Exception("Refresh token inválido")

    return {
        "access_token": create_access_token({
            "sub": payload.get("sub"),
            "roles": payload.get("roles", []),
            "permissions": payload.get("permissions", []),
            "username": payload.get("username")
        })
    }


def authenticate_user(db: Session, email: str, password: str):

    identity = db.query(Identity).filter(
        Identity.email == email
    ).first()

    if not identity:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

    if not identity.password_hash:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login no permitido para este proveedor"
        )

    if not verify_password(password, identity.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

    user = identity.usuario

    if not user.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario desactivado"
        )

    # Resolver roles efectivos
    if identity.rol:
        roles = [identity.rol.nombre]
    else:
        roles = [role.nombre for role in user.roles]

    access_token = create_access_token(
        data={
            "sub": str(user.id_usuario),
            "roles": roles,
            "username": user.nombre,
            "iat": datetime.utcnow(),
            "type": "access"
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user":user,
        "roles":roles
    }