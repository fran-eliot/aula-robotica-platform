# app/modules/dashboard/dashboard_web.py
# 🌐 Router web para dashboard

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.dashboard.dashboard_service import get_dashboard_metrics
from app.modules.auth.auth_dependencies_web import require_permission_web
from app.core.templates import templates

router = APIRouter()


@router.get("/dashboard")
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(require_permission_web("users:read"))
):
    """
    Vista principal del dashboard.

    Requiere:
    - Permiso: users:read

    Muestra:
    - Métricas de usuarios
    - Actividad reciente (audit logs)
    """

    # =========================================================
    # 📊 OBTENER MÉTRICAS
    # =========================================================
    metrics = get_dashboard_metrics(db)

    # =========================================================
    # 🎨 RENDER TEMPLATE
    # =========================================================
    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {
            "request": request,
            **metrics  # expandimos directamente en el contexto
        }
    )