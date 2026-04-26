# app/modules/projects/projects_web.py

# Este archivo define las rutas web para la gestión de proyectos, tareas y
# actividades. Estas rutas renderizan plantillas HTML y permiten a los usuarios
# interactuar con los proyectos a través de una interfaz web. Cada ruta incluye
# las dependencias necesarias para la autenticación, autorización y acceso a la
# base de datos, asegurando que solo los usuarios con los permisos adecuados puedan
# acceder a las funcionalidades correspondientes. Las plantillas HTML se encuentran
# en la carpeta "templates/projects" y "templates/tasks" y se utilizan para mostrar
# la información de los proyectos, tareas y actividades de manera visual y amigable.


from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.render import render
from app.db.session import get_db
from app.core.templates import templates

from app.modules.auth.auth_dependencies_web import require_permission_web
from app.core.constants.actions import Actions
from app.core.constants.resources import Resources

from app.modules.projects.project_model import Project
from app.modules.projects.projects_service import search_projects
from app.modules.tasks.task_model import Task
from app.utils.flash import flash_success

router = APIRouter(prefix="/projects", tags=["Projects Web"])


# =========================================================
# 📋 LISTADO
# =========================================================
@router.get("/")
def projects_list(
    request: Request,
    search: str = "",
    status: str = "all",
    page: int = 1,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.READ,
        )
    ),
):
    per_page = 10

    projects, total = search_projects(
        db,
        search=search,
        status=status,
        page=page,
        per_page=per_page,
    )

    total_pages = (total + per_page - 1) // per_page

    return render(
        request,
        "projects/projects_list.html",
        {
            "projects": projects,
            "search": search,
            "status": status,
            "page": page,
            "total_pages": total_pages,
        },
    )

# =========================================================
# 📝 FORM CREATE
# =========================================================
@router.get("/form", name="project_form_create")
def project_create_form(
    request: Request,
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.CREATE,
        )
    ),
):
    return render(
        request,
        "projects/projects_form.html",
        {
            "project": None,
            "form_data": None,
            "errors": None,
        },
    )


# =========================================================
# 💾 CREATE
# =========================================================
@router.post("/form")
def project_create(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.CREATE,
        )
    ),
):
    name = name.strip()
    description = description.strip()

    errors = {}

    if not name:
        errors["name"] = "El nombre es obligatorio"

    if errors:
        return render(
            request,
            "projects/projects_form.html",
            {
                "project": None,
                "form_data": {
                    "name": name,
                    "description": description,
                },
                "errors": errors,
            },
        )

    project = Project(
        name=name,
        description=description,
        status="Activo",
        created_by=current_user.id_usuario,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    flash_success(
        request,
        "Proyecto creado correctamente",
    )

    return RedirectResponse(
        f"/projects/{project.id_project}",
        status_code=303,
    )


# =========================================================
# 👁️ DETALLE
# =========================================================
@router.get("/{project_id}")
def project_detail(
    request: Request,
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.READ,
        )
    ),
):
    project = (
        db.query(Project)
        .filter(Project.id_project == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Proyecto no encontrado",
        )

    tasks = (
        db.query(Task)
        .filter(Task.project_id == project_id)
        .order_by(Task.id_task.desc())
        .all()
    )

    return render(
        request,
        "projects/projects_detail.html",
        {
            "project": project,
            "tasks": tasks,
        },
    )


# =========================================================
# 📝 FORM EDIT
# =========================================================
@router.get("/{project_id}/edit", name="project_form_edit")
def project_edit_form(
    request: Request,
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.UPDATE,
        )
    ),
):
    project = (
        db.query(Project)
        .filter(Project.id_project == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Proyecto no encontrado",
        )

    return render(
        request,
        "projects/projects_form.html",
        {
            "project": project,
            "form_data": None,
            "errors": None,
        },
    )


# =========================================================
# 💾 UPDATE
# =========================================================
@router.post("/{project_id}/edit")
def project_update(
    request: Request,
    project_id: int,
    name: str = Form(...),
    description: str = Form(""),
    status: str = Form(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.UPDATE,
        )
    ),
):
    project = (
        db.query(Project)
        .filter(Project.id_project == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Proyecto no encontrado",
        )

    name = name.strip()
    description = description.strip()

    errors = {}

    if not name:
        errors["name"] = "El nombre es obligatorio"

    if status not in ["Activo", "Finalizado"]:
        errors["status"] = "Estado inválido"

    if errors:
        return render(
            request,
            "projects/projects_form.html",
            {
                "project": project,
                "form_data": {
                    "name": name,
                    "description": description,
                    "status": status,
                },
                "errors": errors,
            },
        )

    project.name = name
    project.description = description
    project.status = status

    db.commit()

    flash_success(
        request,
        "Proyecto actualizado correctamente",
    )

    return RedirectResponse(
        f"/projects/{project.id_project}",
        status_code=303,
    )


# =========================================================
# 🗑️ DELETE
# =========================================================
@router.post("/{project_id}/delete")
def project_delete(
    request: Request,
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(
            Resources.PROJECTS,
            Actions.DELETE,
        )
    ),
):
    project = (
        db.query(Project)
        .filter(Project.id_project == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Proyecto no encontrado",
        )

    db.delete(project)
    db.commit()

    flash_success(
        request,
        "Proyecto eliminado correctamente",
    )

    return RedirectResponse(
        "/projects/",
        status_code=303,
    )
