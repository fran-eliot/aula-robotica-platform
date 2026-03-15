from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user_from_cookie
from app.models.role import Role
from app.core.templates import templates
from app.services.user_service import get_user_roles
from app.core.authorization import require_admin


router = APIRouter(prefix="/roles", tags=["Roles Web"])


@router.get("/")
def roles_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
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
    current_user=Depends(require_admin)
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
    current_user=Depends(require_admin)
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
    current_user=Depends(require_admin)
):
    
    role = db.query(Role).filter(
        Role.id_rol == role_id
    ).first()

    if not role:
        raise HTTPException(status_code=404)

    db.delete(role)
    db.commit()

    return RedirectResponse("/roles/", status_code=303)