# scripts/init_db.py
# Script para inicializar la base de datos creando las tablas necesarias.

from app.db.base import Base
from app.db.session import engine
from app.modules.users.user_model import User
from app.modules.roles.role_model import Role, Permission, RolePermission
from app.modules.users.user_role_model import UserRole
from app.modules.identities.identity_model import Identity
from app.modules.audit.audit_model import AuditLog


print("📦 Creando tablas...")
Base.metadata.create_all(bind=engine)
print("✔ Tablas creadas")