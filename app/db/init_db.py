# app/db/init_db.py

from app.db.session import engine
from app.db.base import Base

# Importar modelos
from app.modules.users.user_model import User
from app.modules.roles.role_model import Role, Permission, RolePermission
from app.modules.users.user_role_model import UserRole
from app.modules.identities.identity_model import Identity


def init_db():
    Base.metadata.create_all(bind=engine)
