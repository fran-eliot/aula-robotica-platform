# app/web/context.py

from fastapi import Request

from app.core.authorization.permissions import has_permission_from_roles
from app.core.security import decode_token, validate_access_token
from app.core.authorization.roles import has_required_role
from app.modules.users.user_service import get_user_roles

# 🔥 contexto seguro siempre disponible
def get_fallback_context():
    return {
        "current_user_id": None,
        "current_username": None,
        "current_user_roles": [],
        "has_role": lambda *args: False,
        "has_perm": lambda *args: False
    }

def get_template_context(request: Request):
    """
    Contexto global disponible en todas las plantillas Jinja.
    """

    fallback_context = get_fallback_context()

    try:
        # 🔥 1. Intentar usar payload del middleware
        payload = getattr(request.state, "user", None)

        if not payload:
            return get_fallback_context()

        # 🔥 2. Extraer datos
        roles = [r.lower() for r in payload.get("roles", [])]
        user_id = int(payload.get("sub"))
        username = payload.get("username", "Usuario")

        # 🔥 Helpers reutilizando core
        def has_role(*allowed_roles: str):
            return has_required_role(roles, list(allowed_roles))

        def has_perm(*required_permissions: str):
            return has_permission_from_roles(roles, list(required_permissions))

        return {
            "current_user_id": user_id,
            "current_username": username,
            "current_user_roles": roles,
            "has_role": has_role,
            "has_perm": has_perm
        }

    except Exception as e:
        print("🔥 ERROR CONTEXT:", e)
        return fallback_context