from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime, UTC

from app.core.constants.audit_actions import AuditAction
from app.db.session import get_db
from app.api.deps import get_current_user_web, require_admin_web
from app.models.user import User
from app.core.templates import templates
from app.services.audit_service import log_action

router = APIRouter(prefix="/users", tags=["Users Web"])

@router.get("/")
def users_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user =  Depends(require_admin_web)
):

    print("Cookie Token:", request.cookies.get("access_token"))
    users = db.query(User).all()

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
    current_user =  Depends(require_admin_web)
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
    current_user = Depends(require_admin_web)
):

    new_user = User(
        nombre=nombre,
        activo=True,
        fecha_creacion=datetime.now(UTC)
    )

    db.add(new_user)
    db.flush()

    log_action(
        db,
        action=AuditAction.CREATE_USER,
        user_id=current_user.id_usuario,
        resource_type="user",
        resource_id=new_user.id_usuario,
        description=f"Creó usuario {new_user.nombre}",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.get("/{user_id}")
def user_detail(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return templates.TemplateResponse(
        "users/user_detail.html",
        {
            "request": request,
            "user": user
        }
    )

@router.get("/delete/{user_id}")
def delete_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user =Depends(require_admin_web)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user_id = user.id_usuario
    user_name = user.nombre

    db.delete(user)
    db.flush()

    log_action(
        db,
        action=AuditAction.DELETE_USER,
        user_id=user_id,
        resource_type="user",
        resource_id=user_id,
        description=f"Eliminó usuario {user_name}",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.get("/deactivate/{user_id}")
def deactivate_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404)

    user.activo = False

    log_action(
        db,
        action=AuditAction.DEACTIVATE_USER,
        user_id=current_user.id_usuario,
        resource_type="user",
        resource_id=user.id_usuario,
        description=f"Desactivó usuario {user.nombre}",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    return RedirectResponse("/users/", status_code=303)

@router.get("/activate/{user_id}")
def activate_user(
    request:Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404)

    user.activo = True

    log_action(
        db,
        action=AuditAction.ACTIVATE_USER,
        user_id=current_user.id_usuario,
        resource_type="user",
        resource_id=user.id_usuario,
        description=f"Activó usuario {user.nombre}",
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    db.commit()

    return RedirectResponse("/users/", status_code=303)