# 55_CHANGELOG.md

# Aula Robótica Platform — Changelog

## Parte 1/3 — Propósito, principios, formato, versionado, categorías, gobernanza y estructura del historial

---

# 1. Propósito

Este documento mantiene el historial oficial de cambios relevantes de:

```text
Aula Robótica Platform
```

y permite conocer de forma estructurada:

```text
what changed

when it changed

in which version

and

what kind of change it was
```

---

# 2. Primary Objective

El objetivo principal es proporcionar un registro:

```text
chronological

version-oriented

human-readable

maintainable

traceable
```

de la evolución funcional y técnica de la plataforma.

---

# 3. Nature of this Document

`55_CHANGELOG.md` es:

```text
a release-oriented historical record
```

---

# 4. Core Question

Este documento debe responder:

```text
What changed between versions of Aula Robótica Platform?
```

---

# 5. It Is Not

No debe utilizarse como:

```text
current task tracker

product backlog

technical debt registry

known issue registry

architectural decision log

Git commit history replacement

weekly status report
```

---

# 6. Conceptual Separation

La separación entre documentos es:

```text
CHANGELOG

→ what changed


CURRENT_TASKS

→ what is being worked on now


KNOWN_ISSUES

→ what is currently wrong or limited


TECHNICAL_DEBT

→ what structural compromises remain


PRODUCT_ROADMAP

→ where the product is heading


FEATURE_BACKLOG

→ what capabilities may be built


ARCHITECTURAL_DECISIONS

→ why stable technical decisions exist
```

---

# 7. Historical Role

El Changelog debe permitir reconstruir la evolución del producto sin necesitar revisar:

```text
hundreds of commits

closed tasks

pull requests

temporary branches
```

---

# 8. Git History Relationship

Git sigue siendo la fuente detallada de:

```text
individual code changes

authors

commits

diffs

branches
```

---

# 9. Changelog Relationship

El Changelog sintetiza esos cambios en:

```text
meaningful product and engineering evolution
```

---

# 10. Historical Truth Principle

El Changelog debe preservar una distinción estricta entre:

```text
verified historical change

candidate changelog entry

planned capability

future architecture
```

La regla fundamental es:

```text
Verified historical change
    → may appear as completed history

Candidate / example entry
    → template only

Planned capability
    → never historical fact

Future architecture
    → never historical fact
```

---

# 11. Evidence Principle

Una capability solo debe presentarse como entregada cuando exista evidencia suficiente mediante uno o varios de los siguientes elementos:

```text
verified application code

repository history

merged implementation

automated tests

runtime configuration

deployment evidence

release tag

validated project documentation
```

---

# 12. Documentation Is Not Implementation

La existencia de:

```text
architecture documentation

design document

roadmap entry

future-evolution section

candidate changelog entry
```

no constituye por sí misma evidencia de implementación.

---

# 13. Example

Git puede contener:

```text
fix typo

rename helper

add test

update import

refactor function

adjust CSS
```

mientras el Changelog puede registrar:

```text
Improved Task authorization and added regression coverage
for cross-project access.
```

si ese cambio está realmente implementado.

---

# 14. Changelog Audience

Está dirigido principalmente a:

```text
maintainers

developers

reviewers

operators

future contributors

technical evaluators
```

---

# 15. Secondary Audience

También puede resultar útil para:

```text
product stakeholders

project reviewers

portfolio evaluators
```

cuando necesiten comprender la evolución del sistema.

---

# 16. Changelog Philosophy

El documento debe seguir el principio:

```text
curated history

not

raw activity stream
```

---

# 17. Inclusion Principle

Registrar cambios que sean relevantes para comprender:

```text
product capabilities

behavior

security

architecture

operations

data model

developer workflow
```

---

# 18. Exclusion Principle

No registrar automáticamente:

```text
every commit

every typo

every formatting change

every import

every variable rename

every internal cleanup
```

---

# 19. Meaningful Change

Un cambio merece normalmente aparecer cuando afecta a:

```text
users

developers

operators

security posture

system behavior

architecture

deployment

data compatibility
```

---

# 20. Changelog Granularity

La unidad principal del Changelog es:

```text
release
```

---

# 21. Release Entry

Cada release agrupa:

```text
related meaningful changes
```

realizados desde la versión anterior.

---

# 22. Unreleased Work

El documento debe disponer de:

```text
[Unreleased]
```

para cambios ya integrados pero todavía no publicados en una release estable.

---

# 23. Unreleased Meaning

`Unreleased` significa:

```text
merged / integrated

but

not yet part of a released version
```

---

# 24. Not Current Tasks

No deben añadirse a `Unreleased` trabajos que únicamente estén:

```text
planned

assigned

in progress

under discussion
```

---

# 25. Source Document for Active Work

Ese estado pertenece a:

```text
53_CURRENT_TASKS.md
```

---

# 26. Source Document for Planned Work

El trabajo futuro pertenece principalmente a:

```text
47_PRODUCT_ROADMAP.md

49_FEATURE_BACKLOG.md
```

---

# 27. Changelog Format

La estructura recomendada sigue:

```text
Keep a Changelog

+

Semantic Versioning
```

adaptados al proyecto.

---

# 28. Top-level Structure

```markdown
# Changelog

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [X.Y.Z] — YYYY-MM-DD

...
```

---

# 29. Standard Categories

Las categorías principales son:

```text
Added

Changed

Deprecated

Removed

Fixed

Security
```

---

# 30. Added

Utilizar para:

```text
new capabilities

new modules

new endpoints

new workflows

new infrastructure capabilities
```

---

# 31. Added Example

```markdown
### Added

- Added persistent user notifications with unread state.
- Added project activity feed.
- Added WebSocket delivery for selected realtime events.
```

---

# 32. Changed

Utilizar para cambios significativos sobre comportamiento existente.

---

# 33. Changed Example

```markdown
### Changed

- Changed Task authorization to use project-scoped contextual policies.
- Changed realtime reconnect behavior to reconcile authoritative server state.
```

Estas entradas son ejemplos de formato y no deben interpretarse como evidencia de que dichas capabilities estén ya implementadas.

---

# 34. Deprecated

Utilizar cuando una capability sigue disponible temporalmente pero:

```text
should no longer be adopted

and

is expected to disappear
```

---

# 35. Deprecated Example

```markdown
### Deprecated

- Deprecated legacy direct role checks in project-scoped workflows.
```

---

# 36. Removed

Utilizar para capacidades eliminadas.

---

# 37. Removed Example

```markdown
### Removed

- Removed legacy native confirmation flow from destructive Task actions.
```

---

# 38. Fixed

Utilizar para defectos corregidos.

---

# 39. Fixed Example

```markdown
### Fixed

- Fixed stale Task state after WebSocket reconnect.
- Fixed duplicate unread-count increments caused by repeated notification events.
```

Estas entradas representan ejemplos de redacción.

Solo deben convertirse en historial real después de una implementación y validación verificadas.

---

# 40. Security

Utilizar para cambios que:

```text
close vulnerabilities

harden boundaries

strengthen authentication

strengthen authorization

improve sensitive-data handling
```

---

# 41. Security Example

```markdown
### Security

- Added project-scoped authorization for nested resources.
- Added explicit authorization for WebSocket subscriptions.
- Added CSRF protection to authenticated browser mutations.
```

Estas capabilities pertenecen al hardening objetivo mientras no exista evidencia de su implementación completa.

---

# 42. Security Category Priority

Cuando un cambio es principalmente de seguridad, preferir:

```text
Security
```

aunque técnicamente también pudiera considerarse:

```text
Changed

or

Fixed
```

---

# 43. Avoid Duplicate Entries

No repetir el mismo cambio en varias categorías salvo que exista una razón clara.

---

# 44. Category Decision

Preguntar:

```text
What is the most important meaning of this change?
```

---

# 45. Example

Una corrección de autorización podría ser:

```text
Fixed
```

si corrige un bug menor.

---

# 46. Security-sensitive Example

Pero si corrige:

```text
cross-project authorization bypass
```

debe aparecer preferentemente en:

```text
Security
```

---

# 47. Versioning Model

Aula Robótica Platform debe utilizar:

```text
Semantic Versioning
```

con formato:

```text
MAJOR.MINOR.PATCH
```

---

# 48. Example Versions

```text
0.1.0

0.2.0

0.3.0

1.0.0

1.1.0

1.1.1

2.0.0
```

---

# 49. Pre-1.0 Interpretation

Mientras la plataforma permanezca en:

```text
0.x.y
```

el producto puede seguir evolucionando con mayor libertad.

---

# 50. Pre-1.0 Guardrail

Esto no significa:

```text
versioning does not matter
```

---

# 51. Pre-1.0 Meaning

Incluso antes de `1.0.0`, las versiones deben comunicar evolución significativa.

---

# 52. MAJOR

Tras alcanzar estabilidad pública:

```text
MAJOR
```

debe incrementarse cuando existan cambios incompatibles relevantes.

---

# 53. Candidate Major Changes

```text
breaking public API

breaking deployment model

major authentication contract change

incompatible data contract

removal of supported behavior
```

---

# 54. MINOR

Incrementar:

```text
MINOR
```

para nuevas capabilities compatibles.

---

# 55. Candidate Minor Changes

```text
new module

new workflow

new endpoint

new dashboard capability

new realtime capability
```

---

# 56. PATCH

Incrementar:

```text
PATCH
```

para correcciones compatibles.

---

# 57. Candidate Patch Changes

```text
bug fixes

security patches

small reliability fixes

small performance corrections
```

---

# 58. Pre-1.0 Practical Rule

Durante `0.x` puede utilizarse:

```text
0.MINOR.PATCH
```

de forma pragmática.

---

# 59. Example

```text
0.8.0

→ new major internal capability


0.8.1

→ bug fixes


0.9.0

→ next significant capability set
```

---

# 60. Version Source of Truth

La versión publicada debe ser coherente entre:

```text
Git tag

release artifact

application metadata

Changelog
```

cuando esos mecanismos existan.

---

# 61. Release Date

Cada release estable debe utilizar su fecha real de publicación.

Formato recomendado:

```text
YYYY-MM-DD
```

---

# 62. Example

```markdown
## [0.9.0] — 2026-09-14
```

---

# 63. Date Integrity

No inventar fechas para completar artificialmente el historial.

---

# 64. Unknown Historical Date

Si una fase histórica es conocida pero no existe fecha fiable:

```text
do not fabricate one.
```

---

# 65. Release Integrity

No inventar versiones para convertir fases conceptuales en releases aparentemente reales.

---

# 66. Historical Reconstruction

Cuando el historial exacto no esté disponible, es preferible utilizar:

```text
historical phase

or

validated capability group
```

que fabricar una release.

---

# 67. Changelog Entry Style

Cada entrada debe ser:

```text
concise

specific

meaningful

user/developer oriented
```

---

# 68. Preferred Grammar

Preferir frases como:

```text
Added ...

Changed ...

Fixed ...

Removed ...

Hardened ...

Improved ...
```

---

# 69. Avoid Weak Wording

Evitar:

```text
Worked on...

Made changes to...

Updated some...

Various improvements...
```

---

# 70. Good Entry

```markdown
- Added persistent unread state to in-app notifications.
```

---

# 71. Weak Entry

```markdown
- Worked on notifications.
```

---

# 72. Describe Outcome

El Changelog debe describir:

```text
result
```

más que:

```text
implementation activity.
```

---

# 73. Internal Detail

Evitar detalles demasiado internos salvo que sean importantes para:

```text
compatibility

operations

security

architecture
```

---

# 74. Example Internal Detail

No es necesario registrar:

```text
renamed helper from X to Y
```

salvo que forme parte de una API pública.

---

# 75. Technical Precision

Aunque sea conciso, el wording debe ser técnicamente correcto.

---

# 76. Architecture Claims

Una entrada no debe afirmar:

```text
completed architecture
```

si únicamente se implementó una parte.

---

# 77. Example

Evitar:

```markdown
- Completed contextual authorization architecture.
```

si únicamente se añadió una primera policy.

---

# 78. Better

```markdown
- Added contextual authorization to Project update and delete workflows.
```

---

# 79. Scope Precision

Preferir:

```text
exact delivered scope
```

sobre:

```text
broad architectural claim.
```

---

# 80. Historical State Vocabulary

Cuando sea necesario diferenciar estado documental:

```text
CURRENT

PARTIAL

TARGET

PLANNED

FUTURE

CONDITIONAL
```

---

# 81. CURRENT

Una capability puede tratarse como historial implementado cuando existe evidencia de que forma parte de la implementación real.

---

# 82. PARTIAL

Puede utilizarse en documentación explicativa cuando una capability existe parcialmente.

El Changelog debe describir exactamente la parte entregada.

---

# 83. TARGET

Una arquitectura objetivo:

```text
must not appear as completed history.
```

---

# 84. PLANNED

Trabajo aceptado pero todavía no entregado.

No pertenece al historial de releases.

---

# 85. FUTURE

Capacidad posible para una evolución posterior.

No pertenece al historial realizado.

---

# 86. CONDITIONAL

Capacidad cuya adopción depende de un trigger futuro.

No debe presentarse como parte del stack histórico implementado mientras ese trigger no se produzca.

---

# 87. Current Baseline Integrity

El Changelog debe respetar el baseline actualmente verificado:

```text
FastAPI
    CURRENT

SQLAlchemy
    CURRENT

MariaDB
    CURRENT

Jinja2 SSR
    CURRENT

Bootstrap / AdminLTE
    CURRENT

JWT Access Tokens
    CURRENT

JWT Refresh Tokens
    CURRENT

HTTPOnly Cookies
    CURRENT

RBAC
    CURRENT

WebSockets
    CURRENT

Docker / Docker Compose
    CURRENT

Nginx
    CURRENT

Ubuntu / Hetzner VPS
    CURRENT
```

---

# 88. Non-current Capability Integrity

Las siguientes capacidades no deben aparecer como historia implementada salvo evidencia futura que cambie su estado:

```text
SAML
    FUTURE

PostgreSQL
    FUTURE / CANDIDATE

Redis
    CONDITIONAL

Kubernetes
    CONDITIONAL

Microservices
    CONDITIONAL

PWA
    FUTURE

AI / RAG
    FUTURE / EXPERIMENTAL

Multi-tenancy
    FUTURE / CONDITIONAL
```

---

# 89. Partial / Evolving Capability Integrity

Las siguientes áreas requieren especial precisión:

```text
Contextual Authorization
    PARTIAL / IN PROGRESS

ProjectMembership
    TARGET / IN CONSOLIDATION

Kanban
    PLANNED

Realtime Reconnect / Reconciliation
    IN PROGRESS / TARGET HARDENING

CSRF Hardening
    PENDING / IN PROGRESS

Refresh-token Security Hardening
    PENDING / IN PROGRESS

WebSocket Security Hardening
    IN PROGRESS
```

---

# 90. Refresh Token Historical Rule

Debe distinguirse:

```text
JWT Refresh Token Support
    IMPLEMENTED

Refresh-token Workflow
    IMPLEMENTED

Explicit Refresh Endpoint
    IMPLEMENTED

Automatic Access-token Refresh
    IMPLEMENTED

Refresh-token Rotation
    NOT YET VERIFIED AS IMPLEMENTED

Server-side Revocation
    NOT YET VERIFIED AS IMPLEMENTED

Reuse Detection
    NOT YET VERIFIED AS IMPLEMENTED
```

---

# 91. Refresh Token Changelog Example

Es históricamente válido, cuando corresponda a una fase verificada, registrar:

```markdown
### Security

- Added refresh-token support for browser authentication workflows.
```

---

# 92. Refresh Hardening Candidate

No debe registrarse como completado mientras no se implemente:

```markdown
### Security

- Added refresh-token rotation and reuse detection.
```

---

# 93. SAML Historical Rule

La existencia de documentación SAML no significa:

```text
SAML was implemented.
```

Por tanto, SAML no debe incluirse dentro de un grupo de capabilities históricamente entregadas.

---

# 94. PostgreSQL Historical Rule

La base de datos actual es:

```text
MariaDB
```

No existe una migración implementada:

```text
MariaDB → PostgreSQL
```

Por tanto, el Changelog no debe describir:

```text
PostgreSQL adoption

PostgreSQL standardization

PostgreSQL migration
```

como historia completada.

---

# 95. Candidate PostgreSQL Entry

Solo después de una migración real podría existir una entrada como:

```markdown
### Changed

- Migrated the primary relational persistence engine from MariaDB to PostgreSQL.
```

