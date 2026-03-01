from fastapi import APIRouter, Depends
from app.api.deps import get_current_user, require_role
from app.models.user import User

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "Users endpoint working"}

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id_usuario,
        "nombre": current_user.nombre
    }


@router.get("/admin-only")
def admin_only(
    _: None = Depends(require_role("administrador"))
):
    return {"message": "Solo administradores pueden ver esto"}