# app/db/init_db.py

from app.db.base import Base
from app.db.session import engine

# Importar modelos


def init_db():
    Base.metadata.create_all(bind=engine)
