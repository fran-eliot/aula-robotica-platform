from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Union, List

from app.db.session import get_db
from app.models.user import User
from app.core.security import decode_access_token

# Jerarquía de roles para validación

ROLE_HIERARCHY = {
    "administrador": 3,
    "organizador": 2,
    "participante": 1
}

# OAuth2 scheme para extraer token de Authorization header

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# ===== API =====

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    print("TOKEN RECIBIDO:", token)
    payload = decode_access_token(token)
    print("PAYLOAD:", payload)

    user_id = int(payload.get("sub"))
    print("USER_ID:", user_id)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    user = db.query(User).filter(User.id_usuario == user_id).first()
    print("USER DB:", user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return user


def require_roles(required_roles: Union[str, List[str]]):
    """
    Dependency para validar autorización basada en roles.
    Soporta:
        - Un solo rol: "administrador"
        - Varios roles: ["administrador", "organizador"]
    Aplica jerarquía de roles.
    """

    if isinstance(required_roles, str):
        required_roles = [required_roles]

    def role_checker(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
    ):
        # Decodificar token
        payload = decode_access_token(token)

        user_id = payload.get("sub")
        roles = payload.get("roles", [])

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        if not roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario sin roles asignados"
            )

        # Nivel máximo del usuario
        user_max_level = max(
            ROLE_HIERARCHY.get(role, 0) for role in roles
        )

        # Nivel mínimo requerido
        required_min_level = max(
            ROLE_HIERARCHY.get(role, 0) for role in required_roles
        )

        # Comparación jerárquica
        if user_max_level < required_min_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos suficientes"
            )

        # Recuperar usuario desde BD
        user = db.query(User).filter(
            User.id_usuario == int(user_id)
        ).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario no encontrado"
            )

        return user

    return role_checker

# ===== Web =====

def get_current_user_from_cookie(
    request: Request,
    db: Session = Depends(get_db)
):

    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autenticado"
        )

    payload = decode_access_token(token)

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    user = db.query(User).filter(
        User.id_usuario == int(user_id)
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return user