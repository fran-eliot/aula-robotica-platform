# 56_TECHNICAL_DEBT.md

# Aula Robótica Platform — Technical Debt

## Parte 1/3 — Propósito, modelo de deuda, clasificación, severidad, prioridad, ciclo de vida, ownership, registro y criterios de gestión

---

# 1. Propósito

Este documento mantiene el registro oficial de:

```text
Technical Debt
```

de Aula Robótica Platform.

Su objetivo es identificar, clasificar, priorizar y gestionar compromisos técnicos que:

```text
are currently acceptable

but

should not become permanent architecture by accident.
```

---

# 2. Primary Objective

El registro debe permitir responder:

```text
What technical compromises currently exist?

Why do they exist?

What risk do they create?

When should they be addressed?

What would resolving them require?
```

---

# 3. Nature of this Document

`56_TECHNICAL_DEBT.md` es:

```text
a living engineering governance document
```

---

# 4. Core Principle

Technical Debt no significa simplemente:

```text
bad code
```

---

# 5. Better Definition

En este proyecto se entiende como:

```text
a known technical compromise
whose future cost or risk is understood
and intentionally tracked.
```

---

# 6. Debt Can Be Intentional

Puede existir deuda porque se decidió conscientemente:

```text
ship simpler implementation first

defer optimization

avoid premature abstraction

validate product behavior

reduce initial complexity
```

---

# 7. Debt Can Be Emergent

También puede aparecer debido a:

```text
product evolution

new requirements

architecture growth

unexpected usage

legacy assumptions

temporary fixes
```

---

# 8. Debt Is Not Automatically Failure

Una cantidad razonable de deuda puede ser compatible con:

```text
good engineering
```

si está:

```text
known

bounded

prioritized

managed
```

---

# 9. Dangerous Debt

La deuda se vuelve peligrosa cuando:

```text
nobody knows it exists

nobody owns it

risk keeps growing

workarounds accumulate

or

temporary decisions become permanent silently.
```

---

# 10. Core Governance Principle

```text
Technical debt may be deferred.

It must not be forgotten.
```

---

# 11. Document Scope

Este documento registra principalmente deuda relacionada con:

```text
architecture

security

backend

frontend

database

realtime

testing

performance

observability

operations

developer experience

documentation
```

---

# 12. It Is Not

No debe utilizarse como:

```text
feature backlog

bug tracker

current task list

known issue list

product roadmap

changelog

ADR replacement
```

---

# 13. Document Separation

```text
CURRENT_TASKS

→ work being executed now


KNOWN_ISSUES

→ observable defects or limitations


TECHNICAL_DEBT

→ structural compromises that increase future cost or risk


FEATURE_BACKLOG

→ future capabilities


PRODUCT_ROADMAP

→ strategic sequencing


ARCHITECTURAL_DECISIONS

→ stable technical decisions


CHANGELOG

→ delivered historical changes
```

---

# 14. Technical Debt vs Known Issue

Un Known Issue describe principalmente:

```text
something currently wrong,
limited,
or unreliable.
```

---

# 15. Technical Debt

Describe principalmente:

```text
a structural engineering weakness
that may or may not produce an immediate visible defect.
```

---

# 16. Example — Known Issue

```text
WebSocket reconnect can leave the current view stale.
```

---

# 17. Example — Technical Debt

```text
Realtime modules do not share a centralized reconciliation strategy.
```

---

# 18. Relationship

El Known Issue puede ser una consecuencia de la deuda.

---

# 19. Example Flow

```text
Fragmented reconnect handling
        ↓
Technical Debt
        ↓
Stale state after reconnect
        ↓
Known Issue
```

---

# 20. Technical Debt vs Current Task

Technical Debt puede existir durante meses.

---

# 21. Current Task

Representa:

```text
work selected for execution now.
```

---

# 22. Promotion Flow

```text
Technical Debt

↓

Prioritized

↓

Current Task

↓

Implementation

↓

Validation

↓

Resolved
```

---

# 23. Technical Debt vs ADR

Una ADR explica:

```text
why an architectural decision exists.
```

---

# 24. Technical Debt Entry

Puede indicar:

```text
why part of the current implementation should eventually change.
```

---

# 25. ADR Is Not Debt

Una decisión simple o monolítica no constituye deuda automáticamente.

---

# 26. Example

```text
Use modular monolith architecture
```

puede ser una decisión correcta.

---

# 27. Wrong Interpretation

No registrar:

```text
TD: Application is not microservices.
```

si no existe una necesidad real de microservices.

---

# 28. Architecture Principle

```text
Complexity not implemented is not technical debt.
```

---

# 29. Missing Feature Is Not Debt

No registrar:

```text
No Kanban board.
```

como Technical Debt.

---

# 30. Correct Location

Eso pertenece a:

```text
Feature Backlog

or

Product Roadmap.
```

---

# 31. Missing Optimization Is Not Automatically Debt

No tener Redis no significa:

```text
technical debt.
```

---

# 32. It Becomes Debt When

Existe evidencia de que:

```text
current architecture cannot meet required performance
without repeated workarounds.
```

---

# 33. Missing Technology Is Not Debt

No utilizar:

```text
Kafka

Kubernetes

microservices

GraphQL

Redis

Celery
```

no constituye deuda por sí mismo.

---

# 34. Technology Neutrality

La deuda debe definirse por:

```text
engineering problem
```

y no por:

```text
technology envy.
```

---

# 35. Good Debt Statement

```text
Notification delivery currently performs synchronous work that can increase request latency under sustained fan-out.
```

---

# 36. Poor Debt Statement

```text
We do not use Kafka.
```

---

# 37. Technical Debt Categories

Aula Robótica Platform debe utilizar categorías estables.

---

# 38. Recommended Categories

```text
ARCHITECTURE

SECURITY

BACKEND

FRONTEND

DATABASE

REALTIME

TESTING

PERFORMANCE

OBSERVABILITY

OPERATIONS

DX

DOCUMENTATION
```

---

# 39. ARCHITECTURE

Para compromisos que afectan:

```text
system boundaries

module coupling

shared abstractions

dependency direction

domain separation

extension cost
```

---

# 40. Architecture Example

```text
Authorization rules are duplicated across multiple domain services.
```

---

# 41. SECURITY

Para compromisos estructurales que debilitan:

```text
authentication

authorization

session handling

secret management

input trust

security boundaries
```

---

# 42. Security Example

```text
Project-scoped authorization is not yet centralized around explicit membership policies.
```

---

# 43. BACKEND

Para deuda relacionada con:

```text
service structure

router complexity

domain logic

error handling

background work

backend abstractions
```

---

# 44. Backend Example

```text
Some request handlers still combine orchestration, validation, persistence, and presentation concerns.
```

---

# 45. FRONTEND

Para compromisos en:

```text
Jinja structure

JavaScript modules

UI state

accessibility

component reuse

browser behavior
```

---

# 46. Frontend Example

```text
Some dynamic views still implement independent loading and error-state conventions.
```

---

# 47. DATABASE

Para deuda relacionada con:

```text
schema design

constraints

indexes

migration safety

query patterns

data lifecycle
```

---

# 48. Database Example

```text
Selected relationship invariants are enforced primarily in application code rather than database constraints.
```

---

# 49. REALTIME

Para deuda relacionada con:

```text
WebSocket contracts

subscriptions

connection lifecycle

reconnect

delivery

ordering

idempotency

state reconciliation
```

---

# 50. Realtime Example

```text
Realtime consumers do not yet use a fully standardized event envelope and reconciliation contract.
```

---

# 51. TESTING

Para deuda relacionada con:

```text
coverage gaps

missing test layers

flaky tests

slow suites

missing security regression

missing browser tests

missing multi-client tests
```

---

# 52. Testing Example

```text
Critical realtime collaboration behavior lacks complete multi-client integration coverage.
```

---

# 53. PERFORMANCE

Para compromisos que producen:

```text
avoidable latency

unbounded queries

N+1 patterns

excessive payloads

unbounded lists

resource inefficiency
```

---

# 54. Performance Example

```text
Selected SSR detail views perform repeated relationship queries that should be consolidated.
```

---

# 55. OBSERVABILITY

Para deuda relacionada con:

```text
logs

metrics

traces

correlation

diagnostic context

operational visibility
```

---

# 56. Observability Example

```text
Realtime failures cannot yet be correlated consistently across HTTP mutation, event publication, and WebSocket delivery.
```

---

# 57. OPERATIONS

Para deuda relacionada con:

```text
deployment

backup

restore

configuration

health checks

release safety

production recovery
```

---

# 58. Operations Example

```text
Backup procedures exist but automated restore validation is not yet part of operational governance.
```

---

# 59. DX

Developer Experience incluye:

```text
local setup

tooling

automation

feedback loops

repository ergonomics

development workflow
```

---

# 60. DX Example

```text
Local environment initialization still requires several manual configuration steps.
```

---

# 61. DOCUMENTATION

Para documentación cuya ausencia crea riesgo técnico real.

---

# 62. Documentation Example

```text
Critical recovery procedures are not yet validated and documented as executable runbooks.
```

---

# 63. Documentation Guardrail

No registrar cada documento pendiente como deuda.

---

# 64. Documentation Debt Exists When

La ausencia:

```text
creates operational risk

blocks maintenance

causes repeated mistakes

or

makes critical knowledge dependent on one person.
```

---

# 65. Cross-category Debt

Una deuda puede afectar varias áreas.

---

# 66. Primary Category

Debe elegirse:

```text
one primary category
```

para evitar duplicación.

---

# 67. Secondary Tags

Opcionalmente puede registrar:

```text
Related Areas
```

---

# 68. Example

```text
Category: REALTIME
Related Areas: SECURITY, TESTING
```

---

# 69. Debt Identifier

Cada deuda debe tener identificador estable.

---

# 70. Recommended Format

```text
TD-001

TD-002

TD-003
```

---

# 71. Identifier Stability

Una vez asignado:

```text
never reuse it
```

---

# 72. Deleted Debt

No eliminar silenciosamente IDs históricos.

---

# 73. Resolved Debt

Debe marcarse:

```text
RESOLVED
```

---

# 74. Rejected Debt

Si se determina que algo no era realmente deuda:

```text
CLOSED_NOT_DEBT
```

---

# 75. Superseded Debt

Si otra entry la reemplaza:

```text
SUPERSEDED
```

---

# 76. Duplicate Debt

Si se detecta duplicado:

```text
DUPLICATE
```

y se referencia la entry canónica.

---

# 77. Debt Statuses

Estados recomendados:

```text
IDENTIFIED

ACCEPTED

PRIORITIZED

IN_PROGRESS

BLOCKED

RESOLVED

CLOSED_NOT_DEBT

SUPERSEDED

DUPLICATE
```

---

# 78. IDENTIFIED

Significa:

```text
debt discovered

but

not yet fully assessed.
```

---

# 79. ACCEPTED

Significa:

```text
debt is understood

and

deliberately deferred.
```

---

# 80. PRIORITIZED

Significa:

```text
debt should enter execution planning.
```

---

# 81. IN_PROGRESS

Significa:

```text
active remediation work exists.
```

---

# 82. BLOCKED

Significa:

```text
remediation cannot currently progress.
```

---

# 83. RESOLVED

Significa:

```text
structural weakness has been removed
or reduced to the accepted target state.
```

---

# 84. CLOSED_NOT_DEBT

Significa que tras análisis:

```text
current implementation is acceptable

and

no remediation is required.
```

---

# 85. SUPERSEDED

Significa:

```text
another debt entry now represents the problem more accurately.
```

---

# 86. DUPLICATE

Significa:

```text
the same structural concern already exists elsewhere.
```

---

# 87. Debt Lifecycle

```text
IDENTIFIED

↓

Assessment

↓

ACCEPTED / PRIORITIZED / CLOSED_NOT_DEBT

↓

IN_PROGRESS

↓

Validation

↓

RESOLVED
```

---

# 88. Deferred Lifecycle

```text
IDENTIFIED

↓

ACCEPTED

↓

Periodic Review

↓

PRIORITIZED

↓

IN_PROGRESS

↓

RESOLVED
```

---

# 89. Blocked Lifecycle

```text
PRIORITIZED

↓

BLOCKED

↓

dependency resolved

↓

PRIORITIZED / IN_PROGRESS
```

---

# 90. Debt Severity

Severity representa:

```text
technical consequence if the debt remains.
```

---

# 91. Recommended Severity Levels

```text
S0 — Critical

S1 — High

S2 — Medium

S3 — Low
```

---

# 92. S0 — Critical

Deuda que crea riesgo inmediato de:

```text
security compromise

data corruption

major production instability

unrecoverable failure
```

---

# 93. S0 Policy

```text
S0 should not remain accepted debt.
```

---

# 94. S0 Action

Debe convertirse inmediatamente en:

```text
Current Task

or

incident remediation.
```

---

# 95. S1 — High

Deuda con impacto significativo sobre:

```text
security

reliability

maintainability

scalability

release safety
```

---

# 96. S1 Example

```text
Project authorization rules are distributed and cannot guarantee consistent nested-resource enforcement.
```

---

# 97. S1 Policy

Debe tener:

```text
explicit owner

review date

remediation direction
```

---

# 98. S2 — Medium

Deuda que:

```text
increases engineering cost

creates recurring complexity

limits extension

or

causes moderate operational friction.
```

---

# 99. S2 Example

```text
Some SSR views duplicate query/context assembly logic.
```

---

# 100. S3 — Low

Deuda principalmente relacionada con:

```text
cleanup

consistency

minor maintainability friction

small DX improvements
```

---

# 101. S3 Example

```text
Legacy helper naming is inconsistent across a small number of frontend modules.
```

---

# 102. Severity Is Not Priority

```text
Severity

≠

Priority
```

---

# 103. Severity Meaning

```text
How bad is the debt?
```

---

# 104. Priority Meaning

```text
How soon should we address it?
```

---

# 105. Priority Levels

```text
P0 — Immediate

P1 — Next

P2 — Planned

P3 — Opportunistic
```

---

# 106. P0 — Immediate

Debe trabajarse:

```text
now
```

---

# 107. Typical P0

```text
S0 debt

release blocker

active security exposure

data integrity risk
```

---

# 108. P1 — Next

Debe entrar en:

```text
next engineering cycle
```

---

# 109. Typical P1

```text
security hardening

critical authorization structure

realtime reliability

release safety
```

---

# 110. P2 — Planned

Importante, pero puede esperar hasta que:

```text
higher-risk foundations are complete.
```

---

# 111. P3 — Opportunistic

Resolver cuando:

```text
touching the area anyway

or

cost is very low.
```

---

# 112. Priority Matrix

```text
S0 → normally P0

S1 → normally P0/P1

S2 → normally P1/P2

S3 → normally P2/P3
```

---

# 113. Exception

Puede existir:

```text
S2 / P1
```

si bloquea una capability estratégica inmediata.

---

# 114. Another Exception

Puede existir:

```text
S1 / P2
```

solo con justificación explícita.

---

# 115. Risk Model

Cada deuda debería evaluarse por:

```text
Impact

Likelihood

Growth

Blast Radius

Remediation Cost
```

---

# 116. Impact

Pregunta:

```text
If this debt becomes problematic,
how serious is the consequence?
```

---

# 117. Likelihood

Pregunta:

```text
How likely is the debt to cause problems
under expected usage?
```

---

# 118. Growth

Pregunta:

```text
Will this debt become more expensive
as the system evolves?
```

---

# 119. Blast Radius

Pregunta:

```text
How much of the platform can it affect?
```

---

# 120. Remediation Cost

Pregunta:

```text
How expensive will it be to fix later?
```

---

# 121. Debt Interest

Technical Debt genera:

```text
interest
```

cuando aumenta continuamente el coste de trabajar alrededor de ella.

---

# 122. Examples of Debt Interest

```text
more duplicated code

more regression risk

more complex tests

slower feature delivery

more production incidents

harder onboarding
```

---

# 123. High-interest Debt

Debe priorizarse aunque todavía no haya producido un incidente grave.

---

# 124. Example

```text
Duplicated authorization logic
```

puede crecer cada vez que se añade:

```text
new module

new endpoint

new realtime event
```

---

# 125. Debt Growth Indicator

Una señal fuerte es:

```text
Every new feature requires another workaround.
```

---

# 126. Debt Trigger

Cada entry debería indicar:

```text
what condition should trigger remediation.
```

---

# 127. Trigger Examples

```text
before enabling cross-user collaboration

before production deployment

before 1.0

before adding another realtime module

when query count exceeds threshold

when second storage backend is required
```

---

# 128. Trigger Value

Evita dejar deuda con:

```text
fix someday
```

---

# 129. Review Date

Las deudas aceptadas deben tener:

```text
Review
```

---

# 130. Example

```text
Review: before next security hardening cycle
```

---

# 131. Prefer Event-based Reviews

Cuando sea posible:

```text
before Kanban implementation
```

es más útil que:

```text
review eventually.
```

---

# 132. Date-based Review

También puede utilizarse:

```text
Review: 2026-Q4
```

---

# 133. Ownership

Cada deuda relevante debe tener:

```text
Owner
```

---

# 134. Owner Meaning

No significa:

```text
the person who caused the debt.
```

---

# 135. Correct Meaning

Significa:

```text
the person or area responsible for ensuring it is reviewed.
```

---

# 136. Ownership Options

```text
Maintainer

Backend

Frontend

Security

Platform

Database

Realtime
```

según organización futura.

---

# 137. Current Project

Mientras exista un maintainer principal puede utilizarse:

```text
Owner: Maintainer
```

---

# 138. Debt Origin

Puede registrarse:

```text
Origin
```

cuando aporte contexto.

---

# 139. Origin Examples

```text
Initial MVP

Temporary hotfix

Architecture growth

Legacy implementation

Deferred hardening

Performance trade-off
```

---

# 140. Origin Is Not Blame

No debe utilizarse para identificar:

```text
who made a mistake.
```

---

# 141. Debt Rationale

Cada entry debe explicar:

```text
why the current compromise exists.
```

---

# 142. Good Rationale

```text
The initial realtime implementation prioritized delivery of notifications and feed updates before introducing a shared event contract.
```

---

# 143. Poor Rationale

```text
Bad design.
```

---

# 144. Consequence

Cada entry debe explicar:

```text
what happens if we keep it.
```

---

# 145. Example Consequence

```text
Adding new realtime modules requires repeated event parsing and reconnect logic, increasing divergence and regression risk.
```

---

# 146. Remediation Direction

Debe indicar:

```text
what kind of change would resolve the debt.
```

---

# 147. Remediation Is Not Full Design

No necesita contener toda la implementación.

---

# 148. Example

```text
Introduce a versioned realtime event envelope and shared client dispatcher.
```

---

# 149. Acceptance Criteria

Las deudas prioritarias deben definir:

```text
how we know the debt is actually resolved.
```

---

# 150. Example

```text
All realtime modules consume the same versioned envelope and no longer implement independent event parsing.
```

---

# 151. Evidence

Cuando se resuelve, debe registrar evidencia.

---

# 152. Evidence Examples

```text
PR

tests

benchmark

ADR

release

migration
```

---

# 153. Resolution Date

Una deuda resuelta debe incluir:

```text
Resolved: YYYY-MM-DD
```

---

# 154. Resolution Release

Cuando corresponda:

```text
Release: X.Y.Z
```

---

# 155. Changelog Relationship

Una resolución significativa debe aparecer también en:

```text
55_CHANGELOG.md
```

---

# 156. Debt Entry Template

La plantilla recomendada es:

```markdown
## TD-XXX — Short technical debt title

**Status:** IDENTIFIED  
**Category:** ARCHITECTURE  
**Related Areas:** BACKEND, TESTING  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Architecture growth  
**Review:** Before <trigger>

### Context

...

### Current Compromise

...

### Why It Exists

...

### Consequences

...

### Debt Interest

...

### Remediation Direction

...

### Trigger

...

### Acceptance Criteria

- [ ] ...
- [ ] ...

### Related

- ...

### Resolution

Not resolved.
```

---

# 157. Compact Entry

Para deuda menor puede utilizarse una variante más corta.

---

# 158. Compact Template

```markdown
## TD-XXX — Title

**Status:** ACCEPTED  
**Category:** DX  
**Severity:** S3  
**Priority:** P3  
**Owner:** Maintainer

### Debt

...

### Impact

...

### Resolution

...
```

---

# 159. Full Template Use

Utilizar el formato completo para:

```text
S0

S1

cross-cutting debt

security debt

architecture debt

realtime debt

data debt
```

---

# 160. Debt Title

Debe describir el problema estructural.

---

# 161. Good Titles

```text
TD-001 — Project authorization is not centralized

TD-002 — Realtime event contracts are fragmented

TD-003 — Critical realtime workflows lack multi-client coverage
```

---

# 162. Poor Titles

```text
TD-001 — Fix auth

TD-002 — WebSocket stuff

TD-003 — Tests
```

---

# 163. Title Rule

Preferir:

```text
problem statement
```

sobre:

```text
solution statement.
```

---

# 164. Why

La solución puede cambiar durante análisis.

---

# 165. Example

Mejor:

```text
Realtime event contracts are fragmented
```

que:

```text
Implement EventBus class.
```

---

# 166. Debt Description Rule

Debe describir:

```text
current reality
```

no una arquitectura hipotética.

---

# 167. Evidence-based Debt

Cuando sea posible debe existir evidencia como:

```text
duplicated modules

missing tests

query measurements

incident history

security review

architecture review
```

---

# 168. Avoid Speculative Debt

