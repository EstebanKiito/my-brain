# Módulos, compilación y depuración — índice

Cómo se organiza un proyecto C en varios archivos, cómo se compila de forma eficiente con Make y cómo se depura cuando algo falla.

Volver al [[Programación en C/_Índice|mapa de Programación en C]].

> [!note] Origen
> Basado en mis resúmenes de las cápsulas de C (secciones 10 y 11, con 12 diagramas del ejemplo de reptiles). Se completó con la página 10 del CheatSheet de C del curso y con las guías del curso de setup, de depuración en C y de resolución de problemas en tareas. El proyecto de ejemplo con `Makefile` se compiló y probó.

## Orden de estudio
1. [[01 - Archivos de cabecera, include y static|Archivos de cabecera, include y static]]: qué va en el `.h` y en el `.c`, `#include <>` frente a `""` y funciones `static`.
2. [[02 - Compilación separada, enlazado y pragma once|Compilación separada, enlazado y pragma once]]: `gcc -c`, el enlazador, includes repetidos o circulares y `#pragma once`.
3. [[03 - Make y Makefile|Make y Makefile]]: reglas, dependencias, recompilación mínima y `make clean`.
4. [[04 - Depuración de programas en C|Depuración de programas en C]]: errores de compilación, *segfaults*, Valgrind y debugger con breakpoints.

Las imágenes de esta carpeta están en `adjuntos/`.
