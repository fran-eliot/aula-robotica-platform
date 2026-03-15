# DATABASE_SCHEMA.md

## Entidades principales

Usuarios
- id_usuario
- nombre
- activo
- fecha_creacion

Identidades
- id_identidad
- email
- password_hash
- provider
- user_id
- rol_id

Roles
- id_rol
- nombre

AuditLogs
- id_log
- user_id
- action
- description
- ip_address
- user_agent
- created_at

## Relaciones

Usuario 1 — N Identidades
Identidad N — 1 Rol
Usuario 1 — N AuditLogs