# app/web/auth_web.py
# 🌐 Rutas web de autenticación

from fastapi import APIRouter, HTTPException, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.templates import templates
from app.core.presentation import settings
from app.core.constants.audit_actions import AuditAction
from app.core.security import validate_refresh_token

from app.modules.auth.auth_service import (
    authenticate_user,
    refresh_access_token
)
from app.modules.auth.auth_dependencies_web import get_current_user_web
from app.modules.audit.audit_service import log_action

router = APIRouter()


# =========================================================
# 🔐 LOGIN PAGE
# =========================================================
@router.get("/login")
def login_page(request: Request):
    """
    Renderiza formulario de login.
    """
    return templates.TemplateResponse(
        "auth/login.html",
        {"request": request}
    )


# =========================================================
# 🔐 LOGIN ACTION
# =========================================================
@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Procesa login:
    - Autentica usuario
    - Genera tokens
    - Registra auditoría
    - Setea cookies
    """

    try:
        result = authenticate_user(db, email, password)

    except HTTPException:
        return templates.TemplateResponse(
            "auth/login.html",
            {
                "request": request,
                "error": "Credenciales incorrectas"
            }
        )

    user = result["user"]

    # =========================================================
    # 🧾 AUDITORÍA
    # =========================================================
    log_action(
        db,
        action=AuditAction.LOGIN,
        user_id=user.id_usuario,
        resource_type="user",
        resource_id=user.id_usuario,
        description="Inicio de sesión",
        request=request
    )

    db.commit()

    # =========================================================
    # 🍪 RESPONSE + COOKIES
    # =========================================================
    response = RedirectResponse(
        url="/dashboard",
        status_code=303
    )

    cookie_config = {
        "httponly": True,
        "samesite": "lax" if settings.DEBUG else "strict",
        "secure": not settings.DEBUG,
        "path": "/"
    }

    # 🔥 access token
    response.set_cookie(
        key="access_token",
        value=result["access_token"],
        **cookie_config
    )

    # 🔥 refresh token
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        **cookie_config
    )

    return response


# =========================================================
# 🔄 REFRESH TOKEN
# =========================================================
@router.get("/refresh")
def refresh_token(request: Request):
    """
    Genera un nuevo access token a partir del refresh token.
    """

    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(
            status_code=401,
            detail="No refresh token"
        )

    try:
        # 🔐 validar token
        payload = validate_refresh_token(refresh_token)

        # 🔁 generar nuevo access
        new_access_token = refresh_access_token(payload)

        response = RedirectResponse("/dashboard")

        response.set_cookie(
            key="access_token",
            value=new_access_token,
            httponly=True,
            samesite="lax" if settings.DEBUG else "strict",
            secure=not settings.DEBUG,
            path="/"
        )

        return response

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Refresh token inválido"
        )


# =========================================================
# 🚪 LOGOUT
# =========================================================
@router.get("/logout")
def logout(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):
    """
    Cierra sesión:
    - Registra auditoría
    - Elimina cookies
    """

    # 🧾 auditoría
    log_action(
        db,
        action=AuditAction.LOGOUT,
        user_id=current_user.id_usuario,
        resource_type="user",
        resource_id=current_user.id_usuario,
        description="Cierre de sesión",
        request=request
    )

    db.commit()

    # 🍪 eliminar cookies
    response = RedirectResponse(
        url="/login",
        status_code=302
    )

    response.delete_cookie("access_token", path="/")
    response.delete_cookie("refresh_token", path="/")

    return response