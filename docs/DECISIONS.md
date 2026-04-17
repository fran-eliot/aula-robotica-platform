# DECISIONS.md

# Decisiones técnicas del proyecto

Este documento recoge las principales decisiones arquitectónicas y técnicas tomadas durante el desarrollo de Aula Robótica Platform.

Su objetivo es dejar trazabilidad técnica, justificar elecciones y facilitar futuras evoluciones.

---

# DEC-001 — Uso de FastAPI como framework principal

## Decisión

Se adopta FastAPI como base del backend.

## Motivos

- Alto rendimiento ASGI
- Tipado moderno con Python
- Integración nativa con Pydantic
- Documentación automática
- Excelente sistema de dependencias
- Curva de aprendizaje razonable

## Alternativas valoradas

- Flask
- Django
- Spring Boot

## Trade-off

FastAPI ofrece gran flexibilidad, aunque requiere definir más estructura manualmente que Django.

---

# DEC-002 — SQLAlchemy ORM frente a consultas SQL directas

## Decisión

Persistencia gestionada con SQLAlchemy ORM.

## Motivos

- Modelado relacional claro
- Relaciones entre entidades
- Reutilización de consultas
- Menor acoplamiento con motor DB
- Buen estándar profesional en Python

## Trade-off

Mayor complejidad inicial que SQL puro, pero mejor mantenibilidad.

---

# DEC-003 — MariaDB como base de datos relacional

## Decisión

Uso de MariaDB/MySQL compatible.

## Motivos

- Robustez
- Familiaridad académica/profesional
- Excelente integración con SQLAlchemy
- Buen rendimiento
- Fácil despliegue

## Futuro

Migrable a PostgreSQL si el proyecto escala.

---

# DEC-004 — Arquitectura modular por dominios

## Decisión

Separación por módulos funcionales:

- auth
- users
- roles
- identities
- dashboard
- students

## Motivos

- Escalabilidad
- Navegabilidad del código
- Bajo acoplamiento
- Facilita testing
- Permite trabajo por dominios

---

# DEC-005 — Separación Usuario / Identidad

## Decisión

Usuario e identidad son entidades distintas.

## Usuario representa

La persona dentro del sistema.

## Identidad representa

La credencial de acceso:

- email
- password
- provider externo

## Ventajas

- Múltiples logins por usuario
- OAuth futuro
- Modelo más realista

---

# DEC-006 — JWT en cookies HTTPOnly

## Decisión

Tokens almacenados en cookies seguras.

## Motivos

- Evitar localStorage
- Menor exposición a XSS
- Mejor integración con render server-side
- Gestión transparente de sesión

## Trade-off

Requiere estrategia CSRF futura.

---

# DEC-007 — Access Token + Refresh Token

## Decisión

Separación entre token corto y token renovable.

## Ventajas

- Mejor seguridad
- Sesiones más cómodas
- Base preparada para renovación automática

---

# DEC-008 — RBAC + permisos granulares

## Decisión

Sistema híbrido:

- Roles
- Permissions

## Ejemplo

Admin → users:create

## Motivos

- Escalabilidad
- Flexibilidad
- Seguridad realista

---

# DEC-009 — Seguridad también en frontend (UX)

## Decisión

Ocultar botones, menús y acciones no permitidas.

## Importante

La seguridad real se valida siempre en backend.

## Beneficio

- Mejor UX
- Menos ruido visual
- Navegación limpia

---

# DEC-010 — Render server-side con Jinja2

## Decisión

Frontend administrativo basado en plantillas.

## Motivos

- Rapidez de desarrollo
- Menor complejidad que SPA
- Ideal para panel interno
- SEO irrelevante
- Menos JavaScript necesario

## Trade-off

Menor interactividad avanzada.

---

# DEC-011 — Componentización de plantillas

## Decisión

Macros reutilizables:

- tablas
- botones
- formularios
- layouts
- badges
- tabs

## Beneficios

- DRY
- Consistencia visual
- Mantenimiento más simple

---

# DEC-012 — Auditoría centralizada

## Decisión

Registrar acciones críticas en tabla independiente.

## Motivos

- Seguridad
- Trazabilidad
- Soporte
- Diagnóstico

---

# DEC-013 — Menú dinámico por permisos

## Decisión

El menú lateral se genera según permisos efectivos.

## Beneficios

- UX limpia
- Menor confusión
- Escalable

---

# DEC-014 — Preparado para crecimiento futuro

## Decisión

Diseño pensando en futuros módulos:

- estudiantes
- cursos
- competiciones
- proyectos
- equipos

---

# Resumen estratégico

El proyecto prioriza:

1. Seguridad
2. Mantenibilidad
3. Escalabilidad
4. Claridad arquitectónica
5. Realismo profesional