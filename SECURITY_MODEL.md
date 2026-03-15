# SECURITY_MODEL.md

## Autenticación

- bcrypt para hashing de contraseñas
- JWT para autenticación
- Cookies HTTP-only

## Autorización

Sistema RBAC con tres roles:

Administrador
Profesor
Estudiante

## Seguridad implementada

- hashing seguro
- expiración de tokens
- endpoints protegidos
- registro de auditoría

## Próximas mejoras

- auditoría automática mediante middleware
- rate limiting
- protección CSRF