---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Proposiciones y sintaxis de las fórmulas proposicionales]]"
---

# Valuaciones y semántica de los conectivos

Antes de la semántica, una fórmula es solo una secuencia de símbolos. La **semántica** le da significado: dice cuándo una fórmula es verdadera. La idea es fijar primero el valor de las variables y calcular el resto siguiendo la estructura de la fórmula.

## Valuaciones

Una **valuación** (o asignación de verdad) sobre $P$ es una función $\sigma : P \to \{0, 1\}$. Elige un valor para cada variable: cada valuación describe un "mundo posible". Si $\lvert P \rvert = n$, hay $2^n$ valuaciones (dos opciones por variable).

## Valuación extendida

Una valuación solo habla de variables. Se **extiende** a $\hat\sigma : L(P) \to \{0,1\}$ por recursión sobre la fórmula:

- $\hat\sigma(p) = \sigma(p)$ para $p \in P$;
- $\hat\sigma(\neg\psi) = 1$ si $\hat\sigma(\psi) = 0$, y $0$ en otro caso;
- $\hat\sigma(\psi_1 \wedge \psi_2) = 1$ si ambas valen $1$, y $0$ en otro caso;
- $\hat\sigma(\psi_1 \vee \psi_2) = 0$ solo si ambas valen $0$, y $1$ en otro caso;
- $\hat\sigma(\psi_1 \to \psi_2) = 0$ solo si $\hat\sigma(\psi_1) = 1$ y $\hat\sigma(\psi_2) = 0$;
- $\hat\sigma(\psi_1 \leftrightarrow \psi_2) = 1$ si ambas coinciden.

Por simplicidad se escribe $\sigma$ en vez de $\hat\sigma$. Esta recursión es la que le da significado a los conectivos.

## Tablas de verdad de los conectivos

![Tablas de verdad de los cinco conectivos básicos](adjuntos/Tablas%20de%20verdad%20de%20los%20conectivos%20b%C3%A1sicos.png)

> [!example]- Transcripción de la imagen
> Tabla con columnas $p, q, (\neg p), (p \wedge q), (p \vee q), (p \to q), (p \leftrightarrow q)$ y cuatro filas.
> - $(0,0)$: $1, 0, 0, 1, 1$.
> - $(0,1)$: $1, 0, 1, 1, 0$.
> - $(1,0)$: $0, 0, 1, 0, 0$.
> - $(1,1)$: $0, 1, 1, 1, 1$.

Cada fila es una valuación (un mundo posible) y cada columna indica en qué mundos es verdadera esa fórmula. Una fórmula queda determinada semánticamente por su tabla.

> [!warning] La implicancia es falsa en un solo caso
> $p \to q$ vale $0$ únicamente con $p = 1$ y $q = 0$. Si $p = 0$ la implicancia es verdadera sin importar $q$ ("vacuamente"). Es la fuente de errores más común al armar tablas.

## Ejemplo resuelto

Sea $P = \{p, q\}$, $\sigma(p) = 1$, $\sigma(q) = 0$ y $\varphi = ((\neg(\neg p)) \leftrightarrow ((\neg p) \wedge q))$. Se evalúa de adentro hacia afuera:

- $\sigma(\neg p) = 0$ y $\sigma(\neg\neg p) = 1$;
- $\sigma(\neg p \wedge q) = 0 \wedge 0 = 0$;
- $\sigma(\varphi) = (1 \leftrightarrow 0) = 0$.

## Cuántas valuaciones y cuántas tablas

Con $n$ variables hay $2^n$ valuaciones, o sea $2^n$ filas en la tabla. Cada fila puede valer $0$ o $1$ de forma independiente, así que hay $2^{2^n}$ **tablas de verdad distintas**. Para $n = 1, 2, 3$ son $4, 16, 256$. Estos números reaparecen constantemente en computación; el segundo es mucho mayor que el primero, y por eso hay infinitas fórmulas pero solo $2^{2^n}$ "significados" distintos.

## Preguntas de repaso

> [!question]- ¿Por qué la valuación extendida se define por recursión y no fila por fila?
> Porque las fórmulas son inductivas: el valor de $(\psi_1 \star \psi_2)$ depende solo de los valores de las partes. La recursión sigue exactamente las reglas de construcción y está bien definida gracias a que cada fórmula se arma de una única manera.

> [!question]- ¿Cuántas filas tiene la tabla de $(p \to q) \vee r$ y cuántas tablas distintas existen para esas tres variables?
> Tiene $2^3 = 8$ filas, y existen $2^{2^3} = 256$ tablas distintas posibles para tres variables.

> [!question]- Si $\sigma(p) = 0$, ¿cuánto vale $p \to q$ para cualquier $q$?
> Vale $1$, porque la implicancia solo falla cuando la premisa es verdadera y la conclusión falsa.
