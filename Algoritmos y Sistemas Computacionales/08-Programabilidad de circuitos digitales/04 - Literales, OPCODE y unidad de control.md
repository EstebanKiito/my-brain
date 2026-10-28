---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Programabilidad de circuitos digitales"
tags:
  - algoritmos/arquitectura
  - algoritmos/assembler
  - origen/complemento
prerrequisitos:
  - "[[03 - Clock y ejecución automática|Clock y ejecución automática]]"
---

# Literales, OPCODE y unidad de control

Hasta ahora las operaciones se seleccionaban con bits escritos a mano. Para que un programa sea legible y el hardware sepa qué hacer, hacen falta tres ideas: los **literales**, el **OPCODE** y la **unidad de control**.

## Literales

Un **literal** es un valor constante que viene dentro de la instrucción. Por ejemplo, la operación `A = A + 5` suma el valor fijo 5, sin necesidad de cargarlo antes en otro registro.

En el computador del curso, una instrucción con literal ocupa 14 bits: 6 bits de OPCODE y 8 bits de literal. Los 8 bits alcanzan para valores de 0 a 255.

> [!tip] La idea central
> El literal permite cargar o combinar un valor fijo en una sola instrucción. Sin literales, habría que escribir ese valor en un registro antes de usarlo.

## OPCODE

El **OPCODE** (*operation code*) es el número que identifica la instrucción. La unidad de control lo lee y activa las señales correspondientes. Con 6 bits de OPCODE se pueden distinguir hasta $2^6 = 64$ instrucciones distintas.

## Unidad de control

La **unidad de control** es el circuito que contiene todas las instrucciones posibles y sus señales de control. Su trabajo es decodificar el OPCODE y activar las señales correctas: qué multiplexor selecciona cada entrada, qué operación hace la ALU y qué registros se cargan.

Las señales típicas son:

| Señal | Qué controla |
|---|---|
| `La`, `Lb` | Cargan `RegA` o `RegB` con el resultado |
| `Ma0` | Selecciona la entrada A de la ALU (registro o literal) |
| `Mb1`, `Mb0` | Seleccionan la entrada B de la ALU |
| `Sop2`, `Sop1`, `Sop0` | Eligen la operación de la ALU |

## Assembler

Escribir OPCODEs numéricos es incómodo y propenso a errores. El **assembler** es la notación con nombres simbólicos: en vez de `000100`, se escribe `ADDA`. El ensamblador traduce el nombre a OPCODE y el OPCODE a señales.

| Nivel | Ejemplo |
|---|---|
| Assembler | `ADDA` |
| OPCODE | `000100` |
| Señales | `La=1, Lb=0, Sop=000` |

> [!warning] El assembler no es un lenguaje de alto nivel
> El assembler sigue siendo muy cercano al hardware: cada instrucción hace una operación pequeña. Un programa en C se traduce a muchas instrucciones de assembler antes de llegar al procesador.

## Preguntas de repaso

> [!question]- ¿Qué es un literal en una instrucción?
> Un valor constante incluido en la propia instrucción, como el 5 de `A = A + 5`.

> [!question]- ¿Qué hace la unidad de control?
> Decodifica el OPCODE de la instrucción y activa las señales que configuran los multiplexores, la ALU y los registros.

> [!question]- ¿Por qué se usa assembler en vez de escribir OPCODEs?
> Porque los nombres simbólicos son más fáciles de leer y recordar que los números binarios, y reducen los errores.

> [!question]- ¿Cuántas instrucciones distintas se pueden identificar con 6 bits de OPCODE?
> $2^6 = 64$ instrucciones.