Hasta entonces esa entrada es únicamente:

```text
FUTURE EXAMPLE
```

---

# 96. Breaking Changes

Los breaking changes deben ser especialmente visibles.

---

# 97. Breaking Marker

Puede utilizarse:

```text
**Breaking:**
```

---

# 98. Example

```markdown
### Changed

- **Breaking:** Changed the public authentication contract and removed support for the previous token transport.
```

---

# 99. Breaking Change Requirements

Una entrada breaking debe explicar:

```text
what changed

who is affected

what migration is required
```

---

# 100. Migration Notes

Cuando una release requiera acción manual debe incluirla claramente.

---

# 101. Migration Note Example

```markdown
### Changed

- Added a required database migration for the new Project Membership model.

> Migration required before application startup.
```

---

# 102. Migration Integrity

Una migration planificada no debe registrarse como migration ejecutada.

---

# 103. Database Migration Context

Las migrations actuales deben corresponder al motor realmente utilizado:

```text
MariaDB
```

salvo que una release futura cambie explícitamente ese baseline.

---

# 104. Security Disclosure

El Changelog debe informar de mejoras de seguridad sin revelar información que facilite explotación innecesaria.

---

# 105. Good Security Entry

```markdown
### Security

- Hardened authorization checks for project-scoped resources.
```

---

# 106. Excessive Detail

Evitar publicar:

```text
exploit recipe

sensitive internal paths

credentials

secret structure

unnecessary attack details
```

---

# 107. CVE Relationship

Si alguna vulnerabilidad tuviera identificador formal:

```text
CVE
```

puede incluirse cuando corresponda.

---

# 108. Private Security Fixes

Puede ser necesario mantener wording deliberadamente general hasta completar despliegue.

---

# 109. Known Issues Relationship

Cuando una issue conocida se resuelve:

```text
54_KNOWN_ISSUES.md

↓

55_CHANGELOG.md
```

puede registrar la corrección.

---

# 110. Example

```markdown
### Fixed

- Fixed duplicate notification updates after repeated realtime events.
```

---

# 111. Known Issue Closure

Después de release:

```text
Known Issue

→ resolved / archived

Changelog

→ historical fix
```

---

# 112. Current Tasks Relationship

Una tarea no entra en el Changelog al empezar.

---

# 113. Correct Flow

```text
CURRENT_TASKS

↓

implementation

↓

validation

↓

integration

↓

CHANGELOG [Unreleased]

↓

release

↓

versioned history
```

---

# 114. Technical Debt Relationship

Resolver deuda técnica puede merecer una entrada si produce impacto relevante.

---

# 115. Example

```markdown
### Changed

- Consolidated authentication cookie handling to apply a consistent environment-aware security policy.
```

---

# 116. Internal Debt Cleanup

No toda deuda resuelta necesita entrada.

---

# 117. Example Exclusion

```text
renamed internal variable

moved helper

removed dead import
```

---

# 118. Architectural Decision Relationship

Una ADR o decisión arquitectónica:

```text
does not automatically belong in Changelog.
```

---

# 119. Decision vs Delivery

```text
Decision

→ architecture record


Implemented decision

→ possible changelog entry
```

---

# 120. Example

Decidir:

```text
PostgreSQL may be considered as a future persistence candidate
```

no genera una entrada histórica de migración.

---

# 121. Product Roadmap Relationship

Una capability del roadmap no pertenece al Changelog hasta que:

```text
is implemented

validated

and integrated.
```

---

# 122. Feature Backlog Relationship

Lo mismo aplica a ideas del backlog.

---

# 123. Documentation Changes

Los cambios de documentación pueden aparecer cuando son significativos.

---

# 124. Candidate Documentation Entry

```markdown
### Changed

- Reorganized the architecture documentation into domain-specific manuals.
```

---

# 125. Minor Documentation

No registrar cada corrección ortográfica.

---

# 126. Architecture Documentation

Puede registrarse cuando mejora materialmente:

```text
onboarding

operational safety

migration guidance

security understanding
```

---

# 127. Release Notes Relationship

El Changelog y las release notes pueden coexistir.

---

# 128. Changelog

Debe ser:

```text
structured

persistent

version-oriented
```

---

# 129. Release Notes

Pueden ser:

```text
more narrative

audience-specific

release-specific
```

---

# 130. Duplication Guardrail

Las release notes pueden derivarse del Changelog, pero no deberían contradecirlo.

---

# 131. Commit Relationship

No copiar mensajes de commit sin curación.

---

# 132. Pull Request Relationship

Un PR puede producir:

```text
zero

one

or several
```

entradas de Changelog.

---

# 133. Large PR

Un PR que implementa múltiples capabilities puede necesitar varias entradas.

---

# 134. Small PR

Un PR puramente interno puede no necesitar ninguna.

---

# 135. Release Branch Relationship

El Changelog debe reflejar la versión realmente publicada independientemente del workflow concreto de ramas.

---

# 136. Tag Relationship

El tag es una evidencia importante de release.

---

# 137. Tag Integrity

No registrar una versión como publicada si únicamente existe:

```text
planned version number
```

sin release real.

---

# 138. Historical Reconstruction Rule

Cuando no exista información suficiente:

```text
prefer uncertainty over invention.
```

---

# 139. Acceptable Historical Wording

```text
During the IAM expansion phase...
```

es preferible a inventar:

```text
Version 0.4.0 — 2025-03-12
```

si no existe evidencia.

---

# 140. Historical Capability Grouping

Cuando sea necesario reconstruir evolución previa, agrupar por:

```text
Application Foundation

IAM

Administration

Collaboration

Attachments

Awareness

Realtime

UI

Security

Testing

Operations
```

---

# 141. Historical Group Guardrail

Una capability solo debe entrar en el grupo histórico si está verificada como implementada.

---

# 142. Candidate Entries

Los ejemplos del documento deben etiquetarse conceptualmente como:

```text
candidate

example

future entry
```

cuando no representen hechos históricos.

---

# 143. Why Candidate Entries Exist

Permiten mantener:

```text
consistent wording

category guidance

future release quality
```

sin falsificar el historial.

---

# 144. Candidate Entry Lifecycle

```text
Candidate

↓

Capability implemented

↓

Validated

↓

Integrated

↓

Move/adapt into Unreleased

↓

Release
```

---

# 145. Candidate Entry Is Not Unreleased

Una entrada candidata no pertenece automáticamente a:

```text
[Unreleased]
```

---

# 146. Release Grouping

Una release debe agrupar cambios de forma comprensible.

---

# 147. Avoid Excessive Fragmentation

No crear una categoría nueva por cada módulo.

---

# 148. Standard Categories First

Preferir:

```text
Added

Changed

Deprecated

Removed

Fixed

Security
```

---

# 149. Module Names

Los módulos pueden identificarse dentro del texto.

---

# 150. Example

```markdown
### Added

- Added persistent Notifications with unread state.
- Added Activity Feed integration for project collaboration events.
```

---

# 151. Release Summary

Para releases grandes puede añadirse una introducción breve.

---

# 152. Example

```markdown
## [0.X.0] — YYYY-MM-DD

This release expands collaboration and realtime awareness across the platform.
```

---

# 153. Summary Guardrail

No convertir el Changelog en:

```text
marketing release notes.
```

---

# 154. Technical Audience

La prioridad sigue siendo claridad técnica e histórica.

---

# 155. Migration Notes Placement

Las notas de migración deben colocarse cerca del cambio que las requiere.

---

# 156. Example

```markdown
### Added

- Added persistent Project Membership.

> Database migration required before deployment.
```

---

# 157. Operator Action

Debe destacarse cuando una release requiera:

```text
database migration

new environment variable

storage migration

manual data migration

configuration update
```

---

# 158. No-action Release

No es necesario añadir una sección:

```text
Migration
```

si no existe acción.

---

# 159. Environment Changes

Una nueva variable obligatoria merece entrada.

---

# 160. Example

```markdown
### Changed

- Added a required environment variable for external identity-provider configuration.

> Operator action required before enabling the integration.
```

---

# 161. Future Identity-provider Example

El ejemplo anterior no significa que exista actualmente:

```text
SAML

or

another federated identity provider.
```

Solo representa cómo documentar una integración futura si llega a implementarse.

---

# 162. Dependency Updates

No registrar automáticamente todas las actualizaciones de dependencias.

---

# 163. Significant Dependency Update

Sí puede registrarse cuando:

```text
fixes security issue

changes runtime behavior

requires migration

changes compatibility
```

---

# 164. Example

```markdown
### Security

- Updated a security-sensitive dependency to address a known vulnerability.
```

---

# 165. Dependency Noise

Evitar listas extensas de versiones sin valor para el lector.

---

# 166. Runtime Dependency Changes

Un cambio de:

```text
Python version

database driver

container base image
```

puede ser relevante.

---

# 167. Database Driver Integrity

Cualquier cambio de driver debe corresponder al motor de base de datos realmente utilizado.

Actualmente:

```text
MariaDB
```

---

# 168. Database Engine Change

Cambiar de motor relacional sería un cambio arquitectónico y operativo importante.

---

# 169. Candidate Database Migration Entry

Solo después de una migración realmente ejecutada:

```markdown
### Changed

- **Breaking:** Migrated the primary relational database from MariaDB to PostgreSQL.

> Database and deployment migration required.
```

---

# 170. Current Database Rule

Hasta que eso ocurra:

```text
MariaDB

=

CURRENT relational database
```

---

# 171. Realtime Contract Changes

Los contratos realtime deben tratarse como interfaces relevantes.

---

# 172. Example Future Contract Change

```markdown
### Changed

- Standardized realtime event envelopes around explicit event type, resource context, and payload fields.
```

Esta entrada solo debe promoverse a historial cuando la normalización se implemente.

---

# 173. Event Compatibility

Si existen consumidores internos dependientes del contrato, un cambio incompatible debe indicarse.

---

# 174. Example

```markdown
### Changed

- **Breaking:** Replaced legacy realtime payload shapes with the normalized event envelope.
```

---

# 175. Frontend Internal Changes

No registrar cada modificación CSS o JavaScript.

---

# 176. Significant Frontend Change

Sí registrar:

```text
new reusable UI architecture

major workflow redesign

accessibility improvement

new interaction model
```

cuando tenga impacto significativo.

---

# 177. Example

```markdown
### Changed

- Consolidated destructive actions around reusable confirmation dialogs and consistent asynchronous feedback.
```

---

# 178. Native Dialog Example

La eliminación de `alert()` o `confirm()` solo merece una entrada si forma parte de una mejora relevante de UX o arquitectura.

---

# 179. Storage Changes

Los cambios de storage son relevantes cuando afectan:

```text
persistence

deployment

backup

recovery

operator workflow
```

---

# 180. Current Attachment Storage

El almacenamiento actual debe describirse de acuerdo con la implementación real.

---

# 181. Object Storage Rule

Object storage permanece:

```text
FUTURE / CONDITIONAL
```

mientras no exista migración implementada.

---

# 182. Candidate Object Storage Entry

Solo después de una adopción real:

```markdown
### Changed

- Migrated attachment binary storage to S3-compatible object storage.
```

---

# 183. Backup Compatibility

Si una nueva capability introduce nuevos datos persistentes, debe comprobarse si backup/restore necesita actualización.

---

# 184. Example

```markdown
### Changed

- Extended backup procedures to include persistent attachment storage.
```

---

# 185. Observability Changes

Pueden aparecer cuando incorporan capacidades operativas significativas.

---

# 186. Example

```markdown
### Added

- Added realtime connection and subscription metrics for operational diagnostics.
```

---

# 187. Monitoring Changes

Ejemplo:

```markdown
### Added

- Added actionable alerts for application availability and sustained server errors.
```

---

# 188. Candidate Operational Entry Rule

Los ejemplos de observability y monitoring no deben interpretarse como capabilities existentes sin evidencia.

---

# 189. Logging Changes

No registrar pequeños ajustes de mensajes.

---

# 190. Significant Logging Change

Sí registrar:

```text
structured logging adoption

correlation IDs

sensitive-data redaction
```

cuando realmente se implementen.

---

# 191. Example

```markdown
### Security

- Added centralized redaction of authentication secrets from application logs.
```

---

# 192. Audit Changes

Los cambios de Audit son relevantes cuando modifican:

```text
business traceability

recorded events

retention

security evidence
```

---

# 193. Example

```markdown
### Added

- Added immutable audit events for project membership changes.
```

Si Project Membership todavía no está consolidado, esta entrada permanece únicamente como ejemplo futuro.

---

# 194. Testing Infrastructure

Puede aparecer cuando cambia materialmente la capacidad de validar el sistema.

---

# 195. Example

```markdown
### Added

- Added multi-client WebSocket integration testing for realtime authorization and reconnect behavior.
```

---

# 196. Candidate Testing Rule

Los tests todavía planificados no deben describirse como infraestructura ya disponible.

---

# 197. CI Changes

Registrar cuando alteran significativamente el quality gate.

---

# 198. Example

```markdown
### Changed

- Extended CI quality gates with security regression and migration validation.
```

---

# 199. Developer Experience

Cambios importantes de setup pueden aparecer.

---

# 200. Example

```markdown
### Changed

- Simplified local development startup through a unified containerized environment.
```

---

# 201. Minor DX Changes

No registrar cada script auxiliar.

---

# 202. Module Introduction

Cada nuevo módulo funcional importante debería aparecer.

---

# 203. Example Modules

```text
Notifications

Dashboard

Activity Feed

Academic

Inventory

Reservations
```

---

# 204. Module Status Guardrail

La lista anterior puede contener tanto módulos actuales como dominios futuros.

No debe interpretarse como inventario de implementación.

En particular, nuevos dominios como:

```text
Academic

Inventory

Reservations
```

deben permanecer como futuros mientras no exista implementación verificada.

---

# 205. Module Entry Example

```markdown
### Added

- Added the Notifications module with persistent unread state and realtime delivery.
```

---

# 206. Module Evolution

Cambios posteriores deben describir capability concreta.

---

# 207. Example

```markdown
### Changed

- Improved Notifications with idempotent read handling and reconnect state recovery.
```

---

# 208. Module Removal

Si alguna capability experimental se retira:

```markdown
### Removed

- Removed the experimental realtime dashboard refresh mechanism.
```

---

# 209. Changelog Entry Validation

Antes de añadir una entrada preguntar:

```text
Is this true?

Is this delivered?

Is this meaningful?

Is this category correct?

Can a future maintainer understand it?
```

---

# 210. Historical Validation

Añadir además:

```text
Can this claim be supported by implementation evidence?

Does it describe what existed at that point in time?

Does it accidentally promote a target architecture to completed history?
```

---

# 211. Release Validation

Antes de cerrar una versión:

- [ ] versión definida;
- [ ] fecha real;
- [ ] contenido integrado;
- [ ] categorías revisadas;
- [ ] breaking changes visibles;
- [ ] migrations visibles;
- [ ] security fixes visibles;
- [ ] Known Issues resueltos relevantes incluidos;
- [ ] no hay trabajo futuro presentado como entregado;
- [ ] no hay tecnologías futuras presentadas como baseline histórico;
- [ ] las capabilities declaradas están respaldadas por evidencia.

---

# 212. Unreleased Validation

Antes de release:

- [ ] no contiene tareas `IN_PROGRESS`;
- [ ] no contiene ideas del backlog;
- [ ] no contiene cambios descartados;
- [ ] representa únicamente cambios integrados;
- [ ] las entradas siguen siendo ciertas;
- [ ] no contiene candidate entries todavía no implementadas.

---

# 213. Release Cut Procedure

```text
Review Unreleased

↓

Verify implementation evidence

↓

Determine version

↓

Move entries under version

↓

Add release date

↓

Create empty Unreleased

↓

Run release validation

↓

Tag release

↓

Publish
```

---

# 214. Post-release Verification

Después de publicar:

```text
Git tag

Changelog

artifact

deployment metadata
```

deben representar la misma versión.

---

# 215. Patch Release Procedure

Para un hotfix:

```text
branch / fix

↓

tests

↓

merge

↓

Changelog entry

↓

PATCH version

↓

tag

↓

deploy
```

según workflow real del proyecto.

---

# 216. Security Patch Procedure

Debe añadir además:

```text
security validation

regression test

controlled disclosure
```

cuando corresponda.

---

# 217. Failed Release

Si una release nunca se publicó:

```text
do not preserve it as released
```

solo porque se preparó un número de versión.

---

# 218. Yanked Release

Si alguna versión publicada debe retirarse, puede marcarse:

```text
[YANKED]
```

---

# 219. Example

```markdown
## [0.8.3] — 2026-08-20 [YANKED]
```

---

# 220. Yank Reason

Debe explicarse brevemente.

---

# 221. Example

```markdown
> Yanked because the release contained an invalid database migration.
```

---

# 222. Do Not Delete Released History

Una versión realmente publicada no debe desaparecer silenciosamente del Changelog.

---

# 223. Changelog Integrity Principle

```text
Published history should remain historically honest.
```

---

# 224. Release Comparison

Cuando existan tags, pueden añadirse enlaces de comparación al final.

---

# 225. Example Structure

```markdown
[Unreleased]: compare-link
[0.9.0]: release-link
[0.8.0]: release-link
```

---

# 226. Link Policy

Los enlaces deben añadirse solo cuando:

```text
repository URL

and

tag structure
```

sean estables.

---

# 227. Avoid Placeholder URLs

No introducir:

```text
https://github.com/example/example
```

en el documento real.

---

# 228. Repository Independence

La estructura principal del Changelog debe seguir siendo útil incluso sin enlaces externos.

---

# 229. Changelog Maintenance Ownership

Inicialmente puede pertenecer al maintainer principal.

---

# 230. Future Contributor Workflow

Cuando aumenten contribuciones:

```text
contributors propose entries

maintainers curate wording

release owner finalizes version
```

---

# 231. Changelog Conflict Handling

Si varios PR modifican `Unreleased`, los conflictos deben resolverse conservando:

```text
all valid meaningful entries
```

---

# 232. Future Fragment Model

Solo si el volumen crece mucho puede evaluarse:

```text
changelog fragments
```

---

# 233. Current Recommendation

No introducir fragments todavía.

---

# 234. Why

Añadirían complejidad innecesaria para el tamaño actual del proyecto.

---

# 235. Automation Principle

Automatizar:

```text
repetitive mechanics
```

pero mantener humana la curación semántica.

---

# 236. Good Automation Candidates

```text
version validation

date formatting

tag consistency

release link generation
```

---

# 237. Poor Automation Candidate

Generar todo el Changelog directamente desde mensajes de commit sin revisión.

---

# 238. Why

Los commits representan:

```text
implementation activity
```

no necesariamente:

```text
release meaning
```

---

# 239. Conventional Commits

Si el proyecto los utiliza, pueden ayudar a construir candidatos.

---

# 240. But

No sustituyen el Changelog curado.

---

# 241. Example Mapping

```text
feat

→ candidate Added


fix

→ candidate Fixed


security

→ candidate Security
```

---

# 242. Mapping Limitation

Un commit:

```text
refactor(auth)
```

puede representar un cambio suficientemente importante para `Changed`.

---

# 243. Human Review

La categoría final debe decidirse por impacto.

---

# 244. Changelog Definition of Ready

Una entrada está lista cuando:

- [ ] el cambio está integrado;
- [ ] el comportamiento es conocido;
- [ ] la categoría está definida;
- [ ] el wording es comprensible;
- [ ] no revela detalles sensibles;
- [ ] no describe trabajo futuro;
- [ ] existe evidencia suficiente de implementación.

---

# 245. Changelog Definition of Done

Una release del Changelog está completa cuando:

- [ ] refleja el tag real;
- [ ] tiene fecha;
- [ ] contiene cambios relevantes;
- [ ] breaking changes están visibles;
- [ ] security changes están visibles;
- [ ] migration actions están visibles;
- [ ] `Unreleased` queda preparado para el siguiente ciclo;
- [ ] ninguna capability futura aparece como historial completado.

---

# 246. Current Recommended Skeleton

```markdown
# Changelog

All notable changes to Aula Robótica Platform will be documented in this file.

The format is based on Keep a Changelog and the project follows Semantic Versioning.

## [Unreleased]

## [X.Y.Z] — YYYY-MM-DD

### Added

- ...

### Changed

- ...

### Fixed

- ...

### Security

- ...
```

---

# 247. Professional Changelog Goal

El documento debe permitir que un maintainer pueda responder rápidamente:

```text
What did this release add?

What changed?

What was fixed?

Were there security changes?

Do I need to migrate anything?

Is anything breaking?
```

---

# 248. Historical Value

Con el tiempo, `55_CHANGELOG.md` debe convertirse en una representación compacta de la maduración de:

```text
Aula Robótica Platform
```

desde:

```text
initial application foundation
```

hacia una plataforma progresivamente más:

```text
stable

secure

maintainable

observable

operationally mature
```

---

# 249. Historical Honesty

La madurez documental no debe confundirse con madurez de implementación.

Por tanto:

```text
detailed documentation

≠

implemented capability
```

---

# 250. Current Historical Baseline

Mientras no aparezca nueva evidencia, el Changelog debe preservar:

```text
DATABASE

MariaDB
    CURRENT / HISTORICALLY IMPLEMENTED

PostgreSQL
    FUTURE / CANDIDATE


AUTHENTICATION

JWT Access Tokens
    IMPLEMENTED

JWT Refresh Tokens
    IMPLEMENTED

HTTPOnly Cookies
    IMPLEMENTED

SAML
    FUTURE


AUTHORIZATION

Global RBAC
    IMPLEMENTED

Contextual Authorization
    PARTIAL / EVOLVING

ProjectMembership
    TARGET / IN CONSOLIDATION


REALTIME

FastAPI WebSockets
    IMPLEMENTED

Selected Realtime Features
    IMPLEMENTED

Reconnect / Reconciliation Hardening
    IN PROGRESS / TARGET

Distributed Realtime
    FUTURE / CONDITIONAL


INFRASTRUCTURE

Docker
    IMPLEMENTED

Docker Compose
    IMPLEMENTED

Nginx
    IMPLEMENTED

Ubuntu / Hetzner VPS
    IMPLEMENTED

Redis
    CONDITIONAL

Kubernetes
    CONDITIONAL
```

---

# 251. No Guessing Rule

Si una capability no puede confirmarse:

```text
do not promote its historical status.
```

---

# 252. Reverse Correction Rule

Si el código demuestra que una capability sí existe:

```text
do not keep it classified as future
because an older document says so.
```

---

# 253. Confirmed Example — Refresh Tokens

La implementación verificada demuestra:

```text
JWT refresh tokens

+

refresh-token validation

+

explicit refresh endpoint

+

automatic access-token refresh
```

Por tanto, estas capabilities pueden formar parte de la reconstrucción histórica cuando exista evidencia suficiente para situarlas en una fase o release.

---

# 254. Confirmed Example — SAML

No existe evidencia equivalente de una integración SAML implementada.

Por tanto:

```text
SAML

→ FUTURE
```

y no debe aparecer dentro de una fase histórica como capability entregada.

---

# 255. Confirmed Example — Database

El motor relacional actual y verificado es:

```text
MariaDB
```

No existe evidencia de una migración completada a PostgreSQL.

Por tanto:

```text
MariaDB

→ HISTORICAL / CURRENT


PostgreSQL

→ FUTURE / CANDIDATE
```

---

# 256. Candidate vs Historical Entry

Ejemplo:

```markdown
### Added

- Added SAML-based identity integration support.
```

debe etiquetarse actualmente como:

```text
CANDIDATE FUTURE ENTRY
```

mientras:

```markdown
### Security

- Added token-based authentication with access-token and refresh-token support.
```

puede representar una capability histórica real, siempre que su ubicación temporal esté respaldada por evidencia.

---

# 257. Future Architecture Rule

Capacidades como:

```text
Redis

Kubernetes

microservices

object storage

PWA

AI / RAG

multi-tenancy
```

no deben aparecer como evolución ya realizada únicamente porque estén documentadas en:

```text
roadmap

future evolution

architecture proposals

technical challenges
```

---

# 258. Conditional Technology Rule

Una tecnología `CONDITIONAL` solo puede entrar en el historial cuando:

```text
trigger occurred

+

decision was made

+

implementation happened

+

integration was validated
```

---

# 259. Migration Historical Rule

Una migration puede considerarse histórica únicamente cuando:

```text
migration exists

+

was applied or delivered

+

target runtime supports it

+

documentation reflects the resulting state
```

---

# 260. Release Evidence Hierarchy

Para reconstruir releases o fases, utilizar preferentemente:

```text
1. Git tags

2. Release artifacts

3. Repository history

4. Verified code

5. Migrations

6. Automated tests

7. Deployment configuration

8. Current technical documentation

9. Historical project notes

10. Roadmap / future documents
```

---

# 261. Roadmap Evidence Limitation

Roadmap y Future Evolution pueden demostrar:

```text
intent
```

pero no:

```text
delivery.
```

---

# 262. Current Tasks Evidence Limitation

`53_CURRENT_TASKS.md` puede demostrar:

```text
current operational priority
```

pero no necesariamente:

```text
historical completion.
```

---

# 263. Changelog Authority

Una vez validado, este documento debe convertirse en la referencia curada para:

```text
delivered evolution
```

sin reemplazar las evidencias primarias del repositorio.

---

# 264. Changelog Definition of Ready — Historical Reconstruction

Una entrada reconstruida está lista cuando:

- [ ] la capability está confirmada;
- [ ] no contradice el código actual conocido;
- [ ] no depende exclusivamente de documentación futura;
- [ ] su wording refleja exactamente el alcance;
- [ ] no inventa fecha;
- [ ] no inventa versión;
- [ ] no inventa secuencia.

---

# 265. Changelog Definition of Done — Historical Reconstruction

Una fase histórica está suficientemente reconstruida cuando:

- [ ] todas sus capabilities principales están verificadas;
- [ ] las capabilities futuras han sido excluidas;
- [ ] las capabilities parciales están descritas con precisión;
- [ ] no existe contradicción conocida con el baseline actual;
- [ ] la fase puede entenderse sin confundir diseño con implementación.

---

# 266. Current Recommended Historical Skeleton

Cuando no exista versionado fiable:

```markdown
## Historical Evolution

### Application Foundation

- ...

### IAM Expansion

- ...

### Administrative Platform

- ...

### Core Collaboration

- ...

### Realtime Awareness

- ...

### UI Consolidation

- ...

### Quality and Operations

- ...
```

---

# 267. Historical Skeleton Guardrail

La estructura anterior:

```text
does not imply releases.
```

Representa únicamente:

```text
validated evolution phases.
```

---

# 268. Professional Changelog Goal

El documento debe permitir que un maintainer pueda responder rápidamente:

```text
What was actually implemented?

What changed between verified states?

Which capabilities are historical facts?

Which examples are only candidates?

Which migrations actually occurred?

Which security improvements were delivered?

Which technologies remain future?
```

---

# 269. Part 1 Summary

Esta primera parte establece:

```text
Purpose

Scope

Historical truth

Evidence hierarchy

Semantic Versioning

Keep a Changelog structure

Unreleased workflow

Added / Changed / Deprecated / Removed / Fixed / Security

Breaking changes

Migration notes

Security disclosure

Git relationship

Known Issues relationship

Current Tasks relationship

Technical Debt relationship

Release governance

Automation principles

Candidate-entry semantics

CURRENT vs FUTURE integrity

MariaDB historical baseline

JWT access + refresh historical baseline

SAML future status

PostgreSQL future/candidate status
```

---

# 270. Continuation

La **Parte 2/3** continúa con la estructura profesional y detallada del historial de Aula Robótica Platform, incluyendo:

```text
Unreleased

Current hardening cycle

Historical reconstruction

IAM evolution

JWT access and refresh-token evolution

SAML future classification

Administrative platform

Projects

Tasks

Activities

Attachments

Notifications

Dashboard

Activity Feed

Audit

Realtime

Security

Testing

UI

Database

Observability

Deployment

Documentation

Release grouping

Historical reconstruction rules
```

---

# 55_CHANGELOG.md

## Parte 2/3 — Historial funcional y técnico verificado, evolución por dominios y entradas candidatas

---

# 271. Historical Reconstruction

Esta sección reconstruye la evolución funcional y técnica de Aula Robótica Platform.

Su objetivo no es inventar releases históricas donde no existe evidencia suficiente, sino registrar:

```text
verified implementation evolution
```

por fases y dominios.

---

# 272. Historical Reconstruction Principle

Cuando no pueda verificarse:

```text
exact version

exact release date

exact chronological boundary
```

debe preservarse únicamente aquello que sí pueda afirmarse:

```text
capability was implemented

capability became part of the platform

capability evolved later
```

---

# 273. Historical Phase Model

La evolución puede agruparse conceptualmente en:

```text
Application Foundation

↓

Authentication and IAM

↓

Administration

↓

Core Collaboration

↓

Attachments and Awareness

↓

Realtime

↓

UI Consolidation

↓

Testing and Quality

↓

Operations and Deployment

↓

Current Hardening Cycle
```

---

# 274. Phase Model Is Not Version History

Estas fases:

```text
do not represent semantic versions

do not imply exact release dates

do not imply one deployment per phase
```

---

# 275. Historical Ordering

El orden expresa una evolución conceptual del producto.

No debe interpretarse como una cronología exacta de cada commit.

---

# 276. Application Foundation

La base de la plataforma se consolidó alrededor de:

```text
FastAPI

SQLAlchemy

MariaDB

Jinja2

Bootstrap / AdminLTE

modular backend structure
```

---

# 277. Application Architecture

La aplicación evolucionó como:

```text
Modular Monolith
```

con separación progresiva entre:

```text
routers

services

repositories

models

schemas

templates

static assets
```

---

# 278. Backend Foundation

La base backend incorporó:

```text
FastAPI routing

dependency injection

service-oriented business logic

SQLAlchemy persistence

repository-oriented data access
```

---

# 279. Persistence Foundation

El motor relacional utilizado por la plataforma es:

```text
MariaDB
```

---

# 280. Database Historical Invariant

Durante la reconstrucción histórica debe mantenerse:

```text
MariaDB

=

implemented relational database
```

---

# 281. PostgreSQL Correction

No debe incluirse dentro de esta evolución como migración realizada:

```text
MariaDB

↓

PostgreSQL
```

porque dicha migración no fue implementada.

---

# 282. PostgreSQL Classification

PostgreSQL permanece:

```text
FUTURE / CANDIDATE
```

---

# 283. Persistence Architecture

SQLAlchemy proporciona la capa ORM y de persistencia utilizada por la aplicación.

---

# 284. Database Evolution

La evolución real debe describirse mediante:

```text
schema growth

relationships

constraints

indexes

migrations

repository/query evolution
```

sobre el baseline actual de MariaDB.

---

# 285. Candidate Future Database Entry

Solo si se ejecutara una migración futura:

```markdown
### Changed

- Migrated the primary relational database from MariaDB to PostgreSQL.
```

---

# 286. Authentication Foundation

La plataforma incorporó autenticación basada en:

```text
JWT
```

---

# 287. Access Token Capability

El soporte para:

```text
JWT access tokens
```

forma parte de la implementación actual verificada.

---

# 288. Refresh Token Capability

También forma parte de la implementación verificada:

```text
JWT refresh tokens
```

---

# 289. Refresh Token Historical Correction

No debe tratarse el refresh-token workflow como una capability exclusivamente futura.

El código actual confirma:

```text
access-token issuance

refresh-token issuance

HTTPOnly cookie storage

refresh-token validation

explicit refresh endpoint

automatic access-token renewal

logout cookie cleanup
```

---

# 290. Authentication Cookies

Los tokens utilizados por los flujos web se integraron mediante:

```text
HTTPOnly cookies
```

---

# 291. HTTPOnly Security Benefit

Esta estrategia reduce exposición directa de tokens al JavaScript del navegador.

---

# 292. Login Evolution

El flujo de autenticación web permite conceptualmente:

```text
credentials

↓

authentication

↓

access token

+

refresh token

↓

HTTPOnly cookies

↓

authenticated SSR session
```

---

# 293. Explicit Refresh

Existe un endpoint explícito de refresh que:

```text
reads refresh token

↓

validates refresh token

↓

creates new access token

↓

updates access cookie
```

---

# 294. Automatic Access Refresh

La aplicación dispone además de renovación automática del access token desde middleware cuando:

```text
access-token validation fails

and

a valid refresh token is available
```

---

# 295. Authentication State Reconstruction

Después de renovar el access token, el middleware puede reconstruir el contexto autenticado de la request.

---

# 296. Logout

El logout elimina las cookies relacionadas con:

```text
access token

refresh token
```

---

# 297. Refresh Token Historical Entry

Una entrada histórica válida puede expresarse como:

```markdown
### Security

- Added JWT refresh-token support with HTTPOnly cookie storage and access-token renewal.
```

si se ubica en una fase cuya implementación esté verificada.

---

# 298. Refresh Hardening Distinction

No debe confundirse:

```text
refresh-token implementation
```

con:

```text
refresh-token security hardening.
```

---

# 299. Refresh Hardening Current Status

Aspectos como:

```text
rotation

server-side revocation

reuse detection

device/session management
```

no deben declararse implementados sin evidencia específica.

---

# 300. Cookie Policy Hardening

La revisión actual ha identificado además una necesidad de consolidar la política de cookies entre:

```text
login

explicit refresh

automatic middleware refresh
```

---

# 301. Cookie Configuration Concern

La configuración de seguridad debe evitar que una renovación automática pueda utilizar atributos menos estrictos que el flujo principal de autenticación.

---

# 302. Candidate Cookie Hardening Entry

Una vez implementada y validada la corrección:

```markdown
### Security

- Centralized authentication cookie configuration to enforce consistent environment-aware security attributes across login and refresh flows.
```

---

# 303. IAM Evolution

La plataforma amplió progresivamente la gestión de identidad y acceso alrededor de:

```text
Users

Roles

Permissions

Identities

JWT Authentication

Sessions / Request Context

RBAC
```

---

# 304. IAM Historical Correction

No debe incluirse dentro de las capabilities históricamente implementadas:

```text
SAML integration
```

---

# 305. SAML Status

SAML permanece:

```text
FUTURE
```

---

# 306. SAML Documentation Meaning

La existencia de documentación detallada sobre SAML representa:

```text
future integration design
```

y no:

```text
historical implementation.
```

---

# 307. Candidate SAML Entry

Solo después de una implementación real podría utilizarse:

```markdown
### Added

- Added SAML-based federated identity integration.
```

Actualmente esta entrada es:

```text
FUTURE CANDIDATE ENTRY
```

---

# 308. User Management

La plataforma incorporó capacidades administrativas relacionadas con:

```text
user management
```

---

# 309. Role Management

También se desarrolló gestión de:

```text
roles
```

como parte del modelo RBAC.

---

# 310. Permission Model

La autorización global se estructuró mediante:

```text
roles

+

permissions
```

---

# 311. RBAC Historical Status

El RBAC global forma parte del baseline implementado.

Estado:

```text
CURRENT / MATURE
```

---

# 312. Contextual Authorization Evolution

La necesidad de autorización dependiente del contexto apareció al crecer los dominios colaborativos.

---

# 313. Global Role Limitation

Un rol global no siempre responde correctamente a:

```text
what can this user do

inside this specific project?
```

---

# 314. Contextual Authorization Status

La autorización contextual debe describirse como:

```text
PARTIAL / EVOLVING
```

y no como arquitectura completamente consolidada.

---

# 315. ProjectMembership Status

Un modelo explícito de:

```text
ProjectMembership
```

representa:

```text
TARGET / IN CONSOLIDATION
```

---

# 316. ProjectMembership Historical Guardrail

No debe incluirse en una release histórica como capability completamente implementada mientras no exista verificación suficiente.

---

# 317. Candidate Membership Entry

Cuando llegue a completarse:

```markdown
### Added

- Added explicit Project Membership with project-scoped roles and contextual authorization.
```

---

# 318. Administrative Platform Evolution

La plataforma desarrolló progresivamente capacidades administrativas para gestionar entidades y operaciones del sistema.

---

# 319. Administrative UI

La interfaz administrativa evolucionó utilizando:

```text
Jinja2 SSR

Bootstrap

AdminLTE
```

---

# 320. Administrative Patterns

Se consolidaron patrones como:

```text
tables

forms

filters

actions

dialogs

status indicators

navigation
```

---

# 321. SSR Historical Status

Server-Side Rendering con Jinja2 es:

```text
CURRENT
```

---

# 322. SPA Historical Guardrail

No debe describirse una migración a:

```text
React

Vue

Angular

or another SPA architecture
```

como parte de la evolución realizada.

---

# 323. Frontend Architecture

El frontend actual debe describirse como:

```text
SSR

+

Bootstrap / AdminLTE

+

modular JavaScript

+

progressive enhancement
```

---

# 324. Projects Module

Projects constituye uno de los dominios centrales de colaboración.

---

# 325. Projects Core

La plataforma dispone de capacidades funcionales relacionadas con:

```text
project creation

project visualization

project update

project lifecycle
```

según la implementación existente.

---

# 326. Projects Historical Status

El core de Projects puede clasificarse como:

```text
CURRENT / FUNCTIONAL
```

---

# 327. Projects Evolution Direction

La siguiente maduración del dominio se centra en:

```text
membership

contextual roles

project-scoped authorization
```

---

# 328. Projects Changelog Guardrail

No mezclar:

```text
existing Project core
```

con:

```text
future mature Project Membership architecture.
```

---

# 329. Candidate Project Membership Security Entry

```markdown
### Security

- Added project-scoped authorization based on explicit membership and contextual roles.
```

Estado actual:

```text
CANDIDATE / NOT YET HISTORICAL
```

---

# 330. Tasks Module

Tasks constituye un dominio funcional integrado con Projects.

---

# 331. Task Core

La plataforma dispone de capacidades de gestión de Tasks.

---

# 332. Task Workflow

Los estados reales del dominio deben seguir siendo la fuente para cualquier representación visual posterior.

---

# 333. Current Task State Model

La documentación actual debe preservar estados reales como:

```text
TODO

DOING

DONE
```

cuando correspondan al modelo implementado.

---

# 334. Kanban Historical Correction

Kanban no debe aparecer como capability histórica ya implementada.

---

# 335. Kanban Status

```text
PLANNED / NEXT CAPABILITY
```

---

# 336. Kanban Candidate Entry

Después de una implementación real:

```markdown
### Added

- Added a project-scoped Kanban board for Task workflow visualization and state transitions.
```

---

# 337. Live Kanban Candidate Entry

Posteriormente, si se implementa realtime:

```markdown
### Added

- Added realtime synchronization of Kanban Task transitions across authorized clients.
```

---

# 338. Activities Module

Activities forma parte de la capa colaborativa de la plataforma.

---

# 339. Activities Historical Status

El módulo dispone de una implementación funcional avanzada.

---

# 340. Activity Responsibilities

Puede representar trabajo o eventos funcionales relacionados con la actividad de usuario y proyecto según el dominio existente.

---

# 341. Activities Guardrail

No confundir:

```text
Activity domain
```

con:

```text
Audit trail
```

---

# 342. Attachments Module

La plataforma incorporó soporte de:

```text
attachments
```

asociados a recursos funcionales.

---

# 343. Attachment Core

La implementación actual contempla:

```text
metadata

physical file

authorized access

persistent storage
```

---

# 344. Attachment Storage Status

El almacenamiento actual debe mantenerse como:

```text
CURRENT
```

sin asumir object storage.

---

# 345. Object Storage Status

```text
FUTURE / CONDITIONAL
```

---

# 346. Candidate Object Storage Entry

Solo después de una migración real:

```markdown
### Changed

- Migrated attachment binary storage to S3-compatible object storage.
```

---

# 347. Attachment Security

Los Attachments deben mantener autorización coherente con el recurso padre.

---

# 348. Candidate Attachment Security Entry

Si se consolida explícitamente:

```markdown
### Security

- Hardened attachment access using parent-resource authorization policies.
```

---

# 349. Notifications Module

La plataforma dispone de:

```text
persistent in-app notifications
```

---

# 350. Notification Capabilities

El baseline incluye:

```text
persistent notification state

read / unread behavior

realtime delivery or update paths
```

según los flujos implementados.

---

# 351. Notifications Historical Status

```text
CURRENT
```

---

# 352. Notification Future Evolution

No debe declararse como actual sin evidencia:

```text
email delivery

push notifications

digest engine

advanced user preferences

background distributed delivery
```

---

# 353. Candidate Notification Preference Entry

```markdown
### Added

- Added per-user notification preferences by event type and delivery channel.
```

Estado:

```text
FUTURE CANDIDATE
```

---

# 354. Dashboard

La plataforma dispone de Dashboard como superficie de resumen y awareness.

---

# 355. Dashboard Historical Status

```text
CURRENT
```

---

# 356. Dashboard Evolution

Su evolución puede incluir:

```text
metrics

recent activity

status summaries

realtime updates
```

según implementación verificada.

---

# 357. Dashboard Optimization

Las mejoras avanzadas de queries o widgets deben registrarse únicamente después de su implementación.

---

# 358. Candidate Dashboard Optimization Entry

```markdown
### Changed

- Reduced Dashboard query cost through dedicated aggregation queries.
```

---

# 359. Activity Feed

Activity Feed forma parte de las capacidades de awareness de la plataforma.

---

# 360. Activity Feed Historical Status

```text
CURRENT
```

---

# 361. Activity Feed Purpose

Su objetivo es proporcionar:

```text
user-facing operational awareness
```

---

# 362. Activity Feed vs Audit

Debe mantenerse:

```text
Activity Feed

≠

Audit
```

---

# 363. Activity Feed

Está orientado a:

```text
user collaboration

recent activity

product awareness
```

---

# 364. Audit

Está orientado a:

```text
traceability

security

accountability

historical evidence
```

---

# 365. Audit System

La plataforma dispone de un sistema de Audit transversal.

---

# 366. Audit Historical Status

```text
CURRENT / MATURE
```

---

# 367. Audit Evolution

La cobertura puede ampliarse conforme aparecen nuevos eventos relevantes.

---

# 368. Candidate Membership Audit Entry

Después de implementar Project Membership:

```markdown
### Added

- Added audit events for project membership creation, role changes, and removal.
```

---

# 369. Realtime Foundation

La plataforma incorporó capacidades realtime mediante:

```text
FastAPI WebSockets
```

---

# 370. Realtime Historical Status

WebSockets forman parte del baseline implementado.

---

# 371. Current Realtime Features

La implementación actual incluye actualizaciones relacionadas con:

```text
Dashboard

Notifications

Audit Timeline

Activity Feed
```

---

# 372. Realtime Architecture

La implementación actual utiliza un:

```text
in-memory Connection Manager
```

adecuado para la topología actual de una sola instancia.

---

# 373. Redis Historical Correction

No debe describirse Redis como parte del stack realtime actual.

---

# 374. Redis Status

```text
CONDITIONAL
```

---

# 375. Redis Adoption Trigger

Redis o un broker distribuido solo deberían introducirse si aparece una necesidad como:

```text
multiple application instances

cross-process realtime coordination

durable event distribution

independent workers requiring shared delivery
```

---

# 376. Candidate Redis Entry

Solo después de una adopción real:

```markdown
### Changed

- Added Redis-backed realtime coordination for multi-instance deployments.
```

---

# 377. Realtime Reliability Status

La existencia de WebSockets no significa que toda la arquitectura realtime esté terminada.

---

# 378. Current Realtime Hardening

Continúan como áreas de consolidación:

```text
authentication hardening

subscription authorization

event contract normalization

reconnect

reconciliation

multi-client testing
```

---

# 379. Candidate Event Contract Entry

Después de implementarse:

```markdown
### Changed

- Standardized WebSocket events around a shared resource-action envelope.
```

---

# 380. Candidate Reconnect Entry

```markdown
### Changed

- Added controlled WebSocket reconnection with authoritative state reconciliation.
```

---

# 381. Candidate Subscription Security Entry

```markdown
### Security

- Added server-side authorization for project-scoped WebSocket subscriptions.
```

---

# 382. Realtime Source of Truth

La persistencia continúa siendo autoritativa.

Conceptualmente:

```text
MariaDB

↓

authoritative state


WebSocket

↓

state propagation
```

---

# 383. Persist-before-broadcast Evolution

Las mutaciones realtime deben seguir:

```text
validate

↓

authorize

↓

persist

↓

commit

↓

broadcast
```

---

# 384. UI Evolution

La UI evolucionó sobre:

```text
Jinja2

Bootstrap

AdminLTE
```

con comportamiento JavaScript progresivamente modular.

---

# 385. Reusable UI

Se desarrollaron patrones reutilizables para reducir duplicación visual y funcional.

---

# 386. Candidate Reusable Components

Entre los patrones utilizados o evolucionados pueden encontrarse:

```text
dialogs

toasts

tables

badges

status indicators

forms

action controls
```

según implementación concreta.

---

# 387. Modular JavaScript

El frontend utiliza JavaScript modular para comportamientos interactivos.

---

# 388. Progressive Enhancement

La estrategia general preserva:

```text
SSR baseline

+

JavaScript enhancement
```

---

# 389. Native Dialog Cleanup

La eliminación completa de:

```javascript
alert()
confirm()
```

permanece como trabajo de consolidación mientras existan usos relevantes.

---

# 390. Candidate Dialog Entry

Cuando se complete una migración significativa:

```markdown
### Changed

- Replaced native destructive-action dialogs with reusable application confirmation components.
```

---

# 391. Shared Fetch Infrastructure

Una infraestructura común para Fetch representa una mejora objetivo cuando permita centralizar:

```text
CSRF

error handling

JSON parsing

authentication failures
```

---

# 392. Shared Fetch Status

No debe describirse como completamente consolidada sin evidencia.

---

# 393. Security Evolution

La seguridad de la plataforma ha evolucionado alrededor de:

```text
authentication

RBAC

HTTPOnly cookies

authorization

audit

validation

secure deployment
```

---

# 394. Security Maturity Guardrail

No debe utilizarse:

```text
security complete
```

o equivalentes absolutos.

---

# 395. Why

Continúan existiendo áreas de hardening como:

```text
formal CSRF protection

refresh-token lifecycle hardening

cookie-policy consistency

contextual authorization

WebSocket authentication

subscription authorization
```

---

# 396. CSRF Historical Status

La protección CSRF formal debe permanecer:

```text
PENDING / IN PROGRESS
```

hasta verificar su implementación completa.

---

# 397. Candidate CSRF Entry

Cuando se implemente:

```markdown
### Security

- Added formal CSRF protection for authenticated browser mutations.
```

---

# 398. Refresh-token Historical Status

El soporte de refresh token es:

```text
CURRENT
```

---

# 399. Refresh-token Hardening Status

Aspectos avanzados permanecen:

```text
VERIFY / HARDENING
```

---

# 400. Candidate Rotation Entry

Solo después de implementación verificada:

```markdown
### Security

- Added refresh-token rotation and reuse protection.
```

---

# 401. Cookie Policy Candidate Entry

Después de centralizar y validar la política:

```markdown
### Security

- Unified authentication cookie security attributes across login and automatic token-refresh flows.
```

---

# 402. WebSocket Security Status

WebSockets son actuales.

El hardening completo de autenticación y autorización realtime permanece en evolución.

---

# 403. Candidate WebSocket Authentication Entry

```markdown
### Security

- Hardened WebSocket authentication using server-validated identity context.
```

---

# 404. Candidate WebSocket Authorization Entry

```markdown
### Security

- Added authorization checks for realtime subscriptions and project-scoped channels.
```

---

# 405. Testing Evolution

La plataforma dispone de testing automatizado.

---

# 406. Testing Historical Status

```text
CURRENT
```

---

# 407. Testing Scope

La estrategia incluye diferentes niveles según área:

```text
unit

service

repository

API

integration

UI

realtime
```

---

# 408. Coverage Guardrail

La existencia de una estrategia documentada no significa:

```text
complete coverage.
```

---

# 409. Current Testing Maturity

Debe describirse como:

```text
functional

with expanding coverage
```

especialmente en:

```text
UI

realtime

contextual authorization
```

---

# 410. Candidate Authorization Testing Entry

```markdown
### Added

- Added cross-project authorization regression tests for project-scoped resources.
```

---

# 411. Candidate Realtime Testing Entry

```markdown
### Added

- Added multi-client WebSocket tests covering subscription authorization, broadcast, reconnect, and reconciliation.
```

---

# 412. Candidate UI Testing Entry

```markdown
### Added

- Expanded browser-level regression coverage for critical authentication and collaboration journeys.
```

---

# 413. CI Evolution

La plataforma utiliza:

```text
GitHub Actions
```

para automatización de calidad e integración.

---

# 414. CI Historical Status

```text
CURRENT
```

---

# 415. CI Responsibilities

Puede incluir según configuración real:

```text
tests

quality checks

build validation

deployment-related automation
```

---

# 416. CI/CD Precision

No debe describirse:

```text
fully automated continuous deployment
```

si todavía existen pasos manuales o procesos no automatizados.

---

