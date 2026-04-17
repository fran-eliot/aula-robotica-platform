# Aula Robótica Platform

Plataforma web modular para la gestión de usuarios, identidades, permisos y futuros procesos académicos del **Aula de Robótica de la Escuela Politécnica Superior (Universidad de Alcalá)**.

El sistema nace como una solución administrativa real orientada a centralizar autenticación, autorización, operaciones internas y futura gestión de estudiantes, actividades y competiciones como **Eurobot Spain**.

Desarrollado como **Proyecto Final del CFGS en Desarrollo de Aplicaciones Multiplataforma (DAM)**, con enfoque profesional en arquitectura backend, seguridad y escalabilidad.

---

# Tabla de contenidos

- Visión general
- Objetivos
- Estado actual del proyecto
- Funcionalidades implementadas
- Stack tecnológico
- Arquitectura
- Estructura del proyecto
- Modelo de datos
- Seguridad
- Sistema RBAC
- Auditoría
- Frontend administrativo
- Decisiones de diseño
- Trade-offs
- Roadmap y fases futuras
- Instalación y ejecución
- Capturas sugeridas
- Autor

---

# Visión general

Aula Robótica Platform no es solo un CRUD de usuarios.

Es una base sólida para una plataforma interna donde distintos perfiles (administradores, profesorado, personal de gestión, estudiantes) puedan operar bajo reglas de acceso seguras y trazables.

Actualmente el foco está en el **núcleo administrativo y de seguridad**, dejando preparada la plataforma para crecer con nuevos módulos funcionales.

---

# Objetivos del proyecto

## Objetivo principal

Construir una plataforma robusta, mantenible y escalable para la gestión interna del Aula de Robótica.

## Objetivos específicos

- Centralizar usuarios e identidades
- Implementar autenticación segura
- Aplicar autorización granular por permisos
- Disponer de panel web administrativo
- Registrar acciones relevantes del sistema
- Facilitar ampliaciones futuras
- Practicar arquitectura real de software
- Consolidar competencias DAM full stack/backend

---

# Estado actual del proyecto

## Núcleo funcional completado

### Administración

- Gestión de usuarios
- Gestión de roles
- Gestión de identidades
- Dashboard administrativo
- Menú dinámico por permisos

### Seguridad

- Login con JWT
- Access Token + Refresh Token
- Cookies HTTPOnly
- Middleware de autenticación
- Protección de rutas web

### Infraestructura UI

- Plantillas reutilizables
- Componentes Jinja2
- Layout responsive con AdminLTE
- Flash messages
- Tablas reutilizables
- Formularios reutilizables

### Base técnica

- Arquitectura modular
- SQLAlchemy ORM
- MariaDB
- Separación por capas

---

# Funcionalidades implementadas

---

# 1. Autenticación

Sistema de login basado en credenciales.

## Flujo actual

- Usuario introduce email + contraseña
- Se valida identidad
- Se generan tokens
- Se almacenan en cookies seguras
- Se redirige al dashboard

## Tokens utilizados

### Access Token

Incluye:

- user id
- username
- roles
- permissions
- expiración

### Refresh Token

Permite renovación futura de sesión sin relogin completo.

---

# 2. Autorización

El sistema aplica control de acceso en backend y frontend.

## Verificaciones disponibles

- acceso a rutas
- acciones CRUD
- visibilidad de botones
- visibilidad de menús
- ownership de recursos
- permisos granulares

---

# 3. Gestión de Usuarios

Módulo completamente operativo.

## Incluye

- listado paginado
- detalle de usuario
- edición
- creación
- activación / desactivación
- eliminación
- visualización de roles
- visualización de permisos efectivos
- auditoría asociada

---

# 4. Gestión de Roles

Módulo completamente operativo.

## Incluye

- listado
- detalle
- creación
- edición
- eliminación
- asignación de permisos
- visualización agrupada por módulos

---

# 5. Gestión de Identidades

Separación entre persona y credenciales de acceso.

## Incluye

- listado
- creación
- edición
- eliminación
- asociación a usuario
- proveedor de autenticación

## Ventaja conceptual

Un usuario puede tener múltiples identidades:

- login local
- Google OAuth
- GitHub OAuth
- SSO corporativo

---

# 6. Dashboard

Panel inicial del sistema con métricas y accesos rápidos.

## Ejemplos

- total usuarios
- usuarios activos
- roles definidos
- actividad reciente
- accesos directos

---

# 7. Auditoría

Registro centralizado de acciones sensibles.

## Eventos registrados

- login
- logout