# 01_PROJECT_OVERVIEW.md

# 🤖 Aula Robótica Platform — Visión General del Proyecto

---

# 📌 Introducción

Aula Robótica Platform es una plataforma colaborativa educativa desarrollada para la gestión integral de proyectos, tareas, usuarios y actividades dentro del Aula de Robótica de la Escuela Politécnica Superior de la Universidad de Alcalá.

El proyecto surge como respuesta a la necesidad de disponer de una herramienta moderna capaz de centralizar la coordinación de proyectos educativos y colaborativos en un entorno multiusuario, incorporando además capacidades realtime, trazabilidad, seguridad avanzada y despliegue cloud.

A lo largo de su evolución, el sistema pasó de ser una aplicación académica inicial basada en gestión IAM/RBAC a convertirse en una plataforma backend modular desplegada sobre infraestructura Linux real y preparada para futuros escenarios institucionales y cloud-native.

---

# 🎯 Objetivos del Proyecto

El proyecto persigue simultáneamente objetivos funcionales, arquitectónicos y tecnológicos.

---

# Objetivos funcionales

La plataforma permite:

* gestión de usuarios,
* gestión de identidades,
* gestión de roles y permisos,
* coordinación de proyectos,
* gestión de tareas,
* registro de actividades,
* notificaciones,
* dashboards administrativos,
* auditoría y trazabilidad,
* colaboración multiusuario.

---

# Objetivos técnicos

A nivel técnico, el proyecto busca demostrar:

* arquitectura backend modular,
* integración realtime mediante WebSockets,
* diseño IAM avanzado,
* despliegue cloud multicontenedor,
* integración DevOps,
* buenas prácticas de seguridad,
* testing automatizado,
* CI/CD,
* mantenibilidad y escalabilidad.

---

# 🏗️ Arquitectura General

La plataforma sigue una arquitectura backend moderna basada en FastAPI y renderizado SSR mediante Jinja2.

---

# Arquitectura principal

La aplicación se organiza en varias capas funcionales:

| Capa                 | Responsabilidad                          |
| -------------------- | ---------------------------------------- |
| Frontend SSR         | Renderizado visual e interacción usuario |
| FastAPI Backend      | Lógica negocio y APIs                    |
| Service Layer        | Reglas negocio y validaciones            |
| ORM Layer            | Persistencia mediante SQLAlchemy         |
| Database Layer       | MariaDB                                  |
| Realtime Layer       | WebSockets                               |
| Infrastructure Layer | Docker + Nginx + VPS                     |

---

# Arquitectura SSR

La interfaz utiliza:

* Jinja2,
* AdminLTE,
* Bootstrap,
* JavaScript modular.

Este enfoque permite:

* renderizado contextual,
* integración backend/frontend simplificada,
* menor complejidad frontend,
* mayor mantenibilidad,
* seguridad backend-first.

La arquitectura queda preparada para futura evolución hacia SPA desacoplada.

---

# Arquitectura modular

El backend se organiza mediante dominios funcionales independientes.

Cada dominio encapsula:

* routers,
* servicios,
* modelos,
* permisos,
* templates,
* validaciones,
* lógica realtime.

---

# Dominios funcionales principales

| Dominio       | Responsabilidad  |
| ------------- | ---------------- |
| auth          | autenticación    |
| users         | usuarios         |
| identities    | identidades      |
| roles         | roles y permisos |
| projects      | proyectos        |
| tasks         | tareas           |
| activities    | actividades      |
| notifications | notificaciones   |
| audit         | auditoría        |
| dashboard     | métricas         |
| websocket     | realtime         |

---

# ⚡ Sistema Realtime

Uno de los elementos diferenciales del proyecto es la integración de funcionalidades realtime mediante WebSockets.

La plataforma mantiene conexiones persistentes entre clientes y backend para sincronizar información en tiempo real.

---

# Funcionalidades realtime implementadas

Actualmente se utilizan WebSockets para:

* Kanban colaborativo,
* actividad reciente,
* usuarios conectados,
* notificaciones,
* sincronización instantánea,
* actualización dinámica de dashboard.

---

# Arquitectura realtime

La lógica realtime se implementa mediante:

* endpoints WebSocket FastAPI,
* connection managers,
* broadcasting,
* rooms por proyecto,
* sincronización multiusuario.

---

# 🔐 Seguridad e IAM

La seguridad constituye uno de los pilares arquitectónicos del sistema.

