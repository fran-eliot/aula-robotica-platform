from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.auth.auth_dependencies_web import require_admin_web
from app.modules.users.role_model import Role
from app.core.templates import templates


router = APIRouter(prefix="/roles", tags=["Roles Web"])


@router.get("/")
def roles_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin_web)
):
       
    roles = db.query(Role).all()

    return templates.TemplateResponse(
        "roles/roles_list.html",
        {
            "request": request,
            "roles": roles
        }
    )


@router.get("/create")
def roles_create_form(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin_web)
):
    
    return templates.TemplateResponse(
        "roles/roles_create.html",
        {
            "request": request
        }
    )


@router.post("/create")
def roles_create(
    nombre: str = Form(...),
    descripcion: str = Form(None),
    db: Session = Depends(get_db),
    current_user=Depends(require_admin_web)
):
    
    role = Role(
        nombre=nombre,
        descripcion=descripcion
    )

    db.add(role)
    db.commit()

    return RedirectResponse("/roles/", status_code=303)


@router.get("/delete/{role_id}")
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin_web)
):
    
    role = db.query(Role).filter(
        Role.id_rol == role_id
    ).first()

    if not role:
        raise HTTPException(status_code=404)

    db.delete(role)
    db.commit()

    return RedirectResponse("/roles/", status_code=303)