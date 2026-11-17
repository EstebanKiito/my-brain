---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Forma normal disyuntiva desde una tabla de verdad]]"
  - "[[07 - Conectivos funcionalmente completos]]"
---

# Ejercicios de prueba de lógica proposicional y equivalencia

Las interrogaciones y exámenes repiten cinco tipos de pregunta: **completitud funcional** (probarla traduciendo desde un conjunto completo, o refutarla con un invariante), **formas normales** (construir una CNF o DNF, o demostrar que siempre existen), **contraejemplos de equivalencia** (distinguir fórmulas parecidas con una valuación), **conteo de tablas de verdad** y **propiedades por inducción estructural** (monotonía). La pauta valora que se declare la dirección de la traducción y que cada paso nombre su ley.

## Ejercicios

### 1. $\{\neg, \veebar\}$ no es completo (I1, 2015-2)
Sea $\veebar$ el XOR. Demuestre que $C = \{\neg, \veebar\}$ no es funcionalmente completo.

> [!example]- Solución
> Se prueba por inducción estructural que, sobre $n \ge 2$ variables, toda fórmula con $\neg$ y $\veebar$ es verdadera en una cantidad **par** de valuaciones. Una variable lo es en $2^{n-1}$ (par). Si $\varphi_1$ tiene $m_1$ modelos, $\neg\varphi_1$ tiene $2^n - m_1$ (par). Si $\varphi_1, \varphi_2$ tienen $m_1, m_2$ modelos y comparten $m_{12}$, entonces $\varphi_1 \veebar \varphi_2$ tiene $m_1 + m_2 - 2m_{12}$ (par). Pero $p \vee q$, sobre $\{p, q\}$, tiene tres modelos, así que no es equivalente a ninguna fórmula con $C$.

### 2. NAND es completo (I1, 2016-2)
Demuestre que $\{\uparrow\}$ es funcionalmente completo, donde $p \uparrow q = 0$ si y solo si $p = q = 1$.

> [!example]- Solución
> Como $\{\neg, \wedge\}$ es completo, basta expresar ambos con $\uparrow$ por inducción estructural: $\neg\varphi \equiv \varphi \uparrow \varphi$ (vale $1$ si $\varphi = 0$ y $0$ si $\varphi = 1$) y $\varphi \wedge \psi \equiv (\varphi \uparrow \psi) \uparrow (\varphi \uparrow \psi)$ (la negación de un NAND es la conjunción). En el paso inductivo, se reemplazan $\varphi, \psi$ por sus versiones con $\uparrow$ dadas por la HI.

### 3. Toda fórmula tiene una CNF (I1, 2017-1)
Demuestre que toda fórmula $\varphi$ es equivalente a una en CNF.

> [!example]- Solución
> Por la construcción de [[06 - Forma normal disyuntiva desde una tabla de verdad]] existe una DNF $\phi \equiv \neg\varphi$: la disyunción de los términos que codifican las valuaciones con $\varphi = 0$. Entonces $\varphi \equiv \neg\phi$, y al aplicar De Morgan a $\neg\phi$, cada término $\bigwedge \ell_i$ pasa a la cláusula $\bigvee \neg\ell_i$ y la disyunción pasa a conjunción: queda una CNF. Si $\varphi$ es tautología no hay términos y se usa $p \vee \neg p$.

### 4. Completitud de $\leftarrow$ (I1, 2018-2)
El conectivo $\varphi \leftarrow \psi$ equivale a $\psi \to \varphi$. (a) Demuestre que $\{\neg, \leftarrow\}$ es completo. (b) Demuestre que $\{\leftarrow\}$ no lo es.

![Tabla de verdad de la flecha izquierda](adjuntos/Tabla%20de%20verdad%20del%20conectivo%20flecha%20izquierda.png)

> [!example]- Transcripción de la imagen
> Tabla con columnas $\varphi$, $\psi$ y $\varphi \leftarrow \psi$: $(0,0) \mapsto 1$, $(0,1) \mapsto 0$, $(1,0) \mapsto 1$, $(1,1) \mapsto 1$. Solo es falsa cuando $\varphi = 0$ y $\psi = 1$.

> [!example]- Solución
> (a) $\{\neg, \vee\}$ es completo y $\varphi \vee \psi \equiv \neg\varphi \to \psi \equiv \psi \leftarrow \neg\varphi$; la inducción estructural traduce cada $\vee$ de ese modo.
> (b) Sobre una variable $p$, toda fórmula con solo $\leftarrow$ es equivalente a $p$ o a una tautología $\top$. Casos: $p \leftarrow p \equiv \top$, $p \leftarrow \top \equiv p$, $\top \leftarrow p \equiv \top$, $\top \leftarrow \top \equiv \top$. Ninguna es equivalente a $p \wedge \neg p$.

