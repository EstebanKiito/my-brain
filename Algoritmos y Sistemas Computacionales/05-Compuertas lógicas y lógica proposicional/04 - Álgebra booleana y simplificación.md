---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Compuertas lógicas y lógica proposicional"
tags:
  - algoritmos/algebra-booleana
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[03 - Circuitos lógicos y tablas de verdad|Circuitos lógicos y tablas de verdad]]"
---

# Álgebra booleana y simplificación

Un circuito funciona, pero puede tener compuertas de más. El **álgebra booleana** es el conjunto de reglas que permite reescribir una expresión lógica sin cambiar su tabla de verdad. Simplificar ahorra compuertas, espacio y energía, y hace el circuito más fácil de entender.

## Las reglas básicas

| Regla | Expresión |
|---|---|
| Identidad | $A \land 1 = A$; $A \lor 0 = A$ |
| Anulación | $A \land 0 = 0$; $A \lor 1 = 1$ |
| Idempotencia | $A \land A = A$; $A \lor A = A$ |
| Complemento | $A \land \neg A = 0$; $A \lor \neg A = 1$ |
| Doble negación | $\neg(\neg A) = A$ |
| Distributiva | $A \land (B \lor C) = (A \land B) \lor (A \land C)$ |
| De Morgan | $\neg(A \land B) = \neg A \lor \neg B$; $\neg(A \lor B) = \neg A \land \neg B$ |

> [!tip] La idea central
> Dos expresiones son equivalentes si tienen la misma tabla de verdad. El álgebra booleana permite pasar de una a otra sin dibujar la tabla, usando reglas parecidas a las del álgebra común.

## Ejemplo de simplificación

Simplificar $Y = (A \lor B) \land (\neg A \lor C)$:

1. Distribuir: $Y = (A \land \neg A) \lor (A \land C) \lor (B \land \neg A) \lor (B \land C)$.
2. Como $A \land \neg A = 0$, ese término desaparece.
3. Queda $Y = (A \land C) \lor (B \land \neg A) \lor (B \land C)$.

La expresión simplificada usa menos compuertas que la original, pero entrega la misma salida para todas las entradas.

## Un ejemplo conocido: el XOR

La expresión $\neg A \land B \lor A \land \neg B$ parece larga, pero su tabla de verdad es exactamente la del XOR:

| $A$ | $B$ | $\neg A \land B$ | $A \land \neg B$ | $Y$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |

Por eso se escribe directamente $Y = A \oplus B$.

## Un ejercicio de diseño

Diseñar un circuito con entradas $A$, $B$, $C$ cuya salida sea 1 cuando **al menos dos** entradas sean 1. La expresión se arma sumando los casos:

$$Y = (A \land B) \lor (A \land C) \lor (B \land C)$$

Cada término cubre una pareja que puede estar encendida; si las tres están encendidas, igual se cumple al menos un término. El circuito usa tres AND y un OR de tres entradas.

> [!warning] Simplificar no es adivinar
> Cada paso debe justificarse con una regla. Si se elimina un término "porque parece que no se usa", se puede cambiar la tabla de verdad y el circuito deja de funcionar.

## Preguntas de repaso

> [!question]- ¿Por qué $A \land \neg A = 0$?
> Porque ninguna entrada puede ser verdadera y falsa al mismo tiempo. Si $A = 1$, $\neg A = 0$; si $A = 0$, $\neg A = 1$. El AND siempre recibe un 0.

> [!question]- ¿Qué dice la ley de De Morgan sobre $\neg(A \land B)$?
> Que es equivalente a $\neg A \lor \neg B$: negar una conjunción es lo mismo que negar cada parte y unirlas con OR.

> [!question]- ¿Para qué sirve simplificar una expresión lógica?
> Para usar menos compuertas, reducir el costo y el consumo, y obtener un circuito más fácil de leer y de probar.

> [!question]- ¿Cómo se comprueba que dos expresiones son equivalentes?
> Comparando sus tablas de verdad. Si coinciden en todas las filas, las expresiones son equivalentes.
