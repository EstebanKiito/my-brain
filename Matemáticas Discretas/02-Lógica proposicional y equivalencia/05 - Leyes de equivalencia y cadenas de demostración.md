---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[04 - Equivalencia lógica, tautologías y tablas de verdad]]"
---

# Leyes de equivalencia y cadenas de demostración

Las tablas de verdad crecen como $2^n$. Para fórmulas con varias variables conviene un método algebraico: partir de equivalencias ya conocidas (las **leyes**) y reescribir paso a paso hasta llegar a la fórmula buscada. Cada paso cambia la fórmula por una equivalente, así que la cadena completa es una equivalencia.

## Las leyes

Se cumplen para cualesquiera fórmulas $\varphi, \psi, \theta \in L(P)$ y cada una se verifica con una tabla de verdad.

| Ley | Forma |
|---|---|
| Doble negación | $\neg\neg\varphi \equiv \varphi$ |
| De Morgan | $\neg(\varphi \wedge \psi) \equiv \neg\varphi \vee \neg\psi$ y $\neg(\varphi \vee \psi) \equiv \neg\varphi \wedge \neg\psi$ |
| Conmutatividad | $\varphi \wedge \psi \equiv \psi \wedge \varphi$ y lo mismo con $\vee$ |
| Asociatividad | $\varphi \wedge (\psi \wedge \theta) \equiv (\varphi \wedge \psi) \wedge \theta$ y lo mismo con $\vee$ |
| Distributividad | $\varphi \wedge (\psi \vee \theta) \equiv (\varphi \wedge \psi) \vee (\varphi \wedge \theta)$ y $\varphi \vee (\psi \wedge \theta) \equiv (\varphi \vee \psi) \wedge (\varphi \vee \theta)$ |
| Idempotencia | $\varphi \wedge \varphi \equiv \varphi$ y $\varphi \vee \varphi \equiv \varphi$ |
| Absorción | $\varphi \wedge (\varphi \vee \psi) \equiv \varphi$ y $\varphi \vee (\varphi \wedge \psi) \equiv \varphi$ |
| Implicancia material | $\varphi \to \psi \equiv \neg\varphi \vee \psi$ |
| Doble implicancia | $\varphi \leftrightarrow \psi \equiv (\varphi \to \psi) \wedge (\psi \to \varphi)$ |

Se suelen usar también las consecuencias inmediatas: $\varphi \vee \neg\varphi$ es tautología, $\varphi \wedge \neg\varphi$ es contradicción, la contrapositiva $\varphi \to \psi \equiv \neg\psi \to \neg\varphi$ y $\neg(\varphi \to \psi) \equiv \varphi \wedge \neg\psi$.

> [!tip] Estrategia
> La implicancia material y la doble implicancia permiten eliminar $\to$ y $\leftrightarrow$ para trabajar solo con $\neg, \wedge, \vee$, donde De Morgan, distributividad y absorción simplifican.

## Cómo se escribe una cadena

Se anota al margen la ley que justifica cada paso. Ejemplo: probar que $(p \to q) \wedge (p \vee q) \equiv q$.

$$\begin{aligned}
(p \to q) \wedge (p \vee q) &\equiv (\neg p \vee q) \wedge (p \vee q) && \text{implicancia material}\\
&\equiv (q \vee \neg p) \wedge (q \vee p) && \text{conmutatividad}\\
&\equiv q \vee (\neg p \wedge p) && \text{distributividad}\\
&\equiv q && \neg p \wedge p \text{ es contradicción}
\end{aligned}$$

En el último paso se usa que $\varphi \vee (\text{contradicción}) \equiv \varphi$. Una tabla de verdad confirma el resultado: ambas fórmulas valen $1$ exactamente cuando $q = 1$.

## Por qué las leyes se pueden usar dentro de una fórmula

Si $\psi \equiv \psi'$, entonces reemplazar $\psi$ por $\psi'$ **dentro** de una fórmula mayor no cambia su valor: la valuación extendida solo mira el valor de las partes. Por eso se puede aplicar una ley a una subfórmula, como en el segundo paso del ejemplo. Esa justificación es una inducción estructural sencilla sobre la fórmula que contiene la subfórmula.

## Un caso que no cumple las leyes

> [!warning] La implicancia no es conmutativa ni asociativa
> Entre las leyes no figuran $\varphi \to \psi \equiv \psi \to \varphi$ ni la asociatividad de $\to$. Se refutan con un contraejemplo de tabla: para la asociatividad basta $p = q = r = 0$, que da $0$ a un lado y $1$ al otro.

## Preguntas de repaso

> [!question]- ¿Por qué se pueden quitar los paréntesis en $p \vee q \vee r$ pero no en $p \to q \to r$?
> Porque $\vee$ es asociativo (ambos agrupamientos son equivalentes), y entonces el agrupamiento no cambia el significado. Con $\to$ los dos agrupamientos tienen tablas distintas, así que el paréntesis sí importa.

> [!question]- ¿Cuándo conviene una tabla de verdad y cuándo una cadena de leyes?
> La tabla es mecánica y segura con pocas variables ($2^n$ filas). La cadena de leyes escala a más variables y entrega una justificación legible, pero exige elegir bien los pasos.

> [!question]- ¿Cómo se niega una implicancia sin usar $\to$?
> $\neg(\varphi \to \psi) \equiv \neg(\neg\varphi \vee \psi) \equiv \neg\neg\varphi \wedge \neg\psi \equiv \varphi \wedge \neg\psi$, con implicancia material, De Morgan y doble negación.
