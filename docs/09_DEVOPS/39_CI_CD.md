# 39_CI_CD.md

# 🚀 Integración Continua y Despliegue Continuo (CI/CD)

---

# 📌 Introducción

La estrategia de **Integración Continua (Continuous Integration, CI)** y **Despliegue Continuo (Continuous Deployment, CD)** constituye uno de los pilares fundamentales del proceso de desarrollo de Aula Robótica Platform.

Su incorporación permite automatizar gran parte del ciclo de vida del software, garantizando que cada modificación del código fuente sea validada de forma sistemática antes de incorporarse al proyecto.

La automatización reduce significativamente la posibilidad de introducir errores, mejora la calidad del código y facilita la evolución continua de la aplicación.

En Aula Robótica Platform esta estrategia se implementa mediante **GitHub Actions**, integrando herramientas de análisis estático, testing automatizado y validación de calidad antes del despliegue sobre la infraestructura cloud.

---

# 🎯 Objetivos

La estrategia CI/CD persigue varios objetivos complementarios.

## Objetivos funcionales

- automatizar la validación del software;
- detectar errores tempranamente;
- garantizar estabilidad del proyecto;
- facilitar despliegues repetibles;
- mejorar la productividad del desarrollo.

---

## Objetivos técnicos

- automatizar pipelines;
- integrar testing continuo;
- ejecutar análisis estático;
- verificar cobertura;
- validar calidad del código;
- preparar despliegues cloud;
- reducir intervención manual.

---

# 🧠 Filosofía DevOps

La estrategia adoptada sigue los principios fundamentales de DevOps.

El objetivo no consiste únicamente en automatizar tareas, sino en integrar desarrollo, validación y despliegue dentro de un proceso continuo.

Cada cambio realizado sobre el repositorio desencadena automáticamente un conjunto de validaciones que garantizan que el proyecto continúa siendo estable.

Esta filosofía aporta:

- mayor confianza;
- entregas frecuentes;
- reducción de errores;
- mejor mantenibilidad;
- evolución continua.

---

# ¿Qué es la Integración Continua?

La Integración Continua consiste en incorporar pequeños cambios al repositorio de forma frecuente.

Cada integración activa automáticamente un pipeline encargado de validar el estado completo del proyecto.

De esta forma los problemas aparecen inmediatamente después de introducirse, reduciendo enormemente el coste de corregirlos.

---

# ¿Qué es el Despliegue Continuo?

El Despliegue Continuo representa el siguiente paso dentro del ciclo DevOps.

Una vez superadas todas las validaciones automáticas, el software puede desplegarse de forma repetible sobre un entorno controlado.

En Aula Robótica Platform el despliegue se realiza actualmente sobre un VPS Linux utilizando Docker Compose y Nginx.

Aunque el despliegue continúa siendo supervisado, la arquitectura queda preparada para automatizar este proceso en futuras versiones.

---

# Beneficios de CI/CD

La incorporación de CI/CD aporta ventajas tanto durante el desarrollo como en explotación.

Entre las principales destacan:

- reducción de errores;
- detección temprana de incidencias;
- automatización del proceso de validación;
- despliegues repetibles;
- mejora continua;
- mayor calidad del software;
- reducción del trabajo manual.

---

# Arquitectura General

La estrategia CI/CD se integra con el flujo general de desarrollo del proyecto.

```mermaid
flowchart LR

Developer

--> GitHub

GitHub

--> GitHub Actions

GitHub Actions

--> Ruff

GitHub Actions

--> Pytest

GitHub Actions

--> Coverage

GitHub Actions

--> SonarCloud

SonarCloud

--> Quality Gate

Quality Gate

--> Docker Deployment
```

---

# Flujo General del Pipeline

Cada modificación del código sigue una secuencia claramente definida.

```mermaid
flowchart TD

Commit

--> Push

Push

--> Workflow

Workflow

--> Instalación Dependencias

--> Ruff

--> Pytest

--> Coverage

--> SonarCloud

--> Resultado
```

Este flujo garantiza que únicamente el código validado pueda avanzar hacia fases posteriores del ciclo de desarrollo.

---

# Eventos que Activan la Integración Continua

GitHub Actions puede ejecutar automáticamente los pipelines como respuesta a distintos eventos del repositorio.

Entre los más habituales:

- push;
- pull request;
- merge;
- ejecución manual;
- programación periódica.

