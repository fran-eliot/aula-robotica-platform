# 00_MASTER_CONTEXT.md

# 🤖 Aula Robótica Platform — Contexto Maestro del Proyecto

---

# 📌 Identidad del Proyecto

## Nombre del proyecto

**Aula Robótica Platform**

---

## Tipo de sistema

Plataforma colaborativa educativa orientada a la gestión de proyectos de robótica, coordinación académica, colaboración multiusuario y operaciones realtime.

La plataforma ha evolucionado desde un proyecto académico DAM hacia una arquitectura backend moderna desplegada sobre infraestructura cloud Linux real.

---

# 🎯 Visión del Proyecto

Aula Robótica Platform nace como una plataforma moderna destinada a centralizar:

* coordinación de proyectos,
* gestión de tareas,
* actividades colaborativas,
* usuarios y permisos,
* trazabilidad,
* auditoría,
* notificaciones,
* sincronización realtime,
* operaciones administrativas educativas.

El objetivo del proyecto no fue únicamente desarrollar una aplicación CRUD tradicional, sino diseñar una arquitectura mantenible, escalable y preparada para entornos reales.

La plataforma prioriza especialmente:

* modularidad,
* seguridad,
* mantenibilidad,
* colaboración multiusuario,
* despliegue cloud,
* sincronización realtime,
* buenas prácticas backend,
* y aproximación DevOps.

---

# 🧠 Filosofía Arquitectónica

La plataforma sigue varios principios arquitectónicos fundamentales.

---

# 1. Arquitectura backend-first

El backend actúa como fuente principal de verdad del sistema.

Toda la lógica crítica se centraliza en servidor:

* autenticación,
* autorización,
* RBAC,
* ownership,
* auditoría,
* validaciones,
* sincronización realtime,
* control de permisos,
* lógica de negocio.

La interfaz cliente se considera una capa controlada y ligera.

---

# 2. Estrategia SSR-first

La plataforma utiliza una arquitectura basada en:

* FastAPI,
* Jinja2,
* AdminLTE,
* renderizado server-side.

En lugar de adoptar inicialmente una SPA completa, se priorizó:

* simplicidad arquitectónica,
* integración backend/frontend,
* mantenibilidad,
* rapidez de desarrollo,
* seguridad,
* renderizado contextual basado en permisos.

La arquitectura queda preparada para futura evolución hacia SPA desacoplada.

---

# 3. Arquitectura modular por dominios

El backend se organiza mediante dominios funcionales independientes.

Cada módulo encapsula:

* routers,
* servicios,
* modelos,
* validaciones,
* templates,
* lógica JavaScript,
* permisos,
* sincronización realtime.

---

## Principales dominios funcionales

* auth
* users
* identities
* roles
* permissions
* projects
* tasks
* activities
* notifications
* dashboard
* audit
* websocket
* realtime feeds

---

# 4. Colaboración realtime

La colaboración en tiempo real constituye una característica central del sistema.

La plataforma utiliza conexiones WebSocket persistentes para:

* sincronización Kanban,
* actividad reciente,
* usuarios conectados,
* notificaciones live,
* coordinación multiusuario,
* actualización dinámica de dashboard.

La lógica realtime se implementa mediante endpoints WebSocket y connection managers gestionados desde FastAPI.

---

# 5. Arquitectura preparada para cloud

La plataforma evolucionó desde un entorno puramente local hacia una arquitectura desplegada sobre infraestructura Linux real basada en:

* Docker,
* Docker Compose,
* Nginx Reverse Proxy,
* VPS Linux,
* MariaDB persistente,
* WebSockets,
* contenedores desacoplados,
* reverse proxy,
* persistencia Docker.

La infraestructura fue diseñada para aproximarse a escenarios productivos reales.

---

# 🏗️ Arquitectura Actual del Sistema

---

# Backend

## Tecnologías principales

* Python 3.13
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* WebSockets

---

# Frontend SSR

## Tecnologías principales

* Jinja2
* AdminLTE
* Bootstrap
* Chart.js
* JavaScript modular

---

# Persistencia

* MariaDB 11
* SQLAlchemy ORM
* modelo relacional

---

# Infraestructura

* Ubuntu Server 24.04
* Docker
* Docker Compose
* Nginx
* Hetzner Cloud VPS

---

# DevOps y Calidad

* GitHub Actions
* Ruff
* SonarCloud
* pytest
* pytest-cov
* validación despliegue
* logs Docker

---

# ☁️ Infraestructura Cloud

La plataforma se encuentra desplegada sobre infraestructura cloud Linux real.

