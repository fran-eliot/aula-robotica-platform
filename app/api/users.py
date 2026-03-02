from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.api.deps import get_current_user, require_roles


router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    user = Depends(require_roles("administrador"))
):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_roles("administrador"))
):
    usuario = db.query(User).filter(User.id_usuario == user_id).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario

@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user = Depends(get_current_user)):
    return current_user

@router.post("/", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    user = Depends(require_roles("administrador"))
):
    nuevo = User(
        nombre=data.nombre,
        activo=True
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_roles("administrador"))
):
    usuario = db.query(User).filter(User.id_usuario == user_id).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    db.delete(usuario)
    db.commit()

    return {"message": "Usuario eliminado correctamente"}