La automatización evita depender de ejecuciones manuales por parte del desarrollador.

---

# Pipeline como Código

Toda la definición del pipeline forma parte del propio repositorio.

Esto proporciona varias ventajas:

- versionado;
- trazabilidad;
- revisión mediante pull requests;
- reproducibilidad;
- colaboración.

La configuración permanece almacenada junto al resto del código fuente.

---

# Componentes Principales del Pipeline

La estrategia CI integra distintas herramientas especializadas.

| Componente | Responsabilidad |
|------------|-----------------|
| GitHub | Gestión del código fuente |
| GitHub Actions | Automatización del pipeline |
| Ruff | Linting |
| Pytest | Testing |
| Coverage | Cobertura de código |
| SonarCloud | Calidad software |
| Docker | Preparación del despliegue |

Cada herramienta aporta una validación diferente dentro del proceso global.

---

# Integración con el Flujo de Desarrollo

El pipeline forma parte del flujo habitual de trabajo del desarrollador.

```text
Modificar código

↓

Commit

↓

Push

↓

GitHub Actions

↓

Validaciones automáticas

↓

Corrección de errores

↓

Merge
```

Gracias a este modelo, la calidad del proyecto se controla de forma continua y no únicamente al finalizar el desarrollo de una funcionalidad.

---

# Integración con Git

La estrategia CI se encuentra estrechamente integrada con el sistema de control de versiones.

Cada commit representa una unidad de trabajo que puede ser validada automáticamente.

Esto permite detectar rápidamente el commit responsable de una incidencia cuando alguna validación falla.

---

# Integración con Docker

La evolución reciente del proyecto ha permitido integrar la estrategia CI con la infraestructura Docker utilizada durante el despliegue.

Aunque actualmente el despliegue sobre el VPS continúa siendo supervisado, la arquitectura ya está preparada para automatizar completamente la generación de imágenes Docker y su despliegue en futuras versiones.

Esta separación facilita mantener un pipeline único para validación y otro específico para despliegue.

---

# Integración con SonarCloud

Uno de los elementos más importantes del pipeline es la incorporación de SonarCloud como herramienta de análisis estático.

SonarCloud complementa los tests automáticos evaluando aspectos que no pueden detectarse únicamente mediante testing funcional.

Entre ellos:

- mantenibilidad;
- duplicación;
- complejidad;
- code smells;
- cobertura;
- calidad global.

El uso de **Quality Gates** impide que cambios con problemas importantes avancen dentro del proceso de integración.

---

# Preparación para DevOps

La arquitectura actual deja preparada la evolución hacia una estrategia DevOps más completa.

La automatización existente permite incorporar posteriormente:

- despliegues automáticos;
- generación de imágenes Docker;
- publicación en registros;
- despliegues por entornos;
- monitorización;
- rollback automático.

La separación entre integración continua y despliegue facilita realizar esta evolución sin modificar la estructura general del proyecto.

---

# 🧪 Estrategia de Validación

La Integración Continua implementada en Aula Robótica Platform no se limita a ejecutar pruebas automatizadas.

El pipeline combina diferentes mecanismos de validación que permiten evaluar múltiples aspectos del software antes de aceptar cualquier modificación en el repositorio.

Cada herramienta aporta información complementaria sobre la calidad del proyecto.

---

# Arquitectura de Validación

```mermaid
flowchart TD

Código Fuente

--> Ruff

Código Fuente

--> Pytest

Código Fuente

--> Coverage

Código Fuente

--> SonarCloud

Ruff --> Resultado

Pytest --> Resultado

Coverage --> Resultado

SonarCloud --> Resultado

Resultado

--> Quality Gate
```

---

# Linting

El primer nivel de validación corresponde al análisis estático del código.

Su objetivo consiste en detectar:

- errores sintácticos;
- incumplimiento del estilo;
- importaciones innecesarias;
- código redundante;
- posibles problemas de mantenimiento.

La detección temprana de este tipo de incidencias reduce considerablemente la aparición de errores posteriores.

---

# Testing Automatizado

Tras superar el análisis estático, el pipeline ejecuta la batería completa de pruebas automatizadas.

Estas pruebas verifican el correcto funcionamiento de:

- servicios;
- modelos;
- endpoints;
- autenticación;
- autorización;
- lógica de negocio.

Cada modificación queda validada automáticamente antes de poder integrarse en la rama principal.

---

# Cobertura de Código

