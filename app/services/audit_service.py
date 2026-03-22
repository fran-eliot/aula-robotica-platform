from sqlalchemy.orm import Session
from datetime import datetime, UTC
from app.models.audit_log import AuditLog


def log_action(
   db: Session,
    action: str,
    user_id: int | None = None,
    resource_type: str | None = None,
    resource_id: int | None = None,
    description: str | None = None,
    ip_address: str | None = None,
    user_agent: str | None = None
):

    log = AuditLog(
        action=action,
        user_id=user_id,
        resource_type=resource_type,
        resource_id=resource_id,
        description=description,
        ip_address=ip_address,
        user_agent=user_agent,
        created_at=datetime.now(UTC)
    )

    db.add(log)
  