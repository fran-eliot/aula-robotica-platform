# 02_TECH_STACK.md

# ⚙️ Aula Robótica Platform — Stack Tecnológico

---

# 📌 Introducción

Aula Robótica Platform utiliza un stack tecnológico moderno orientado al desarrollo backend modular, colaboración realtime y despliegue cloud multicontenedor.

La selección tecnológica se realizó priorizando:

* mantenibilidad,
* modularidad,
* rendimiento,
* simplicidad arquitectónica,
* seguridad,
* capacidad realtime,
* y aproximación a entornos productivos reales.

El stack combina tecnologías backend modernas, renderizado SSR, sincronización WebSocket, despliegue Docker y herramientas DevOps orientadas a calidad software y despliegue cloud.

---

# 🧠 Filosofía Tecnológica

La arquitectura tecnológica del proyecto sigue varios principios fundamentales:

* Backend-first architecture
* SSR-first rendering
* Modular domain-driven structure
* Realtime collaboration
* Cloud-ready deployment
* DevOps-oriented infrastructure
* Seguridad backend-centralizada
* Despliegue reproducible

---

# 🐍 Backend Principal

El núcleo de la plataforma está desarrollado en Python utilizando FastAPI como framework principal.

---

# Python 3.13

## Uso principal

Lenguaje base de toda la plataforma.

## Motivos de selección

* Sintaxis clara y mantenible
* Excelente ecosistema backend
* Alto soporte para asincronía
* Integración natural con FastAPI
* Gran productividad de desarrollo

## Uso dentro del proyecto

* Backend completo
* Lógica negocio
* WebSockets
* Servicios
* Persistencia
* Middleware
* IAM

---

# FastAPI

## Rol

Framework backend principal.

## Responsabilidades

* APIs REST
* Renderizado SSR
* Endpoints WebSocket
* Middleware
* Dependency Injection
* Validación automática

## Motivos de selección

* Alto rendimiento ASGI
* Excelente soporte async
* Integración WebSocket
* Documentación automática OpenAPI
* Tipado moderno
* Arquitectura modular

## Uso en el proyecto

* Gestión IAM
* Gestión proyectos
* Gestión tareas
* Dashboard
* Auditoría
* Notificaciones
* Realtime

---

# Uvicorn

## Rol

Servidor ASGI principal.

## Responsabilidades

* ejecución FastAPI
* conexiones HTTP
* conexiones WebSocket
* soporte asincronía

## Motivos de selección

* Alto rendimiento
* Compatibilidad ASGI
* Integración FastAPI
* Soporte realtime

---

# 🧩 Arquitectura Frontend SSR

La interfaz sigue una arquitectura SSR (Server-Side Rendering).

---

# Jinja2

## Rol

Motor de templates principal.

## Responsabilidades

* renderizado HTML
* templates reutilizables
* macros
* layouts
* rendering contextual

## Motivos de selección

* Integración FastAPI
* Simplicidad
* Flexibilidad
* Renderizado backend-first

## Uso dentro del proyecto

* Dashboard
* Kanban
* Gestión usuarios
* Actividades
* Auditoría
* Notificaciones

---

# AdminLTE

## Rol

Framework visual administrativo.

## Responsabilidades

* estructura visual
* componentes UI
* dashboards
* cards
* tablas
* navegación lateral

## Motivos de selección

* Diseño enterprise-style
* Componentes administrativos
* Responsive
* Integración Bootstrap

---

# Bootstrap

## Rol

Framework CSS principal.

## Responsabilidades

* grid system
* responsive layout
* componentes visuales
* formularios

---

# JavaScript

## Uso principal

* interacción cliente
* integración realtime
* WebSockets
* actualización dinámica DOM
* gráficos
* eventos UI

---

# Chart.js

## Rol

Biblioteca gráficos dashboard.

## Uso actual

* productividad
* métricas tareas
* actividad dashboard

---

# ⚡ Realtime Stack

La plataforma incorpora sincronización realtime multiusuario mediante WebSockets.

---

# FastAPI WebSockets

## Responsabilidades

* conexiones persistentes
* sincronización realtime
* broadcasting
* rooms
* eventos live

## Funcionalidades implementadas

* Kanban colaborativo
* actividad reciente
* notificaciones
* usuarios conectados
* dashboard dinámico

---

# Arquitectura realtime

La lógica realtime se implementa mediante:

* WebSocket endpoints
* connection managers
* broadcasting
* eventos servidor
* sincronización frontend

---

# 🗄️ Persistencia y Base de Datos

---

# MariaDB 11

## Rol

Base de datos principal.

## Responsabilidades

* persistencia usuarios
* proyectos
* tareas
* actividades
* auditoría
* notificaciones

## Motivos de selección

* motor relacional robusto
* compatibilidad MySQL
* integridad relacional
* facilidad despliegue Docker

---

# SQLAlchemy

## Rol

ORM principal.

## Responsabilidades

* modelos relacionales
* relaciones ORM
* queries
* persistencia
* abstracción SQL

## Motivos de selección

* integración FastAPI
* mantenibilidad
* separación lógica SQL
* tipado Python

