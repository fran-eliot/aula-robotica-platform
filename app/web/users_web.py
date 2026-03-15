from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.api.deps import get_current_user_from_cookie
from app.models.user import User
from app.models.identity import Identity
from app.core.templates import templates
from app.services.audit_service import log_action

router = APIRouter(prefix="/users", tags=["Users Web"])

@router.get("/")
def users_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
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
    current_user = Depends(get_current_user_from_cookie)
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
    current_user = Depends(get_current_user_from_cookie)
):

    new_user = User(
        nombre=nombre,
        activo=True,
        fecha_creacion=datetime.utcnow()
    )

    db.add(new_user)
    db.commit()

    log_action(
        db,
        action="create_user",
        user_id=current_user.id_usuario,
        description=f"Creó usuario {new_user.nombre}"
    )

    return RedirectResponse("/users/", status_code=303)

@router.get("/{user_id}")
def user_detail(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
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
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()

    log_action(
        db,
        action="delete_user",
        user_id=current_user.id_usuario,
        description=f"Eliminó usuario {user.nombre}"
    )

    return RedirectResponse("/users/", status_code=303)

@router.get("/deactivate/{user_id}")
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404)

    user.activo = False
    db.commit()

    log_action(
        db,
        action="deactivate_user",
        user_id=current_user.id_usuario,
        description=f"Desactivó usuario {user.nombre}"
    )

    return RedirectResponse("/users/", status_code=303)

@router.get("/activate/{user_id}")
def activate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
):

    user = db.query(User).filter(
        User.id_usuario == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404)

    user.activo = True
    db.commit()

    return RedirectResponse("/users/", status_code=303)