---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Álgebra de proposiciones: De Morgan y equivalencias]]"
  - "[[06 - Técnicas de demostración como tautologías]]"
---

# Ejercicios de prueba de lógica proposicional

Preguntas de interrogaciones de semestres anteriores. Se repiten tres tipos: armar una tabla de verdad, probar una equivalencia **sin tablas** (usando leyes lógicas y nombrándolas) y deducir valores de verdad a partir de que una proposición es verdadera o falsa. En las pautas, cada ley usada suele dar puntaje, así que conviene escribir el nombre al lado de cada paso.

## Ejercicios

### 1. Contrarrecíproca, con tabla y en palabras
(a) Demuestre que $p \Rightarrow q$ es lógicamente equivalente a $\neg q \Rightarrow \neg p$. (b) Escriba en palabras la contrarrecíproca de "si el último dígito de un número (de más de dos dígitos) es cero, entonces el número es divisible por 5".

> [!example]- Solución
> (a) Basta comparar las columnas:
>
> | $p$ | $q$ | $\neg q$ | $\neg p$ | $p \Rightarrow q$ | $\neg q \Rightarrow \neg p$ |
> |---|---|---|---|---|---|
> | V | V | F | F | V | V |
> | V | F | V | F | F | F |
> | F | V | F | V | V | V |
> | F | F | V | V | V | V |
>
> Las dos últimas columnas coinciden fila a fila, así que son equivalentes.
> (b) "Si un número no es divisible por 5, entonces su último dígito no es cero." Hay que negar **las dos** partes e **intercambiarlas**; negar sin intercambiar da la contraria, que no es equivalente.

### 2. Una tautología con tres variables
Verifique que $[(\neg p \vee q) \vee (\neg r \wedge \neg p)] \Leftrightarrow (\neg q \Rightarrow \neg p)$ es una tautología.

> [!example]- Solución
> Con tabla, de 8 filas: la columna de cada lado coincide en todas las filas, así que la equivalencia es siempre V. Sin tabla es más corto:
> - **Lado izquierdo:** $(\neg p \vee q) \vee (\neg r \wedge \neg p) \equiv q \vee [\neg p \vee (\neg p \wedge \neg r)] \equiv q \vee \neg p$, por asociatividad y **absorción** ($\neg p \vee (\neg p \wedge \neg r) \equiv \neg p$).
> - **Lado derecho:** $\neg q \Rightarrow \neg p \equiv \neg\neg q \vee \neg p \equiv q \vee \neg p$, por caracterización de la implicación y doble negación.
>
> Los dos lados son equivalentes a $q \vee \neg p$, así que la bicondicional es una tautología.

### 3. Simplificar hasta llegar a $p$
Pruebe, sin tablas, que $[(\neg p \wedge q) \Rightarrow (q \Rightarrow p)] \wedge p \equiv p$.

> [!example]- Solución
> $$\begin{aligned}
> [(\neg p \wedge q) \Rightarrow (q \Rightarrow p)] \wedge p &\equiv [\neg(\neg p \wedge q) \vee (q \Rightarrow p)] \wedge p && \text{(caracterización de la implicación)} \\
> &\equiv [(p \vee \neg q) \vee (q \Rightarrow p)] \wedge p && \text{(De Morgan y doble negación)} \\
> &\equiv [(p \vee \neg q) \vee (\neg q \vee p)] \wedge p && \text{(caracterización de la implicación)} \\
> &\equiv (p \vee \neg q) \wedge p && \text{(conmutatividad e idempotencia)} \\
> &\equiv p && \text{(absorción)}
> \end{aligned}$$

### 4. La implicación no es asociativa
(a) Con tablas, muestre que $p \Rightarrow (q \Rightarrow r)$ no es equivalente a $(p \Rightarrow q) \Rightarrow r$. (b) Sin tablas, demuestre que $p \Rightarrow (q \Rightarrow r) \equiv (p \wedge q) \Rightarrow r$.

