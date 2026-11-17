---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Leyes de equivalencia y cadenas de demostración]]"
  - "[[07 - Conectivos funcionalmente completos]]"
---

# Ejercicios de ayudantías de lógica proposicional y equivalencia

Las ayudantías practican cuatro habilidades: **demostrar por inducción estructural** una propiedad de las fórmulas, **traducir un texto a fórmulas** y razonar con tablas, **armar la tabla de un conectivo definido por una condición** y **demostrar una equivalencia con leyes**. Cada solución indica la ley o la regla usada en cada paso.

## Ejercicios

### 1. La fórmula dual equivale a la negación
Sea $\varphi$ una fórmula construida solo con $\neg, \wedge, \vee$. Se llama $\varphi'$ a la que resulta de cambiar cada $\wedge$ por $\vee$, cada $\vee$ por $\wedge$ y cada variable por su negación. Demuestre que $\varphi' \equiv \neg\varphi$.

> [!example]- Solución
> Inducción estructural sobre fórmulas con $\neg, \wedge, \vee$.
> - **Base.** $\varphi = p$: $\varphi' = \neg p \equiv \neg\varphi$.
> - **HI.** $\varphi' \equiv \neg\varphi$ y $\psi' \equiv \neg\psi$.
> - **Negación.** Con $\theta = \neg\varphi$, la transformación mantiene el $\neg$ y cambia el interior: $\theta' = \neg(\varphi')$. Por HI, $\neg(\varphi') \equiv \neg\neg\varphi = \neg\theta$.
> - **Disyunción.** $(\varphi \vee \psi)' = \varphi' \wedge \psi' \equiv \neg\varphi \wedge \neg\psi \equiv \neg(\varphi \vee \psi)$ (HI y De Morgan).
> - **Conjunción.** $(\varphi \wedge \psi)' = \varphi' \vee \psi' \equiv \neg\varphi \vee \neg\psi \equiv \neg(\varphi \wedge \psi)$.
>
> Ejemplo: $\varphi = (p \wedge \neg q) \vee r$ da $\varphi' = (\neg p \vee \neg\neg q) \wedge \neg r$, que equivale a $\neg\varphi$ (se comprobó con la tabla de verdad de tres variables).

### 2. Superman no existe
Se afirma: si Superman fuera capaz ($P$) y deseara prevenir el mal ($Q$), lo haría ($M$); si fuera incapaz, sería impotente ($R$); si no deseara prevenirlo, sería malévolo ($S$); si existe ($E$), no es ni impotente ni malévolo; y no previene el mal. Demuestre que no existe.

> [!example]- Solución
> Se modela con $N = (P \wedge Q \to M) \wedge (\neg P \to R) \wedge (\neg Q \to S) \wedge (E \to \neg(R \vee S)) \wedge \neg M$ y se debe probar que $N \to \neg E$ es tautología. Esa implicancia solo puede fallar si $N = 1$ y $E = 1$; se muestra que ese caso es imposible.
> 1. $E = 1$ y $E \to \neg(R \vee S)$ fuerzan $R = 0$ y $S = 0$.
> 2. $\neg P \to R$ con $R = 0$ obliga a $\neg P = 0$, o sea $P = 1$. Igual con $\neg Q \to S$: $Q = 1$.
> 3. $\neg M = 1$ da $M = 0$. Entonces $P \wedge Q \to M$ es $1 \to 0 = 0$, y $N$ vale $0$: contradicción.
>
> Luego no hay valuación con $N = E = 1$, y $N \to \neg E$ es tautología. Un recorrido de las $2^6$ valuaciones lo confirma.

### 3. Tabla de un conectivo ternario
El conectivo $EQ(p,q,r)$ vale $1$ si y solo si $3(q + r) - 5p \ge 0$. Determine su tabla.

> [!example]- Solución
> Se evalúa la expresión en cada fila:
>
> | $p$ | $q$ | $r$ | $3(q+r) - 5p$ | $EQ$ |
> |---|---|---|---|---|
> | 0 | 0 | 0 | $0$ | 1 |
> | 0 | 0 | 1 | $3$ | 1 |
> | 0 | 1 | 0 | $3$ | 1 |
> | 0 | 1 | 1 | $6$ | 1 |
> | 1 | 0 | 0 | $-5$ | 0 |
> | 1 | 0 | 1 | $-2$ | 0 |
> | 1 | 1 | 0 | $-2$ | 0 |
> | 1 | 1 | 1 | $1$ | 1 |
>
> Con $p = 0$ siempre vale $1$ (la expresión es no negativa). Con $p = 1$ solo vale $1$ si $q = r = 1$. Es decir, $EQ(p,q,r) \equiv p \to (q \wedge r)$.

### 4. Una equivalencia con cinco factores
Demuestre que $(p \vee (p \to q)) \wedge \neg(r \wedge \neg p) \wedge (p \wedge (r \vee q)) \wedge (r \to q) \equiv p \wedge q$.

> [!example]- Solución
> - $p \vee (p \to q) \equiv p \vee \neg p \vee q$ (implicancia material), que es tautología y se descarta de la conjunción.
> - $\neg(r \wedge \neg p) \equiv \neg r \vee p$ (De Morgan y doble negación).
> - $r \to q \equiv \neg r \vee q$.
>
> Queda $(p \vee \neg r) \wedge p \wedge (r \vee q) \wedge (\neg r \vee q)$. Por absorción, $p \wedge (p \vee \neg r) \equiv p$, así que equivale a $p \wedge (r \vee q) \wedge (\neg r \vee q)$. Por distributividad, $(r \vee q) \wedge (\neg r \vee q) \equiv (r \wedge \neg r) \vee q \equiv q$. El resultado es $p \wedge q$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 1 hace falta restringirse a $\neg, \wedge, \vee$?
> Porque la transformación solo está definida para esos conectivos, y el paso inductivo usa De Morgan y doble negación, que son sus leyes. Para $\to$ o $\leftrightarrow$ habría que reducirlos antes con la implicancia material.

> [!question]- ¿Qué estructura tiene el argumento de Superman para demostrar $N \to \neg E$?
> Es una prueba por contradicción sobre la única fila que podría hacerla falsa ($N = 1$ y $E = 1$): propagando los valores forzados se llega a que alguna conjunción de $N$ vale $0$.

> [!question]- ¿Cómo se reconoce que $EQ$ equivale a $p \to (q \wedge r)$?
> Mirando la tabla: es falso exactamente cuando $p = 1$ y $q \wedge r = 0$, que es la condición de falsedad de una implicancia con premisa $p$ y conclusión $q \wedge r$.
