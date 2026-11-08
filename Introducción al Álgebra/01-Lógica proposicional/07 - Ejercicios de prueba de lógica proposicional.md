---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Implicación y equivalencia]]"
  - "[[05 - Álgebra de proposiciones: De Morgan y equivalencias]]"
---

# Ejercicios de prueba de lógica proposicional

Preguntas de la guía del curso y de tareas anteriores sobre proposiciones, tablas de verdad, tautologías y técnicas de demostración. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Tabla de verdad y negación
Considere $M : (p \vee q) \Rightarrow (p \wedge r)$. Construya su tabla de verdad y halle la negación $\neg M$.

> [!example]- Solución
> Con tres proposiciones la tabla tiene $2^3 = 8$ filas:
>
> | $p$ | $q$ | $r$ | $p \vee q$ | $p \wedge r$ | $M$ |
> |---|---|---|---|---|---|
> | V | V | V | V | V | V |
> | V | V | F | V | F | F |
> | V | F | V | V | V | V |
> | V | F | F | V | F | F |
> | F | V | V | V | F | F |
> | F | V | F | V | F | F |
> | F | F | V | F | F | V |
> | F | F | F | F | F | V |
>
> La negación es $\neg M \equiv \neg\big[(p \vee q) \Rightarrow (p \wedge r)\big]$. Como una implicación es falsa solo cuando la hipótesis es V y la conclusión es F, $\neg M \equiv (p \vee q) \wedge \neg(p \wedge r)$, y por De Morgan $\neg M \equiv (p \vee q) \wedge (\neg p \vee \neg r)$.

### 2. Equivalencia con implicación
Demuestre que $(p \wedge q) \Rightarrow r$ es lógicamente equivalente a $(p \wedge \neg r) \Rightarrow \neg q$.

> [!example]- Solución
> Usando la caracterización de la implicación y las leyes de De Morgan:
> $$
> (p \wedge q) \Rightarrow r \;\equiv\; \neg(p \wedge q) \vee r \;\equiv\; (\neg p \vee \neg q) \vee r \;\equiv\; (\neg p \vee r) \vee \neg q \;\equiv\; \neg(p \wedge \neg r) \vee \neg q \;\equiv\; (p \wedge \neg r) \Rightarrow \neg q .
> $$

### 3. Argumento válido
Determine si es válido el argumento: "Si no estudias esta semana, reprobarás cálculo. Si no estudias, no saldrás de vacaciones. Apruebas cálculo o sales de vacaciones. Por lo tanto, estudiaste esta semana."

> [!example]- Solución
> Sean $e$: "estudias esta semana", $c$: "repruebas cálculo" (así $\neg c$ es "apruebas") y $v$: "sales de vacaciones". Las premisas son $\neg e \Rightarrow c$, $\neg e \Rightarrow \neg v$ y $\neg c \vee v$; la conclusión es $e$.
>
> **Es válido.** Si $e$ fuera falsa, entonces $\neg e$ es verdadera, y de las dos primeras premisas se obtiene $c$ (reprobar) y $\neg v$ (no salir). Pero entonces la tercera premisa sería $\neg c \vee v = F \vee F = F$, contradiciendo que es verdadera. Luego $e$ no puede ser falsa: estudiaste.

### 4. Un conectivo nuevo
Si $p \star q$ es falsa si y solo si $p$ y $q$ son verdaderas, demuestre que $\big[(p \Rightarrow q) \vee q\big] \Leftrightarrow \big[(p \wedge \neg q) \star \neg q\big]$ es una tautología.

> [!example]- Solución
> La definición dice $p \star q \equiv \neg(p \wedge q)$. El lado izquierdo es $(p \Rightarrow q) \vee q \equiv (\neg p \vee q) \vee q \equiv \neg p \vee q$. El lado derecho es
> $$
> (p \wedge \neg q) \star \neg q \;\equiv\; \neg\big[(p \wedge \neg q) \wedge \neg q\big] \;\equiv\; \neg(p \wedge \neg q) \;\equiv\; \neg p \vee q .
> $$
> Ambos lados son $\neg p \vee q$, así que la equivalencia es una tautología.