---

# Autenticación

La plataforma implementa:

* JWT Authentication,
* cookies HTTPOnly,
* middleware de sesión,
* validación backend,
* autenticación stateless.

---

# Autorización

El sistema combina:

* RBAC,
* permisos granulares,
* ownership,
* autorización contextual,
* validación por recurso.

---

# Modelo IAM

La arquitectura IAM separa:

* usuarios,
* identidades,
* roles,
* permisos,
* proveedores.

Este diseño deja preparada la plataforma para futura integración con:

* SAML,
* OAuth2,
* SSO institucional,
* identidad federada.

---

# 🗄️ Persistencia y Modelo de Datos

La plataforma utiliza MariaDB como sistema de persistencia principal.

La persistencia se gestiona mediante:

* SQLAlchemy ORM,
* relaciones relacionales,
* modelos desacoplados,
* validaciones backend.

---

# Principales entidades

| Entidad       | Función                   |
| ------------- | ------------------------- |
| users         | usuarios sistema          |
| identities    | identidades autenticación |
| roles         | roles globales            |
| permissions   | permisos                  |
| projects      | proyectos                 |
| tasks         | tareas Kanban             |
| activities    | actividades               |
| notifications | notificaciones            |
| audit_logs    | auditoría                 |

---

# ☁️ Infraestructura Cloud y DevOps

La plataforma se encuentra desplegada sobre infraestructura Linux real.

---

# Entorno cloud actual

| Elemento          | Tecnología          |
| ----------------- | ------------------- |
| Cloud Provider    | Hetzner Cloud       |
| Sistema operativo | Ubuntu Server 24.04 |
| Backend           | FastAPI             |
| Persistencia      | MariaDB 11          |
| Reverse Proxy     | Nginx               |
| Contenedores      | Docker Compose      |

---

# Arquitectura multicontenedor

La infraestructura se organiza mediante Docker Compose separando:

* backend,
* base de datos,
* reverse proxy.

Esto permite:

* aislamiento,
* mantenibilidad,
* persistencia,
* despliegue reproducible,
* aproximación productiva.

---

# Reverse Proxy

Nginx actúa como:

* reverse proxy HTTP,
* proxy WebSocket,
* capa de aislamiento backend,
* punto de entrada público.

---

# Persistencia Docker

La infraestructura utiliza volúmenes persistentes para:

* MariaDB,
* uploads,
* logs,
* backups.

---

# Seguridad Infraestructura

Se implementaron medidas como:

* acceso SSH mediante claves,
* deshabilitación root,
* firewall,
* aislamiento contenedores,
* backend protegido tras Nginx.

---

# 🧪 Calidad Software

La calidad software forma parte activa del proyecto.

---

# Testing

El sistema incorpora:

* pytest,
* tests backend,
* validación API,
* validación despliegue,
* validación WebSockets.

---

# Calidad código

La plataforma utiliza:

* Ruff,
* SonarCloud,
* coverage,
* linting,
* quality gates.

---

# CI/CD

GitHub Actions automatiza:

* testing,
* coverage,
* análisis calidad,
* validación pipeline.

---

# 📈 Estado Actual

Actualmente la plataforma dispone de:

✅ Arquitectura modular funcional
✅ IAM avanzado operativo
✅ WebSockets operativos
✅ Kanban realtime funcional
✅ Auditoría operativa
✅ Notificaciones operativas
✅ Dashboard operativo
✅ Despliegue cloud funcional
✅ Docker Compose operativo
✅ Reverse proxy Nginx operativo

---

# 🚀 Evolución Futura

La arquitectura actual deja preparada la plataforma para futuras mejoras:

* HTTPS completo,
* SAML institucional,
* SPA desacoplada,
* observabilidad,
* métricas avanzadas,
* monitorización,
* Kubernetes,
* escalabilidad horizontal,
* evolución cloud-native.

---

# 📌 Conclusión

Aula Robótica Platform evolucionó progresivamente desde un sistema académico inicial hacia una plataforma backend colaborativa moderna capaz de integrar:

* realtime,
* IAM avanzado,
* WebSockets,
* Docker,
* despliegue cloud,
* DevOps,
* auditoría,
* sincronización multiusuario,
* arquitectura modular,
* y seguridad backend-first.

El proyecto demuestra la viabilidad de construir una plataforma educativa moderna utilizando tecnologías backend actuales y aproximaciones arquitectónicas cercanas a entornos reales.
