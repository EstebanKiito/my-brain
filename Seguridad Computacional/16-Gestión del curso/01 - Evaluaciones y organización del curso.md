---
ramo: "Seguridad Computacional"
tema: "Gestión del curso"
tags:
  - gestion
  - origen/apuntes
prerrequisitos: []
---

# Evaluaciones y organización del curso

Seguridad Computacional (IIC2531) es un curso de **amplitud más que de profundidad**: recorre muchas áreas de la seguridad con casos de estudio reales, en vez de ahondar en una sola. El docente es Ignacio Parada, con un equipo de ayudantes del club de ciberseguridad.

## Contenidos
Modelos de amenaza, arquitectura enfocada en seguridad, separación de privilegios, aislación de componentes, seguridad de dispositivos móviles, seguridad en redes y otros temas, con varias charlas de invitados (SDLC seguro, DDoS y botnets, ataques a la cadena de suministro).

## Evaluaciones
- **Dos interrogaciones (I1 e I2) y un examen final.**
- **Cinco laboratorios:** defensas y/o ataques a sistemas bastante reales (poco código, mucho pensamiento no estándar): desbordamiento de búfer, separación de privilegios con contenedores, ejecución simbólica, ataques web (XSS) y cifrado de archivos.
- **Proyecto final** con presentaciones al final del semestre, orientado al ataque o a la defensa.
- Se lee un *paper* por clase; las ayudantías apoyan los laboratorios y la preparación de las interrogaciones.

## Qué materia entra en cada evaluación
| Evaluación | Temas del vault |
|---|---|
| **I1** | [[Seguridad Computacional/01-Fundamentos de seguridad/_Índice\|Fundamentos]], [[Seguridad Computacional/02-Buffer overflows y baggy bounds/_Índice\|buffer overflows]], [[Seguridad Computacional/03-Autenticación de usuarios/_Índice\|autenticación]], [[Seguridad Computacional/04-Arquitectura de seguridad de Google/_Índice\|arquitectura de Google]], [[Seguridad Computacional/05-Separación de privilegios con OKWS/_Índice\|OKWS]], [[Seguridad Computacional/06-Contenedores y microVMs/_Índice\|contenedores]] y [[Seguridad Computacional/15-SDLC seguro/_Índice\|SDLC seguro]] |
| **I2** | Firecracker, [[Seguridad Computacional/07-Sandboxing de software/_Índice\|WebAssembly y RLBox]], [[Seguridad Computacional/08-Seguridad móvil/_Índice\|iOS y Android]], [[Seguridad Computacional/09-Ejecución simbólica/_Índice\|ejecución simbólica]], [[Seguridad Computacional/10-Seguridad web/_Índice\|seguridad web y OWASP]], [[Seguridad Computacional/11-Seguridad TCP-IP/_Índice\|TCP/IP]] y [[Seguridad Computacional/12-TLS y certificados/_Índice\|TLS]] |
| **Examen** | Todo el ramo; además [[Seguridad Computacional/13-Mensajería segura/_Índice\|mensajería]] y [[Seguridad Computacional/14-DDoS y cadena de suministro/_Índice\|DDoS y cadena de suministro]], que no figuran en los resúmenes de las interrogaciones |

> [!tip] Cómo estudiar
> Cada caso de estudio sigue el mismo esquema: qué amenaza se modela, qué aislamiento o mecanismo se usa y qué limita su seguridad. Conviene repasarlos con las preguntas de repaso de cada nota.

## Preguntas de repaso

> [!question]- ¿Qué tipo de actividades evalúan los laboratorios?
> Defensas y ataques sobre sistemas realistas, que exigen razonar como atacante más que escribir mucho código.

> [!question]- ¿Qué distingue el enfoque del curso?
> Busca amplitud: recorre casos de estudio de muchas áreas y deja la profundidad de cada una para otros cursos.

> [!question]- ¿Qué técnica común aparece en la mayoría de los casos de estudio?
> El aislamiento y el privilegio mínimo: separar componentes para que un compromiso quede contenido.
