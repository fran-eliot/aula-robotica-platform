from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.constants.audit_actions import AuditAction
from app.db.session import get_db
from app.api.deps import get_current_user_web
from app.services.auth_service import authenticate_user
from app.core.templates import templates
from app.services.audit_service import log_action

router = APIRouter()

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        "auth/login.html",
        {"request": request}
    )

@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    result = authenticate_user(db, email, password)

    if not result:
        return templates.TemplateResponse(
            "auth/login.html",
            {
                "request": request,
                "error": "Credenciales incorrectas"
            }
        )
    
    token = result["access_token"]

    user = result["user"]

    log_action(
        db,
        action=AuditAction.LOGIN,
        user_id=user.id_usuario,
        resource_type="user",
        resource_id=user.id_usuario,
        description="Inicio de sesión",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    response = RedirectResponse(
        url="/dashboard/",
        status_code=303
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=False,
        path="/"
    )

    return response

@router.get("/logout")
def logout(request: Request,
           db:Session = Depends(get_db),
           current_user = Depends(get_current_user_web)):

    log_action(
        db,
        action=AuditAction.LOGOUT,
        user_id=current_user.id_usuario,
        resource_type="user",
        resource_id=current_user.id_usuario,
        description="Cierre de sesión",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    response = RedirectResponse(
        url="/login",
        status_code=302
    )

    response.delete_cookie("access_token")
    
    return response