# 51_CODING_RULES.md

# Aula Robótica Platform — Coding Rules

## Parte 1 — Principios, arquitectura del código, Python, FastAPI, SQLAlchemy, Pydantic y persistencia

---

# 1. Propósito

Este documento define las reglas de desarrollo de **Aula Robótica Platform**.

Su objetivo es mantener una base de código:

- consistente;
- legible;
- mantenible;
- segura;
- modular;
- testeable;
- reutilizable;
- observable;
- extensible;
- alineada con la arquitectura SSR de la plataforma.

---

# 2. Alcance

Estas reglas aplican a:

```text
Python

FastAPI

SQLAlchemy

Pydantic

Jinja2

HTML

CSS

JavaScript

WebSockets

Testing

Database

Security

Observability

Documentation
```

---

# 3. Naturaleza de las reglas

Este documento define convenciones de implementación.

No sustituye a:

```text
Architecture documentation

Architectural Decision Records

Testing Strategy

Security documentation

Observability documentation
```

---

# 4. Relación documental

```text
Architecture
    ↓
Architectural Decisions
    ↓
Coding Rules
    ↓
Implementation
    ↓
Static Analysis + Tests
```

---

# 5. Objetivo principal

El código debe permitir que otro desarrollador pueda responder fácilmente:

```text
What does this code do?

Why is it here?

Which layer owns this behavior?

How is it validated?

How can it be safely changed?
```

---

# 6. Coding Principle

```text
Optimize for understanding

before optimizing for cleverness.
```

---

# 7. Regla de claridad

Preferir:

```text
explicit code

clear naming

small abstractions

predictable control flow
```

frente a:

```text
clever code

hidden behavior

premature abstractions

implicit side effects
```

---

# 8. Regla de consistencia

Cuando existan varias soluciones técnicamente válidas:

```text
prefer the solution already established by the project
```

siempre que siga siendo adecuada.

---

# 9. Consistency over Personal Preference

No introducir una convención diferente únicamente por preferencia personal.

---

# 10. Excepción

Una convención existente puede cambiar cuando:

- produce errores;
- aumenta deuda técnica;
- dificulta testing;
- perjudica seguridad;
- contradice una decisión arquitectónica;
- existe una alternativa claramente superior.

---

# 11. Cambio de convención

Un cambio transversal debe hacerse:

```text
intentionally

consistently

incrementally

documented when necessary
```

---

# 12. Simplicidad

La implementación más simple que satisface correctamente los requisitos debe ser la opción inicial.

---

# 13. Simplicity Principle

```text
Do not build complexity for requirements that do not exist.
```

---

# 14. YAGNI

Aplicar:

```text
You Aren't Gonna Need It
```

cuando una abstracción solo intenta anticipar necesidades hipotéticas.

---

# 15. YAGNI Guardrail

YAGNI no significa ignorar extensibilidad conocida.

---

# 16. Ejemplo

Si existe una necesidad explícita de migrar almacenamiento:

```text
storage abstraction
```

puede estar justificada.

No implica que también debamos construir anticipadamente:

```text
multi-cloud replication

distributed storage orchestration

complex provider routing
```

---

# 17. DRY

Evitar duplicación significativa.

---

# 18. DRY Principle

```text
Duplicate knowledge is more dangerous than duplicate syntax.
```

---

# 19. Duplicación candidata a extracción

Puede consolidarse mediante:

- services;
- helpers;
- policies;
- macros;
- partials;
- row components;
- JavaScript utilities;
- shared validation;
- reusable UI components.

---

# 20. DRY Guardrail

No extraer automáticamente dos fragmentos únicamente porque parecen similares.

---

# 21. Premature Abstraction

Evitar crear:

```text
generic universal helper

base service for everything

generic repository abstraction

mega component
```

sin una necesidad real.

---

# 22. Rule of Three

Como heurística:

```text
first occurrence → implement

second occurrence → observe

third occurrence → consider abstraction
```

---

# 23. Rule of Three Guardrail

No es una regla matemática.

Una abstracción puede justificarse antes si representa una política crítica.

---

# 24. Separation of Concerns

Cada capa debe mantener una responsabilidad claramente delimitada.

---

# 25. Capas principales

| Capa | Responsabilidad principal |
|---|---|
| Router | Entrada HTTP y construcción de respuesta |
| Service | Casos de uso y lógica de negocio |
| Model | Persistencia y relaciones |
| Schema | Validación y contratos de datos |
| Policy / Authorization | Reglas reutilizables de acceso |
| Template | Presentación SSR |
| JavaScript | Interacción y comportamiento cliente |
| WebSocket | Transporte realtime |
| Infrastructure | Integraciones técnicas externas |

---

# 26. Regla fundamental

```text
Business logic does not belong in presentation code.
```

---

# 27. Dependency Direction

Las dependencias deben avanzar hacia componentes con responsabilidades claras.

---

# 28. Flujo conceptual

```text
HTTP / UI
    ↓
Router
    ↓
Service
    ↓
Domain / Persistence
```

---

# 29. Presentation Boundary

Templates y JavaScript no deben convertirse en fuentes autoritativas de reglas de negocio.

---

# 30. Persistence Boundary

Los modelos ORM no deben absorber indiscriminadamente lógica de aplicación.

---

# 31. Router Boundary

Los routers no deben convertirse en services.

---

# 32. Service Boundary

Los services no deben convertirse en:

```text
HTTP-aware controllers

HTML renderers

global utility containers
```

---

# 33. Side Effects

Los side effects deben ser:

```text
intentional

localized

traceable
```

---

# 34. Ejemplos de side effects

```text
database writes

file storage

notification creation

realtime emission

audit event creation

email delivery
```

---

# 35. Side Effect Rule

Una función aparentemente de lectura no debe producir side effects inesperados.

---

# 36. Principle of Least Surprise

El comportamiento de una función debe corresponder con:

```text
its name

its layer

its contract
```

---

# 37. Cohesion

Cada módulo debe agrupar comportamiento relacionado.

---

# 38. High Cohesion

Preferir:

```text
projects/
tasks/
activities/
notifications/
```

frente a organizar toda la aplicación únicamente por tipo técnico.

---

# 39. Modularidad por dominio

Cada dominio principal debe vivir en su módulo.

---

# 40. Estructura conceptual

```text
modules/
├── users/
├── roles/
├── identities/
├── projects/
├── tasks/
├── activities/
├── attachments/
├── notifications/
├── dashboard/
└── audit/
```

---

# 41. Evolución modular

La estructura puede crecer con dominios futuros como:

```text
students/

courses/

inventory/

reservations/

competitions/
```

cuando formen parte real del producto.

---

# 42. Module Ownership

Cada módulo debe ser propietario de sus reglas principales.

---

# 43. Contenido típico de módulo

Según necesidad:

```text
model

service

router / web

schemas

policies

templates

static assets

tests
```

---

# 44. Module Guardrail

No todos los módulos necesitan obligatoriamente todos esos elementos.

---

# 45. Avoid Empty Architecture

No crear:

```text
service.py

schemas.py

policies.py
```

vacíos únicamente para cumplir una estructura teórica.

---

# 46. Cross-module Dependencies

Las dependencias entre módulos deben ser explícitas.

---

# 47. Cross-module Rule

Evitar acceder directamente a internals de otro módulo cuando existe una interfaz pública adecuada.

---

# 48. Circular Dependencies

No introducir dependencias circulares entre módulos.

---

# 49. Circular Dependency Signal

Una dependencia circular puede indicar:

```text
incorrect ownership

missing abstraction

mixed responsibilities
```

---

# 50. Shared Code

El código compartido debe representar comportamiento realmente transversal.

---

# 51. Shared Guardrail

No mover código a `shared`, `common` o `utils` simplemente porque no sabemos dónde colocarlo.

---

# 52. Utils Smell

Un directorio:

```text
utils/
```

que crece continuamente puede indicar pérdida de ownership.

---

# 53. Better Question

Antes de crear un helper global:

```text
Which domain actually owns this behavior?
```

---

# 54. General Naming Principle

Los nombres deben expresar intención.

---

# 55. Naming Goals

Un nombre debe ayudar a entender:

```text
what

not how
```

---

# 56. Variables

Utilizar `snake_case`.

---

# 57. Ejemplos

```python
user_id
project_id
task_id
activity_id
current_user
project_members
uploaded_file
```

---

# 58. Avoid Generic Variables

Evitar cuando exista alternativa más precisa:

```python
data
item
obj
thing
tmp
x
```

---

# 59. Contextual Exception

`data` puede ser válido cuando el contexto ya define claramente qué representa.

---

# 60. Boolean Naming

Los booleanos deben expresar una condición.

---

# 61. Ejemplos

```python
is_active
is_owner
has_permission
can_update
should_notify
```

---

# 62. Avoid Negative Boolean Complexity

Preferir:

```python
is_active
```

frente a:

```python
is_not_inactive
```

---

# 63. Function Naming

Las funciones deben utilizar verbos.

---

# 64. Ejemplos

```python
create_user()
assign_task()
upload_attachment()
mark_notification_as_read()
get_project_members()
```

---

# 65. Query Naming

Para lectura:

```text
get_

find_

list_

search_
```

según semántica.

---

# 66. `get_`

Utilizar cuando se espera una entidad concreta.

---

# 67. `find_`

Puede utilizarse cuando la ausencia es un resultado normal.

---

# 68. `list_`

Utilizar para colecciones.

---

# 69. `search_`

Utilizar cuando existen filtros o criterios de búsqueda.

---

# 70. Mutation Naming

Para operaciones que cambian estado:

```text
create_

update_

delete_

assign_

remove_

mark_

archive_

restore_
```

---

# 71. Naming Side Effects

Una función con side effects debe sugerirlos mediante su nombre.

---

# 72. Class Naming

Utilizar `PascalCase`.

---

# 73. Ejemplos

```python
ProjectService
ActivityAttachment
NotificationService
ProjectMembership
```

---

# 74. Constant Naming

Utilizar:

```python
UPPER_SNAKE_CASE
```

---

# 75. Ejemplo

```python
MAX_ATTACHMENT_SIZE
DEFAULT_PAGE_SIZE
SUPPORTED_IMAGE_TYPES
```

---

# 76. Python Style

El código Python debe seguir convenciones idiomáticas y mantener compatibilidad con las herramientas configuradas en el proyecto.

---

# 77. Formatting

El formato debe ser consistente y automatizable.

---

# 78. Static Analysis

El proyecto utiliza:

```text
Ruff

SonarCloud
```

para reforzar calidad y consistencia.

---

# 79. Static Analysis Principle

```text
Treat analysis findings as engineering feedback

not as a score to game.
```

---

# 80. Static Analysis Guardrail

No degradar diseño o legibilidad únicamente para eliminar una métrica.

---

# 81. Quality Gate

Los findings deben:

```text
fix

justify

or intentionally accept
```

según contexto.

---

# 82. Ignoring Rules

No añadir exclusiones generales sin comprender el finding.

---

# 83. Suppression Rule

Una supresión local debe ser:

```text
minimal

intentional

justifiable
```

---

# 84. Dead Code

Eliminar código no utilizado.

---

# 85. Commented-out Code

No mantener bloques antiguos comentados.

---

# 86. Source Control Principle

```text
Git preserves old code.

The source file does not need to.
```

---

# 87. Imports

Los imports deben ser:

```text
necessary

clear

free of unused symbols
```

---

# 88. Wildcard Imports

No utilizar:

```python
from module import *
```

---

# 89. Import Side Effects

Evitar módulos cuya importación produzca efectos inesperados.

---

# 90. Functions

Las funciones deben tener una responsabilidad comprensible.

---

# 91. Function Size

No existe un límite rígido de líneas.

---

# 92. Function Smell

Considerar extracción cuando una función:

- mezcla varios niveles de abstracción;
- realiza varias responsabilidades;
- requiere comentarios para separar fases;
- tiene demasiadas ramas;
- resulta difícil de testear.

---

# 93. Small Function Principle

```text
Small enough to understand as one unit.
```

---

# 94. Parameters

Evitar funciones con un número excesivo de parámetros relacionados.

---

# 95. Parameter Smell

Ejemplo problemático:

```python
create_task(
    title,
    description,
    project_id,
    assigned_to,
    status,
    priority,
    due_date,
    created_by,
    ...
)
```

---

# 96. Better Contract

Cuando represente un contrato coherente:

```python
create_task(db, task_data, current_user)
```

---

# 97. Parameter Object Guardrail

No encapsular parámetros arbitrariamente si reduce claridad.

---

# 98. Return Values

Las funciones deben devolver resultados coherentes.

---

# 99. Mixed Return Smell

Evitar contratos como:

```python
User | False | str | None
```

---

# 100. Explicit Contracts

Preferir tipos y comportamientos predecibles.

---

# 101. Type Hints

El código Python nuevo debe utilizar type hints cuando aporten claridad.

---

# 102. Type Hint Principle

Especialmente en:

```text
public functions

services

helpers

complex data structures
```

---

# 103. Type Hint Guardrail

No crear anotaciones extremadamente complejas que dificulten más la lectura que el propio código.

---

# 104. `Any`

Evitar `Any` cuando existe un tipo razonablemente conocido.

---

# 105. Optional Values

La posibilidad de `None` debe ser explícita.

---

# 106. Example

```python
def find_project(project_id: int) -> Project | None:
    ...
```

---

# 107. Mutable Defaults

No utilizar valores mutables como defaults.

---

# 108. Incorrect

```python
def add_items(items=[]):
    ...
```

---

# 109. Correct

```python
def add_items(items=None):
    if items is None:
        items = []
```

---

# 110. Exceptions

Las excepciones deben representar condiciones excepcionales o errores del dominio/aplicación.

---

# 111. Exception Principle

No utilizar excepciones como flujo normal innecesario.

---

# 112. Broad Exception Handling

Evitar:

```python
except Exception:
    pass
```

---

# 113. Silent Failure

Nunca ocultar errores relevantes silenciosamente.

---

# 114. Better Handling

Capturar:

```text
the narrowest meaningful exception
```

---

# 115. Error Context

Cuando se propague o transforme un error debe conservarse contexto suficiente para diagnosticarlo.

---

# 116. Error Logging

No registrar el mismo error repetidamente en cada capa.

---

# 117. Logging Ownership

Preferir que el error se registre en el punto donde exista suficiente contexto operativo.

---

# 118. Comments

Los comentarios deben explicar:

```text
why
```

cuando el código no pueda expresarlo suficientemente.

---

# 119. Avoid Obvious Comments

No:

```python
# Increment counter
counter += 1
```

---

# 120. Useful Comment

Puede explicar:

```text
business constraint

external limitation

non-obvious compatibility reason
```

---

# 121. Comment Drift

Los comentarios incorrectos son peores que la ausencia de comentarios.

---

# 122. TODOs

Los TODOs deben ser accionables.

---

# 123. Weak TODO

```python
# TODO improve
```

---

# 124. Better TODO

```python
# TODO: Replace process-local event delivery when horizontal scaling is introduced.
```

---

# 125. TODO Guardrail

Trabajo significativo pendiente debería vivir también en el sistema de backlog cuando corresponda.

---

# 126. Docstrings

Utilizar docstrings cuando ayuden a comprender:

```text
public service behavior

non-obvious contracts

complex helpers

integration boundaries
```

---

# 127. Docstring Guardrail

No escribir docstrings que únicamente repitan el nombre de la función.

---

# 128. FastAPI

FastAPI representa la capa de entrada HTTP de la aplicación.

---

# 129. Router Principle

```text
Routers should orchestrate HTTP.

Services should orchestrate business behavior.
```

---

# 130. Router Responsibilities

Un router puede:

- recibir la request;
- resolver dependencies;
- leer path/query/form parameters;
- validar el contrato de entrada;
- obtener el usuario autenticado;
- invocar services;
- mapear resultados a responses;
- preparar contexto mínimo de template;
- realizar redirects.

---

# 131. Router Non-responsibilities

