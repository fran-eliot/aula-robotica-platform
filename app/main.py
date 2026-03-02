from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api import auth, users

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Introduce el token JWT obtenido en /auth/login"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    title="Eurobot Spain Backend API",
    description="""
API REST para la gestión de autenticación, autorización y usuarios
del Aula de Robótica de la Escuela Politécnica (Universidad de Alcalá).

###Funcionalidades principales:

- Autenticación basada en JWT
- Autorización jerárquica basada en roles (RBAC)
- Persistencia con MariaDB
- Arquitectura modular con FastAPI y SQLAlchemy
- Documentación automática OpenAPI

Proyecto académico vinculado a la Escuela Politécnica Superior
de la Universidad de Alcalá.
""",
    version="1.0.0",
    contact={
        "name": "Francisco Ramírez Martín",
        "email": "ramirez.martin.francisco@gmail.com"
    }
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])

app.openapi = custom_openapi

