# ARCHITECTURE.md

## Arquitectura por capas

API Layer
- Routers FastAPI
- Endpoints REST

Service Layer
- Lógica de negocio
- Servicios de autenticación
- Servicios de usuarios

Persistence Layer
- SQLAlchemy ORM
- Modelos de datos
- Sesiones de base de datos

Security Layer
- JWT
- bcrypt
- RBAC helpers

Presentation Layer
- Plantillas Jinja2
- AdminLTE

## Principios
- Arquitectura modular
- Separación de responsabilidades
- Seguridad por diseño