from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy import func
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.db.session import get_db
from app.core.render import render
from app.core.templates import templates
from app.modules.users.user_model import User
from app.web.context import get_template_context

from app.modules.auth.auth_dependencies_web import (
    require_permission_web,
    get_current_user_web,
)

from app.core.constants.resources import Resources
from app.core.constants.actions import Actions

from app.modules.tasks.task_model import Task
from app.modules.projects.project_model import Project

from app.utils.flash import flash_success
from app.core.utils.validation  import format_pydantic_errors

router = APIRouter(prefix="/tasks", tags=["Tasks Web"])

# =========================================================
# 📋 LISTADO DE TAREAS (con filtros + paginado)
# =========================================================

@router.get("/", response_class=HTMLResponse)
def tasks_list(
    request: Request,
    search: str = "",
    status: str = "all",
    project_id: int | None = None,
    page: int = 1,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.READ)
    ),
):
    per_page = 10

    query = db.query(Task)

    if search:
        query = query.filter(
            Task.name.ilike(f"%{search}%")
        )

    if status != "all":
        query = query.filter(
            Task.status == status
        )

    if project_id:
        query = query.filter(
            Task.project_id == project_id
        )

    # Query filtrada para métricas
    stats_query = query

    total = query.count()

    tasks = (
        query.order_by(Task.id_task.desc())
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )

    total_pages = (total + per_page - 1) // per_page

    projects = db.query(Project).all()

    pending_count = stats_query.filter(
        Task.status == "Pendiente"
    ).count()

    progress_count = stats_query.filter(
        Task.status == "En progreso"
    ).count()

    completed_count = stats_query.filter(
        Task.status == "Completada"
    ).count()

    return render(
        request,
        "tasks/tasks_list.html",
        {
            "tasks": tasks,
            "projects": projects,
            "search": search,
            "status": status,
            "project_id": project_id,
            "page": page,
            "total_pages": total_pages,
            "total_count": total,
            "pending_count": pending_count,
            "progress_count": progress_count,
            "completed_count": completed_count,
        },
    )


# =========================================================
# 📝 FORM CREATE
# =========================================================
@router.get("/form", name="task_form_create")
def task_create_form(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.CREATE)
    ),
):
    projects = db.query(Project).all()
    users = db.query(User).all()

    return templates.TemplateResponse(
        request,
        "tasks/tasks_form.html",
        {
            **get_template_context(request),
            "task": None,
            "projects": projects,
            "users": users,
            "form_data": None,
            "errors": None,
        },
    )


# =========================================================
# 📝 FORM EDIT
# =========================================================
@router.get("/{task_id}/edit", response_class=HTMLResponse)
def task_edit_form(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.UPDATE)
    ),
):
    task = db.query(Task).filter(
        Task.id_task == task_id
    ).first()

    if not task:
        raise HTTPException(404, "Tarea no encontrada")

    projects = db.query(Project).all()
    users = db.query(User).all()

    return render(
        request,
        "tasks/tasks_form.html",
        {
            "task": task,
            "projects": projects,
            "users": users,
            "errors": None,
            "form_data": None,
        },
    )


# =========================================================
# 💾 CREATE
# =========================================================
@router.post("/form")
def task_create(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    project_id: int = Form(...),
    assigned_user_id: int | None = Form(None),
    status: str = Form("Pendiente"),
    priority: str = Form("Media"),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.CREATE)
    ),
):
    task = Task(
        name=name,
        description=description,
        project_id=project_id,
        assigned_user_id=assigned_user_id,
        status=status,
        priority=priority,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return RedirectResponse(
        f"/tasks/{task.id_task}",
        status_code=303
    )


# =========================================================
# 💾 UPDATE
# =========================================================
@router.post("/{task_id}/edit")
def task_update(
    task_id: int,
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    project_id: int = Form(...),
    assigned_user_id: int | None = Form(None),
    status: str = Form(...),
    priority: str = Form(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.UPDATE)
    ),
):
    task = db.query(Task).filter(
        Task.id_task == task_id
    ).first()

    if not task:
        raise HTTPException(404, "Tarea no encontrada")

    task.name = name
    task.description = description
    task.project_id = project_id
    task.assigned_user_id = assigned_user_id
    task.status = status
    task.priority = priority

    db.commit()

    return RedirectResponse(
        f"/tasks/{task.id_task}",
        status_code=303
    )


# =========================================================
# 👁️ DETALLE
# =========================================================
@router.get("/{task_id}", response_class=HTMLResponse)
def task_detail(
    request: Request,
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.READ)
    ),
):
    task = db.query(Task).filter(Task.id_task == task_id).first()

    if not task:
        raise HTTPException(404, "Tarea no encontrada")

    return render(
        request,
        "tasks/tasks_detail.html",
        {
            "task": task,
        },
    )

# =========================================================
# 🗑️ DELETE
# =========================================================
@router.post("/{task_id}/delete")
def task_delete(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission_web(Resources.TASKS, Actions.DELETE)
    ),
):
    task = db.query(Task).filter(
        Task.id_task == task_id
    ).first()

    if not task:
        raise HTTPException(404, "Tarea no encontrada")

    db.delete(task)
    db.commit()

    return RedirectResponse(
        "/tasks/",
        status_code=303
    )