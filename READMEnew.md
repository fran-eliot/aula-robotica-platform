# 🤖 Aula Robótica Platform

![Tests](https://github.com/fran-eliot/aula-robotica-platform/actions/workflows/tests.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-76%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-success)

Backend modular para gestión de **usuarios, identidades y control de acceso (RBAC)** desarrollado para el **Aula de Robótica de la Escuela Politécnica Superior (Universidad de Alcalá)**.

Diseñado como una plataforma escalable para soportar operaciones internas, autenticación centralizada y futuras extensiones (equipos, proyectos, competiciones como Eurobot Spain).

---

## 🚀 Demo técnica

* ✅ Autenticación JWT con cookies seguras  
* ✅ Sistema RBAC completo (roles + permisos)  
* ✅ Panel administrativo web  
* ✅ Auditoría de acciones  
* ✅ Tests automatizados + CI (GitHub Actions)  
* ✅ ~70% coverage  

---

## 🧠 Visión del proyecto

Este proyecto no es solo un CRUD. Es una **base de arquitectura backend real**, preparada para:

* Múltiples tipos de usuarios.
* Múltiples proveedores de identidad.
* Control granular de permisos.
* Trazabilidad completa de acciones.
* Crecimiento modular.

---

## 🎯 Objetivos

* Centralizar autenticación e identidades.
* Implementar autorización segura y escalable.
* Proporcionar panel administrativo.
* Registrar auditoría de acciones.
* Aplicar arquitectura profesional en FastAPI.

---

## 🧱 Stack tecnológico

### Backend
* **Lenguaje:** Python 3.13
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Base de Datos:** MariaDB / SQLite (para tests)

### Seguridad
* JWT (Access + Refresh Tokens)
* Cookies HTTPOnly
* Encriptación con bcrypt
* RBAC (roles + permisos)

### Frontend
* Jinja2 (Templating)
* AdminLTE
* Bootstrap

### Dev & Infra
* **uv:** Gestión de dependencias
* **Pytest:** Suite de testing
* **GitHub Actions:** Integración Continua (CI)

---

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en capas para asegurar la mantenibilidad:

```text
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
    ```
    ![Arquitectura](docs/diagramas/architecture_backend.png)

---

## 🔐 Sistema de seguridad

### Autenticación

- Login con email + contraseña
- Tokens JWT (access + refresh)
- Cookies seguras HTTPOnly

### Autorización (RBAC)

Sistema híbrido:

- Roles → nivel alto (admin, student…)
- Permisos → control granular (`users:create`, etc.)

### Protección

- Middleware de autenticación
- Dependencias FastAPI para permisos
- Control de ownership

---

## ⚙️ Funcionalidades

### 👤 Usuarios
- CRUD completo
- activación / desactivación
- roles y permisos efectivos
- auditoría asociada

### 🔑 Identidades
- múltiples credenciales por usuario
- soporte para distintos providers
- separación user / auth

### 🛡️ Roles
- creación y edición
- asignación de permisos
- agrupación por módulos

### 📊 Dashboard
- métricas básicas
- accesos rápidos

### 🧾 Auditoría
Registro de:
- login
- acciones CRUD
- cambios en sistema

Incluye:
- usuario
- acción
- recurso
- IP
- timestamp

---

## 🧪 Testing & Calidad

- 22 tests automatizados
- cobertura aproximada: **69%**
- CI con GitHub Actions

Ejecutar tests:

```bash
uv run pytest -v
```

Coverage:

```bash
uv run pytest --cov=app --cov-report=term-missing
```
---

##📁 Estructura del proyecto

```text
app/
 ├── core/              # config, seguridad, middleware
 ├── modules/           # dominios (users, roles, identities...)
 ├── db/                # conexión DB
 ├── web/               # vistas web
 └── utils/             # utilidades
 ```

 🧩 Modelo de datos
Users
Identities
Roles
Permissions
Audit Logs

Relaciones:

User 1 ─── N Identities
User N ─── N Roles
User 1 ─── N AuditLogs

⚖️ Decisiones de diseño
JWT en cookies

✔ evita XSS
✔ compatible con SSR

Roles en token

✔ rendimiento
✖ requiere relogin si cambian

Permisos en código

✔ simple
✖ menos flexible

Jinja vs SPA

✔ rapidez
✖ menos interactividad

---

## 🚀 Instalación

```bash
git clone https://github.com/fran-eliot/aula-robotica-platform
cd aula-robotica-platform

uv sync
uvicorn app.main:app --reload
```

App en :
http://127.0.0.1:8000

---

## 🛣️ Roadmap
OAuth / SSO (Google, GitHub)
Gestión de equipos
Gestión de proyectos
Métricas avanzadas
API pública

---

## 👨‍💻 Autor

Francisco Ramírez Martín

Backend Developer · Data Engineer en formación

🔗 LinkedIn
https://linkedin.com/in/franeliot

💻 GitHub
https://github.com/fran-eliot
