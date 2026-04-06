from fastapi import Request


def add_flash(request: Request, message: str, category: str = "success"):
    """
    Añade mensaje flash a la sesión (cookies temporales).
    """
    if not hasattr(request.state, "flash"):
        request.state.flash = []

    request.state.flash.append({
        "message": message,
        "category": category
    })


def get_flash(request: Request):
    return getattr(request.state, "flash", [])


def flash_success(request, msg):
    add_flash(request, msg, "success")
    

def flash_error(request, msg):
    add_flash(request, msg, "danger")