La cobertura constituye uno de los indicadores utilizados para medir el grado de validación automática del proyecto.

Durante la ejecución del pipeline se calcula el porcentaje de líneas ejecutadas por los tests.

En la versión actual del proyecto:

- cobertura real aproximada: **75 %**
- cobertura registrada por SonarCloud: **73,7 %**

La diferencia se debe al método de cálculo empleado por ambas herramientas.

---

# Quality Gates

Uno de los aspectos más importantes del pipeline es la utilización de **Quality Gates**.

Un Quality Gate representa un conjunto de condiciones que el proyecto debe cumplir antes de considerarse válido.

Entre los indicadores evaluados pueden encontrarse:

- cobertura mínima;
- ausencia de errores críticos;
- complejidad aceptable;
- duplicación reducida;
- mantenibilidad.

Si alguna condición no se cumple, el pipeline finaliza con error.

---

# Flujo de Validación

```mermaid
flowchart LR

Código

--> Ruff

Ruff

--> Pytest

Pytest

--> Coverage

Coverage

--> SonarCloud

SonarCloud

--> Quality Gate

Quality Gate

--> Pipeline Correcto
```

---

# SonarCloud

SonarCloud constituye la herramienta principal para el análisis avanzado de calidad.

Complementa las pruebas funcionales incorporando métricas relacionadas con:

- mantenibilidad;
- fiabilidad;
- seguridad;
- duplicación;
- complejidad;
- deuda técnica.

Este análisis permite detectar problemas que normalmente no aparecen durante la ejecución de los tests.

---

# Métricas Analizadas

Entre las métricas principales evaluadas destacan:

| Métrica | Objetivo |
|----------|----------|
| Bugs | detectar errores potenciales |
| Vulnerabilities | identificar problemas de seguridad |
| Code Smells | mejorar mantenibilidad |
| Coverage | validar pruebas |
| Duplications | reducir código repetido |
| Maintainability | facilitar evolución |

---

# Calidad del Código

La calidad software no depende exclusivamente del correcto funcionamiento de la aplicación.

También resulta importante mantener:

- arquitectura limpia;
- bajo acoplamiento;
- alta cohesión;
- complejidad controlada;
- nomenclatura consistente;
- ausencia de duplicación.

El pipeline ayuda a mantener estos criterios de forma automática.

---

# Gestión de Errores

Cuando alguna validación falla, GitHub Actions interrumpe inmediatamente la ejecución del pipeline.

Esto evita:

- integrar código defectuoso;
- desplegar versiones inestables;
- aumentar la deuda técnica;
- introducir regresiones.

El desarrollador recibe información detallada sobre el origen del problema para facilitar su resolución.

---

# Validación de Pull Requests

Uno de los escenarios más importantes consiste en la validación automática de Pull Requests.

Antes de aceptar una integración se ejecutan nuevamente todas las comprobaciones del pipeline.

De esta forma únicamente las ramas que superan todas las validaciones pueden incorporarse al proyecto principal.

---

# Beneficios para el Equipo

La automatización del pipeline aporta ventajas importantes durante el desarrollo colaborativo.

Entre ellas:

- criterios homogéneos;
- reducción de errores humanos;
- integración frecuente;
- menor tiempo de revisión;
- mayor confianza en los cambios.

---

# Integración con Docker

La estrategia CI queda preparada para integrarse con la infraestructura Docker utilizada durante el despliegue.

En futuras versiones el pipeline podrá incorporar automáticamente:

- construcción de imágenes;
- etiquetado de versiones;
- publicación en registros;
- validación de contenedores.

Esto permitirá automatizar completamente el ciclo de construcción.

---

# Preparación para Continuous Deployment

Aunque actualmente el despliegue sobre el VPS continúa realizándose de forma supervisada, la arquitectura se encuentra preparada para evolucionar hacia un modelo de Continuous Deployment.

El flujo previsto sería:

```mermaid
flowchart TD

Commit

--> CI

CI

--> Quality Gate

Quality Gate

--> Build Docker

Build Docker

--> Docker Registry

Docker Registry

--> VPS

VPS

--> Docker Compose

Docker Compose

--> Aplicación Desplegada
```

---

# Integración con la Infraestructura Cloud

La evolución del proyecto hacia un entorno desplegado sobre Hetzner Cloud permite conectar la fase de integración continua con el despliegue sobre una infraestructura Linux real.