### 5. El conectivo "ni… ni" ($\downarrow$)
Si $p \downarrow q$ significa "ni $p$ ni $q$" (es verdadera solo cuando ambas son falsas), demuestre las equivalencias $\neg p \Leftrightarrow (p \downarrow p)$, $p \vee q \Leftrightarrow (p \downarrow q) \downarrow (p \downarrow q)$ y $p \wedge q \Leftrightarrow (p \downarrow p) \downarrow (q \downarrow q)$.

> [!example]- Solución
> El conectivo $\downarrow$ es la negación de la disyunción: $p \downarrow q \equiv \neg(p \vee q)$.
>
> - $p \downarrow p \equiv \neg(p \vee p) \equiv \neg p$, luego $\neg p \Leftrightarrow p \downarrow p$.
> - $(p \downarrow q) \downarrow (p \downarrow q) \equiv \neg\big[(p \downarrow q) \vee (p \downarrow q)\big] \equiv \neg(p \downarrow q) \equiv \neg\neg(p \vee q) \equiv p \vee q$.
> - $(p \downarrow p) \downarrow (q \downarrow q) \equiv (\neg p) \downarrow (\neg q) \equiv \neg(\neg p \vee \neg q) \equiv \neg\neg p \wedge \neg\neg q \equiv p \wedge q$.

### 6. Simplificar con propiedades
Demuestre, usando propiedades y no tablas, que $(p \vee (q \wedge (r \Rightarrow \neg p))) \Leftrightarrow (p \vee q)$ es una tautología.

> [!example]- Solución
> Primero, $r \Rightarrow \neg p \equiv \neg r \vee \neg p$, así que
> $$
> p \vee (q \wedge (\neg r \vee \neg p)) \;\equiv\; p \vee (q \wedge \neg r) \vee (q \wedge \neg p).
> $$
> Ahora $p \vee (q \wedge \neg p) \equiv (p \vee q) \wedge (p \vee \neg p) \equiv (p \vee q) \wedge V \equiv p \vee q$, y $p \vee q \vee (q \wedge \neg r) \equiv p \vee q$ por absorción. Por lo tanto la proposición equivale a $p \vee q$.

### 7. Determinar valores de verdad
Se sabe que $[s \Rightarrow (r \vee \neg r)] \Rightarrow [(p \Rightarrow q) \wedge s \wedge r]$ es verdadera. Determine los valores de verdad de $p, q, r, s$.

> [!example]- Solución
> El antecedente $s \Rightarrow (r \vee \neg r)$ es siempre verdadero, porque $r \vee \neg r \equiv V$ (tercio excluso) y $s \Rightarrow V \equiv V$. Entonces la implicación, que es $V \Rightarrow \big[(p \Rightarrow q) \wedge s \wedge r\big]$, solo puede ser verdadera si el consecuente es V. Por lo tanto:
> $$
> (p \Rightarrow q) \wedge s \wedge r \equiv V,
> $$
> de donde $s = V$, $r = V$ y $p \Rightarrow q = V$. Los valores individuales de $p$ y $q$ **no** quedan determinados: solo se sabe que no ocurre $p = V$ con $q = F$.

## Preguntas de repaso

> [!question]- ¿Qué técnica conviene para probar una equivalencia $p \Leftrightarrow q$?
> La equivalencia dividida: probar por separado $p \Rightarrow q$ y $q \Rightarrow p$. Si es posible, también se puede partir de un lado y transformarlo en el otro usando solo equivalencias (caracterización de la implicación y De Morgan).

> [!question]- En el ejercicio 3, ¿por qué suponer que la conclusión es falsa y llegar a una contradicción demuestra el argumento?
> Porque es una reducción al absurdo: si negar la conclusión (no estudiaste) hace que una premisa se vuelva falsa, entonces la negación de la conclusión es insostenible, y la conclusión debe ser verdadera.

> [!question]- ¿Qué se aprende al expresar $\vee$ y $\wedge$ solo con el conectivo $\downarrow$?
> Que un solo conectivo basta para escribir toda la lógica proposicional. Como $p \downarrow q \equiv \neg(p \vee q)$, a partir de él se reconstruyen la negación, la disyunción y la conjunción (y con ellas, la implicación).
