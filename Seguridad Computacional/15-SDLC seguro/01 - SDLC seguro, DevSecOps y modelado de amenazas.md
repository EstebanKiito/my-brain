---
ramo: "Seguridad Computacional"
tema: "SDLC seguro"
tags:
  - seguridad/sdlc
  - origen/apuntes
prerrequisitos:
  - "[[03 - Defensa en profundidad y seguridad imperfecta]]"
---

# SDLC seguro, DevSecOps y modelado de amenazas

La seguridad suele aparecer al último minuto del ciclo de vida del software. Un **SDLC seguro** la incluye en cada etapa: planificación (qué esperan los usuarios), análisis y diseño (cómo se hará), codificación, *testing* (identificar vulnerabilidades), despliegue y mantenimiento (monitoreo continuo).

## Vulnerabilidades comunes en el ciclo
- **Herramientas DevOps e infraestructura:** configuraciones por defecto priorizan velocidad y eficiencia, no seguridad.
- **Manipulación de código:** cambios no autorizados e inyección de código malicioso.
- **Prácticas inseguras:** credenciales expuestas, falta de validación (ver [[03 - OWASP Top 10|OWASP]]).
- **Filtraciones** de código privado o datos de usuarios, accidentales o maliciosas.

## Gobernanza
No se puede proteger lo que no se ve, así que se parte por la **visibilidad** de herramientas, personas y procesos. Luego: **privilegios mínimos** para desarrollo y operaciones, **autenticación** MFA/SSO, **protección de ramas** (revisión de código por el equipo, firmar commits, sin *force push* ni repositorios personales, búsqueda de secretos, pruebas unitarias) y supervisión de cambios (los cambios a controles requieren aprobación de seguridad y alertas ante cambios no autorizados). Según el docente, esto no ralentiza el desarrollo: son partes racionales del proceso.

## Shift left y DevSecOps
> [!tip] Dos ideas complementarias
> **Shift Left Security:** mover las prácticas de seguridad a las etapas tempranas, donde corregir cuesta menos. **DevSecOps:** hacer de la seguridad una responsabilidad compartida durante todo el ciclo, entre desarrolladores, operaciones y seguridad.

| Fase | Prácticas |
|---|---|
| Planificación, análisis, diseño | Seguridad participa desde el inicio, evalúa el impacto de los requisitos y la arquitectura |
| Codificación | **SAST** (análisis estático en IDE y git), revisión y aprobación de código, **SCA** (seguridad de dependencias open source) |
| Testing y despliegue | **DAST** (pruebas dinámicas), análisis de contenedores, ambientes separados (desarrollo, pruebas, staging, producción) |
| Mantenimiento | Telemetría, **WAF**, análisis de logs en tiempo real, alertas relevantes, *bug bounty* con divulgación responsable |

## Modelado de amenazas
Se examina el sistema y el flujo de datos, idealmente con un dibujo (identidades, usuarios, base de datos, llamadas, y **fronteras de confianza**: un formulario de inscripción atraviesa varias). Cuatro preguntas: ¿qué estamos construyendo?, ¿qué puede salir mal?, ¿qué haremos al respecto?, ¿lo hicimos bien?

**STRIDE** ordena lo que puede salir mal:

| Letra | Amenaza | Ejemplo |
|---|---|---|
| **S**poofing | Robo de identidad | Hacerse pasar por otro usuario |
| **T**ampering | Alterar datos o saltarse un componente | Modificar una petición |
| **R**epudiation | Negar o borrar el rastro de una acción | Eliminar un registro |
| **I**nformation disclosure | Violación de confidencialidad | Fuga de datos sensibles |
| **D**enial of service | Denegación de servicio | Botnet (DDoS) |
| **E**levation of privilege | Obtener más privilegios | Pasar de usuario a administrador |

## Cómo lograr un SDLC seguro
Mentalidad shift left y DevSecOps, expertos de seguridad desde temprano, modelado de amenazas, capacitar a desarrolladores, revisión de código, monitoreo, actualizar el ciclo ante nuevas amenazas y un protocolo de respuesta a incidentes ([[02 - Respuesta a incidentes y metodologías de SSDLC|siguiente nota]]).

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre Shift Left Security y DevSecOps?
> Shift left trata de *cuándo* se corrige (lo antes posible, por menor costo); DevSecOps trata de *quién*: la seguridad es responsabilidad compartida de desarrollo, operaciones y seguridad durante todo el ciclo.

> [!question]- ¿Cuál es la diferencia entre SAST y DAST?
> SAST analiza el código fuente sin ejecutarlo (durante la codificación); DAST prueba la aplicación en ejecución (durante testing y despliegue).

> [!question]- ¿Para qué sirven las fronteras de confianza en un modelo de amenazas?
> Muestran dónde los datos cruzan entre componentes con distinto nivel de confianza, que es donde hay que validar y donde pueden ocurrir las amenazas STRIDE.
