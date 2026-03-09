from fastapi import APIRouter, Request, Depends

from app.api.deps import get_current_user_from_cookie
from app.models.identity import Identity
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.role import Role
from app.models.user import User
from app.models.user import User
from app.services.user_service import get_user_roles
from app.core.templates import templates

router = APIRouter(prefix="/dashboard", tags=["Dashboard Web"])

@router.get("/")
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_from_cookie)
):
    total_users = db.query(User).count()

    active_users = db.query(User).filter(User.activo == True).count()

    identities = db.query(Identity).count()

    total_roles = db.query(Role).count()

    roles = get_user_roles(db, current_user.id_usuario)

    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {
            "request": request,
            "current_user": current_user,
            "current_user_roles": roles,
            "total_users": total_users,
            "active_users": active_users,
            "identities": identities,
            "total_roles": total_roles
        }
    )