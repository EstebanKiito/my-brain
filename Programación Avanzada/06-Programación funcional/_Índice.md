# Programación funcional — índice

Conceptos y herramientas del paradigma funcional en Python: principios de diseño con funciones puras y ausencia de efectos colaterales, comunicación bidireccional en generadores con `.send()`, funciones de orden superior (`map`, `filter` y `reduce`), expresiones anónimas `lambda`, empaquetamiento paralelo con `zip` y enumeración con `enumerate`, herramientas avanzadas de iteración y combinatoria con `itertools`, y arquitectura de tuberías de datos (*pipelines*) para procesamiento masivo en memoria constante $O(1)$.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cuatro notebooks de la séptima semana del curso (paradigma funcional, funciones generadoras, funciones que usan iterables y aplicaciones prácticas).

## Orden de estudio
1. [[01 - Paradigma funcional y funciones puras|Paradigma funcional y funciones puras]]: fundamentos declarativos, funciones puras, determinismo, eliminación de efectos colaterales y composición funcional.
2. [[02 - Generadores avanzados: envío de datos con send|Generadores avanzados: envío de datos con send]]: bidireccionalidad de `yield`, inyección de datos con `.send()`, cebado inicial y control con `.close()` y `.throw()`.
3. [[03 - Funciones de orden superior: map, filter y reduce|Funciones de orden superior]]: transformación con `map`, filtrado booleano con `filter` y plegado acumulativo con `reduce`.
4. [[04 - Funciones anónimas lambda, zip y enumerate|Funciones anónimas lambda, zip y enumerate]]: sintaxis concisa con `lambda`, emparejamiento paralelo con `zip()` e indexación idiomática con `enumerate()`.
5. [[05 - Herramientas de iteración: itertools y combinatoria|Herramientas de iteración: itertools y combinatoria]]: iteradores infinitos (`count`, `cycle`), encadenamiento con `chain`, cortes con `islice`, permutaciones y combinaciones.
6. [[06 - Pipelines de datos y evaluación perezosa en la práctica|Pipelines de datos y evaluación perezosa en la práctica]]: construcción de tuberías de datos modulares, agregación con diccionarios y análisis de eficiencia en memoria constante $O(1)$.