---

# PyMySQL

## Rol

Driver conexión MariaDB/MySQL.

---

# 🔐 Seguridad e IAM

La seguridad constituye una parte central de la arquitectura.

---

# JWT

## Uso principal

Autenticación stateless.

## Responsabilidades

* tokens autenticación
* sesiones backend
* validación usuarios

---

# Cookies HTTPOnly

## Uso principal

Almacenamiento seguro de sesión.

## Beneficios

* mitigación parcial XSS
* integración SSR
* sesiones transparentes

---

# RBAC Contextual

## Responsabilidades

* roles
* permisos
* ownership
* autorización granular

## Implementación

* middleware auth
* validación backend
* permisos contextuales

---

# Middleware de Seguridad

## Funciones principales

* validación sesión
* autorización
* protección endpoints
* control acceso

---

# ☁️ Infraestructura Cloud y DevOps

La plataforma evolucionó hacia una infraestructura cloud moderna desplegada sobre Linux real.

---

# Hetzner Cloud

## Rol

Proveedor cloud VPS.

## Uso actual

* despliegue producción-like
* hosting plataforma
* snapshots
* networking

## Motivos de selección

* buena relación coste/rendimiento
* VPS Linux flexible
* control infraestructura

---

# Ubuntu Server 24.04

## Rol

Sistema operativo servidor.

## Responsabilidades

* infraestructura Linux
* ejecución Docker
* networking
* seguridad
* despliegue

---

# Docker

## Rol

Contenerización aplicación.

## Responsabilidades

* aislamiento servicios
* reproducibilidad
* despliegue consistente

## Uso actual

* API FastAPI
* MariaDB
* Nginx

---

# Docker Compose

## Rol

Orquestación multicontenedor.

## Responsabilidades

* coordinación servicios
* redes Docker
* persistencia
* despliegue completo

## Arquitectura actual

| Servicio | Función         |
| -------- | --------------- |
| api      | backend FastAPI |
| mariadb  | persistencia    |
| nginx    | reverse proxy   |

---

# Nginx

## Rol

Reverse Proxy principal.

## Responsabilidades

* entrada HTTP pública
* forwarding backend
* proxy WebSocket
* aislamiento infraestructura
* preparación HTTPS

## Motivos de selección

* alto rendimiento
* estándar industria
* integración WebSockets
* arquitectura productiva

---

# Persistencia Docker

## Uso actual

Persistencia mediante volúmenes Docker para:

* MariaDB
* uploads
* logs
* backups

---

# Firewall y Hardening

## Medidas implementadas

* SSH mediante claves
* root deshabilitado
* firewall Linux
* aislamiento backend
* separación contenedores

---

# 🧪 Calidad Software

La calidad software forma parte activa del flujo desarrollo.

---

# pytest

## Rol

Framework testing principal.

## Uso actual

* tests backend
* tests servicios
* tests repositorios
* validación API

---

# pytest-cov

## Rol

Cobertura código.

## Estado actual

Cobertura aproximada:

* ≈ 75%

---

# Ruff

## Rol

Linting y análisis estático.

## Responsabilidades

* calidad código
* formato
* detección problemas

---

# SonarCloud

## Rol

Análisis calidad software.

## Uso actual

* quality gates
* maintainability
* code smells
* coverage

---

# 🔄 CI/CD

---

# GitHub Actions

## Rol

Pipeline automatización principal.

## Validaciones actuales

* testing
* coverage
* linting
* SonarCloud
* validación despliegue

---

# 📊 Observabilidad y Logging

Actualmente el proyecto utiliza:

* logs Docker
* logs FastAPI
* logs WebSocket
* validación runtime

La arquitectura queda preparada para futura evolución hacia:

* observabilidad avanzada,
* métricas centralizadas,
* monitoring,
* tracing.

---

# 🚀 Estado Tecnológico Actual

Actualmente la plataforma dispone de:

✅ Backend modular FastAPI
✅ Renderizado SSR operativo
✅ WebSockets realtime operativos
✅ MariaDB persistente
✅ Docker deployment funcional
✅ Reverse proxy Nginx operativo
✅ VPS Linux desplegado
✅ CI/CD automatizado
✅ Calidad software integrada

---

# 🔮 Evolución Tecnológica Futura

La arquitectura actual prepara el sistema para futura evolución hacia:

* HTTPS completo
* SAML institucional
* SPA desacoplada
* observabilidad avanzada
* Kubernetes
* cloud-native scaling
* monitorización avanzada
* métricas centralizadas

---

# 📌 Conclusión

El stack tecnológico seleccionado permitió evolucionar Aula Robótica Platform desde un entorno académico inicial hacia una plataforma backend moderna capaz de integrar:

* realtime,
* IAM avanzado,
* Docker,
* despliegue cloud,
* WebSockets,
* DevOps,
* reverse proxy,
* arquitectura modular,
* y colaboración multiusuario.

La combinación de tecnologías backend modernas, infraestructura Linux real y despliegue multicontenedor aproxima la plataforma a arquitecturas utilizadas habitualmente en entornos profesionales reales.