Un router no debería contener:

- reglas de negocio complejas;
- queries extensas;
- lógica de ownership duplicada;
- transacciones complejas;
- reglas de autorización dispersas;
- cálculos de dominio;
- lógica de auditoría manual repetida.

---

# 132. Correct Router Example

```python
@router.post("/users")
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    user_service.create_user(db, data)

    return RedirectResponse(
        url="/users",
        status_code=303,
    )
```

---

# 133. Router Smell

Ejemplo conceptual:

```text
router

→ query database

→ inspect roles

→ inspect project membership

→ validate business rule

→ create entity

→ create audit event

→ send notification

→ broadcast websocket

→ render response
```

---

# 134. Better

```text
router

→ service

→ response
```

---

# 135. Dependency Injection

Utilizar FastAPI dependencies para concerns de request apropiados.

---

# 136. Candidate Dependencies

```text
database session

authenticated user

request-scoped context

common parameter validation
```

---

# 137. Dependency Guardrail

No esconder lógica de negocio compleja dentro de dependencies.

---

# 138. Authentication Dependency

La resolución del usuario autenticado puede formar parte de una dependency.

---

# 139. Authorization Dependency

Puede utilizarse para reglas globales simples.

---

# 140. Contextual Authorization

Las reglas dependientes de una entidad concreta suelen necesitar validación contextual dentro del flujo de aplicación.

---

# 141. Example

```text
Global:
user has projects:update

Contextual:
user can update this specific project
```

---

# 142. HTTP Semantics

Las rutas deben respetar semántica HTTP razonable.

---

# 143. GET

Debe utilizarse para lectura.

---

# 144. GET Side Effects

No realizar mutaciones de dominio mediante GET.

---

# 145. POST

Puede utilizarse para:

```text
creation

commands

SSR form mutations
```

---

# 146. PUT / PATCH

En API pueden utilizarse para actualización según contrato definido.

---

# 147. DELETE

En APIs puede representar eliminación.

---

# 148. SSR Forms

Cuando las limitaciones HTML lo requieran, una acción de eliminación puede utilizar POST mediante una ruta explícita.

---

# 149. Redirect after POST

En flujos SSR, preferir:

```text
POST

↓

Redirect

↓

GET
```

---

# 150. PRG Pattern

Esto reduce:

```text
duplicate form submission

refresh ambiguity
```

---

# 151. Redirect Status

Para redirects posteriores a mutaciones:

```text
303 See Other
```

es la opción preferida cuando corresponda.

---

# 152. Route Naming

Las rutas deben ser consistentes y predecibles.

---

# 153. Convención Web

```text
/resource

/resource/form

/resource/{id}

/resource/{id}/edit

/resource/{id}/delete
```

---

# 154. Convención API

```text
/api/resource

/api/resource/{id}
```

---

# 155. Fixed Routes

Definir rutas fijas antes de rutas dinámicas cuando puedan colisionar.

---

# 156. Correct

```text
/activities/form

/activities/{activity_id}
```

---

# 157. Route Parameters

Los nombres deben expresar la entidad.

---

# 158. Prefer

```python
/project/{project_id}
/task/{task_id}
```

frente a un genérico:

```python
/resource/{id}
```

en código interno donde la precisión ayude.

---

# 159. Status Codes

Los códigos HTTP deben reflejar el resultado real.

---

# 160. Error Mapping

No convertir indiscriminadamente todos los errores en:

```text
500 Internal Server Error
```

---

# 161. Expected Errors

Ejemplos:

```text
400 → invalid request semantics

401 → unauthenticated

403 → authenticated but unauthorized

404 → resource not found

409 → conflicting state

422 → validation error
```

---

# 162. Status Code Guardrail

La semántica exacta debe mantenerse consistente con los contratos existentes de la plataforma.

---

# 163. HTTP Exceptions

La capa HTTP puede transformar errores conocidos de aplicación en respuestas apropiadas.

---

# 164. Domain Independence

Los services no deberían necesitar conocer:

```text
HTTPException

RedirectResponse

TemplateResponse
```

---

# 165. Request Objects

Evitar pasar `Request` profundamente por services salvo que exista una razón arquitectónica explícita.

---

# 166. Request Context

Extraer la información realmente necesaria.

---

# 167. Service Layer

Los services contienen comportamiento de aplicación y dominio.

---

# 168. Service Responsibilities

Pueden incluir:

- lógica de negocio;
- validaciones funcionales;
- autorización contextual;
- coordinación de persistencia;
- transacciones;
- auditoría;
- creación de notificaciones;
- coordinación de eventos;
- integración con infraestructura.

---

# 169. Business Rule Principle

```text
If a rule matters to the business,

it must not exist only in the router or UI.
```

---

# 170. Service Example

```python
def update_task(
    db: Session,
    task: Task,
    data: TaskUpdate,
    actor: User,
) -> Task:
    ensure_can_update_task(actor, task)

    apply_task_changes(task, data)
    register_task_activity(db, task, actor)

    db.commit()
    db.refresh(task)

    return task
```

---

# 171. Service Design

Un service debe representar:

```text
meaningful application behavior
```

no únicamente envolver una línea ORM sin aportar semántica.

---

# 172. Thin Service Guardrail

No crear wrappers triviales solo para afirmar que existe una service layer.

---

# 173. Service Granularity

Preferir operaciones orientadas a casos de uso.

---

# 174. Example

Preferir:

```python
assign_task(...)
```

frente a:

```python
set_task_assigned_to(...)
```

cuando la asignación implica reglas adicionales.

---

# 175. Service Side Effects

Los side effects deben coordinarse conscientemente.

---

# 176. Example

Una actualización de Task puede requerir:

```text
update entity

create activity

create notification

emit realtime event
```

---

# 177. Transaction Boundary

Las operaciones que forman una única unidad lógica deben compartir una estrategia transaccional coherente.

---

# 178. Partial Mutation Risk

Evitar:

```text
Task updated

but

Activity creation failed

and

transaction already committed
```

si ambos forman una misma operación lógica.

---

# 179. Commit Ownership

Debe existir una convención consistente sobre qué capa controla `commit()`.

---

# 180. Recommended Rule

Para operaciones de aplicación:

```text
service owns the transaction boundary
```

salvo excepción documentada.

---

# 181. Commit Guardrail

Evitar múltiples commits intermedios innecesarios dentro del mismo caso de uso.

---

# 182. Flush

Utilizar `flush()` cuando sea necesario obtener cambios persistidos dentro de la transacción sin cerrarla.

---

# 183. Rollback

Los errores transaccionales deben permitir rollback coherente.

---

# 184. Service Reusability

Un service bien diseñado puede ser reutilizado desde:

```text
SSR route

API route

background process

future CLI
```

sin depender de detalles HTTP.

---

# 185. Service Return Values

Debe devolver:

```text
domain/application result
```

no HTML o respuestas HTTP.

---

# 186. Service Error Model

Los errores esperados pueden representarse mediante excepciones específicas de aplicación.

---

# 187. Example

```python
class ProjectAccessDeniedError(Exception):
    pass
```

---

# 188. Exception Granularity

No crear una jerarquía enorme sin necesidad.

---

# 189. Authorization Policies

Las reglas de autorización reutilizables pueden encapsularse en:

```text
policies

authorization helpers

service guards
```

---

# 190. Authorization Naming

Ejemplos:

```python
can_update_project(...)
can_delete_activity(...)
ensure_project_access(...)
ensure_task_owner(...)
```

---

# 191. `can_*`

Debe responder una condición.

---

# 192. `ensure_*`

Puede lanzar un error cuando la condición requerida no se cumple.

---

# 193. Example

```python
if can_update_project(user, project):
    ...
```

frente a:

```python
ensure_can_update_project(user, project)
```

según necesidad.

---

# 194. Authorization Duplication

No repetir manualmente:

```text
role check

+

membership check

+

ownership check
```

en múltiples routers.

---

# 195. SQLAlchemy Models

Los modelos representan persistencia y relaciones.

---

# 196. Model Principle

```text
Models describe persisted state.

Services coordinate application behavior.
```

---

# 197. Model Responsibilities

Pueden incluir:

- columnas;
- constraints;
- relaciones;
- metadata ORM;
- invariantes locales simples;
- representación del estado persistido.

---

# 198. Model Non-responsibilities

Evitar cargar modelos con:

- lógica HTTP;
- rendering;
- request context;
- envío de notificaciones;
- WebSocket broadcasting;
- coordinación compleja entre módulos.

---

# 199. One Main Entity per Model

Mantener una entidad principal claramente identificable por modelo.

---

# 200. Relationship Explicitness

Las relaciones deben ser explícitas.

---

# 201. Relationship Example

```python
project = relationship(
    "Project",
    back_populates="tasks",
)
```

---

# 202. `back_populates`

Preferir `back_populates` cuando haga explícita la relación bidireccional.

---

# 203. Foreign Keys

Las Foreign Keys deben seguir naming consistente.

---

# 204. Python Attribute Example

```python
project_id = Column(
    Integer,
    ForeignKey("projects.id"),
    nullable=False,
)
```

---

# 205. Legacy Schema Compatibility

Si el esquema existente utiliza nombres como:

```python
ForeignKey("usuarios.id_usuario")
```

debe mantenerse compatibilidad mientras ese naming siga siendo parte real del modelo de datos.

---

# 206. FK Naming Principle

A nivel de código Python:

```text
<entity>_id
```

es la convención preferida.

---

# 207. Relationships and IDs

Cuando sea útil pueden coexistir:

```python
project_id
project
```

---

# 208. Cascades

Las cascadas deben configurarse conscientemente.

---

# 209. Cascade Risk

No utilizar:

```text
delete cascade
```

sin comprender el impacto sobre entidades relacionadas.

---

# 210. Ownership Relationships

El ownership debe representarse explícitamente cuando forma parte del dominio.

---

# 211. Example

```text
Activity

→ created_by / owner

Attachment

→ uploader
```

según el modelo concreto.

---

# 212. Model Defaults

Los defaults deben ser:

```text
deterministic

appropriate to domain semantics
```

---

# 213. Timestamp Defaults

Los timestamps deben seguir una política temporal consistente.

---

# 214. Timezone Principle

Preferir timestamps conscientes de zona horaria cuando el stack y esquema lo permitan.

---

# 215. Time Source

Evitar dispersar múltiples estrategias temporales por el código.

---

# 216. Temporal Consistency

El proyecto debe utilizar una convención común para:

```text
created_at

updated_at

completed_at

read_at
```

---

# 217. Database Naming

La base de datos debe mantener naming consistente.

---

# 218. Tables

Convención preferida:

```text
plural
```

---

# 219. Columns

Utilizar:

```text
snake_case
```

---

# 220. Foreign Keys

Utilizar:

```text
<entity>_id
```

cuando el esquema no esté condicionado por naming legacy.

---

# 221. Primary Keys

Mantener una estrategia consistente.

---

# 222. Naming Migration Guardrail

No renombrar tablas o columnas existentes únicamente por estética si el coste de migración no está justificado.

---

# 223. Database Constraints

Las invariantes que puedan protegerse de forma fiable en base de datos deben considerarse para constraints.

---

# 224. Candidate Constraints

```text
NOT NULL

UNIQUE

FOREIGN KEY

CHECK
```

según soporte y necesidad.

---

# 225. Application Validation ≠ Integrity Constraint

La validación en application layer no siempre sustituye integridad en DB.

---

# 226. Example

Una regla:

```text
a project membership cannot be duplicated
```

puede requerir:

```text
application validation

+

UNIQUE constraint
```

---

# 227. Race Conditions

La base de datos debe proteger invariantes que puedan romperse por concurrencia.

---

# 228. Example

```text
check if reservation exists

then insert
```

sin constraint/transacción adecuada puede fallar bajo concurrencia.

---

# 229. Relationship Patterns

| Relación | Implementación típica |
|---|---|
| 1:N | Foreign Key |
| N:M | Tabla intermedia |
| Ownership | FK explícita |
| Membership | Tabla relacional |
| Context | Relación explícita |

---

# 230. Many-to-Many

Las relaciones N:M con metadata propia deben modelarse como entidades asociativas explícitas.

---

# 231. Example

Si Project Membership contiene:

```text
role

joined_at

status
```

no debería tratarse únicamente como una tabla técnica invisible.

---

# 232. Data Duplication

No duplicar información sin una razón concreta.

---

# 233. Denormalization

Puede utilizarse cuando exista:

```text
measured performance need

read-model requirement

explicit architectural decision
```

---

# 234. Denormalization Guardrail

No desnormalizar por intuición prematura.

---

# 235. Database Business Logic

Evitar lógica de negocio compleja escondida en la base de datos.

---

# 236. Database Enforcement

Esto no impide utilizar:

```text
constraints

indexes

foreign keys
```

para integridad.

---

# 237. Query Placement

Queries específicas del caso de uso deben mantenerse fuera de routers y templates.

---

# 238. Query Complexity

Una query compleja merece:

```text
clear ownership

meaningful name

tests when behavior is important
```

---

# 239. N+1 Queries

Evitar patrones N+1 en vistas y servicios.

---

# 240. Relationship Loading

Elegir estrategia de carga según caso de uso.

---

# 241. Loading Guardrail

No convertir todas las relaciones en eager loading global.

---

# 242. Query Performance Principle

```text
Load what the use case needs.

Not everything the entity can reach.
```

---

# 243. Pagination

Las colecciones potencialmente grandes deben considerar paginación.

---

# 244. Pagination Candidates

```text
activities

notifications

audit events

projects

tasks

future inventory history
```

según volumen real.

---

# 245. Unbounded Query

Evitar consultas sin límite sobre colecciones con crecimiento indefinido.

---

# 246. Ordering

Las colecciones visibles deben tener ordering determinista.

---

# 247. Example

```text
created_at DESC

+

id DESC
```

cuando sea necesario resolver empates.

---

# 248. Indexes

Los índices deben responder a patrones de consulta reales.

---

# 249. Index Candidates

```text
foreign keys

frequent filters

frequent ordering

unique business keys
```

---

# 250. Index Guardrail

No indexar cada columna.

---

# 251. Migration Discipline

Los cambios de esquema deben realizarse mediante el mecanismo de migrations adoptado por el proyecto.

---

# 252. Migration Principle

```text
Schema evolution must be reproducible.
```

---

# 253. Manual Schema Changes

Evitar cambios manuales no reproducibles en entornos compartidos.

---

# 254. Migration Review

Una migration debe revisarse por:

```text
data loss

locking

defaults

nullability

rollback implications
```

---

# 255. Destructive Migration

Debe tratarse con especial cuidado.

---

# 256. Destructive Examples

```text
DROP COLUMN

DROP TABLE

irreversible data conversion
```

---

# 257. Additive-first Strategy

Cuando sea viable:

```text
add

↓

migrate

↓

switch

↓

remove later
```

---

# 258. Migration and Deployment

Los cambios de schema deben ser compatibles con la estrategia real de despliegue.

---

# 259. Pydantic Schemas

Los schemas representan contratos de datos y validación.

---

# 260. Schema Principle

```text
Validate at boundaries.

Do not expose persistence accidentally.
```

---

# 261. Input / Output Separation

Separar schemas de entrada y salida cuando tengan responsabilidades diferentes.

---

# 262. Example

```python
class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
```

---

# 263. Input Schema

Debe aceptar únicamente datos que el cliente puede controlar.

---

# 264. Sensitive Fields

No permitir que un cliente establezca directamente campos como:

```text
created_by

owner_id

internal_status

audit metadata
```

si deben derivarse del contexto.

---

# 265. Mass Assignment

Evitar patrones donde todos los campos recibidos se copien automáticamente al ORM sin control.

---

# 266. Incorrect Concept

```python
for key, value in payload.items():
    setattr(model, key, value)
```

cuando `payload` no está estrictamente controlado.

---

# 267. Better

Utilizar:

```text
validated schema

+

explicit allowed fields
```

---

