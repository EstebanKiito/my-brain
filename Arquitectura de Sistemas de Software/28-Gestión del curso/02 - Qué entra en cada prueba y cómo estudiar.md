---
ramo: "Arquitectura de Sistemas de Software"
tema: "Gestión del curso"
tags:
  - arquisis/gestion
  - origen/complemento
prerrequisitos:
  - "[[01 - Evaluaciones y cálculo de la nota]]"
  - "[[01 - Método para resolver un caso de prueba]]"
---

# Qué entra en cada prueba y cómo estudiar

La materia del curso es **acumulativa**: cada prueba puede preguntar todo lo anterior, y siempre hay una pregunta de diagrama UML de componentes. Esta nota reúne qué entra en cada evaluación, cómo usar el material y qué se permite con IA, más una ruta de estudio por las notas de este ramo.

## Contenidos por evaluación (2026-2)

| Evaluación | Contenidos | Notas del vault |
|---|---|---|
| **I1** | Introducción y definiciones, atributos de calidad, NFR, DDD estratégico, diagramación y UML, estilos y patrones | Temas 01 a 13 |
| **I2** | **Todo hasta Escalabilidad** (es acumulativa, con preguntas de UML), con **foco teórico** en lo que no entró en la I1: **Integración, DDD táctico, Performance y Escalabilidad** | Temas 14 a 25, más el repaso de 01 a 13 |
| **Examen** | Todo el curso (en 2025-2 incluyó además NoSQL, seguridad, cloud y despliegue) | Todo el vault |

Para la I2 se publicó en Canvas un **compilado de preguntas** de pruebas anteriores, que se resuelve en el tema [[01 - Método para resolver un caso de prueba]] y en las notas siguientes.

## Formato típico de la I2

1. **Preguntas de desarrollo** (dos, con un máximo de 8 a 11 líneas cada una): comparar o explicar con un caso. Ejemplos: falacias de la red, CAP y PACELC, cookies frente a OAuth o JWT, caché y consistencia, relacional frente a NoSQL.
2. **Alternativas** (2 a 4 puntos cada una): caché, sharding, leader-follower, REST, gRPC o GraphQL, tácticas de integrabilidad.
3. **Caso** (elegir uno de dos, unos 34 puntos): tres preguntas propias y cuatro comunes (características, estilos, diagrama de componentes y falencias).

## Cómo usar el material

- **Bibliografía clave:** *Fundamentals of Software Architecture* (Richards y Ford, 2.ª ed.), *Software Architecture in Practice* (Bass y Kazman, 4.ª ed.), *Patterns of Enterprise Application Architecture* (Fowler) y *Domain-Driven Design Distilled* (Vernon).
- **Se espera leer la literatura adjunta**: en clase se asume que ya se leyó.
- **Las slides son un apoyo referencial, no un traspaso completo**: tienen los puntos clave, pero hay que complementarlas con notas e investigación propias.
- **Cómo estudiar:** ir a clases y estudiar los tópicos a tiempo, para que maduren; trabajar con **casos**, donde las ayudantías ayudan mucho; **practicar la diagramación**; y preguntar sin miedo.

## Uso de IA

- Es **perjudicial en el aprendizaje inicial**: hay muchos conceptos nuevos y conexiones entre conceptos nuevos y antiguos que conviene hacer uno mismo.
- **Proyecto:** libre en el código, e incluso solicitado.
- **Interrogaciones:** solo para resumir o consultar conceptos, y solo en el caso online. El estudiante es responsable de verificar que la información sea correcta.
- **Actividades y debates:** no se permite.

> [!tip] Ruta de estudio para la I2
> 1. **Integración** (temas 14 a 17), cerrando con la guía para elegir el mecanismo de integración.
> 2. **DDD táctico** (tema 18).
> 3. **Performance** (temas 19 a 22): tácticas, falacias de la red y caché.
> 4. **Escalabilidad** (temas 23 a 25): leyes, métodos, CAP, sharding y leader-follower.
> 5. **Repaso de la I1**: atributos y escenarios (04 a 07), UML (09) y la tabla de estilos (13).
> 6. **Casos resueltos** (tema 26) y las preguntas de repaso de cada nota.

## Preguntas de repaso

> [!question]- ¿Qué contenidos tienen foco teórico en la I2 y por qué igual hay que repasar la I1?
> El foco teórico está en Integración, DDD táctico, Performance y Escalabilidad. Hay que repasar la I1 porque la materia es acumulativa: siempre hay preguntas de atributos, estilos y un diagrama de componentes UML que usan esos contenidos.

> [!question]- ¿Qué formato tiene la pregunta de caso de la I2?
> Se elige uno de dos casos. Se responden tres preguntas propias del caso (medidas concretas) y cuatro comunes: características arquitectónicas en orden, estilos con su responsabilidad, un diagrama de componentes UML y dos falencias de la solución.

> [!question]- ¿Qué libros forman la bibliografía clave del curso?
> *Fundamentals of Software Architecture* (Richards y Ford), *Software Architecture in Practice* (Bass y Kazman), *Patterns of Enterprise Application Architecture* (Fowler) y *Domain-Driven Design Distilled* (Vernon).

> [!question]- ¿En qué instancias se permite usar IA?
> En el proyecto, libremente en el código. En las interrogaciones, solo para resumir o consultar conceptos en la modalidad online, siendo responsable de verificar la información. No se permite en actividades ni debates.

> [!question]- ¿Por qué las slides "no son un handoff"?
> Porque son un apoyo con puntos clave y tips, no un traspaso completo de la materia. Se espera complementarlas con lecturas, notas propias e investigación.

> [!question]- V o F: "Como la I2 tiene foco en Integración, Performance y Escalabilidad, no habrá preguntas de UML".
> Falso. La materia es acumulativa y el equipo docente advirtió que habrá preguntas de UML. Además, la pregunta de caso siempre incluye un diagrama de componentes.