No registrar:

```text
This may become slow if we have 100 million users.
```

sin escenario razonable.

---

# 169. Scale Assumptions

La deuda debe evaluarse contra:

```text
expected platform scale
```

---

# 170. Avoid Hyperscale Architecture

Aula Robótica Platform no debe introducir deuda artificial por no estar diseñada para:

```text
Netflix-scale traffic

global multi-region active-active

billions of events
```

si no son requisitos.

---

# 171. Simplicity Principle

```text
A simple architecture that satisfies requirements
is not debt.
```

---

# 172. Premature Abstraction

Introducir abstracciones sin necesidad también puede generar deuda.

---

# 173. Example

```text
Generic repository framework used by only one entity
and harder to maintain than direct persistence logic.
```

podría convertirse en deuda.

---

# 174. Overengineering Debt

Debe reconocerse también:

```text
unnecessary abstraction

unused infrastructure

excessive indirection

technology introduced without requirement
```

---

# 175. Debt Is Bidirectional

Puede aparecer por:

```text
too little structure

or

too much structure.
```

---

# 176. Current Architecture Guardrail

El modular monolith no debe considerarse deuda mientras siga proporcionando:

```text
clear boundaries

acceptable deployment

acceptable scalability

maintainability
```

---

# 177. Microservice Trigger

Solo evaluar separación cuando exista evidencia como:

```text
independent scaling need

independent deployment need

clear ownership boundary

isolated reliability requirement
```

---

# 178. Microservices Are Not Debt Repayment by Default

Migrar a microservices puede:

```text
increase debt
```

si se hace prematuramente.

---

# 179. Realtime Infrastructure Guardrail

Tampoco introducir:

```text
Kafka

Redis Streams

RabbitMQ
```

únicamente para “modernizar”.

---

# 180. Event Infrastructure Trigger

Debe existir necesidad como:

```text
durable asynchronous processing

cross-process fan-out

delivery guarantees

high event volume

independent consumers
```

---

# 181. Current WebSocket Simplicity

Mientras un proceso y connection manager satisfagan los requisitos:

```text
that simplicity is acceptable.
```

---

# 182. Future Scaling Debt

Solo debe registrarse cuando el deployment model cambie de forma que la solución actual deje de funcionar correctamente.

---

# 183. Database Guardrail

PostgreSQL no debe considerarse deuda por no usar:

```text
multiple databases

NoSQL

distributed database
```

---

# 184. ORM Guardrail

SQLAlchemy no debe considerarse deuda por existir queries manuales cuando esas queries sean:

```text
clear

tested

efficient
```

---

# 185. Frontend Guardrail

SSR + Jinja2 + progressive enhancement no es deuda por no utilizar:

```text
React

Vue

Angular
```

---

# 186. Frontend Debt Trigger

Debe existir problema real como:

```text
unmanageable client state

duplicated browser logic

accessibility regressions

interaction complexity
```

---

# 187. Testing Guardrail

No perseguir:

```text
100% coverage
```

como objetivo aislado.

---

# 188. Testing Debt

Debe definirse por:

```text
unprotected risk
```

---

# 189. Example

Mejor:

```text
Cross-project authorization has no negative regression matrix.
```

que:

```text
Coverage is only 87%.
```

---

# 190. Performance Guardrail

No optimizar únicamente por intuición.

---

# 191. Performance Debt Evidence

Preferir:

```text
query count

latency

memory

CPU

payload size

production behavior
```

---

# 192. Observability Guardrail

No introducir:

```text
full distributed tracing stack
```

si el sistema todavía puede diagnosticarse adecuadamente con:

```text
structured logs

correlation IDs

metrics
```

---

# 193. Operations Guardrail

No convertir todo procedimiento manual en deuda automáticamente.

---

# 194. Automation Debt Trigger

La automatización se justifica cuando el proceso manual es:

```text
error-prone

frequent

slow

security-sensitive

release-critical
```

---

# 195. Documentation Guardrail

No documentar cada implementación interna.

---

# 196. Documentation Debt Trigger

Existe cuando la falta de documentación:

```text
creates repeated uncertainty

or

makes critical operation unsafe.
```

---

# 197. Debt Budget

El proyecto puede tolerar una cantidad limitada de deuda.

---

# 198. Debt Budget Concept

No se trata de:

```text
number of debt entries
```

sino de:

```text
aggregate risk and engineering drag.
```

---

# 199. Healthy Debt Profile

Puede contener:

```text
several S2/S3 accepted items

few S1 items with owners

zero unmanaged S0 items
```

---

# 200. Unhealthy Debt Profile

```text
multiple S1 without owner

S0 accepted indefinitely

same workaround repeated everywhere

critical areas without tests

release safety dependent on tribal knowledge
```

---

# 201. Debt Review Cadence

Debe revisarse:

```text
periodically

and

at architectural milestones.
```

---

# 202. Recommended Review Events

```text
before major release

before 1.0

before major module expansion

after production incident

after security review

after architecture review
```

---

# 203. Weekly Review

No es necesario revisar todas las entries cada semana.

---

# 204. Weekly Focus

Revisar principalmente:

```text
P0

P1

IN_PROGRESS

BLOCKED
```

---

# 205. Release Review

Antes de cada release revisar:

```text
S0

S1

security debt

migration debt

operational debt
```

---

# 206. Architecture Review

Debe comprobar:

```text
Is debt interest increasing?

Are workarounds spreading?

Has an accepted assumption stopped being true?
```

---

# 207. Debt Aging

La antigüedad por sí sola no determina prioridad.

---

# 208. Important

Una deuda S3 antigua puede seguir siendo menos importante que una S1 reciente.

---

# 209. Aging Signal

Pero una deuda aceptada durante mucho tiempo debe revisarse para comprobar:

```text
whether its original rationale is still valid.
```

---

# 210. Accepted Debt Review

Cada review puede resultar en:

```text
remain ACCEPTED

become PRIORITIZED

become CLOSED_NOT_DEBT

become SUPERSEDED
```

---

# 211. Debt Escalation

Una deuda puede subir de:

```text
S2 → S1
```

si cambia el contexto.

---

# 212. Example

Un sistema de autorización simple puede ser aceptable con:

```text
single-user project ownership
```

pero volverse crítico al introducir:

```text
multi-user collaboration.
```

---

# 213. Debt De-escalation

También puede reducirse si:

```text
feature is removed

usage changes

architecture evolves
```

---

# 214. Debt Closure

No cerrar porque:

```text
we no longer want to think about it.
```

---

# 215. Valid Closure

Debe existir:

```text
evidence that the structural concern no longer applies.
```

---

# 216. Partial Remediation

Puede ocurrir que una deuda se reduzca sin desaparecer.

---

# 217. Option A

Mantener la misma entry y actualizar:

```text
scope

severity

remaining debt
```

---

# 218. Option B

Resolver la original y crear:

```text
new narrower debt entry
```

si mejora trazabilidad.

---

# 219. Preferred Approach

Usar Option B cuando el cambio sea arquitectónicamente significativo.

---

# 220. Example

```text
TD-002 fragmented realtime lifecycle
```

puede resolverse tras centralizar conexiones.

---

# 221. Remaining Concern

Si todavía falta:

```text
durable cross-process delivery
```

y ya es requisito real, crear una nueva entry específica.

---

# 222. Debt Resolution Quality

Resolver deuda no significa:

```text
rewrite everything.
```

---

# 223. Good Remediation

Debe ser:

```text
targeted

measurable

risk-reducing

maintainable
```

---

# 224. Refactor Scope

Evitar que deuda pequeña provoque:

```text
unbounded rewrite.
```

---

# 225. Boy Scout Rule

Deuda P3 puede resolverse oportunísticamente:

```text
when working safely in the same area.
```

---

# 226. Guardrail

No ampliar una tarea pequeña hasta convertirla en:

```text
hidden architecture project.
```

---

# 227. Debt and Feature Delivery

Al diseñar una nueva feature debe preguntarse:

```text
Does this feature increase existing debt?

Does existing debt make this feature unsafe?

Should debt be resolved first?
```

---

# 228. Example — Kanban

Antes de Live Kanban debe revisarse:

```text
Project authorization

Realtime contracts

Reconnect reconciliation

Multi-client testing
```

---

# 229. Why

Construir Live Kanban encima de deuda crítica de realtime:

```text
compounds the debt.
```

---

# 230. Debt Sequencing

Por tanto:

```text
foundational debt

before

dependent feature
```

cuando el riesgo lo justifique.

---

# 231. Security Debt Rule

Security debt debe recibir tratamiento especialmente estricto.

---

# 232. Security Debt Cannot Be Accepted Casually

Debe existir:

```text
explicit threat

scope

mitigation

review trigger
```

---

# 233. Security Compensating Controls

Si se aplaza, registrar:

```text
temporary mitigation
```

---

# 234. Example

```text
Project collaboration remains restricted while contextual authorization is incomplete.
```

---

# 235. Security Debt Trigger

Debe indicar cuándo la mitigación deja de ser suficiente.

---

# 236. Example

```text
Must be resolved before enabling cross-user project collaboration.
```

---

# 237. Data Debt Rule

Deuda que pueda afectar integridad debe incluir:

```text
data risk

migration impact

backup implications
```

---

# 238. Realtime Debt Rule

Debe considerar:

```text
delivery

ordering

duplication

authorization

disconnect

reconnect

convergence
```

---

# 239. Testing Debt Rule

Debe expresarse como:

```text
risk not protected by tests
```

---

# 240. Performance Debt Rule

Debe incluir evidencia o trigger medible cuando sea posible.

---

# 241. Observability Debt Rule

Debe explicar:

```text
what failure cannot currently be diagnosed reliably.
```

---

# 242. Operations Debt Rule

Debe explicar:

```text
what production/recovery action remains unsafe or manual.
```

---

# 243. Documentation Debt Rule

Debe explicar:

```text
what engineering knowledge is currently fragile.
```

---

# 244. Debt Register Ordering

Las entries activas deberían ordenarse preferentemente por:

```text
Priority

↓

Severity

↓

Identifier
```

---

# 245. Alternative

También puede mantenerse por ID y añadir una tabla resumen ordenada por prioridad.

---

# 246. Recommended Model

Utilizar:

```text
summary register

+

detailed entries
```

---

# 247. Summary Register Columns

```text
ID

Title

Category

Severity

Priority

Status

Owner

Trigger
```

---

# 248. Example

```markdown
| ID | Title | Category | Severity | Priority | Status | Owner |
|---|---|---|---|---|---|---|
| TD-001 | Project authorization is not centralized | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-002 | Realtime event contracts are fragmented | REALTIME | S1 | P1 | PRIORITIZED | Maintainer |
| TD-003 | Critical realtime workflows lack multi-client coverage | TESTING | S1 | P1 | PRIORITIZED | Maintainer |
```

---

# 249. Summary Purpose

Permite detectar rápidamente:

```text
where debt risk is concentrated.
```

---

# 250. Debt Metrics

Pueden utilizarse métricas ligeras.

---

# 251. Useful Metrics

```text
active debt by severity

active debt by category

P0/P1 count

S1 aging

resolved debt per release
```

---

# 252. Avoid Vanity Metrics

No utilizar como objetivo:

```text
zero debt entries.
```

---

# 253. Why

Un registro vacío puede significar:

```text
perfect architecture

or

poor visibility.
```

---

# 254. Better Goal

```text
zero unmanaged critical debt.
```

---

# 255. Debt Trend

Es más útil observar:

```text
risk trend
```

que:

```text
raw count.
```

---

# 256. Example

Pasar de:

```text
4 S1 + 3 S2
```

a:

```text
1 S1 + 8 S2
```

puede representar una mejora aunque aumente el número total.

---

# 257. Debt Discovery

Debe ser normal registrar deuda durante:

```text
code review

architecture review

security review

testing

incident analysis

feature implementation

performance profiling
```

---

# 258. Discovery Is Positive

Encontrar deuda no debe interpretarse automáticamente como:

```text
project quality getting worse.
```

---

# 259. Better Interpretation

Puede significar:

```text
engineering visibility is improving.
```

---

# 260. Debt Creation During Delivery

Si una implementación introduce deuda intencionada:

```text
record it close to the decision.
```

---

# 261. Example

```text
Temporary synchronous notification fan-out accepted for first production release.
```

---

# 262. Why Record Immediately

Porque meses después puede parecer:

```text
accidental architecture.
```

---

# 263. Debt Commenting

No es necesario llenar el código de:

```text
TODO technical debt
```

si existe registro estructurado.

---

# 264. Code TODO

Debe reservarse para:

```text
local implementation follow-up
```

---

# 265. Cross-cutting Debt

Debe registrarse aquí.

---

# 266. TODO Reference

Cuando sea útil:

```python
# TODO(TD-XXX): ...
```

puede enlazar con el registro.

---

# 267. Guardrail

No crear TODO sin:

```text
context

or

owner
```

para problemas importantes.

---

# 268. Debt and Changelog

El Changelog registra:

```text
debt repayment outcome
```

---

# 269. Example

Technical Debt:

```text
TD-002 — Realtime event contracts are fragmented.
```

---

# 270. Changelog after Resolution

```markdown
### Changed

- Standardized realtime event contracts across collaborative modules.
```

---

# 271. Debt and ADR

Si resolver deuda requiere decisión arquitectónica importante:

```text
Technical Debt

↓

ADR

↓

Implementation

↓

Changelog
```

---

# 272. Debt and Known Issues

Si deuda produce defecto visible:

```text
Technical Debt

↓

Known Issue
```

---

# 273. Debt and Current Tasks

Cuando se prioriza:

```text
Technical Debt

↓

Current Task
```

---

# 274. Debt and Product Roadmap

Solo deuda estructural estratégica debería influir directamente en roadmap.

---

# 275. Example

Antes de:

```text
Live Kanban
```

puede existir milestone de:

```text
Realtime Reliability
```

---

# 276. Roadmap Should Not Become Debt List

No trasladar todas las TD al roadmap.

---

# 277. Debt and Weekly Update

El Weekly Update puede mencionar:

```text
debt resolved

debt escalated

major debt discovered
```

cuando sea relevante.

---

# 278. Debt Governance

El objetivo no es evitar toda deuda.

---

# 279. Governance Objective

Es garantizar que:

```text
debt is intentional when accepted

visible when discovered

prioritized by risk

and

resolved before it becomes structural failure.
```

---

# 280. Part 1 Summary

Esta primera parte establece:

```text
Technical Debt definition

Scope

Debt vs Known Issues

Debt vs Current Tasks

Debt vs ADRs

Categories

Stable identifiers

Statuses

Severity

Priority

Risk model

Debt interest

Triggers

Ownership

Entry templates

Architecture guardrails

Security debt

Realtime debt

Testing debt

Performance debt

Observability debt

Operations debt

Debt register

Metrics

Lifecycle

Governance
```

---

# 281. Continuation

La **Parte 2/3** desarrolla el registro técnico detallado y profesional de deuda de Aula Robótica Platform, incluyendo:

```text
Security and Authorization Debt

Project Membership

Nested-resource Authorization

CSRF

Session and Refresh-token Hardening

WebSocket Authentication

Realtime Subscription Authorization

Realtime Event Contracts

Reconnect and Reconciliation

Event Idempotency

Multi-client Testing

SSR Context Duplication

Database Constraints

Pagination

Query Efficiency

Attachment Storage

Backup and Restore

Structured Logging

Correlation

Metrics

Health Checks

Deployment

Frontend Consistency

Accessibility

Testing Architecture

Documentation and Operational Debt
```

---

# 56_TECHNICAL_DEBT.md

# Aula Robótica Platform — Technical Debt

## Parte 2/3 — Registro técnico detallado: seguridad, autorización, realtime, testing, persistencia, rendimiento, frontend, observabilidad y operaciones

---

# 282. Active Technical Debt Register

El siguiente registro representa las principales áreas de deuda técnica estructural que deben vigilarse durante la evolución de Aula Robótica Platform.

---

# 283. Register Interpretation

Las entries siguientes deben entenderse como:

```text
engineering concerns

↓

to validate against implementation

↓

prioritize when confirmed

↓

resolve before dependent capabilities amplify them
```

---

# 284. Important Accuracy Rule

Una entry no debe mantenerse como deuda confirmada si la implementación actual demuestra que:

```text
the structural concern no longer exists.
```

---

# 285. Recommended Initial Register

| ID | Title | Category | Severity | Priority | Status | Owner |
|---|---|---|---|---|---|---|
| TD-001 | Project-scoped authorization is not fully centralized | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-002 | Explicit Project Membership is not yet the canonical collaboration boundary | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-003 | Nested-resource authorization requires systematic consolidation | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-004 | CSRF protection requires explicit hardening across authenticated mutations | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-005 | Browser session and refresh-token lifecycle requires further hardening | SECURITY | S1 | P1 | ACCEPTED | Maintainer |
| TD-006 | WebSocket authentication and subscription authorization require consolidation | SECURITY | S1 | P1 | PRIORITIZED | Maintainer |
| TD-007 | Realtime event contracts are fragmented | REALTIME | S1 | P1 | PRIORITIZED | Maintainer |
| TD-008 | Realtime reconnect does not yet guarantee authoritative state reconciliation | REALTIME | S1 | P1 | PRIORITIZED | Maintainer |
| TD-009 | Realtime duplicate and ordering semantics are not fully standardized | REALTIME | S2 | P2 | ACCEPTED | Maintainer |
| TD-010 | Critical realtime behavior lacks complete multi-client regression coverage | TESTING | S1 | P1 | PRIORITIZED | Maintainer |
| TD-011 | Critical browser journeys lack systematic UI regression coverage | TESTING | S2 | P1 | ACCEPTED | Maintainer |
| TD-012 | SSR request context assembly contains opportunities for consolidation | ARCHITECTURE | S2 | P2 | ACCEPTED | Maintainer |
| TD-013 | Selected relational invariants require stronger database enforcement | DATABASE | S2 | P2 | ACCEPTED | Maintainer |
| TD-014 | Selected list and history views require bounded pagination | PERFORMANCE | S2 | P2 | ACCEPTED | Maintainer |
| TD-015 | Selected SSR views require query-count validation and optimization | PERFORMANCE | S2 | P2 | ACCEPTED | Maintainer |
| TD-016 | Attachment storage remains coupled to the current storage implementation | ARCHITECTURE | S2 | P2 | ACCEPTED | Maintainer |
| TD-017 | Backup coverage requires systematic restore validation | OPERATIONS | S1 | P1 | ACCEPTED | Maintainer |
| TD-018 | Application logging requires stronger structured context and correlation | OBSERVABILITY | S2 | P2 | ACCEPTED | Maintainer |
| TD-019 | Realtime operational metrics remain incomplete | OBSERVABILITY | S2 | P2 | ACCEPTED | Maintainer |
| TD-020 | Health semantics require explicit liveness and readiness separation | OPERATIONS | S2 | P2 | ACCEPTED | Maintainer |
| TD-021 | Frontend async interaction states are not fully standardized | FRONTEND | S2 | P2 | ACCEPTED | Maintainer |
| TD-022 | Accessibility regression coverage remains incomplete | TESTING | S2 | P2 | ACCEPTED | Maintainer |
| TD-023 | Release readiness still depends partly on manual governance | OPERATIONS | S2 | P2 | ACCEPTED | Maintainer |
| TD-024 | Critical operational procedures require executable validation | DOCUMENTATION | S2 | P2 | ACCEPTED | Maintainer |

---

# 286. Register Status Warning

La tabla anterior debe actualizarse cuando:

```text
implementation evidence

tests

security review

architecture review
```

demuestren un estado diferente.

---

# 287. Security Debt Cluster

El principal cluster de deuda estructural se concentra inicialmente en:

```text
Project access boundaries

Nested authorization

CSRF

Session lifecycle

Realtime authorization
```

---

# 288. Why Security Comes First

Estas foundations afectan directamente a futuras capabilities como:

```text
multi-user Projects

Live Kanban

shared Tasks

shared Activities

Attachments

Notifications

Activity Feed

realtime collaboration
```

---

# 289. TD-001 — Project-scoped Authorization Is Not Fully Centralized

**Status:** PRIORITIZED  
**Category:** SECURITY  
**Related Areas:** ARCHITECTURE, BACKEND, REALTIME  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Incremental collaboration growth  
**Review:** Before expanding multi-user collaboration

---

# 290. TD-001 Context

La plataforma dispone de autorización global mediante:

```text
Users

Roles

Permissions
```

pero la colaboración introduce una segunda dimensión:

```text
Can this actor access this specific Project?
```

---

# 291. TD-001 Current Compromise

Parte de la autorización contextual puede depender todavía de:

```text
resource ownership

local service checks

route-level conditions

template visibility

resource relationships
```

sin una política contextual única.

---

# 292. TD-001 Risk

A medida que aumentan los recursos:

```text
Project

Task

Activity

Attachment

Notification

Feed event

WebSocket subscription
```

la duplicación de reglas puede producir inconsistencias.

---

# 293. TD-001 Debt Interest

Cada nueva capability project-scoped puede añadir:

```text
another authorization implementation

another negative-path matrix

another opportunity for divergence
```

---

# 294. TD-001 Remediation Direction

Introducir una capa explícita de:

```text
contextual authorization policies
```

capaz de responder consistentemente:

```text
can_view_project()

can_modify_project()

can_create_task()

can_modify_task()

can_access_activity()

can_access_attachment()

can_subscribe_project()
```

---

# 295. TD-001 Acceptance Criteria