Esta separación entre validación y despliegue facilita:

- despliegues repetibles;
- reducción de riesgos;
- recuperación rápida;
- futuras automatizaciones.

---

# Beneficios Globales

La estrategia CI/CD implementada aporta numerosos beneficios al ciclo de vida del software.

Entre los más relevantes destacan:

- validación continua;
- calidad objetiva;
- automatización;
- reducción de errores;
- mejora de la mantenibilidad;
- integración con Docker;
- preparación para despliegues automáticos;
- alineación con prácticas DevOps modernas.

---

# Estado Actual

Actualmente la estrategia de integración continua incorpora:

✅ GitHub Actions.

✅ Ruff.

✅ Pytest.

✅ Coverage.

✅ SonarCloud.

✅ Quality Gates.

✅ Validación automática.

✅ Integración con Docker.

✅ Preparación para despliegue cloud.

---

# ☁️ Estrategia de Despliegue Continuo

La estrategia de **Continuous Deployment (CD)** constituye la evolución natural del proceso de Integración Continua implantado en Aula Robótica Platform.

Mientras que la Integración Continua garantiza que cada modificación del código cumple los estándares de calidad definidos, el Despliegue Continuo persigue automatizar la publicación de nuevas versiones sobre la infraestructura de producción o preproducción.

Actualmente el proyecto utiliza un modelo de **despliegue supervisado**, donde las validaciones son completamente automáticas y la publicación final sobre el VPS se realiza de forma controlada por el desarrollador.

Este enfoque proporciona un equilibrio adecuado entre automatización y control operativo.

---

# Arquitectura General del Despliegue

```mermaid
flowchart LR

Developer

--> GitHub

GitHub

--> GitHub Actions

GitHub Actions

--> Build

Build

--> Docker Image

Docker Image

--> Docker Compose

Docker Compose

--> VPS Ubuntu

VPS Ubuntu

--> Aplicación
```

---

# Integración con Docker

Docker constituye el elemento fundamental sobre el que se apoya la estrategia de despliegue.

La contenerización permite que el mismo entorno validado durante el proceso de integración pueda ejecutarse posteriormente en producción con un comportamiento idéntico.

Entre las ventajas obtenidas destacan:

- entornos reproducibles;
- aislamiento de dependencias;
- facilidad de actualización;
- despliegues consistentes;
- reducción de errores de configuración.

---

# Docker Compose

La orquestación de los servicios se realiza mediante Docker Compose.

Actualmente coordina los siguientes componentes:

| Servicio | Función |
|-----------|-------------------------|
| FastAPI | Aplicación backend |
| MariaDB | Persistencia |
| Nginx | Reverse Proxy |

Esta organización simplifica el despliegue y facilita futuras ampliaciones de la infraestructura.

---

# Relación entre CI y Docker

La arquitectura deja claramente diferenciadas dos fases.

## Continuous Integration

Valida:

- código;
- calidad;
- pruebas;
- cobertura;
- análisis estático.

---

## Continuous Deployment

Gestiona:

- construcción de imágenes;
- actualización de contenedores;
- despliegue;
- publicación.

Esta separación mejora considerablemente la mantenibilidad del proceso DevOps.

---

# Integración con Nginx

Una vez desplegada la aplicación, Nginx constituye el punto único de entrada a la infraestructura.

Entre sus responsabilidades destacan:

- recepción de peticiones HTTP;
- proxy hacia FastAPI;
- gestión de recursos estáticos;
- soporte WebSocket;
- preparación para HTTPS.

La integración entre Docker Compose y Nginx permite mantener desacoplados los distintos servicios de la plataforma.

---

# Infraestructura Cloud

El despliegue actual se realiza sobre una infraestructura cloud basada en:

- Hetzner Cloud;
- VPS Ubuntu Server;
- Docker;
- Docker Compose;
- Nginx;
- MariaDB persistente.

Esta infraestructura aproxima el proyecto a escenarios habituales de explotación utilizados en aplicaciones backend profesionales.

---

# Flujo Completo DevOps

```mermaid
flowchart TD

Código Fuente

--> GitHub

GitHub

--> GitHub Actions

GitHub Actions

--> Ruff

--> Pytest

--> Coverage

--> SonarCloud

SonarCloud

--> Quality Gate

Quality Gate

--> Docker Build

Docker Build

--> Docker Compose

Docker Compose

--> VPS Ubuntu

VPS Ubuntu

--> Plataforma Operativa
```

