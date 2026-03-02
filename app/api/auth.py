from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.auth_service import authenticate_user
from app.schemas.auth import LoginRequest

router = APIRouter()

@router.post("/login",
             summary="Iniciar sesión, autenticación de usuario",
             description="Autentica una identidad y devuelve un token JWT válido para acceder a los endpoints protegidos.",
             responses={
                 200: {"description": "Inicio de sesión exitoso, devuelve token JWT"},
                 401: {"description": "Credenciales inválidas o usuario desactivado"}
             })
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return authenticate_user(db, data.email, data.password)