from fastapi import Request
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db.session import SessionLocal
from app.models.user import User
from app.services.user_service import get_user_roles


def get_template_context(request: Request):
    """
    Contexto global disponible en todas las plantillas Jinja.
    Añade automáticamente el usuario autenticado y sus roles.
    """

    token = request.cookies.get("access_token")

    if not token:
        return {}

    try:
        payload = decode_access_token(token)
        user_id = int(payload.get("sub"))

        db: Session = SessionLocal()

        user = db.query(User).filter(
            User.id_usuario == user_id
        ).first()

        roles = get_user_roles(db, user_id)

        db.close()

        return {
            "current_user": user,
            "current_user_roles": roles
        }

    except Exception:
        return {}