from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    nombre: str

class UserResponse(BaseModel):
    id_usuario: int
    nombre: str
    activo: bool
    fecha_creacion: datetime

    class Config:
        from_attributes = True