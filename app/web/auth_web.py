from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.auth_service import authenticate_user
from app.core.security import create_access_token
from app.core.templates import templates

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

    response = RedirectResponse(
        url="/dashboard",
        status_code=302
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    return response

@router.get("/logout")
def logout():

    response = RedirectResponse(
        url="/login",
        status_code=302
    )

    response.delete_cookie("access_token")

    return response