# app/modules/projects/task_model.py

# Este archivo define el modelo de datos para las tareas en la aplicación.
# Utiliza SQLAlchemy para definir la estructura de la tabla "tasks" en la base
# de datos, incluyendo sus columnas, tipos de datos, relaciones y restricciones.
# El modelo también incluye un método de representación para facilitar la depuración
# y visualización de los objetos de tarea.


from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id_task = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.id_project", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)

    status = Column(String(50), default="Pendiente", nullable=False)
    priority = Column(String(20), default="Media", nullable=False)

    assigned_user_id = Column(
        Integer,
        ForeignKey("usuarios.id_usuario"),
        nullable=True
    )

    due_date = Column(Date, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.now(UTC),
        nullable=False
    )

    # Relaciones
    project = relationship("Project", back_populates="tasks")

    assigned_user = relationship("User")

    activities = relationship(
        "Activity",
        back_populates="task",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Task(id={self.id_task}, name='{self.name}')>"