### 5. Implicaciones anidadas (I1, 2019-1)
Sean $\alpha_n = p_1 \to (p_2 \to (\cdots \to (p_{n-1} \to p_n)))$, $\beta_n = (\cdots((p_1 \to p_2) \to p_3) \to \cdots) \to p_n$ y $\gamma_n = (p_1 \to p_2) \wedge \cdots \wedge (p_{n-1} \to p_n)$. ¿Para qué $n \ge 2$ valen $\alpha_n \equiv \gamma_n$ y $\beta_n \equiv \gamma_n$?

> [!example]- Solución
> Solo para $n = 2$, donde las tres fórmulas son $p_1 \to p_2$. Para $n \ge 3$ sirve la valuación $(1, 0, 1, \dots, 1)$. Hace falsa a $\gamma_n$ por el factor $p_1 \to p_2 = 1 \to 0$. En cambio $\alpha_n = 1$ porque $p_2 = 0$ vuelve verdadera la implicancia interior $p_2 \to (\cdots)$, y $\beta_n = 1$ porque $\beta_2 = 0$ implica $\beta_3 = 1$ y de ahí todos los $p_k = 1$ mantienen el valor. Se comprobó computacionalmente para $n = 3, \dots, 6$.

### 6. Bicondicionales recursivos (control, 2020-1)
Con $\varphi_1 = p_1 \leftrightarrow p_2$ y $\varphi_k = \varphi_{k-1}(p_1, \dots, p_{2^{k-1}}) \leftrightarrow \varphi_{k-1}(p_{2^{k-1}+1}, \dots, p_{2^k})$: (a) $\varphi_k(p_1, \dots, p_{2^{k-1}}, p_1, \dots, p_{2^{k-1}})$ es tautología; (b) $\varphi_k$ no cambia al invertir todos los valores de una valuación.

> [!example]- Solución
> (a) Con la valuación dada, ambas mitades son la misma fórmula evaluada en los mismos valores. Si $b$ es su valor, $\varphi_k$ vale $b \leftrightarrow b = 1$.
> (b) Como $a \leftrightarrow b$ vale $1 \oplus a \oplus b$ (suma módulo 2), $\varphi_k$ es la suma módulo 2 de todas las variables más una constante. Invertir los $2^k$ valores cambia la suma $2^k$ veces, una cantidad par, así que el valor no cambia. Se verificó para $k = 1, \dots, 4$ sobre todas las valuaciones.

### 7. Contar fórmulas no equivalentes (I1, 2022-1)
Para $n$ variables, construya un conjunto satisfacible $\Sigma$ de $2^{2^{n-1}}$ fórmulas no equivalentes dos a dos.

> [!example]- Solución
> Hay $2^{2^n}$ tablas de verdad distintas. Las que valen $1$ en la valuación $(0, \dots, 0)$ son $2^{2^n - 1}$, porque queda libre el resto de las filas. Para cada una existe una fórmula con esa tabla (por la construcción de forma normal), y son no equivalentes entre sí. Todas son satisfechas por $(0, \dots, 0)$. Como $2^n - 1 \ge 2^{n-1}$, basta quedarse con $2^{2^{n-1}}$ de ellas. En realidad se alcanza $2^{2^n - 1}$, más que lo pedido.

### 8. CNF, DNF y mayoría (I1, 2024-2)
(a) CNF y DNF de $(p \vee \neg q) \to (r \vee \neg s)$. (b) Tabla del conectivo $\mathrm{Mayoría}(p,q,r)$, que vale $1$ si el valor más frecuente es $1$. (c) Una fórmula con $\neg, \wedge, \vee$ equivalente.

> [!example]- Solución
> (a) Por implicancia material y De Morgan, $\neg(p \vee \neg q) \vee r \vee \neg s \equiv (\neg p \wedge q) \vee r \vee \neg s$ (DNF). Distribuyendo $\vee$ sobre $\wedge$: $(\neg p \vee r \vee \neg s) \wedge (q \vee r \vee \neg s)$ (CNF).
> (b) Vale $1$ en $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ y $(1,1,1)$ (al menos dos unos).
> (c) $(\neg p \wedge q \wedge r) \vee (p \wedge \neg q \wedge r) \vee (p \wedge q \wedge \neg r) \vee (p \wedge q \wedge r)$. Una más corta es $(p \wedge q) \vee (p \wedge r) \vee (q \wedge r)$.

