# app/modules/users/user_service.py

from datetime import datetime,UTC

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.authorization.permissions import has_permission
from app.core.constants.audit_actions import AuditAction
from app.modules.audit.audit_service import audit_user_action
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


def is_owner(current_user, target_user) -> bool:
    return current_user.id_usuario == target_user.id_usuario


def can_access_user(current_user, target_user, required_permissions: list[str]) -> bool:
    # 👤 dueño
    if is_owner(current_user, target_user):
        return True

    # 🔐 permisos
    return has_permission(current_user.roles_token, required_permissions)


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(
        User.id_usuario == user_id
    ).first()


def create_user_with_audit(db, nombre, current_user:None, request:None):
    user = User(nombre=nombre, 
                activo=True,
                fecha_creacion=datetime.now(datetime.UTC))

    db.add(user)
    db.flush()

    if current_user and request:
        audit_user_action(
            db, 
            AuditAction.CREATE_USER,
            current_user,
            user,
            request,
            f"Creó usuario {user.nombre}"
        )

    return user


def delete_user_with_audit(db, user, current_user: None, request: None):
    user_id = user.id_usuario
    user_name = user.nombre

    db.delete(user)

    if current_user and request:
        audit_user_action(
            db,     
            AuditAction.DELETE_USER,
            current_user,
            user,
            request,
            f"Eliminó usuario {user_name}"
        )


def set_user_active_with_audit(db, user, active, current_user: None, request: None):
    user.activo = active

    if current_user and request:
        action = AuditAction.ACTIVATE_USER if active else AuditAction.DEACTIVATE_USER
        description = f"{'Activó' if active else 'Desactivó'} usuario {user.nombre}"

        audit_user_action(
            db,
            action,
            current_user,
            user,
            request,
            description
        )


def get_user_or_404(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user