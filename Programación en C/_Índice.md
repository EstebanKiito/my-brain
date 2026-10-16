# Programación en C — mapa

Tutorial del lenguaje C usado en Estructuras de Datos (IIC2133): sintaxis, punteros, memoria dinámica, structs y compilación con módulos y Make. Cada nota cubre **un concepto**, y dentro de cada carpeta el número indica el orden de lectura. Las notas de [[Estructuras de Datos/_Índice|Estructuras de Datos]] enlazan aquí cuando implementan algo en C.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` y `prerrequisitos` (lo que conviene leer antes).
- **Cuerpo:** prosa explicativa que parte por el problema que resuelve cada concepto, con programas cortos que compilan con `gcc -Wall -Wextra` y se probaron. Los errores típicos van en callouts `[!warning]` y las reglas clave en `[!tip]`.
- **Imágenes:** diagramas de memoria y salidas de terminal de las cápsulas, cada uno con su transcripción en un callout plegable. En las capturas que mostraban la cámara del expositor, esa esquina se tapó.
- **Cierre:** cada nota termina con preguntas de repaso con la respuesta oculta en un callout plegable.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Programación en C/01-Fundamentos del lenguaje/_Índice\|Fundamentos del lenguaje]] | Estructura de un programa, compilación con gcc, tipos y casting, control de flujo, funciones y stack |
| [[Programación en C/02-Punteros, arreglos y strings/_Índice\|Punteros, arreglos y strings]] | Direcciones y punteros, paso por valor, aritmética de punteros, arreglos, strings y `argv` |
| [[Programación en C/03-Memoria dinámica y Valgrind/_Índice\|Memoria dinámica y Valgrind]] | Stack frente a heap, `malloc`/`calloc`/`free`, matrices dinámicas, errores de memoria y Valgrind |
| [[Programación en C/04-Structs/_Índice\|Structs]] | Definición, `typedef`, punteros a structs y `->`, structs anidados y recursivos, patrón init/destroy |
| [[Programación en C/05-Módulos, compilación y depuración/_Índice\|Módulos, compilación y depuración]] | Headers y `static`, compilación separada, `#pragma once`, Make y depuración |

## Ruta de estudio sugerida
1. **Fundamentos → Punteros:** lo mínimo para leer cualquier programa C del curso. Lo central es entender qué guarda un puntero y por qué un arreglo "es" su primer elemento.
2. **Memoria dinámica → Structs:** con estos dos temas ya se puede implementar una lista ligada, un heap o un árbol.
3. **Módulos y depuración:** para organizar un proyecto con varios archivos y encontrar los errores que C no reporta.