# 268. Validation Types

Distinguir:

```text
structural validation

business validation
```

---

# 269. Structural Validation

Pertenece principalmente al schema.

---

# 270. Examples

```text
required field

string length

format

enum

basic numeric range
```

---

# 271. Business Validation

Pertenece al service/domain.

---

# 272. Examples

```text
user belongs to project

task can transition to status

reservation does not conflict

activity can be modified by actor
```

---

# 273. Schema Guardrail

No intentar trasladar todas las reglas de negocio a validators Pydantic.

---

# 274. Validation Error Quality

Los errores deben ser suficientemente claros para:

```text
API clients

SSR forms

developers
```

---

# 275. Output Schemas

No exponer campos internos innecesarios.

---

# 276. ORM Exposure

Evitar devolver modelos SQLAlchemy directamente como contrato público sin una decisión consciente.

---

# 277. API Stability

Los schemas públicos forman parte del contrato API.

---

# 278. Schema Change

Un cambio incompatible debe tratarse como modificación contractual.

---

# 279. Enums

Utilizar enums cuando el conjunto de valores sea cerrado y significativo.

---

# 280. Enum Example

```python
class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
```

---

# 281. Enum Guardrail

No utilizar enums para conjuntos realmente dinámicos administrados por usuarios.

---

# 282. Validation Normalization

La normalización debe ser predecible.

---

# 283. Example

Puede ser razonable:

```text
trim surrounding whitespace
```

---

# 284. Dangerous Normalization

Evitar modificar silenciosamente datos cuando pueda cambiar su significado.

---

# 285. IDs from Client

Nunca asumir que un ID válido sintácticamente implica acceso autorizado.

---

# 286. Example

```text
project_id = 5
```

debe validar:

```text
exists

+

actor can access project 5
```

---

# 287. Resource Lookup

Las búsquedas de recursos deben diferenciar correctamente:

```text
not found

unauthorized
```

según la política de seguridad adoptada.

---

# 288. Information Disclosure

En algunos contextos puede ser apropiado no revelar la existencia de un recurso no autorizado.

---

# 289. Authorization Policy Consistency

La decisión debe aplicarse consistentemente.

---

# 290. Data Integrity Principle

```text
Invalid state should be difficult to represent

and harder to persist.
```

---

# 291. Application + Database

Las reglas críticas pueden necesitar defensa en varias capas.

---

# 292. Example

```text
Schema:
valid input

Service:
valid business transition

Database:
valid persistent invariant
```

---

# 293. Layered Validation

Esto no es duplicación accidental cuando cada capa protege una responsabilidad diferente.

---

# 294. Transaction Example

```text
Create Activity

↓

Persist Activity

↓

Persist Attachments metadata

↓

Create Audit Event

↓

Commit
```

cuando esas operaciones formen una única unidad lógica.

---

# 295. External Side Effects

Los efectos externos requieren especial cuidado alrededor de transacciones.

---

# 296. Example

```text
database commit

+

WebSocket broadcast
```

no poseen atomicidad automática.

---

# 297. Side-effect Ordering

Debe definirse qué ocurre si:

```text
DB succeeds

but

realtime delivery fails
```

---

# 298. Realtime Principle

La persistencia autoritativa no debe depender de que el broadcast realtime tenga éxito.

---

# 299. Source of Truth

Para estado de negocio:

```text
database

is authoritative
```

salvo decisión arquitectónica diferente.

---

# 300. Event Failure

Un fallo de notificación o broadcast no debe dejar el dominio en un estado parcialmente persistido sin una política explícita.

---

# 301. Idempotency

Las operaciones susceptibles de repetición deben considerar idempotencia.

---

# 302. Candidate Cases

```text
retryable requests

background jobs

event processing

reconnect workflows
```

---

# 303. Idempotency Guardrail

No introducir mecanismos complejos de idempotencia donde no exista riesgo real.

---

# 304. Concurrency

Las operaciones concurrentes deben considerar:

```text
race conditions

lost updates

duplicate creation

conflicting transitions
```

---

# 305. Concurrency Protection

Puede requerir:

```text
database constraints

transactions

locking

version checks
```

según el caso.

---

# 306. Concurrency Example

Reservas futuras deberán evitar:

```text
two concurrent requests

→ both see availability

→ both reserve same resource
```

---

# 307. Database Session

La sesión SQLAlchemy debe tener un lifecycle controlado.

---

# 308. Request Lifecycle

En HTTP:

```text
request

↓

database dependency

↓

service operation

↓

commit / rollback

↓

session cleanup
```

---

# 309. Session Leakage

No conservar sesiones request-scoped fuera de su lifecycle.

---

# 310. Lazy Loading Guardrail

Evitar depender accidentalmente de lazy loading después de cerrar la sesión.

---

# 311. Serialization

Los datos requeridos para response/render deben estar disponibles dentro del lifecycle adecuado.

---

# 312. Bulk Operations

Las operaciones masivas deben evaluar:

```text
memory

transaction size

authorization

auditability
```

---

# 313. Bulk Authorization

Una acción bulk no debe saltarse autorización individual/contextual cuando sea necesaria.

---

# 314. Bulk Error Policy

Debe definirse si una operación es:

```text
all-or-nothing

or

partial success
```

---

# 315. Auditability

Las operaciones relevantes deben permitir reconstruir:

```text
who

did what

to which resource

when
```

según los requisitos de auditoría.

---

# 316. Audit vs Application Logs

No confundir:

```text
audit event

with

debug/application log
```

---

# 317. Audit Event

Representa una acción relevante de negocio o seguridad.

---

# 318. Application Log

Representa información operativa para diagnóstico.

---

# 319. Audit Data

Debe ser:

```text
structured

minimal

relevant

protected
```

---

# 320. Sensitive Data

No almacenar datos sensibles en auditoría si no son necesarios.

---

# 321. Repository Pattern

No introducir un repository layer genérico automáticamente.

---

# 322. Repository Adoption

Puede justificarse si:

```text
query complexity grows

persistence needs isolation

multiple implementations exist

testing benefits materially
```

---

# 323. Current Principle

Mientras SQLAlchemy pueda utilizarse claramente desde services/query helpers:

```text
avoid abstraction for abstraction's sake
```

---

# 324. Generic CRUD Repository

Evitar patrones universales que oculten semántica de dominio.

---

# 325. Example

Preferir:

```python
list_accessible_projects(...)
```

frente a:

```python
generic_repository.find_all(...)
```

cuando el primer nombre expresa una regla real.

---

# 326. Domain Queries

Las queries importantes deben tener nombres de intención.

---

# 327. Examples

```python
list_user_projects(...)
list_project_tasks(...)
find_activity_with_access(...)
list_unread_notifications(...)
```

---

# 328. Query Security

Una query contextual puede incorporar scope de acceso cuando sea apropiado.

---

# 329. Defense in Depth

Aun así, el service debe mantener responsabilidad sobre la autorización del caso de uso.

---

# 330. Data Access Optimization

No optimizar queries antes de medir o identificar un problema real.

---

# 331. Performance Smells

Sí deben investigarse:

```text
N+1

unbounded queries

repeated identical queries

large unnecessary payloads

missing indexes
```

---

# 332. Caching

No introducir caching sin:

```text
clear performance need

invalidation strategy

ownership
```

---

# 333. Cache Principle

```text
Every cache creates another state consistency problem.
```

---

# 334. Cache Invalidation

Debe definirse antes de adoptar el cache.

---

# 335. Database as Source of Truth

El cache nunca debe convertirse accidentalmente en una fuente divergente del estado persistido.

---

# 336. Backend Definition of Quality

El código backend debe ser:

```text
explicit

transactionally coherent

authorization-aware

testable

observable

predictable
```

---

# 337. Backend Review Questions

Antes de aceptar una implementación:

```text
Is this logic in the correct layer?

Is authorization enforced server-side?

Can invalid state be persisted?

Is the transaction boundary clear?

Are side effects intentional?

Can this behavior be tested?

Can failures be diagnosed?
```

---

# 338. Database Review Questions

```text
Are relationships explicit?

Are constraints protecting important invariants?

Can concurrency break the rule?

Is the query bounded?

Is ordering deterministic?

Does the migration preserve data?
```

---

# 339. Schema Review Questions

```text
Does the client control only allowed fields?

Are input and output responsibilities separated?

Is this structural validation or business validation?

Are internal fields exposed?

Does the schema preserve API compatibility?
```

---

# 340. Part 1 Summary

Esta primera parte establece las reglas para:

```text
general engineering principles

separation of concerns

modularity

DRY / YAGNI

Python conventions

naming

FastAPI routers

service layer

authorization boundaries

SQLAlchemy models

database design

transactions

Pydantic schemas

validation

data integrity

query design

concurrency

auditability
```

---

# 341. Continuation

La **Parte 2/3** continúa con:

```text
Security

Authentication

Authorization

RBAC

Contextual Policies

Jinja2

SSR Templates

Reusable UI

Forms

Flash Messages

Toasts

Confirm Dialogs

JavaScript

DOM

Progressive Enhancement

Frontend State

Accessibility
```

---

# 51_CODING_RULES.md

# Aula Robótica Platform — Coding Rules

## Parte 2 — Security, Authentication, Authorization, Jinja2, SSR, Forms, JavaScript, UX y Accessibility

---

# 342. Security as a Coding Concern

La seguridad forma parte de la implementación diaria.

No debe tratarse únicamente como:

```text
deployment concern

or

final review step
```

---

# 343. Security Principle

```text
Every input is untrusted until validated.

Every action is unauthorized until allowed.
```

---

# 344. Security Layers

La implementación debe considerar:

```text
Authentication

Authorization

Validation

Output Encoding

Session Security

CSRF

File Security

Realtime Security

Audit
```

---

# 345. Defense in Depth

Las capas de seguridad deben complementarse.

---

# 346. Example

Para una actualización de Task:

```text
UI

→ hides unavailable action

HTTP

→ authenticates request

Service

→ validates contextual authorization

Schema

→ validates structure

Database

→ preserves integrity
```

---

# 347. UI Security Limitation

La UI nunca debe considerarse una frontera de seguridad.

---

# 348. Hidden Button Rule

Esto:

```html
{% if can_delete %}
    <button>Delete</button>
{% endif %}
```

mejora UX.

No sustituye:

```text
server-side authorization
```

---

# 349. Trust Boundary

El navegador pertenece al lado no confiable del sistema.

---

# 350. Client Manipulation

Debe asumirse que un usuario puede:

- modificar HTML;
- modificar JavaScript;
- enviar requests manuales;
- cambiar IDs;
- repetir requests;
- omitir campos;
- añadir campos;
- manipular WebSocket messages.

---

# 351. Server Enforcement

Toda regla crítica debe aplicarse en servidor.

---

# 352. Authentication

La autenticación responde:

```text
Who is the actor?
```

---

# 353. Authorization

La autorización responde:

```text
Can this actor perform this action on this resource?
```

---

# 354. Authentication ≠ Authorization

Un usuario autenticado no tiene automáticamente acceso a todos los recursos.

---

# 355. Authentication Boundary

La identidad debe resolverse de forma consistente antes de ejecutar comportamiento protegido.

---

# 356. Current User

Preferir nombres explícitos:

```python
current_user
actor
```

según contexto.

---

# 357. Actor Naming

`actor` resulta especialmente útil en servicios y auditoría.

---

# 358. Authentication Failures

Los fallos deben mapearse de forma consistente.

---

# 359. Unauthenticated Request

Debe producir el comportamiento definido por la arquitectura:

```text
redirect to login
```

para flujo SSR,

o:

```text
401
```

para API cuando corresponda.

---

# 360. Session Tokens

Los tokens de autenticación deben tratarse como secretos.

---

# 361. Token Logging

Nunca registrar:

```text
access token

refresh token

Authorization header

session cookie
```

---

# 362. Token Storage

La estrategia adoptada por la plataforma debe preservarse de forma consistente.

---

# 363. HTTPOnly Cookies

Cuando se utilicen cookies para tokens sensibles:

```text
HttpOnly
```

debe mantenerse.

---

# 364. Secure Cookie

En producción sobre HTTPS:

```text
Secure
```

debe utilizarse según configuración.

---

# 365. SameSite

Debe establecerse conscientemente según el flujo real de autenticación.

---

# 366. Cookie Configuration

La configuración de cookies no debe quedar dispersa en múltiples puntos.

---

# 367. Session Expiration

El frontend debe tratar expiración de sesión de forma consistente.

---

# 368. Session Failure UX

No dejar la UI indefinidamente en estado de loading cuando la sesión ha expirado.

---

# 369. Refresh Tokens

Si existe refresh token:

```text
refresh behavior

expiration

rotation

revocation
```

deben mantenerse coherentes.

---

# 370. Refresh Guardrail

No implementar retries infinitos frente a errores de autenticación.

---

# 371. Authentication Loop

Evitar:

```text
request fails 401

↓

refresh fails

↓

retry original

↓

401

↓

refresh again

...
```

---

# 372. Logout

Debe invalidar o eliminar la sesión cliente de acuerdo con la estrategia adoptada.

---

# 373. Future Revocation

Si se introduce revocación server-side, debe centralizarse y no implementarse ad hoc por módulo.

---

# 374. Password Handling

Las contraseñas nunca deben almacenarse en texto plano.

---

# 375. Password Hashing

El hashing debe depender de una implementación segura y centralizada.

---

# 376. Password Comparison

No implementar algoritmos criptográficos manuales.

---

# 377. Password Logging

Nunca registrar:

```text
password

password confirmation
```

---

# 378. Authentication Error Messages

Evitar revelar información innecesaria sobre cuentas.

---

# 379. Example

Preferir un mensaje genérico:

```text
Invalid credentials
```

cuando distinguir usuario inexistente y contraseña incorrecta pueda revelar información.

---

# 380. Authorization Architecture

La autorización debe centralizar reglas reutilizables.

---

# 381. Authorization Model

Puede combinar:

```text
Global Roles

Global Permissions

Contextual Roles

Membership

Ownership

Resource State
```

---

# 382. Authorization Principle

```text
Authorization is action-specific.
```

---

# 383. Weak Check

```python
if user.is_admin:
    ...
```

en todos los casos.

---

# 384. Better Check

```python
ensure_can_update_project(actor, project)
```

---

# 385. Why

La policy puede considerar:

```text
global role

project membership

contextual role

resource status
```

sin dispersar esa lógica.

---

# 386. Role Checks

Los roles no deben compararse mediante strings arbitrarios dispersos.

---

# 387. Avoid

```python
if user.role == "admin":
```

si el proyecto dispone de enum/policy central.

---

# 388. Prefer

```python
user.role == Role.ADMIN
```

o una policy más semántica.

---

# 389. Permission Naming

Las permissions deben expresar:

```text
resource:action
```

o una convención equivalente consistente.

---

# 390. Examples

```text
projects:create

projects:update

projects:delete

users:read

audit:read
```

---

# 391. Permission Guardrail

No crear permissions extremadamente granulares sin necesidad real.

---

# 392. Contextual Authorization

Un permiso global puede no ser suficiente.

---

# 393. Example

```text
projects:update
```

puede significar:

```text
user may update projects

if contextual rules also allow this project
```

---

# 394. Membership

La pertenencia a un Project no implica automáticamente todas las operaciones.

---

# 395. Ownership

El ownership puede modificar permisos.

---

# 396. Resource State

El estado del recurso también puede afectar.

---

# 397. Example

Un Project:

```text
ARCHIVED
```

puede impedir modificaciones aunque el usuario siga siendo miembro.

---

# 398. Policy Interface

Las policies deben ser fáciles de testear de forma aislada.

---

# 399. Boolean Policy Example

```python
def can_update_project(
    actor: User,
    project: Project,
) -> bool:
    ...
```

---

# 400. Guard Policy Example

```python
def ensure_can_update_project(
    actor: User,
    project: Project,
) -> None:
    if not can_update_project(actor, project):
        raise ProjectAccessDeniedError
```

