from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(example="laura_admin@eurobot.es")
    password: str = Field(example="123456")