- [ ] Las reglas project-scoped tienen una fuente canónica.
- [ ] Routers no reconstruyen políticas complejas manualmente.
- [ ] Services reutilizan las mismas reglas.
- [ ] Templates reciben capabilities calculadas server-side.
- [ ] Realtime subscriptions reutilizan la misma boundary.
- [ ] Existen tests negativos cross-project.
- [ ] No se confía en visibilidad UI como control de seguridad.

---

# 296. TD-001 Trigger

```text
Must be resolved before broad multi-user Project collaboration becomes a supported core capability.
```

---

# 297. TD-002 — Explicit Project Membership Is Not Yet the Canonical Collaboration Boundary

**Status:** PRIORITIZED  
**Category:** SECURITY  
**Related Areas:** DATABASE, ARCHITECTURE  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Initial simpler Project access model  
**Review:** Before collaborative authorization hardening

---

# 298. TD-002 Context

La autorización contextual necesita representar explícitamente:

```text
which users belong to which Projects

and

what contextual role/capabilities they have.
```

---

# 299. TD-002 Current Compromise

Sin una relación canónica de membership, las reglas pueden inferirse indirectamente desde:

```text
ownership

assignment

global permissions

resource relationships
```

---

# 300. TD-002 Consequence

La inferencia indirecta dificulta responder con precisión:

```text
Who can see this Project?

Who can modify it?

Who can receive its realtime events?

Who can access nested resources?
```

---

# 301. TD-002 Remediation Direction

Introducir explícitamente:

```text
ProjectMembership
```

con invariantes como:

```text
project_id

user_id

contextual role / membership type

active state if required

timestamps if useful
```

---

# 302. TD-002 Database Invariant

Debe existir una constraint equivalente conceptualmente a:

```text
UNIQUE(project_id, user_id)
```

---

# 303. TD-002 Migration Concern

Existing Projects necesitarán:

```text
membership backfill
```

antes de activar políticas que dependan exclusivamente de la nueva relación.

---

# 304. TD-002 Acceptance Criteria

- [ ] Membership tiene representación persistente explícita.
- [ ] Existe unicidad Project/User.
- [ ] Existing data tiene migration/backfill definido.
- [ ] Project access utiliza membership como boundary canónica.
- [ ] Nested resources heredan Project scope.
- [ ] Realtime recipient selection utiliza membership.
- [ ] Tests cubren members y non-members.

---

# 305. TD-002 Trigger

```text
Before contextual authorization becomes authoritative.
```

---

# 306. TD-003 — Nested-resource Authorization Requires Systematic Consolidation

**Status:** PRIORITIZED  
**Category:** SECURITY  
**Related Areas:** BACKEND, TESTING  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Incremental domain expansion  
**Review:** Security hardening cycle

---

# 307. TD-003 Scope

Afecta especialmente:

```text
Project
  └── Task
       └── Activity

Project / Task / Activity
  └── Attachment
```

---

# 308. TD-003 Threat

Un actor podría intentar acceder a:

```text
/task/{id}

/activity/{id}

/attachment/{id}
```

directamente, evitando navegar desde el Project legítimo.

---

# 309. TD-003 Core Principle

```text
Knowing a resource identifier
must never imply authorization.
```

---

# 310. TD-003 Current Risk

Si cada endpoint comprueba únicamente:

```text
resource exists
```

sin validar su contexto superior, puede producirse:

```text
IDOR / BOLA-style authorization failure
```

---

# 311. TD-003 Remediation Direction

Resolver siempre:

```text
resource

↓

owning Project

↓

actor membership / capability

↓

requested operation
```

---

# 312. TD-003 Attachment Rule

Para Attachment:

```text
attachment

↓

parent resource

↓

Project

↓

authorization
```

---

# 313. TD-003 Acceptance Criteria

- [ ] Task access valida Project scope.
- [ ] Activity access valida Project scope.
- [ ] Attachment access valida parent scope.
- [ ] Mutation y read paths comparten políticas.
- [ ] Cross-project identifier tests existen.
- [ ] Unauthorized access no filtra información sensible.
- [ ] Realtime events respetan la misma scope hierarchy.

---

# 314. TD-003 Trigger

```text
Before external or broader collaborative access.
```

---

# 315. TD-004 — CSRF Protection Requires Explicit Hardening Across Authenticated Mutations

**Status:** PRIORITIZED  
**Category:** SECURITY  
**Related Areas:** FRONTEND, BACKEND, TESTING  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Cookie-authenticated SSR architecture  
**Review:** Security hardening cycle

---

# 316. TD-004 Context

La arquitectura browser-facing utiliza autenticación asociada a:

```text
cookies

SSR forms

Fetch mutations
```

---

# 317. TD-004 Security Principle

Cuando el navegador envía automáticamente credenciales mediante cookies:

```text
authenticated

does not imply

CSRF-safe.
```

---

# 318. TD-004 Scope

Debe revisarse:

```text
POST

PUT

PATCH

DELETE
```

y cualquier operación state-changing equivalente.

---

# 319. TD-004 Remediation Direction

Establecer una estrategia uniforme como:

```text
CSRF token

+

server validation

+

same-site cookie policy

+

Origin / Referer validation where appropriate
```

---

# 320. TD-004 Frontend Integration

La protección debe cubrir tanto:

```text
HTML forms
```

como:

```text
JavaScript Fetch requests.
```

---

# 321. TD-004 Acceptance Criteria

- [ ] Todas las browser mutations relevantes están protegidas.
- [ ] Formularios SSR incluyen mecanismo CSRF.
- [ ] Fetch mutations transmiten el token correctamente.
- [ ] Server rechaza tokens ausentes o inválidos.
- [ ] SameSite está configurado deliberadamente.
- [ ] Existen tests positivos y negativos.
- [ ] SAML/authentication flows compatibles están validados.

---

# 322. TD-004 Trigger

```text
Before production-grade browser security is considered complete.
```

---

# 323. TD-005 — Browser Session and Refresh-token Lifecycle Requires Further Hardening

**Status:** ACCEPTED  
**Category:** SECURITY  
**Related Areas:** BACKEND, DATABASE  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Incremental IAM evolution  
**Review:** Before production security baseline

---

# 324. TD-005 Scope

Debe evaluarse explícitamente:

```text
access token lifetime

refresh token lifetime

rotation

revocation

logout

reuse detection

session invalidation

concurrent sessions
```

---

# 325. TD-005 Risk

Un refresh token comprometido puede tener un impacto mayor que un access token de corta duración.

---

# 326. TD-005 Remediation Direction

Evaluar un modelo de:

```text
short-lived access token

+

rotating refresh token

+

server-side session state

+

revocation

+

reuse handling
```

según necesidades reales.

---

# 327. TD-005 Guardrail

No añadir complejidad criptográfica o session infrastructure sin:

```text
clear threat model

and

tested lifecycle.
```

---

# 328. TD-005 Acceptance Criteria

- [ ] Lifetimes explícitos.
- [ ] Logout invalida el estado esperado.
- [ ] Refresh rotation definida o justificada.
- [ ] Revocation strategy definida.
- [ ] Reuse behavior definido.
- [ ] Cookie flags seguros.
- [ ] Session expiry tests existentes.
- [ ] Documentation sincronizada.

---

# 329. TD-006 — WebSocket Authentication and Subscription Authorization Require Consolidation

**Status:** PRIORITIZED  
**Category:** SECURITY  
**Related Areas:** REALTIME, TESTING  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Realtime capability growth  
**Review:** Before Live Kanban

---

# 330. TD-006 Context

Realtime añade una nueva boundary distinta de HTTP.

---

# 331. TD-006 Core Requirement

El servidor debe determinar:

```text
who is connected

and

what channels/resources that actor may receive.
```

---

# 332. TD-006 Security Rule

No confiar en identidad proporcionada por el cliente como:

```text
user_id query parameter

project_id without authorization

claimed role

claimed permission
```

---

# 333. TD-006 Authentication Direction

La identidad debe derivarse de:

```text
server-validated authentication context.
```

---

# 334. TD-006 Subscription Direction

Cada subscription debe validar:

```text
actor

+

requested scope

+

current authorization.
```

---

# 335. TD-006 Recipient Scopes

Conceptualmente:

```text
USER

PROJECT

ADMIN / PRIVILEGED
```

cuando sean necesarios.

---

# 336. TD-006 Acceptance Criteria

- [ ] WebSocket identity es server-derived.
- [ ] Invalid authentication rechaza conexión.
- [ ] Project subscription requiere Project access.
- [ ] Revoked access deja de permitir nuevas subscriptions.
- [ ] Sensitive admin streams requieren permiso explícito.
- [ ] No existe cross-project event leakage.
- [ ] Multi-client security tests cubren isolation.

---

# 337. TD-006 Trigger

```text
Before project-wide realtime collaboration is expanded.
```

---

# 338. Realtime Debt Cluster

El segundo cluster prioritario afecta:

```text
event contracts

reconnect

reconciliation

duplicates

ordering

testing
```

---

# 339. TD-007 — Realtime Event Contracts Are Fragmented

**Status:** PRIORITIZED  
**Category:** REALTIME  
**Related Areas:** ARCHITECTURE, FRONTEND  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Incremental realtime modules  
**Review:** Realtime consolidation cycle

---

# 340. TD-007 Context

Distintos módulos realtime pueden evolucionar con payloads y handlers independientes.

---

# 341. TD-007 Debt

Sin contrato común aumenta el riesgo de:

```text
different event shapes

different naming

different parsing

different error behavior

different compatibility assumptions
```

---

# 342. TD-007 Remediation Direction

Introducir un envelope versionado equivalente conceptualmente a:

```json
{
  "type": "task.updated",
  "version": 1,
  "scope": {
    "type": "project",
    "id": "..."
  },
  "resource": {
    "type": "task",
    "id": "..."
  },
  "event_id": "...",
  "occurred_at": "...",
  "payload": {}
}
```

---

# 343. TD-007 Contract Principle

El envelope debe separar:

```text
event metadata

from

domain payload.
```

---

# 344. TD-007 Event Naming

Preferir nombres semánticos:

```text
notification.created

task.updated

activity.created

attachment.deleted
```

---

# 345. TD-007 Avoid

No basar contrato público únicamente en:

```text
Python class names

database table names

JavaScript handler names.
```

---

# 346. TD-007 Versioning

El contrato debe poder evolucionar sin:

```text
silent consumer breakage.
```

---

# 347. TD-007 Acceptance Criteria

- [ ] Existe envelope canónico.
- [ ] Existe naming convention.
- [ ] Event version está definida.
- [ ] Scope está explícito cuando aplica.
- [ ] Event ID está disponible cuando se necesita deduplicación.
- [ ] Consumers utilizan dispatcher común.
- [ ] Unknown event behavior está definido.
- [ ] Contract tests existen.

---

# 348. TD-008 — Realtime Reconnect Does Not Yet Guarantee Authoritative State Reconciliation

**Status:** PRIORITIZED  
**Category:** REALTIME  
**Related Areas:** FRONTEND, TESTING  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Initial push-oriented realtime design  
**Review:** Before Live Kanban

---

# 349. TD-008 Fundamental Problem

WebSocket delivery puede interrumpirse.

---

# 350. Failure Window

```text
connected

↓

disconnect

↓

server state changes

↓

reconnect
```

---

# 351. TD-008 Risk

El cliente puede haber perdido eventos durante la desconexión.

---

# 352. Critical Principle

```text
Reconnect does not prove state convergence.
```

---

# 353. TD-008 Wrong Assumption

No asumir:

```text
socket reconnected

→ UI is current.
```

---

# 354. TD-008 Remediation Direction

Después de reconnect:

```text
re-establish authorization

↓

re-establish subscriptions

↓

fetch authoritative state

↓

reconcile local UI

↓

resume event processing
```

---

# 355. Reconciliation Options

Según módulo:

```text
full resource refresh

bounded collection refresh

version comparison

cursor-based replay
```

---

# 356. Current Simplicity Preference

Para el estado actual, preferir:

```text
authoritative HTTP refresh
```

antes de introducir sistemas complejos de event replay si no son necesarios.

---

# 357. TD-008 Acceptance Criteria

- [ ] Reconnect utiliza backoff acotado.
- [ ] Subscription state se restablece.
- [ ] Authoritative state se recupera.
- [ ] Missed events no dejan UI stale permanentemente.
- [ ] Repeated reconnect no duplica handlers.
- [ ] Multi-client tests cubren missed-event windows.

---

# 358. TD-009 — Realtime Duplicate and Ordering Semantics Are Not Fully Standardized

**Status:** ACCEPTED  
**Category:** REALTIME  
**Related Areas:** FRONTEND, BACKEND  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Initial realtime implementation  
**Review:** Before high-frequency collaborative interactions

---

# 359. TD-009 Context

Distributed delivery puede producir:

```text
duplicate messages

out-of-order observations

retries

rapid consecutive updates
```

---

# 360. TD-009 Guardrail

No es necesario resolver ordering global si el producto no lo requiere.

---

# 361. Required Question

Por cada event type:

```text
Does order matter?

Can it be duplicated?

Can latest authoritative state replace event replay?
```

---

# 362. TD-009 Preferred Strategy

Cuando sea posible:

```text
events notify

authoritative state decides.
```

---

# 363. Idempotency

Consumers deben tolerar eventos repetidos cuando sea razonable.

---

# 364. TD-009 Event ID

Un:

```text
event_id
```

puede permitir deduplicación bounded.

---

# 365. TD-009 Acceptance Criteria

- [ ] Event types tienen semántica de ordering documentada.
- [ ] Duplicate handling definido.
- [ ] Critical mutations son idempotent cuando corresponde.
- [ ] UI no duplica visualmente recursos por event replay.
- [ ] Tests cubren duplicate delivery relevante.

---

# 366. TD-010 — Critical Realtime Behavior Lacks Complete Multi-client Regression Coverage

**Status:** PRIORITIZED  
**Category:** TESTING  
**Related Areas:** REALTIME, SECURITY  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Testing maturity gap  
**Review:** Before Live Kanban

---

# 367. TD-010 Risk

Realtime no puede validarse adecuadamente solo con:

```text
single client

single request

single WebSocket
```

---

# 368. Required Scenarios

La suite debe cubrir:

```text
Client A mutates

↓

Server persists

↓

Server publishes

↓

Client B receives

↓

Client B converges
```

---

# 369. Security Scenarios

También:

```text
authorized client receives

unauthorized client does not receive
```

---

# 370. Lifecycle Scenarios

```text
disconnect

reconnect

missed events

duplicate delivery

multiple subscriptions

client closure
```

---

# 371. TD-010 Acceptance Criteria

- [ ] Dos clientes autorizados convergen.
- [ ] Cliente no autorizado queda aislado.
- [ ] Reconnect está cubierto.
- [ ] Missed-event reconciliation está cubierta.
- [ ] Duplicate event handling está cubierto.
- [ ] Connection cleanup está cubierto.
- [ ] Tests son deterministas.

---

# 372. TD-011 — Critical Browser Journeys Lack Systematic UI Regression Coverage

**Status:** ACCEPTED  
**Category:** TESTING  
**Related Areas:** FRONTEND, SECURITY  
**Severity:** S2  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Backend-first test maturity  
**Review:** Before production release baseline

---

# 373. TD-011 Critical Journeys

Como mínimo deben evaluarse:

```text
login

logout

navigation

Project access

Task mutation

Activity mutation

Attachment workflow

Notification interaction
```

---

# 374. Future Critical Journey

Cuando exista:

```text
Kanban status transition
```

debe añadirse.

---

# 375. UI Test Purpose

No probar:

```text
every Bootstrap class
```

---

# 376. Better Focus

Proteger:

```text
critical user behavior

permissions

browser integration

accessibility-sensitive interaction
```

---

# 377. TD-011 Acceptance Criteria

- [ ] Critical journey inventory definido.
- [ ] Browser test framework estable.
- [ ] Authentication journeys cubiertos.
- [ ] Permission-sensitive journeys cubiertos.
- [ ] Critical mutations cubiertas.
- [ ] Realtime UI journeys cubiertos cuando existan.
- [ ] Suite integrada en CI de forma sostenible.

---

# 378. Architecture and Backend Debt Cluster

El siguiente grupo afecta principalmente:

```text
SSR request composition

service boundaries

shared context

resource loading
```

---

# 379. TD-012 — SSR Request Context Assembly Contains Opportunities for Consolidation

**Status:** ACCEPTED  
**Category:** ARCHITECTURE  
**Related Areas:** BACKEND, PERFORMANCE  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Incremental SSR expansion  
**Review:** During SSR performance hardening

---

# 380. TD-012 Context

Las vistas SSR requieren contexto como:

```text
current user

permissions

navigation state

notification count

page-specific data
```

---

# 381. TD-012 Risk

Si cada route construye independientemente ese contexto puede aparecer:

```text
duplicated queries

duplicated authorization logic

inconsistent navigation state

higher maintenance cost
```

---

# 382. TD-012 Remediation Direction

Consolidar únicamente contexto realmente transversal mediante:

```text
request-scoped context

shared helpers

dependencies

template context builders
```

---

# 383. Guardrail

No crear:

```text
giant global context object
```

con todos los datos de la aplicación.

---

# 384. Principle

```text
Shared context should remain small,
stable,
and request-relevant.
```

---

# 385. TD-012 Acceptance Criteria

- [ ] Authentication context no se recalcula innecesariamente.
- [ ] Navigation permissions tienen fuente común.
- [ ] Notification summary evita consultas redundantes.
- [ ] Page-specific data permanece local.
- [ ] Query counts se validan antes/después.

---

# 386. Database and Performance Debt Cluster

La persistencia debe reforzarse donde las reglas del dominio puedan expresarse mejor mediante:

```text
constraints

indexes

bounded queries

explicit loading strategies
```

---

# 387. TD-013 — Selected Relational Invariants Require Stronger Database Enforcement

**Status:** ACCEPTED  
**Category:** DATABASE  
**Related Areas:** BACKEND, SECURITY  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Incremental schema evolution  
**Review:** During Project Membership migration

---

# 388. TD-013 Principle

Las invariantes críticas no deberían depender exclusivamente de:

```text
application code.
```

---

# 389. Candidate Invariants

Ejemplos a revisar:

```text
unique membership per Project/User

required ownership relationships

valid foreign keys

uniqueness of selected identity relationships
```

---

# 390. Database Role

La base de datos debe actuar como:

```text
last line of integrity enforcement.
```

---

# 391. TD-013 Acceptance Criteria

- [ ] Critical uniqueness rules identificadas.
- [ ] Foreign keys revisadas.
- [ ] Nullability revisada.
- [ ] Constraints coherentes con dominio.
- [ ] Migrations seguras.
- [ ] Integrity violations tienen manejo backend claro.

---

# 392. TD-014 — Selected List and History Views Require Bounded Pagination

**Status:** ACCEPTED  
**Category:** PERFORMANCE  
**Related Areas:** DATABASE, FRONTEND  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Small-data initial implementation  
**Review:** Before production data growth

---

# 393. TD-014 Candidate Views

Especialmente:

```text
Notifications

Audit

Activity Feed

large Task lists

large Activity lists
```

---

# 394. TD-014 Risk

Unbounded retrieval aumenta:

```text
query time

memory

HTML size

browser work

response latency
```

---

# 395. TD-014 Remediation Direction

Aplicar:

```text
bounded page size

stable ordering

appropriate indexes

navigation/cursor strategy
```

---

# 396. Offset vs Cursor

No introducir cursor pagination automáticamente.

---

# 397. Selection Rule

```text
Use the simplest pagination
that satisfies consistency and scale requirements.
```

---

# 398. TD-014 Acceptance Criteria

- [ ] High-growth lists tienen límites.
- [ ] Ordering determinista.
- [ ] Page sizes razonables.
- [ ] Queries indexables.
- [ ] UI conserva usabilidad.
- [ ] Realtime interaction con listas paginadas está definida.

---

# 399. TD-015 — Selected SSR Views Require Query-count Validation and Optimization

**Status:** ACCEPTED  
**Category:** PERFORMANCE  
**Related Areas:** DATABASE, BACKEND  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Domain relationship growth  
**Review:** Performance hardening cycle

---

# 400. TD-015 Candidate Views

```text
Dashboard

Project detail

Task detail

Activity detail

Audit history
```

---

# 401. TD-015 Risk

Relationship growth puede introducir:

```text
N+1 queries

duplicate loading

repeated count queries

unnecessary eager loading
```

---

# 402. TD-015 Evidence Rule

No optimizar sin medir.

---

# 403. Recommended Measurements

```text
query count

response latency

rows loaded

payload/HTML size
```

---

# 404. TD-015 Remediation Options

Según evidencia:

```text
selectin loading

joined loading

explicit aggregate queries

request context reuse

bounded collections
```

---

# 405. Guardrail

No convertir cada view en:

```text
one giant SQL query
```

por perseguir un número artificialmente bajo de queries.

---

# 406. TD-015 Acceptance Criteria

- [ ] Critical SSR views tienen baseline.
- [ ] N+1 patterns eliminados cuando existen.
- [ ] Relationship loading es explícito.
- [ ] Query count permanece bounded con dataset de referencia.
- [ ] Optimización tiene test o benchmark reproducible.

---

# 407. Attachment Storage Debt Cluster

Attachments añaden un boundary operacional diferente de la base de datos.

---

# 408. TD-016 — Attachment Storage Remains Coupled to the Current Storage Implementation

