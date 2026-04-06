# app/core/authorization/policies.py

def can_user_action(action: str, user_payload: dict, target=None) -> bool:
    """
    Motor central de autorización.
    """

    roles = user_payload.get("roles", [])
    permissions = user_payload.get("permissions", [])
    user_id = int(user_payload.get("sub") or 0)

    # 🔥 Admin override
    if "admin" in roles:
        return True

    # 🔥 Ownership
    if target and hasattr(target, "id_usuario"):
        if target.id_usuario == user_id:
            if action in ["view", "edit"]:
                return True

    # 🔥 Permisos
    action_map = {
        "view": "users:read",
        "edit": "users:update",
        "delete": "users:delete",
        "create": "users:create"
    }

    required_perm = action_map.get(action)

    if required_perm and required_perm in permissions:
        return True

    return False