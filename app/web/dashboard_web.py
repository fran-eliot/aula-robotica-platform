from typing import Optional
from datetime import datetime

from fastapi import APIRouter, Request, Depends

from app.modules.auth.auth_dependencies_web import require_roles_web
from app.core.utils import clean, clean_date, clean_int
from app.modules.users.identity_model import Identity
from sqlalchemy.orm import Session, joinedload
from app.db.session import get_db
from app.modules.users.role_model import Role
from app.modules.users.user_model import User
from app.modules.audit.audit_model import AuditLog
from app.modules.users.user_service import get_user_roles
from app.core.templates import templates

router = APIRouter(prefix="/dashboard", tags=["Dashboard Web"])

@router.get("")
@router.get("/")
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(require_roles_web("admin", "profesor")),
    # filtros
    user_id: Optional[str] = None,
    action: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None
):
    print("👉 DASHBOARD COOKIES:", request.cookies)
    user_id = clean_int(user_id)
    action = clean(action)
    date_from = clean_date(date_from)
    date_to = clean_date(date_to)
    
    total_users = db.query(User).count()

    active_users = db.query(User).filter(User.activo.is_(True)).count()

    identities = db.query(Identity).count()

    total_roles = db.query(Role).count()

    roles = get_user_roles(db, current_user.id_usuario)

    query = db.query(AuditLog).options(joinedload(AuditLog.user))

    if user_id:
        query = query.filter(AuditLog.user_id == int(user_id))

    if action:
        query = query.filter(AuditLog.action.ilike(f"%{action}%"))

    if date_from:
        date_from_parsed = datetime.strptime(date_from, "%Y-%m-%d")
        query = query.filter(AuditLog.created_at >= date_from_parsed)

    if date_to:
        date_to_parsed = datetime.strptime(date_to, "%Y-%m-%d")
        query = query.filter(AuditLog.created_at <= date_to_parsed)

    recent_logs = query.order_by(AuditLog.created_at.desc()).limit(50).all()

    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {
            "request": request,
            "current_user": current_user,
            "current_user_roles": roles,
            "total_users": total_users,
            "active_users": active_users,
            "identities": identities,
            "total_roles": total_roles,
            "recent_logs":recent_logs
        }
    )