**Status:** ACCEPTED  
**Category:** ARCHITECTURE  
**Related Areas:** OPERATIONS, BACKEND  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Simple initial storage design  
**Review:** Before requiring multiple application instances or external object storage

---

# 409. TD-016 Current Compromise

La implementación inicial puede depender directamente de:

```text
local/persistent filesystem behavior.
```

---

# 410. Current Acceptability

Esto puede ser perfectamente válido para:

```text
single deployment

small installation

simple operational model.
```

---

# 411. Debt Trigger

Se convierte en limitación relevante cuando se necesite:

```text
multiple application instances

independent storage scaling

object storage

distributed deployment

external retention policy
```

---

# 412. TD-016 Remediation Direction

Introducir una abstracción mínima:

```text
AttachmentStorage
```

con operaciones conceptuales:

```text
save

open/read

delete

exists
```

---

# 413. Guardrail

No implementar:

```text
S3

MinIO

Azure Blob

GCS
```

sin requisito.

---

# 414. TD-016 Acceptance Criteria

- [ ] Domain/service logic no depende de path físico específico.
- [ ] Storage backend puede sustituirse sin reescribir autorización.
- [ ] Metadata permanece separada del binary storage.
- [ ] Delete semantics están definidas.
- [ ] Backup semantics están definidas.

---

# 415. Operations and Recovery Debt Cluster

Una plataforma production-ready necesita demostrar no solo:

```text
backup exists
```

sino:

```text
restore works.
```

---

# 416. TD-017 — Backup Coverage Requires Systematic Restore Validation

**Status:** ACCEPTED  
**Category:** OPERATIONS  
**Related Areas:** DATABASE, DOCUMENTATION  
**Severity:** S1  
**Priority:** P1  
**Owner:** Maintainer  
**Origin:** Operational maturity gap  
**Review:** Before production readiness

---

# 417. TD-017 Scope

Debe considerar conjuntamente:

```text
PostgreSQL data

Attachment binaries

required configuration references
```

---

# 418. Backup Principle

```text
An untested backup is only a hypothesis.
```

---

# 419. TD-017 Risk

Posibles fallos:

```text
backup incomplete

attachment/database mismatch

restore procedure outdated

credentials unavailable

recovery time unknown
```

---

# 420. TD-017 Remediation Direction

Establecer:

```text
scheduled backups

retention

restore procedure

restore validation

recovery evidence
```

---

# 421. Data Consistency

Debe considerarse consistencia entre:

```text
Attachment metadata

and

binary storage.
```

---

# 422. TD-017 Acceptance Criteria

- [ ] Database backup automatizado.
- [ ] Attachment storage incluido.
- [ ] Retention definida.
- [ ] Restore probado.
- [ ] Restored application arranca.
- [ ] Critical data verificada.
- [ ] Recovery procedure documentado.
- [ ] Restore validation se repite periódicamente.

---

# 423. Observability Debt Cluster

La plataforma debe poder responder:

```text
What failed?

Where?

For whom?

During which request/event?

How often?
```

---

# 424. TD-018 — Application Logging Requires Stronger Structured Context and Correlation

**Status:** ACCEPTED  
**Category:** OBSERVABILITY  
**Related Areas:** BACKEND, REALTIME  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Operational maturity growth  
**Review:** Observability hardening cycle

---

# 425. TD-018 Current Risk

Logs sin contexto consistente dificultan correlacionar:

```text
request

actor

resource

mutation

realtime publication

failure
```

---

# 426. TD-018 Remediation Direction

Estandarizar campos como:

```text
timestamp

level

logger

request_id

event_id

actor_id where appropriate

resource_type

resource_id

operation

outcome
```

---

# 427. Sensitive-data Rule

Nunca registrar indiscriminadamente:

```text
passwords

tokens

session secrets

SAML assertions

sensitive file contents
```

---

# 428. Correlation Flow

Idealmente:

```text
HTTP request_id

↓

domain operation

↓

audit event

↓

realtime event_id

↓

delivery log
```

---

# 429. TD-018 Acceptance Criteria

- [ ] Request correlation ID disponible.
- [ ] Structured fields consistentes.
- [ ] Error logs contienen diagnostic context.
- [ ] Sensitive values están filtrados.
- [ ] Realtime publication puede correlacionarse.
- [ ] Logging policy está documentada.

---

# 430. TD-019 — Realtime Operational Metrics Remain Incomplete

**Status:** ACCEPTED  
**Category:** OBSERVABILITY  
**Related Areas:** REALTIME, OPERATIONS  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Initial functionality-first realtime implementation  
**Review:** Before realtime becomes critical workflow infrastructure

---

# 431. TD-019 Candidate Metrics

```text
active WebSocket connections

connection attempts

authentication failures

subscription failures

messages published

delivery failures

disconnects

reconnects

reconciliation failures
```

---

# 432. Metric Cardinality Guardrail

No utilizar labels de alta cardinalidad como:

```text
user_id

resource_id

event_id
```

en métricas agregadas.

---

# 433. Logs vs Metrics

```text
Metrics

→ how often / how much


Logs

→ what happened specifically
```

---

# 434. TD-019 Acceptance Criteria

- [ ] Connection count observable.
- [ ] Authentication failures observable.
- [ ] Subscription failures observable.
- [ ] Delivery failures observable.
- [ ] Reconnect behavior observable.
- [ ] Metrics tienen cardinalidad controlada.
- [ ] Alerting se basa únicamente en señales accionables.

---

# 435. TD-020 — Health Semantics Require Explicit Liveness and Readiness Separation

**Status:** ACCEPTED  
**Category:** OPERATIONS  
**Related Areas:** OBSERVABILITY  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Deployment maturity growth  
**Review:** Before orchestrated production deployment

---

# 436. TD-020 Problem

Un único endpoint:

```text
/health
```

puede mezclar dos preguntas distintas.

---

# 437. Liveness

```text
Is the application process alive?
```

---

# 438. Readiness

```text
Can the application safely serve traffic?
```

---

# 439. Readiness Dependencies

Puede considerar:

```text
database connectivity

required storage availability

critical initialization
```

---

# 440. Guardrail

Liveness no debe fallar simplemente porque una dependency temporal esté caída si reiniciar el proceso no resolvería el problema.

---

# 441. TD-020 Acceptance Criteria

- [ ] Liveness semantics definidas.
- [ ] Readiness semantics definidas.
- [ ] Critical dependencies clasificadas.
- [ ] Checks son bounded.
- [ ] No exponen información sensible.
- [ ] Deployment utiliza el check correcto.

---

# 442. Frontend Debt Cluster

La UI SSR-first debe mantener consistencia a medida que crece la capa de progressive enhancement.

---

# 443. TD-021 — Frontend Async Interaction States Are Not Fully Standardized

**Status:** ACCEPTED  
**Category:** FRONTEND  
**Related Areas:** TESTING, UX  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Incremental JavaScript enhancement  
**Review:** UI consolidation cycle

---

# 444. TD-021 Scope

Operaciones dinámicas deberían compartir convenciones para:

```text
idle

loading

success

empty

validation error

authorization error

server error

retry
```

---

# 445. TD-021 Risk

Sin convenciones comunes aparecen:

```text
different spinners

different error handling

duplicate submission

silent failures

inconsistent toast behavior
```

---

# 446. TD-021 Remediation Direction

Definir patrones reutilizables para:

```text
button pending state

form submission

Fetch wrapper behavior

toast feedback

inline validation

retry
```

---

# 447. TD-021 Accessibility Requirement

Loading state debe mantener:

```text
keyboard behavior

focus clarity

accessible status communication
```

---

# 448. TD-021 Acceptance Criteria

- [ ] Critical Fetch workflows comparten error semantics.
- [ ] Duplicate submission está prevenido.
- [ ] Loading state visible.
- [ ] Error feedback accesible.
- [ ] Success feedback consistente.
- [ ] Reusable utilities no ocultan domain behavior.

---

# 449. TD-022 — Accessibility Regression Coverage Remains Incomplete

**Status:** ACCEPTED  
**Category:** TESTING  
**Related Areas:** FRONTEND  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** UI maturity gap  
**Review:** Before major UI interaction expansion

---

# 450. TD-022 Scope

Debe proteger especialmente:

```text
navigation

forms

dialogs

toasts

dynamic updates

drag-and-drop alternatives

focus management
```

---

# 451. Accessibility Principle

No basta con:

```text
page looks correct.
```

---

# 452. Required Dimensions

```text
keyboard

focus

labels

semantics

status announcements

contrast

responsive interaction
```

---

# 453. TD-022 Automated Coverage

Puede incluir:

```text
automated accessibility checks
```

pero no sustituye totalmente revisión manual.

---

# 454. TD-022 Kanban Requirement

Cuando exista drag-and-drop:

```text
keyboard-accessible status transition
```

debe formar parte del diseño, no un añadido posterior.

---

# 455. TD-022 Acceptance Criteria

- [ ] Critical pages tienen automated accessibility smoke checks.
- [ ] Keyboard journeys revisados.
- [ ] Modal focus management probado.
- [ ] Dynamic feedback accesible.
- [ ] Kanban dispone de alternativa accesible si existe.
- [ ] Violations críticas bloquean release cuando corresponda.

---

# 456. Release Engineering Debt Cluster

El proceso de release debe evolucionar desde:

```text
maintainer knowledge
```

hacia:

```text
repeatable validated process.
```

---

# 457. TD-023 — Release Readiness Still Depends Partly on Manual Governance

**Status:** ACCEPTED  
**Category:** OPERATIONS  
**Related Areas:** TESTING, DX  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Project maturity growth  
**Review:** Before 1.0

---

# 458. TD-023 Current Acceptability

Para una plataforma mantenida inicialmente por una persona, cierta validación manual es razonable.

---

# 459. TD-023 Risk

A medida que aumenta el proyecto:

```text
release steps may be forgotten

migration checks may diverge

version/tag mismatch may occur

quality gates may become inconsistent
```

---

# 460. TD-023 Remediation Direction

Automatizar progresivamente:

```text
tests

lint

static analysis

migration validation

version consistency

Changelog presence

artifact build
```

---

# 461. Human Review Remains

No automatizar la decisión semántica de:

```text
whether the release is actually safe.
```

---

# 462. TD-023 Acceptance Criteria

- [ ] Required CI gates automatizados.
- [ ] Version/tag consistency validada.
- [ ] Migration validation integrada.
- [ ] Release checklist disponible.
- [ ] Artifact reproducible.
- [ ] Manual steps están documentados.
- [ ] Release no depende de memoria individual.

---

# 463. TD-024 — Critical Operational Procedures Require Executable Validation

**Status:** ACCEPTED  
**Category:** DOCUMENTATION  
**Related Areas:** OPERATIONS  
**Severity:** S2  
**Priority:** P2  
**Owner:** Maintainer  
**Origin:** Documentation maturity growth  
**Review:** Production-readiness cycle

---

# 464. TD-024 Problem

Un procedimiento puede estar bien escrito y aun así:

```text
not work under incident conditions.
```

---

# 465. Critical Procedures

Especialmente:

```text
deployment

rollback

database restore

attachment restore

secret rotation

migration recovery
```

---

# 466. Documentation Principle

```text
Critical runbooks should be executable,
not merely descriptive.
```

---

# 467. TD-024 Remediation Direction

Cada runbook crítico debe contener:

```text
preconditions

commands/actions

expected outcome

validation

failure handling
```

---

# 468. Validation

Debe probarse periódicamente en:

```text
safe environment
```

cuando sea razonable.

---

# 469. TD-024 Acceptance Criteria

- [ ] Critical runbooks identificados.
- [ ] Preconditions documentadas.
- [ ] Validation steps presentes.
- [ ] Recovery paths presentes.
- [ ] Procedures han sido ejecutadas.
- [ ] Last validation puede rastrearse.
- [ ] Obsolete instructions se eliminan.

---

# 470. Cross-cutting Dependency Map

Las principales deudas no son independientes.

---

# 471. Security Dependency Chain

```text
TD-002 Project Membership

↓

TD-001 Contextual Authorization

↓

TD-003 Nested-resource Authorization

↓

TD-006 Realtime Subscription Authorization
```

---

# 472. Realtime Dependency Chain

```text
TD-007 Event Contracts

↓

TD-008 Reconnect + Reconciliation

↓

TD-009 Duplicate / Ordering Semantics

↓

TD-010 Multi-client Testing
```

---

# 473. Production-readiness Chain

```text
TD-017 Restore Validation

TD-018 Logging + Correlation

TD-019 Realtime Metrics

TD-020 Health Semantics

TD-023 Release Readiness

TD-024 Executable Runbooks
```

---

# 474. UI Reliability Chain

```text
TD-021 Async UI States

↓

TD-011 Browser Regression Tests

↓

TD-022 Accessibility Regression Coverage
```

---

# 475. Data and Performance Chain

```text
TD-013 Constraints

TD-014 Pagination

TD-015 Query Validation
```

---

# 476. Recommended Remediation Order

Una secuencia razonable sería:

```text
1. TD-002 — Project Membership

2. TD-001 — Contextual Authorization

3. TD-003 — Nested-resource Authorization

4. TD-004 — CSRF

5. TD-006 — WebSocket Authorization

6. TD-007 — Realtime Event Contracts

7. TD-008 — Reconnect / Reconciliation

8. TD-010 — Multi-client Realtime Tests

9. TD-005 — Session / Refresh Hardening

10. TD-017 — Restore Validation
```

---

# 477. Why This Order

Prioriza:

```text
trust boundaries

↓

collaboration safety

↓

realtime reliability

↓

production recovery
```

---

# 478. Secondary Remediation Group

Posteriormente:

```text
TD-011

TD-012

TD-013

TD-014

TD-015

TD-018

TD-019

TD-020

TD-021

TD-022

TD-023

TD-024
```

según evidencia y roadmap.

---

# 479. Dependency on Live Kanban

Live Kanban no debería ampliar la deuda existente de:

```text
authorization

realtime contracts

reconciliation

multi-client testing.
```

---

# 480. Recommended Pre-Kanban Gate

Antes de Live Kanban deberían estar suficientemente resueltas:

```text
TD-001

TD-002

TD-003

TD-006

TD-007

TD-008

TD-010
```

---

# 481. CSRF Relationship

Si Kanban realiza browser mutations autenticadas mediante cookies:

```text
TD-004
```

también forma parte del gate.

---

# 482. Pre-Production Gate

Antes de considerar production readiness fuerte deberían revisarse especialmente:

```text
TD-004

TD-005

TD-017

TD-018

TD-020

TD-023

TD-024
```

---

# 483. Pre-1.0 Gate

Antes de `1.0.0` no deberían permanecer sin resolución o aceptación explícita:

```text
S1 security debt

S1 realtime reliability debt

S1 recovery debt
```

---

# 484. Debt Clustering

Cuando varias entries se trabajen conjuntamente pueden agruparse en una iniciativa.

---

# 485. Example Initiative

```text
Security Hardening
```

puede cubrir:

```text
TD-001

TD-002

TD-003

TD-004

TD-005

TD-006
```

---

# 486. Another Initiative

```text
Realtime Reliability
```

puede cubrir:

```text
TD-007

TD-008

TD-009

TD-010
```

---

# 487. Another Initiative

```text
Production Readiness
```

puede cubrir:

```text
TD-017

TD-018

TD-019

TD-020

TD-023

TD-024
```

---

# 488. Initiative Guardrail

Agrupar no significa:

```text
close all debt with one generic task.
```

---

# 489. Individual Traceability

Cada TD debe conservar:

```text
its own acceptance criteria

status

evidence

resolution.
```

---

# 490. Debt Interaction with Current Tasks

Cuando una entry se selecciona para ejecución:

```text
TD-XXX

↓

CT-XXX
```

---

# 491. Current Task Reference

La entry debe añadir:

```markdown
### Related

- Current Task: CT-XXX
```

---

# 492. In-progress Transition

Entonces:

```text
PRIORITIZED

↓

IN_PROGRESS
```

---

# 493. Completion

Cuando la tarea termina:

```text
implementation

↓

tests

↓

validation

↓

Changelog

↓

TD RESOLVED
```

---

# 494. Debt Interaction with Known Issues

Una misma remediation puede resolver:

```text
one Technical Debt

+

multiple Known Issues.
```

---

# 495. Example

```text
TD-008
Realtime reconciliation missing
```

puede explicar varios problemas visuales de stale state.

---

# 496. Resolution Rule

No cerrar la TD simplemente porque:

```text
one symptom disappeared.
```

---

# 497. Structural Resolution

Debe desaparecer:

```text
the underlying compromise.
```

---

# 498. Debt Interaction with ADRs

Si remediation cambia una boundary estable:

```text
create/update ADR before or during implementation.
```

---

# 499. Candidate ADR Areas

```text
Project Membership model

Contextual Authorization

Realtime Event Contract

Attachment Storage abstraction

Session lifecycle
```

---

# 500. Debt Interaction with Changelog

La resolución de una deuda importante debe convertirse en una entrada orientada a outcome.

---

# 501. Example

No:

```markdown
- Resolved TD-007.
```

---

# 502. Better

```markdown
### Changed

- Standardized realtime event contracts across collaborative modules.
```

---

# 503. Debt Interaction with Weekly Update

Puede informarse:

```text
Security hardening reduced three S1 debt items.
```

---

# 504. Avoid Internal Noise

No es necesario listar cada TD semanalmente.

---

# 505. Technical Debt Heatmap

Una vista conceptual puede utilizar:

| Area | Current Risk | Main Concern |
|---|---|---|
| Security | High | Contextual authorization |
| Realtime | High | Contracts and reconciliation |
| Testing | High/Medium | Multi-client and browser coverage |
| Operations | Medium/High | Restore and release readiness |
| Database | Medium | Constraints and bounded access |
| Performance | Medium | Query validation and pagination |
| Observability | Medium | Correlation and realtime metrics |
| Frontend | Medium | Async-state consistency |
| Documentation | Medium | Executable operational knowledge |

---

# 506. Heatmap Purpose

No pretende ser:

```text
precise mathematical scoring.
```

---

# 507. Heatmap Value

Permite visualizar:

```text
where architectural attention should go next.
```

---

# 508. Current Strategic Observation

La deuda más importante no parece concentrarse en:

```text
language

framework

monolith architecture

SSR choice
```

---

# 509. Instead

Se concentra principalmente en la transición desde:

```text
functional application
```

hacia:

```text
secure collaborative platform.
```

---

# 510. This Matters

Por tanto, la prioridad no debería ser:

```text
rewrite technology stack.
```

---

# 511. Preferred Direction

Debe ser:

```text
harden existing architecture

before

adding unnecessary architectural complexity.
```

---

# 512. Current Architecture Strength

La arquitectura existente puede continuar evolucionando mediante:

```text
modular boundaries

explicit policies

better tests

better contracts

better observability

better operations
```

sin necesidad inmediata de reemplazar el stack.

---

# 513. Debt Repayment Principle

```text
Strengthen the architecture where evidence shows risk.

Do not rewrite the architecture to look more sophisticated.
```

---

# 514. Part 2 Summary

Esta segunda parte define y prioriza deuda técnica relacionada con:

```text
Project Membership

Contextual Authorization

Nested-resource Security

CSRF

Sessions

Refresh Tokens

WebSocket Authentication

Realtime Subscription Authorization

Realtime Event Contracts

Reconnect

Reconciliation

Duplicates

Ordering

Multi-client Testing

UI Testing

SSR Context

Database Constraints

Pagination

Query Performance

Attachment Storage

Backup

Restore

Structured Logging

Correlation

Realtime Metrics

Health Checks

Frontend Async States

Accessibility

Release Readiness

Operational Runbooks
```

---

# 515. Continuation

La **Parte 3/3** completa `56_TECHNICAL_DEBT.md` con:

```text
Debt Remediation Workflow

Debt Review Process

Architecture Review Integration

Security Review Integration

Release Integration

Scoring Model

Debt Interest Assessment

Debt Budget

Escalation Rules

Resolution Evidence

Partial Resolution

Debt Prevention

Code Review Rules

Testing Rules

ADR Rules

Documentation Rules

Metrics

Dashboards

Anti-patterns

Detailed Checklists

Definition of Ready

Definition of Done

Pre-1.0 Debt Gate

Final Governance Principles

Recommended Final Document Structure
```

---

# 56_TECHNICAL_DEBT.md

# Aula Robótica Platform — Technical Debt

## Parte 3/4 — Remediation workflow, scoring, debt interest, reviews, prevención, integración con desarrollo y evidencia de resolución

---

# 516. Technical Debt Remediation Workflow

La resolución de deuda técnica debe seguir un flujo explícito:

```text
Discover

↓

Assess

↓

Classify

↓

Prioritize

↓

Plan

↓

Implement

↓

Validate

↓

Release

↓

Resolve

↓

Review
```

---

# 517. Step 1 — Discover

La deuda puede descubrirse durante:

```text
feature development

code review

architecture review

security review

testing

performance analysis

incident investigation

production operations

dependency upgrades
```

---

# 518. Discovery Principle

Detectar deuda no obliga automáticamente a resolverla inmediatamente.

---

# 519. First Decision

Debe determinarse:

```text
Is this actually technical debt?
```

---

# 520. Debt Qualification Questions

Preguntar:

```text
Is there a current structural compromise?

Does it increase future cost or risk?

Is the compromise currently accepted or unavoidable?

Does remediation require meaningful engineering work?

Is this different from a bug or missing feature?
```

---

# 521. Not Debt

Si la respuesta describe únicamente:

```text
future capability

isolated defect

personal preference

technology preference

cosmetic cleanup
```