---

# 401. Authorization Error

Debe mapearse de forma consistente a la capa HTTP.

---

# 402. Not Found vs Forbidden

La plataforma debe mantener una policy coherente sobre:

```text
404

vs

403
```

para recursos protegidos.

---

# 403. Enumeration Risk

En áreas sensibles puede ser preferible no revelar la existencia del recurso.

---

# 404. Policy Consistency

No aplicar una estrategia diferente por router sin una razón explícita.

---

# 405. Authorization in Lists

Las colecciones también deben respetar acceso.

---

# 406. Incorrect

```text
query all projects

↓

render only authorized actions
```

si el usuario no debería conocer ciertos Projects.

---

# 407. Correct Principle

```text
filter unauthorized resources before exposure
```

---

# 408. Counts

Los counts también pueden revelar información.

---

# 409. Example

```text
You have access to 3 of 12 projects
```

puede revelar existencia de 9 recursos protegidos.

---

# 410. Search Authorization

Las búsquedas deben filtrar resultados según acceso.

---

# 411. Realtime Authorization

Las conexiones realtime requieren autenticación y autorización independientes.

---

# 412. Connection Authentication

La conexión debe asociarse con una identidad válida.

---

# 413. Room Authorization

Entrar en:

```text
project room
```

requiere verificar acceso al Project.

---

# 414. Subscription Validation

No confiar en:

```text
project_id
```

enviado por cliente sin validación.

---

# 415. Broadcast Scope

Los eventos deben dirigirse únicamente a recipients autorizados.

---

# 416. Realtime Leak

Un evento enviado al cliente equivocado es una vulnerabilidad aunque la API HTTP esté correctamente protegida.

---

# 417. Message Validation

Los mensajes recibidos por WebSocket también deben validarse.

---

# 418. Message Size

Puede aplicarse límite para prevenir abuso.

---

# 419. Message Type

Los tipos permitidos deben estar explícitamente definidos.

---

# 420. Unknown Message

Debe rechazarse de forma controlada.

---

# 421. Origin Validation

La estrategia WebSocket debe considerar origen cuando corresponda.

---

# 422. CSRF

Los flujos autenticados mediante cookies deben considerar CSRF.

---

# 423. CSRF Principle

```text
Authentication cookie

does not prove

intentional user action.
```

---

# 424. Mutating Request

Las operaciones que cambian estado deben utilizar el mecanismo CSRF adoptado.

---

# 425. GET Rule

Nunca utilizar GET para mutaciones también ayuda a reducir riesgos CSRF.

---

# 426. CSRF Token Handling

No registrar tokens CSRF en logs.

---

# 427. CSRF in Forms

Los formularios protegidos deben incluir el token cuando la estrategia lo requiera.

---

# 428. CSRF in JavaScript

Las mutaciones AJAX/fetch deben transmitir el token de acuerdo con la arquitectura definida.

---

# 429. Security Headers

Los headers deben configurarse centralmente.

---

# 430. Candidate Headers

Según deployment:

```text
Content-Security-Policy

X-Content-Type-Options

Referrer-Policy

Permissions-Policy
```

entre otros.

---

# 431. Header Guardrail

No copiar configuraciones genéricas sin verificar compatibilidad con la aplicación.

---

# 432. CSP

Una futura Content Security Policy estricta debe influir en las reglas frontend.

---

# 433. Inline Script Reduction

Evitar JavaScript inline facilita CSP.

---

# 434. Inline Style Reduction

También puede facilitar políticas más estrictas.

---

# 435. XSS Prevention

El output del usuario debe renderizarse con escaping apropiado.

---

# 436. Jinja Escaping

No desactivar autoescaping salvo necesidad muy específica y contenido confiable.

---

# 437. `|safe`

Evitar:

```jinja2
{{ user_content | safe }}
```

---

# 438. `safe` Rule

Solo utilizar sobre contenido:

```text
trusted

sanitized

explicitly reviewed
```

---

# 439. User-generated HTML

No debe renderizarse como HTML directamente sin sanitización segura.

---

# 440. HTML Construction in JavaScript

Evitar interpolar texto no confiable mediante:

```javascript
element.innerHTML = userValue;
```

---

# 441. Prefer

```javascript
element.textContent = userValue;
```

cuando se desea texto.

---

# 442. DOM API Security

Construir nodos mediante DOM APIs es preferible para contenido dinámico no confiable.

---

# 443. URL Validation

Los enlaces dinámicos deben generarse a partir de rutas conocidas cuando sea posible.

---

# 444. Open Redirect

No redirigir indiscriminadamente a URLs proporcionadas por usuario.

---

# 445. Redirect Whitelist

Si existe `next` o retorno dinámico:

```text
validate allowed destination
```

---

# 446. Input Validation

Todo input externo debe validarse.

---

# 447. Input Sources

Incluye:

```text
path params

query params

forms

JSON

headers

cookies

WebSocket payloads

file metadata
```

---

# 448. Hidden Fields

Los campos hidden del formulario siguen siendo input no confiable.

---

# 449. Select Options

El hecho de que una UI solo muestre opciones válidas no impide enviar otra manualmente.

---

# 450. Database IDs

Validar existencia y acceso.

---

# 451. File Upload Security

Los uploads requieren controles adicionales.

---

# 452. File Security Dimensions

```text
size

content type

extension

filename

storage path

authorization

download behavior
```

---

# 453. Filename Trust

No utilizar directamente el nombre original como path físico.

---

# 454. Path Traversal

Debe impedirse cualquier posibilidad de:

```text
../../
```

o equivalentes.

---

# 455. Storage Filename

Preferir identificadores generados como:

```text
UUID
```

para almacenamiento interno.

---

# 456. Original Filename

Puede conservarse como metadata para presentación.

---

# 457. MIME Type

No confiar únicamente en:

```text
Content-Type
```

enviado por cliente.

---

# 458. Extension

Tampoco confiar únicamente en extensión.

---

# 459. File Size

Validar límites antes de consumir recursos innecesarios cuando la infraestructura lo permita.

---

# 460. Upload Authorization

Debe comprobarse que el actor puede adjuntar al recurso objetivo.

---

# 461. Download Authorization

Debe validarse de nuevo al descargar.

---

# 462. Attachment URL

Conocer una URL o ID de Attachment no implica permiso.

---

# 463. Security Logging

Los eventos relevantes deben registrarse sin exponer información sensible.

---

# 464. Security Log Candidates

```text
authentication failure

authorization denial

invalid upload

unexpected token failure
```

según política.

---

# 465. Log Noise

No convertir comportamientos esperados en miles de logs ERROR.

---

# 466. Audit

Los cambios de seguridad relevantes deben generar Audit cuando corresponda.

---

# 467. Jinja2 Templates

Los templates son responsables de presentación SSR.

---

# 468. Template Principle

```text
Templates render state.

They do not own business logic.
```

---

# 469. Template Responsibilities

Pueden:

- mostrar datos;
- aplicar layout;
- incluir partials;
- utilizar macros;
- renderizar estados;
- seleccionar elementos según permisos ya calculados;
- construir formularios.

---

# 470. Template Non-responsibilities

No deberían:

- hacer queries;
- realizar cambios persistentes;
- implementar reglas complejas;
- calcular permisos mediante lógica repetida;
- procesar datos complejos.

---

# 471. Template Context

El contexto enviado debe ser:

```text
explicit

minimal

sufficient
```

---

# 472. Avoid Context Dump

No pasar objetos y estructuras completas "por si acaso".

---

# 473. Context Naming

Utilizar nombres claros:

```python
{
    "project": project,
    "tasks": tasks,
    "can_edit": can_edit,
}
```

---

# 474. Permission Context

La UI puede recibir:

```text
can_edit

can_delete

can_assign
```

cuando simplifique la presentación.

---

# 475. Permission Computation

Debe ocurrir en Python, no duplicarse en Jinja.

---

# 476. Weak Template

```jinja2
{% if user.role == "admin" or user.id == project.owner_id or ... %}
```

---

# 477. Better Template

```jinja2
{% if can_edit_project %}
```

---

# 478. Base Layout

Las páginas deben extender layouts comunes.

---

# 479. Example

```jinja2
{% extends "base.html" %}
```

---

# 480. Template Blocks

Utilizar bloques con responsabilidades claras.

---

# 481. Candidate Blocks

```text
title

content

head_extra

scripts
```

según la arquitectura existente.

---

# 482. Reusable Components

Utilizar:

```text
macros

partials

includes
```

para patrones repetidos.

---

# 483. Macro

Adecuada para componentes parametrizables.

---

# 484. Partial

Adecuada para fragmentos con contexto conocido.

---

# 485. Include Guardrail

No crear includes diminutos para cada etiqueta HTML.

---

# 486. Component Extraction

Extraer cuando exista:

```text
repetition

semantic component

independent complexity
```

---

# 487. Template Naming

Los nombres deben seguir patrón predecible.

---

# 488. Candidate Structure

```text
templates/
├── base.html
├── components/
├── projects/
│   ├── list.html
│   ├── detail.html
│   ├── form.html
│   └── _row.html
```

---

# 489. Private Partials

Puede utilizarse prefijo:

```text
_
```

para indicar fragmentos no navegables directamente.

---

# 490. Template Logic

Mantener lógica simple.

---

# 491. Acceptable

```jinja2
{% if tasks %}
{% for task in tasks %}
```

---

# 492. Smell

Múltiples niveles de:

```text
if

for

set

filters

business decisions
```

pueden indicar lógica fuera de lugar.

---

# 493. Template Variables

No reasignar numerosas variables para simular lógica de aplicación.

---

# 494. Filters

Los filtros custom deben utilizarse para presentación.

---

# 495. Good Filter

```text
format_datetime
```

---

# 496. Weak Filter

```text
user_can_delete_project
```

si encapsula policy de autorización desde template.

---

# 497. Date Formatting

Centralizar formato cuando sea posible.

---

# 498. Timezone Presentation

Los timestamps deben mostrarse según la estrategia temporal definida.

---

# 499. Null Values

La UI debe representar ausencia de datos explícitamente cuando sea útil.

---

# 500. Example

```text
Not assigned
```

en lugar de:

```text
None
```

---

# 501. Empty Collections

Debe existir empty state.

---

# 502. Empty State Structure

Puede responder:

```text
What is empty?

Why might it be empty?

What can the user do?
```

---

# 503. Example

```text
No tasks yet.

Create the first task to start organizing project work.
```

si el usuario puede crear.

---

# 504. Unauthorized Empty State

No sugerir una acción que el usuario no puede ejecutar.

---

# 505. Forms

Los formularios deben ser consistentes en estructura, validación y feedback.

---

# 506. Form Principle

```text
Validate on server.

Enhance on client.
```

---

# 507. Client Validation

Puede mejorar UX.

---

# 508. Server Validation

Permanece autoritativa.

---

# 509. Labels

Todo input debe disponer de label apropiado.

---

# 510. Placeholder

No utilizar placeholder como sustituto del label.

---

# 511. Required Fields

Deben indicarse de forma comprensible.

---

# 512. Error Association

Cada error de campo debe estar asociado visual y semánticamente al input.

---

# 513. Error Summary

En formularios complejos puede existir un resumen de errores.

---

# 514. Preserve Input

Después de un error, preservar valores válidos cuando sea posible.

---

# 515. Avoid Data Loss

Un validation error no debe obligar al usuario a rellenar todo el formulario nuevamente.

---

# 516. Select Fields

Las opciones deben generarse desde datos autorizados.

---

# 517. Disabled Options

No utilizar únicamente disabled state para proteger recursos no autorizados.

---

# 518. Hidden Values

No confiar en IDs hidden.

---

# 519. Form Method

Mutaciones deben utilizar:

```text
POST
```

o el mecanismo adecuado definido.

---

# 520. Form Actions

Las actions deben apuntar a rutas explícitas.

---

# 521. Destructive Forms

Las operaciones destructivas deben diferenciarse visualmente.

---

# 522. Confirmations

No todos los cambios requieren confirmación modal.

---

# 523. Confirmation Principle

```text
Use confirmation when accidental execution has meaningful cost.
```

---

# 524. Good Confirmation Candidates

```text
delete project

remove user

cancel reservation
```

según reversibilidad.

---

# 525. Poor Confirmation Candidate

```text
mark notification as read
```

---

# 526. Confirmation Fatigue

Demasiadas confirmaciones reducen su eficacia.

---

# 527. Dialog System

Los dialogs deben utilizar un sistema común.

---

# 528. Dialog Responsibilities

```text
open

close

focus

escape

backdrop

confirm

cancel
```

---

# 529. Native Dialog

Si se utiliza `<dialog>`, debe manejarse de forma accesible y consistente.

---

# 530. Dialog Trigger

Utilizar atributos declarativos cuando ayuden.

---

# 531. Example

```html
<button
    type="button"
    data-dialog-open="delete-project-dialog"
>
    Delete
</button>
```

---

# 532. Dialog JavaScript

La lógica debe ser reutilizable.

---

# 533. Avoid One-off Dialog Scripts

No crear un script distinto por cada modal.

---

# 534. Confirmation Context

El dialog debe indicar claramente qué recurso será afectado.

---

# 535. Destructive Confirmation

Ejemplo:

```text
Delete project "Autonomous Robot"?

This action cannot be undone.
```

si realmente es irreversible.

---

# 536. Dynamic Dialog Content

Debe insertarse de forma segura.

---

# 537. Toasts

Los toasts proporcionan feedback temporal.

---

# 538. Toast Use Cases

```text
successful mutation

non-blocking warning

background notification
```

---

# 539. Toast Non-use Cases

No utilizarlos como único mecanismo para errores críticos que requieran acción.

---

# 540. Toast Message

Debe ser:

```text
short

specific

action-oriented when necessary
```

---

# 541. Weak Toast

```text
Success.
```

---

# 542. Better Toast

```text
Task moved to In Progress.
```

---

# 543. Error Toast

Debe explicar lo suficiente.

---

# 544. Example

```text
Task could not be updated. Reload the board and try again.
```

cuando ese sea el recovery apropiado.

---

# 545. Toast Duration

No desaparecer demasiado rápido si contiene información relevante.

---

# 546. Accessibility

El sistema debe considerar lectores de pantalla.

---

# 547. Flash Messages

Los flujos SSR pueden utilizar flash messages cuando corresponda.

---

# 548. Flash vs Toast

No duplicar innecesariamente el mismo mensaje en ambos sistemas.

---

# 549. Feedback Ownership

Debe existir una estrategia consistente por tipo de interacción.

---

# 550. SSR Mutation

Puede utilizar:

```text
redirect

+

flash
```

---

# 551. AJAX Mutation

Puede utilizar:

```text
response

+

toast / inline state
```

---

# 552. Error Feedback

Los errores de formulario deben aparecer inline cuando sea posible.

---

# 553. JavaScript Philosophy

La plataforma utiliza:

```text
SSR-first

+

Progressive Enhancement
```

---

# 554. JavaScript Principle

```text
Use JavaScript where interaction needs it.

Do not rebuild server-rendered behavior unnecessarily.
```

---

# 555. Baseline Functionality

Las funcionalidades fundamentales deberían degradar razonablemente cuando JavaScript no esté disponible, cuando sea viable.

---

# 556. Progressive Enhancement

JavaScript puede mejorar:

```text
dialogs

toasts

drag and drop

realtime

inline updates

filters
```

---

# 557. No Accidental SPA

No introducir un estado cliente global complejo sin una necesidad clara.

---

# 558. Client State

Debe mantenerse mínimo y localizado.

---

# 559. Server State

El estado persistente pertenece al servidor.

---

# 560. DOM State

El DOM refleja una vista local del estado.

---

# 561. Realtime State

Los eventos actualizan esa vista, pero no deben convertirse en fuente autoritativa.

---

# 562. JavaScript Module Organization

La lógica debe dividirse por responsabilidad.

---

# 563. Candidate Structure

