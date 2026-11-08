---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos:
  - "[[03 - Implicación y equivalencia]]"
---

# Tautologías, contradicciones y leyes lógicas

Algunas fórmulas son verdaderas (o falsas) *sin importar* los valores de sus proposiciones. Reconocerlas es la herramienta principal para simplificar y demostrar: permiten reescribir una expresión lógica en otra equivalente, paso a paso, como se despeja en álgebra.

## Tautología y contradicción

Una **tautología** es una proposición siempre verdadera, cualquiera sea el valor de sus proposiciones constituyentes. Una **contradicción** es una proposición siempre falsa.

Son tautologías:

- $p \vee \neg p$ (tercio excluso: $p$ es V o F, no hay tercera opción).
- $p \Rightarrow (p \vee q)$ (relajación: si $p$, con más razón $p$ o $q$).
- $(p \Leftrightarrow q) \Leftrightarrow (q \Leftrightarrow p)$.

La proposición $p \wedge \neg p$ es una **contradicción**: no puede ser a la vez $p$ y no $p$.

> [!tip] Tautología y contradicción
> Una **tautología** es siempre V (su tabla de verdad tiene V en todas las filas) y una **contradicción** es siempre F. El resto de fórmulas, que valen V en unas filas y F en otras, se llaman **contingencias**.

## Leyes lógicas básicas

Las siguientes equivalencias son tautologías y forman el "álgebra" de la lógica proposicional. Aquí $V$ y $F$ denotan las proposiciones constantes verdadero y falso.

| Ley | Equivalencias |
|---|---|
| Dominancia | $p \vee V \Leftrightarrow V$, $p \wedge F \Leftrightarrow F$ |
| Identidad | $p \wedge V \Leftrightarrow p$, $p \vee F \Leftrightarrow p$ |
| Idempotencia | $p \wedge p \Leftrightarrow p$, $p \vee p \Leftrightarrow p$ |
| Doble negación | $\neg(\neg p) \Leftrightarrow p$ |
| Tercio excluso | $p \vee \neg p \Leftrightarrow V$ |
| Consistencia | $p \wedge \neg p \Leftrightarrow F$ |
| Absorción | $p \vee (p \wedge q) \Leftrightarrow p$, $p \wedge (p \vee q) \Leftrightarrow p$ |
| Relajación | $p \wedge q \Rightarrow p$, $p \Rightarrow p \vee q$ |
| Caracterización de la implicación | $(p \Rightarrow q) \Leftrightarrow (\neg p \vee q)$ |

La **caracterización de la implicación** es especialmente útil: convierte una implicación en una disyunción, lo que permite "operarla" con las leyes de De Morgan y la distributividad.

> [!warning] Tercio excluso vs. consistencia
> Son duales: $p \vee \neg p$ es la tautología que afirma que no hay término medio, y $p \wedge \neg p$ es la contradicción que afirma que $p$ y su negación no pueden coexistir. Confundirlas (por ejemplo, negar un "o" y dejar el mismo conectivo) es el error más común al simplificar.

## Preguntas de repaso

> [!question]- ¿Qué distingue una tautología de una contingencia?
> La tautología vale V en **todas** las filas de su tabla de verdad; la contingencia vale V en algunas y F en otras. La contradicción vale F en todas.

> [!question]- Simplifique $p \wedge V$ y $p \vee V$.
> Por identidad, $p \wedge V \Leftrightarrow p$. Por dominancia, $p \vee V \Leftrightarrow V$ (si algo es "o verdadero", ya es verdadero).

> [!question]- Use la caracterización de la implicación para reescribir $p \Rightarrow q$ sin usar $\Rightarrow$.
> $(p \Rightarrow q) \Leftrightarrow (\neg p \vee q)$. La implicación es "falsa solo si $p$ V y $q$ F", que es exactamente "se cumple $\neg p$ o se cumple $q$".

> [!question]- ¿Es $(p \wedge q) \Rightarrow p$ una tautología? Justifique sin tabla.
> Sí, es una relajación. Si $p \wedge q$ es V, entonces en particular $p$ es V, así que $p \wedge q \Rightarrow p$ es V siempre (y si $p \wedge q$ es F, la implicación es V por hipótesis falsa).