no debería registrarse como Technical Debt.

---

# 522. Step 2 — Assess

Una deuda confirmada debe evaluarse según:

```text
Impact

Likelihood

Growth

Blast Radius

Remediation Cost

Dependencies
```

---

# 523. Assessment Output

El resultado debe permitir asignar:

```text
Severity

Priority

Status

Trigger
```

---

# 524. Step 3 — Classify

Asignar:

```text
Category

Related Areas

Origin
```

---

# 525. Category Stability

La categoría principal debe representar:

```text
the core structural problem
```

no necesariamente el lugar donde se detectó.

---

# 526. Example

Un fallo descubierto mediante un test WebSocket puede ser principalmente:

```text
SECURITY
```

si el problema real es authorization leakage.

---

# 527. Step 4 — Prioritize

La prioridad debe considerar:

```text
risk

debt interest

roadmap dependency

release dependency

remediation cost
```

---

# 528. Priority Is Contextual

Una deuda puede pasar de:

```text
P2

to

P1
```

sin que su implementación haya cambiado.

---

# 529. Example

```text
Realtime reconciliation
```

puede ser P2 mientras realtime sea complementario.

---

# 530. Priority Escalation

Antes de implementar:

```text
Live Kanban
```

puede convertirse en:

```text
P1.
```

---

# 531. Step 5 — Plan

Una deuda `PRIORITIZED` debe convertirse en trabajo ejecutable.

---

# 532. Planning Output

Debe conocerse:

```text
scope

dependencies

acceptance criteria

tests

migration impact

security impact

operational impact
```

---

# 533. Current Task Integration

Cuando comienza ejecución:

```text
TD-XXX

↓

Current Task
```

---

# 534. Traceability

La Technical Debt debe referenciar la tarea activa cuando exista.

---

# 535. Step 6 — Implement

La remediation debe atacar:

```text
root structural weakness
```

y no únicamente:

```text
visible symptom.
```

---

# 536. Example

Si el problema es:

```text
duplicated project authorization
```

no basta con corregir un endpoint.

---

# 537. Structural Fix

Debe consolidarse:

```text
authorization policy
```

y migrar los consumers relevantes.

---

# 538. Step 7 — Validate

La validación debe demostrar:

```text
the debt no longer creates the recorded risk.
```

---

# 539. Validation Sources

Pueden incluir:

```text
unit tests

integration tests

security tests

browser tests

realtime tests

benchmarks

migration validation

operational exercise
```

---

# 540. Step 8 — Release

Una remediation significativa debe integrarse en:

```text
55_CHANGELOG.md
```

orientada al outcome.

---

# 541. Step 9 — Resolve

La entry puede pasar a:

```text
RESOLVED
```

solo cuando:

```text
implementation

+

validation

+

required migration

+

documentation
```

estén completas.

---

# 542. Step 10 — Review

Después de resolución debe comprobarse:

```text
Did remediation introduce new debt?

Did risk move elsewhere?

Are old workarounds still present?
```

---

# 543. Debt Scoring Model

Severity y Priority continúan siendo los campos principales.

Un scoring auxiliar puede ayudar a ordenar casos similares.

---

# 544. Scoring Purpose

El score no debe sustituir:

```text
engineering judgment.
```

---

# 545. Recommended Factors

Asignar de `1` a `5`:

```text
Impact

Likelihood

Growth

Blast Radius
```

---

# 546. Impact Scale

```text
1 — negligible

2 — limited

3 — moderate

4 — significant

5 — critical
```

---

# 547. Likelihood Scale

```text
1 — unlikely

2 — possible

3 — plausible

4 — likely

5 — already recurring
```

---

# 548. Growth Scale

```text
1 — stable

2 — slow

3 — moderate

4 — fast

5 — compounds with nearly every related change
```

---

# 549. Blast Radius Scale

```text
1 — isolated helper/component

2 — single module

3 — multiple related modules

4 — cross-cutting platform concern

5 — security/data/platform-wide boundary
```

---

# 550. Base Risk Score

Puede calcularse:

```text
Risk Score =
Impact
+
Likelihood
+
Growth
+
Blast Radius
```

---

# 551. Score Range

```text
Minimum: 4

Maximum: 20
```

---

# 552. Suggested Interpretation

```text
4–7   → Low

8–11  → Moderate

12–15 → High

16–20 → Critical
```

---

# 553. Scoring Guardrail

Un resultado numérico no puede degradar automáticamente:

```text
known security risk

data integrity risk

release blocker.
```

---

# 554. Remediation Cost

Puede evaluarse separadamente:

```text
1 — trivial

2 — small

3 — moderate

4 — large

5 — major architectural work
```

---

# 555. Why Separate Cost

Una deuda puede ser:

```text
high risk

and

high cost.
```

---

# 556. Wrong Formula

No debe hacerse:

```text
high remediation cost

↓

lower priority
```

automáticamente.

---

# 557. Better Interpretation

High cost puede justificar:

```text
earlier action
```

si el coste seguirá creciendo.

---

# 558. Debt Interest Assessment

Además del riesgo actual debe evaluarse:

```text
future engineering interest.
```

---

# 559. Interest Levels

```text
LOW

MEDIUM

HIGH

COMPOUNDING
```

---

# 560. LOW Interest

La deuda permanece relativamente aislada.

---

# 561. Example

```text
minor naming inconsistency
```

---

# 562. MEDIUM Interest

Aumenta moderadamente el coste de cambios relacionados.

---

# 563. Example

```text
duplicated SSR context assembly
```

---

# 564. HIGH Interest

Cada nueva capability relacionada aumenta significativamente:

```text
duplication

testing burden

regression risk
```

---

# 565. Example

```text
fragmented realtime contracts
```

---

# 566. COMPOUNDING Interest

La deuda se replica estructuralmente con cada expansión.

---

# 567. Example

```text
non-centralized contextual authorization
```

si cada nuevo recurso introduce otra implementación.

---

# 568. Recommended Entry Extension

Las entries importantes pueden incluir:

```markdown
**Debt Interest:** COMPOUNDING
```

---

# 569. Interest Escalation Rule

Una deuda `COMPOUNDING` debe revisarse antes de añadir:

```text
another dependent capability.
```

---

# 570. Debt Budget

El proyecto debe controlar:

```text
risk budget
```

más que:

```text
entry count.
```

---

# 571. Recommended Debt Budget Policy

```text
S0

→ 0 accepted


S1

→ limited and explicitly owned


S2

→ manageable backlog


S3

→ opportunistic
```

---

# 572. S0 Budget

```text
0
```

---

# 573. S1 Budget

No establecer inicialmente un número artificial rígido.

---

# 574. Better S1 Rule

Cada S1 debe tener:

```text
owner

priority

trigger

review

remediation direction
```

---

# 575. S1 Accumulation

Si aparecen múltiples S1 en la misma boundary:

```text
pause dependent feature expansion

and

create a hardening initiative.
```

---

# 576. Current Example

El cluster:

```text
TD-001

TD-002

TD-003

TD-006
```

indica que:

```text
project collaboration security
```

debe consolidarse antes de crecer significativamente.

---

# 577. Realtime Example

El cluster:

```text
TD-007

TD-008

TD-010
```

indica necesidad de:

```text
Realtime Reliability
```

antes de Live Kanban avanzado.

---

# 578. Debt Budget Review

Debe realizarse:

```text
before major roadmap expansion

before major release

before 1.0
```

---

# 579. Escalation Rules

Una deuda debe escalarse cuando cambia su contexto.

---

# 580. Escalation Trigger — Security

Si aparece posibilidad real de:

```text
unauthorized access

cross-project leakage

credential compromise
```

debe revisarse inmediatamente.

---

# 581. Escalation Trigger — Data

Si puede producir:

```text
corruption

orphaned records

irreversible loss
```

debe escalarse.

---

# 582. Escalation Trigger — Reliability

Si comienza a producir:

```text
recurrent incidents

stale state

failed deployments

unrecoverable workflows
```

debe revisarse.

---

# 583. Escalation Trigger — Growth

Si cada feature requiere:

```text
another workaround
```

la deuda está acumulando interés.

---

# 584. Escalation Trigger — Roadmap

Si una capability planificada depende de la deuda:

```text
review before implementation.
```

---

# 585. Escalation Trigger — Release

Si la deuda contradice:

```text
release readiness expectations
```

debe elevarse antes de publicar.

---

# 586. Escalation Trigger — 1.0

Una deuda que comprometa el supported core debe revisarse antes de:

```text
1.0.0
```

---

# 587. De-escalation Rules

Puede reducirse severity o priority cuando exista evidencia de:

```text
reduced scope

new compensating control

feature removal

lower exposure

partial structural remediation
```

---

# 588. De-escalation Evidence

Debe quedar documentado:

```text
why the risk changed.
```

---

# 589. Debt Review Process

La revisión debe ser ligera pero sistemática.

---

# 590. Review Inputs

```text
Technical Debt Register

Current Tasks

Known Issues

Product Roadmap

Architecture Decisions

recent incidents

recent releases
```

---

# 591. Review Question 1

```text
Is every active debt still real?
```

---

# 592. Review Question 2

```text
Has its severity changed?
```

---

# 593. Review Question 3

```text
Has its priority changed?
```

---

# 594. Review Question 4

```text
Is debt interest increasing?
```

---

# 595. Review Question 5

```text
Has its trigger occurred?
```

---

# 596. Review Question 6

```text
Does a roadmap capability depend on it?
```

---

# 597. Review Question 7

```text
Does a Known Issue provide new evidence?
```

---

# 598. Review Question 8

```text
Should it become a Current Task?
```

---

# 599. Review Question 9

```text
Can it be closed?
```

---

# 600. Review Question 10

```text
Has remediation created another debt?
```

---

# 601. Review Output

Cada revisión debe producir solo cambios necesarios:

```text
status

severity

priority

trigger

owner

scope

related references
```

---

# 602. Avoid Review Churn

No modificar entries simplemente para demostrar actividad.

---

# 603. Architecture Review Integration

Las architecture reviews deben utilizar Technical Debt como input.

---

# 604. Architecture Review Questions

```text
Are module boundaries still clear?

Is coupling increasing?

Are dependencies flowing correctly?

Are cross-cutting policies centralized?

Are abstractions justified?

Are workarounds spreading?
```

---

# 605. Architecture Debt Discovery

Puede aparecer cuando:

```text
same logic exists across several modules

new modules depend on internal details

shared services become god objects

domain boundaries blur
```

---

# 606. Architecture Refactor Trigger

Una refactorización arquitectónica se justifica cuando:

```text
current structure creates measurable delivery or risk cost.
```

---

# 607. Architecture Rewrite Guardrail

No iniciar rewrite porque:

```text
new architecture looks cleaner in theory.
```

---

# 608. Strangler-style Improvement

Cuando un área requiera cambio importante, preferir cuando sea posible:

```text
introduce new boundary

↓

migrate consumers incrementally

↓

remove legacy path
```

---

# 609. Example — Authorization

```text
Create canonical policy

↓

migrate Project routes

↓

migrate Task routes

↓

migrate Activity routes

↓

migrate Attachments

↓

migrate WebSockets

↓

remove legacy checks
```

---

# 610. Security Review Integration

Security review debe examinar especialmente:

```text
TD-001

TD-002

TD-003

TD-004

TD-005

TD-006
```

---

# 611. Security Review Questions

```text
What does the client control?

What does the server trust?

Where is identity established?

Where is authorization enforced?

Can identifiers cross boundaries?

Can events leak across scopes?

Can sessions be revoked?
```

---

# 612. Threat-model Relationship

Security debt relevante puede requerir:

```text
threat model update.
```

---

# 613. Compensating Control Review

Si una deuda security permanece `ACCEPTED`:

```text
temporary mitigation
```

debe seguir siendo válida.

---

# 614. Example

Si la mitigación era:

```text
single-user Project access
```

deja de ser válida cuando se habilita:

```text
multi-user collaboration.
```

---

# 615. Automatic Escalation

En ese momento la deuda debe:

```text
PRIORITIZED

or

IN_PROGRESS
```

antes de ampliar exposición.

---

# 616. Testing Review Integration

La deuda de testing debe vincularse a:

```text
risk

not

coverage vanity.
```

---

# 617. Testing Review Questions

```text
Which critical behavior could regress unnoticed?

Which trust boundary lacks negative tests?

Which integration lacks realistic tests?

Which user journey is unprotected?

Which incident would our suite fail to reproduce?
```

---

# 618. Risk-based Testing Debt

Ejemplo correcto:

```text
No multi-client test verifies that unauthorized project users cannot receive Task events.
```

---

# 619. Weak Testing Debt

Ejemplo incorrecto:

```text
Need more tests.
```

---

# 620. Test Pyramid Guardrail

No forzar porcentajes rígidos entre:

```text
unit

integration

UI
```

---

# 621. Better Model

Utilizar:

```text
fast tests for local logic

integration tests for boundaries

browser tests for critical journeys

multi-client tests for realtime behavior.
```

---

# 622. Performance Review Integration

Performance debt debe partir de:

```text
measurement.
```

---

# 623. Performance Review Questions

```text
Which requests are slow?

Which views issue excessive queries?

Which lists grow without bounds?

Which payloads grow with total history?

Which operation scales poorly with expected usage?
```

---

# 624. Baseline Requirement

Antes de optimizar:

```text
capture baseline.
```

---

# 625. After Remediation

Capturar:

```text
same measurement
```

para validar resultado.

---

# 626. Benchmark Stability

Los benchmarks deben usar:

```text
representative dataset

repeatable environment

same measurement method.
```

---

# 627. Database Review Integration

Database debt debe revisarse cuando cambian:

```text
entities

relationships

authorization

high-growth tables

retention requirements.
```

---

# 628. Database Review Questions

```text
Are invariants enforced?

Are indexes aligned with queries?

Can relationships become orphaned?

Are migrations reversible or forward-fixable?

Are deletes safe?

Are high-growth tables bounded operationally?
```

---

# 629. Migration Debt

Una migration improvisada que no contempla existing data puede convertirse en deuda o issue antes incluso de deployment.

---

# 630. Migration Prevention

Cada schema change debe evaluar:

```text
existing rows

constraints

backfill

deployment order

rollback / forward fix.
```

---

# 631. Frontend Review Integration

Frontend debt debe revisarse cuando crecen:

```text
JavaScript interactions

dynamic forms

realtime UI

dialogs

drag-and-drop

client-side state.
```

---

# 632. Frontend Review Questions

```text
Is SSR still authoritative?

Is browser state duplicated unnecessarily?

Are async states consistent?

Does interaction remain accessible?

Is authorization still server-side?

Can the page recover after failed JavaScript?
```

---

# 633. Progressive Enhancement Guardrail

Siempre que sea razonable:

```text
HTML provides baseline behavior

JavaScript enhances it.
```

---

# 634. Exception

Algunas realtime interactions pueden depender legítimamente de JavaScript.

---

# 635. Required Fallback

Eso no significa necesariamente que cada realtime feature necesite:

```text
full no-JavaScript equivalent.
```

---

# 636. Accessibility Requirement

Sí debe existir una forma accesible de realizar acciones esenciales.

---

# 637. Observability Review Integration

Observability debt debe revisarse a partir de:

```text
diagnostic failures.
```

---

# 638. Core Question

```text
Could we diagnose this failure from production evidence?
```

---

# 639. If No

Existe una posible deuda de:

```text
logging

metrics

correlation

or

runbooks.
```

---

# 640. Logging Expansion Guardrail

No resolver falta de contexto mediante:

```text
logging everything.
```

---

# 641. Better

Registrar:

```text
structured useful context
```

sin:

```text
sensitive data

unbounded payloads

noise.
```

---

# 642. Operations Review Integration

Operations debt debe revisarse mediante escenarios reales.

---

# 643. Questions

```text
Can we deploy?

Can we detect failure?

Can we rollback?

Can we restore?

Can we rotate secrets?

Can we recover from migration failure?
```

---

# 644. Operational Exercise

Algunas respuestas solo pueden validarse mediante:

```text
exercise

or

simulation.
```

---

# 645. Example

Un restore procedure no está realmente validado porque:

```text
the commands look correct.
```

---

# 646. It Is Validated When

```text
a restored environment actually works.
```

---

# 647. Release Integration

Cada release debe revisar Technical Debt.

---

# 648. Release Questions

```text
Did this release create new debt?

Did it resolve existing debt?

Did it increase debt severity?

Does accepted debt make this release unsafe?
```

---

# 649. Release Blockers

Normalmente:

```text
S0

→ blocker
```

---

# 650. S1 Release Review

Cada S1 debe revisarse explícitamente.

---

# 651. S1 Does Not Automatically Block

Puede existir una S1 aceptada si:

```text
scope is controlled

mitigation exists

release does not cross its trigger.
```

---

# 652. Example

Una deuda de object storage puede permanecer si:

```text
deployment remains single-instance

and

persistent filesystem is supported.
```

---

# 653. Security Exception

Una S1 security que permita unauthorized access real no debe aceptarse simplemente para cumplir una fecha.

---

# 654. Release Debt Creation

Si una release introduce compromiso intencional:

```text
record before or with release.
```

---

# 655. Hotfix Debt

Los hotfixes merecen revisión especial.

---

# 656. Hotfix Question

```text
Did we restore service with a temporary workaround?
```

---

# 657. If Yes

Crear:

```text
Technical Debt
```

para remediation estructural.

---

# 658. Example

```text
temporary event deduplication in one handler
```

puede resolver incidente.

---

# 659. Structural Debt

Pero si el problema requiere:

```text
platform-wide idempotency strategy
```

debe registrarse.

---

# 660. Debt Prevention

La mejor gestión de deuda no consiste únicamente en:

```text
repaying debt.
```

---

# 661. It Also Means

```text
preventing unnecessary debt.
```

---

# 662. Prevention — Requirements

Antes de implementar:

```text
understand actual requirement.
```

---

# 663. Prevention — Simplicity

Elegir:

```text
simplest architecture satisfying known requirements.
```

---

# 664. Prevention — Boundaries

Mantener:

```text
clear module ownership

clear dependency direction

clear trust boundaries.
```

---

# 665. Prevention — Tests

Añadir tests en:

```text
high-risk boundaries
```

durante implementación.

---

# 666. Prevention — Database

Expresar invariantes importantes mediante:

```text
schema constraints
```

cuando sea adecuado.

---

# 667. Prevention — Security

Centralizar:

```text
authorization policies
```

antes de que se dupliquen.

---

# 668. Prevention — Realtime

Definir contratos antes de multiplicar producers y consumers.

---

# 669. Prevention — UI

Crear reusable pattern cuando:

```text
the same interaction appears repeatedly.
```

---

# 670. Prevention Guardrail

No abstraer después del primer uso solo porque:

```text
it may be reusable someday.
```

---

# 671. Rule of Repetition

La repetición real proporciona mejor evidencia para diseñar una abstracción.

---

# 672. Prevention — Operations

Automatizar:

```text
frequent

error-prone

release-critical
```

steps.

---

# 673. Prevention — Documentation

Documentar:

```text
decisions

boundaries

critical operations
```

más que implementation trivia.

---

# 674. Code Review Integration

Code review debe detectar deuda nueva.

---

# 675. Code Review Questions

```text
Does this duplicate an existing policy?

Does this create another source of truth?

Does this weaken authorization?

Does this introduce an unbounded query?

Does this create hidden client state?

Does this bypass established contracts?

Does this require a TODO that should be a TD?
```

---

# 676. Review Decision

Una deuda introducida deliberadamente puede aceptarse si:

```text
trade-off is justified

risk is bounded

entry is created

trigger is known.
```

---

# 677. Code Review Anti-pattern

No bloquear automáticamente todo cambio que:

```text
is not architecturally perfect.
```

---

# 678. Better Question

```text
Is the compromise appropriate for the current requirement?
```

---

# 679. TODO Governance

TODOs deben clasificarse.

---

# 680. Local TODO

Ejemplo:

```text
rename helper after nearby refactor
```

puede permanecer local.

---

# 681. Structural TODO

Ejemplo:

```text
authorization duplicated until membership model exists
```

debe convertirse en:

```text
Technical Debt.
```

---

# 682. TODO Reference Format

Opcional:

```text
TODO(TD-001)
```

---

# 683. TODO Cleanup

Cuando TD se resuelve:

```text
related TODOs must disappear
```

o actualizarse.

---

# 684. ADR Integration Rules

Crear ADR cuando remediation decide algo:

```text
architecturally significant

long-lived

cross-cutting

difficult to reverse.
```

---

# 685. ADR Not Required

No crear ADR para:

```text
minor refactor

small helper extraction

routine index addition
```

salvo contexto especial.

---

# 686. Example ADR Candidate

```text
Adopt explicit Project Membership as the canonical project access model.
```

---

# 687. Another Candidate

```text
Adopt versioned realtime event envelopes.
```

---

# 688. Another Candidate

```text
Introduce Attachment Storage abstraction.
```

si existe necesidad real de múltiples backends.

---

# 689. ADR Sequence

Puede ser:

```text
TD identified

↓

ADR proposed

↓

decision accepted

↓

Current Task

↓

implementation

↓

TD resolved
```

---

# 690. Documentation Integration Rules

Resolver deuda puede requerir actualizar:

```text
architecture

security

module docs

testing

deployment

operations
```

---

# 691. Documentation Scope

Actualizar solo documentos afectados.

---

# 692. Example

Resolver Project Membership puede requerir:

```text
Architecture

Security

Projects module

Database

Testing

Changelog
```

---

# 693. Documentation Is Part of Resolution

Si el nuevo boundary no está documentado y esto dificulta mantenimiento:

```text
the remediation is incomplete.
```

---

# 694. Resolution Evidence Model

Una entry resuelta debe registrar evidencia mínima.

---

# 695. Recommended Resolution Section

```markdown
### Resolution

**Resolved:** YYYY-MM-DD  
**Release:** X.Y.Z

Implemented:
- ...

Validated by:
- ...

Related:
- ADR-...
- CT-...
- KI-...
```

---

# 696. Evidence Types

```text
commit

PR

test suite

benchmark

migration

ADR

release

runbook exercise
```

---

# 697. Evidence Quality

Preferir evidencia que demuestre:

```text
outcome
```

no únicamente:

```text
code changed.
```

---

# 698. Security Resolution Evidence

Debe incluir:

```text
negative authorization tests

or equivalent security validation.
```

---

# 699. Performance Resolution Evidence

Debe incluir:

```text
before / after measurement.
```

---

# 700. Operations Resolution Evidence

Debe incluir:

```text
successful execution.
```

---

# 701. Realtime Resolution Evidence

Debe incluir escenarios:

```text
multiple clients

disconnect

reconnect

authorization

convergence
```

cuando correspondan.

---

# 702. Partial Resolution

No toda remediation elimina toda la deuda.

---

# 703. Example

Se centraliza:

```text
HTTP project authorization
```

pero WebSocket subscriptions siguen usando otra lógica.

---

# 704. Incorrect Closure

No cerrar:

```text
TD-001
```

si su scope incluía ambas boundaries.

---

# 705. Option

Mantener:

```text
IN_PROGRESS
```

hasta completar scope.

---

# 706. Alternative

Si la parte restante es claramente independiente:

```text
resolve original

+

create narrower follow-up TD.
```

---

# 707. Partial Resolution Documentation

Debe quedar claro:

```text
what improved

and

what remains.
```

---

# 708. Superseding Debt

Una entry puede resultar demasiado amplia.

---

# 709. Example

```text
TD-XXX — Realtime architecture needs improvement
```

puede dividirse en:

```text
event contracts

reconciliation

multi-client testing.
```

---

# 710. Supersede Process

La original pasa a:

```text
SUPERSEDED
```

y referencia nuevas IDs.

---

# 711. Duplicate Process

Una duplicate pasa a:

```text
DUPLICATE
```

con referencia a la canónica.

---

# 712. Closed-not-debt Process

Si una revisión demuestra que:

```text
current implementation is intentionally simple
and fully satisfies requirements
```

usar:

```text
CLOSED_NOT_DEBT.
```

---

# 713. Example

```text
No distributed event broker
```

no es deuda si:

```text
single-process realtime remains the required deployment model.
```

---

# 714. Debt Resolution Anti-pattern — Rewrite

No asumir:

```text
technical debt

↓

rewrite.
```

---

# 715. Preferred Approach

```text
incremental structural improvement.
```

---

# 716. Debt Resolution Anti-pattern — Technology Replacement

No:

```text
replace Jinja2 with React
```

para resolver una inconsistencia menor de UI.

---

# 717. Better

Resolver:

```text
the actual interaction inconsistency.
```

---

# 718. Debt Resolution Anti-pattern — Framework Upgrade

No considerar que actualizar dependencies resuelve automáticamente deuda arquitectónica.

---

# 719. Dependency Upgrade

Puede resolver:

```text
security vulnerability

compatibility limitation
```

pero no:

```text
duplicated domain policy.
```

---

# 720. Debt Resolution Anti-pattern — More Abstraction

Más layers no significan automáticamente:

```text
less debt.
```

---

# 721. Abstraction Cost

Cada abstraction añade:

```text
concept

maintenance

testing

navigation cost.
```

---

# 722. Abstraction Test

Antes de crearla:

```text
What repeated problem does this abstraction remove?
```

---

# 723. Debt Resolution Anti-pattern — Generic Service

No convertir múltiples concerns en:

```text
UniversalManagerService
```

para eliminar duplicación superficial.

---

# 724. Better

Crear boundaries según:

```text
cohesive responsibility.
```

---

# 725. Debt Resolution Anti-pattern — Test Quantity

No cerrar testing debt porque:

```text
coverage percentage increased.
```

---

# 726. Correct Closure

Cerrar cuando:

```text
recorded risk is protected.
```

---

# 727. Debt Resolution Anti-pattern — Documentation Only

No cerrar deuda estructural porque:

```text
the limitation is documented.
```

---

# 728. Documentation Can Mitigate

Pero no elimina necesariamente:

```text
underlying risk.
```

---

# 729. Debt Resolution Anti-pattern — Monitoring Only

Añadir monitoring puede reducir:

```text
detection time
```

pero no elimina necesariamente la causa.

---

# 730. Example

Monitorizar N+1 queries no resuelve:

```text
N+1 query debt.
```

---

# 731. Debt Resolution Anti-pattern — Hidden Scope Expansion

No convertir remediation de:

```text
one authorization boundary
```

en:

```text
complete IAM rewrite
```

sin decisión explícita.

---

# 732. Scope Discipline

Toda remediation debe tener:

```text
clear stop condition.
```

---

# 733. Acceptance Criteria as Stop Condition

Los criterios permiten saber:

```text
when enough is enough.
```

---

# 734. Debt Metrics

El proyecto puede mantener métricas simples.

---

# 735. Active Debt Count

```text
count by severity
```

---

# 736. Priority Debt Count

```text
P0 + P1 active
```

---

# 737. Security Debt Count

```text
active SECURITY debt
```

---

# 738. Aging

```text
time since identification
```

como señal secundaria.

---

# 739. Resolution Rate

```text
significant debt resolved per release / period
```

---

# 740. Creation Rate

```text
new significant debt identified
```

---

# 741. Trend Interpretation

No asumir:

```text
more discovered debt

=

worse engineering.
```

---

# 742. Healthy Discovery

Durante auditorías puede aumentar temporalmente el registro porque:

```text
visibility improved.
```

---

# 743. Better Metric

Observar:

```text
high-risk unmanaged debt.
```

---

# 744. Target

```text
S0 unmanaged = 0
```

---

# 745. Another Target

```text
S1 without owner = 0
```

---

# 746. Another Target

```text
S1 without trigger/review = 0
```

---

# 747. Debt Dashboard

Si el proyecto crece, puede existir una vista documental o automatizada.

---

# 748. Candidate Dashboard

```text
Active by Severity

Active by Category

P0/P1

Oldest S1

Compounding Debt

Recently Resolved
```

---

# 749. Dashboard Guardrail

No dedicar más esfuerzo a:

```text
measuring debt
```

que a:

```text
understanding and reducing risk.
```

---

# 750. Debt Heatmap Review

La heatmap debe actualizarse cuando cambie significativamente:

```text
risk concentration.
```

---

# 751. Current Expected Concentration

Durante la fase actual:

```text
SECURITY

REALTIME

TESTING

OPERATIONS
```

deben recibir especial atención.

---

# 752. Future Shift

Tras hardening, la concentración puede desplazarse hacia:

```text
performance

domain complexity

operations

developer experience
```

---

# 753. Debt Prevention in Feature Design

Cada feature importante debería incluir una pregunta explícita:

```text
Which existing debt does this depend on?
```

---

# 754. Second Question

```text
Which new debt could this introduce?
```

---

# 755. Third Question

```text
Can we avoid compounding debt with a small structural improvement now?
```

---

# 756. Example — Inventory

Antes de Inventory revisar:

```text
authorization model

audit patterns

attachment relationships

pagination patterns
```

si se reutilizan.

---

# 757. Example — PWA

Antes de PWA revisar:

```text
session semantics

offline state

cache invalidation

security boundaries
```

---

# 758. Example — AI/RAG

Antes de RAG revisar:

```text
authorization-aware retrieval

document boundaries

auditability

sensitive data

evaluation
```

---

# 759. AI Debt Prevention

No añadir AI sobre un authorization model que no pueda garantizar:

```text
which documents the actor may retrieve.
```

---

# 760. Example — Multi-instance Deployment

Antes de escalar horizontalmente revisar:

```text
WebSocket connection state

Attachment storage

session state

background work

event fan-out
```

---

# 761. Scaling Principle

```text
Deployment topology changes
can turn previously acceptable simplicity
into technical debt.
```

---

# 762. Dependency Upgrade Debt

Dependencies obsoletas pueden convertirse en deuda cuando:

```text
security support ends

runtime compatibility breaks

maintenance becomes blocked.
```

---

# 763. Dependency Debt Entry

Debe indicar:

```text
dependency

supported baseline

risk

upgrade blocker
```

---

# 764. Avoid Upgrade Churn

No registrar como deuda:

```text
a library is one minor version behind
```

sin necesidad.

---

# 765. Runtime Debt

Un runtime fuera de soporte sí puede ser:

```text
S1
```

según exposición.

---

# 766. Dependency Review

Debe formar parte de:

```text
security

maintenance

release planning.
```

---

# 767. Documentation Drift Debt

Documentación desactualizada puede convertirse en deuda si:

```text
developers or operators make unsafe decisions from it.
```

---

# 768. Drift Detection

Comparar periódicamente:

```text
architecture docs

security docs

deployment docs

actual implementation.
```

---

# 769. Generated Documentation

Puede reducir drift para:

```text
API schemas

dependency inventories

configuration references
```

cuando sea apropiado.

---

# 770. Guardrail

No generar automáticamente documentación conceptual que requiere:

```text
engineering reasoning.
```

---

# 771. Debt and Learning

La resolución de deuda debe dejar aprendizaje reutilizable.

---

# 772. Learning Capture

Puede quedar en:

```text
ADR

Coding Rules

Testing Strategy

Security docs

runbook
```

---

# 773. Goal

Evitar:

```text
same debt pattern reappears later.
```

---

# 774. Example

Tras resolver authorization duplication:

```text
Coding Rules
```

puede establecer:

```text
project-scoped authorization must use canonical policies.
```

---

# 775. Example

Tras resolver realtime contract fragmentation:

```text
Realtime architecture
```

puede exigir:

```text
all events use the canonical envelope.
```

---

# 776. Institutionalization

Una deuda está mejor resuelta cuando:

```text
architecture changed

and

the old failure pattern is harder to reintroduce.
```

---

# 777. Prevention Through Tests

Regression tests son una forma de:

```text
institutionalized memory.
```

---

# 778. Prevention Through Constraints

Database constraints son otra forma.

---

# 779. Prevention Through CI

Automated gates son otra.

---

# 780. Prevention Through Shared Policies

Centralized authorization es otra.

---

# 781. Prevention Through Documentation

ADRs y Coding Rules complementan esas safeguards.

---

# 782. Technical Debt Review Record

Para cambios relevantes puede añadirse:

```markdown
### Review History

- 2026-XX-XX — Severity confirmed as S1; remediation required before Live Kanban.
- 2026-XX-XX — Promoted to PRIORITIZED after Project Membership work began.
```

---

# 783. Review History Guardrail

No registrar:

```text
every minor review.
```

---

# 784. Useful Reviews

Solo eventos que cambien:

```text
risk

priority

scope

status

trigger.
```

---

# 785. Resolution History

No eliminar el contexto original después de resolver.

---

# 786. Why

Permite entender:

```text
why remediation existed.
```

---

# 787. Resolved Debt Placement

Puede mantenerse en sección:

```text
Resolved Technical Debt
```

---

# 788. Active Register

La tabla principal puede mostrar únicamente:

```text
active entries.
```

---

# 789. Historical Register

Las resueltas pueden mantenerse en una tabla secundaria.

---

# 790. Recommended Resolved Table

```markdown
| ID | Title | Category | Resolved | Release |
|---|---|---|---|---|
| TD-XXX | ... | SECURITY | YYYY-MM-DD | X.Y.Z |
```

---

# 791. Never Reuse ID

Incluso tras moverla a histórico:

```text
TD-XXX remains permanently reserved.
```

---

# 792. Part 3 Summary

Esta tercera parte establece:

```text
Remediation Workflow

Debt Qualification

Risk Scoring

Debt Interest

Debt Budget

Escalation

De-escalation

Architecture Reviews

Security Reviews

Testing Reviews

Performance Reviews

Database Reviews

Frontend Reviews

Observability Reviews

Operations Reviews

Release Integration

Hotfix Debt

Debt Prevention

Code Review

TODO Governance

ADR Integration

Documentation Integration

Resolution Evidence

Partial Resolution

Superseding

Metrics

Debt Dashboards

Feature-design Prevention

Dependency Debt

Documentation Drift

Institutionalized Learning
```

---

# 793. Continuation

La **Parte 4/4** completa `56_TECHNICAL_DEBT.md` con:

```text
Anti-pattern Catalog

Debt Entry Quality Rules

Security Debt Checklist

Realtime Debt Checklist

Database Debt Checklist

Testing Debt Checklist

Performance Debt Checklist

Operations Debt Checklist

Documentation Debt Checklist

Definition of Ready

Definition of Done

Resolution Checklist

Release Debt Gate

Pre-1.0 Debt Gate

Technical Debt Governance

Recommended Final Register Structure

Final Principles

Final Technical Debt Statement
```

---

# 56_TECHNICAL_DEBT.md

# Aula Robótica Platform — Technical Debt

## Parte 4/4 — Anti-patterns, quality rules, checklists, Definition of Ready, Definition of Done, release gates, pre-1.0 governance y principios finales

---

# 794. Technical Debt Anti-pattern Catalog

La gestión de deuda técnica también debe identificar prácticas que aparentan mejorar el sistema pero que pueden aumentar:

```text
complexity

risk

maintenance cost

or

architectural ambiguity.
```

---

# 795. Anti-pattern — Everything Is Technical Debt

No clasificar cualquier mejora pendiente como:

```text
Technical Debt.
```

---

# 796. Why It Fails

Si todo es deuda:

```text
nothing is meaningfully prioritized.
```

---

# 797. Correct Classification

Preguntar primero si corresponde a:

```text
Feature Backlog

Known Issue

Current Task

Technical Debt

Architecture Decision

Documentation improvement
```

---

# 798. Anti-pattern — Missing Technology Equals Debt

Incorrecto:

```text
No Kafka

No Redis

No Kubernetes

No React

No microservices
```

---

# 799. Correct Principle

```text
Missing technology is not technical debt.

Unmet engineering requirements may be.
```

---

# 800. Anti-pattern — Architecture Fashion

No migrar arquitectura para alinearse con:

```text
current industry fashion
```

sin problema concreto.

---

# 801. Examples

```text
modular monolith → microservices

SSR → SPA

PostgreSQL → distributed database

WebSocket manager → event broker
```

no son mejoras automáticas.

---

# 802. Architecture Fitness

La pregunta correcta es:

```text
Does the current architecture still satisfy
the required quality attributes?
```

---

# 803. Anti-pattern — Debt Without Evidence

Evitar:

```text
This might be a problem someday.
```

como única justificación.

---

# 804. Better

Registrar:

```text
current compromise

credible risk

growth path

trigger
```

---

# 805. Anti-pattern — Debt Without Trigger

Evitar:

```text
Fix later.
```

---

# 806. Better

```text
Resolve before multi-user collaboration.
```

---

# 807. Anti-pattern — Debt Without Owner

Una entry sin owner tiende a convertirse en:

```text
permanent forgotten architecture.
```

---

# 808. Anti-pattern — Permanent ACCEPTED

`ACCEPTED` no significa:

```text
ignore forever.
```

---

# 809. Required Behavior

Debe existir:

```text
review

trigger

owner

and

explicit rationale
```

para mantener una deuda en estado:

```text
ACCEPTED.
```

---

# 810. Anti-pattern — Fixing Symptoms Only

No considerar resuelta una deuda cuando únicamente desaparece:

```text
one visible symptom.
```

---

# 811. Example

Si existen múltiples comprobaciones de autorización duplicadas:

```text
fixing one endpoint
```

no resuelve:

```text
fragmented contextual authorization.
```

---

# 812. Correct Resolution

La remediation debe eliminar o reducir suficientemente:

```text
the structural cause.
```

---

# 813. Anti-pattern — Rewrite as Default Remediation

Evitar:

```text
technical debt

↓

rewrite subsystem
```

como respuesta automática.

---

# 814. Rewrite Risk

Los rewrites pueden introducir:

```text
new regressions

feature parity gaps

migration complexity

new technical debt

long delivery cycles
```

---

# 815. Preferred Strategy

Cuando sea posible:

```text
stabilize

↓

introduce better boundary

↓

migrate incrementally

↓

validate

↓

remove legacy path
```

---

# 816. Anti-pattern — Refactoring Without Exit Criteria

Una remediation sin criterios de finalización puede convertirse en:

```text
open-ended cleanup.
```

---

# 817. Required Exit Criteria

Toda remediation relevante debe conocer:

```text
what must be true

for the debt to be considered resolved.
```

---

# 818. Anti-pattern — Refactoring Everything Nearby

Resolver deuda no autoriza automáticamente:

```text
cleaning every adjacent module.
```

---

# 819. Scope Rule

```text
Touch what is necessary to remove the recorded risk.
```

---

# 820. Anti-pattern — Premature Generalization

No convertir una solución local clara en:

```text
generic framework
```

antes de conocer patrones reales de reutilización.

---

# 821. Example

No crear:

```text
UniversalResourceAuthorizationEngine
```

si únicamente existen dos políticas concretas y claras.

---

# 822. Better

Construir:

```text
small explicit policies
```

y generalizar únicamente cuando exista evidencia.

---

# 823. Anti-pattern — God Service Remediation

No eliminar duplicación moviéndola toda a:

```text
one enormous service.
```

---

# 824. Result

Eso sustituye:

```text
duplication debt
```

por:

```text
coupling and cohesion debt.
```

---

# 825. Anti-pattern — Shared Utility Dump

Evitar módulos como:

```text
utils.py

helpers.py

common.py
```

que acumulen responsabilidades sin relación.

---

# 826. Better Utility Rule

Compartir únicamente lógica con:

```text
clear purpose

stable semantics

cohesive responsibility.
```

---

# 827. Anti-pattern — Layer Proliferation

No introducir capas como:

```text
Manager

Coordinator

Facade

Provider

Adapter

Handler

Processor
```

sin responsabilidad claramente diferenciada.

---

# 828. Layer Test

Cada layer debe responder:

```text
What boundary does this layer protect?
```

---

# 829. Anti-pattern — Repository Abstraction Without Need

No introducir repositories genéricos únicamente porque:

```text
other architectures use repositories.
```

---

# 830. Current Principle

SQLAlchemy persistence puede permanecer directa y explícita mientras:

```text
domain boundaries remain clear

queries remain testable

storage substitution is not required.
```

---

# 831. Anti-pattern — Event-driven Everything

No convertir todas las operaciones internas en:

```text
events
```

sin necesidad.

---

# 832. Events Are Appropriate When

Existe valor en:

```text
decoupled reaction

asynchronous processing

realtime notification

audit propagation

multiple independent consumers.
```

---

# 833. Events Are Not Free

Añaden:

```text
ordering concerns

delivery concerns

debugging complexity

event contracts

testing complexity.
```

---

# 834. Anti-pattern — Distributed System Before Need

No introducir:

```text
distributed cache

message broker

service mesh

distributed tracing

microservices
```

como pago de deuda de un sistema que todavía funciona correctamente como:

```text
modular monolith.
```

---

# 835. Anti-pattern — Cache Before Measurement

No utilizar cache para ocultar:

```text
poor query design.
```

---

# 836. Preferred Performance Order

```text
measure

↓

fix query/data access

↓

bound data

↓

index appropriately

↓

cache only when justified
```

---

# 837. Anti-pattern — Index Everything

Más índices pueden producir:

```text
slower writes

higher storage

migration overhead

maintenance cost.
```

---

# 838. Index Rule

Crear índices basados en:

```text
real query patterns

constraints

measured access paths.
```

---

# 839. Anti-pattern — Logging Everything

No resolver observability mediante:

```text
maximum log volume.
```

---

# 840. Logging Quality

Preferir:

```text
structured

contextual

actionable

privacy-aware
```

logs.

---

# 841. Anti-pattern — Metrics Without Questions

No añadir métricas porque:

```text
metrics are good.
```

---

# 842. Better Metric Question

```text
What operational question will this metric answer?
```

---

# 843. Anti-pattern — Alerts for Every Failure

Alerting excesivo produce:

```text
alert fatigue.
```

---

# 844. Alert Requirement

Una alerta debe representar:

```text
actionable operational condition.
```

---

# 845. Anti-pattern — Tests for Coverage Only

No escribir tests únicamente para aumentar:

```text
coverage percentage.
```

---

# 846. Better Testing Goal

```text
protect important behavior and boundaries.
```

---

# 847. Anti-pattern — Mock Everything

Exceso de mocks puede producir tests que:

```text
validate implementation assumptions

instead of

real integration behavior.
```

---

# 848. Integration Priority

Boundaries importantes deben validarse con componentes reales cuando sea razonable:

```text
database

authentication

authorization

WebSocket lifecycle

HTTP integration.
```

---

# 849. Anti-pattern — E2E Everything

Tampoco convertir toda validación en:

```text
browser E2E tests.
```

---

# 850. Why

Puede producir suites:

```text
slow

fragile

hard to diagnose

expensive to maintain.
```

---

# 851. Balanced Testing

```text
Unit

+

Integration

+

Security

+

Browser

+

Realtime
```

