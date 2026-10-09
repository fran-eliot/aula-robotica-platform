# 🤖 Aula Robótica Platform

> Plataforma colaborativa educativa desarrollada para la gestión de proyectos de robótica, con arquitectura backend modular, IAM avanzado, WebSockets realtime y despliegue cloud multicontenedor.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Docker](https://img.shields.io/badge/Docker-Deployed-2496ED)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-009639)
![MariaDB](https://img.shields.io/badge/MariaDB-11-blue)
![WebSockets](https://img.shields.io/badge/WebSockets-Realtime-purple)
![Coverage](https://img.shields.io/badge/Coverage-75%25-success)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-Automated-black)
![License](https://img.shields.io/badge/license-Educational-lightgrey)

---

# 📚 Tabla de contenidos

* Descripción
* Características principales
* Arquitectura
* Infraestructura Cloud
* Stack tecnológico
* Seguridad e IAM
* Realtime y WebSockets
* Calidad software
* Docker y despliegue
* Instalación local
* Estructura del proyecto
* Documentación técnica
* Estado actual
* Roadmap
* Autor

---

# 📖 Descripción

**Aula Robótica Platform** es una plataforma colaborativa educativa orientada a la gestión de proyectos de robótica desarrollada como **Proyecto Final del CFGS DAM (Desarrollo de Aplicaciones Multiplataforma)**.

La aplicación permite gestionar usuarios, identidades, proyectos, tareas, actividades y notificaciones mediante una arquitectura backend moderna basada en:

* FastAPI
* SQLAlchemy
* MariaDB
* JWT Authentication
* WebSockets
* Arquitectura IAM desacoplada
* RBAC contextual
* Docker
* Nginx Reverse Proxy

El proyecto ha evolucionado desde un entorno académico local hasta una infraestructura cloud desplegada sobre Linux real utilizando Docker Compose y arquitectura multicontenedor.

---

# ✨ Características principales

## ⚡ Realtime Collaboration

* WebSockets multiusuario
* Kanban sincronizado
* Actualización instantánea de actividad
* Dashboard realtime
* Notificaciones live
* Sincronización colaborativa

---

## 🔐 IAM & Security

* JWT Authentication
* Cookies HTTPOnly
* RBAC contextual
* Roles globales y contextuales
* Middleware de autorización
* Auditoría integrada
* Arquitectura preparada para SAML/SSO

---

## 👥 Gestión de usuarios

* CRUD completo
* Gestión de identidades
* Activación y desactivación
* Roles y permisos efectivos
* Auditoría de cambios

---

## 📁 Gestión de proyectos

* Gestión colaborativa
* Miembros y coordinadores
* Feed de actividad
* Actividades asociadas
* Métricas por proyecto
* Control contextual de acceso

---

## ✅ Gestión de tareas

* Kanban colaborativo
* Drag & Drop
* Prioridades
* Estados
* Asignaciones
* Auditoría
* Realtime mediante WebSockets

---

## 🔔 Notificaciones

* Notificaciones contextuales
* Sistema realtime
* Marcado de lectura
* Integración con proyectos y tareas

---

# 🏗 Arquitectura del sistema

La plataforma utiliza una arquitectura modular multicapa.

```text
┌──────────────────────────────┐
│        Frontend SSR          │
│ Jinja2 + AdminLTE + Bootstrap│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ FastAPI Routers + WebSockets │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Service Layer / IAM      │
│ RBAC / Business Logic        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       SQLAlchemy ORM         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          MariaDB             │
└──────────────────────────────┘
```

---

# ☁️ Infraestructura Cloud

La plataforma ha sido desplegada y validada sobre una infraestructura cloud real.

## Infraestructura utilizada

* Hetzner Cloud VPS (CX22)
* Ubuntu Server 24.04 LTS
* Docker Engine
* Docker Compose
* Nginx Reverse Proxy
* MariaDB 11
* Docker Volumes
* WebSockets operativos
* SSH Hardening
* Firewall Cloud
* Snapshot de recuperación

---

## Arquitectura desplegada

```text
Internet
    │
    ▼
Nginx Reverse Proxy
    │
    ▼
FastAPI + WebSockets
    │
    ▼
MariaDB
```

### Características del despliegue

* Arquitectura multicontenedor
* Persistencia desacoplada
* Reverse proxy dedicado
* Networking privado Docker
* Realtime validado
* Despliegue reproducible

---

# 🧱 Stack tecnológico

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy
* PyMySQL
* Pydantic
* Uvicorn

---

## Frontend SSR

* Jinja2
* AdminLTE
* Bootstrap
* JavaScript
* Chart.js
* SweetAlert2

---

## Base de datos

* MariaDB 11

---

## Seguridad

* JWT
* Cookies HTTPOnly
* RBAC contextual
* Middleware Authentication
* Auditoría

---

## DevOps

* Docker
* Docker Compose
* Nginx
* Ubuntu Server
* Hetzner Cloud
* GitHub Actions

---

# 🔐 Seguridad e IAM

La plataforma implementa una arquitectura IAM desacoplada orientada a entornos educativos y colaborativos.

## Características

* Gestión User / Identity desacoplada
* Roles globales
* Roles contextuales
* Ownership validation
* RBAC granular
* Auditoría de acciones
* Middleware de autorización

---

## Seguridad de infraestructura

* SSH mediante claves ED25519
* Root deshabilitado
* Usuario administrativo dedicado
* Firewall Cloud
* Docker Network privada
* Backend no expuesto directamente
* Reverse Proxy Nginx

---

# ⚡ Realtime y WebSockets

La plataforma incorpora comunicación realtime autenticada.

## Funcionalidades

* Dashboard realtime
* Kanban sincronizado
* Notificaciones live
* Activity Feed
* Actualización instantánea

---

## Endpoints principales

```text
/ws/dashboard
/ws/notifications
/ws/projects/{id}
```

---

## Validación realizada

* HTTP 101 Switching Protocols
* Múltiples clientes simultáneos
* Sincronización realtime funcional
* Logs Docker verificados

---

# 🧪 Calidad software

La calidad del software constituye uno de los pilares principales del proyecto.

## Herramientas utilizadas

* Pytest
* Ruff
* SonarCloud
* GitHub Actions
* Coverage

---

## Cobertura y testing

Actualmente el proyecto dispone de:

* Más de 240 tests automatizados
* Cobertura superior al 75%
* Testing de servicios críticos
* Validación automática CI/CD
* Análisis estático automatizado

---

## Componentes cubiertos

* Autenticación
* Permisos
* Dashboard
* Usuarios
* Roles
* Identidades
* Proyectos
* Tareas
* Notificaciones
* Activity Feed

---

# 🐳 Docker y despliegue

La infraestructura completa está preparada para desplegarse mediante Docker Compose.

## Servicios desplegados

* FastAPI
* MariaDB
* Nginx Reverse Proxy

---

## Despliegue rápido

```bash
git clone https://github.com/fran-eliot/aula-robotica-platform.git

cd aula-robotica-platform/deploy

cp .env.example .env

docker compose up -d --build
```

---

## Gestión de contenedores

```bash
docker compose ps
```

```bash
docker compose logs -f
```

```bash
docker compose down
```

---

# 🚀 Instalación local

## Clonar repositorio

```bash
git clone https://github.com/fran-eliot/aula-robotica-platform.git

cd aula-robotica-platform
```

---

## Instalar dependencias

```bash
uv sync
```

---

## Configurar entorno

Crear:

```text
.env
```

a partir de:

```text
.env.example
```

---

## Ejecutar aplicación

```bash
uv run uvicorn app.main:app --reload
```

Disponible en:

```text
http://127.0.0.1:8000
```

---

# 📂 Estructura del proyecto

```text
app/
├── core/
├── db/
├── modules/
│   ├── auth/
│   ├── users/
│   ├── roles/
│   ├── identities/
│   ├── projects/
│   ├── tasks/
│   ├── notifications/
│   ├── dashboard/
│   ├── activities/
│   └── audit/
│
├── templates/
├── static/
└── main.py

deploy/
├── Dockerfile
├── docker-compose.yml
├── nginx/
├── scripts/
└── .env.example

docs/

tests/
```

---

# 📚 Documentación técnica

El proyecto incorpora documentación técnica detallada en:

```text
docs/
```

Incluyendo:

* Arquitectura
* Seguridad IAM
* Docker
* Despliegue Cloud
* Realtime
* Testing
* Modelo de datos
* Decisiones arquitectónicas
* Integración SAML

---

# 🚀 Estado actual

✅ Plataforma funcional

✅ IAM avanzado

✅ Realtime operativo

✅ WebSockets autenticados

✅ Docker Compose operativo

✅ Despliegue Cloud realizado

✅ Reverse Proxy Nginx

✅ MariaDB persistente

✅ Seguridad documentada

✅ Cobertura > 75%

✅ CI/CD operativo

---

# 🔮 Roadmap

## Seguridad

* HTTPS completo
* Certificados SSL
* OAuth2
* SAML real
* MFA

---

## Infraestructura

* Deploy automático
* Observabilidad
* Monitorización
* Backups automatizados

---

## Plataforma

* Métricas avanzadas
* SPA complementaria
* Mobile support
* Escalabilidad horizontal
* Kubernetes

---

# 👨‍💻 Autor

## Francisco Ramírez Martín

**Backend Developer · Full Stack Developer · Data & AI Enthusiast**

### Formación

* CFGS DAM — IES Lope de Vega
* Grado en Ingeniería Informática — UNED
* Bootcamp Full Stack Development
* Bootcamp Data Analytics

### Tecnologías principales

* Python
* FastAPI
* Java
* Spring Boot
* Angular
* SQL
* Docker
* AWS

### Contacto

🔗 LinkedIn

https://linkedin.com/in/franeliot

💻 GitHub

https://github.com/fran-eliot

---

# 📈 Conclusión

Aula Robótica Platform demuestra la viabilidad de una plataforma educativa colaborativa moderna basada en arquitectura modular, IAM avanzado, WebSockets realtime, despliegue cloud, Docker y buenas prácticas DevOps.

El proyecto combina backend moderno, seguridad, testing, realtime e infraestructura cloud real, reproduciendo una arquitectura cercana a la utilizada en numerosos entornos profesionales actuales.