# 417. Quality Tooling

Las herramientas de análisis estático y quality gates deben describirse únicamente según su integración real.

---

# 418. SonarCloud Status

Cuando la configuración actual lo confirme, SonarCloud forma parte del quality workflow.

---

# 419. Candidate Quality Entry

```markdown
### Changed

- Extended CI quality gates with additional automated regression checks.
```

---

# 420. Deployment Evolution

La plataforma dispone de un deployment containerizado.

---

# 421. Current Deployment Baseline

```text
Docker

Docker Compose

Nginx

Ubuntu

Hetzner VPS
```

---

# 422. Deployment Historical Status

Estas tecnologías forman parte del entorno operativo actual.

---

# 423. Kubernetes Historical Correction

Kubernetes no forma parte del deployment actual.

---

# 424. Kubernetes Status

```text
CONDITIONAL / NOT CURRENT
```

---

# 425. Candidate Kubernetes Entry

Solo después de una migración real:

```markdown
### Changed

- Migrated production orchestration from Docker Compose to Kubernetes.
```

---

# 426. Microservices Historical Correction

La plataforma no debe describirse como arquitectura de microservicios.

---

# 427. Current Architecture

```text
Modular Monolith
```

---

# 428. Microservices Status

```text
CONDITIONAL
```

---

# 429. Candidate Service Extraction Entry

Solo si un boundary se extrae realmente:

```markdown
### Changed

- Extracted the notification delivery boundary into an independently deployable service.
```

---

# 430. Observability Evolution

La plataforma dispone de documentación y capacidades operativas relacionadas con:

```text
logging

monitoring

observability

audit
```

---

# 431. Observability Precision

Debe diferenciarse:

```text
documented target

from

implemented telemetry.
```

---

# 432. Logging

El logging operativo no debe confundirse con Audit.

---

# 433. Logging vs Audit

```text
Logging

→ technical diagnostics


Audit

→ business/security traceability
```

---

# 434. Candidate Structured Logging Entry

```markdown
### Changed

- Standardized application logs around structured request and error context.
```

solo si dicha estandarización está implementada.

---

# 435. Monitoring Candidate Entry

```markdown
### Added

- Added operational monitoring for application availability and critical service health.
```

solo si existe implementación real.

---

# 436. Backup Evolution

Los cambios significativos de backup/restore deben registrarse cuando afecten la seguridad operativa.

---

# 437. Candidate Backup Entry

```markdown
### Changed

- Extended backup procedures to cover relational data and persistent attachment storage.
```

---

# 438. Restore Importance

Un backup no debe considerarse plenamente operativo si:

```text
restore has never been validated.
```

---

# 439. Documentation Evolution

La plataforma ha desarrollado una documentación técnica extensa y estructurada.

---

# 440. Documentation Architecture

El corpus cubre:

```text
overview

architecture

security

backend

frontend

realtime

database

modules

operations

DevOps

testing

product

engineering guidelines

decisions

status

project history
```

---

# 441. Documentation Historical Value

La documentación constituye una parte importante de la mantenibilidad del proyecto.

---

# 442. Documentation Historical Risk

Sin embargo:

```text
detailed documentation

can describe future architecture.
```

Por tanto:

```text
documentation depth

≠

implementation evidence.
```

---

# 443. Documentation Changelog Entry

Una reorganización importante sí puede registrarse:

```markdown
### Changed

- Reorganized technical documentation into dedicated architecture, security, backend, frontend, realtime, operations, testing, and project-history manuals.
```

si corresponde a un cambio real.

---

# 444. Documentation Naming Consistency

Las referencias internas deben coincidir con los nombres reales de archivo.

---

# 445. Known Filename Correction

La documentación debe converger de:

```text
37_LOGGIN.md
```

hacia:

```text
37_LOGGING.md
```

actualizando las referencias asociadas cuando se realice el cambio.

---

# 446. Known Reference Correction

Las referencias a:

```text
58_TECHNICAL_CHALLENGE.md
```

deben utilizar:

```text
58_TECHNICAL_CHALLENGES.md
```

---

# 447. Document 61 Correction

El documento real es:

```text
61_LESSONS_LEARNED.md
```

No debe referenciarse como:

```text
61_ARCHITECTURE_REVIEW.md
```

---

# 448. Documentation Correction Entry

Cuando estas correcciones se integren:

```markdown
### Fixed

- Corrected stale and inconsistent internal documentation references.
```

---

# 449. Product History vs Future Evolution

Los documentos históricos deben contener:

```text
what happened
```

mientras:

```text
62_FUTURE_EVOLUTION.md
```

debe contener:

```text
what may happen later.
```

---

# 450. Changelog vs Future Evolution

Por tanto:

```text
55_CHANGELOG

→ delivered changes


62_FUTURE_EVOLUTION

→ possible evolution
```

---

# 451. No Back-propagation Rule

Una capability descrita en Future Evolution no debe aparecer retroactivamente en el Changelog como si ya hubiese sido implementada.

---

# 452. Historical IAM Reconstruction

La evolución IAM verificada debe conservar como mínimo:

```text
User model

↓

Authentication

↓

JWT access token

↓

JWT refresh token

↓

HTTPOnly cookie integration

↓

Role / Permission model

↓

RBAC

↓

Session/request authentication context
```

---

# 453. IAM Historical Exclusion

No añadir al flujo anterior:

```text
SAML
```

hasta que exista una integración real.

---

# 454. IAM Current Hardening

La siguiente fase puede incluir:

```text
cookie-policy consolidation

refresh-token lifecycle hardening

contextual authorization expansion
```

---

# 455. IAM Candidate Historical Entry

Cuando se complete ese hardening:

```markdown
### Security

- Hardened browser authentication by consolidating cookie policy and strengthening refresh-token lifecycle controls.
```

---

# 456. Collaboration Historical Reconstruction

La evolución colaborativa puede representarse conceptualmente como:

```text
Projects

↓

Tasks

↓

Activities

↓

Attachments

↓

Notifications

↓

Activity Feed

↓

Realtime Awareness
```

---

# 457. Collaboration Guardrail

Este orden es conceptual.

No afirma una secuencia exacta de releases.

---

# 458. Collaboration Next Step

La evolución objetivo añade:

```text
Project Membership

↓

Contextual Authorization

↓

Kanban

↓

Realtime Kanban
```

---

# 459. Collaboration Status Boundary

Debe mantenerse:

```text
Projects
    CURRENT

Tasks
    CURRENT

Activities
    CURRENT

Attachments
    CURRENT

Notifications
    CURRENT

Activity Feed
    CURRENT

WebSockets
    CURRENT


ProjectMembership
    TARGET / IN CONSOLIDATION

Kanban
    PLANNED

Live Kanban
    PLANNED
```

---

# 460. Security Historical Reconstruction

La evolución real puede describirse mediante:

```text
Authentication

↓

HTTPOnly token transport

↓

RBAC

↓

Validation

↓

Audit

↓

Security-oriented deployment controls
```

---

# 461. Security Next Step

La siguiente maduración se centra en:

```text
formal CSRF

cookie-policy consistency

refresh-token hardening

contextual authorization

WebSocket authentication

subscription authorization

negative security tests
```

---

# 462. Realtime Historical Reconstruction

La evolución real puede describirse como:

```text
WebSocket foundation

↓

Connection management

↓

Realtime feature integration

↓

Dashboard / Notifications / Audit / Activity Feed updates
```

---

# 463. Realtime Next Step

La siguiente maduración se centra en:

```text
event normalization

authentication hardening

subscription authorization

reconnect

reconciliation

multi-client testing
```

---

# 464. Realtime Scaling Boundary

Solo después de una necesidad real de múltiples instancias debe evaluarse:

```text
Redis

broker

distributed event coordination
```

---

# 465. Deployment Historical Reconstruction

La infraestructura actual puede representarse como:

```text
Application

↓

Docker

↓

Docker Compose

↓

Nginx

↓

Ubuntu

↓

Hetzner VPS
```

---

# 466. Deployment Future Boundary

No añadir:

```text
Kubernetes

multi-region

service mesh
```

a la historia implementada sin evidencia futura.

---

# 467. Database Historical Reconstruction

La evolución persistente debe mantenerse alrededor de:

```text
SQLAlchemy

+

MariaDB
```

---

# 468. Database Future Boundary

PostgreSQL puede continuar evaluándose como:

```text
candidate migration target
```

pero no forma parte de la historia realizada.

---

# 469. Current Hardening Cycle

El trabajo actual se orienta principalmente a consolidar:

```text
Contextual Authorization

Security Hardening

Realtime Reliability

Testing

Frontend Consistency

Performance Measurement
```

---

# 470. Current Hardening Is Not Historical Yet

Mientras estas tareas permanezcan:

```text
READY

IN_PROGRESS

BLOCKED

VALIDATION
```

no deben aparecer como cambios completados de una release.

---

# 471. Candidate Current Hardening Entries

Las siguientes entradas permanecen como candidatas hasta su implementación:

```markdown
### Security

- Added formal CSRF protection for authenticated browser mutations.
- Centralized authentication cookie security attributes across login and refresh flows.
- Hardened WebSocket authentication and project-scoped subscription authorization.
- Added contextual authorization for project-scoped resources.

### Changed

- Standardized realtime event contracts.
- Added reconnect and authoritative state reconciliation.

### Added

- Added explicit Project Membership.
- Added a project-scoped Kanban board.
- Added multi-client realtime integration tests.
```

---

# 472. Candidate Entry Promotion Rule

Cada entrada anterior solo debe pasar a:

```text
[Unreleased]
```

cuando:

```text
implementation exists

+

tests pass

+

integration is complete
```

---

# 473. Unreleased Integrity

`[Unreleased]` no debe convertirse en:

```text
wish list.
```

---

# 474. Current Unreleased Strategy

Si no puede verificarse que una tarea actual esté ya integrada:

```text
leave it out of Unreleased.
```

---

# 475. Historical Reconstruction Quality Gate

Antes de aceptar una fase histórica:

- [ ] MariaDB sigue siendo el motor histórico real.
- [ ] PostgreSQL no aparece como migración completada.
- [ ] Refresh tokens aparecen como implementados.
- [ ] Refresh rotation no aparece como implementada sin evidencia.
- [ ] SAML no aparece como implementado.
- [ ] RBAC aparece como implementado.
- [ ] Contextual authorization no aparece como completamente madura.
- [ ] ProjectMembership no aparece como completamente consolidado.
- [ ] Kanban no aparece como entregado.
- [ ] WebSockets aparecen como implementados.
- [ ] Redis no aparece como actual.
- [ ] Docker Compose sigue representando el deployment actual.
- [ ] Kubernetes no aparece como actual.
- [ ] Microservices no aparecen como arquitectura actual.

---

# 476. Historical Consistency Matrix

| Capability | Historical Classification |
| :--- | :--- |
| FastAPI | IMPLEMENTED |
| SQLAlchemy | IMPLEMENTED |
| MariaDB | IMPLEMENTED |
| PostgreSQL | FUTURE / CANDIDATE |
| Jinja2 SSR | IMPLEMENTED |
| Bootstrap / AdminLTE | IMPLEMENTED |
| JWT Access Token | IMPLEMENTED |
| JWT Refresh Token | IMPLEMENTED |
| HTTPOnly Cookies | IMPLEMENTED |
| Explicit Token Refresh | IMPLEMENTED |
| Automatic Access Refresh | IMPLEMENTED |
| RBAC | IMPLEMENTED |
| Contextual Authorization | PARTIAL / EVOLVING |
| ProjectMembership | TARGET / IN CONSOLIDATION |
| SAML | FUTURE |
| Projects | IMPLEMENTED |
| Tasks | IMPLEMENTED |
| Activities | IMPLEMENTED |
| Attachments | IMPLEMENTED |
| Notifications | IMPLEMENTED |
| Dashboard | IMPLEMENTED |
| Activity Feed | IMPLEMENTED |
| Audit | IMPLEMENTED |
| WebSockets | IMPLEMENTED |
| Reconnect / Reconciliation Hardening | IN PROGRESS / TARGET |
| Redis | CONDITIONAL |
| Kanban | PLANNED |
| Docker | IMPLEMENTED |
| Docker Compose | IMPLEMENTED |
| Nginx | IMPLEMENTED |
| Ubuntu / Hetzner VPS | IMPLEMENTED |
| Kubernetes | CONDITIONAL |
| Microservices | CONDITIONAL |
| Object Storage | FUTURE / CONDITIONAL |
| PWA | FUTURE |
| AI / RAG | FUTURE / EXPERIMENTAL |

---

# 477. Changelog Historical Invariant

El historial debe conservar siempre:

```text
implemented reality

>

documented aspiration
```

---

# 478. Part 2 Summary

Esta segunda parte consolida la reconstrucción histórica y establece como hechos actuales:

```text
FastAPI

SQLAlchemy

MariaDB

Jinja2 SSR

Bootstrap / AdminLTE

JWT Access Tokens

JWT Refresh Tokens

HTTPOnly Cookies

RBAC

Projects

Tasks

Activities

Attachments

Notifications

Dashboard

Activity Feed

Audit

FastAPI WebSockets

Docker

Docker Compose

Nginx

Ubuntu

Hetzner VPS

Automated Testing

GitHub Actions
```

y mantiene fuera del historial completado:

```text
SAML

PostgreSQL migration

ProjectMembership fully consolidated

Kanban

Live Kanban

formal CSRF hardening

refresh-token rotation unless verified

complete WebSocket subscription hardening

Redis

Kubernetes

microservices

object-storage migration

PWA

AI / RAG

multi-tenancy
```

---

# 479. Continuation

La **Parte 3/3** completa `55_CHANGELOG.md` con:

```text
Changelog Operational Governance

Release Lifecycle

Historical Release Reconstruction

Current Unreleased Rules

Candidate Entry Registry

Security Candidate Entries

Realtime Candidate Entries

Authorization Candidate Entries

Database Candidate Entries

Deployment Candidate Entries

Documentation Candidate Entries

Promotion and Archiving Rules

Cross-document Synchronization

Audit Checklist

Current Changelog Snapshot

Final Historical Invariants

Maintenance Rules

Conclusion
```

---

# 55_CHANGELOG.md

## Parte 3/3 — Gobernanza operativa, ciclo de releases, registro de candidatos, sincronización documental, auditoría y estado final

---

# 480. Changelog Operational Governance

El Changelog necesita una gobernanza explícita para evitar que con el tiempo se convierta en:

```text
task log

roadmap

commit dump

architecture proposal

or

unverified historical narrative
```

---

# 481. Governance Objective

La gobernanza debe garantizar:

```text
historical accuracy

release traceability

consistent terminology

clear CURRENT / FUTURE boundaries

maintainable release history
```

---

# 482. Changelog Authority Model

La relación entre evidencias debe interpretarse como:

```text
Repository / Runtime Evidence

↓

Implementation Truth

↓

Curated Changelog

↓

Historical Documentation
```

---

# 483. Changelog Is Curated Evidence

`55_CHANGELOG.md` no sustituye a:

```text
Git

tests

migrations

deployment configuration

runtime evidence
```

pero proporciona una interpretación histórica curada de esas evidencias.

---

# 484. Release Lifecycle

El ciclo recomendado es:

```text
Implementation

↓

Tests

↓

Review

↓

Merge / Integration

↓

[Unreleased]

↓

Release Validation

↓

Version Assignment

↓

Tag

↓

Deployment / Publication

↓

Versioned Changelog History
```

---

# 485. Pre-implementation State

Antes de existir implementación:

```text
Roadmap

Feature Backlog

Current Tasks
```

pueden contener la capability.

El Changelog todavía no.

---

# 486. Implementation State

Durante desarrollo:

```text
READY

IN_PROGRESS

BLOCKED

VALIDATION
```

siguen siendo estados operativos.

No son estados de Changelog.

---

# 487. Integration Boundary

Una capability puede entrar en:

```text
[Unreleased]
```

cuando está:

```text
implemented

+

integrated

+

sufficiently validated
```

---

# 488. Release Boundary

Una capability pasa de:

```text
[Unreleased]
```

a:

```text
[X.Y.Z]
```

cuando forma parte de una release real.

---

# 489. Historical Boundary

Una vez publicada:

```text
versioned entry

=

historical record
```

y no debe reinterpretarse silenciosamente.

---

# 490. Historical Correction

Si posteriormente se descubre un error factual en el Changelog, debe corregirse.

---

# 491. Historical Correction Principle

Corregir:

```text
false statement
```

no equivale a:

```text
rewriting legitimate history.
```

---

# 492. Example Historical Correction

Si una entrada afirmara:

```text
Migrated from MariaDB to PostgreSQL
```

sin que esa migración hubiera ocurrido, debe corregirse o eliminarse.

---

# 493. Historical Preservation

En cambio, una capability realmente publicada y posteriormente eliminada debe conservarse en su release histórica.

---

# 494. Example Historical Preservation

```text
Version A
    capability added

Version B
    capability deprecated

Version C
    capability removed
```

Las tres entradas son históricamente válidas.

---

# 495. Current Unreleased Section

La sección:

```markdown
## [Unreleased]
```

debe contener exclusivamente cambios integrados todavía no incluidos en una release.

---

# 496. Empty Unreleased Is Valid

Es completamente válido mantener:

```markdown
## [Unreleased]

No unreleased changes currently recorded.
```

si no existen cambios integrados pendientes de release.

---

# 497. Never Fill Unreleased Artificially

No añadir trabajo únicamente para evitar que la sección parezca vacía.

---

# 498. Unreleased Exclusions

Excluir:

```text
ProjectMembership
```

si sigue siendo TARGET.

Excluir:

```text
Kanban
```

si sigue siendo PLANNED.

Excluir:

```text
PostgreSQL
```

si sigue siendo FUTURE / CANDIDATE.

Excluir:

```text
SAML
```

si sigue siendo FUTURE.

---

# 499. Current Hardening Exclusion

También deben permanecer fuera de `Unreleased` mientras no estén completadas:

```text
formal CSRF protection

refresh-token rotation

cookie-policy consolidation

WebSocket authentication hardening

subscription authorization

reconnect/reconciliation hardening
```

---

# 500. Existing Refresh Workflow Exception

No debe excluirse del historial el soporte existente de:

```text
JWT refresh tokens

explicit refresh endpoint

automatic access-token refresh

HTTPOnly refresh cookie
```

porque estas capabilities sí están implementadas.

---

# 501. Candidate Entry Registry

Las entradas futuras pueden mantenerse como un registro de candidatos.

Su función es:

```text
prepare consistent release wording

without

claiming delivery.
```

---

# 502. Candidate Registry Rule

Toda entrada candidata debe poder distinguirse inequívocamente de:

```text
Unreleased

Released History
```

---

# 503. Candidate Status

Un candidato puede encontrarse conceptualmente en:

```text
PLANNED

TARGET

FUTURE

CONDITIONAL
```

---

# 504. Candidate Promotion

```text
Candidate

↓

Implementation

↓

Validation

↓

Integration

↓

Unreleased
```

---

# 505. Candidate Rejection

Si la capability deja de tener valor:

```text
Candidate

↓

Discarded / Deferred
```

sin necesidad de aparecer en el historial.

---

# 506. Candidate Security Registry

Entradas candidatas de seguridad:

```markdown
### Security — Candidate

- Add formal CSRF protection for authenticated browser mutations.
- Centralize environment-aware authentication cookie configuration.
- Harden refresh-token lifecycle with an explicit rotation and revocation strategy.
- Harden WebSocket authentication using server-validated identity.
- Add project-scoped WebSocket subscription authorization.
- Expand contextual authorization across project-scoped resources.
```

---

# 507. Candidate Security Integrity

La entrada:

```text
Harden refresh-token lifecycle
```

no significa:

```text
implement refresh tokens.
```

El refresh-token workflow ya existe.

---

# 508. Candidate CSRF Integrity

La entrada CSRF permanece candidata hasta que la protección formal esté:

```text
implemented

tested

integrated
```

---

# 509. Candidate Cookie Integrity

La consolidación de cookies debe resolver de forma centralizada atributos como:

```text
HttpOnly

Secure

SameSite

Path

expiry
```

según entorno.

---

# 510. Candidate Refresh Hardening Integrity

Antes de promover la entrada deben verificarse específicamente:

```text
rotation

revocation

reuse behavior

logout semantics

expiry behavior
```

---

# 511. Candidate Authorization Registry

```markdown
### Security — Candidate

- Add explicit Project Membership semantics.
- Add project-scoped contextual authorization.
- Add cross-project authorization regression protection.
```

---

# 512. ProjectMembership Promotion Requirement

No promover:

```text
Project Membership
```

por la mera existencia de:

```text
Project

User

Role
```

---

# 513. Membership Evidence

Debe existir evidencia de:

```text
explicit membership model

persistence semantics

service behavior

authorization integration

tests
```

---

# 514. Contextual Authorization Promotion

Debe promoverse únicamente el scope realmente implementado.

---

# 515. Example Partial Promotion

Si solo se protege:

```text
Project update

Project delete
```

la entrada debe decir exactamente eso.

---

# 516. Avoid Overclaiming

No utilizar:

```markdown
- Completed contextual authorization across the platform.
```

si quedan dominios sin cobertura.

---

# 517. Candidate Realtime Registry

```markdown
### Changed — Candidate

- Standardize realtime event envelopes.
- Add controlled WebSocket reconnect behavior.
- Add authoritative state reconciliation after reconnect.

### Security — Candidate

- Harden WebSocket authentication.
- Add authorization for project-scoped subscriptions.

### Added — Candidate

- Add multi-client realtime integration tests.
```

---

# 518. Realtime Promotion Requirement

Una entrada realtime debe demostrar comportamiento en:

```text
server

client

failure path
```

cuando sea relevante.

---

# 519. Reconnect Promotion Requirement

No basta con:

```text
socket reconnects.
```

Debe verificarse qué ocurre con:

```text
missed events

subscriptions

authoritative state
```

---

# 520. Reconciliation Promotion Requirement

La reconciliación debe permitir:

```text
client state

↓

converge with

↓

authoritative persisted state
```

---

# 521. Candidate Kanban Registry

```markdown
### Added — Candidate

- Add an SSR project Kanban board.
- Add authorized Task status transitions from the board.
- Add drag-and-drop as progressive enhancement.
- Add realtime Kanban synchronization.
```

---

# 522. Kanban Promotion Sequence

La promoción recomendada es incremental:

```text
SSR Board

↓

Authorized Mutation

↓

Drag & Drop

↓

Realtime Synchronization
```

---

# 523. Kanban Historical Guardrail

No convertir la existencia actual de:

```text
TODO

DOING

DONE
```

en evidencia de que:

```text
Kanban UI
```

ya existe.

---

# 524. Candidate Database Registry

Actualmente:

```text
no database-engine migration belongs in Unreleased
```

salvo nueva evidencia.

---

# 525. PostgreSQL Candidate Entry

Puede mantenerse únicamente como ejemplo futuro:

```markdown
### Changed — Future Candidate

- Migrate the primary relational persistence engine from MariaDB to PostgreSQL.
```

---

# 526. PostgreSQL Promotion Gate

Antes de promoverla deben existir:

```text
explicit architecture decision

compatibility analysis

schema migration strategy

data migration strategy

driver/configuration changes

container changes

backup/restore changes

tests

rollback strategy

actual migration
```

---

# 527. Database Historical Invariant

Hasta entonces:

```text
MariaDB

=

CURRENT
```

---

# 528. Candidate Distributed Realtime Registry

```markdown
### Changed — Conditional Candidate

- Add distributed realtime coordination for multi-instance application deployment.
```

---

# 529. Redis Promotion Gate

No debe mencionarse necesariamente Redis en la entrada final si la solución elegida utiliza otra tecnología.

---

# 530. Redis Trigger

La necesidad debe proceder de problemas reales como:

```text
multiple application instances

cross-process connection ownership

distributed event delivery
```

---

# 531. Candidate Deployment Registry

```markdown
### Changed — Conditional Candidate

- Introduce orchestration suitable for multi-instance production deployment.
```

---

# 532. Kubernetes Promotion Gate

No debe convertirse automáticamente en:

```text
Kubernetes
```

sin una decisión real.

---

# 533. Current Deployment Invariant

La baseline actual continúa siendo:

```text
Docker

Docker Compose

Nginx

Ubuntu

Hetzner VPS
```

---

# 534. Candidate Storage Registry

```markdown
### Changed — Future Candidate

- Migrate attachment binaries to external object storage.
```

---

# 535. Object Storage Trigger

Debe existir una necesidad concreta relacionada con:

```text
scale

durability

multi-instance deployment

backup strategy

operational separation
```

---

# 536. Candidate PWA Registry

```markdown
### Added — Future Candidate

- Add installable PWA capabilities and controlled offline behavior.
```

---

# 537. PWA Guardrail

No confundir:

```text
responsive web application
```

con:

```text
PWA.
```

---

# 538. Candidate AI Registry

```markdown
### Added — Experimental Future Candidate

- Add AI-assisted functionality for a validated product use case.
```

---

# 539. AI Promotion Gate

Antes de promoverla deben existir:

```text
defined use case

data boundaries

privacy analysis

evaluation criteria

failure behavior

implemented integration
```

---

# 540. Candidate SAML Registry

```markdown
### Added — Future Candidate

- Add SAML-based federated identity integration.
```

---

# 541. SAML Promotion Gate

Debe verificarse:

```text
identity-provider integration

assertion validation

attribute mapping

account linking/provisioning

login flow

logout implications

security tests
```

antes de registrarlo como entregado.

---

# 542. Current SAML Invariant

Hasta entonces:

```text
SAML

=

FUTURE
```

---

# 543. Candidate Multi-tenancy Registry

```markdown
### Added — Conditional Candidate

- Add explicit tenant isolation and tenant-scoped administration.
```

---

# 544. Multi-tenancy Guardrail

No inferir:

```text
Project

=

Tenant
```

sin una decisión explícita.

---

# 545. Candidate Microservices Registry

No debe existir una entrada genérica:

```markdown
- Migrated to microservices.
```

sin una transformación real y verificable.

---

# 546. Better Service Extraction Entry

Si algún día se extrae un boundary concreto:

```markdown
### Changed

- Extracted <domain> into an independently deployable service.
```

---

# 547. Microservices Current Invariant

La arquitectura actual continúa siendo:

```text
Modular Monolith
```

---

# 548. Candidate Performance Registry

```markdown
### Changed — Candidate

- Reduced Dashboard query cost after profiling identified repeated database access.
- Optimized selected SSR views using measured query baselines.
```

---

# 549. Performance Promotion Rule

No registrar:

```text
optimized performance
```

sin medición o evidencia suficiente.

---

# 550. Candidate UI Registry

```markdown
### Changed — Candidate

- Consolidate asynchronous actions around shared Fetch handling.
- Replace remaining native destructive-action dialogs with reusable application dialogs.
- Improve critical workflow accessibility.
```

---

# 551. UI Promotion Rule

Promover únicamente el alcance realmente completado.

---

# 552. Candidate Testing Registry

```markdown
### Added — Candidate

- Add cross-project authorization regression tests.
- Add multi-client realtime integration tests.
- Expand browser-level coverage of critical user journeys.
```

---

# 553. Testing Entry Meaning

Una entrada de testing puede ser relevante incluso sin cambiar comportamiento de usuario cuando mejora significativamente:

```text
regression safety

security confidence

release reliability
```

---

# 554. Candidate Observability Registry

```markdown
### Added — Candidate

- Add operational metrics for realtime connections and subscription behavior.
- Add actionable health monitoring for critical application dependencies.
```

---

# 555. Observability Promotion Rule

No confundir:

```text
logging exists
```

con:

```text
observability stack exists.
```

---

# 556. Candidate Documentation Registry

```markdown
### Fixed — Candidate

- Correct inconsistent internal documentation filenames and references.

### Changed — Candidate

- Clarify CURRENT, PARTIAL, TARGET, PLANNED, FUTURE, and CONDITIONAL capability status across architecture manuals.
```

---

# 557. Documentation Corrections

Entre las correcciones conocidas se encuentran:

```text
37_LOGGIN.md
    →
37_LOGGING.md
```

---

# 558. Technical Challenges Reference

Corregir:

```text
58_TECHNICAL_CHALLENGE.md
```

a:

```text
58_TECHNICAL_CHALLENGES.md
```

---

# 559. Lessons Learned Reference

Corregir referencias obsoletas a:

```text
61_ARCHITECTURE_REVIEW.md
```

porque el documento real es:

```text
61_LESSONS_LEARNED.md
```

---

# 560. Documentation Status Vocabulary

La documentación transversal debe converger hacia:

```text
CURRENT

PARTIAL

TARGET

PLANNED

FUTURE

CONDITIONAL

DEFERRED
```

---

# 561. Cross-document Synchronization

Cuando una capability cambia realmente de estado, deben revisarse los documentos afectados.

---

# 562. Capability Lifecycle Example

```text
FUTURE

↓

PLANNED

↓

CURRENT TASK

↓

IMPLEMENTED

↓

UNRELEASED

↓

RELEASED

↓

HISTORICAL
```

---

# 563. Not Every Capability Uses Every State

Una capability puede:

```text
be discarded

remain conditional

be deferred

skip formal roadmap stages
```

---

# 564. Current Tasks Synchronization

Cuando una tarea se completa:

```text
53_CURRENT_TASKS.md

↓

remove/archive active task
```

y, si el cambio está integrado:

```text
55_CHANGELOG.md

↓

add to Unreleased
```

---

# 565. Known Issues Synchronization

Cuando se corrige un problema relevante:

```text
54_KNOWN_ISSUES.md

↓

mark resolved/archive

+

55_CHANGELOG.md

↓

record meaningful fix
```

---

# 566. Technical Debt Synchronization

Cuando se elimina deuda relevante:

```text
56_TECHNICAL_DEBT.md

↓

update debt status
```

y, si tiene impacto suficiente:

```text
55_CHANGELOG.md

↓

record outcome
```

---

# 567. Roadmap Synchronization

Cuando una capability futura se activa:

```text
47_PRODUCT_ROADMAP.md

↓

update roadmap status

53_CURRENT_TASKS.md

↓

register execution
```

pero todavía:

```text
not Changelog
```

hasta que exista implementación integrada.

---

# 568. Future Evolution Synchronization

`62_FUTURE_EVOLUTION.md` puede describir posibilidades.

Cuando una de ellas se adopte realmente:

```text
Future Evolution

↓

Architecture Decision

↓

Current Tasks

↓

Implementation

↓

Changelog
```

---

# 569. Architecture Decision Synchronization

Las decisiones significativas deben quedar reflejadas en:

```text
52_ARCHITECTURAL_DECISIONS.md
```

cuando corresponda.

---

# 570. Decision Is Not Release

Una decisión aceptada no debe aparecer como:

```text
delivered capability
```

hasta implementarse.

---

# 571. Major Decisions Synchronization

El historial de decisiones debe diferenciar:

```text
decision made

from

decision implemented.
```

---

# 572. Project Evolution Synchronization

`57_PROJECT_EVOLUTION.md` debe derivar su narrativa histórica de hechos compatibles con el Changelog.

---

# 573. Technical Challenges Synchronization

`58_TECHNICAL_CHALLENGES.md` puede explicar problemas y soluciones.

Debe distinguir:

```text
challenge identified

solution designed

solution implemented
```

---

# 574. Timeline Synchronization

`59_IMPLEMENTATION_TIMELINE.md` debe contener únicamente hitos realmente ocurridos o etiquetar explícitamente cualquier planificación.

---

# 575. Timeline PostgreSQL Correction

No debe aparecer:

```text
PostgreSQL standardization
```

como hito completado.

---

# 576. Timeline SAML Correction

No debe aparecer:

```text
SAML integration completed
```

sin evidencia.

---

# 577. Lessons Learned Synchronization

`61_LESSONS_LEARNED.md` puede extraer conclusiones de:

```text
actual implementation experience
```

pero no debe aprender retrospectivamente de migraciones que nunca ocurrieron.

---

# 578. Future Evolution Synchronization

`62_FUTURE_EVOLUTION.md` debe preservar PostgreSQL, Redis, Kubernetes, microservices y otras evoluciones no realizadas como:

```text
future

candidate

or conditional
```

según corresponda.

---

# 579. Release Review Checklist

Antes de cerrar cualquier release:

- [ ] todos los cambios incluidos están integrados;
- [ ] todos los cambios incluidos son verificables;
- [ ] la fecha es real;
- [ ] la versión es real;
- [ ] no existen tareas activas presentadas como terminadas;
- [ ] no existen candidate entries dentro de la release;
- [ ] los breaking changes son visibles;
- [ ] las migrations están documentadas;
- [ ] los cambios de seguridad están identificados;
- [ ] los cambios operativos están identificados;
- [ ] las nuevas variables/configuraciones están identificadas;
- [ ] el wording no exagera el alcance.

