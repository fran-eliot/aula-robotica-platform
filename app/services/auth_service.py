# app/services/auth_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.identity import Identity
from app.models.user import User
from app.core.security import verify_password, create_access_token


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
            "roles": roles
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }