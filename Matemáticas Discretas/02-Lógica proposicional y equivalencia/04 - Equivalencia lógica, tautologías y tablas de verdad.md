---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[03 - Valuaciones y semántica de los conectivos]]"
---

# Equivalencia lógica, tautologías y tablas de verdad

Fórmulas distintas por escrito pueden decir lo mismo. Poder reconocerlo permite simplificar, transformar y comparar fórmulas sin cambiar su significado. La herramienta básica es la tabla de verdad.

## Equivalencia lógica

> [!tip] Definición
> Dos fórmulas $\varphi, \psi \in L(P)$ son **lógicamente equivalentes**, $\varphi \equiv \psi$, si $\sigma(\varphi) = \sigma(\psi)$ para **toda** valuación $\sigma$.

Equivalentes comparten semántica aunque tengan sintaxis distinta; es decir, tienen la misma tabla de verdad. Es una relación de equivalencia, no un conectivo: $\varphi \equiv \psi$ afirma algo sobre dos fórmulas, mientras que $\varphi \leftrightarrow \psi$ es una fórmula más.

## Cómo demostrar una equivalencia con tablas

Se escriben todas las valuaciones de las variables que aparecen y se calculan ambas fórmulas. Si las columnas coinciden en todas las filas, son equivalentes. Si difieren en una sola fila, **no** lo son, y esa fila es un contraejemplo.

Ejemplo: $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$. Ambas valen $1$ solo en la fila $p = q = r = 1$ y $0$ en las otras siete, así que sus tablas coinciden. Con esto se prueba que $\wedge$ es **asociativo**.

Otro ejemplo, el que motiva la clase: $\neg(\neg p \wedge \neg q)$ tiene tabla $(0,0) \mapsto 0$, $(0,1) \mapsto 1$, $(1,0) \mapsto 1$, $(1,1) \mapsto 1$, que es la de $p \vee q$. Luego $\neg(\neg p \wedge \neg q) \equiv p \vee q$.

## Tautologías y contradicciones

- Una **tautología** vale $1$ en toda valuación (por ejemplo $p \vee \neg p$).
- Una **contradicción** vale $0$ en toda valuación (por ejemplo $p \wedge \neg p$).
- Las demás son **contingentes**: dependen de la valuación.

La equivalencia se reduce a una tautología: $\varphi \equiv \psi$ si y solo si $\varphi \leftrightarrow \psi$ es tautología. Y dos tautologías cualesquiera son equivalentes entre sí, igual que dos contradicciones.

## Un ejemplo: la implicancia no es asociativa

¿Es $(p \to q) \to r \equiv p \to (q \to r)$? No. Con $p = q = r = 0$: el lado izquierdo es $(0 \to 0) \to 0 = 1 \to 0 = 0$, y el derecho es $0 \to (0 \to 0) = 0 \to 1 = 1$. También difieren con $(0, 1, 0)$ y en ninguna otra valuación. Por eso se pueden omitir paréntesis en cadenas de $\wedge$ o $\vee$, pero **no** en cadenas de $\to$.

> [!warning] El costo de las tablas
> Una tabla con $n$ variables tiene $2^n$ filas. Sirve para tres o cuatro variables; para más conviene transformar con las leyes de [[05 - Leyes de equivalencia y cadenas de demostración]].

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre $\varphi \equiv \psi$ y $\varphi \leftrightarrow \psi$?
> $\varphi \leftrightarrow \psi$ es una fórmula, que puede ser verdadera o falsa según la valuación. $\varphi \equiv \psi$ es una afirmación sobre fórmulas: que $\varphi \leftrightarrow \psi$ sea verdadera en **todas** las valuaciones, es decir, que sea tautología.

> [!question]- ¿Cómo se refuta una equivalencia?
> Basta una valuación en la que las dos fórmulas difieran. Con la tabla, esa fila es el contraejemplo.

> [!question]- ¿Es $p \to q$ equivalente a $q \to p$?
> No: con $p = 0$ y $q = 1$ la primera vale $1$ y la segunda $0$. En cambio $p \to q \equiv \neg q \to \neg p$ (contrapositiva).
