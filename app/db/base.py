# app/db/base.py

from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models so SQLAlchemy registers them
import app.models