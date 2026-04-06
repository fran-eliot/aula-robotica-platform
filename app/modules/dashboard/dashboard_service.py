# app/modules/dashboard/dashboard_service.py
# 📊 Servicio de métricas para el dashboard

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.modules.users.user_model import User
from app.modules.audit.audit_model import AuditLog


def get_dashboard_metrics(db: Session) -> dict:
    """
    Obtiene métricas clave del sistema para el dashboard.

    Incluye:
    - Conteo de usuarios
    - Estado de usuarios (activos/inactivos)
    - Últimos logs de auditoría
    """

    # =========================================================
    # 👥 MÉTRICAS DE USUARIOS
    # =========================================================

    # 🔥 Mejor práctica: usar agregaciones en una sola query
    user_stats = db.query(
        func.count(User.id_usuario).label("total"),
        func.sum(User.activo == True).label("active"),
        func.sum(User.activo == False).label("inactive")
    ).one()

    total_users = user_stats.total or 0
    active_users = int(user_stats.active or 0)
    inactive_users = int(user_stats.inactive or 0)

    # =========================================================
    # 🧾 LOGS RECIENTES
    # =========================================================

    recent_logs = (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .limit(10)
        .all()
    )

    # =========================================================
    # 📦 RESULTADO
    # =========================================================

    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users,
        "recent_logs": recent_logs
    }