---

# 580. Historical Audit Checklist

Para revisar una entrada antigua:

- [ ] ¿Existe evidencia de implementación?
- [ ] ¿La tecnología formaba realmente parte del sistema?
- [ ] ¿La capability estaba completa o solo parcial?
- [ ] ¿Se está confundiendo documentación con código?
- [ ] ¿Se está confundiendo roadmap con historia?
- [ ] ¿Se está confundiendo una decisión con su implementación?
- [ ] ¿Se inventó una fecha?
- [ ] ¿Se inventó una versión?
- [ ] ¿La entrada contradice el baseline verificado?

---

# 581. Database Audit Checklist

- [ ] MariaDB aparece como motor implementado.
- [ ] PostgreSQL no aparece como migración completada.
- [ ] Las migrations corresponden al motor real.
- [ ] Los cambios de esquema se describen con precisión.
- [ ] Backup/restore se actualiza cuando sea necesario.

---

# 582. Authentication Audit Checklist

- [ ] JWT access tokens aparecen como implementados.
- [ ] JWT refresh tokens aparecen como implementados.
- [ ] HTTPOnly cookies aparecen como implementadas.
- [ ] Explicit refresh aparece como implementado.
- [ ] Automatic access refresh aparece como implementado.
- [ ] Rotation no se presenta como implementada sin evidencia.
- [ ] Revocation no se presenta como implementada sin evidencia.
- [ ] SAML no aparece como implementado.

---

# 583. Authorization Audit Checklist

- [ ] RBAC aparece como implementado.
- [ ] Contextual authorization se describe según cobertura real.
- [ ] ProjectMembership no se promociona prematuramente.
- [ ] Cross-project protection no se declara completa sin tests/evidencia.

---

# 584. Realtime Audit Checklist

- [ ] FastAPI WebSockets aparecen como implementados.
- [ ] El Connection Manager actual puede describirse como in-memory.
- [ ] Redis no aparece como dependencia actual.
- [ ] Reconnect no se declara completo sin evidencia.
- [ ] Reconciliation no se declara completa sin evidencia.
- [ ] Subscription authorization no se declara completa sin evidencia.
- [ ] Multi-client testing no se declara completo sin evidencia.

---

# 585. Frontend Audit Checklist

- [ ] Jinja2 SSR aparece como current.
- [ ] Bootstrap/AdminLTE aparecen como current.
- [ ] Modular JavaScript aparece como current.
- [ ] SPA migration no aparece como realizada.
- [ ] Kanban no aparece como current sin implementación.

---

# 586. Infrastructure Audit Checklist

- [ ] Docker aparece como current.
- [ ] Docker Compose aparece como current.
- [ ] Nginx aparece como current.
- [ ] Ubuntu aparece como current.
- [ ] Hetzner VPS aparece como current.
- [ ] Kubernetes no aparece como current.
- [ ] Microservices no aparecen como current architecture.

---

# 587. Storage Audit Checklist

- [ ] Attachment storage actual está descrito según implementación.
- [ ] Object storage no aparece como migración completada.
- [ ] Las implicaciones de backup se reflejan cuando corresponda.

---

# 588. Security Audit Checklist

- [ ] No se utiliza `security complete`.
- [ ] CSRF se describe según estado real.
- [ ] Refresh-token hardening se separa de refresh-token implementation.
- [ ] Cookie-policy hardening se describe según estado real.
- [ ] WebSocket authentication se describe según estado real.
- [ ] Subscription authorization se describe según estado real.

---

# 589. Candidate Entry Audit

Cada candidate entry debe responder:

```text
Is this clearly marked as non-historical?

Could a future reader mistake it for delivered work?

What evidence will be required before promotion?
```

---

# 590. No Guessing Rule

Si no existe evidencia suficiente:

```text
do not guess.
```

---

# 591. Conservative Historical Rule

Cuando exista duda entre:

```text
CURRENT

and

FUTURE
```

investigar antes de promover.

---

# 592. Partial Capability Rule

Cuando exista evidencia de una parte:

```text
describe the implemented part
```

en lugar de clasificar toda la capability como:

```text
complete.
```

---

# 593. Reverse Evidence Rule

Cuando el código contradiga una clasificación documental antigua:

```text
verified code wins
```

para determinar el estado de implementación.

---

# 594. Confirmed Reverse Evidence — Refresh Tokens

La verificación del código actual demuestra:

```text
JWT refresh tokens
    IMPLEMENTED

refresh-token validation
    IMPLEMENTED

explicit refresh endpoint
    IMPLEMENTED

automatic access refresh
    IMPLEMENTED

HTTPOnly refresh cookie
    IMPLEMENTED
```

---

# 595. Confirmed Hardening Gap — Cookies

También existe evidencia de una inconsistencia que debe tratarse como hardening:

```text
login / explicit authentication cookie policy

≠

automatic middleware refresh cookie policy
```

si los atributos no se centralizan de forma coherente.

---

# 596. Cookie Hardening Historical Rule

Hasta que se corrija:

```text
do not claim centralized cookie security policy.
```

---

# 597. Confirmed Non-implementation — SAML

No existe evidencia equivalente que permita promover:

```text
SAML
```

a capability histórica implementada.

---

# 598. Confirmed Non-migration — PostgreSQL

No existe una migración ejecutada:

```text
MariaDB

↓

PostgreSQL
```

---

# 599. Current Database Historical Truth

```text
MariaDB

=

CURRENT

+

HISTORICALLY IMPLEMENTED
```

---

# 600. Current Architecture Historical Truth

```text
Modular Monolith

=

CURRENT ARCHITECTURE
```

---

# 601. Current Realtime Historical Truth

```text
FastAPI WebSockets

+

in-memory Connection Manager

=

CURRENT REALTIME FOUNDATION
```

---

# 602. Current Deployment Historical Truth

```text
Docker

+

Docker Compose

+

Nginx

+

Ubuntu

+

Hetzner VPS

=

CURRENT DEPLOYMENT BASELINE
```

---

# 603. Current Authentication Historical Truth

```text
JWT Access Token

+

JWT Refresh Token

+

HTTPOnly Cookies

+

Explicit Refresh

+

Automatic Access Refresh

=

CURRENT AUTHENTICATION BASELINE
```

---

# 604. Current Authorization Historical Truth

```text
RBAC

=

CURRENT


Contextual Authorization

=

PARTIAL / EVOLVING


ProjectMembership

=

TARGET / IN CONSOLIDATION
```

---

# 605. Current Frontend Historical Truth

```text
Jinja2 SSR

+

Bootstrap / AdminLTE

+

Modular JavaScript

=

CURRENT FRONTEND BASELINE
```

---

# 606. Current Realtime Hardening Truth

```text
WebSockets

=

IMPLEMENTED


Reliable reconnect

Subscription authorization

Reconciliation

Distributed coordination

=

NOT TO BE ASSUMED COMPLETE
```

---

# 607. Current Security Truth

La plataforma dispone de una base de seguridad real y significativa.

Pero:

```text
security baseline

≠

security completion
```

---

# 608. Current Quality Truth

```text
Automated Testing

+

GitHub Actions

=

CURRENT
```

mientras la cobertura continúa evolucionando.

---

# 609. Current Changelog Snapshot

El Changelog debe poder resumir el estado histórico consolidado de esta forma:

```text
IMPLEMENTED

FastAPI
SQLAlchemy
MariaDB
Modular Monolith
Jinja2 SSR
Bootstrap / AdminLTE
Modular JavaScript
JWT Access Tokens
JWT Refresh Tokens
HTTPOnly Cookies
Explicit Token Refresh
Automatic Access Refresh
RBAC
Projects
Tasks
Activities
Attachments
Notifications
Dashboard
Activity Feed
Audit
FastAPI WebSockets
In-memory Connection Management
Docker
Docker Compose
Nginx
Ubuntu
Hetzner VPS
Automated Testing
GitHub Actions
```

---

# 610. Partial / Evolving Snapshot

```text
PARTIAL / EVOLVING

Contextual Authorization
Realtime Reliability Hardening
UI Test Coverage
Realtime Test Coverage
Security Hardening
Performance Optimization
```

---

# 611. Target / Planned Snapshot

```text
TARGET / PLANNED

ProjectMembership consolidation
Project-scoped authorization expansion
Formal CSRF protection
Refresh-token lifecycle hardening
Cookie-policy consolidation
WebSocket authentication hardening
Subscription authorization
Realtime contract normalization
Reconnect / reconciliation
Kanban
Live Kanban
```

---

# 612. Future / Conditional Snapshot

```text
FUTURE / CONDITIONAL

SAML
PostgreSQL migration
Redis
Kubernetes
Microservices
Object Storage migration
PWA
AI / RAG
Multi-tenancy
Multi-region deployment
```

---

# 613. Historical Snapshot Guardrail

La tabla conceptual anterior describe:

```text
implementation status
```

y no:

```text
release chronology.
```

---

# 614. Release Chronology Rule

No inventar una cronología detallada a partir de esta clasificación.

---

# 615. Historical Release Reconstruction

Si posteriormente se desea reconstruir releases antiguas, debe hacerse desde:

```text
Git tags

commit history

migrations

repository state

deployment artifacts
```

---

# 616. Reconstruction Output

Solo entonces podrán generarse entradas como:

```markdown
## [0.X.0] — YYYY-MM-DD
```

con suficiente confianza.

---

# 617. No Synthetic Releases

No transformar automáticamente las fases:

```text
Foundation

IAM

Realtime

UI
```

en versiones ficticias.

---

# 618. Release Naming

Preferir versiones SemVer.

Evitar nombres arbitrarios salvo que el proyecto adopte formalmente release codenames.

---

# 619. Unreleased Maintenance

Después de cada release:

```text
create clean [Unreleased]
```

y comenzar el siguiente ciclo.

---

# 620. Entry Ordering

Dentro de cada categoría, ordenar preferentemente por:

```text
logical relevance
```

en lugar de:

```text
commit order.
```

---

# 621. Security Ordering

Los cambios críticos de seguridad deben ser fáciles de localizar.

---

# 622. Breaking Ordering

Los breaking changes deben aparecer con visibilidad suficiente.

---

# 623. Migration Ordering

Las acciones requeridas para deployment deben situarse cerca del cambio correspondiente.

---

# 624. Changelog Review Ownership

La persona responsable de cortar una release debe revisar:

```text
historical truth

scope

wording

migration impact

security impact
```

---

# 625. Contributor Responsibility

Quien implementa una capability debe proporcionar información suficiente para redactar una entrada correcta.

---

# 626. Reviewer Responsibility

El reviewer debe detectar:

```text
overclaiming

missing migration note

missing security classification

future capability promoted as current
```

---

# 627. Release Owner Responsibility

El release owner debe garantizar coherencia entre:

```text
tag

artifact

Changelog

deployment
```

---

# 628. Changelog Maintenance Anti-patterns

Evitar:

```text
commit dump

roadmap leakage

candidate entries in released history

invented versions

invented dates

technology-name inflation

future architecture presented as current

duplicated entries

vague entries

silent breaking changes
```

---

# 629. Anti-pattern — Technology Inflation

Ejemplo incorrecto:

```markdown
- Modernized persistence with PostgreSQL.
```

si la aplicación continúa usando MariaDB.

---

# 630. Anti-pattern — Security Inflation

Ejemplo incorrecto:

```markdown
- Completed application security hardening.
```

si todavía existen gaps conocidos.

---

# 631. Anti-pattern — IAM Inflation

Ejemplo incorrecto:

```markdown
- Completed enterprise IAM with SAML.
```

si SAML no está implementado.

---

# 632. Anti-pattern — Realtime Inflation

Ejemplo incorrecto:

```markdown
- Completed distributed realtime architecture.
```

si existe únicamente un Connection Manager in-memory.

---

# 633. Anti-pattern — Authorization Inflation

Ejemplo incorrecto:

```markdown
- Completed project-scoped authorization.
```

si ProjectMembership y cobertura contextual siguen evolucionando.

---

# 634. Anti-pattern — Kanban Inflation

Ejemplo incorrecto:

```markdown
- Added collaborative realtime Kanban.
```

si Kanban continúa planificado.

---

# 635. Anti-pattern — Infrastructure Inflation

Ejemplo incorrecto:

```markdown
- Migrated production to Kubernetes.
```

si el deployment real sigue utilizando Docker Compose.

---

# 636. Anti-pattern — AI Inflation

Ejemplo incorrecto:

```markdown
- Added AI-powered platform capabilities.
```

si AI/RAG continúa siendo una posibilidad futura.

---

# 637. Good Historical Entry Principle

Una buena entrada debe ser:

```text
true

specific

bounded

meaningful

verifiable
```

---

# 638. Example — Authentication

```markdown
### Security

- Added JWT refresh-token support with HTTPOnly cookie storage and access-token renewal.
```

---

# 639. Example — Realtime

Si está verificado:

```markdown
### Added

- Added WebSocket-based realtime updates for in-app notifications.
```

---

# 640. Example — Deployment

Si corresponde históricamente:

```markdown
### Changed

- Containerized application deployment with Docker Compose behind Nginx.
```

---

# 641. Example — Audit

```markdown
### Added

- Added persistent audit records for security and business traceability.
```

si el scope corresponde a la implementación real.

---

# 642. Example — Future Security

Todavía candidato:

```markdown
### Security

- Added explicit authorization for project-scoped WebSocket subscriptions.
```

---

# 643. Example — Future Kanban

Todavía candidato:

```markdown
### Added

- Added an SSR-first Kanban board with authorized Task transitions.
```

---

# 644. Example — Future Database

Todavía candidato:

```markdown
### Changed

- Migrated the relational database from MariaDB to PostgreSQL.
```

---

# 645. Example — Future SAML

Todavía candidato:

```markdown
### Added

- Added SAML-based federated identity integration.
```

---

# 646. Example — Conditional Scaling

Todavía condicional:

```markdown
### Changed

- Added distributed realtime coordination for multi-instance deployment.
```

---

# 647. Changelog Health Indicators

El documento está sano cuando:

```text
Unreleased contains only integrated work

released history contains only delivered work

candidate entries are clearly separated

future technologies remain future

historical baseline matches implementation
```

---

# 648. Changelog Warning Indicators

Revisar inmediatamente si aparecen:

```text
PostgreSQL as current

SAML as implemented

Redis as current

Kubernetes as current

microservices as current

Kanban as delivered

ProjectMembership as fully mature

refresh tokens as missing
```

sin nueva evidencia que justifique esos cambios.

---

# 649. Documentation Audit Trigger

Una contradicción entre varios manuales debe provocar:

```text
evidence review
```

antes de elegir una versión de los hechos.

---

# 650. Implementation Evidence Priority

Para determinar estado actual:

```text
verified implementation

>

stale descriptive documentation
```

---

# 651. Historical Documentation Priority

Para reconstruir contexto histórico:

```text
repository evidence

+

validated historical documentation
```

deben combinarse.

---

# 652. Future Documentation Limitation

Los documentos de roadmap y evolución futura no son evidencia histórica de entrega.

---

# 653. Changelog Maintenance Frequency

Actualizar:

```text
when meaningful work is integrated
```

y revisar:

```text
before every release.
```

---

# 654. Avoid End-of-project Reconstruction

No esperar meses para reconstruir retrospectivamente todos los cambios si puede mantenerse `Unreleased` durante el desarrollo.

---

# 655. Small Increment Principle

Es más fiable registrar:

```text
small verified meaningful changes
```

que reconstruir después una gran release desde memoria.

---

# 656. Historical Memory Is Not Evidence

La memoria humana puede ayudar a localizar evidencias.

No debe sustituirlas cuando exista incertidumbre importante.

---

# 657. Changelog and Documentation Audit

La auditoría actual del corpus documental debe utilizar este documento para impedir que:

```text
future architecture

leaks into

historical truth.
```

---

# 658. Documents Requiring Historical Alignment

Especial atención a:

```text
57_PROJECT_EVOLUTION.md

58_TECHNICAL_CHALLENGES.md

59_IMPLEMENTATION_TIMELINE.md

60_MAJOR_DECISIONS.md

61_LESSONS_LEARNED.md

62_FUTURE_EVOLUTION.md
```

---

# 659. Database Alignment

Todos ellos deben respetar:

```text
MariaDB
    CURRENT

PostgreSQL
    FUTURE / CANDIDATE
```

---

# 660. IAM Alignment

Todos ellos deben respetar:

```text
JWT Access
    CURRENT

JWT Refresh
    CURRENT

RBAC
    CURRENT

SAML
    FUTURE
```

---

# 661. Authorization Alignment

Todos ellos deben respetar:

```text
Global RBAC
    CURRENT

Contextual Authorization
    PARTIAL / EVOLVING

ProjectMembership
    TARGET / IN CONSOLIDATION
```

---

# 662. Realtime Alignment

Todos ellos deben respetar:

```text
FastAPI WebSockets
    CURRENT

In-memory Connection Manager
    CURRENT

Reliability Hardening
    EVOLVING

Redis / Distributed Coordination
    CONDITIONAL
```

---

# 663. Deployment Alignment

Todos ellos deben respetar:

```text
Docker
    CURRENT

Docker Compose
    CURRENT

Nginx
    CURRENT

Ubuntu / Hetzner VPS
    CURRENT

Kubernetes
    CONDITIONAL
```

---

# 664. Product Alignment

Todos ellos deben respetar:

```text
Projects
    CURRENT

Tasks
    CURRENT

Activities
    CURRENT

Attachments
    CURRENT

Notifications
    CURRENT

Dashboard
    CURRENT

Activity Feed
    CURRENT

Audit
    CURRENT

Kanban
    PLANNED
```

---

# 665. Future Technology Alignment

Mantener como futuras o condicionales:

```text
PostgreSQL

SAML

Redis

Kubernetes

Microservices

Object Storage migration

PWA

AI / RAG

Multi-tenancy
```

hasta que nueva evidencia cambie su clasificación.

---

# 666. Changelog Final Invariants

Las siguientes reglas son invariantes de mantenimiento:

```text
1. Never invent a release.

2. Never invent a release date.

3. Never promote planned work to history.

4. Never treat documentation as implementation evidence by itself.

5. Never hide a breaking change.

6. Never hide required migration work.

7. Never downgrade verified implementation because documentation is stale.

8. Never present conditional architecture as current infrastructure.

9. Prefer exact scope over broad claims.

10. Preserve historical truth.
```

---

# 667. Final Database Invariant

```text
MariaDB is the implemented relational database.

PostgreSQL is a future candidate.
```

---

# 668. Final Authentication Invariant

```text
Access tokens are implemented.

Refresh tokens are implemented.

HTTPOnly token cookies are implemented.

Explicit refresh is implemented.

Automatic access refresh is implemented.

Advanced refresh-token hardening must be verified separately.
```

---

# 669. Final SAML Invariant

```text
SAML documentation exists.

SAML implementation is FUTURE.
```

---

# 670. Final Authorization Invariant

```text
RBAC is implemented.

Contextual authorization is evolving.

ProjectMembership is a target being consolidated.
```

---

# 671. Final Realtime Invariant

```text
WebSockets are implemented.

Selected realtime features are implemented.

Reliable reconnect and reconciliation require further consolidation.

Redis is conditional.
```

---

# 672. Final Frontend Invariant

```text
Jinja2 SSR is current.

Bootstrap / AdminLTE are current.

Modular JavaScript is current.

Kanban remains planned until implementation evidence exists.
```

---

# 673. Final Deployment Invariant

```text
Docker + Docker Compose + Nginx + Ubuntu + Hetzner VPS

=

current deployment baseline.
```

---

# 674. Final Scaling Invariant

```text
Kubernetes

Microservices

Distributed Broker

Multi-instance Realtime

=

conditional future architecture.
```

---

# 675. Final Product Evolution Invariant

El Changelog debe reflejar:

```text
delivered evolution
```

y nunca sustituir:

```text
Roadmap

Future Evolution

Feature Backlog
```

---

# 676. Final Operational Workflow

```text
Idea

↓

Backlog / Roadmap

↓

Current Task

↓

Implementation

↓

Validation

↓

Integration

↓

Unreleased

↓

Release

↓

Changelog History

↓

Project Evolution / Lessons Learned
```

---

# 677. Final Candidate Workflow

```text
Candidate Changelog Entry

↓

wait for implementation

↓

verify evidence

↓

adapt wording to actual scope

↓

promote to Unreleased

↓

release
```

---

# 678. Final Correction Workflow

Cuando se detecte una afirmación histórica incorrecta:

```text
Detect contradiction

↓

Find implementation evidence

↓

Determine actual state

↓

Correct Changelog

↓

Correct dependent historical documents

↓

Run consistency audit
```

---

# 679. Changelog Maintenance Definition of Done

`55_CHANGELOG.md` se considera correctamente mantenido cuando:

- [ ] el historial representa cambios reales;
- [ ] `Unreleased` contiene únicamente trabajo integrado;
- [ ] candidatos y ejemplos están claramente separados;
- [ ] no existen releases o fechas inventadas;
- [ ] MariaDB permanece como database actual;
- [ ] PostgreSQL permanece futuro/candidato;
- [ ] refresh tokens aparecen como implementados;
- [ ] refresh-token hardening permanece separado;
- [ ] SAML permanece futuro;
- [ ] RBAC aparece como actual;
- [ ] contextual authorization refleja su madurez real;
- [ ] ProjectMembership no se sobredeclara;
- [ ] WebSockets aparecen como actuales;
- [ ] Redis permanece condicional;
- [ ] Docker Compose representa el deployment actual;
- [ ] Kubernetes permanece condicional;
- [ ] Kanban permanece planificado hasta su implementación;
- [ ] las referencias documentales son coherentes.

---

# 680. Changelog Quality Gate

Antes de cada merge que modifique este documento:

```text
Historical truth

↓

Scope precision

↓

Status precision

↓

Security classification

↓

Migration impact

↓

Cross-document consistency
```

---

# 681. No Guessing Final Rule

Cuando una afirmación no pueda verificarse:

```text
do not turn uncertainty into history.
```

---

# 682. Evidence-driven History

La filosofía final es:

```text
Architecture may describe possibilities.

Roadmaps may describe intentions.

Current Tasks may describe execution.

Code demonstrates implementation.

Releases demonstrate delivery.

Changelog records delivered evolution.
```

---

# 683. Changelog as Project Memory

Bien mantenido, el Changelog constituye una memoria técnica compacta del proyecto.

Permite comprender:

```text
where the platform came from

what capabilities were actually added

which boundaries evolved

which risks were corrected

and

how the current system emerged
```

---

# 684. Changelog as Audit Boundary

También actúa como barrera contra un problema frecuente en proyectos con documentación extensa:

```text
future design

↓

repeated in multiple documents

↓

mistaken for implementation

↓

rewritten as historical fact
```

---

# 685. Required Countermeasure

La defensa es:

```text
status vocabulary

+

implementation evidence

+

candidate-entry separation

+

cross-document audit
```

---

# 686. Historical Integrity Example

Correcto:

```text
MariaDB
    implemented

PostgreSQL
    possible future migration
```

Incorrecto:

```text
MariaDB
    old database

PostgreSQL
    standardized current database
```

---

# 687. Authentication Integrity Example

Correcto:

```text
JWT refresh token
    implemented

rotation / reuse detection
    hardening to verify or implement
```

Incorrecto:

```text
refresh tokens
    future capability
```

---

# 688. IAM Integrity Example

Correcto:

```text
RBAC
    implemented

SAML
    future
```

Incorrecto:

```text
enterprise IAM including SAML
    completed
```

---

# 689. Realtime Integrity Example

Correcto:

```text
FastAPI WebSockets
    implemented

in-memory Connection Manager
    implemented

Redis coordination
    conditional
```

Incorrecto:

```text
distributed Redis realtime architecture
    current
```

---

# 690. Deployment Integrity Example

Correcto:

```text
Docker Compose deployment
    current

Kubernetes
    conditional
```

Incorrecto:

```text
container orchestration standardized on Kubernetes
    current
```

---

# 691. Product Integrity Example

Correcto:

```text
Tasks
    current

Kanban
    planned
```

Incorrecto:

```text
collaborative realtime Kanban
    delivered
```

---

# 692. Authorization Integrity Example

Correcto:

```text
RBAC
    mature/current

Contextual Authorization
    partial/evolving

ProjectMembership
    target/in consolidation
```

Incorrecto:

```text
fully mature contextual project authorization
    current
```

---

# 693. Current Changelog State Model

El documento queda gobernado por cuatro áreas claramente diferenciadas:

```text
RELEASED HISTORY

    verified delivered changes


UNRELEASED

    verified integrated changes


CANDIDATE ENTRIES

    possible future release wording


GOVERNANCE

    rules preserving historical truth
```

---

# 694. Released History Rule

```text
Released

=

implemented

+

validated

+

released
```

---

# 695. Unreleased Rule

```text
Unreleased

=

implemented

+

validated

+

integrated

-

not yet released
```

---

# 696. Candidate Rule

```text
Candidate

=

not historical fact
```

---

# 697. Future Rule

```text
Future

=

possible later capability

not

current stack
```

---

# 698. Conditional Rule

```text
Conditional

=

adopt only if trigger justifies complexity.
```

---

# 699. Current Baseline Reference

Para futuras revisiones del Changelog, utilizar como baseline:

```text
APPLICATION
    FastAPI
    Modular Monolith

PERSISTENCE
    SQLAlchemy
    MariaDB

FRONTEND
    Jinja2 SSR
    Bootstrap / AdminLTE
    Modular JavaScript

AUTHENTICATION
    JWT Access Tokens
    JWT Refresh Tokens
    HTTPOnly Cookies
    Explicit Refresh
    Automatic Access Refresh

AUTHORIZATION
    RBAC
    Partial Contextual Authorization

COLLABORATION
    Projects
    Tasks
    Activities
    Attachments

AWARENESS
    Notifications
    Dashboard
    Activity Feed
    Audit

REALTIME
    FastAPI WebSockets
    In-memory Connection Manager

QUALITY
    Automated Testing
    GitHub Actions

DEPLOYMENT
    Docker
    Docker Compose
    Nginx
    Ubuntu
    Hetzner VPS
```

---

# 700. Non-baseline Reference

No incluir como baseline actual:

```text
PostgreSQL

SAML

Redis

Kubernetes

Microservices

Object Storage migration

PWA

AI / RAG

Multi-tenancy

Kanban
```

---

# 701. Evolving Baseline Reference

Tratar con precisión:

```text
Contextual Authorization

ProjectMembership

CSRF Hardening

Refresh-token Hardening

Cookie-policy Hardening

WebSocket Security Hardening

Reconnect

Reconciliation

UI Testing

Realtime Testing

SSR Performance
```

---

# 702. Future Changelog Update Protocol

Cuando se complete una tarea:

```text
1. Verify implementation.

2. Verify tests.

3. Determine user / developer / operator impact.

4. Select changelog category.

5. Write bounded entry.

6. Add to Unreleased.

7. Update related status documents.

8. Release normally.
```

---

# 703. Future Release Audit Protocol

Antes de crear una versión:

```text
1. Review Unreleased.

2. Remove accidental future entries.

3. Verify breaking changes.

4. Verify migrations.

5. Verify security changes.

6. Verify operational actions.

7. Assign real SemVer.

8. Add real date.

9. Tag.

10. Preserve history.
```

---

# 704. Historical Audit Protocol

Cuando se revise una fase antigua:

```text
1. Locate evidence.

2. Verify capability.

3. Verify technology.

4. Verify temporal placement if possible.

5. Avoid invented dates.

6. Avoid invented releases.

7. Correct false future-to-history promotion.

8. Correct stale history-to-future demotion.

9. Synchronize dependent documents.
```

---

# 705. Documentation Audit Protocol

Después de corregir el conjunto documental:

```text
search globally for:

PostgreSQL

SAML

Redis

Kubernetes

microservices

ProjectMembership

Kanban

refresh token

CSRF

WebSocket authorization
```

y comprobar cada aparición en su contexto.

---

# 706. PostgreSQL Audit Pattern

Cada aparición debe clasificarse como:

```text
future candidate

migration discussion

conditional evolution

comparison
```

salvo que una implementación futura cambie la realidad.

---

# 707. SAML Audit Pattern

Cada aparición debe clasificarse como:

```text
future integration

design

candidate

planned possibility
```

hasta implementación real.

---

# 708. Redis Audit Pattern

Cada aparición debe clasificarse como:

```text
conditional scaling mechanism
```

salvo adopción futura.

---

# 709. Kubernetes Audit Pattern

Cada aparición debe clasificarse como:

```text
conditional deployment evolution
```

salvo migración futura.

---

# 710. Refresh Token Audit Pattern

Cada aparición debe diferenciar:

```text
refresh-token support
    CURRENT

from

refresh-token hardening
    EVOLVING
```

---

# 711. ProjectMembership Audit Pattern

Cada aparición debe diferenciar:

```text
current Project relationships

from

target explicit ProjectMembership model.
```

---

# 712. Kanban Audit Pattern

Cada aparición debe diferenciar:

```text
current Task status model

from

planned Kanban UI.
```

---

# 713. Realtime Audit Pattern

Cada aparición debe diferenciar:

```text
current WebSocket functionality

from

future reliability / distributed scaling.
```

---

# 714. Changelog Long-term Evolution

Si el número de releases crece significativamente, puede evaluarse:

```text
archive older major versions

generate release pages

use changelog fragments

automate link generation
```

---

# 715. Long-term Guardrail

No introducir esa complejidad antes de necesitarla.

---

# 716. Changelog Scalability

El documento puede seguir siendo único mientras permanezca:

```text
navigable

maintainable

reviewable
```

---

# 717. Archive Strategy

Si en el futuro fuera necesario:

```text
CHANGELOG.md

↓

recent releases


docs/changelog/

↓

historical major versions
```

---

# 718. Archive Integrity

Archivar no significa eliminar historial.

---

# 719. Release Automation Future

Puede automatizarse:

```text
version consistency

tag validation

release link generation

empty Unreleased creation
```

---

# 720. Human Curation Remains Required

No automatizar completamente:

```text
historical meaning

security classification

scope wording

future/current distinction
```

---

# 721. Changelog Success Criteria

`55_CHANGELOG.md` cumple su función cuando un lector puede distinguir sin ambigüedad:

```text
what exists

what changed

what was released

what is still being built

what is only planned

what is merely conditional
```

---

# 722. Final Summary

El Changelog de Aula Robótica Platform debe conservar una historia basada en evidencia.

El baseline histórico actualmente validado incluye:

```text
FastAPI

SQLAlchemy

MariaDB

Modular Monolith

Jinja2 SSR

Bootstrap / AdminLTE

Modular JavaScript

JWT Access Tokens

JWT Refresh Tokens

HTTPOnly Cookies

Explicit Token Refresh

Automatic Access Refresh

RBAC

Projects

Tasks

Activities

Attachments

Notifications

Dashboard

Activity Feed

Audit

FastAPI WebSockets

In-memory Realtime Connection Management

Docker

Docker Compose

Nginx

Ubuntu

Hetzner VPS

Automated Testing

GitHub Actions
```

---

# 723. Final Non-current Summary

No deben convertirse en historia implementada sin nueva evidencia:

```text
PostgreSQL migration

SAML integration

Redis-backed realtime

Kubernetes deployment

Microservices architecture

Object Storage migration

PWA

AI / RAG

Multi-tenancy

Kanban

Live Kanban
```

---

# 724. Final Evolving Summary

Deben describirse con precisión como áreas parciales, de hardening o próximas:

```text
Contextual Authorization

ProjectMembership

Formal CSRF Protection

Refresh-token Security Hardening

Cookie-policy Consistency

WebSocket Authentication Hardening

Subscription Authorization

Realtime Event Normalization

Reconnect

Reconciliation

UI Test Expansion

Realtime Test Expansion

SSR Performance Optimization
```

---

# 725. Final Historical Principle

```text
Do not document what the architecture could become

as if it were what the platform already became.
```

---

# 726. Final Evidence Principle

```text
Verified implementation

defines current capability.

Verified release

defines delivered history.
```

---

# 727. Final Changelog Principle

```text
Roadmap describes intention.

Current Tasks describe execution.

Code demonstrates implementation.

Releases demonstrate delivery.

Changelog preserves history.
```

---

# 728. Conclusion

`55_CHANGELOG.md` debe funcionar como la memoria curada de la evolución entregada de Aula Robótica Platform.

Su valor depende menos de registrar una gran cantidad de cambios que de preservar correctamente la frontera entre:

```text
REALITY

and

INTENTION
```

La regla final es:

```text
Record what happened.

Describe exactly what changed.

Never invent when it happened.

Never promote what has not happened.

Preserve the evidence.

Preserve the history.
```
