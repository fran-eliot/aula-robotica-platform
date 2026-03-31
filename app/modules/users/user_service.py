# app/modules/users/user_service.py

from sqlalchemy.orm import Session

from app.modules.users.identity_model import Identity
from app.modules.users.user_model import User


def get_user_roles(db: Session, user_id: int) -> list[str]:
    """
    Devuelve la lista de roles asociados a un usuario.
    """

    identity = db.query(Identity).filter(
        Identity.user_id == user_id
    ).first()

    if identity and identity.rol:
        return [identity.rol.nombre]

    return []

def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(
        User.id_usuario == user_id
    ).first()


def create_user(db: Session, nombre: str):
    user = User(
        nombre=nombre,
        activo=True
    )

    db.add(user)
    db.flush()

    return user


def delete_user(db: Session, user: User):
    db.delete(user)


def set_user_active(db: Session, user: User, active: bool):
    user.activo = active