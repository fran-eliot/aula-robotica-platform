# RBAC_MODEL.md

# Modelo RBAC

El sistema usa Role-Based Access Control combinado con permisos específicos.

## Estructura

Usuario → Roles → Permisos

## Ejemplo

Admin:
- users:create
- users:update
- roles:delete
- dashboard:read

## Ventajas

- Fácil administración
- Escalable
- Seguro
- Flexible

## Evolución futura

Roles previstos:

- profesor
- estudiante
- coordinador
- gestor