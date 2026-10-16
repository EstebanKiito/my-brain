# Structs — índice

Cómo agrupar datos en C: definir e inicializar structs, manejarlos con punteros y la flecha `->`, anidarlos y hacerlos recursivos, y organizarlos como "objetos" con funciones init/destroy.

Volver al [[Programación en C/_Índice|mapa de Programación en C]].

> [!note] Origen
> Basado en mis resúmenes de las cápsulas de C (sección 9, con 4 diagramas de memoria) y en la segunda parte del taller introductorio (struct `gatito`, ejemplo de la cuenta por valor y por puntero). Se completó con la página 9 del CheatSheet de C del curso (struct.struct*, tabla de memoria de structs recursivos).

## Orden de estudio
1. [[01 - Definición e inicialización de structs|Definición e inicialización de structs]]: campos, `typedef`, inicialización por posición o nombre, compound literals.
2. [[02 - Punteros a structs y operador flecha|Punteros a structs y operador flecha]]: por valor frente a por puntero, structs en el heap y `->`.
3. [[03 - Structs anidados y structs recursivos|Structs anidados y structs recursivos]]: struct contenido frente a referenciado y por qué un struct recursivo necesita un puntero.
4. [[04 - Structs como objetos y tipos compuestos|Structs como objetos y tipos compuestos]]: patrón init/métodos/destroy, la interfaz de una lista y tipos que se pasan por valor.

Las imágenes de esta carpeta están en `adjuntos/`.
