# app/core/authorization/policies.py
# Politicas de autorización personalizadas

def can_user_action(action, resource, user_payload, target_user=None):
    """
    Compatible con:
    - dict JWT
    - User SQLAlchemy
    - roles como strings
    - roles como objetos Role
    """

    roles = []
    permissions = []
    user_id = None

    # ==================================================
    # JWT payload (dict)
    # ==================================================
    if isinstance(user_payload, dict):
        roles = [str(r).lower() for r in user_payload.get("roles", [])]
        permissions = user_payload.get("permissions", [])
        user_id = int(user_payload.get("sub"))

    else:
        # ==================================================
        # SQLAlchemy User
        # ==================================================
        user_id = getattr(user_payload, "id_usuario", None)

        raw_roles = (
            getattr(user_payload, "roles_token", None)
            or getattr(user_payload, "roles", [])
        )

        roles = [
            r.lower() if isinstance(r, str)
            else r.nombre.lower()
            for r in raw_roles
        ]

        permissions = getattr(user_payload, "permissions", [])

    # ==================================================
    # PERMISSION CHECK
    # ==================================================
    permission_name = f"{resource}:{action}"

    if permission_name in permissions:
        return True

    if "admin" in roles:
        return True

    # ==================================================
    # OWNER RULES
    # ==================================================
    target_id = getattr(target_user, "id_usuario", None)

    if action in ["read", "update"] and user_id == target_id:
        return True

    return False