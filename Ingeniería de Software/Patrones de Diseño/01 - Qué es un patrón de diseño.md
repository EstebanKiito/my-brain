---
ramo: Ingeniería de Software
tema: Patrones de Diseño
tags: [ingsoft/patrones, origen/apuntes]
prerrequisitos: ["[[01 - Buen diseño de software|Buen diseño de software]]", "[[06 - Principio abierto-cerrado|Principio abierto-cerrado]]"]
---
# Qué es un patrón de diseño

Un patrón de diseño es una **solución habitual y probada a un problema de diseño que se repite**. No es código para copiar, sino un concepto general que se adapta a cada caso.

## Patrones de diseño
- **Soluciones habituales a problemas frecuentes** al diseñar software.
- Es un **concepto general** para resolver un problema particular.

**Patrones vistos en el curso:**
| Comportamiento | Estructurales | Creacionales |
|---|---|---|
| [[01 - Patrón Strategy\|Strategy]] | Decorator | Abstract Factory |
| [[03 - Patrón Template Method\|Template Method]] | Composite | Builder |
| [[05 - Patrón Observer\|Observer]] | Adapter | Factory Method |
| | Proxy | Singleton |

> [!tip] Complemento (slides "Patrones de Diseño: Comportamiento" y libro del curso, cap. 9)
> - Son como **planos prefabricados** que se personalizan para resolver un problema de diseño recurrente. El patrón **no es una función de código**, sino un concepto.
> - **En qué consiste un patrón:**
>   - **Propósito:** explica brevemente el problema y la solución.
>   - **Motivación:** explica en más detalle el problema y cómo lo resuelve el patrón.
>   - **Estructura:** las clases del patrón, sus partes y cómo se relacionan (diagrama UML).
> - **Origen:** el arquitecto Christopher Alexander (fines de los 70) habló de patrones como "la solución de un problema en un contexto". Gamma, Helm, Johnson y Vlissides, la **Gang of Four (GoF)**, publicaron *Design Patterns* con **23 patrones** en 3 grupos: **creacionales** (cómo se crean objetos), **estructurales** (cómo se componen clases y objetos) y **de comportamiento** (cómo se reparten responsabilidades y se comunican los objetos).
> - **Por qué estudiarlos** (libro): para **reutilizar soluciones** encontradas por otros con experiencia, en vez de llegar a ellas por prueba y error, y para tener una **terminología común** en el equipo ("lo resolvimos con un adaptador").
> - Casi todos persiguen lo mismo: **bajo acoplamiento, buena cohesión y extensibilidad** (abierto/cerrado), usando clases abstractas, herencia, composición y polimorfismo.
> - Referencia muy usada en el curso: https://refactoring.guru/es/design-patterns
> - Comparación útil: [[02 - Strategy vs Template Method|Strategy vs Template Method]].

## Preguntas de repaso

1. ¿Qué es un patrón de diseño?
> [!question]- Respuesta
> Una solución habitual a un problema que se repite al diseñar software. Es un concepto general que se adapta al caso, no código para copiar.

2. ¿Cuáles son las tres familias de patrones y qué resuelve cada una?
> [!question]- Respuesta
> Creacionales (cómo crear objetos), estructurales (cómo componer clases y objetos en estructuras mayores) y de comportamiento (cómo se reparten responsabilidades y se comunican los objetos).

3. ¿Qué partes describen a un patrón?
> [!question]- Respuesta
> Propósito, motivación y estructura (y en el GoF, además, sus consecuencias y restricciones).

4. Da dos razones para aprender patrones.
> [!question]- Respuesta
> Reutilizar soluciones probadas y tener un vocabulario común para comunicar diseños dentro del equipo.
