# tests/test_audit_ui.py
# Este archivo contiene pruebas para las funciones de utilidad relacionadas con la interfaz de auditoría. Se verifica que las funciones `get_audit_icon` y `get_audit_color` devuelvan los valores correctos para acciones conocidas como "create", "update", "delete", "login" y "logout". También se comprueba que para acciones desconocidas, se devuelvan los valores por defecto ("fa-info-circle" para el icono y "bg-primary" para el color).

from app.core.utils.audit_ui import get_audit_icon, get_audit_color


def test_get_audit_icon_returns_string():
    assert isinstance(get_audit_icon("create"), str)
    assert isinstance(get_audit_icon("update"), str)
    assert isinstance(get_audit_icon("delete"), str)


def test_get_audit_icon_unknown_action():
    assert get_audit_icon("random") == "fa-info-circle"


def test_get_audit_color_returns_string():
    assert isinstance(get_audit_color("create"), str)
    assert isinstance(get_audit_color("update"), str)
    assert isinstance(get_audit_color("delete"), str)


def test_get_audit_color_unknown_action():
    assert get_audit_color("random") == "bg-primary"


def test_get_audit_icon_real_values():
    assert get_audit_icon("CREATE_USER") == "fa-user-plus"
    assert get_audit_icon("DELETE_USER") == "fa-user-times"
    assert get_audit_icon("ACTIVATE_USER") == "fa-check"
    assert get_audit_icon("DEACTIVATE_USER") == "fa-ban"
    assert get_audit_icon("LOGIN") == "fa-sign-in-alt"
    assert get_audit_icon("LOGOUT") == "fa-sign-out-alt"


def test_get_audit_icon_default():
    assert get_audit_icon("OTHER") == "fa-info-circle"


def test_get_audit_color_branches():
    assert get_audit_color("DELETE_USER") == "bg-danger"
    assert get_audit_color("CREATE_USER") == "bg-success"
    assert get_audit_color("ACTIVATE_USER") == "bg-success"
    assert get_audit_color("DEACTIVATE_USER") == "bg-warning"
    assert get_audit_color("OTHER") == "bg-primary"