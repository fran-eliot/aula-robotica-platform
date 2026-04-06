# app/modules/auth/auth_schemas.py
# 📋 Schemas de autenticación

from pydantic import BaseModel, EmailStr, Field, field_validator


class LoginRequest(BaseModel):
    """
    Datos necesarios para autenticación de usuario.
    """

    email: EmailStr = Field(
        ...,
        example="laura_admin@eurobot.es",
        description="Email del usuario"
    )

    password: str = Field(
        ...,
        min_length=4,
        example="123456",
        description="Contraseña del usuario"
    )

    # =========================================================
    # 🔎 VALIDACIONES
    # =========================================================
    @field_validator("password")
    def validate_password(cls, v):
        if not v.strip():
            raise ValueError("La contraseña no puede estar vacía")
        return v