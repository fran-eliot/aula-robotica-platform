# app/modules/auth/auth_dependencies_web.py
# 🔐 Dependencias de autenticación y autorización (WEB)

from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.users.user_model import User
from app.modules.users.user_service import can_access_user, get_user_or_404
from app.core.authorization.permissions import has_permission
from app.core.authorization.roles import has_required_role


# =========================================================
# 👤 CURRENT USER (desde token / middleware)
# =========================================================
def get_current_user_web(
    request: Request,
    db: Session = Depends(get_db)
) -> User:
    """
    Obtiene el usuario autenticado desde request.state.user.

    El middleware debe haber inyectado:
    - sub (user_id)
    - roles
    - permissions
    """

    payload = getattr(request.state, "user", None)

    print("PAYLOAD EN DEPENDENCY:", payload)

    if not payload:
        raise HTTPException(status_code=401, detail="No autenticado")

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido")

    # 🔎 Buscar usuario en BD
    user = db.query(User).filter(
        User.id_usuario == int(user_id)
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    # =========================================================
    # 🔥 Enriquecemos el objeto user con datos del token
    # =========================================================
    user.roles_token = payload.get("roles", [])
    user.permissions = payload.get("permissions", [])

    return user


# =========================================================
# 🎭 REQUIRE ROLES
# =========================================================
def require_roles_web(*allowed_roles: str):
    """
    Permite acceso solo si el usuario tiene alguno de los roles indicados.
    """

    def role_checker(
        current_user: User = Depends(get_current_user_web)
    ) -> User:

        if not has_required_role(
            current_user.roles_token,
            list(allowed_roles)
        ):
            raise HTTPException(
                status_code=403,
                detail="No tienes el rol requerido"
            )

        return current_user

    return role_checker


# =========================================================
# 🔑 REQUIRE PERMISSIONS
# =========================================================
def require_permission_web(*required_permissions: str):
    """
    Permite acceso solo si el usuario tiene los permisos indicados.
    """

    def permission_checker(
        current_user: User = Depends(get_current_user_web)
    ) -> User:

        user_permissions = getattr(current_user, "permissions", [])

        print("USER PERMISSIONS", user_permissions)
        print("REQUIRED PERMISSIONS", required_permissions)

        if not has_permission(
            user_permissions,
            list(required_permissions)
        ):
            raise HTTPException(
                status_code=403,
                detail="No tienes permisos suficientes"
            )

        return current_user

    return permission_checker


# =========================================================
# 👤 OWNER OR PERMISSION
# =========================================================
def require_owner_or_permission_web(permission: str):
    """
    Permite acceso si:
    - El usuario es el dueño
    - O tiene el permiso indicado
    """

    def checker(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user_web)
    ) -> User:

        target_user = get_user_or_404(db, user_id)

        if not can_access_user(
            current_user,
            target_user,
            [permission]
        ):
            raise HTTPException(
                status_code=403,
                detail="No autorizado"
            )

        return target_user

    return checker


# =========================================================
# 🚫 PERMISSION + NOT SELF
# =========================================================
def require_permission_and_not_self_web(permission: str):
    """
    Permite acción solo si:
    - Tiene permiso
    - Y NO es sobre sí mismo (ej: delete)
    """

    def checker(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user_web)
    ) -> User:

        target_user = get_user_or_404(db, user_id)

        # 🚫 evitar auto-acción peligrosa
        if current_user.id_usuario == target_user.id_usuario:
            raise HTTPException(
                status_code=400,
                detail="No puedes realizar esta acción sobre ti mismo"
            )

        # 🔐 validar permisos
        if not has_permission(
            current_user.permissions,
            [permission]
        ):
            raise HTTPException(
                status_code=403,
                detail="No autorizado"
            )

        return target_user

    return checker