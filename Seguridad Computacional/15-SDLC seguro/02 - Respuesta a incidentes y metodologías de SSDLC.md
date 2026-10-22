---
ramo: "Seguridad Computacional"
tema: "SDLC seguro"
tags:
  - seguridad/sdlc
  - origen/complemento
prerrequisitos:
  - "[[01 - SDLC seguro, DevSecOps y modelado de amenazas]]"
---

# Respuesta a incidentes y metodologías de SSDLC

Ningún ciclo de desarrollo evita todos los incidentes, por lo que se necesita un protocolo para actuar rápido y aprender de cada uno.

## Protocolo de respuesta a incidentes
1. **Equipos especializados:** sistema de guardia (*on-call*) con rotaciones.
2. **Invocar a los actores involucrados:** es un esfuerzo colaborativo entre equipos.
3. **Identificar la severidad:** superficie de ataque y exposición, y asignar prioridad (P1, P2…). **CVSS** (*Common Vulnerability Scoring System*) puntúa la gravedad de una vulnerabilidad con métricas como el vector de ataque, la complejidad y el impacto.
4. **Identificar causa y soluciones:** una solución inmediata y otra de mediano o largo plazo.
5. **Documentar y comunicar:** plantilla de incidente, compromisos y responsables, y comunicación responsable a los afectados.
6. **Reuniones de equipos** y revisión posterior.
7. **Post mortem:** qué salió bien, qué salió mal, en qué hubo suerte y qué se aprende.

## Metodologías populares

| Metodología | Qué es |
|---|---|
| **Microsoft SDL** | Ciclo de desarrollo seguro de Microsoft |
| **OWASP SAMM** | Modelo de madurez para evaluar y mejorar prácticas de seguridad del software |
| **NIST CSF** | Marco de ciberseguridad del NIST para gestionar riesgos |
| **Google SLSA** | Niveles de seguridad de artefactos y de la cadena de suministro de software |
| **ISO/IEC 27001** | Estándar de sistemas de gestión de seguridad de la información |

Referencias de aprendizaje de la charla: OWASP Top 10, la calculadora CVSS, el *Secure Developer Podcast* y LiveOverflow.

## Preguntas de repaso

> [!question]- ¿Por qué se hace un post mortem incluso si el incidente se resolvió?
> Para aprender: identifica qué falló, qué funcionó y dónde hubo suerte, y alimenta mejoras del ciclo de desarrollo para evitar repetirlo.

> [!question]- ¿Para qué sirve CVSS al responder un incidente?
> Para estimar la gravedad de la vulnerabilidad de forma estándar y así asignar prioridad y recursos.

> [!question]- ¿Qué problema aborda SLSA frente a los demás marcos?
> La integridad de la cadena de suministro: que los artefactos de software provengan de una construcción verificable y no hayan sido alterados.
