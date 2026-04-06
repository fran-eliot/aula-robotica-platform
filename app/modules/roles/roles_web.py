# app/modules/roles/roles_web.py
# 🔐 Rutas web para gestión de Roles y Permisos (RBAC)

from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.templates import templates
from app.utils.flash import flash_success, flash_error

from app.modules.auth.auth_dependencies_web import require_permission_web
from app.modules.roles.role_service import (
    get_all_roles,
    get_role_or_404,
    create_role,
    update_role,
    delete_role,
    get_all_permissions,
    sync_role_permissions,
    group_permissions,
    get_role_audit_logs
)

router = APIRouter(prefix="/roles", tags=["Roles Web"])


# =========================================================
# 📋 LISTADO
# =========================================================
@router.get("/")
def roles_list(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:read"))
):
    """
    Lista todos los roles.
    """

    roles = get_all_roles(db)

    return templates.TemplateResponse(
        "roles/roles_list.html",
        {
            "request": request,
            "roles": roles
        }
    )


# =========================================================
# 🔍 DETALLE
# =========================================================
@router.get("/{role_id}")
def role_detail(
    request: Request,
    role_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:read"))
):
    """
    Vista detalle de rol:
    - Permisos agrupados
    - Auditoría
    """

    role = get_role_or_404(db, role_id)

    grouped_permissions = group_permissions(role.permissions)
    logs = get_role_audit_logs(db, role_id)

    return templates.TemplateResponse(
        "roles/roles_detail.html",
        {
            "request": request,
            "role": role,
            "grouped_permissions": grouped_permissions,
            "logs": logs
        }
    )


# =========================================================
# 📝 FORMULARIO (CREATE + EDIT)
# =========================================================
@router.get("/form")
@router.get("/{role_id}/edit")
def role_form(
    request: Request,
    role_id: int | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):
    """
    Formulario unificado para crear o editar roles.
    """

    role = None

    if role_id:
        role = get_role_or_404(db, role_id)

    permissions = get_all_permissions(db)
    grouped_permissions = group_permissions(permissions)

    return templates.TemplateResponse(
        "roles/roles_form.html",
        {
            "request": request,
            "role": role,
            "grouped_permissions": grouped_permissions
        }
    )


# =========================================================
# 💾 GUARDAR (CREATE + UPDATE)
# =========================================================
@router.post("/form")
@router.post("/{role_id}/edit")
def role_save(
    request: Request,
    nombre: str = Form(...),
    descripcion: str = Form(""),
    permissions: list[int] = Form([]),
    role_id: int | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:update"))
):
    """
    Guarda rol:
    - Si existe → update
    - Si no → create
    """

    try:
        # 🔥 UPDATE
        if role_id:
            role = get_role_or_404(db, role_id)

            update_role(db, role, nombre, descripcion)
            sync_role_permissions(db, role, permissions)

            flash_success(request, "Rol actualizado correctamente")

        # 🔥 CREATE
        else:
            role = create_role(db, nombre, descripcion)
            sync_role_permissions(db, role, permissions)

            flash_success(request, "Rol creado correctamente")

        db.commit()

        return RedirectResponse("/roles/", status_code=303)

    except HTTPException as e:
        flash_error(request, e.detail)

        permissions_all = get_all_permissions(db)

        return templates.TemplateResponse(
            "roles/roles_form.html",
            {
                "request": request,
                "role": None,
                "grouped_permissions": group_permissions(permissions_all)
            }
        )


# =========================================================
# 🗑️ ELIMINAR
# =========================================================
@router.post("/{role_id}/delete")
def role_delete(
    request: Request,
    role_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:delete"))
):
    """
    Elimina un rol.
    """

    role = get_role_or_404(db, role_id)

    delete_role(db, role)

    db.commit()

    flash_success(request, "Rol eliminado correctamente")

    return RedirectResponse("/roles/", status_code=303)