según riesgo.

---

# 852. Anti-pattern — Documentation as Architecture

No considerar que una arquitectura es correcta únicamente porque:

```text
it is documented.
```

---

# 853. Documentation Role

La documentación:

```text
describes

explains

governs
```

pero no sustituye:

```text
implementation quality.
```

---

# 854. Anti-pattern — Architecture Existing Only in Documentation

La implementación debe reflejar:

```text
documented boundaries.
```

---

# 855. Drift

Si documentación e implementación divergen:

```text
one or both must be corrected.
```

---

# 856. Anti-pattern — Permanent Temporary Fix

Todo workaround explícitamente temporal debe tener:

```text
owner

trigger

or

removal condition.
```

---

# 857. Anti-pattern — Debt Hidden in Comments

No mantener problemas estructurales importantes únicamente mediante:

```text
TODO

FIXME

HACK
```

---

# 858. Required Action

Convertirlos en una entry cuando:

```text
scope

risk

or

future cost
```

lo justifique.

---

# 859. Technical Debt Entry Quality Rules

Toda entry debe cumplir un mínimo de calidad.

---

# 860. Quality Rule 1 — Specific Problem

Debe explicar:

```text
what structural compromise exists.
```

---

# 861. Quality Rule 2 — Current Reality

Debe describir:

```text
current architecture
```

y no únicamente una solución futura.

---

# 862. Quality Rule 3 — Rationale

Debe explicar:

```text
why the compromise exists.
```

---

# 863. Quality Rule 4 — Consequence

Debe explicar:

```text
what risk or cost it creates.
```

---

# 864. Quality Rule 5 — Scope

Debe quedar claro:

```text
which modules or boundaries are affected.
```

---

# 865. Quality Rule 6 — Severity

Debe asignarse según:

```text
technical consequence.
```

---

# 866. Quality Rule 7 — Priority

Debe asignarse según:

```text
when remediation is needed.
```

---

# 867. Quality Rule 8 — Ownership

Debe existir responsable de:

```text
review and follow-up.
```

---

# 868. Quality Rule 9 — Trigger

Debe conocerse:

```text
when deferral stops being acceptable.
```

---

# 869. Quality Rule 10 — Remediation Direction

Debe existir una dirección plausible sin exigir:

```text
full implementation design.
```

---

# 870. Quality Rule 11 — Acceptance Criteria

Debe poder determinarse:

```text
when the debt is resolved.
```

---

# 871. Quality Rule 12 — Evidence

Cuando se cierre debe existir:

```text
validation evidence.
```

---

# 872. Entry Quality Checklist

Antes de aceptar una nueva TD:

```text
[ ] It describes a structural compromise.

[ ] It is not merely a bug.

[ ] It is not merely a missing feature.

[ ] It is not technology preference.

[ ] Current impact is understood.

[ ] Future interest is understood.

[ ] Category is clear.

[ ] Severity is justified.

[ ] Priority is justified.

[ ] Owner exists.

[ ] Trigger exists.

[ ] Remediation direction exists.
```

---

# 873. Security Debt Checklist

Para cualquier deuda `SECURITY`:

```text
[ ] Trust boundary identified.

[ ] Threat identified.

[ ] Exposed actor identified.

[ ] Protected resource identified.

[ ] Current mitigation identified.

[ ] Authorization implications reviewed.

[ ] Authentication implications reviewed.

[ ] Session implications reviewed if applicable.

[ ] Realtime implications reviewed if applicable.

[ ] Data exposure reviewed.

[ ] Negative tests planned.

[ ] Trigger defined.

[ ] Release impact reviewed.
```

---

# 874. Security Debt Additional Rule

Una deuda security no debe describirse de forma vaga como:

```text
security could be improved.
```

---

# 875. Required Security Statement

Debe identificar:

```text
what could be accessed

by whom

through which boundary

under what condition.
```

---

# 876. Authorization Debt Checklist

```text
[ ] Actor identity is server-derived.

[ ] Resource scope is explicit.

[ ] Project boundary is resolved.

[ ] Nested-resource ancestry is validated.

[ ] Read authorization exists.

[ ] Mutation authorization exists.

[ ] Realtime authorization exists where applicable.

[ ] UI visibility is not treated as security.

[ ] Cross-project tests exist.

[ ] Non-member tests exist.

[ ] Privilege escalation tests exist.
```

---

# 877. Session Debt Checklist

```text
[ ] Access-token lifetime defined.

[ ] Refresh-token lifetime defined.

[ ] Rotation behavior defined.

[ ] Revocation behavior defined.

[ ] Logout semantics defined.

[ ] Reuse behavior defined.

[ ] Cookie flags reviewed.

[ ] CSRF interaction reviewed.

[ ] Concurrent session behavior defined.

[ ] Expiration tests exist.
```

---

# 878. Realtime Debt Checklist

```text
[ ] Authentication source defined.

[ ] Subscription authorization defined.

[ ] Event scope defined.

[ ] Event contract versioned.

[ ] Event identity defined where required.

[ ] Duplicate semantics defined.

[ ] Ordering semantics defined.

[ ] Disconnect behavior defined.

[ ] Reconnect behavior defined.

[ ] Reconciliation behavior defined.

[ ] Unauthorized isolation tested.

[ ] Multi-client convergence tested.

[ ] Cleanup tested.

[ ] Operational metrics considered.
```

---

# 879. Realtime Contract Checklist

```text
[ ] Event type has semantic name.

[ ] Event version exists.

[ ] Scope is explicit.

[ ] Resource identity is explicit.

[ ] occurred_at semantics defined.

[ ] event_id semantics defined.

[ ] Payload is bounded.

[ ] Sensitive information excluded.

[ ] Unknown-event behavior defined.

[ ] Compatibility expectations documented.
```

---

# 880. Reconciliation Checklist

```text
[ ] Missed-event window considered.

[ ] Reconnect does not assume convergence.

[ ] Authoritative state source identified.

[ ] Re-subscription occurs safely.

[ ] Repeated reconnect is idempotent.

[ ] Duplicate handlers are prevented.

[ ] Client can recover from stale state.

[ ] Multi-client tests reproduce disconnect window.
```

---

# 881. Database Debt Checklist

```text
[ ] Domain invariant identified.

[ ] Foreign keys reviewed.

[ ] Nullability reviewed.

[ ] Uniqueness reviewed.

[ ] Index requirements reviewed.

[ ] Existing data considered.

[ ] Backfill considered.

[ ] Migration ordering considered.

[ ] Delete behavior considered.

[ ] Integrity errors handled.

[ ] Backup implications reviewed.
```

---

# 882. Migration Debt Checklist

```text
[ ] Existing rows compatible.

[ ] New constraints can be applied safely.

[ ] Backfill strategy exists.

[ ] Deployment ordering exists.

[ ] Application compatibility during migration considered.

[ ] Failure handling defined.

[ ] Forward-fix strategy understood.

[ ] Restore implications understood.
```

---

# 883. Performance Debt Checklist

```text
[ ] Actual bottleneck identified.

[ ] Baseline measured.

[ ] Representative dataset used.

[ ] Query count reviewed.

[ ] Rows loaded reviewed.

[ ] Payload size reviewed.

[ ] Pagination reviewed.

[ ] Indexes reviewed.

[ ] N+1 behavior reviewed.

[ ] Memory implications reviewed.

[ ] Before/after validation planned.
```

---

# 884. Performance Optimization Guardrail Checklist

```text
[ ] Optimization solves measured problem.

[ ] Complexity increase is justified.

[ ] Correctness remains primary.

[ ] Authorization remains intact.

[ ] Readability remains acceptable.

[ ] Benchmark is reproducible.

[ ] No premature cache introduced.

[ ] No unnecessary infrastructure introduced.
```

---

# 885. Backend Debt Checklist

```text
[ ] Domain logic location reviewed.

[ ] Router responsibility reviewed.

[ ] Service responsibility reviewed.

[ ] Transaction boundary reviewed.

[ ] Error semantics reviewed.

[ ] Authorization location reviewed.

[ ] Persistence coupling reviewed.

[ ] Shared abstraction justified.

[ ] Tests protect behavior.
```

---

# 886. Frontend Debt Checklist

```text
[ ] SSR remains authoritative where intended.

[ ] Client state is minimal.

[ ] Loading state exists.

[ ] Error state exists.

[ ] Empty state exists.

[ ] Duplicate submission prevented.

[ ] Authorization is server-enforced.

[ ] Keyboard behavior reviewed.

[ ] Focus behavior reviewed.

[ ] Dynamic feedback accessible.

[ ] Realtime recovery considered.
```

---

# 887. UI Testing Debt Checklist

```text
[ ] Critical journey identified.

[ ] Business risk identified.

[ ] Browser-specific behavior requires E2E test.

[ ] Authentication path covered.

[ ] Authorization path covered.

[ ] Error path covered.

[ ] Accessibility-sensitive behavior covered.

[ ] Test remains deterministic.

[ ] Test does not duplicate lower-layer coverage unnecessarily.
```

---

# 888. Testing Debt Checklist

```text
[ ] Unprotected risk identified.

[ ] Correct test layer selected.

[ ] Positive path covered.

[ ] Negative path covered.

[ ] Boundary conditions covered.

[ ] Security-sensitive behavior covered.

[ ] Integration behavior covered where required.

[ ] Realtime multi-client behavior covered where required.

[ ] Flakiness risk considered.

[ ] CI execution cost considered.
```

---

# 889. Observability Debt Checklist

```text
[ ] Operational question identified.

[ ] Failure currently difficult to diagnose.

[ ] Required log context identified.

[ ] Correlation requirement identified.

[ ] Metric requirement identified.

[ ] Sensitive data excluded.

[ ] Cardinality controlled.

[ ] Alert is actionable if created.

[ ] Retention implications considered.
```

---

# 890. Logging Debt Checklist

```text
[ ] Structured fields defined.

[ ] Request correlation available.

[ ] Actor context included only when appropriate.

[ ] Resource context available where useful.

[ ] Error context sufficient.

[ ] Secrets excluded.

[ ] Tokens excluded.

[ ] Sensitive payloads excluded.

[ ] Log level appropriate.

[ ] Duplicate noisy logging avoided.
```

---

# 891. Operations Debt Checklist

```text
[ ] Deployment procedure known.

[ ] Rollback strategy known.

[ ] Backup exists.

[ ] Restore tested.

[ ] Health checks meaningful.

[ ] Secrets manageable.

[ ] Migration recovery defined.

[ ] Required persistent data identified.

[ ] Failure detection exists.

[ ] Runbook exists where needed.
```

---

# 892. Backup and Restore Checklist

```text
[ ] PostgreSQL included.

[ ] Attachments included.

[ ] Retention defined.

[ ] Encryption requirements reviewed.

[ ] Backup access restricted.

[ ] Restore environment available.

[ ] Restore procedure executed.

[ ] Application starts after restore.

[ ] Critical data validated.

[ ] Recovery evidence recorded.
```

---

# 893. Deployment Debt Checklist

```text
[ ] Build reproducible.

[ ] Configuration externalized appropriately.

[ ] Secrets not committed.

[ ] Migration order defined.

[ ] Readiness validated.

[ ] Persistent storage validated.

[ ] Rollback path understood.

[ ] Version/tag consistent.

[ ] Release artifact traceable.
```

---

# 894. Documentation Debt Checklist

```text
[ ] Missing knowledge is operationally or technically important.

[ ] Correct source-of-truth document identified.

[ ] Current implementation verified.

[ ] Procedure is actionable where required.

[ ] Preconditions documented.

[ ] Validation documented.

[ ] Failure handling documented.

[ ] Ownership clear.

[ ] Drift risk considered.
```

---

# 895. Architecture Debt Checklist

```text
[ ] Boundary problem identified.

[ ] Coupling problem identified.

[ ] Duplication is structural, not incidental.

[ ] Current architecture limitation evidenced.

[ ] Simpler remediation considered.

[ ] Rewrite avoided unless justified.

[ ] New abstraction has concrete responsibility.

[ ] Dependency direction remains clear.

[ ] ADR need evaluated.
```

---

# 896. Developer Experience Debt Checklist

```text
[ ] Friction is recurring.

[ ] Friction affects development reliability or speed.

[ ] Manual step is error-prone.

[ ] Automation benefit is clear.

[ ] Local setup complexity identified.

[ ] Feedback-loop impact measured qualitatively or quantitatively.

[ ] Proposed tooling does not create disproportionate maintenance.
```

---

# 897. Definition of Ready — Technical Debt

Una Technical Debt está preparada para ejecución cuando:

```text
problem is understood

scope is bounded

risk is known

remediation direction is plausible

dependencies are known

validation can be defined.
```

---

# 898. Technical Debt DoR Checklist

```text
[ ] TD identifier exists.

[ ] Title describes structural problem.

[ ] Category assigned.

[ ] Severity assigned.

[ ] Priority assigned.

[ ] Owner assigned.

[ ] Context documented.

[ ] Current compromise documented.

[ ] Consequences documented.

[ ] Debt interest understood.

[ ] Trigger documented.

[ ] Remediation direction documented.

[ ] Dependencies identified.

[ ] Acceptance criteria defined.

[ ] Required tests identified.

[ ] Migration impact reviewed.

[ ] Security impact reviewed.

[ ] Operational impact reviewed.

[ ] ADR requirement evaluated.
```

---

# 899. Ready Exception

Una S0 puede comenzar remediation inmediatamente aunque:

```text
full documentation is incomplete.
```

---

# 900. Emergency Rule

En riesgo crítico:

```text
contain first

document immediately after stabilization.
```

---

# 901. Definition of Done — Technical Debt

Una Technical Debt está `RESOLVED` cuando:

```text
structural compromise is removed or reduced to accepted target

and

the result is validated.
```

---

# 902. Technical Debt DoD Checklist

```text
[ ] Root structural issue addressed.

[ ] Legacy workaround removed where applicable.

[ ] New boundary implemented.

[ ] Relevant consumers migrated.

[ ] Tests updated.

[ ] Negative tests added where required.

[ ] Security validation completed.

[ ] Database migration completed where required.

[ ] Performance validation completed where required.

[ ] Realtime validation completed where required.

[ ] Operational validation completed where required.

[ ] Documentation updated.

[ ] ADR updated/created where required.

[ ] Coding Rules updated if a reusable rule emerged.

[ ] Known Issues updated.

[ ] Current Task closed.

[ ] Changelog updated.

[ ] Resolution evidence recorded.

[ ] Resolution date recorded.

[ ] Release recorded when applicable.

[ ] No obsolete TODO(TD-XXX) remains.
```

---

# 903. Resolution Checklist

Antes de cambiar:

```text
IN_PROGRESS

↓

RESOLVED
```

preguntar:

```text
Did we fix the structural cause?

Did we validate the original risk?

Did we migrate all relevant paths?

Did we remove obsolete workarounds?

Did we update governance?
```

---

# 904. Resolution Failure

Si alguna respuesta crítica es:

```text
No
```

la deuda debería permanecer:

```text
IN_PROGRESS
```

o dividirse explícitamente.

---

# 905. Technical Debt Release Gate

Cada release debería revisar:

```text
new debt

changed debt

resolved debt

release-blocking debt.
```

---

# 906. Release Gate Checklist

```text
[ ] No unmanaged S0 debt.

[ ] S1 debt reviewed.

[ ] Security debt reviewed.

[ ] Data integrity debt reviewed.

[ ] Migration debt reviewed.

[ ] Operational debt reviewed.

[ ] New intentional debt registered.

[ ] Resolved debt has evidence.

[ ] Changelog reflects significant remediation.

[ ] Release does not cross an unresolved debt trigger.
```

---

# 907. Release Trigger Rule

La condición más importante es:

```text
Does this release make an accepted debt assumption false?
```

---

# 908. Example

Si TD-002 se acepta porque Projects todavía no tienen colaboración multi-user:

```text
a release enabling multi-user collaboration
```

no puede publicarse sin reevaluarla.

---

# 909. Another Example

Si local attachment storage se acepta porque existe:

```text
single application instance
```

una release multi-instance debe reevaluar:

```text
TD-016.
```

---

# 910. Another Example

Si realtime reconciliation es limitada mientras realtime solo actualiza información secundaria:

```text
Live Kanban
```

cambia radicalmente ese supuesto.

---

# 911. Release Gate Principle

```text
Debt becomes dangerous when product evolution
invalidates the assumptions that made it acceptable.
```

---

# 912. Pre-Production Technical Debt Gate

Antes de considerar la plataforma production-ready debe revisarse especialmente:

```text
Security

Data Integrity

Recovery

Observability

Deployment

Critical Testing
```

---

# 913. Pre-Production Security Gate

```text
[ ] Project access boundary explicit.

[ ] Nested authorization systematic.

[ ] Browser mutations CSRF-protected.

[ ] Session lifecycle defined.

[ ] WebSocket authentication trusted server-side.

[ ] Realtime subscriptions authorized.

[ ] Sensitive logging prevented.

[ ] Security regression tests exist.
```

---

# 914. Pre-Production Data Gate

```text
[ ] Critical constraints enforced.

[ ] Migrations validated.

[ ] Backup complete.

[ ] Restore tested.

[ ] Attachment consistency considered.

[ ] Destructive operations understood.
```

---

# 915. Pre-Production Reliability Gate

```text
[ ] Critical browser journeys tested.

[ ] Critical realtime behavior tested.

[ ] Reconnect behavior validated.

[ ] Health semantics defined.

[ ] Failure paths understood.
```

---

# 916. Pre-Production Operations Gate

```text
[ ] Deployment repeatable.

[ ] Configuration documented.

[ ] Secrets handled securely.

[ ] Rollback understood.

[ ] Restore executable.

[ ] Critical runbooks validated.
```

---

# 917. Pre-Production Observability Gate

```text
[ ] Structured logging available.

[ ] Request correlation available.

[ ] Critical failures observable.

[ ] Health status observable.

[ ] Realtime failures diagnosable.

[ ] No sensitive telemetry leakage.
```

---

# 918. Pre-1.0 Technical Debt Gate

La versión:

```text
1.0.0
```

debe representar una plataforma cuyo core soportado tenga:

```text
stable architecture

explicit security boundaries

reliable persistence

tested collaboration

recoverable operations

maintainable contracts.
```

---

# 919. Pre-1.0 S0 Rule

```text
Active S0 debt = 0
```

---

# 920. Pre-1.0 S1 Rule

Toda S1 debe estar:

```text
RESOLVED

or

explicitly accepted with strong justification,
bounded exposure,
owner,
mitigation,
and trigger.
```

---

# 921. Pre-1.0 Security Rule

No debería existir deuda S1 aceptada que permita:

```text
known unauthorized access

known cross-project leakage

known privilege escalation

known session compromise path
```

en el supported core.

---

# 922. Pre-1.0 Realtime Rule

Si realtime forma parte del core:

```text
authentication

authorization

reconnect

reconciliation

multi-client convergence
```

deben estar suficientemente consolidados.

---

# 923. Pre-1.0 Recovery Rule

Debe existir evidencia de:

```text
successful restore.
```

---

# 924. Pre-1.0 Testing Rule

Los workflows críticos deben tener protección adecuada mediante:

```text
integration

security

browser

realtime
```

según corresponda.

---

# 925. Pre-1.0 Operations Rule

Deployment y recovery no deben depender exclusivamente de:

```text
maintainer memory.
```

---

# 926. Pre-1.0 Documentation Rule

Las boundaries críticas deben estar reflejadas en documentación vigente.

---

# 927. Pre-1.0 Architecture Rule

No se exige:

```text
zero technical debt.
```

---

# 928. Required State

Se exige:

```text
no unmanaged debt capable of undermining
the promises represented by 1.0.
```

---

# 929. Pre-Live-Kanban Debt Gate

Antes de Live Kanban revisar:

```text
TD-001

TD-002

TD-003

TD-004

TD-006

TD-007

TD-008

TD-009

TD-010

TD-021

TD-022
```

---

# 930. Live Kanban Security Gate

```text
[ ] Project membership authoritative.

[ ] Task access project-scoped.

[ ] Status mutation authorized.

[ ] WebSocket subscription authorized.

[ ] Browser mutation CSRF-safe.

[ ] Cross-project events isolated.
```

---

# 931. Live Kanban Realtime Gate

```text
[ ] Event contract stable.

[ ] Task update event defined.

[ ] Reconnect strategy defined.

[ ] Authoritative reconciliation defined.

[ ] Duplicate behavior safe.

[ ] Ordering requirements understood.

[ ] Multi-client convergence tested.
```

---

# 932. Live Kanban UI Gate

```text
[ ] Pending mutation state exists.

[ ] Failed mutation recovers safely.

[ ] Realtime update does not duplicate cards.

[ ] Stale board can reconcile.

[ ] Keyboard alternative exists.

[ ] Focus behavior remains usable.
```

---

# 933. Pre-Inventory Debt Gate

Antes de Inventory revisar:

```text
Project authorization

database constraints

audit integration

pagination patterns

attachment/storage implications
```

según diseño final.

---

# 934. Pre-PWA Debt Gate

Antes de offline/PWA capabilities revisar:

```text
session behavior

cache policy

authorization-sensitive caching

offline mutation semantics

state reconciliation

version invalidation
```

---

# 935. PWA Warning

Offline capability puede transformar deuda previamente pequeña en:

```text
distributed state consistency problem.
```

---

# 936. Pre-AI/RAG Debt Gate

Antes de introducir AI/RAG revisar:

```text
authorization

document access

data classification

auditability

retrieval isolation

prompt/input handling

evaluation

observability
```

---

# 937. AI/RAG Security Principle

```text
The model must never become
an authorization bypass.
```

---

# 938. Retrieval Principle

RAG retrieval debe aplicar:

```text
the same or stronger access boundaries
as direct resource access.
```

---

# 939. AI Debt Guardrail

No introducir una AI abstraction compleja antes de disponer de:

```text
concrete use case

evaluation criteria

data boundaries.
```

---

# 940. Technical Debt Governance Roles

Mientras Aula Robótica Platform mantenga una estructura pequeña:

```text
Maintainer
```

puede asumir ownership general.

---

# 941. Future Governance

Si aumenta el equipo, ownership puede distribuirse por:

```text
Backend

Frontend

Security

Platform

Data

Realtime
```

---

# 942. Owner Responsibility

El owner debe:

```text
understand debt

review trigger

track risk

promote remediation when required.
```

---

# 943. Owner Does Not Mean Sole Implementer

La implementación puede involucrar:

```text
multiple contributors.
```

---

# 944. Maintainer Responsibility

El maintainer debe garantizar:

```text
consistent classification

priority coherence

release review

historical traceability.
```

---

# 945. Contributor Responsibility

Un contributor que detecte deuda debería:

```text
describe evidence

identify scope

avoid speculative solution

raise it for classification.
```

---

# 946. Code Reviewer Responsibility

El reviewer debe comprobar:

```text
whether new compromise is intentional

whether it needs registration

whether existing debt is compounded.
```

---

# 947. Release Reviewer Responsibility

Debe comprobar:

```text
whether release assumptions conflict with accepted debt.
```

---

# 948. Architecture Review Responsibility

Debe comprobar:

```text
whether debt clusters reveal boundary problems.
```

---

# 949. Security Review Responsibility

Debe comprobar:

```text
whether accepted security assumptions remain valid.
```

---

# 950. Debt Governance Cadence

Una cadencia razonable puede ser:

```text
continuous discovery

weekly P0/P1 awareness

release review

milestone review

pre-1.0 full review
```

---

# 951. Continuous Discovery

Durante trabajo normal:

```text
record meaningful structural compromises.
```

---

# 952. Weekly Awareness

No requiere reunión formal.

Puede consistir en revisar:

```text
P0

P1

BLOCKED

IN_PROGRESS
```

---

# 953. Release Review

Debe comprobar:

```text
release safety

new debt

resolved debt

trigger crossings.
```

---

# 954. Milestone Review

Debe analizar clusters y roadmap dependencies.

---

# 955. Full Review

Antes de:

```text
1.0
```

revisar todas las entries activas.

---

# 956. Technical Debt Register Maintenance

La tabla resumen debe permanecer:

```text
current

concise

actionable.
```

---

# 957. Active Register

Debe incluir principalmente:

```text
non-resolved entries.
```

---

# 958. Resolved Register

Debe preservar:

```text
historical traceability.
```

---

# 959. Recommended Active Register Structure

```markdown
## Active Technical Debt

| ID | Title | Category | Severity | Priority | Interest | Status | Owner | Trigger |
|---|---|---|---|---|---|---|---|---|
| TD-001 | ... | SECURITY | S1 | P1 | COMPOUNDING | PRIORITIZED | Maintainer | Before ... |
```

---

# 960. Recommended Resolved Register Structure

```markdown
## Resolved Technical Debt

| ID | Title | Category | Resolved | Release |
|---|---|---|---|---|
| TD-XXX | ... | SECURITY | YYYY-MM-DD | X.Y.Z |
```

---

# 961. Detailed Entry Placement

Tras el summary register:

```text
Security Debt

Realtime Debt

Testing Debt

Architecture Debt

Database Debt

Performance Debt

Frontend Debt

Observability Debt

Operations Debt

DX Debt

Documentation Debt
```

---

# 962. Alternative Ordering

Si priority management resulta más útil:

```text
P0

P1

P2

P3
```

puede utilizarse para el resumen.

---

# 963. Recommended Approach

Mantener:

```text
summary ordered by priority

details grouped by category.
```

---

# 964. Why

Combina:

```text
execution visibility

+

architectural readability.
```

---

# 965. Debt Entry Metadata Standard

Para entries completas utilizar:

```markdown
**Status:**  
**Category:**  
**Related Areas:**  
**Severity:**  
**Priority:**  
**Debt Interest:**  
**Owner:**  
**Origin:**  
**Review:**  
```

---

# 966. Required Metadata

Como mínimo:

```text
Status

Category

Severity

Priority

Owner
```

---

# 967. Recommended Metadata

Para S1:

```text
Debt Interest

Origin

Review

Trigger
```

también deberían existir.

---

# 968. Debt Review History

Puede añadirse solo cuando aporta trazabilidad significativa.

---

# 969. Resolution Metadata

Para resueltas:

```text
Resolved

Release

Evidence
```

---

# 970. Source-of-truth Principle

`56_TECHNICAL_DEBT.md` debe ser la fuente canónica para:

```text
structural engineering compromises.
```

---

# 971. Do Not Duplicate Full Entries

Otros documentos deberían:

```text
reference TD IDs
```

en lugar de copiar toda la descripción.

---

# 972. Current Tasks Reference

Ejemplo:

```markdown
Related Technical Debt:

- TD-007
- TD-008
```

---

# 973. Known Issues Reference

Ejemplo:

```markdown
Root Technical Debt:

- TD-008
```

---

# 974. ADR Reference

Ejemplo:

```markdown
Addresses:

- TD-002
```

---

# 975. Changelog Reference

El Changelog puede omitir IDs en texto público si no aportan valor.

---

# 976. Internal Traceability

Puede conservarse referencia interna cuando sea útil.

---

# 977. Technical Debt and Versioning

Resolver deuda puede justificar:

```text
PATCH

MINOR

or

MAJOR
```

dependiendo del cambio observable.

---

# 978. PATCH Example

```text
internal query optimization
without behavior change
```

---

# 979. MINOR Example

```text
new security/session capability
introduced compatibly
```

---

# 980. MAJOR Example

Solo si remediation introduce:

```text
intentional incompatible contract change
```

en una interfaz versionada estable.

---

# 981. Debt Does Not Determine Version Alone

SemVer depende de:

```text
public compatibility impact.
```

---

# 982. Technical Debt and Changelog Categories

La remediation puede aparecer como:

```text
Changed

Fixed

Security

Performance
```

según outcome.

---

# 983. Security Remediation

Cuando sea relevante:

```text
Security
```

debe comunicar el resultado sin exponer detalles explotables innecesarios.

---

# 984. Technical Debt and Product Roadmap

El roadmap puede incluir iniciativas como:

```text
Security Hardening

Realtime Reliability

Production Readiness
```

---

# 985. Roadmap Abstraction

No debería contener:

```text
every TD identifier.
```

---

# 986. Backlog Integration

El backlog puede contener tareas derivadas de Technical Debt.

---

# 987. Separation

```text
Technical Debt

→ why structural remediation matters


Backlog / Current Task

→ what work will be executed
```

---

# 988. Technical Debt and Weekly Update

El Weekly Update puede mencionar:

```text
major debt discovered

major debt resolved

risk escalation

hardening initiative progress.
```

---

# 989. Weekly Update Guardrail

No convertirlo en:

```text
Technical Debt status dump.
```

---

# 990. Technical Debt and Coding Rules

Cuando una remediation descubre una regla reusable:

```text
51_CODING_RULES.md
```

debe actualizarse.

---

# 991. Example Rule

Tras TD-001:

```text
Project-scoped authorization must use canonical contextual policies.
```

---

# 992. Example Rule

Tras TD-007:

```text
Realtime events must use the canonical versioned event envelope.
```

---

# 993. Example Rule

Tras TD-014:

```text
High-growth collection endpoints must use bounded retrieval.
```

---

# 994. Technical Debt and Architectural Decisions

`52_ARCHITECTURAL_DECISIONS.md` debe registrar:

```text
stable decision
```

cuando remediation cambie una boundary importante.

---

# 995. Technical Debt and Current Tasks

`53_CURRENT_TASKS.md` debe representar:

```text
selected remediation work.
```

---

# 996. Technical Debt and Known Issues

`54_KNOWN_ISSUES.md` debe representar:

```text
observable symptoms or limitations.
```

---

# 997. Technical Debt and Changelog

`55_CHANGELOG.md` debe representar:

```text
delivered remediation outcome.
```

---

# 998. Governance Chain

```text
Technical Debt
      ↓
Prioritization
      ↓
Current Task
      ↓
Architectural Decision
   when required
      ↓
Implementation
      ↓
Testing
      ↓
Known Issue resolution
   when applicable
      ↓
Changelog
      ↓
Technical Debt RESOLVED
```

---

# 999. Technical Debt Quality Indicators

Una gestión madura muestra:

```text
few unmanaged high-risk items

clear ownership

clear triggers

risk-based prioritization

evidence-based remediation

historical traceability.
```

---

# 1000. Poor Debt Governance Indicators

```text
hundreds of vague TODOs

no owner

no severity

no triggers

permanent accepted S1 debt

rewrites without evidence

technology-driven remediation

debt closed without validation.
```

---

# 1001. Healthy Architecture Indicator

Una arquitectura sana no es una arquitectura sin deuda.

---

# 1002. Better Definition

Es una arquitectura donde:

```text
known compromises remain understandable,
bounded,
and reversible.
```

---

# 1003. Reversibility Principle

Las decisiones temporales deberían intentar preservar:

```text
future changeability.
```

---

# 1004. Example

Local Attachment storage puede ser simple hoy si:

```text
storage concerns remain sufficiently isolated
```

para permitir sustitución futura.

---

# 1005. Another Example

Single-process WebSocket management puede ser correcto si:

```text
domain events are not deeply coupled
to process-local implementation details.
```

---

# 1006. Another Example

SSR puede continuar siendo adecuado si:

```text
client-side complexity remains bounded.
```

---

# 1007. Technical Debt and Simplicity

Simplicity es una herramienta de reducción de deuda.

---

# 1008. But

Simplicity no significa:

```text
ignore required structure.
```

---

# 1009. Correct Balance

```text
Simple where possible.

Explicit where necessary.

Structured where risk demands it.
```

---

# 1010. Technical Debt and Security

Security boundaries deben favorecer:

```text
explicitness
```

sobre:

```text
implicit convenience.
```

---

# 1011. Technical Debt and Data

Data integrity debe favorecer:

```text
enforced invariants
```

sobre:

```text
developer assumptions.
```

---

# 1012. Technical Debt and Realtime

Realtime debe favorecer:

```text
eventual authoritative convergence
```

sobre:

```text
assuming perfect delivery.
```

---

# 1013. Technical Debt and Testing

Testing debe favorecer:

```text
risk protection
```

sobre:

```text
coverage vanity.
```

---

# 1014. Technical Debt and Performance

Performance debe favorecer:

```text
measurement
```

sobre:

```text
intuition.
```

---

# 1015. Technical Debt and Observability

Observability debe favorecer:

```text
diagnostic usefulness
```

sobre:

```text
telemetry volume.
```

---

# 1016. Technical Debt and Operations

Operations debe favorecer:

```text
tested recovery
```

sobre:

```text
documented optimism.
```

---

# 1017. Technical Debt and Documentation

Documentation debe favorecer:

```text
maintainable knowledge
```

sobre:

```text
maximum document volume.
```

---

# 1018. Technical Debt and Architecture

Architecture debe favorecer:

```text
clear boundaries

low accidental coupling

incremental evolution
```

sobre:

```text
architectural fashion.
```

---

# 1019. Technical Debt and Product Development

Product delivery y engineering quality no deben tratarse como objetivos opuestos.

---

# 1020. Better Model

```text
Product work creates learning.

Engineering work preserves the ability
to continue learning safely.
```

---

# 1021. Strategic Debt Principle

Puede aceptarse deuda para aprender más rápido cuando:

```text
scope is bounded

risk is controlled

future trigger is known.
```

---

# 1022. Example

Una implementación simple de Attachment storage puede ser apropiada para validar:

```text
actual attachment usage.
```

---

# 1023. Wrong Strategic Debt

No aceptar conscientemente:

```text
broken authorization
```

para acelerar una feature collaborative.

---

# 1024. Non-negotiable Boundaries

Algunas áreas requieren mayor rigor:

```text
security

data integrity

recoverability

privacy.
```

---

# 1025. Debt Priority Principle

```text
Prioritize debt by risk and dependency,
not by developer annoyance alone.
```

---

# 1026. Debt Interest Principle

```text
Repay compounding debt
before building many features on top of it.
```

---

# 1027. Debt Evidence Principle

```text
Measure before optimizing.

Threat-model before security redesign.

Test before declaring reliability.

Restore before trusting backup.
```

---

# 1028. Debt Ownership Principle

```text
Every significant debt needs someone
responsible for ensuring it is not forgotten.
```

---

# 1029. Debt Trigger Principle

```text
Every deferred significant debt should have
a condition that ends the deferral.
```

---

# 1030. Debt Resolution Principle

```text
Resolve the structural cause,
not only the latest symptom.
```

---

# 1031. Debt Validation Principle

```text
A refactor is not debt repayment
until the original risk is demonstrably reduced.
```

---

# 1032. Debt History Principle

```text
Resolved debt remains useful engineering history.
```

---

# 1033. Debt Prevention Principle

```text
The cheapest debt to repay
is unnecessary debt never introduced.
```

---

# 1034. Architecture Evolution Principle

```text
Evolve architecture when requirements demand it,
not when a more fashionable architecture becomes available.
```

---

# 1035. Platform-specific Priority

Para Aula Robótica Platform, el foco principal debe mantenerse en:

```text
secure collaboration

reliable realtime behavior

data integrity

testable boundaries

recoverable operations

maintainable modular architecture.
```

---

# 1036. Current Strategic Debt Clusters

Los principales clusters identificados son:

```text
Security Hardening

Realtime Reliability

Testing Maturity

Production Readiness
```

---

# 1037. Security Hardening Cluster

Incluye principalmente:

```text
TD-001

TD-002

TD-003

TD-004

TD-005

TD-006
```

---

# 1038. Realtime Reliability Cluster

Incluye:

```text
TD-007

TD-008

TD-009

TD-010
```

---

# 1039. Testing Maturity Cluster

Incluye principalmente:

```text
TD-010

TD-011

TD-022
```

---

# 1040. Production Readiness Cluster

Incluye principalmente:

```text
TD-017

TD-018

TD-019

TD-020

TD-023

TD-024
```

---

# 1041. Data and Performance Cluster

Incluye:

```text
TD-013

TD-014

TD-015
```

---

# 1042. Architecture Evolution Cluster

Incluye principalmente:

```text
TD-012

TD-016
```

junto con cualquier deuda futura derivada de cambios reales de escala.

---

# 1043. Frontend Reliability Cluster

Incluye:

```text
TD-011

TD-021

TD-022
```

---

# 1044. Recommended Strategic Order

```text
1. Secure collaboration boundaries

2. Consolidate realtime reliability

3. Protect critical workflows with tests

4. Validate recovery and production operations

5. Optimize measured persistence/performance issues

6. Improve developer and documentation ergonomics
```

---

# 1045. Strategic Guardrail

Este orden no debe impedir resolver inmediatamente:

```text
new critical security

data

or

production risk.
```

---

# 1046. Recommended Final Document Structure

La versión consolidada de `56_TECHNICAL_DEBT.md` debería mantener:

```text
1. Purpose

2. Scope

3. Debt Definition

4. Debt vs Other Governance Artifacts

5. Categories

6. Severity

7. Priority

8. Lifecycle

9. Risk Model

10. Debt Interest

11. Ownership

12. Entry Template

13. Active Debt Register

14. Detailed Debt Entries

15. Dependency Map

16. Remediation Workflow

17. Scoring Model

18. Debt Budget

19. Review Process

20. Architecture Integration

21. Security Integration

22. Testing Integration

23. Release Integration

24. Debt Prevention

25. Resolution Evidence

26. Anti-patterns

27. Domain Checklists

28. Definition of Ready

29. Definition of Done

30. Release Gate

31. Pre-Production Gate

32. Pre-1.0 Gate

33. Governance

34. Final Principles
```

---

# 1047. Document Maintenance Rule

No es necesario conservar esta numeración exhaustiva si posteriormente se reorganiza el documento.

---

# 1048. Content Rule

Sí deben conservarse:

```text
conceptual boundaries

register traceability

governance rules

acceptance criteria

risk-based prioritization.
```

---

# 1049. Register Maintenance Rule

Cuando se añada nueva deuda:

```text
1. assign new TD ID

2. classify

3. assess severity

4. assess priority

5. assign owner

6. define trigger

7. add summary entry

8. add detailed entry when warranted
```

---

# 1050. Resolution Maintenance Rule

Cuando se resuelva:

```text
1. validate acceptance criteria

2. record evidence

3. update related Current Task

4. update Known Issues if applicable

5. update ADR if applicable

6. update documentation

7. update Changelog

8. mark RESOLVED

9. move to historical register when appropriate
```

---

# 1051. Auditability

El documento debe permitir reconstruir:

```text
what compromise existed

why it was accepted

when it became important

how it was resolved.
```

---

# 1052. Technical Debt Governance Statement

Aula Robótica Platform acepta que:

```text
technical debt is a normal consequence
of iterative software development.
```

---

# 1053. However

La plataforma no acepta:

```text
unmanaged structural risk

as a normal operating model.
```

---

# 1054. Final Engineering Position

Technical Debt debe tratarse como:

```text
explicit engineering risk
```

y no como:

```text
a vague list of code imperfections.
```

---

# 1055. Final Architecture Position

La arquitectura debe evolucionar mediante:

```text
evidence

requirements

risk

incremental improvement.
```

---

# 1056. Final Security Position

La seguridad debe mantener:

```text
server-controlled identity

explicit authorization

resource isolation

secure session boundaries

tested negative paths.
```

---

# 1057. Final Realtime Position

Realtime debe asumir:

```text
connections fail

messages may be missed

duplicates may occur

clients can become stale.
```

---

# 1058. Therefore

La arquitectura realtime debe priorizar:

```text
authorization

reconnection

reconciliation

idempotency

observable behavior

multi-client testing.
```

---

# 1059. Final Database Position

La persistencia debe proteger:

```text
domain invariants

data integrity

bounded access

recoverability.
```

---

# 1060. Final Testing Position

La estrategia de testing debe proteger:

```text
critical behavior

trust boundaries

integration contracts

collaborative workflows.
```

---

# 1061. Final Performance Position

La optimización debe seguir:

```text
measure

↓

understand

↓

optimize

↓

measure again.
```

---

# 1062. Final Observability Position

La plataforma debe poder explicar:

```text
what happened

where

when

for which operation

and

with what outcome
```

sin comprometer información sensible.

---

# 1063. Final Operations Position

Production readiness requiere:

```text
deployment

detection

recovery

restore

repeatability.
```

---

# 1064. Final Documentation Position

La documentación debe preservar:

```text
decisions

boundaries

critical procedures

engineering rationale.
```

---

# 1065. Final Simplicity Position

```text
Simplicity is preferred
until requirements justify complexity.
```

---

# 1066. Final Complexity Rule

Toda nueva complejidad debería poder responder:

```text
Which concrete problem does this solve?
```

---

# 1067. Final Debt Rule

Toda deuda significativa debería poder responder:

```text
What compromise exists?

Why is it acceptable now?

What risk does it create?

What ends that acceptance?

How will we know it is resolved?
```

---

# 1068. Final Governance Rule

```text
Known debt may remain.

Unknown debt should be discovered.

Unowned debt should be assigned.

Compounding debt should be prioritized.

Critical debt should not be normalized.
```

---

# 1069. Final Platform Rule

```text
Do not optimize Aula Robótica Platform
for hypothetical architectural prestige.

Optimize it for secure,
reliable,
maintainable,
observable,
and evolvable product delivery.
```

---

# 1070. Final Technical Debt Statement

```text
Technical debt is not the opposite of good engineering.

Unmanaged technical debt is.

Aula Robótica Platform may intentionally accept
bounded technical compromises when they support
incremental product delivery and learning.

Those compromises must remain visible,
owned,
reviewable,
testable,
and reversible.

Security, data integrity, recoverability,
and collaboration boundaries receive stricter treatment
because failure in those areas can invalidate
the trustworthiness of the platform itself.

The objective is therefore not zero debt.

The objective is controlled architectural evolution
with no unmanaged structural risk capable of
silently becoming permanent.
```

---

# 1071. Document Status

```text
Status: Living Document

Scope: Platform-wide Technical Debt Governance

Primary Owner: Maintainer

Review Triggers:
- major architecture changes
- security hardening
- realtime expansion
- production-readiness work
- major releases
- pre-1.0 review
```

---

# 1072. Related Documentation

```text
44_TESTING_STRATEGY.md

45_UI_TESTING.md

46_REALTIME_TESTING.md

47_PRODUCT_ROADMAP.md

48_PRODUCT_VISION.md

49_FEATURE_BACKLOG.md

50_WEEKLY_UPDATE.md

51_CODING_RULES.md

52_ARCHITECTURAL_DECISIONS.md

53_CURRENT_TASKS.md

54_KNOWN_ISSUES.md

55_CHANGELOG.md

36_MONITORING.md

37_LOGGING.md

38_OBSERVABILITY.md
```

---

# 1073. Final Status

```text
56_TECHNICAL_DEBT.md

Detailed Professional Version

Complete
```
