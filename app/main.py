from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api import auth, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from app.core.middleware.auth_middleware import AuthMiddleware
from app.web import auth_web, users_web, dashboard_web, identities_web, roles_web
from app.core.templates import templates


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
    title="Aula de Robótica EPS-UAH Backend API",
    description="""
API REST para la gestión de autenticación, autorización y usuarios
del Aula de Robótica de la Escuela Politécnica Superior (Universidad de Alcalá).

### Funcionalidades principales:

- Autenticación basada en JWT (HS256)
- Autorización jerárquica basada en roles (RBAC)
- Gestión administrativa de usuarios (CRUD)
- Persistencia con MariaDB
- Arquitectura modular con FastAPI y SQLAlchemy
- Documentación automática OpenAPI

### Seguridad:
Todos los endpoints (excepto login) requieren autenticación mediante Bearer Token.

""",
    version="1.0.0",
    contact={
        "name": "Francisco Ramírez Martín",
        "email": "ramirez.martin.francisco@gmail.com"
    }
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(auth_web.router, tags=["Authentication Web"])
app.include_router(dashboard_web.router, tags=["Dashboard Web"])
app.include_router(users_web.router, tags=["Users Web"])
app.include_router(identities_web.router, tags=["Identities Web"])
app.include_router(roles_web.router, tags=["Roles Web"])

app.add_middleware(AuthMiddleware)

app.openapi = custom_openapi

app.mount("/static", StaticFiles(directory="app/static"), name="static")