### 9. Fórmulas monótonas (examen, 2024-2)
Una valuación cumple $\sigma \le \sigma'$ si $\sigma(p) \le \sigma'(p)$ para toda variable; una fórmula es monótona si $\sigma \le \sigma'$ implica $\sigma(\varphi) \le \sigma'(\varphi)$. (a) Toda fórmula con solo $\vee, \wedge$ es monótona. (b) ¿Y si se permite $\to$?

> [!example]- Solución
> (a) Inducción estructural. Una variable es monótona por definición de $\le$. Sean $\varphi_1, \varphi_2$ monótonas y $\sigma \le \sigma'$. Si $\sigma(\varphi_1 \vee \varphi_2) = 1$, algún $\sigma(\varphi_i) = 1$, luego $\sigma'(\varphi_i) = 1$ y $\sigma'(\varphi_1 \vee \varphi_2) = 1$. Si $\sigma(\varphi_1 \wedge \varphi_2) = 1$, ambas valen $1$ y también en $\sigma'$. Si el valor en $\sigma$ es $0$, no hay nada que probar.
> (b) No. Para $p \to q$ con $\sigma = (0, 0) \le \sigma' = (1, 0)$ se tiene $\sigma(\varphi) = 1$ y $\sigma'(\varphi) = 0$.

### 10. Un conectivo ternario completo (I1, 2026-1)
El conectivo $\delta$ tiene la tabla de la figura. (a) Escriba $\delta$ en DNF y CNF. (b) Demuestre que $\{\delta\}$ es completo, sabiendo que $\{\mathrm{NOR}\}$ lo es.

![Tabla de verdad del conectivo delta](adjuntos/Tabla%20de%20verdad%20del%20conectivo%20ternario%20delta.png)

> [!example]- Transcripción de la imagen
> Tabla con columnas $p, q, r, \delta(p,q,r)$ y ocho filas en orden binario. $\delta$ vale $1$ en $(0,0,0)$, $(1,0,1)$ y $(1,1,0)$, y $0$ en las otras cinco.

> [!example]- Solución
> (a) DNF, un término por fila con $1$: $(\neg p \wedge \neg q \wedge \neg r) \vee (p \wedge \neg q \wedge r) \vee (p \wedge q \wedge \neg r)$. CNF, una cláusula por fila con $0$: $(p \vee q \vee \neg r) \wedge (p \vee \neg q \vee r) \wedge (p \vee \neg q \vee \neg r) \wedge (\neg p \vee q \vee r) \wedge (\neg p \vee \neg q \vee \neg r)$.
> (b) Si se identifican $q = r$, $\delta(p, q, q)$ vale $1$ solo con $p = q = 0$: es $\mathrm{NOR}(p, q) = \neg(p \vee q)$. Como $\{\mathrm{NOR}\}$ es completo, cada NOR se reemplaza por $\delta(\cdot, \cdot, \cdot)$ con el segundo argumento repetido, y $\{\delta\}$ también lo es.

### 11. Una DNF que es tautología (examen, 2026-1)
Determine si $(a \wedge b) \vee (b \wedge c) \vee (c \wedge d) \vee (d \wedge a) \vee (\neg a \wedge \neg c) \vee (\neg b \wedge \neg d)$ es tautología.

> [!example]- Solución
> Sí. Se ubican $a, b, c, d$ en los vértices de un cuadrado: los cuatro primeros términos son los **lados** con dos unos y los dos últimos son las **diagonales** con dos ceros. Si la fórmula valiera $0$, no habría lado con dos unos ni diagonal con dos ceros. Por falta de diagonales de ceros, hay un vértice con $1$ (si todos fueran $0$, la diagonal $a, c$ sería de ceros). Sus dos vecinos deben ser $0$ (si no, habría un lado con dos unos), pero esos dos vecinos son los extremos de una diagonal: dos ceros, contradicción. Con $16$ valuaciones se confirma por exhaustividad.

## Preguntas de repaso

> [!question]- ¿Qué tienen en común los argumentos para $\{\neg\}$, $\{\leftarrow\}$ y $\{\neg, \veebar\}$ no completos?
> Todos fijan una propiedad que cualquier fórmula del conjunto conserva (ser equivalente a $p$ o $\neg p$, a $p$ o $\top$, tener un número par de modelos) y muestran una función que la viola.

> [!question]- ¿Cómo se obtiene una CNF a partir de una DNF de la negación?
> Se construye la DNF de $\neg\varphi$ (términos de las filas con $0$ de $\varphi$), se niega y se aplica De Morgan: cada término se vuelve una cláusula y la disyunción se vuelve conjunción.

> [!question]- ¿Por qué un contraejemplo basta para refutar una equivalencia pero no para probarla?
> Una equivalencia afirma igualdad de valor en **todas** las valuaciones. Una valuación que las distinga la refuta; una valuación que las iguale no dice nada sobre las demás.
