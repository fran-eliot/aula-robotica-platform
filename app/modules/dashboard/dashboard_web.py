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

    print("Entrando al dashboard con usuario:", current_user.nombre)
   
    # =========================================================
    # 📊 OBTENER MÉTRICAS
    # =========================================================
    metrics = get_dashboard_metrics(db)

    # =========================================================
    # 🎨 RENDER TEMPLATE
    # =========================================================
    try:
        return templates.TemplateResponse(
            "dashboard/dashboard.html",
            {
                "request": request,
                **metrics  # expandimos directamente en el contexto
            }
        )
    except Exception as e:
        print("Error renderizando dashboard:", e)
        return templates.TemplateResponse(
            "dashboard/dashboard.html",
            {
                "request": request,
                "error": "Error al cargar el dashboard"
            }
        )