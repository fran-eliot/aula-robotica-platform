from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user_from_cookie
from app.services.user_service import get_user_roles


def require_roles(*allowed_roles: str):

    def role_checker(
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user_from_cookie)
    ):

        user_roles = get_user_roles(db, current_user.id_usuario)

        if not any(role in user_roles for role in allowed_roles):
            raise HTTPException(status_code=403, detail="No autorizado")

        return current_user

    return role_checker


require_admin = require_roles("administrador")
require_profesor = require_roles("profesor")
require_estudiante = require_roles("estudiante")