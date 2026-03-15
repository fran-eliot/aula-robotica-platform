from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


def log_action(
    db: Session,
    action: str,
    user_id: int | None = None,
    description: str | None = None,
    ip_address: str | None = None,
    user_agent: str | None = None
):

    log = AuditLog(
        action=action,
        user_id=user_id,
        description=description,
        ip_address=ip_address,
        user_agent=user_agent
    )

    db.add(log)
    db.commit()