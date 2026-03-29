# app/modules/audit/audit_service.py

from fastapi import Request
from sqlalchemy.orm import Session
from datetime import datetime, UTC
from app.modules.audit.audit_model import AuditLog


def log_action(
   db: Session,
    action: str,
    user_id: int | None = None,
    resource_type: str | None = None,
    resource_id: int | None = None,
    description: str | None = None,
    request: Request | None = None
):

    log = AuditLog(
        action=action,
        user_id=user_id,
        resource_type=resource_type,
        resource_id=resource_id,
        description=description,
        ip_address=request.client.host if request else None,
        user_agent=request.headers.get("user-agent") if request else None,
        created_at=datetime.now(UTC)
    )

    db.add(log)
    db.flush()
  