---
ramo: "Seguridad Computacional"
tema: "DDoS y cadena de suministro"
tags:
  - seguridad/cadena-de-suministro
  - origen/complemento
prerrequisitos:
  - "[[01 - DoS, DDoS y ataques de reflexión]]"
  - "[[03 - OWASP Top 10]]"
---

# Ataques a la cadena de suministro en npm

Un **ataque a la cadena de suministro** compromete un sistema no directamente, sino atacando alguno de sus componentes externos: dependencias de terceros, registros de paquetes, *pipelines* de CI/CD, herramientas de *build* o imágenes base. El objetivo es insertar código malicioso, robar datos, credenciales y tokens, o dejar puertas traseras sin ser detectado.

## Por qué npm es atractivo
- Ecosistema masivo con millones de paquetes, muchos sin mantenimiento, y cadenas de dependencias de decenas o cientos.
- **Confianza implícita:** `npm install` confía en el registro y en los mantenedores, y mucho código se ejecuta en scripts `postinstall`.
- Impacto amplificado: un paquete comprometido llega a miles de proyectos.

## Anatomía y patrones
1. **Compromiso:** tomar la cuenta del mantenedor, ingeniería social o adoptar un paquete abandonado.
2. **Inyección:** código en `index.js`, dependencias nuevas o scripts de ciclo de vida que ejecutan binarios remotos.
3. **Distribución:** se publica una nueva versión y quienes usan `^` o `~` la reciben sin darse cuenta.

| Patrón | Idea |
|---|---|
| **Typosquatting** | Publicar `expresss` o `react-domm` esperando errores de tipeo |
| **Dependency confusion** | Subir a npm un paquete con el nombre de uno interno; gana si el resolutor prioriza npm |
| **Maintainer compromise** | Robo de credenciales o tokens, o un colaborador malicioso |
| **Package takeover** | Adoptar paquetes abandonados y cambiar su comportamiento |

Vectores técnicos: scripts `preinstall`/`install`/`postinstall`, dependencias transitivas difíciles de auditar y exfiltración silenciosa de variables de entorno (`process.env`) a un servidor C2.

## Casos reales
- **event-stream (2018):** el mantenedor cede el control y se añade una dependencia que roba billeteras de Bitcoin.
- **ua-parser-js (2021):** cuenta comprometida; versiones con un minero de criptomonedas.
- **colors y faker (2022):** el propio mantenedor introduce código dañino como protesta: el riesgo no es solo externo.
- **Nx (2025):** el mantenedor es hackeado y se publican versiones que ejecutan código y exfiltran repositorios de GitHub.

## Factores de riesgo y defensas
Riesgos: rangos de versión laxos (`^1.2.3`), no usar *lockfiles*, no revisar dependencias ("npm install y listo") y CI/CD sin restricciones.

> [!tip] Defensas
> Usar **lockfiles** y versiones fijas, revisar los scripts de instalación, y configurar registros de confianza o *proxies* con políticas (Verdaccio, Sonatype, JFrog). Relacionado con "fallos de integridad" y "componentes vulnerables" de [[03 - OWASP Top 10|OWASP]].

## Preguntas de repaso

> [!question]- ¿Por qué un rango `^1.2.3` es un riesgo de cadena de suministro?
> Porque permite actualizar automáticamente a versiones nuevas: si el mantenedor publica una versión maliciosa, el proyecto la instala sin que nadie la revise.

> [!question]- ¿Cómo funciona la *dependency confusion*?
> El atacante publica en el registro público un paquete con el mismo nombre que uno interno; si el resolutor prioriza el registro público, instala el del atacante.

> [!question]- ¿Qué enseña el caso de colors y faker?
> Que la amenaza también puede venir de quien tiene acceso legítimo: confiar ciegamente en la última versión es un riesgo aunque no haya hackers externos.
