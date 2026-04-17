# SECURITY_MODEL.md

# Modelo de seguridad

La seguridad es un eje central del proyecto.

---

# Autenticación

Sistema basado en credenciales + JWT.

## Login actual

- email
- password

## Verificación

- password hash con bcrypt
- búsqueda de identidad
- validación de usuario activo

---

# Tokens

## Access Token

Contiene:

- sub
- username
- roles
- permissions
- exp

## Refresh Token

Usado para renovación de sesión futura.

---

# Transporte de tokens

Los tokens se almacenan en cookies seguras.

## Ventajas

- no localStorage
- menor exposición a XSS
- integración natural con server-side rendering

---

# Autorización

Sistema híbrido RBAC + permisos granulares.

---

# Roles actuales

- admin

(Estructura preparada para nuevos roles)

---

# Permisos actuales

## Users

- users:read
- users:create
- users:update
- users:delete

## Roles

- roles:read
- roles:create
- roles:update
- roles:delete

## Identities

- identities:read
- identities:create
- identities:update
- identities:delete

## Otros

- dashboard:read
- students:read
- audit:read

---

# Capas de protección

## Backend

- dependencias FastAPI
- guards de permisos
- ownership checks
- middleware JWT

## Frontend

- ocultación de botones
- ocultación de menús
- navegación contextual

> La seguridad real siempre reside en backend.

---

# Auditoría

Se registran acciones críticas:

- login
- logout
- create
- update
- delete

---

# Riesgos mitigados

## XSS

Mitigado evitando localStorage.

## Acceso no autorizado

Mitigado con permisos.

## Elevación de privilegios

Mitigado con RBAC centralizado.

## Trazabilidad

Mitigado con logs de auditoría.

---

# Mejoras futuras

- CSRF tokens
- Rate limiting
- Refresh rotation
- Revocación de sesiones
- 2FA
- OAuth2
- SSO
- Alertas de seguridad
- Logs externos (SIEM)