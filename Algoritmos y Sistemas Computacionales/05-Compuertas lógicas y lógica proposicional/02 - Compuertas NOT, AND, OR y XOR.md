---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Compuertas lógicas y lógica proposicional"
tags:
  - algoritmos/compuertas-logicas
  - algoritmos/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Del transistor a las compuertas lógicas|Del transistor a las compuertas lógicas]]"
---

# Compuertas NOT, AND, OR y XOR

Cuatro compuertas bastan para construir casi cualquier circuito digital. Cada una tiene un símbolo, una expresión lógica y una **tabla de verdad** que dice qué sale para cada combinación de entradas. Reconocerlas es el primer paso para leer y diseñar circuitos.

## La compuerta NOT

La compuerta **NOT** invierte su única entrada: si entra 0, sale 1; si entra 1, sale 0. Se escribe $\neg A$ o $\text{not}(A)$, y su símbolo es un triángulo con un pequeño círculo en la salida.

| $A$ | $\neg A$ |
|---:|---:|
| 0 | 1 |
| 1 | 0 |

## La compuerta AND

La compuerta **AND** entrega 1 solo cuando **ambas** entradas son 1. Se escribe $A \land B$ o $A \text{ and } B$, y su símbolo tiene forma de D.

| $A$ | $B$ | $A \land B$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## La compuerta OR

La compuerta **OR** entrega 1 cuando **al menos una** entrada es 1. Se escribe $A \lor B$ o $A \text{ or } B$, y su símbolo tiene forma de escudo con una curva en la entrada.

| $A$ | $B$ | $A \lor B$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

## La compuerta XOR

La compuerta **XOR** (*exclusive or*) entrega 1 cuando **exactamente una** entrada es 1. Se escribe $A \oplus B$ o $A \text{ xor } B$, y su símbolo es como el OR pero con una doble curva en la entrada.

| $A$ | $B$ | $A \oplus B$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Los símbolos

![Símbolos de las compuertas NOT, AND, OR y XOR con sus entradas y salidas](adjuntos/S%C3%ADmbolos%20de%20compuertas%20l%C3%B3gicas.png)

> [!example]- Transcripción de la imagen
> - **Arriba a la izquierda:** NOT, un triángulo con un círculo en la punta; entrada $A$, salida $\text{not}(A)$.
> - **Arriba a la derecha:** AND, una forma de D; entradas $A$ y $B$, salida $A \text{ and } B$.
> - **Abajo a la izquierda:** OR, un escudo con la entrada curva; entradas $A$ y $B$, salida $A \text{ or } B$.
> - **Abajo a la derecha:** XOR, como el OR pero con una segunda curva; entradas $A$ y $B$, salida $A \text{ xor } B$.

> [!tip] La idea central
> AND exige que **todas** las entradas sean 1. OR se conforma con **al menos una**. XOR exige **exactamente una**. NOT solo tiene una entrada y la invierte.

## Combinar compuertas

Las compuertas se conectan entre sí: la salida de una puede ser la entrada de otra. Por ejemplo, para construir un circuito cuya salida sea 1 solo si las dos entradas son iguales, se puede usar:

$$Y = (\neg A \land \neg B) \lor (A \land B)$$

Esa expresión también se escribe $Y = \neg(A \oplus B)$: el circuito es un XOR negado (XNOR). Su tabla de verdad es:

| $A$ | $B$ | $Y$ |
|---:|---:|---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Preguntas de repaso

> [!question]- ¿Qué sale de una AND si una entrada es 0 y la otra 1?
> Sale 0. La AND solo entrega 1 cuando ambas entradas son 1.

> [!question]- ¿Qué diferencia hay entre OR y XOR cuando ambas entradas son 1?
> El OR entrega 1 (al menos una es verdadera); el XOR entrega 0 (no es exactamente una, son dos).

> [!question]- ¿Cómo se construye un XNOR con compuertas básicas?
> Con un XOR y un NOT a la salida, o con dos AND, dos NOT y un OR: $(\neg A \land \neg B) \lor (A \land B)$.

> [!question]- ¿Cuántas filas tiene la tabla de verdad de una compuerta de dos entradas?
> Cuatro, porque cada entrada puede ser 0 o 1: $2^2 = 4$ combinaciones.
