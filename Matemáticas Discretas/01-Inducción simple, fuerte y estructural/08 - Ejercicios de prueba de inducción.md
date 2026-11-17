---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Equivalencia entre buen orden e inducción]]"
  - "[[06 - Inducción estructural]]"
---

# Ejercicios de prueba de inducción

Las interrogaciones y exámenes repiten cuatro formatos: **demostrar propiedades numéricas** por inducción simple o fuerte, **definir y demostrar sobre estructuras** (listas, palabras, árboles), **comparar principios** (buen orden, simple, fuerte) y **encontrar el error** en una demostración falsa. En cada uno, la pauta puntúa el caso base completo, el uso explícito de la HI y la conclusión.

## Ejercicios

### 1. Múltiplos de 3 y dígitos (I1, 2015-2)
Demuestre que para todo $n \in \mathbb{N}$, $n$ menos la suma de sus dígitos es múltiplo de $3$.

> [!example]- Solución
> Se escribe $n = \sum_i d_i 10^i$. Entonces $n - \sum_i d_i = \sum_i d_i(10^i - 1)$, y cada $10^i - 1$ es múltiplo de $3$ (por inducción: $10^0 - 1 = 0$ y $10^{i+1} - 1 = 10(10^i - 1) + 9$). Luego la suma es múltiplo de $3$. Otra forma: inducción sobre la cantidad de dígitos, con $n' = \lfloor n/10 \rfloor$ y $n - \sum d_i = 9n' + (n' - \sum_{i \le k} d_i)$.

### 2. Listas: suma, sufijo e igualdad (I1, 2016-2)
Defina inductivamente $\mathrm{sum}$ y $\mathrm{suf}$ sobre $L_\mathbb{N}$ y pruebe que, si $L_1, L_2 \neq \emptyset$, $L_1 = L_2$ si y solo si $\mathrm{suf}(L_1) = \mathrm{suf}(L_2)$ y $\mathrm{sum}(L_1) = \mathrm{sum}(L_2)$.

> [!example]- Solución
> $\mathrm{sum}(\emptyset) = 0$ y $\mathrm{sum}(L \to k) = \mathrm{sum}(L) + k$; $\mathrm{suf}(\to k) = \emptyset$ y $\mathrm{suf}(L \to k) = \mathrm{suf}(L) \to k$ para $L \neq \emptyset$. La demostración es el teorema de [[06 - Inducción estructural]]: base con $\to k$ y $\to j$ (de la suma sale $k = j$) y paso con $L_1 \to k$ y $L_2 \to j$ (de $\mathrm{suf}(L_1) \to k = \mathrm{suf}(L_2) \to j$ salen $\mathrm{suf}(L_1) = \mathrm{suf}(L_2)$ y $k = j$; luego las sumas son iguales y la HI da $L_1 = L_2$).

### 3. Palíndromos (I3, 2017-1)
Para un alfabeto $\Sigma$, $P_\Sigma$ es el menor conjunto con $\varepsilon \in P_\Sigma$, $a \in P_\Sigma$ para todo $a \in \Sigma$ y, si $u \in P_\Sigma$, $aua \in P_\Sigma$. Con $w^R$ la palabra al revés, demuestre que $w \in P_\Sigma \iff w = w^R$.

> [!example]- Solución
> ($\Rightarrow$) Inducción estructural: $\varepsilon$ y $a$ cumplen $w = w^R$; si $u = u^R$, entonces $(aua)^R = a\,u^R\,a = aua$. ($\Leftarrow$) Inducción fuerte sobre el largo de $w$: largos $0$ y $1$ son los casos base, que están en $P_\Sigma$. Si $\lvert w \rvert \ge 2$ y $w = w^R$, la primera y la última letra coinciden, así que $w = aua$ con $u = u^R$ de largo menor; por HI $u \in P_\Sigma$ y la tercera regla da $w \in P_\Sigma$.

### 4. Cota $3^n$ y la falacia del nombre (I1, 2017-2)
(a) Con $G_0 = 1$, $G_1 = 3$, $G_2 = 9$ y $G_n = G_{n-1} + 3G_{n-2} + 3G_{n-3}$, pruebe $G_n \le 3^n$. (b) Se "demuestra" por inducción que todas las personas tienen el mismo nombre: la base es $n = 1$ y en el paso se quita una persona de cada extremo. ¿Cuál es el error?

> [!example]- Solución
> (a) Inducción fuerte con **tres** casos base ($G_0, G_1, G_2$ valen exactamente $3^0, 3^1, 3^2$). Para $n \ge 3$:
> $$G_n \le 3^{n-1} + 3 \cdot 3^{n-2} + 3 \cdot 3^{n-3} = 7 \cdot 3^{n-2} < 9 \cdot 3^{n-2} = 3^n.$$
> (b) El paso no vale para $n = 1$ (de uno a dos): los grupos $\{1\}$ y $\{2\}$ no comparten ninguna persona, así que el argumento "los dos grupos se intersectan" falla. Como el caso $P(1) \Rightarrow P(2)$ es falso, la cadena de implicaciones no arranca.

### 5. Inducción simple implica fuerte (I3, 2018-1)
Demuestre que el principio de inducción simple implica el de inducción fuerte.

> [!example]- Solución
> Se parte de $A \subseteq \mathbb{N}$ con $\{0, \dots, n-1\} \subseteq A \Rightarrow n \in A$ para todo $n$. Sea $B = \{n \mid \{0, \dots, n\} \subseteq A\}$. $0 \in B$ pues $\emptyset \subseteq A$ da $0 \in A$. Si $n \in B$, entonces $\{0, \dots, n\} \subseteq A$ y la premisa da $n+1 \in A$, o sea $n + 1 \in B$. Por inducción simple, $B = \mathbb{N}$, y como $B \subseteq A$ en cada $n$, $A = \mathbb{N}$.

### 6. Intersección de intervalos (I3, 2018-1)
Si $I_1, \dots, I_n$ son intervalos abiertos con $I_i \cap I_j \neq \emptyset$ para todo par, demuestre que $I_1 \cap \dots \cap I_n \neq \emptyset$.

> [!example]- Solución
> Inducción simple con base $n = 2$ (hipótesis). Dados $I_1, \dots, I_{n+1}$ se reemplazan $I_n$ e $I_{n+1}$ por $I_n' = I_n \cap I_{n+1} = (\max(a_n, a_{n+1}), \min(b_n, b_{n+1}))$, que es un intervalo abierto no vacío. Además $I_i \cap I_n' \neq \emptyset$ para todo $i$ porque $\max(a_i, a_n, a_{n+1}) < \min(b_i, b_n, b_{n+1})$ (cada par se intersecta). Por HI aplicada a $I_1, \dots, I_{n-1}, I_n'$, la intersección total no es vacía.

### 7. Sumas de impares y $n = 2p + 7q$ (I1, 2018-2)
(a) La suma de los primeros $n$ impares es $n^2$. (b) Todo $n \ge 6$ se escribe como $2p + 7q$ con $p, q \ge 0$ enteros.

> [!example]- Solución
> (a) $1 = 1^2$ y $n^2 + (2n+1) = (n+1)^2$. (b) Se fortalece la propiedad: si $n$ es par, $n = 2p + 7q$ con $p \ge 3$; si $n$ es impar, con $q \ge 1$. Base $n = 6 = 2 \cdot 3$. Paso: si $n$ es impar ($q \ge 1$), $n + 1 = 2(p + 4) + 7(q - 1)$ es par con coeficiente de $2$ al menos $4 \ge 3$; si $n$ es par ($p \ge 3$), $n + 1 = 2(p - 3) + 7(q + 1)$ es impar con $q + 1 \ge 1$.

### 8. Fibonacci: múltiplos de 5 y paridad (I1, 2019-2)
(a) Si $n$ es múltiplo de $5$, $F_n$ es múltiplo de $5$. (b) La paridad sigue el patrón par, impar, impar, par, impar, impar, …

> [!example]- Solución
> (a) Inducción sobre $k$ para $F_{5k}$: $F_0 = 0$ y $F_{5k+5} = 5F_{5k+1} + 3F_{5k}$, múltiplo de $5$ por HI. (b) Inducción fuerte: $F_n$ es par si $n = 3k$ e impar si $n = 3k + 1$ o $3k + 2$. Bases $F_0 = 0$ y $F_1 = 1$; en el paso se usa $F_n = F_{n-1} + F_{n-2}$ según el resto de $n$ módulo $3$ (impar + impar es par; par + impar es impar).

### 9. Árboles binarios: rama más corta (Examen, 2020-1)
Con la definición de árboles binarios de [[07 - Ejercicios de ayudantías de inducción]], sea $f(\bullet) = 0$ y $f(\bullet(t_1, t_2)) = \min\{f(t_1), f(t_2)\} + 1$. Explique qué mide $f$ y demuestre $f(t) \le \log_2(\#\mathrm{nodes}(t))$.

> [!example]- Solución
> $f(t)$ es el largo de la rama más corta, es decir, la distancia de la raíz a la hoja más cercana. Sea $t = \bullet(t_1, t_2)$ y $t_s$ el subárbol con menos nodos, de modo que $\#\mathrm{nodes}(t_s) \le \tfrac{\#\mathrm{nodes}(t) - 1}{2}$. Como el mínimo es menor o igual que cada término, $f(t) \le f(t_s) + 1$, y por HI
> $$f(t) \le \log_2\!\left(\tfrac{\#\mathrm{nodes}(t) - 1}{2}\right) + 1 = \log_2(\#\mathrm{nodes}(t) - 1) \le \log_2(\#\mathrm{nodes}(t)).$$
> La base es $f(\bullet) = 0 = \log_2 1$.

## Preguntas de repaso

> [!question]- ¿Qué error común aparece en las falacias del tipo "todos los caballos son del mismo color"?
> Que el paso inductivo no se cumple para algún valor pequeño (típicamente $n = 1 \to 2$), de modo que la cadena de implicaciones no está completa.

> [!question]- ¿Cuándo conviene fortalecer la propiedad que se quiere demostrar, como en el ejercicio 7?
> Cuando la HI no alcanza para el paso (aquí necesitaba saber más sobre $p$ y $q$ según la paridad); una propiedad más fuerte da una HI más útil.

> [!question]- ¿Cómo se decide entre inducción simple, fuerte y estructural?
> Simple si el caso $n+1$ solo necesita el $n$; fuerte si necesita varios anteriores; estructural si los objetos están definidos recursivamente (listas, palabras, árboles).
