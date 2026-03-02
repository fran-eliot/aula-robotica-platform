from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    nombre: str = Field(
        example="Laura García"
    )

class UserResponse(BaseModel):
    id_usuario: int = Field(
        example=1
    )
    nombre: str = Field(
        example="Laura García"
    )
    activo: bool = Field(
        example=True
    )
    fecha_creacion: datetime = Field(
        example="2024-01-01T00:00:00Z"
    )

    class Config:
        from_attributes = True