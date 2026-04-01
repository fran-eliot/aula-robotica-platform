# app/core/deps/web_auth.py

from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.core.authorization.permissions import has_permission
from app.db.session import get_db
from app.modules.users.user_model import User
from app.core.authorization.roles import has_required_role
from app.modules.users.user_service import can_access_user, get_user_or_404


def get_current_user_web(
    request: Request,
    db: Session = Depends(get_db)
):
    payload = getattr(request.state, "user", None)

    if not payload:
        raise HTTPException(status_code=401)

    user_id = payload.get("sub")
    roles = payload.get("roles", [])
    permissions = payload.get("permissions", [])

    user = db.query(User).filter(User.id_usuario == int(user_id)).first()

    if not user:
        raise HTTPException(status_code=401)

    user.roles_token = roles
    user.permissions = permissions
    return user


def require_roles_web(*allowed_roles: str):

    def role_checker(current_user: User = Depends(get_current_user_web)):

        print("ROLES USER:", current_user.roles_token)
        print("ROLES REQUERIDOS:", allowed_roles)

        if not has_required_role(current_user.roles_token, list(allowed_roles)):
            raise HTTPException(status_code=403)

        return current_user
    
    return role_checker


def require_permission_web(*required_permissions: str):

    def permission_checker(current_user = Depends(get_current_user_web)):

        user_permissions = getattr(current_user, "permissions", [])

        print("PERMISOS USER:", user_permissions)
        print("PERMISOS REQUERIDOS:", required_permissions)

        if not has_permission(user_permissions, list(required_permissions)):
            raise HTTPException(status_code=403)

        return current_user

    return permission_checker


def require_owner_or_permission_web(permission: str):

    def checker(
        user_id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user_web)
    ):
        user = get_user_or_404(db, user_id)

        if not can_access_user(current_user, user, [permission]):
            raise HTTPException(status_code=403, detail="No autorizado")

        return user
    
    return checker

def require_permission_and_not_self_web(permission: str):

    def checker(
        user_id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user_web)
    ):
        user = get_user_or_404(db, user_id)

        if current_user.id_usuario == user.id_usuario:
            raise HTTPException(status_code=400, detail="No puedes eliminarte a ti mismo")

        if not has_permission(current_user.permissions, [permission]):
            raise HTTPException(status_code=403, detail="No autorizado")

        return user

    return checker

# shortcuts
require_admin_web = require_roles_web("admin")
require_profesor_web = require_roles_web("profesor")