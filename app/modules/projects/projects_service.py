# app/modules/projects/projects_service.py
# 📋 Servicio de proyectos: lógica de negocio relacionada con proyectos, tareas y 
# actividades.


from sqlalchemy.orm import Session
from app.modules.projects.project_model import Project


def search_projects(
    db: Session,
    search: str = "",
    status: str = "all",
    page: int = 1,
    per_page: int = 10,
):
    query = db.query(Project)

    # 🔎 Buscar por nombre
    if search:
        query = query.filter(
            Project.name.ilike(f"%{search}%")
        )

    # 📊 Filtrar estado
    if status != "all":
        query = query.filter(
            Project.status == status
        )

    total = query.count()

    projects = (
        query.order_by(Project.id_project.desc())
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )

    return projects, total