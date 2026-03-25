from fastapi import Request

from app.core.authorization.permissions import has_permission_from_roles
from app.core.security import decode_access_token
from app.core.authorization.roles import has_required_role
from app.db.session import SessionLocal
from app.models.user import User
from app.services.user_service import get_user_roles


def get_template_context(request: Request):
    """
    Contexto global disponible en todas las plantillas Jinja.
    Añade automáticamente:
    - Usuario autenticado
    - Roles
    - Helper has_role()
    """

    token = request.cookies.get("access_token")

    if not token:
        return {}

    try:
        payload = decode_access_token(token)
        user_id = int(payload.get("sub"))

        with SessionLocal() as db:
            user = db.query(User).filter(
                User.id_usuario == user_id
            ).first()

            roles = get_user_roles(db, user_id)

        # 🔥 Helper reutilizando lógica central
        def has_role(*allowed_roles: str):
            return has_required_role(roles, list(allowed_roles))
        
        def has_perm(*required_permissions: str):
            return has_permission_from_roles(roles, list(required_permissions))

        return {
            "current_user": user,
            "current_user_roles": roles,  # opcional (se puede eliminar)
            "has_role": has_role,
            "has_perm": has_perm
        }

    except Exception:
        return {}