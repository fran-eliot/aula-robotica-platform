# app/modules/dashboard/dashboard_service.py
# 📊 Servicio de métricas para el dashboard

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.modules.audit.audit_model import AuditLog
from app.modules.identities.identity_model import Identity
from app.modules.roles.role_model import Role
from app.modules.users.user_model import User


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
        func.sum(User.activo.is_(True)).label("active"),
        func.sum(User.activo.is_(False)).label("inactive")
    ).one()

    total_users = user_stats.total or 0
    active_users = int(user_stats.active or 0)
    inactive_users = int(user_stats.inactive or 0)

    # =========================================================
    # 🛡️ MÉTRICAS DE ROLES
    # =========================================================

    total_roles = db.query(func.count(Role.id_rol)).scalar() or 0

    # ================= IDENTITIES METRICS =================
    identities_stats = db.query(
        func.count(Identity.id).label("total"),
        func.sum(Identity.provider == "local").label("local"),
        func.sum(Identity.provider != "local").label("external")
    ).one()

    total_identities = identities_stats.total or 0
    local_identities = identities_stats.local or 0
    external_identities = identities_stats.external or 0

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
        "total_roles": total_roles,
        "total_identities": total_identities,
        "local_identities": local_identities,
        "external_identities": external_identities,
        "recent_logs": recent_logs
    }