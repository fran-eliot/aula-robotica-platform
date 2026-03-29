from fastapi import APIRouter, HTTPException, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.authorization.role_permissions import ROLE_PERMISSIONS
from app.core.config import settings
from app.core.constants.audit_actions import AuditAction
from app.core.security import create_access_token, create_refresh_token, validate_refresh_token
from app.db.session import get_db
from app.modules.auth.auth_dependencies_web import get_current_user_web
from app.modules.auth.auth_service import authenticate_user
from app.core.templates import templates
from app.modules.audit.audit_service import log_action

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
    
    user = result["user"]

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

    response = RedirectResponse(
        url="/dashboard",
        status_code=303
    )

    roles = result.get("roles", [])

    permissions = []

    for role in roles:
        permissions.extend(ROLE_PERMISSIONS.get(role, []))

    access_token = create_access_token({
        "sub": str(user.id_usuario),
        "roles": roles,
        "permissions": permissions,
        "username": user.nombre
    })

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax" if settings.DEBUG else "strict",
        secure = settings.ENV == "prod",
        path="/"
    )

    # 🔥 crear refresh token
    refresh_token = create_refresh_token({
        "sub": str(user.id_usuario),
        "roles": roles,
        "permissions": permissions,
        "username": user.nombre
    })

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="lax" if settings.DEBUG else "strict",
        secure = settings.ENV == "prod",
        path="/"
    )

    return response

@router.get("/refresh")
def refresh_token(request: Request):

    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token")

    payload = validate_refresh_token(refresh_token)

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Token inválido")

    user_id = payload.get("sub")
    roles = payload.get("roles", [])
    username = payload.get("username")
    permissions = payload.get("permissions",[])

    new_access_token = create_access_token({
        "sub": user_id,
        "roles": roles,
        "username":username,
        "permissions":permissions
    })

    response = RedirectResponse("/dashboard")

    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        samesite="lax" if settings.DEBUG else "strict",
        secure = settings.ENV == "prod",
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
        request=request
    )

    db.commit()

    response = RedirectResponse(
        url="/login",
        status_code=302
    )

    response.delete_cookie("access_token", path="/")
    response.delete_cookie("refresh_token", path="/")
    
    return response