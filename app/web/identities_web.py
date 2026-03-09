from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user_from_cookie
from app.models.identity import Identity
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password
from app.core.templates import templates


router = APIRouter(prefix="/identities", tags=["Identities Web"])


@router.get("/")
def identities_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
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
    current_user = Depends(get_current_user_from_cookie)
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
    rol_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
):

    existing = db.query(Identity).filter(
        Identity.email == email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")

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
    current_user = Depends(get_current_user_from_cookie)
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
    current_user = Depends(get_current_user_from_cookie)
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
    current_user = Depends(get_current_user_from_cookie)
):

    identity = db.query(Identity).filter(
        Identity.id_identidad == identity_id
    ).first()

    if not identity:
        raise HTTPException(status_code=404, detail="Identidad no encontrada")

    db.delete(identity)
    db.commit()

    return RedirectResponse("/identities/", status_code=303)