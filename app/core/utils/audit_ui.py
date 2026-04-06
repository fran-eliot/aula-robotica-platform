# app/core/utils/audit_ui.py
# Utilidades para la interfaz de auditoría (iconos, etiquetas, etc.)

def get_audit_icon(action: str) -> str:

    mapping = {
        "CREATE_USER": "fa-user-plus",
        "DELETE_USER": "fa-user-times",
        "ACTIVATE_USER": "fa-check",
        "DEACTIVATE_USER": "fa-ban",
        "LOGIN": "fa-sign-in-alt",
        "LOGOUT": "fa-sign-out-alt"
    }

    return mapping.get(action, "fa-info-circle")


def get_audit_color(action: str) -> str:
    if "DELETE" in action:
        return "bg-danger"
    if "CREATE" in action:
        return "bg-success"
    if "ACTIVATE" in action:
        return "bg-success"
    if "DEACTIVATE" in action:
        return "bg-warning"
    return "bg-primary"