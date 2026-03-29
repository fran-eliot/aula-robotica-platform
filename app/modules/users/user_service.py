from sqlalchemy.orm import Session

from app.modules.users.identity_model import Identity


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