```text
static/js/
├── core/
├── components/
├── modules/
│   ├── projects/
│   ├── tasks/
│   ├── notifications/
│   └── dashboard/
└── realtime/
```

---

# 564. Structure Guardrail

La estructura real debe mantenerse tan simple como permita el tamaño del código.

---

# 565. Inline JavaScript

Evitar scripts inline en templates salvo casos mínimos y justificados.

---

# 566. Benefits

Reduce:

```text
duplication

CSP friction

testing difficulty

template complexity
```

---

# 567. Event Handlers

Preferir:

```javascript
element.addEventListener(...)
```

frente a:

```html
onclick="..."
```

---

# 568. Why

Mantiene comportamiento fuera de markup.

---

# 569. Data Attributes

Utilizar atributos `data-*` para conectar HTML y comportamiento JavaScript.

---

# 570. Example

```html
<button
    data-task-id="42"
    data-action="complete-task"
>
    Complete
</button>
```

---

# 571. Data Attribute Rule

Solo deben contener datos necesarios para interacción cliente.

---

# 572. Sensitive Data

No incluir secretos ni información protegida en data attributes.

---

# 573. DOM Selection

Preferir selectors estables.

---

# 574. Avoid Styling Coupling

No seleccionar elementos únicamente mediante clases destinadas a estilos si existe una alternativa semántica.

---

# 575. Better

```javascript
document.querySelector("[data-action='delete-task']")
```

---

# 576. CSS Class Separation

Puede distinguirse:

```text
visual classes

behavior hooks
```

---

# 577. DOM Queries

Centralizar cuando el componente las utiliza repetidamente.

---

# 578. Null Safety

Un script reutilizable debe tolerar páginas donde el componente no existe.

---

# 579. Example

```javascript
const dialog = document.querySelector("[data-dialog]");

if (!dialog) {
    return;
}
```

---

# 580. Initialization

Los módulos deben tener una estrategia de inicialización clara.

---

# 581. Example

```javascript
export function initTaskBoard() {
    ...
}
```

---

# 582. Multiple Initialization

Evitar registrar listeners duplicados si el init se ejecuta más de una vez.

---

# 583. Idempotent Initialization

Cuando sea relevante, el init debe poder ejecutarse de forma segura.

---

# 584. Event Delegation

Puede utilizarse para listas dinámicas.

---

# 585. Delegation Guardrail

No delegar todo al `document` sin necesidad.

---

# 586. Local Scope

Preferir el contenedor más cercano.

---

# 587. DOM Mutation

Las actualizaciones deben ser pequeñas y predecibles.

---

# 588. Full Reload

No evitar recarga a cualquier coste.

---

# 589. SSR Reload

Una recarga puede ser la solución más simple y fiable para ciertas operaciones poco frecuentes.

---

# 590. Dynamic Update

Debe utilizarse cuando aporte:

```text
lower friction

realtime freshness

interaction continuity
```

---

# 591. Fetch

Las requests JavaScript deben utilizar una capa consistente.

---

# 592. Fetch Wrapper

Puede existir un helper para:

```text
credentials

CSRF

JSON parsing

common errors
```

si reduce duplicación.

---

# 593. Fetch Wrapper Guardrail

No ocultar completamente el comportamiento HTTP.

---

# 594. Response Validation

No asumir que toda response es JSON válida.

---

# 595. HTTP Error

`fetch()` no rechaza automáticamente todos los códigos HTTP no exitosos.

---

# 596. Required Check

Debe evaluarse:

```javascript
response.ok
```

o la estrategia equivalente.

---

# 597. Error Handling

Cada interacción debe tener recovery razonable.

---

# 598. Loading State

Las operaciones asíncronas deben mostrar feedback cuando la espera sea perceptible.

---

# 599. Disable During Mutation

Puede deshabilitarse temporalmente una acción para evitar double-submit.

---

# 600. Double-submit

Debe considerarse tanto en cliente como en backend cuando la operación sea sensible.

---

# 601. Button State Recovery

Después de error, reactivar el botón cuando corresponda.

---

# 602. `finally`

Puede ser útil para restaurar estado visual.

---

# 603. Async Functions

Utilizar `async/await` para claridad cuando corresponda.

---

# 604. Promise Chains

No son incorrectas, pero evitar mezclar estilos dentro del mismo flujo sin necesidad.

---

# 605. Error Boundaries

El frontend debe evitar que un error en un componente rompa toda la página cuando sea posible.

---

# 606. Console Logging

No dejar logs de debug indiscriminados en producción.

---

# 607. `console.log`

Debe eliminarse cuando ya no sea necesario.

---

# 608. `console.error`

Puede utilizarse para errores técnicos significativos, pero no sustituye observabilidad.

---

# 609. Frontend Error Tracking

Si se introduce una herramienta de error tracking, debe centralizarse.

---

# 610. Client-side Validation

Debe replicar solo validaciones útiles para feedback rápido.

---

# 611. Client Validation Rule

No asumir que evita requests maliciosas.

---

# 612. JavaScript Naming

Seguir convención consistente.

---

# 613. Variables and Functions

Preferir:

```text
camelCase
```

---

# 614. Classes

Utilizar:

```text
PascalCase
```

cuando existan clases.

---

# 615. Constants

Puede utilizarse:

```text
UPPER_SNAKE_CASE
```

para constantes verdaderamente globales/inmutables.

---

# 616. Boolean JS

Ejemplos:

```javascript
isLoading
hasPermission
canSubmit
```

---

# 617. JavaScript Functions

Deben expresar acción:

```javascript
openDialog()
updateTaskCard()
showToast()
connectNotificationsSocket()
```

---

# 618. Global Variables

Evitar contaminar:

```javascript
window
```

---

# 619. Global Exposure

Solo usar cuando exista una necesidad clara de integración.

---

# 620. Module State

Preferir estado encapsulado dentro del módulo.

---

# 621. Event Names

Los custom events deben tener nombres consistentes.

---

# 622. Candidate Convention

```text
task:updated

notification:read

project:member-added
```

---

# 623. Event Naming Guardrail

No crear custom events si una llamada directa entre componentes simples es suficiente.

---

# 624. Event Payload

Debe contener únicamente datos necesarios.

---

# 625. Realtime Events

Los eventos realtime deben utilizar contratos explícitos.

---

# 626. Realtime Payload Example

```json
{
  "type": "task.updated",
  "version": 1,
  "task_id": 42,
  "project_id": 7
}
```

---

# 627. Event Contract

Debe definir:

```text
type

version

payload

scope
```

---

# 628. Event Version

Puede incorporarse cuando exista evolución contractual real.

---

# 629. Event Naming

Preferir nombres semánticos:

```text
task.updated
```

frente a:

```text
event_12
```

---

# 630. Event Payload Size

Mantener payload razonablemente pequeño.

---

# 631. Full Entity Payload

No enviar entidades completas si el cliente solo necesita:

```text
id + changed state
```

---

# 632. Sensitive Fields

No incluirlos aunque el recipient tenga acceso si no son necesarios.

---

# 633. Realtime Update Strategy

Debe decidirse por tipo de evento si:

```text
patch DOM directly
```

o:

```text
re-fetch authoritative resource
```

---

# 634. Re-fetch Strategy

Preferible cuando:

```text
state is complex

event may be incomplete

reconciliation matters
```

---

# 635. Direct Update Strategy

Puede ser adecuada para cambios pequeños y claros.

---

# 636. Duplicate Events

Los handlers deben ser tolerantes cuando sea razonable.

---

# 637. Example

Recibir dos veces:

```text
notification.read
```

no debería romper la UI.

---

# 638. Out-of-order Events

No asumir orden perfecto si la arquitectura no lo garantiza.

---

# 639. Sequence Data

Si el orden es crítico, debe existir mecanismo explícito.

---

# 640. Reconnection

El cliente debe implementar estrategia de reconexión controlada.

---

# 641. Reconnect Backoff

Preferir:

```text
incremental / exponential backoff
```

con límites.

---

# 642. Reconnect Storm

Evitar reconnect inmediato infinito.

---

# 643. Reconnect State

Una conexión recuperada no implica estado recuperado.

---

# 644. Reconciliation Rule

Después de una desconexión significativa:

```text
re-fetch authoritative state
```

cuando sea necesario.

---

# 645. Connection Indicator

Puede mostrarse si la pérdida de realtime afecta significativamente a la fiabilidad percibida.

---

# 646. Accessibility

La accesibilidad forma parte del Definition of Done de UI.

---

# 647. Accessibility Principle

```text
Accessible by default

not patched later.
```

---

# 648. Semantic HTML

Utilizar el elemento HTML adecuado siempre que sea posible.

---

# 649. Button vs Div

Acciones deben utilizar:

```html
<button>
```

no:

```html
<div onclick="...">
```

---

# 650. Link vs Button

Usar:

```text
link
```

para navegación.

Usar:

```text
button
```

para acción.

---

# 651. Heading Hierarchy

Mantener jerarquía lógica:

```text
h1

h2

h3
```

sin elegir niveles por tamaño visual.

---

# 652. Page H1

Cada vista principal debería tener un heading principal claro.

---

# 653. Landmarks

Utilizar elementos como:

```html
<header>
<nav>
<main>
<footer>
```

cuando correspondan.

---

# 654. Form Labels

Todo control necesita nombre accesible.

---

# 655. Input Description

Puede utilizarse `aria-describedby` para errores o ayuda.

---

# 656. Error State

El error debe asociarse al campo correspondiente.

---

# 657. ARIA

Utilizar ARIA cuando HTML semántico no sea suficiente.

---

# 658. ARIA Guardrail

```text
No ARIA is better than bad ARIA.
```

---

# 659. Keyboard

Toda interacción crítica debe poder operarse mediante teclado.

---

# 660. Focus Visibility

No eliminar `outline` sin proporcionar una alternativa clara.

---

# 661. Focus Order

Debe seguir un flujo lógico.

---

# 662. Dialog Focus

Al abrir un dialog:

```text
focus moves inside
```

---

# 663. Dialog Close

Al cerrar:

```text
focus returns to trigger
```

cuando sea apropiado.

---

# 664. Escape

Dialogs modales deberían permitir cierre mediante Escape salvo flujo que lo impida justificadamente.

---

# 665. Focus Trap

Un modal debe mantener el foco dentro mientras está activo cuando corresponda.

---

# 666. Drag and Drop

Una interacción drag-and-drop necesita alternativa accesible.

---

# 667. Kanban Accessibility

Mover una Task no debe depender únicamente del ratón.

---

# 668. Candidate Alternative

```text
Move to...

select/menu/button
```

---

# 669. Color

No utilizar únicamente color para transmitir estado.

---

# 670. Example

No distinguir estados solo por:

```text
green

red
```

---

# 671. Better

Combinar:

```text
text

icon

color
```

---

# 672. Contrast

Los componentes deben mantener contraste suficiente.

---

# 673. Reduced Motion

Respetar:

```css
prefers-reduced-motion
```

cuando existan animaciones.

---

# 674. Animation Principle

Las animaciones deben apoyar comprensión, no decoración constante.

---

# 675. Toast Accessibility

Los toasts deben utilizar una estrategia apropiada de live region.

---

# 676. Live Region

No anunciar cada cambio realtime irrelevante.

---

# 677. Notification Noise

La accesibilidad también implica controlar frecuencia de anuncios.

---

# 678. Dynamic Content

Los cambios importantes deben ser detectables sin generar interrupción excesiva.

---

# 679. Table Accessibility

Las tablas deben utilizar:

```html
<table>
<thead>
<th>
```

cuando los datos sean tabulares.

---

# 680. Responsive Tables

No eliminar estructura semántica únicamente para facilitar móvil.

---

# 681. Icon Buttons

Deben tener nombre accesible.

---

# 682. Example

```html
<button aria-label="Delete task">
    ...
</button>
```

---

# 683. Decorative Icons

Deben ocultarse de tecnologías asistivas cuando no aporten información.

---

# 684. Images

Las imágenes informativas necesitan `alt` apropiado.

---

# 685. Decorative Images

Utilizar:

```html
alt=""
```

cuando sean puramente decorativas.

---

# 686. Responsive Design

La UI debe adaptarse a:

```text
desktop

tablet

mobile
```

según workflows reales.

---

# 687. Responsive Principle

No diseñar desktop y luego simplemente comprimirlo.

---

# 688. Mobile Priority

Priorizar:

```text
content

primary action

navigation
```

---

# 689. Touch Targets

Los targets deben tener tamaño suficiente para interacción táctil.

---

# 690. Hover

No depender de hover para acceder a información o acciones esenciales.

---

# 691. Tables on Mobile

Pueden utilizar:

```text
horizontal scroll

responsive columns

alternative cards
```

según contexto.

---

# 692. Information Preservation

No ocultar información crítica únicamente porque la pantalla sea pequeña.

---

# 693. Forms on Mobile

Los inputs deben aprovechar tipos apropiados:

```html
type="email"
type="date"
type="number"
```

cuando corresponda.

---

# 694. Mobile Keyboard

Tipos correctos mejoran teclado virtual.

---

# 695. UX Consistency

Los mismos patrones deben comportarse igual en toda la plataforma.

---

# 696. Create Action

La acción principal de creación debe aparecer en lugares predecibles.

---

# 697. Edit Action

Debe utilizar un patrón visual consistente.

---

# 698. Delete Action

Debe mantener semántica destructiva común.

---

# 699. Status Badges

Deben reutilizar un componente o convención.

---

# 700. Empty States

Deben compartir patrón.

---

# 701. Pagination

Debe presentar navegación coherente.

---

# 702. Search and Filters

Deben mantener placement y comportamiento predecibles.

---

# 703. Error States

No crear mensajes completamente distintos para el mismo tipo de error por módulo.

---

# 704. UI Authorization

Las acciones visibles deben corresponder con backend capabilities.

---

# 705. Authorization Mismatch

Debe evitarse:

```text
button visible

↓

server always returns 403
```

si la UI ya conoce que el usuario no puede actuar.

---

# 706. Opposite Mismatch

También evitar:

```text
button hidden

but

backend would allow action
```

cuando perjudique usabilidad.

---

# 707. UI Permission Mapping

Debe derivarse de la misma política conceptual.

---

# 708. CSS

Las reglas CSS deben favorecer reutilización y previsibilidad.

---

# 709. CSS Naming

Seguir la convención ya adoptada por el proyecto.

---

# 710. CSS Guardrail

No introducir un segundo sistema de naming sin necesidad.

---

# 711. Utility Classes

Pueden utilizarse para patrones simples.

---

# 712. Component Classes

Deben representar componentes semánticos.

---

# 713. Inline Styles

Evitar:

```html
style="..."
```

salvo valores dinámicos muy específicos y justificados.

---

# 714. Magic Numbers

Evitar valores arbitrarios repetidos.

---

# 715. CSS Variables

Utilizar custom properties para tokens reutilizables.

---

# 716. Candidate Tokens

```text
spacing

radius

font size

surface

border

shadow
```

según design system.

---

# 717. Hard-coded Colors

Evitar dispersión de valores de color si existe sistema de tokens.

---

# 718. Theme Consistency

Los componentes deben utilizar variables comunes.

---

# 719. Specificity

Evitar selectors excesivamente específicos.

---

# 720. Avoid

```css
main .content .panel div.card ul li a.button
```

---

# 721. Better

```css
.task-card__action
```

o la convención vigente.

---

# 722. `!important`

Evitar salvo necesidad excepcional.

---

# 723. `!important` Smell

Puede indicar conflicto de arquitectura CSS.

---

# 724. Global Styles

Deben reservarse para:

```text
reset

typography

layout primitives

shared tokens
```

---

# 725. Component Isolation

Los estilos de un componente no deben modificar inesperadamente otros módulos.

---

# 726. JavaScript and CSS Coupling

No usar nombres de clase visuales como contrato JavaScript si puede evitarse.

---

# 727. Data Hooks

Preferir:

```text
data-action

data-component
```

para comportamiento.

---

