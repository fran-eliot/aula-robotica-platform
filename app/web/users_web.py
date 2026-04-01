# app/web/users_web.py

from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import UTC

from app.core.constants.audit_actions import AuditAction
from app.db.session import get_db
from app.modules.auth.auth_dependencies_web import get_current_user_web, require_permission_web
from app.modules.users import user_service
from app.modules.users.user_model import User
from app.core.templates import templates
from app.modules.audit.audit_service import log_action

router = APIRouter(prefix="/users", tags=["Users Web"])

@router.get("/")
def users_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user =  Depends(require_permission_web("users:read"))
):

    print("Cookie Token:", request.cookies.get("access_token"))
    users = user_service.get_all_users(db)

    return templates.TemplateResponse(
        "users/users_list.html",
        {
            "request": request,
            "users": users
        }
    )

@router.get("/create")
def users_create_form(
    request: Request,
    db: Session = Depends(get_db),
    current_user =  Depends(require_permission_web("users:create"))
):

    return templates.TemplateResponse(
        "users/users_create.html",
        {
            "request": request,
        }
    )

@router.post("/create")
def users_create(
    request: Request,
    nombre: str = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:create"))
):

    user_service.create_user_with_audit(db, nombre, current_user, request)

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.get("/{user_id}")
def user_detail(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:read"))
):

    user = user_service.get_user_or_404(db, user_id)

    return templates.TemplateResponse(
        "users/user_detail.html",
        {
            "request": request,
            "user": user
        }
    )

@router.get("/me", name="my_profile")
def my_profile(
    request: Request,
    current_user = Depends(get_current_user_web)
):
    return templates.TemplateResponse(
        "users/user_detail.html",
        {
            "request": request,
            "user": current_user
        }
    )

@router.post("/{user_id}/delete")
def delete_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:delete"))
):

    user = user_service.get_user_or_404(db, user_id)

    user_service.delete_user_with_audit(db, user, current_user, request)

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.post("/{user_id}/deactivate")
def deactivate_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):

    user = user_service.get_user_or_404(db, user_id)

    user_service.set_user_active_with_audit(db, user, False, current_user, request)

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.post("/{user_id}/activate")
def activate_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):

    user = user_service.get_user_or_404(db, user_id)

    user_service.set_user_active_with_audit(db, user, True, current_user, request)

    db.commit()

    return RedirectResponse("/users/", status_code=303)