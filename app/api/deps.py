from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.authorization.roles import has_required_role
from app.db.session import get_db
from app.models.user import User
from app.core.security import decode_access_token

# Jerarquía de roles para validación

ROLE_HIERARCHY = {
    "admin": 3,
    "profesor": 2,
    "estudiante": 1
}

# OAuth2 scheme para extraer token de Authorization header

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# ===== API =====

def get_current_user_api(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    user_id = payload.get("sub")
    roles = payload.get("roles", [])

    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = db.query(User).filter(User.id_usuario == int(user_id)).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    # 🔥 añadir roles desde JWT
    user.roles_token = roles

    return user

def require_roles_api(*allowed_roles: str):

    def role_checker(current_user: User = Depends(get_current_user_api)):

        if not has_required_role(current_user.roles_token, list(allowed_roles)):
            raise HTTPException(status_code=403, detail="No autorizado")

        return current_user

    return role_checker

# ===== Web =====

def get_current_user_web(
    request: Request,
    db: Session = Depends(get_db)
):
    print("👉 HEADERS:", request.headers)
    print("👉 COOKIES:", request.cookies)
    
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="No autenticado")

    payload = decode_access_token(token)

    user_id = payload.get("sub")
    roles = payload.get("roles", [])

    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = db.query(User).filter(User.id_usuario == int(user_id)).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    # 🔥 clave
    user.roles_token = roles

    return user

def require_roles_web(*allowed_roles: str):

    def role_checker(
        request: Request,
        current_user: User = Depends(get_current_user_web)
    ):
        token = request.cookies.get("access_token")

        if not token:
            raise HTTPException(status_code=401, detail="No autenticado")

        payload = decode_access_token(token)

        roles = payload.get("roles", [])

        print("👉 ROLES TOKEN:", roles)
        print("👉 ROLES REQUERIDOS:", allowed_roles)

        if not any(role in allowed_roles for role in roles):
            raise HTTPException(status_code=403, detail="No autorizado")

        return current_user

    return role_checker

# API
require_admin_api = require_roles_api("admin")
require_profesor_api = require_roles_api("profesor")
require_estudiante_api = require_roles_api("estudiante")

# WEB
require_admin_web = require_roles_web("admin")
require_profesor_web = require_roles_web("profesor")