# 728. UI Component Responsibility

Cada componente debe tener:

```text
clear purpose

clear states

clear interactions
```

---

# 729. Component States

Considerar:

```text
default

hover

focus

disabled

loading

error

empty
```

según aplicabilidad.

---

# 730. Disabled State

No debe confundirse con unauthorized state.

---

# 731. Loading State

Debe impedir acciones duplicadas cuando corresponda.

---

# 732. Error Recovery

El componente debe volver a un estado usable después de error.

---

# 733. Frontend State Principle

```text
Local unless there is a clear reason to share.
```

---

# 734. Global Store

No introducir un state manager global sin necesidad real.

---

# 735. Cross-page State

Debe vivir preferiblemente en servidor o URL, no en memoria cliente global.

---

# 736. URL as State

Los filtros navegables pueden reflejarse en query params.

---

# 737. Benefits

Permite:

```text
bookmarking

sharing

back/forward navigation

SSR rendering
```

---

# 738. Filter Example

```text
/tasks?status=in_progress&assignee=me
```

---

# 739. URL Guardrail

No incluir información sensible en URLs.

---

# 740. Browser History

Las interacciones que representan navegación significativa deben respetar historial.

---

# 741. Accessibility Review Questions

Antes de aceptar una UI:

```text
Can it be used with keyboard?

Does focus move predictably?

Are controls semantically correct?

Do errors have accessible descriptions?

Does information depend only on color?

Does dynamic content create announcement noise?
```

---

# 742. Frontend Review Questions

```text
Is this behavior needed in JavaScript?

Could SSR solve it more simply?

Is client state minimal?

Is server state authoritative?

Are errors recoverable?

Does this component reuse shared patterns?
```

---

# 743. Security Review Questions

```text
Is the actor authenticated?

Is this exact resource authorized?

Can IDs be manipulated?

Can the client set protected fields?

Can this output create XSS?

Can this action be forged via CSRF?

Could realtime leak information?
```

---

# 744. Template Review Questions

```text
Is business logic leaking into Jinja?

Are permissions precomputed?

Is user content escaped?

Is this component duplicated?

Does the empty state respect authorization?
```

---

# 745. Form Review Questions

```text
Is server validation authoritative?

Are labels present?

Are errors associated with fields?

Are user values preserved after failure?

Could hidden fields be tampered with?

Is destructive intent clear?
```

---

# 746. JavaScript Review Questions

```text
Does this module have one clear responsibility?

Does it tolerate missing DOM?

Can it initialize twice safely?

Are fetch errors handled?

Can duplicated realtime events break it?

Does it expose unnecessary globals?
```

---

# 747. UX Review Questions

```text
Does the user know what happened?

Does the user know what to do next?

Is accidental destructive action prevented?

Are loading and error states visible?

Is the interaction consistent with the rest of the platform?
```

---

# 748. Part 2 Summary

Esta segunda parte establece reglas para:

```text
security

authentication

authorization

RBAC

contextual access

CSRF

XSS

file security

realtime security

Jinja2

SSR

forms

dialogs

toasts

JavaScript

progressive enhancement

frontend state

CSS

responsive behavior

accessibility

UX consistency
```

---

# 749. Continuation

La **Parte 3/3** completa `51_CODING_RULES.md` con:

```text
WebSockets and Realtime contracts

Notifications

Activity Feed

Audit

Logging

Monitoring

Observability

Testing rules

Unit / Integration / UI / Realtime tests

Fixtures

Mocks

CI/CD

Git

Branches

Commits

Pull Requests

Documentation

Code Review

Performance

Dependencies

Technical Debt

Definition of Done

Coding Checklist

Anti-patterns

Final Engineering Principles
```

---

# 51_CODING_RULES.md

# Aula Robótica Platform — Coding Rules

## Parte 3 — Realtime, Testing, Observability, Git, CI/CD, Documentation, Code Review, Performance, Technical Debt y Definition of Done

---

# 750. Realtime Coding Rules

Realtime debe considerarse una mejora de sincronización sobre el estado persistido.

---

# 751. Realtime Principle

```text
Persistence is authoritative.

Realtime improves freshness.
```

---

# 752. No Realtime Authority

El estado del cliente no debe considerarse correcto únicamente porque recibió un evento WebSocket.

---

# 753. Realtime Architecture

El flujo conceptual debe mantenerse:

```text
Domain Mutation

↓

Database Commit

↓

Domain / Application Event

↓

Realtime Delivery

↓

Client Update
```

---

# 754. Commit Before Broadcast

No debe anunciarse un cambio como confirmado antes de que la persistencia autoritativa haya tenido éxito.

---

# 755. Incorrect Flow

```text
broadcast task.updated

↓

database commit fails
```

---

# 756. Correct Principle

```text
Persist first.

Notify second.
```

---

# 757. Delivery Failure

Si la persistencia tiene éxito pero el delivery realtime falla:

```text
business state remains valid
```

---

# 758. Client Recovery

El cliente debe poder recuperar el estado mediante:

```text
HTTP / SSR authoritative read
```

---

# 759. Realtime Event Contract

Cada evento debe tener un contrato explícito.

---

# 760. Candidate Envelope

```json
{
  "type": "task.updated",
  "version": 1,
  "event_id": "uuid",
  "occurred_at": "2026-08-16T14:35:00Z",
  "payload": {}
}
```

---

# 761. Required Event Information

Según el caso:

```text
type

version

resource identifier

context identifier

payload
```

---

# 762. Event ID

Puede utilizarse para:

- deduplication;
- diagnostics;
- tracing.

---

# 763. Event ID Guardrail

No introducirlo sin utilizarlo si el contrato todavía es simple.

---

# 764. Event Type Naming

Preferir:

```text
<resource>.<past-tense-action>
```

---

# 765. Examples

```text
task.created

task.updated

task.deleted

notification.created

activity.created

project.member_added
```

---

# 766. Event Naming Consistency

No mezclar:

```text
TASK_UPDATE

taskUpdated

task.updated
```

sin motivo.

---

# 767. Event Semantics

Un evento debe describir algo que ya ocurrió.

---

# 768. Command vs Event

```text
update_task
```

representa una intención/comando.

```text
task.updated
```

representa un hecho.

---

# 769. Event Payload

Debe contener únicamente la información necesaria para el consumidor.

---

# 770. Payload Guardrail

No serializar automáticamente todo el ORM model.

---

# 771. Event Security

El payload debe respetar:

```text
least data

least privilege
```

---

# 772. Project-scoped Events

Un evento de Project debe contener suficiente contexto para routing sin revelar información fuera del scope autorizado.

---

# 773. Routing

La lógica de routing debe permanecer separada de la lógica de dominio.

---

# 774. Room Naming

Utilizar convención consistente.

---

# 775. Candidate Room Names

```text
user:{user_id}

project:{project_id}
```

---

# 776. Room Name Guardrail

El nombre del room no constituye autorización.

---

# 777. Join Room

Antes de unir un socket a:

```text
project:42
```

debe comprobarse acceso a Project 42.

---

# 778. Leave Room

Debe limpiarse membership al cerrar o cambiar contexto.

---

# 779. Connection Registry

Si existe registry de conexiones, debe tener ownership claro.

---

# 780. Registry Guardrail

No utilizar estructuras globales dispersas para conexiones.

---

# 781. Single-instance Assumption

Mientras realtime sea process-local, esta limitación debe permanecer explícita.

---

# 782. Future Multi-instance

No implementar broker hasta que exista necesidad.

---

# 783. Client Reconnect

Debe aplicar backoff.

---

# 784. Candidate Backoff

Conceptualmente:

```text
1s

2s

4s

8s

bounded maximum
```

---

# 785. Backoff Jitter

Puede añadirse cuando múltiples clientes podrían reconectar simultáneamente.

---

# 786. Infinite Reconnect

El cliente puede seguir intentando, pero no mediante loop agresivo.

---

# 787. Reconnect UX

Debe evitar saturar al usuario con mensajes repetitivos.

---

# 788. Reconciliation

Tras una desconexión relevante, el cliente debe comprobar estado autoritativo.

---

# 789. Reconciliation Pattern

```text
WebSocket reconnect

↓

resubscribe

↓

fetch current authoritative state

↓

render

↓

continue realtime updates
```

---

# 790. Missed Events

No intentar reconstruir necesariamente todos los eventos perdidos si recuperar el estado actual es más simple.

---

# 791. Event Replay

Solo debe introducirse si existe un requirement real.

---

# 792. Duplicate Event Handling

Los handlers deberían ser idempotentes cuando sea razonable.

---

# 793. Example

Dos eventos:

```text
notification.read
```

no deberían producir errores o estados inconsistentes.

---

# 794. Deleted Resource Event

El cliente debe tolerar que un recurso ya no exista.

---

# 795. Out-of-date Client

Un handler no debe asumir siempre que el DOM contiene exactamente el estado esperado.

---

# 796. Defensive DOM Update

Debe verificar existencia de elementos antes de modificarlos.

---

# 797. Complex Realtime Update

Cuando una mutación afecta varias áreas de la página:

```text
prefer authoritative refresh/re-fetch
```

sobre múltiples patches frágiles.

---

# 798. Realtime Logging

Debe registrar suficiente contexto para diagnosticar:

```text
connection

subscription

delivery failure

disconnect
```

---

# 799. Realtime Sensitive Data

No registrar payloads completos si contienen datos de usuario.

---

# 800. Realtime Metrics

Deben considerarse:

```text
active connections

connects

disconnects

delivery failures

reconnects
```

---

# 801. Realtime Tests

Todo evento crítico debe tener cobertura apropiada.

---

# 802. Realtime Test Questions

```text
Who receives it?

Who must not receive it?

What happens after reconnect?

What happens twice?

What happens if delivery fails?
```

---

# 803. Notifications Coding Rules

Notifications representan señales persistentes de atención.

---

# 804. Notification Principle

```text
A notification is not merely a realtime message.
```

---

# 805. Persistence

Una Notification importante debe persistirse cuando su significado requiera recuperar el aviso posteriormente.

---

# 806. Realtime Delivery

Realtime puede anunciar una Notification nueva.

---

# 807. Notification Creation

Debe realizarse desde lógica de aplicación asociada al evento relevante.

---

# 808. Notification Router Guardrail

No crear Notifications manualmente en numerosos routers.

---

# 809. Notification Recipient

Debe calcularse server-side.

---

# 810. Client Recipient ID

No confiar en un recipient enviado por cliente.

---

# 811. Notification Content

Debe ser:

```text
human-readable

contextual

minimal
```

---

# 812. Notification Link

Cuando sea accionable debe apuntar al recurso adecuado.

---

# 813. Link Authorization

El hecho de recibir una Notification no sustituye autorización posterior sobre el recurso.

---

# 814. Stale Notification

El recurso puede dejar de existir o de ser accesible.

La UI debe manejarlo correctamente.

---

# 815. Read State

Debe ser idempotente.

---

# 816. Mark as Read

Ejecutarlo dos veces debe producir el mismo estado final.

---

# 817. Notification Categories

Deben representar significado funcional.

---

# 818. Avoid Technical Category Names

No utilizar:

```text
EVENT_TYPE_4
```

en UI.

---

# 819. Notification Noise

No generar Notifications para cambios de bajo valor.

---

# 820. Notification vs Feed

```text
Notification

=

attention directed to a user
```

```text
Feed Event

=

awareness of contextual activity
```

---

# 821. Activity Feed Coding Rules

Activity Feed es una proyección orientada a humanos.

---

# 822. Feed Principle

```text
Feed is not Audit.
```

---

# 823. Feed Event

Debe poder convertirse en frase comprensible.

---

# 824. Example

```text
Fran moved "Integrate lidar" to In Progress.
```

---

# 825. Feed Source

Preferir eventos de aplicación/dominio consistentes.

---

# 826. Feed Guardrail

No construir Feed leyendo directamente logs técnicos.

---

# 827. Feed Authorization

La consulta debe filtrar eventos según acceso actual.

---

# 828. Historic Access

Debe definirse qué ocurre cuando un usuario pierde acceso al recurso.

---

# 829. Feed Pagination

Debe evitar historial ilimitado en una request.

---

# 830. Feed Ordering

Debe ser determinista.

---

# 831. Feed Deduplication

No mostrar varios eventos equivalentes por duplicación técnica.

---

# 832. Audit Coding Rules

Audit registra trazabilidad formal.

---

# 833. Audit Principle

```text
Audit records business/security facts.

Logs explain runtime behavior.
```

---

# 834. Audit Fields

Según diseño:

```text
actor

action

resource_type

resource_id

timestamp

relevant metadata
```

---

# 835. Audit Actor

Debe derivarse del contexto autenticado o de una identidad de sistema.

---

# 836. System Actor

Background jobs futuros deben poder identificarse como:

```text
system / automation
```

---

# 837. Audit Action Naming

Utilizar nombres consistentes.

---

# 838. Candidate Actions

```text
created

updated

deleted

assigned

archived

restored
```

---

# 839. Audit Payload

Evitar almacenar snapshots completos sin necesidad.

---

# 840. Audit Sensitive Data

Nunca incluir secretos.

---

# 841. Audit Transaction

Cuando el Audit forma parte de la operación, debe considerar coherencia transaccional.

---

# 842. Logging Coding Rules

Los logs deben apoyar diagnóstico.

---

# 843. Logging Principle

```text
Log events worth understanding.

Do not narrate every line of execution.
```

---

# 844. Structured Logging

Preferir logs estructurados cuando la infraestructura lo permita.

---

# 845. Useful Log Context

Puede incluir:

```text
request_id

actor_id

resource_type

resource_id

operation
```

cuando sea seguro.

---

# 846. Log Levels

Utilizar consistentemente:

```text
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

---

# 847. DEBUG

Para detalles de diagnóstico no necesarios normalmente en producción.

---

# 848. INFO

Para eventos operativos normales relevantes.

---

# 849. WARNING

Para situación inesperada pero recuperable.

---

# 850. ERROR

Para fallo que impide una operación o requiere investigación.

---

# 851. CRITICAL

Reservar para fallos severos del sistema.

---

# 852. Logging Guardrail

No utilizar ERROR para validaciones normales del usuario.

---

# 853. Example

```text
Invalid form field
```

normalmente no constituye ERROR operacional.

---

# 854. Logging Exceptions

Cuando se registra una excepción, evitar duplicar stack trace en múltiples capas.

---

# 855. Exception Context

El punto de logging debe conocer suficiente contexto.

---

# 856. PII in Logs

Minimizar datos personales.

---

# 857. Never Log

```text
passwords

tokens

cookies

Authorization headers

secret keys

file contents
```

---

# 858. Log Formatting

No construir manualmente strings enormes con objetos completos.

---

# 859. Observability Coding Rules

El código importante debe producir señales suficientes para comprender comportamiento.

---

# 860. Observability Signals

```text
Logs

Metrics

Traces
```

---

# 861. Instrumentation Principle

```text
Instrument boundaries and outcomes

not every internal function.
```

---

# 862. Candidate Instrumentation Points

```text
HTTP requests

database operations

external integrations

background jobs

realtime delivery
```

---

# 863. Metrics Naming

Debe utilizar naming consistente.

---

# 864. Metric Cardinality

Evitar labels de alta cardinalidad.

---

# 865. Bad Label

```text
user_id
```

en una métrica Prometheus general.

---

# 866. Good Labels

Ejemplos:

```text
method

route

status_class

event_type
```

cuando sean bounded.

---

# 867. Metric Cardinality Principle

```text
Do not turn identifiers into metric dimensions.
```

---

# 868. Business Metrics

No deben mezclarse indiscriminadamente con telemetry técnica.

---

# 869. Trace IDs

Si existe tracing, debe propagarse consistentemente.

---

# 870. Testing Coding Rules

Los tests forman parte del código de producción en términos de mantenibilidad.

---

# 871. Test Principle

```text
Test behavior

not implementation trivia.
```

---

# 872. Test Readability

Un test debe expresar claramente:

```text
given

