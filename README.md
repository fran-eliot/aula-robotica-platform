# Aula Robótica Platform

Backend de gestión de identidades y control de acceso para el **Aula de
Robótica de la Escuela Politécnica Superior (Universidad de Alcalá)**.

El sistema proporciona una infraestructura de autenticación,
autorización y administración de usuarios para las distintas actividades
del Aula de Robótica, incluyendo el soporte a la competición **Eurobot
Spain**.

Este proyecto forma parte del **Proyecto Final del CFGS en Desarrollo de
Aplicaciones Multiplataforma (DAM)**.

------------------------------------------------------------------------

# Objetivos del proyecto

Desarrollar una plataforma backend que permita:

-   gestión centralizada de usuarios
-   autenticación segura
-   control de acceso basado en roles
-   administración desde panel web
-   trazabilidad de acciones mediante auditoría

El sistema está diseñado para ser reutilizable por distintos proyectos
del laboratorio de robótica.

------------------------------------------------------------------------

# Tecnologías utilizadas

## Backend

-   Python
-   FastAPI
-   SQLAlchemy ORM
-   MariaDB

## Seguridad

-   JWT (JSON Web Token)
-   bcrypt (hash de contraseñas)
-   RBAC (Role Based Access Control)

## Frontend administrativo

-   Jinja2
-   AdminLTE
-   Bootstrap

## Infraestructura

-   Uvicorn
-   entorno virtual con `uv`

------------------------------------------------------------------------

# Funcionalidades principales

## Autenticación

-   login con email y contraseña
-   emisión de JWT
-   almacenamiento del token en cookie segura

## Gestión de usuarios

-   creación de usuarios
-   activación / desactivación
-   eliminación
-   visualización de perfiles

## Gestión de identidades

Una identidad representa una credencial de acceso:

-   email
-   contraseña
-   proveedor de autenticación
-   asociación con usuario
-   rol contextual

## Gestión de roles

Sistema RBAC con roles configurables.

Roles actuales:

-   administrador
-   profesor
-   estudiante

## Panel administrativo

Interfaz web con AdminLTE para:

-   gestión de usuarios
-   gestión de identidades
-   gestión de roles
-   visualización de métricas

## Auditoría

Registro de eventos de seguridad:

-   login
-   logout
-   creación de usuarios
-   modificación de identidades
-   eliminación de recursos

Cada registro almacena:

-   usuario
-   acción
-   descripción
-   dirección IP
-   user agent
-   timestamp

------------------------------------------------------------------------

# Arquitectura del sistema

El sistema sigue una arquitectura modular en capas.

    Presentation Layer
            │
            ▼
    Web Controllers (FastAPI routers)
            │
            ▼
    Service Layer
            │
            ▼
    Persistence Layer (SQLAlchemy)
            │
            ▼
    Database (MariaDB)

    ![Arquitectura](docs/diagramas/architecture_backend.png)

------------------------------------------------------------------------

# Modelo de datos

Entidades principales:

-   usuarios
-   identidades
-   roles
-   audit_logs

Relaciones principales:

    Usuario 1 ─── N Identidades
    Usuario N ─── N Roles
    Usuario 1 ─── N AuditLogs

------------------------------------------------------------------------

# Estado actual del proyecto

Implementado:

-   autenticación JWT
-   RBAC
-   gestión de usuarios
-   gestión de identidades
-   gestión de roles
-   panel administrativo
-   auditoría de acciones

------------------------------------------------------------------------

# Posibles extensiones futuras

El sistema está preparado para integrar módulos adicionales:

-   gestión de equipos
-   registro de robots
-   gestión de competiciones
-   resultados y métricas
-   autenticación OAuth

------------------------------------------------------------------------

# Ejecución del proyecto

Clonar repositorio:

    git clone https://github.com/fran-eliot/aula-robotica-platform

Instalar dependencias:

    uv sync

Ejecutar servidor:

    uvicorn app.main:app --reload

Servidor disponible en:

    http://127.0.0.1:8000

------------------------------------------------------------------------

# Autor

Francisco Ramírez Martín

Backend Developer · Data Engineer en formación

LinkedIn\
https://linkedin.com/in/franeliot

GitHub\
https://github.com/fran-eliot
