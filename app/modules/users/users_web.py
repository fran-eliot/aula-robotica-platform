# app/modules/users/users_web.py

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.templates import templates

# 🔐 Auth / permisos
from app.modules.auth.auth_dependencies_web import (
    get_current_user_web,
    require_permission_web,
    require_permission_and_not_self_web,
    require_owner_or_permission_web
)

# 🧠 Services
from app.modules.users.user_service import (
    get_user_or_404,
    get_user_by_id,
    search_users,
    create_user_with_audit,
    update_user_with_audit,
    delete_user_with_audit,
    set_user_active_with_audit,
    sync_user_roles,
)

from app.modules.roles.role_service import get_all_roles
from app.modules.users.user_view_service import build_user_detail_view

# 📦 Schemas
from app.modules.users.user_schemas import UserUpdate

# 🧰 Utils
from app.core.utils.validation import format_pydantic_errors
from app.utils.flash import flash_success


router = APIRouter(prefix="/users", tags=["Users Web"])


# =========================================================
# 📋 LISTADO DE USUARIOS
# =========================================================
@router.get("/")
def users_list(
    request: Request,
    search: str = "",
    status: str = "all",  # all | active | inactive
    page: int = 1,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:read"))
):
    """
    Listado de usuarios con búsqueda, filtro y paginación.
    """

    per_page = 10

    users, total = search_users(
        db,
        search=search,
        status=status,
        page=page,
        per_page=per_page
    )

    total_pages = (total + per_page - 1) // per_page

    return templates.TemplateResponse(
        "users/users_list.html",
        {
            "request": request,
            "users": users,
            "search": search,
            "status": status,
            "page": page,
            "total_pages": total_pages
        }
    )


# =========================================================
# 📝 FORMULARIO (CREATE + EDIT)
# =========================================================
@router.get("/form", name="user_form_create")
@router.get("/{user_id}/edit", name="user_form_edit")
def user_form(
    request: Request,
    user_id: int | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):
    """
    Formulario reutilizable para crear o editar usuarios.
    """

    user = None

    if user_id:
        user = get_user_or_404(db, user_id)

    roles = get_all_roles(db)

    return templates.TemplateResponse(
        "users/user_form.html",
        {
            "request": request,
            "user": user,
            "roles": roles,
            "form_data": None,
            "errors": None
        }
    )


# =========================================================
# 💾 GUARDAR (CREATE + UPDATE)
# =========================================================
@router.post("/form")
@router.post("/{user_id}/edit")
def user_save(
    request: Request,
    nombre: str = Form(...),
    activo: bool = Form(False),
    roles: list[int] = Form([]),
    user_id: int | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_owner_or_permission_web("users:update"))
):
    """
    Guarda usuario:
    - CREATE → crea usuario + asigna roles
    - UPDATE → actualiza usuario + sincroniza roles
    """

    user = None

    if user_id:
        user = get_user_or_404(db, user_id)

    # =========================================================
    # 🔎 VALIDACIÓN
    # =========================================================
    try:
        data = UserUpdate(nombre=nombre, activo=activo)

    except ValidationError as e:
        return templates.TemplateResponse(
            "users/user_form.html",
            {
                "request": request,
                "user": user,
                "roles": get_all_roles(db),  # 🔥 importante
                "form_data": {
                    "nombre": nombre,
                    "activo": activo,
                    "roles": roles
                },
                "errors": format_pydantic_errors(e.errors())
            }
        )

    # =========================================================
    # 🔥 UPDATE
    # =========================================================
    if user:

        update_user_with_audit(
            db, user, data.nombre, current_user, request
        )

        user.activo = (
            data.activo if data.activo is not None else user.activo
        )

    # =========================================================
    # 🔥 CREATE
    # =========================================================
    else:

        user = create_user_with_audit(
            db, data.nombre, current_user, request
        )

    # =========================================================
    # 🔐 ROLES (SIEMPRE DESPUÉS)
    # =========================================================
    sync_user_roles(db, user, roles)

    # =========================================================
    # 💾 COMMIT FINAL
    # =========================================================
    db.commit()

    flash_success(
        request,
        "Usuario actualizado correctamente" if user_id else "Usuario creado correctamente"
    )

    return RedirectResponse(
        f"/users/{user.id_usuario}",
        status_code=303
    )


# =========================================================
# 👤 DETALLE DE USUARIO
# =========================================================
@router.get("/{user_id}")
def user_detail(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):
    """
    Vista completa del usuario:
    - roles
    - permisos
    - auditoría
    """

    context = build_user_detail_view(db, user_id)

    return templates.TemplateResponse(
        "users/user_detail.html",
        {
            "request": request,
            **context
        }
    )


# =========================================================
# 🙋 MI PERFIL
# =========================================================
@router.get("/me", name="my_profile")
def my_profile(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):
    """
    Perfil del usuario autenticado.
    """

    context = build_user_detail_view(db, current_user.id_usuario)

    return templates.TemplateResponse(
        "users/user_detail.html",
        {
            "request": request,
            **context
        }
    )


# =========================================================
# 🔐 ROLES DEL USUARIO
# =========================================================
@router.post("/{user_id}/roles")
def update_user_roles(
    request: Request,
    user_id: int,
    roles: list[int] = Form([]),
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):
    """
    Sincroniza los roles del usuario.
    """

    user = get_user_by_id(db, user_id)

    sync_user_roles(db, user, roles)

    db.commit()

    flash_success(request, "Roles actualizados correctamente")

    return RedirectResponse(f"/users/{user_id}", status_code=303)


# =========================================================
# 🗑️ ELIMINAR USUARIO
# =========================================================
@router.post("/{user_id}/delete")
def delete_user(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_and_not_self_web("users:delete"))
):
    """
    Elimina un usuario (con auditoría).
    """

    user = get_user_or_404(db, user_id)

    delete_user_with_audit(db, user, current_user, request)

    db.commit()

    flash_success(request, "Usuario eliminado correctamente")

    return RedirectResponse("/users/", status_code=303)


# =========================================================
# 🔄 ACTIVAR / DESACTIVAR
# =========================================================
@router.post("/{user_id}/deactivate")
def deactivate_user(
    request: Request,
    user = Depends(require_owner_or_permission_web("users:update")),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):
    """
    Desactiva un usuario.
    """

    set_user_active_with_audit(db, user, False, current_user, request)

    db.commit()

    flash_success(request, "Usuario desactivado")

    return RedirectResponse(f"/users/{user.id_usuario}", status_code=303)


@router.post("/{user_id}/activate")
def activate_user(
    request: Request,
    user = Depends(require_owner_or_permission_web("users:update")),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_web)
):
    """
    Activa un usuario.
    """

    set_user_active_with_audit(db, user, True, current_user, request)

    db.commit()

    flash_success(request, "Usuario activado")

    return RedirectResponse(f"/users/{user.id_usuario}", status_code=303)