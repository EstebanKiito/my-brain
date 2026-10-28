---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Gestión del curso"
tags:
  - algoritmos/gestion
  - origen/complemento
prerrequisitos:
  - "[[01 - Evaluaciones y reglas del curso|Evaluaciones y reglas del curso]]"
---

# Materia por evaluación y cómo estudiar

Cada interrogación cubre un bloque de temas. Esta nota conecta cada evaluación con las notas del vault y propone un orden de repaso para no estudiar de memoria, sino entendiendo cómo se conectan los conceptos.

## Qué entra en la I1

| Tema | Notas | Qué practicar |
|---|---|---|
| Representación numérica | [[Algoritmos y Sistemas Computacionales/02-Representación numérica/_Índice\|Representación numérica]] | Conversiones binario↔decimal↔hexadecimal |
| Operaciones y complemento a dos | [[Algoritmos y Sistemas Computacionales/03-Operaciones binarias y complemento a dos/_Índice\|Operaciones binarias y complemento a dos]] | Sumas, negativos, restas y rango |
| Codificación | [[Algoritmos y Sistemas Computacionales/04-Codificación de caracteres/_Índice\|Codificación de caracteres]] | ASCII, UTF-8 y decodificación |
| Compuertas lógicas | [[Algoritmos y Sistemas Computacionales/05-Compuertas lógicas y lógica proposicional/_Índice\|Compuertas lógicas y lógica proposicional]] | Tablas de verdad y simplificación |
| Circuitos sumadores | [[Algoritmos y Sistemas Computacionales/06-Circuitos sumadores/_Índice\|Circuitos sumadores]] | Medio sumador, sumador completo y restador |

La I1 termina en los circuitos sumadores. No entra la programabilidad de circuitos ni los sistemas operativos.

## Qué entra en la I2

| Tema | Notas | Qué practicar |
|---|---|---|
| Multiplexores y demultiplexores | [[Algoritmos y Sistemas Computacionales/07-Multiplexores y demultiplexores/_Índice\|Multiplexores y demultiplexores]] | Selección, tablas y unidades de selección |
| Programabilidad de circuitos | [[Algoritmos y Sistemas Computacionales/08-Programabilidad de circuitos digitales/_Índice\|Programabilidad de circuitos digitales]] | Trazas del computador básico y set de instrucciones |
| Sistemas operativos | [[Algoritmos y Sistemas Computacionales/09-Sistemas operativos/_Índice\|Sistemas operativos]] | Procesos, paginación, archivos y SO |

La I2 se apoya en lo anterior: para entender el computador básico hay que manejar la ALU, los multiplexores y el complemento a dos.

## Ruta de repaso

1. **Conversiones y complemento a dos:** son la base de casi todo. Practicar hasta hacerlas sin pensar.
2. **Compuertas y tablas de verdad:** construir la tabla columna por columna, sin saltarse pasos.
3. **Sumadores:** entender por qué el acarreo se propaga y cómo se encadena un sumador completo.
4. **MUX y DEMUX:** distinguir N a 1 de 1 a N y contar líneas de selección.
5. **Computador básico:** seguir un programa con PC, registros, MUX y ALU.
6. **Sistemas operativos:** procesos, paginación, archivos y asignación de bloques.
7. **Algoritmos:** contar operaciones, comparar crecimiento y trazar BFS/DFS/Dijkstra.

> [!tip] La idea central
> Los temas no son independientes: la representación alimenta las operaciones, las operaciones alimentan los circuitos, los circuitos alimentan el computador y el computador necesita un sistema operativo. Estudiar en ese orden hace que cada tema tenga sentido.

## Consejos para la interrogación

- **Escribe el procedimiento.** Aunque el resultado esté mal, el desarrollo puede dar puntaje parcial.
- **Revisa las unidades y la base.** Un número sin subíndice se asume decimal; `0x` y `0b` cambian la interpretación.
- **Dibuja la tabla o el circuito.** Ordena la información y reduce los errores.
- **Comprueba los resultados.** Una suma binaria se puede verificar pasando a decimal; una resta con complemento a dos se comprueba sumando.
- **No memorices sin entender.** Las preguntas suelen pedir explicar por qué, no repetir una definición.

> [!warning] El error más caro
> Confundir el acarreo con el desbordamiento, o el complemento de uno con el de dos. Son cosas distintas y aparecen en casi todas las evaluaciones.

## Preguntas de repaso

> [!question]- ¿Qué temas de la I1 se apoyan en la representación numérica?
> Casi todos: operaciones y complemento a dos, codificación y circuitos sumadores. Las conversiones son la base.

> [!question]- ¿Por qué la I2 incluye sistemas operativos si el curso es de algoritmos y sistemas?
> Porque el ramo cubre ambos lados: los sistemas computacionales (hardware, SO) y los algoritmos. La I2 cierra la parte de sistemas.

> [!question]- ¿Conviene estudiar los temas en el orden del vault?
> Sí. El orden está pensado para que cada tema use lo anterior: representación → operaciones → circuitos → computador → SO → algoritmos.

> [!question]- ¿Qué se gana mostrando el desarrollo en una evaluación?
> Puntaje parcial si el resultado final es incorrecto, y claridad para detectar en qué paso se cometió el error.
