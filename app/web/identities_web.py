from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.auth.auth_dependencies_web import require_admin_web
from app.modules.users.identity_model import Identity
from app.modules.users.user_model import User
from app.modules.users.role_model import Role
from app.core.security import hash_password
from app.core.templates import templates


router = APIRouter(prefix="/identities", tags=["Identities Web"])


@router.get("/")
def identities_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    identities = db.query(Identity).all()

    return templates.TemplateResponse(
        "identities/identities_list.html",
        {
            "request": request,
            "identities": identities
        }
    )


@router.get("/create")
def identities_create_form(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    users = db.query(User).all()
    roles = db.query(Role).all()

    return templates.TemplateResponse(
        "identities/identities_create.html",
        {
            "request": request,
            "users": users,
            "roles": roles
        }
    )


@router.post("/create")
def identities_create(
    email: str = Form(...),
    password: str = Form(...),
    user_id: int = Form(...),
    rol_id: int | None = Form(None),
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    existing = db.query(Identity).filter(
        Identity.email == email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    # -------------------------
    # Rol por defecto: estudiante
    # -------------------------

    if not rol_id:

        default_role = db.query(Role).filter(
            Role.nombre == "estudiante"
        ).first()

        if not default_role:
            raise HTTPException(
                status_code=500,
                detail="Rol 'estudiante' no existe en la base de datos"
            )

        rol_id = default_role.id_rol

    # -------------------------

    identity = Identity(
        email=email,
        password_hash=hash_password(password),
        user_id=user_id,
        rol_id=rol_id,
        provider="local"
    )

    db.add(identity)
    db.commit()

    return RedirectResponse("/identities/", status_code=303)

@router.get("/edit/{identity_id}")
def edit_identity_form(
    request: Request,
    identity_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    identity = db.query(Identity).filter(
        Identity.id_identidad == identity_id
    ).first()

    if not identity:
        raise HTTPException(status_code=404, detail="Identidad no encontrada")

    users = db.query(User).all()
    roles = db.query(Role).all()

    return templates.TemplateResponse(
        "identities/identities_edit.html",
        {
            "request": request,
            "identity": identity,
            "users": users,
            "roles": roles
        }
    )

@router.post("/edit/{identity_id}")
def edit_identity(
    identity_id: int,
    email: str = Form(...),
    user_id: int = Form(...),
    rol_id: int = Form(...),
    password: str = Form(None),
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    identity = db.query(Identity).filter(
        Identity.id_identidad == identity_id
    ).first()

    if not identity:
        raise HTTPException(status_code=404, detail="Identidad no encontrada")

    identity.email = email
    identity.user_id = user_id
    identity.rol_id = rol_id

    if password:
        identity.password_hash = hash_password(password)

    db.commit()

    return RedirectResponse("/identities/", status_code=303)


@router.get("/delete/{identity_id}")
def delete_identity(
    identity_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_web)
):

    identity = db.query(Identity).filter(
        Identity.id_identidad == identity_id
    ).first()

    if not identity:
        raise HTTPException(status_code=404, detail="Identidad no encontrada")

    db.delete(identity)
    db.commit()

    return RedirectResponse("/identities/", status_code=303)