when

then
```

aunque no utilice esos comentarios literalmente.

---

# 873. Test Naming

Debe describir comportamiento.

---

# 874. Example

```python
def test_project_member_can_update_task():
    ...
```

---

# 875. Weak Name

```python
def test_update_1():
    ...
```

---

# 876. Test Structure

Preferir:

```text
Arrange

Act

Assert
```

---

# 877. Arrange

Preparar únicamente estado necesario.

---

# 878. Act

Ejecutar una acción principal.

---

# 879. Assert

Comprobar resultado observable.

---

# 880. Multiple Assertions

Son válidas cuando verifican un mismo comportamiento coherente.

---

# 881. Test Isolation

Un test no debe depender del orden de ejecución.

---

# 882. Shared State

Evitar estado global mutable entre tests.

---

# 883. Database Tests

Deben ejecutarse sobre estado controlado.

---

# 884. Fixture Principle

```text
Fixtures provide reusable state.

They should not hide the meaning of the test.
```

---

# 885. Overloaded Fixture

Evitar fixtures que creen:

```text
10 users

8 projects

30 tasks
```

para cada test si solo necesita dos entidades.

---

# 886. Fixture Naming

Debe expresar el objeto/contexto creado.

---

# 887. Examples

```python
admin_user
project_member
sample_project
task_in_progress
```

---

# 888. Factory Pattern

Puede utilizarse para crear datos flexibles.

---

# 889. Test Factories

Son útiles cuando existen múltiples variaciones de una entidad.

---

# 890. Factory Guardrail

No construir un framework interno complejo para pocos tests.

---

# 891. Mocking

Utilizar mocks en boundaries apropiados.

---

# 892. Good Mock Candidates

```text
email provider

object storage

external API

LLM provider
```

---

# 893. Poor Mock Candidate

No mockear indiscriminadamente el propio dominio hasta que el test deje de verificar comportamiento real.

---

# 894. Database Mocking

Para lógica que depende realmente de constraints o queries:

```text
use integration test
```

---

# 895. Unit Tests

Adecuados para:

```text
pure functions

policies

domain rules

transformations
```

---

# 896. Integration Tests

Adecuados para:

```text
database behavior

services + persistence

HTTP boundaries

authorization integration
```

---

# 897. UI Tests

Adecuados para journeys críticos.

---

# 898. Realtime Tests

Deben validar múltiples clientes cuando el comportamiento lo requiera.

---

# 899. Security Tests

Las reglas de autorización críticas necesitan casos:

```text
allowed

denied

cross-resource access
```

---

# 900. Negative Tests

No probar únicamente happy path.

---

# 901. Validation Tests

Deben incluir input inválido relevante.

---

# 902. Boundary Tests

Probar límites cuando exista semántica:

```text
minimum

maximum

empty

duplicate
```

---

# 903. Time Tests

Evitar depender del reloj real cuando la precisión temporal sea parte del comportamiento.

---

# 904. Clock Injection

Puede considerarse si el dominio necesita tests temporales deterministas.

---

# 905. Timezone Tests

Deben existir cuando la conversión temporal sea relevante.

---

# 906. Test Data

No utilizar datos sensibles reales.

---

# 907. Determinism

Los tests deben producir resultados repetibles.

---

# 908. Randomness

Si se utiliza randomness:

```text
seed or control it
```

cuando afecte reproducibilidad.

---

# 909. Sleep in Tests

Evitar:

```python
time.sleep(...)
```

como sincronización arbitraria.

---

# 910. Better

Esperar:

```text
observable condition

event

state
```

---

# 911. UI Waits

No utilizar sleeps fijos.

---

# 912. Realtime Test Wait

Esperar:

```text
specific event

or

authoritative state
```

---

# 913. Flaky Test Rule

Un test flaky debe tratarse como defecto.

---

# 914. Flaky Test Handling

No simplemente reintentar indefinidamente para ocultarlo.

---

# 915. Test Failure

Debe producir suficiente información para diagnóstico.

---

# 916. Test Coverage

Utilizar coverage como señal.

---

# 917. Coverage Guardrail

No escribir tests triviales únicamente para elevar porcentaje.

---

# 918. Regression Test

Todo bug significativo debería considerar un test que reproduzca el fallo.

---

# 919. Bug Fix Flow

```text
reproduce

↓

write regression test

↓

fix

↓

validate
```

cuando sea viable.

---

# 920. Test Placement

Los tests deben seguir estructura predecible.

---

# 921. Candidate Structure

```text
tests/
├── unit/
├── integration/
├── ui/
└── realtime/
```

o equivalente según organización real.

---

# 922. Test Co-location

También puede utilizarse co-location por módulo si se mantiene consistencia.

---

# 923. Test Helper Ownership

Helpers específicos deben permanecer cerca del dominio que los utiliza.

---

# 924. Global Test Utils

Solo para comportamiento transversal real.

---

# 925. CI Coding Rules

El código debe permanecer compatible con ejecución automatizada.

---

# 926. CI Principle

```text
If it only works on one developer machine,

it is not reproducible.
```

---

# 927. Local vs CI

Los mismos comandos principales deberían funcionar localmente y en CI.

---

# 928. CI Checks

Según madurez:

```text
lint

static analysis

tests

security scans

build
```

---

# 929. Fail Fast

Los checks rápidos pueden ejecutarse antes de suites más costosas.

---

# 930. Pipeline Order

Ejemplo:

```text
format/lint

↓

unit tests

↓

integration tests

↓

security

↓

UI/E2E

↓

build
```

según coste real.

---

# 931. CI Environment

No depender de estado manual no reproducible.

---

# 932. Secrets in CI

Deben proporcionarse mediante secret store del proveedor.

---

# 933. CI Logs

No imprimir secrets.

---

# 934. Artifact Build

Debe ocurrir desde código validado.

---

# 935. Immutable Artifact

Preferir promover el mismo artefacto entre entornos.

---

# 936. Migration in CI

Las migrations deben validarse automáticamente cuando sea posible.

---

# 937. Git Coding Rules

Git debe mantener una historia comprensible.

---

# 938. Branch Principle

Cada rama de trabajo debe tener propósito claro.

---

# 939. Branch Naming

Seguir convención vigente.

---

# 940. Candidate Examples

```text
feature/task-filtering

fix/realtime-reconnect

docs/coding-rules
```

---

# 941. Branch Guardrail

No mezclar varios objetivos no relacionados.

---

# 942. Commit Principle

```text
One logical change per commit
```

cuando sea razonablemente posible.

---

# 943. Atomic Commit

Debe poder entenderse y revisarse aisladamente.

---

# 944. Weak Commit

```text
changes
```

---

# 945. Better Commit

```text
fix(realtime): reconcile task board after reconnect
```

---

# 946. Commit Convention

Seguir la convención de commits adoptada por el proyecto.

---

# 947. Candidate Conventional Commits

```text
feat

fix

docs

test

refactor

chore

ci

perf
```

---

# 948. Commit Scope

Puede utilizar dominio:

```text
feat(tasks):

fix(attachments):

test(realtime):
```

---

# 949. Commit Message

Debe explicar:

```text
what changed
```

---

# 950. Commit Body

Puede explicar:

```text
why
```

cuando no sea evidente.

---

# 951. Formatting-only Commit

Separarlo cuando facilite review.

---

# 952. Refactor Commit

No debería mezclar cambios de comportamiento innecesariamente.

---

# 953. Pull Requests

Los PR deben ser revisables.

---

# 954. PR Principle

```text
Small enough to review.

Complete enough to be useful.
```

---

# 955. PR Scope

Debe representar un objetivo coherente.

---

# 956. PR Description

Debe incluir según necesidad:

```text
what

why

how validated

risks

screenshots
```

---

# 957. PR Tests

Indicar qué se ejecutó.

---

# 958. PR Screenshots

Para cambios visuales relevantes, incluir evidencia.

---

# 959. PR Security

Cambios de seguridad deben señalarse.

---

# 960. PR Database

Cambios de schema deben señalar migration e impacto.

---

# 961. PR Reviewability

Evitar PR gigantescos cuando puedan dividirse.

---

# 962. Large PR Exception

Puede justificarse en:

```text
mechanical rename

generated change

foundation refactor
```

si está claramente explicado.

---

# 963. Code Review

La review debe evaluar comportamiento y diseño, no únicamente estilo.

---

# 964. Review Priorities

Orden aproximado:

```text
Correctness

Security

Architecture

Data Integrity

Testing

Readability

Style
```

---

# 965. Review Question — Correctness

```text
Does it actually satisfy the intended behavior?
```

---

# 966. Review Question — Security

```text
Can a different actor/resource bypass this?
```

---

# 967. Review Question — Architecture

```text
Is the logic in the correct layer/module?
```

---

# 968. Review Question — Data

```text
Can invalid persistent state appear?
```

---

# 969. Review Question — Testing

```text
What protects this behavior from regression?
```

---

# 970. Review Question — Readability

```text
Can another developer understand this next year?
```

---

# 971. Review Comments

Deben ser:

```text
specific

actionable

respectful
```

---

# 972. Review Severity

Puede distinguirse informalmente:

```text
blocking

suggestion

nit
```

---

# 973. Nit

No debería bloquear por preferencia personal cuando el código ya cumple la convención.

---

# 974. Automated Style

No discutir manualmente lo que formatter/linter puede resolver.

---

# 975. Documentation Coding Rules

La documentación debe actualizarse cuando cambia un contrato o comportamiento relevante.

---

# 976. Documentation Principle

```text
Document stable knowledge.

Do not duplicate the code line by line.
```

---

# 977. Documentation Candidates

Actualizar cuando cambie:

```text
architecture

module responsibility

API contract

deployment

security

testing strategy
```

---

# 978. Code Comments vs Docs

```text
local implementation nuance

→ code comment
```

```text
cross-cutting decision

→ documentation / ADR
```

---

# 979. README

Debe explicar:

```text
what the project is

how to run it

where to find deeper docs
```

---

# 980. Module Documentation

Debe explicar behavior y boundaries del módulo.

---

# 981. ADR

Debe utilizarse para decisiones arquitectónicas significativas.

---

# 982. Documentation Drift

Debe tratarse como deuda.

---

# 983. Performance Coding Rules

La performance debe optimizarse con evidencia.

---

# 984. Performance Principle

```text
Measure first.

Optimize second.
```

---

# 985. Premature Optimization

Evitar complejidad significativa para una mejora no medida.

---

# 986. Common Performance Risks

```text
N+1 queries

unbounded collections

large payloads

repeated rendering

unnecessary network calls

excessive DOM work
```

---

# 987. Query Count

Debe considerarse en vistas complejas.

---

# 988. Dashboard

Especial atención porque combina múltiples fuentes.

---

# 989. Pagination

Aplicar antes de que listas crezcan indefinidamente.

---

# 990. Payload

Enviar únicamente datos necesarios.

---

# 991. Frontend Bundles

Mantener JavaScript contenido.

---

# 992. Dependency Cost

Cada library frontend aumenta:

```text
bundle

maintenance

security surface
```

---

# 993. Realtime Performance

No emitir eventos innecesarios.

---

# 994. Broadcast Scope

Enviar solo al contexto necesario.

---

# 995. Re-rendering

No reconstruir listas completas por un cambio pequeño salvo que simplifique significativamente consistencia.

---

# 996. Caching

Solo con evidencia.

---

# 997. Dependency Management

Cada dependencia debe justificar su coste.

---

# 998. Dependency Questions

```text
What problem does it solve?

Can the standard library solve it?

Is it maintained?

Is it secure?

What is its license?

How difficult is replacement?
```

---

# 999. New Dependency

Debe evitarse para una utilidad trivial.

---

# 1000. Example

No añadir una library completa para:

```text
format one date
```

si la solución estándar es suficiente.

---

# 1001. Version Pinning

Seguir la estrategia de dependency management del proyecto.

---

# 1002. Major Upgrade

Debe revisar:

```text
breaking changes

security

runtime behavior

tests
```

---

# 1003. Dependency Removal

Eliminar dependencies no utilizadas.

---

# 1004. Supply Chain

Las dependencias aumentan superficie de riesgo.

---

# 1005. Technical Debt Coding Rules

La deuda técnica debe ser explícita.

---

# 1006. Debt Principle

```text
Temporary is acceptable.

Invisible permanent temporary code is not.
```

---

# 1007. Acceptable Debt

Debe ser:

```text
known

bounded

documented when meaningful

revisitable
```

---

# 1008. Debt Example

```text
Realtime remains process-local until horizontal scaling is required.
```

---

# 1009. Bad Debt

Un workaround sin comentario, Issue ni contexto que nadie entiende posteriormente.

---

# 1010. Refactoring

Debe mejorar estructura sin cambiar comportamiento observable salvo intención explícita.

---

# 1011. Refactor Protection

Los tests deben reducir riesgo.

---

# 1012. Refactor Scope

Evitar refactor transversal innecesario dentro de una feature pequeña.

---

# 1013. Boy Scout Rule

Puede mejorarse código cercano si:

```text
change is small

safe

relevant
```

---

# 1014. Boy Scout Guardrail

No convertir cada feature en una reescritura del módulo.

---

# 1015. Deprecated Code

Debe retirarse cuando ya no tenga consumidores.

---

# 1016. Compatibility Layer

Puede mantenerse temporalmente con trigger de retirada.

---

# 1017. Magic Values

Evitar strings y números significativos dispersos.

---

# 1018. Extract Constants

Cuando el valor tenga significado de dominio o configuración.

---

# 1019. Example

```python
MAX_UPLOAD_SIZE_BYTES
```

---

# 1020. Configuration vs Constant

Si puede variar por entorno:

```text
configuration
```

no constante hardcoded.

---

# 1021. Environment Variables

Deben utilizarse para configuración externa apropiada.

---

# 1022. Environment Variable Naming

Utilizar nombres explícitos y consistentes.

---

# 1023. Missing Required Config

Debe fallar claramente al startup cuando sea crítica.

---

# 1024. Secret Defaults

No proporcionar defaults inseguros para secretos en producción.

---

# 1025. Development Defaults

Pueden existir solo si están claramente limitados al entorno local.

---

# 1026. Error Handling Final Rules

Los errores deben conservar:

```text
correct state

useful user feedback

diagnostic context
```

---

# 1027. Error Translation

Puede ocurrir:

```text
Infrastructure error

↓

Application error

↓