---

# Observabilidad del Pipeline

Uno de los beneficios del pipeline automatizado consiste en disponer de información detallada sobre cada ejecución.

Cada pipeline proporciona información relativa a:

- estado de ejecución;
- duración;
- pruebas ejecutadas;
- cobertura obtenida;
- errores detectados;
- artefactos generados.

Esta información facilita enormemente la detección de incidencias.

---

# Recuperación ante Errores

La automatización también simplifica la recuperación cuando alguna validación falla.

En función del punto donde se produzca el error, el proceso puede detenerse antes de afectar al resto de la infraestructura.

Esto evita:

- despliegues incompletos;
- versiones inestables;
- pérdida de consistencia;
- errores difíciles de reproducir.

---

# Buenas Prácticas Aplicadas

La estrategia CI/CD implementada sigue diversas recomendaciones ampliamente aceptadas dentro del desarrollo moderno.

Entre ellas destacan:

- automatización temprana;
- validaciones frecuentes;
- integración continua;
- separación entre construcción y despliegue;
- pipelines reproducibles;
- Infrastructure as Code;
- versionado del pipeline;
- despliegues controlados.

---

# Roadmap DevOps

La arquitectura actual deja preparada la incorporación progresiva de nuevas capacidades.

Entre ellas:

- publicación automática de imágenes Docker;
- Docker Registry;
- despliegues automáticos;
- múltiples entornos;
- staging;
- rollback automático;
- monitorización;
- observabilidad;
- despliegues blue-green;
- Kubernetes.

---

# Evolución Hacia Producción

La infraestructura implementada permite evolucionar hacia un entorno de producción completo incorporando:

- HTTPS mediante Let's Encrypt;
- balanceadores de carga;
- alta disponibilidad;
- escalado horizontal;
- Redis;
- monitorización Prometheus;
- Grafana;
- copias de seguridad automatizadas.

La arquitectura actual constituye una base sólida para estas futuras ampliaciones.

---

# Estado Actual

Actualmente Aula Robótica Platform dispone de una estrategia DevOps formada por:

✅ GitHub como repositorio principal.

✅ GitHub Actions como motor CI.

✅ Ruff para análisis estático.

✅ Pytest para testing automatizado.

✅ Coverage para medición de pruebas.

✅ SonarCloud para calidad software.

✅ Quality Gates automáticos.

✅ Docker como entorno de ejecución.

✅ Docker Compose como orquestador.

✅ Nginx como Reverse Proxy.

✅ VPS Ubuntu desplegado en Hetzner Cloud.

---

# Beneficios Obtenidos

La incorporación de CI/CD ha permitido:

- automatizar la validación del proyecto;
- aumentar la estabilidad del software;
- detectar errores de forma temprana;
- reducir el trabajo manual;
- mejorar la calidad del código;
- facilitar el despliegue;
- aproximar el proyecto a prácticas DevOps profesionales.

---

# 🔮 Evolución Futura

La estrategia actual deja preparada la evolución hacia un ciclo DevOps completamente automatizado.

Las principales líneas de evolución previstas incluyen:

- despliegue completamente automático;
- publicación de imágenes Docker;
- integración con registros privados;
- múltiples entornos de ejecución;
- observabilidad avanzada;
- despliegues progresivos;
- recuperación automática;
- escalado horizontal.

Estas mejoras podrán incorporarse sin modificar la arquitectura general del sistema gracias a la separación existente entre integración continua, despliegue e infraestructura.

---

# 📌 Conclusiones

La estrategia de Integración Continua y Despliegue Continuo implementada en Aula Robótica Platform constituye uno de los elementos que más contribuyen a la calidad global del proyecto.

La combinación de GitHub, GitHub Actions, Ruff, Pytest, Coverage, SonarCloud, Docker, Docker Compose y la infraestructura desplegada sobre Hetzner Cloud permite automatizar gran parte del ciclo de vida del software, reduciendo errores y aumentando la confianza en cada nueva versión.

Aunque el despliegue continúa realizándose de forma supervisada, la arquitectura ha sido diseñada para evolucionar hacia un modelo DevOps más avanzado, manteniendo una clara separación entre validación, construcción y publicación.

Esta aproximación proporciona una base sólida para futuras mejoras y acerca el proyecto a los procesos utilizados habitualmente en entornos profesionales de desarrollo backend y cloud.

