# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DEBUG: bool = True  
    ENV: str = "dev"  # dev | prod

    app_base_url: str = "http://127.0.0.1:8000"

    saml_entity_id: str | None = None
    saml_acs_url: str | None = None
    saml_metadata_url: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