---

# Entorno VPS

## Proveedor

Hetzner Cloud

---

## Sistema operativo

Ubuntu Server 24.04 LTS

---

# Características de infraestructura

* VPS Linux
* arquitectura multicontenedor
* servicios Dockerizados
* persistencia de datos
* reverse proxy
* soporte WebSockets
* snapshots cloud
* acceso SSH endurecido

---

# Arquitectura Docker

La plataforma se despliega mediante Docker Compose.

---

## Servicios principales

| Servicio | Responsabilidad                 |
| -------- | ------------------------------- |
| api      | Backend FastAPI                 |
| mariadb  | Persistencia relacional         |
| nginx    | Reverse Proxy y WebSocket proxy |

---

# Arquitectura Reverse Proxy

Nginx gestiona:

* entrada HTTP pública,
* proxy inverso,
* forwarding de peticiones,
* proxy WebSocket,
* aislamiento backend,
* preparación HTTPS futura.

---

# Persistencia

Los volúmenes Docker permiten persistencia de:

* MariaDB,
* uploads,
* logs,
* backups.

Esto permite reconstruir contenedores sin pérdida de datos.

---

# 🔐 Modelo de Seguridad

La seguridad constituye una preocupación arquitectónica central.

---

# Autenticación

La plataforma utiliza:

* JWT Authentication,
* cookies HTTPOnly,
* sesiones stateless,
* middleware de validación.

---

# Autorización

El sistema combina:

* RBAC,
* permisos contextuales,
* ownership,
* control granular de acceso,
* validación de recursos.

---

# Modelo IAM

La arquitectura IAM separa:

* usuarios,
* identidades,
* roles,
* permisos,
* proveedores.

Esto prepara el sistema para futura integración con:

* SAML,
* OAuth2,
* SSO institucional,
* identidad federada.

---

# Seguridad Infraestructura

Actualmente se implementan:

* autenticación SSH mediante claves,
* root deshabilitado,
* usuario administrativo dedicado,
* firewall,
* aislamiento Docker,
* backend protegido tras Nginx.

---

# ⚡ Sistema Realtime

La comunicación realtime se implementa mediante WebSockets gestionados por FastAPI.

---

# Características realtime actuales

* Kanban colaborativo,
* actividad reciente,
* notificaciones live,
* usuarios conectados,
* sincronización instantánea,
* colaboración multiusuario.

---

# Validación realtime

La sincronización realtime fue validada mediante:

* múltiples clientes simultáneos,
* DevTools navegador,
* verificación HTTP 101,
* logs Docker,
* sincronización live.

---

# 🧪 Calidad Software

La calidad software forma parte del flujo de desarrollo.

---

# Testing

La estrategia de testing incluye:

* pytest,
* cobertura,
* tests servicios,
* tests repositorios,
* tests API,
* validación despliegue.

---

# Calidad y análisis estático

El proyecto utiliza:

* Ruff,
* SonarCloud,
* linting,
* formatting,
* quality gates.

---

# CI/CD

GitHub Actions valida automáticamente:

* testing,
* cobertura,
* linting,
* calidad código,
* consistencia despliegue.

---

# 📈 Estado Actual del Proyecto

---

# Estado funcional

✅ Sistema autenticación operativo
✅ RBAC operativo
✅ Realtime operativo
✅ Kanban operativo
✅ Dashboard operativo
✅ Notificaciones operativas
✅ Auditoría operativa
✅ Actividad reciente operativa

---

# Estado infraestructura

✅ Docker desplegado
✅ Arquitectura multicontenedor operativa
✅ Reverse proxy operativo
✅ VPS Linux desplegado
✅ Persistencia validada
✅ WebSockets operativos
✅ Despliegue cloud validado

---

# 🚀 Visión a Largo Plazo

La arquitectura actual prepara el sistema para futura evolución hacia:

* HTTPS completo,
* integración SAML,
* SSO institucional,
* frontend SPA desacoplado,
* observabilidad,
* métricas centralizadas,
* Kubernetes,
* escalabilidad horizontal,
* evolución cloud-native.

---

# 📌 Posicionamiento Estratégico

Aula Robótica Platform no debe entenderse únicamente como una aplicación CRUD académica.

El proyecto evolucionó progresivamente hacia una plataforma backend colaborativa que integra:

* realtime,
* IAM avanzado,
* Docker,
* despliegue cloud,
* DevOps,
* reverse proxy,
* auditoría,
* WebSockets,
* arquitectura modular moderna,

manteniendo simultáneamente un enfoque educativo y colaborativo.
