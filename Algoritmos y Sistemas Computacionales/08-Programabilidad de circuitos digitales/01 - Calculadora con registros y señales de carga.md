---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Programabilidad de circuitos digitales"
tags:
  - algoritmos/arquitectura
  - algoritmos/registros
  - origen/complemento
prerrequisitos:
  - "[[03 - Unidad de selección y ALU|Unidad de selección y ALU]]"
---

# Calculadora con registros y señales de carga

Una ALU sola calcula y olvida: no guarda el resultado. Para encadenar operaciones hace falta agregarle **registros**, que son espacios de almacenamiento dentro del circuito, y **señales de carga**, que deciden cuándo un registro se actualiza. Con esas dos piezas nace una calculadora que acumula resultados.

## La calculadora de 4 bits

El primer circuito del tema tiene dos registros, `RegA` y `RegB`, de 4 bits cada uno, una ALU y un controlador de display. El usuario ingresa los valores con interruptores, la ALU ejecuta la operación seleccionada por `S` y el display muestra el resultado.

![Calculadora de 4 bits con registros RegA y RegB, ALU y display](adjuntos/Calculadora%20de%204%20bits.png)

> [!example]- Transcripción de la imagen
> - Arriba, los registros `RegA` y `RegB`, con entradas de 4 bits y señales de carga.
> - Al centro, la ALU con entradas `A` y `B`, selector `S` y salida `Result` de 4 bits.
> - Abajo, el `Display Controller` y un display de 7 segmentos.
> - Las líneas con números indican el ancho en bits (4 para los datos, 3 para el selector).

## El set de instrucciones

La ALU acepta 8 operaciones, seleccionadas con 3 bits:

| Selector | Operación |
|---|---|
| 000 | Suma |
| 001 | Resta |
| 010 | AND |
| 011 | OR |
| 100 | NOT A |
| 101 | XOR |
| 110 | Shift left A |
| 111 | Shift right A |

## Registros acumuladores

En la calculadora de 8 bits, el resultado se guarda de vuelta en `RegA` o `RegB` al final de cada ejecución. La siguiente operación usa esos valores actualizados: los registros funcionan como **acumuladores**.

El detalle clave son las señales de carga `La` y `Lb`:

- Si `La = 1`, `RegA` se actualiza con el resultado al final del ciclo; si `La = 0`, conserva su valor.
- Lo mismo pasa con `Lb` y `RegB`.

Así, una instrucción se describe con 5 bits: la operación `S` (3 bits) y las señales `La`, `Lb` (2 bits).

> [!tip] La idea central
> La ALU calcula, pero los registros deciden qué se conserva. Con las señales de carga se puede ejecutar una operación y guardar el resultado solo en el registro que corresponde.

## Un ejemplo de acumulación

Partiendo con `RegA = 0x76` y `RegB = 0x05`:

| Paso | Operación | La | Lb | RegA | RegB |
|---|---|---:|---:|---|---|
| 1 | Suma (000) | 1 | 0 | 0x7B | 0x05 |
| 2 | Shift right (111) | 0 | 1 | 0x7B | 0x3D |
| 3 | Resta (001) | 1 | 0 | 0x3E | 0x3D |
| 4 | AND (010) | 0 | 1 | 0x3E | 0x3C |

Cada fila es una instrucción: la ALU opera con los valores actuales y las señales de carga deciden qué registro cambia.

> [!warning] Una operación por ciclo
> En cada ciclo se ejecuta una sola instrucción y se actualizan como máximo los registros indicados. No se puede sumar y restar al mismo tiempo con esta estructura.

## Preguntas de repaso

> [!question]- ¿Por qué una ALU sola no basta para hacer una calculadora?
> Porque no guarda los resultados. Sin registros, el valor calculado se perdería al terminar el ciclo.

> [!question]- ¿Qué hace la señal de carga `La`?
> Si vale 1, el registro `RegA` se actualiza con el resultado al final del ciclo; si vale 0, mantiene su valor anterior.

> [!question]- ¿Cuántos bits tiene una instrucción en esta calculadora y qué representan?
> Cinco bits: tres para la operación (`S`) y dos para las señales de carga (`La` y `Lb`).

> [!question]- ¿Qué significa que un registro sea acumulador?
> Que guarda el resultado de la operación y lo usa como entrada de la siguiente, acumulando el cálculo.
