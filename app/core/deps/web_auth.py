from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.core.security import validate_access_token
from app.core.authorization.roles import has_required_role


def get_current_user_web(
    request: Request,
    db: Session = Depends(get_db)
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401)

    payload = getattr(request.state, "user", None)

    if not payload:
        payload = validate_access_token(token)

    user_id = payload.get("sub")
    roles = payload.get("roles", [])

    user = db.query(User).filter(User.id_usuario == int(user_id)).first()

    if not user:
        raise HTTPException(status_code=401)

    user.roles_token = roles
    return user


def require_roles_web(*allowed_roles: str):

    def role_checker(current_user: User = Depends(get_current_user_web)):

        print("ROLES USER:", current_user.roles_token)
        print("ROLES REQUERIDOS:", allowed_roles)

        if not has_required_role(current_user.roles_token, list(allowed_roles)):
            raise HTTPException(status_code=403)

        return current_user
    
    return role_checker


# shortcuts
require_admin_web = require_roles_web("admin")
require_profesor_web = require_roles_web("profesor")