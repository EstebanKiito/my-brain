---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Compuertas lógicas y lógica proposicional"
tags:
  - algoritmos/circuitos-logicos
  - algoritmos/tablas-de-verdad
  - origen/complemento
prerrequisitos:
  - "[[02 - Compuertas NOT, AND, OR y XOR|Compuertas NOT, AND, OR y XOR]]"
---

# Circuitos lógicos y tablas de verdad

Un **circuito lógico** es una combinación de compuertas conectadas entre sí. Para saber qué hace, se construye una **tabla de verdad**: se enumeran todas las combinaciones de las entradas y se calcula la salida de cada compuerta, columna por columna.

## Cómo analizar un circuito

El método tiene tres pasos:

1. Identificar las entradas y la salida final.
2. Etiquetar los cables intermedios con una letra o una expresión.
3. Construir la tabla de verdad, agregando una columna por cada compuerta y una final para la salida.

> [!tip] La idea central
> La tabla de verdad es la "foto" del comportamiento del circuito: dice qué sale para cada combinación posible de entradas. Si dos circuitos tienen la misma tabla, son equivalentes aunque sus compuertas estén conectadas de otra forma.

## Ejemplo: $Y = (A \land B) \lor \neg A$

Primero se calculan las columnas intermedias: $A \land B$ y $\neg A$. Después se aplica el OR.

| $A$ | $B$ | $A \land B$ | $\neg A$ | $Y$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 |

La salida es 1 en tres de las cuatro combinaciones. Solo es 0 cuando $A = 1$ y $B = 0$.

## Ejemplo: $Y = (A \lor B) \land \neg B$

| $A$ | $B$ | $A \lor B$ | $\neg B$ | $Y$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 |

En este caso la salida solo es 1 cuando $A = 1$ y $B = 0$. El circuito se comporta como "A y no B".

## De la fórmula al circuito

Cada operador de la fórmula se reemplaza por su compuerta:

- $\land$ → compuerta AND.
- $\lor$ → compuerta OR.
- $\neg$ → compuerta NOT.
- $\oplus$ → compuerta XOR.

El orden de las operaciones se respeta con paréntesis. Por ejemplo, $Y = (A \land B) \lor \neg A$ se arma con una AND para $A \land B$, una NOT para $\neg A$ y una OR que une ambas ramas.

> [!warning] El orden importa
> $A \land B \lor C$ es ambiguo sin paréntesis: puede significar $(A \land B) \lor C$ o $A \land (B \lor C)$, y las tablas de verdad son distintas. Siempre conviene escribir los paréntesis.

## Preguntas de repaso

> [!question]- ¿Cuántas filas tiene la tabla de verdad de un circuito con 3 entradas?
> $2^3 = 8$ filas, una por cada combinación de 0 y 1.

> [!question]- ¿Qué significa que dos circuitos sean equivalentes?
> Que tienen la misma tabla de verdad: para cada combinación de entradas entregan la misma salida, aunque usen compuertas distintas.

> [!question]- En el ejemplo $Y = (A \land B) \lor \neg A$, ¿para qué entradas la salida es 0?
> Solo para $A = 1$ y $B = 0$, porque en ese caso $A \land B = 0$ y $\neg A = 0$.

> [!question]- ¿Cómo se pasa de una fórmula con $\oplus$ a un circuito?
> Con una compuerta XOR conectada a las dos entradas que indica la fórmula.
