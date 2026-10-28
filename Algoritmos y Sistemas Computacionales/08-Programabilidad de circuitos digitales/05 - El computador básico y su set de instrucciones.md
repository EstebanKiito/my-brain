---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Programabilidad de circuitos digitales"
tags:
  - algoritmos/arquitectura
  - algoritmos/assembler
  - origen/complemento
prerrequisitos:
  - "[[04 - Literales, OPCODE y unidad de control|Literales, OPCODE y unidad de control]]"
---

# El computador básico y su set de instrucciones

El **computador básico** del curso reúne todas las piezas de los temas anteriores: dos registros de 8 bits, dos multiplexores, una ALU, una memoria de instrucciones, un PC y una unidad de control. Esta nota muestra cómo se conectan y cómo se lee su set de instrucciones.

## El diagrama

Las piezas y sus conexiones:

- **RegA y RegB**: registros de 8 bits que guardan los operandos y los resultados.
- **MUX A y MUX B**: eligen qué entra a la ALU: el valor de un registro o un literal de la instrucción.
- **ALU**: ejecuta la operación indicada por `Sop2 Sop1 Sop0`.
- **PC**: guarda la dirección de la instrucción actual.
- **Memoria de instrucciones**: entrega la instrucción de 14 bits (6 de OPCODE y 8 de literal).
- **Unidad de control**: decodifica el OPCODE y activa `La`, `Lb`, `Ma0`, `Mb1`, `Mb0` y `Sop`.

![Computador básico: registros, multiplexores, ALU, PC, memoria de instrucciones y unidad de control](adjuntos/Computador%20b%C3%A1sico.png)

> [!example]- Transcripción de la imagen
> - Arriba, el `PC` de 8 bits entrega la dirección a la memoria de instrucciones.
> - La memoria entrega 14 bits: 6 de OPCODE van a la unidad de control y 8 de literal van a los multiplexores.
> - `RegA` y `RegB` de 8 bits se conectan a `Mux A` y `Mux B`.
> - La ALU recibe `A` y `B`, usa `Sop2 Sop1 Sop0` y entrega `R` de 8 bits, que vuelve a los registros.

## El set de instrucciones

La unidad de control reconoce 28 instrucciones. La tabla muestra el OPCODE, las señales y la operación:

| Instrucción | OPCODE | La | Lb | Ma0 | Mb1 | Mb0 | Sop2 | Sop1 | Sop0 | Operación |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MOVAB | 000000 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | A = B |
| MOVBA | 000001 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | B = A |
| MOVAL | 000010 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | A = literal |
| MOVBL | 000011 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | B = literal |
| ADDA | 000100 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | A = A + B |
| ADDB | 000101 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | B = A + B |
| ADDL | 000110 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | A = A + literal |
| SUBA | 000111 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | A = A − B |
| SUBB | 001000 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | B = A − B |
| SUBL | 001001 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | A = A − literal |
| ANDA | 001010 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | A = A ∧ B |
| ANDB | 001011 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | B = A ∧ B |
| ANDL | 001100 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | A = A ∧ literal |
| ORA | 001101 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | A = A ∨ B |
| ORB | 001110 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | B = A ∨ B |
| ORL | 001111 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | A = A ∨ literal |
| NOTA | 010000 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | A = ¬A |
| NOTB | 010001 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | B = ¬A |
| NOTL | 010010 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | A = ¬literal |
| XORA | 010011 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | A = A ⊕ B |
| XORB | 010100 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | B = A ⊕ B |
| XORL | 010101 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | A = A ⊕ literal |
| SHLA | 010110 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | A = shift left(A) |
| SHLB | 010111 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | B = shift left(A) |
| SHLL | 011000 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | A = shift left(literal) |
| SHRA | 011001 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | A = shift right(A) |
| SHRB | 011010 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | B = shift right(A) |
| SHRL | 011011 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | A = shift right(literal) |

> [!tip] Cómo leer la tabla
> `La = 1` significa que el resultado se guarda en `RegA`; `Lb = 1`, en `RegB`. Las columnas `Ma0`, `Mb1`, `Mb0` configuran los multiplexores, y `Sop2 Sop1 Sop0` eligen la operación de la ALU.

## Un programa paso a paso

Este programa carga 5 en A, 3 en B, suma, resta, hace AND y niega A:

| PC | Instrucción | RegA | RegB |
|---:|---|---:|---:|
| 0 | MOVAL 0x05 | 0x05 | 0x00 |
| 1 | MOVBL 0x03 | 0x05 | 0x03 |
| 2 | ADDA | 0x08 | 0x03 |
| 3 | SUBA | 0x05 | 0x03 |
| 4 | ANDA | 0x01 | 0x03 |
| 5 | NOTA | 0xFE | 0x03 |

En el paso 4, $5 \land 3 = 1$; en el paso 5, $\neg 1 = 11111110_2 = \text{0xFE}$. El PC avanza de 0 a 5 y el programa termina.

> [!warning] El programa no se detiene solo
> En este modelo, después de la última instrucción el PC sigue avanzando y lee direcciones vacías. Un programa real necesita una instrucción de salto o de detención para terminar de forma controlada.

## Preguntas de repaso

> [!question]- ¿Qué hace `MOVAL 0x05`?
> Carga el literal 5 en `RegA`. El OPCODE de `MOVAL` activa `La` y configura el multiplexor A para tomar el literal.

> [!question]- ¿Qué diferencia hay entre `ADDA` y `ADDL`?
> `ADDA` suma `RegA + RegB`; `ADDL` suma `RegA + literal`. La diferencia está en qué entrada elige el multiplexor.

> [!question]- ¿Cómo se ejecuta `NOTA`?
> La ALU aplica NOT a `RegA` y el resultado se guarda en `RegA` porque `La = 1`.

> [!question]- ¿Por qué el computador puede ejecutar programas distintos con el mismo hardware?
> Porque las instrucciones están almacenadas en memoria. Cambiando la memoria cambia el programa, pero los registros, la ALU y la unidad de control siguen siendo los mismos.