HTTP / UI response
```

---

# 1028. Error Leakage

No mostrar stack trace interno al usuario.

---

# 1029. Error IDs

Puede proporcionarse un correlation/request ID para soporte.

---

# 1030. User-facing Error

Debe utilizar lenguaje funcional.

---

# 1031. Developer-facing Error

Los logs pueden contener contexto técnico adicional seguro.

---

# 1032. Resilience

Los fallos de capabilities secundarias deben degradarse razonablemente.

---

# 1033. Example

Si realtime falla:

```text
core persisted operation may still succeed
```

---

# 1034. Example

Si Analytics falla:

```text
Project editing should remain available
```

---

# 1035. Core Dependency

Las dependencias críticas sí deben producir fallo claro.

---

# 1036. Fail Fast

Configuración crítica inválida debe detectarse al startup cuando sea posible.

---

# 1037. Feature Flags

Si se introducen, deben tener lifecycle.

---

# 1038. Temporary Flag

Debe retirarse tras rollout.

---

# 1039. Flag Guardrail

No utilizar flags para mantener dos arquitecturas permanentemente sin necesidad.

---

# 1040. Security Checklist

Antes de considerar una feature lista:

- [ ] La autenticación está aplicada donde corresponde.
- [ ] La autorización se valida en backend.
- [ ] Los IDs manipulables están validados.
- [ ] Los campos protegidos no dependen del cliente.
- [ ] Se ha considerado CSRF.
- [ ] El output no introduce XSS.
- [ ] Los uploads están protegidos si existen.
- [ ] Los eventos realtime respetan scope.
- [ ] Los logs no contienen secretos.

---

# 1041. Backend Checklist

- [ ] La lógica está en la capa correcta.
- [ ] El service representa un caso de uso claro.
- [ ] La transacción tiene boundary definido.
- [ ] No existen commits intermedios innecesarios.
- [ ] Las relaciones ORM son explícitas.
- [ ] Las invariantes importantes están protegidas.
- [ ] Las queries están acotadas.
- [ ] Los errores tienen semántica clara.
- [ ] El código dispone de type hints razonables.

---

# 1042. Database Checklist

- [ ] Foreign Keys correctas.
- [ ] Nullability deliberada.
- [ ] Unique constraints cuando corresponda.
- [ ] Índices para queries relevantes.
- [ ] Ordering determinista.
- [ ] Concurrencia evaluada.
- [ ] Migration reproducible.
- [ ] No existe pérdida de datos accidental.

---

# 1043. Schema Checklist

- [ ] Input schema no acepta campos internos.
- [ ] Output schema no expone datos innecesarios.
- [ ] Structural validation está en boundary.
- [ ] Business validation permanece en service/domain.
- [ ] Enums representan conjuntos realmente cerrados.
- [ ] `None` está representado explícitamente.

---

# 1044. SSR Checklist

- [ ] Template no contiene lógica de negocio compleja.
- [ ] El contexto es explícito.
- [ ] User content está escaped.
- [ ] Existe empty state.
- [ ] Las acciones visibles respetan permissions.
- [ ] Los forms preservan input tras error.
- [ ] Los mensajes de error son comprensibles.

---

# 1045. JavaScript Checklist

- [ ] JavaScript aporta valor real.
- [ ] No recrea innecesariamente comportamiento SSR.
- [ ] Los listeners no se duplican.
- [ ] Los DOM selectors son estables.
- [ ] `fetch()` gestiona respuestas no OK.
- [ ] Existe loading state.
- [ ] Existe recovery tras error.
- [ ] No hay globals innecesarios.
- [ ] No quedan logs de debug.

---

# 1046. Accessibility Checklist

- [ ] Semantic HTML.
- [ ] Labels correctos.
- [ ] Navegación por teclado.
- [ ] Focus visible.
- [ ] Dialog focus correcto.
- [ ] Drag-and-drop tiene alternativa.
- [ ] Estado no depende solo del color.
- [ ] Icon buttons tienen accessible name.
- [ ] Dynamic updates no generan ruido.
- [ ] Responsive no elimina información crítica.

---

# 1047. Realtime Checklist

- [ ] Evento tiene contrato claro.
- [ ] El resource scope está definido.
- [ ] El recipient está autorizado.
- [ ] El commit ocurre antes del broadcast.
- [ ] Delivery failure no invalida persistencia.
- [ ] Duplicados son tolerables.
- [ ] Reconnect tiene backoff.
- [ ] Existe reconciliación cuando procede.
- [ ] Los tests cubren múltiples clientes si aplica.

---

# 1048. Testing Checklist

- [ ] Happy path.
- [ ] Negative path.
- [ ] Authorization.
- [ ] Validation.
- [ ] Regression si corrige un bug.
- [ ] Database integration cuando aplica.
- [ ] No depende de execution order.
- [ ] No utiliza sleeps arbitrarios.
- [ ] Fixtures son comprensibles.
- [ ] Test name describe behavior.

---

# 1049. Observability Checklist

- [ ] Los fallos importantes pueden diagnosticarse.
- [ ] Los logs tienen contexto suficiente.
- [ ] No contienen datos sensibles.
- [ ] Las métricas tienen cardinalidad controlada.
- [ ] Los errors no se registran duplicadamente.
- [ ] Existe correlation cuando aporta valor.

---

# 1050. Git / PR Checklist

- [ ] Rama con propósito claro.
- [ ] Commits coherentes.
- [ ] Mensajes descriptivos.
- [ ] PR acotado.
- [ ] Tests indicados.
- [ ] Security impact señalado.
- [ ] Migration señalada.
- [ ] Screenshots si cambia UI.
- [ ] Documentación actualizada.

---

# 1051. Code Review Checklist

- [ ] Correctness.
- [ ] Authorization.
- [ ] Data integrity.
- [ ] Transaction boundary.
- [ ] Error handling.
- [ ] Testing.
- [ ] Readability.
- [ ] Observability.
- [ ] Performance when relevant.
- [ ] No unnecessary complexity.

---

# 1052. Coding Anti-pattern — Fat Router

```text
HTTP

+

business logic

+

database

+

authorization

+

notifications
```

todo en la misma función.

---

# 1053. Coding Anti-pattern — God Service

Un service que conoce todos los módulos.

---

# 1054. Coding Anti-pattern — Generic Utils Dump

Funciones sin ownership acumuladas en `utils.py`.

---

# 1055. Coding Anti-pattern — Generic Repository Everything

Abstracción que oculta todas las queries bajo CRUD genérico.

---

# 1056. Coding Anti-pattern — Business Logic in Template

Reglas de acceso y estado dentro de Jinja.

---

# 1057. Coding Anti-pattern — JavaScript as Security

Confiar en hidden/disabled buttons.

---

# 1058. Coding Anti-pattern — ORM Serialization Everywhere

Exponer modelos directamente sin contrato.

---

# 1059. Coding Anti-pattern — Commit Everywhere

Cada helper llama `db.commit()` independientemente.

---

# 1060. Coding Anti-pattern — Broadcast before Commit

Realtime anuncia estado no persistido.

---

# 1061. Coding Anti-pattern — Silent Exception

```python
except Exception:
    pass
```

---

# 1062. Coding Anti-pattern — Catch Everything

Convertir todos los errores en la misma respuesta.

---

# 1063. Coding Anti-pattern — Unbounded Query

```text
SELECT all historical notifications
```

sin límite.

---

# 1064. Coding Anti-pattern — Client-owned Security Fields

Aceptar:

```text
owner_id

created_by

is_admin
```

desde un form/request cuando deben derivarse del contexto.

---

# 1065. Coding Anti-pattern — Fragile DOM

Depender de estructura HTML incidental.

---

# 1066. Coding Anti-pattern — Fixed Sleeps

Especialmente en UI/realtime tests.

---

# 1067. Coding Anti-pattern — Test Implementation Details

Probar llamadas internas que no forman parte del comportamiento.

---

# 1068. Coding Anti-pattern — Mock Everything

Suite que nunca utiliza persistencia real.

---

# 1069. Coding Anti-pattern — Coverage Gaming

Tests sin valor para elevar porcentaje.

---

# 1070. Coding Anti-pattern — Dependency for Every Problem

Añadir librerías para utilidades pequeñas.

---

# 1071. Coding Anti-pattern — Premature Distributed Architecture

Añadir:

```text
Kafka

Redis

microservices
```

sin necesidad.

---

# 1072. Coding Anti-pattern — Premature Caching

Crear estado duplicado sin estrategia de invalidación.

---

# 1073. Coding Anti-pattern — Inline Everything

CSS y JS dispersos en templates.

---

# 1074. Coding Anti-pattern — Magic Permission Strings

Strings de roles/permissions repetidos.

---

# 1075. Coding Anti-pattern — Audit = Logs

Asumir que los logs técnicos proporcionan auditoría durable.

---

# 1076. Coding Anti-pattern — Realtime = Source of Truth

Confiar en eventos sin reconciliación.

---

# 1077. Coding Anti-pattern — Huge PR

Cambios funcionales, refactor, formatting y arquitectura mezclados.

---

# 1078. Coding Anti-pattern — Stale TODO

TODO antiguo sin contexto ni tracking.

---

# 1079. Coding Anti-pattern — Commented-out Code

Código muerto conservado "por si acaso".

---

# 1080. Coding Anti-pattern — Abstract before Understanding

Interfaces y factories creadas sin variabilidad real.

---

# 1081. Definition of Ready for Implementation

Una feature está preparada para desarrollo cuando:

- [ ] el comportamiento esperado es comprensible;
- [ ] el módulo responsable está identificado;
- [ ] las reglas principales son conocidas;
- [ ] autorización está definida;
- [ ] implicaciones de datos están entendidas;
- [ ] existen acceptance criteria;
- [ ] no existe una decisión arquitectónica crítica abierta.

---

# 1082. Definition of Done — Code

La implementación está completa cuando:

- [ ] código cumple convenciones;
- [ ] no existen findings críticos conocidos;
- [ ] lógica está en la capa adecuada;
- [ ] autorización server-side existe;
- [ ] validación está aplicada;
- [ ] transacciones son coherentes;
- [ ] errores se gestionan;
- [ ] tests relevantes pasan;
- [ ] observabilidad suficiente existe;
- [ ] documentación necesaria está actualizada.

---

# 1083. Definition of Done — Backend

- [ ] Service behavior definido.
- [ ] ORM relationships correctas.
- [ ] Constraints evaluados.
- [ ] Query scope correcto.
- [ ] Authorization testada.
- [ ] Error mapping correcto.
- [ ] Audit aplicado cuando corresponde.

---

# 1084. Definition of Done — Frontend

- [ ] SSR baseline funciona.
- [ ] Progressive enhancement funciona.
- [ ] Loading state.
- [ ] Error state.
- [ ] Success feedback.
- [ ] Keyboard access.
- [ ] Responsive behavior.
- [ ] Realtime state recovery si aplica.

---

# 1085. Definition of Done — Realtime

- [ ] Event contract.
- [ ] Authorized routing.
- [ ] Commit-before-broadcast.
- [ ] Failure behavior.
- [ ] Duplicate tolerance.
- [ ] Reconnect.
- [ ] Reconciliation.
- [ ] Tests.

---

# 1086. Definition of Done — Database Change

- [ ] Migration.
- [ ] Constraint review.
- [ ] Index review.
- [ ] Existing data considered.
- [ ] Rollback implications understood.
- [ ] CI migration validation.
- [ ] No accidental destructive change.

---

# 1087. Definition of Done — Security-sensitive Change

- [ ] Threat considered.
- [ ] Server authorization.
- [ ] Negative tests.
- [ ] Input validation.
- [ ] Output safety.
- [ ] Logging safety.
- [ ] Audit if relevant.
- [ ] No secret exposure.

---

# 1088. Coding Quality Dimensions

Todo código debe buscar equilibrio entre:

```text
Correctness

Clarity

Security

Maintainability

Testability

Observability

Performance
```

---

# 1089. Correctness

El código debe hacer lo esperado.

---

# 1090. Clarity

Debe ser comprensible.

---

# 1091. Security

Debe respetar fronteras de confianza.

---

# 1092. Maintainability

Debe poder modificarse con coste razonable.

---

# 1093. Testability

Debe permitir demostrar comportamiento.

---

# 1094. Observability

Debe permitir diagnosticar fallos.

---

# 1095. Performance

Debe ser suficientemente eficiente para las necesidades reales.

---

# 1096. Trade-offs

No todas las dimensiones pueden maximizarse simultáneamente.

---

# 1097. Trade-off Principle

Cuando exista trade-off importante:

```text
make it explicit
```

---

# 1098. Example

Una re-fetch tras reconnect puede ser menos eficiente que aplicar eventos perdidos, pero inicialmente puede ser:

```text
simpler

safer

more correct
```

---

# 1099. Architecture Alignment

El código debe respetar las decisiones recogidas en:

```text
52_ARCHITECTURAL_DECISIONS.md
```

y ADRs futuros.

---

# 1100. Rule Conflict

Si una regla de este documento contradice una decisión arquitectónica explícita más reciente:

```text
architectural decision wins
```

y este documento debe actualizarse.

---

# 1101. Static Analysis Alignment

Ruff y SonarCloud deben apoyar estas reglas.

---

# 1102. Automated Enforcement

Siempre que una regla pueda verificarse automáticamente de forma fiable:

```text
prefer automation
```

---

# 1103. Human Review

Las herramientas no pueden sustituir evaluación de:

```text
architecture

business correctness

security intent

UX quality
```

---

# 1104. Coding Rules Evolution

Estas reglas deben evolucionar con la plataforma.

---

# 1105. Change Criteria

Actualizar cuando:

- una nueva arquitectura lo requiera;
- se adopte una herramienta;
- aparezca un patrón repetido;
- una regla deje de ser útil;
- una incidencia revele una carencia.

---

# 1106. Avoid Rule Accumulation

No añadir reglas por cada bug aislado.

---

# 1107. Generalizable Learning

Una nueva regla debe representar aprendizaje reutilizable.

---

# 1108. Exceptions

Puede existir una excepción legítima.

---

# 1109. Exception Principle

```text
Understand the rule

before breaking the rule.
```

---

# 1110. Exception Requirements

Una excepción significativa debe ser:

```text
intentional

local

understandable

justifiable
```

---

# 1111. Final Coding Principles

1. Optimizar para comprensión.
2. Mantener responsabilidades claras.
3. Evitar lógica de negocio en routers y templates.
4. Mantener Services independientes de HTTP.
5. Validar en boundaries.
6. Aplicar autorización en servidor.
7. Proteger invariantes también en base de datos cuando corresponda.
8. Mantener transacciones coherentes.
9. Persistir antes de emitir realtime.
10. Tratar realtime como mejora, no como fuente de verdad.
11. Mantener JavaScript progresivo y localizado.
12. Diseñar accesibilidad desde el inicio.
13. Escribir tests sobre comportamiento.
14. Considerar los tests flaky como defectos.
15. Registrar logs útiles sin información sensible.
16. Medir antes de optimizar.
17. Añadir dependencies solo cuando aporten valor.
18. Mantener Git y PRs revisables.
19. Hacer visible Technical Debt significativa.
20. Evitar complejidad hasta que el problema la justifique.

---

# 1112. Core Engineering Rule

```text
Make the correct behavior

the easiest behavior

to understand, test and maintain.
```

---

# 1113. Architecture Rule

```text
Put behavior

where its responsibility belongs.
```

---

# 1114. Security Rule

```text
Never trust the client

to enforce server rules.
```

---

# 1115. Data Rule

```text
Protect important invariants

at the strongest practical layer.
```

---

# 1116. Realtime Rule

```text
Persist first.

Broadcast second.

Reconcile when uncertain.
```

---

# 1117. Frontend Rule

```text
SSR for the baseline.

JavaScript for enhancement.

Realtime for freshness.
```

---

# 1118. Testing Rule

```text
Confidence comes from meaningful validation

not from test count.
```

---

# 1119. Observability Rule

```text
If a critical behavior can fail,

there must be a practical way to understand why.
```

---

# 1120. Dependency Rule

```text
Every dependency becomes part of the system you maintain.
```

---

# 1121. Performance Rule

```text
Measure before optimizing.
```

---

# 1122. Refactoring Rule

```text
Improve structure

without expanding scope unnecessarily.
```

---

# 1123. Review Rule

```text
Review for correctness first.

Style second.
```

---

# 1124. Documentation Rule

```text
Document decisions and stable knowledge.

Let code describe implementation.
```

---

# 1125. Simplicity Rule

```text
Choose the simplest design

that protects current requirements

and leaves reasonable room to evolve.
```

---

# 1126. Final Engineering Standard

El código de Aula Robótica Platform debe aspirar a que cada cambio pueda responder afirmativamente:

```text
Is it correct?

Is it secure?

Is it understandable?

Is it in the right place?

Can it be tested?

Can it be diagnosed?

Can it evolve?
```

---

# 1127. Coding Rules Summary

La estrategia completa puede resumirse:

```text
Clear Domain Boundaries

+

Thin HTTP Layer

+

Explicit Services

+

Relational Integrity

+

Server-side Authorization

+

SSR-first UI

+

Progressive Enhancement

+

Reliable Realtime

+

Meaningful Tests

+

Observable Operations
```

---

# 1128. End of Document

**Aula Robótica Platform — Coding Rules**

```text
Clear code.

Explicit boundaries.

Secure behavior.

Reliable state.

Meaningful tests.

Sustainable evolution.
```