> [!example]- Solución
> (a) Conviene reescribir antes: $p \Rightarrow (q \Rightarrow r) \equiv \neg p \vee \neg q \vee r$ y $(p \Rightarrow q) \Rightarrow r \equiv \neg(\neg p \vee q) \vee r \equiv (p \wedge \neg q) \vee r$. En la fila $p = F$, $q = V$, $r = F$ la primera vale V (porque $\neg p$ es V) y la segunda F (porque $p \wedge \neg q$ y $r$ son F). Basta una fila distinta para que no sean equivalentes (también difieren en $p = q = r = F$).
> (b) Partiendo del lado derecho:
> $$(p \wedge q) \Rightarrow r \equiv \neg(p \wedge q) \vee r \equiv (\neg p \vee \neg q) \vee r \equiv \neg p \vee (\neg q \vee r) \equiv p \Rightarrow (q \Rightarrow r).$$
> (Caracterización, De Morgan, asociatividad y dos veces caracterización.) Esta equivalencia se llama **exportación**: "si $p$, entonces si $q$, entonces $r$" dice lo mismo que "si $p$ y $q$, entonces $r$".

### 5. Deducir valores de verdad desde una implicación falsa
(a) Si $p \Rightarrow q$ es falsa, determine el valor de verdad de $[(p \vee r) \wedge \neg q] \Rightarrow [(\neg p \wedge s) \Rightarrow (t \vee p)]$. (b) Si $[(p \Leftrightarrow q) \wedge \neg(r \Rightarrow s) \wedge \neg t] \Rightarrow [s \vee (q \Rightarrow s)]$ es falsa, determine los valores de $p, q, r, s, t$.

> [!example]- Solución
> (a) Una implicación es falsa solo si el antecedente es V y el consecuente F: $p = V$ y $q = F$. Entonces $(p \vee r) \wedge \neg q \equiv V \wedge V \equiv V$ y $(\neg p \wedge s) \Rightarrow (t \vee p) \equiv (F \wedge s) \Rightarrow (\dots) \equiv F \Rightarrow (\dots) \equiv V$. Antecedente V y consecuente V: la proposición es **verdadera**, sin importar $r$, $s$ y $t$.
> (b) Que sea falsa obliga a antecedente V y consecuente F.
> - Consecuente F: $s \vee (q \Rightarrow s) \equiv F$ exige $s = F$ y $q \Rightarrow s \equiv F$, así que $q = V$.
> - Antecedente V: cada parte de la conjunción es V. $\neg t \equiv V$ da $t = F$; $\neg(r \Rightarrow s) \equiv V$, con $s = F$, da $r = V$; y $p \Leftrightarrow q$ con $q = V$ da $p = V$.
>
> Respuesta: $p = q = r = V$ y $s = t = F$ (única asignación posible).

### 6. Equivalencia con una contradicción
Sin tablas, demuestre que $(f \wedge \neg g) \Rightarrow (h \wedge \neg h)$ es equivalente a $f \Rightarrow g$.

> [!example]- Solución
> $$\begin{aligned}
> (f \wedge \neg g) \Rightarrow (h \wedge \neg h) &\equiv \neg(f \wedge \neg g) \vee (h \wedge \neg h) && \text{(caracterización de la implicación)} \\
> &\equiv \neg(f \wedge \neg g) \vee F && (h \wedge \neg h \text{ es una contradicción}) \\
> &\equiv \neg f \vee g && \text{(neutro de } \vee \text{, De Morgan y doble negación)} \\
> &\equiv f \Rightarrow g && \text{(caracterización de la implicación)}
> \end{aligned}$$
> Esta es exactamente la tautología de la **reducción al absurdo**: suponer $f$ y $\neg g$ y llegar a una contradicción demuestra $f \Rightarrow g$.

## Preguntas de repaso

> [!question]- ¿Cuál es el primer paso casi obligado al simplificar una proposición con implicaciones?
> Reemplazar cada $a \Rightarrow b$ por $\neg a \vee b$ (caracterización de la implicación). Después todo se reduce a $\neg$, $\wedge$ y $\vee$, donde valen De Morgan, distributividad y absorción.

> [!question]- Para mostrar que dos proposiciones **no** son equivalentes, ¿hace falta la tabla completa?
> No: basta exhibir una sola asignación de valores en que difieren. La tabla completa solo es necesaria para probar que **sí** lo son.

> [!question]- ¿Qué información da saber que una implicación es falsa?
> Fija dos valores a la vez: el antecedente es V y el consecuente es F. Es la única fila falsa de la implicación, por eso estas preguntas tienen solución única.
