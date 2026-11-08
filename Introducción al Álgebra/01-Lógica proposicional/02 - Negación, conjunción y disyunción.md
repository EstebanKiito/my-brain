---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos:
  - "[[01 - Proposiciones y valores de verdad]]"
---

# Negación, conjunción y disyunción

A partir de proposiciones simples se construyen otras **compuestas** mediante operaciones llamadas **conectivos lógicos**. Un conectivo combina los valores de verdad de sus operandos y devuelve uno nuevo, y la forma de especificarlo es la **tabla de verdad**, que recorre todas las combinaciones posibles de V y F.

## La tabla de verdad

Con dos proposiciones $p$ y $q$ hay $2 \times 2 = 4$ combinaciones de valores de verdad. En general, con $n$ proposiciones hay $2^n$ filas.

| $p$ | $q$ |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

Cada conectivo se define diciendo, fila por fila, qué valor de verdad entrega.

## Negación ($\neg p$)

La negación de $p$, escrita $\neg p$ (el apunte usa una barra sobre la letra, $\bar{p}$), toma el valor contrario a $p$.

| $p$ | $\neg p$ |
|---|---|
| V | F |
| F | V |

La negación de "murió el roto Quezada" es "no murió el roto Quezada". Es un conectivo *unario*: actúa sobre una sola proposición.

## Disyunción ($p \vee q$)

La **disyunción** ("o lógico") $p \vee q$ es falsa solo cuando $p$ y $q$ son ambas falsas.

| $p$ | $q$ | $p \vee q$ |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

Basta que una de las dos sea verdadera para que $p \vee q$ lo sea.

## Conjunción ($p \wedge q$)

La **conjunción** ("y lógico") $p \wedge q$ es verdadera solo cuando $p$ y $q$ son ambas verdaderas.

| $p$ | $q$ | $p \wedge q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

> [!tip] Los dos conectivos "y/o"
> $\wedge$ es exigente: pide que **ambas** sean V. $\vee$ es generoso: solo falla cuando **ambas** son F. Son duales: $p \vee q$ y $p \wedge q$ se relacionan por la negación (leyes de De Morgan, más adelante).

> [!warning] El "o" lógico es inclusivo
> En el lenguaje cotidiano "o" a veces excluye ("¿té o café?"). En lógica $p \vee q$ es **inclusivo**: vale V también cuando ambas son V. Para el "o exclusivo" (una y solo una) se usa otro conectivo, que no forma parte de esta base.

## Preguntas de repaso

> [!question]- ¿Cuál es la única fila donde $p \vee q$ es F? ¿Y la única fila donde $p \wedge q$ es V?
> $p \vee q$ es F solo en la fila $p=F$, $q=F$. $p \wedge q$ es V solo en la fila $p=V$, $q=V$. Son los dos extremos opuestos de la tabla.

> [!question]- Si $p$ es V y $q$ es F, calcule $\neg p$, $p \vee q$, $p \wedge q$ y $\neg q$.
> $\neg p = F$, $p \vee q = V$, $p \wedge q = F$, $\neg q = V$.

> [!question]- ¿Cuántas filas tiene la tabla de verdad de una fórmula con tres proposiciones $p, q, r$?
> $2^3 = 8$ filas: cada nueva proposición duplica el número de combinaciones posibles.

> [!question]- Escriba con símbolos y con palabras la negación de "hoy es lunes y llueve".
> La frase es $p \wedge q$ con $p$: "hoy es lunes" y $q$: "llueve". Su negación es $\neg(p \wedge q)$, que en palabras es "no es cierto que (hoy es lunes y llueve)". Cómo se simplifica se ve con las leyes de De Morgan.
