# app/db/init_db.py

from app.db.session import engine
from app.db.base import Base

# Importar modelos
from app.modules.users.user_model import User
from app.modules.users.role_model import Role
from app.modules.users.identity_model import Identity
from app.modules.users.user_role_model import UserRole

def init_db():
    Base.metadata.create_all(bind=engine)
