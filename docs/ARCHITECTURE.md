# ARCHITECTURE.md

# Arquitectura del sistema

Aula Robótica Platform sigue una arquitectura modular por capas orientada a mantenibilidad, escalabilidad y separación clara de responsabilidades.

---

# Visión general

```text
Cliente Web
   │
   ▼
Presentation Layer
(Jinja2 + AdminLTE)

   │
   ▼
Application Layer
(FastAPI Routers)

   │
   ▼
Domain / Service Layer
(Lógica de negocio)

   │
   ▼
Persistence Layer
(SQLAlchemy ORM)

   │
   ▼
MariaDB
```
---

# Arquitectura del Sistema

## 1. Presentation Layer (Capa de Presentación)
Responsable de la interfaz administrativa renderizada en servidor.

### Tecnologías
* **Jinja2**
* **AdminLTE**
* **Bootstrap**
* **JavaScript ligero**

### Responsabilidades
* Renderizado HTML
* Componentes reutilizables
* Menús dinámicos
* Formularios
* Tablas
* Feedback visual
* Navegación

---

## 2. Application Layer (Capa de Aplicación)
Expone funcionalidades mediante routers FastAPI.

### Incluye
* Endpoints web
* Endpoints REST
* Dependencias
* Validaciones de acceso
* Redirecciones
* Flash messages

### Módulos actuales
* `auth`
* `dashboard`
* `users`
* `roles`
* `identities`
* `students` (base inicial)

---

## 3. Domain / Service Layer (Capa de Dominio / Servicio)
Contiene lógica de negocio desacoplada del transporte HTTP.

### Ejemplos
* Creación de usuarios
* Asignación de roles
* Cálculo de permisos efectivos
* Auditoría
* Validaciones funcionales

---

## 4. Persistence Layer (Capa de Persistencia)
Abstracción de acceso a datos mediante ORM.

### Componentes
* **SQLAlchemy models**
* Session management
* Queries
* Relaciones

---

## 5. Security Layer (Capa de Seguridad)
Transversal a todas las capas.

### Componentes
* JWT tokens
* Password hashing
* Middleware auth
* RBAC (Role-Based Access Control)
* Policies
* Permission guards

---

## Estructura Modular
```text
app/
├── core/
│   ├── security/
│   ├── middleware/
│   ├── templates/
│   ├── constants/
│   └── authorization/
│
├── modules/
│   ├── auth/
│   ├── users/
│   ├── roles/
│   ├── identities/
│   ├── dashboard/
│   └── students/
│
├── db/
│   ├── base.py
│   └── session.py
│
├── templates/
├── static/
└── main.py
```
---

## Principios Aplicados

* **Separación de responsabilidades**: Cada módulo gestiona su propio dominio.
* **Reutilización**: Macros Jinja2, helpers y componentes compartidos.
* **Seguridad por diseño**: Autorización centralizada y rutas protegidas.
* **Escalabilidad**: Preparado para nuevos módulos sin romper existentes.
* **Mantenibilidad**: Código organizado y fácilmente navegable.

---

## Flujo típico de petición

**Usuario** → **Router** → **Dependency Auth** → **Service** → **ORM** → **DB** *Resultado:* **Template Render**

---

## Próximas evoluciones arquitectónicas

- [ ] API pública versionada
- [ ] Frontend SPA desacoplado
- [ ] Tests automatizados
- [ ] Dockerización
- [ ] CI/CD
- [ ] Microservicios futuros (si escala)
