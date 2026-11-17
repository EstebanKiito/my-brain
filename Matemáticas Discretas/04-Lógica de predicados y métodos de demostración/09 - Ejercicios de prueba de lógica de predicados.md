---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Equivalencias y negación con cuantificadores]]"
  - "[[05 - Consecuencia lógica en predicados y reglas de inferencia]]"
---

# Ejercicios de prueba de lógica de predicados

Las interrogaciones repiten cinco formatos: **decidir equivalencias** entre fórmulas (con demostración o contramodelo), **decidir si un argumento es válido**, **formalizar** enunciados en un vocabulario restringido, **construir oraciones que distingan estructuras** y **demostrar propiedades semánticas** de las fórmulas. La pauta puntúa que cada afirmación de equivalencia o consecuencia se justifique sobre una interpretación arbitraria o con un contramodelo explícito.

## Ejercicios

### 1. Argumento y estructuras distintas (I1, 2015-2)
(a) ¿Es válido? *Todos los albos son borrachos. Algunos cruzados no son borrachos. No hay hinchas cruzados y albos a la vez. Luego ningún cruzado es borracho.* (b) Con $A_1 = (\mathbb{N}, <)$, $A_2 = (\mathbb{Z}, <)$, $A_3 = (\mathbb{Q}, <)$, $A_4 = (\mathbb{Q} \cap [0, 1], <)$, construya fórmulas $\varphi_i$ verdaderas en $A_i$ y falsas en las otras tres.

> [!example]- Solución
> (a) **No es válido.** Con $A$, $B$, $C$ para albo, borracho y cruzado, las premisas son $\forall x\,(A(x) \to B(x))$, $\exists x\,(C(x) \wedge \neg B(x))$ y $\neg\exists x\,(C(x) \wedge A(x))$, y la conclusión $\forall x\,(C(x) \to \neg B(x))$. En el dominio $\{1, 2, 3, 4\}$ con $A = \{1\}$, $B = \{1, 2, 3\}$, $C = \{3, 4\}$ las tres premisas son verdaderas (el $4$ es cruzado y no borracho), pero el $3$ es cruzado y borracho: la conclusión falla.
>
> (b) Sean $\text{mín} := \exists x\,\forall y\,(x < y \vee x = y)$ y $\text{denso} := \forall x\,\forall y\,(x < y \to \exists z\,(x < z \wedge z < y))$. Entonces $\varphi_1 = \neg\text{denso} \wedge \text{mín}$, $\varphi_2 = \neg\text{denso} \wedge \neg\text{mín}$, $\varphi_3 = \text{denso} \wedge \neg\text{mín}$ y $\varphi_4 = \text{denso} \wedge \text{mín}$ (cada estructura ocupa una combinación distinta de las dos propiedades; véase la tabla de la nota sobre interpretaciones).

### 2. Equivalencias entre cuantificadores (I1, 2016-2)
¿Son válidas? (a) $\forall x\,(P \wedge Q) \equiv \forall x\,P \wedge \forall x\,Q$; (b) $\exists x\,(P \wedge Q) \equiv \exists x\,P \wedge \exists x\,Q$; (c) $\forall x\,\exists y\,\varphi(x, y) \equiv \exists x\,\forall y\,\varphi(x, y)$.

> [!example]- Solución
> (a) **Válida**: para cualquier $I$, todos los elementos cumplen $P \wedge Q$ si y sólo si todos cumplen $P$ y todos cumplen $Q$. (b) **No válida**: en $\mathbb{N}$ con $P$ = «par» y $Q$ = «impar», la derecha es verdadera y $\exists x\,(P \wedge Q)$ es falsa. (c) **No válida**: en $\mathbb{Z}$ con $\varphi = x < y$, la izquierda es verdadera y la derecha falsa (no hay mínimo).

### 3. Propiedades de grafos con sólo $E$ (examen, 2016-2)
Para un grafo $G = (V, E)$ con $E(x, y)$ la adyacencia, dé una fórmula con sólo $E$ y $=$ que exprese: (a) $G$ es completo; (b) $G$ tiene un clique de tamaño $3$; (c) tiene un conjunto independiente de tamaño $3$; (d) tiene un ciclo de tamaño $4$; (e) todo par de nodos está a distancia a lo más $3$.

> [!example]- Solución
> (a) $\forall x\,\forall y\,(x = y \vee E(x, y))$.
> (b) $\exists x\,\exists y\,\exists z\,(x \ne y \wedge x \ne z \wedge y \ne z \wedge E(x, y) \wedge E(x, z) \wedge E(y, z))$.
> (c) Igual, con $\neg E$ en las tres aristas.
> (d) $\exists w\,\exists x\,\exists y\,\exists z$ con los cuatro distintos y $E(w, x) \wedge E(x, y) \wedge E(y, z) \wedge E(z, w)$.
> (e) $\forall x\,\forall y\,\big(x \ne y \to (E(x, y) \vee \exists p\,(E(x, p) \wedge E(p, y)) \vee \exists p\,\exists q\,(E(x, p) \wedge E(p, q) \wedge E(q, y)))\big)$, con implicación y no con $\wedge$ (de otro modo exigiría $x \ne y$ para todo par).

### 4. Interpretación sobre los primos (I1, 2017-1)
En $I_{\text{primos}}$ (dominio $\mathbb{N}$, $=$, $\le$ y $P(n)$ = «$n$ es primo») (1) diga si $\alpha := \forall x\,(P(x) \to \exists y\,(x \le y \wedge \neg(x = y) \wedge P(y)))$ es verdadera y qué significa; (2) escriba «para todo par de primos distintos de $2$ y $3$ existe un natural entre ellos que no es primo».

> [!example]- Solución
> (1) $\alpha$ dice que para todo primo hay otro primo mayor; es **verdadera** porque hay infinitos primos (prueba por contradicción de [[06 - Demostración directa, por contrapositivo y por contradicción]]). (2) Usando constantes para $2$ y $3$:
> $$\forall x\,\forall y\,\Big(\big(P(x) \wedge P(y) \wedge x \ne y \wedge x \ne 2 \wedge x \ne 3 \wedge y \ne 2 \wedge y \ne 3\big) \to \exists z\,\big(((x \le z \wedge z \le y) \vee (y \le z \wedge z \le x)) \wedge z \ne x \wedge z \ne y \wedge \neg P(z)\big)\Big).$$
> Sin constantes se definen como en la nota de [[08 - Ejercicios de ayudantías de lógica de predicados]].

### 5. Silogismo de gatos, perros y reptiles (I1, 2017-2)
¿Es válida? *Todo gato es querido por al menos un perro. Ningún perro quiere a un reptil. Luego ningún gato es reptil.*

> [!example]- Solución
> Con $G, P, R$ unarios y $Q(x, y)$: «$x$ quiere a $y$»: $\varphi_1 = \forall x\,(G(x) \to \exists y\,(P(y) \wedge Q(y, x)))$, $\varphi_2 = \forall x\,\forall y\,((P(x) \wedge R(y)) \to \neg Q(x, y))$ y $\psi = \forall x\,(G(x) \to \neg R(x))$. Se refuta $\{\varphi_1, \varphi_2, \neg\psi\}$: de $\neg\psi$ sale $G(a) \wedge R(a)$; de $\varphi_1$ con $a$ sale $\neg G(a) \vee P(b)$ y $\neg G(a) \vee Q(b, a)$ ($b$ nuevo); de $\varphi_2$ con $b, a$ sale $\neg P(b) \vee \neg R(a) \vee \neg Q(b, a)$. Resolviendo se obtiene $P(b)$, $Q(b, a)$, $R(a)$ y entonces la cláusula vacía. **Válida.**

### 6. Equivalencias con $R$ y $S$ (I1, 2018-1)
Diga si son equivalentes y justifique: (1) $\alpha_1 = \forall x\,(S(x) \to \exists y\,R(x, y))$ y $\alpha_2 = \forall x\,\forall y\,(S(x) \to R(x, y))$; (2) $\beta_1 = \forall x\,((\exists y\,R(x, y)) \to S(x))$ y $\beta_2 = \forall x\,\forall y\,(R(x, y) \to S(x))$.

> [!example]- Solución
> (1) **No equivalentes.** Dominio $\{0, 1\}$, $S = \{0\}$, $R = \{(0, 0)\}$: $\alpha_1$ es verdadera (para $x = 0$ sirve $y = 0$) y $\alpha_2$ es falsa ($S(0)$ pero $R(0, 1)$ no se cumple).
>
> (2) **Equivalentes:** $\beta_1 \equiv \forall x\,(\neg\exists y\,R(x, y) \vee S(x)) \equiv \forall x\,((\forall y\,\neg R(x, y)) \vee S(x)) \equiv \forall x\,\forall y\,(\neg R(x, y) \vee S(x)) \equiv \beta_2$. El paso de meter $\forall y$ dentro de la disyunción se justifica porque $y$ no aparece libre en $S(x)$; no es una de las cuatro equivalencias básicas, así que conviene probarlo.

### 7. Definibilidad con $\le$ y $=$ (I1, 2019-1)
Sobre $\mathbb{N}$ con $O(x, y) := x \le y$ y $E(x, y) := x = y$, un elemento $a$ es *definible* si existe $\varphi(x)$ con $I \models \varphi(b) \iff b = a$. Pruebe que $0$, $2$ y todo $n$ son definibles.

> [!example]- Solución
> $\varphi_0(x) = \forall y\,O(x, y)$. El sucesor es $S(x, y) := O(x, y) \wedge \neg E(x, y) \wedge \forall z\,((O(x, z) \wedge O(z, y)) \to (E(x, z) \vee E(z, y)))$; la cláusula $\neg E(x, y)$ es necesaria, porque sin ella $S$ sería refleja y la fórmula siguiente definiría al $1$. Luego $\varphi_2(x) = \forall y\,\forall z\,((\varphi_0(z) \wedge S(z, y)) \to S(y, x))$ y, por recursión, $\varphi_n(x) = \forall y\,(\varphi_{n-1}(y) \to S(y, x))$.

### 8. Interpretaciones y propiedades de una relación (I1, 2019-2)
Con $\varphi_1$: refleja, $\varphi_2$: simétrica, $\varphi_3$: antisimétrica y $\varphi_4$: transitiva (sobre un predicado binario $R$), halle para cada $\varphi$ una interpretación que la satisfaga y otra que no: (a) $\varphi_1 \wedge \varphi_4$; (b) $\varphi_1 \wedge \varphi_2 \wedge \varphi_4$; (c) $\varphi_1 \wedge \varphi_3 \wedge \varphi_4$.

> [!example]- Solución
> Sobre $\mathbb{N}$. (a) Satisface: $R(x, y) := x \le y$ (refleja y transitiva). No satisface: $R(x, y) := x \ne y$, que no es refleja. (b) Satisface: $R(x, y) := x = y$ (refleja, simétrica y transitiva). No satisface: $\le$, que es refleja y transitiva pero no simétrica ($1 \le 2$ y no $2 \le 1$). (c) Satisface: $\le$ (refleja, antisimétrica y transitiva). No satisface: $\ne$, de nuevo por no ser refleja.

### 9. Una función binaria como predicado ternario (I1, 2025-1)
En un vocabulario con $R$ ternario, (1) halle $\phi$ tal que $\mathcal{A} \models \phi$ si y sólo si $R$ codifica una función binaria (para cada $(a, b)$ hay un único $c$ con $(a, b, c) \in R$); (2) halle $\psi$ que exprese que esa función es asociativa.

> [!example]- Solución
> (1) $\phi = \forall x\,\forall y\,\big[\exists z\,R(x, y, z) \wedge \neg\exists z_1\,\exists z_2\,(R(x, y, z_1) \wedge R(x, y, z_2) \wedge z_1 \ne z_2)\big]$: existencia y unicidad.
>
> (2) $\psi = \forall x\,\forall y\,\forall z\,\forall u\,\forall v\,\forall w\,\big[(R(x, y, u) \wedge R(u, z, v) \wedge R(y, z, w)) \to R(x, w, v)\big]$. Aquí $u = x \cdot y$, $v = u \cdot z$ y $w = y \cdot z$, y se exige $v = x \cdot w$.

### 10. Una tautología de primer orden (I1, 2026-1)
Demuestre que $\big[\forall x\,\forall y\,\forall z\,(A(x, y) \vee A(y, z) \vee A(z, x))\big] \to \forall x\,\forall y\,\big[A(x, y) \vee A(y, x) \vee (A(x, x) \wedge A(y, y))\big]$ es una tautología.

> [!example]- Solución
> Por contradicción: si fuera falsa en alguna interpretación (de dominio no vacío), el antecedente se cumple y existen $x_0, y_0$ con $A(x_0, y_0) = A(y_0, x_0) = 0$ y $A(x_0, x_0) \wedge A(y_0, y_0) = 0$, es decir, $A(x_0, x_0) = 0$ o $A(y_0, y_0) = 0$.
> - Si $A(x_0, x_0) = 0$, se instancia el antecedente en $(x, y, z) = (x_0, y_0, x_0)$: sus tres disyunciones $A(x_0, y_0)$, $A(y_0, x_0)$ y $A(x_0, x_0)$ son falsas, lo que contradice que el antecedente se cumple.
> - Si $A(y_0, y_0) = 0$, se instancia en $(y_0, x_0, y_0)$ y ocurre lo mismo con $A(y_0, x_0)$, $A(x_0, y_0)$ y $A(y_0, y_0)$.
>
> En ambos casos hay contradicción, luego la oración es verdadera en toda interpretación.

### 11. Formalizar con animales (I2, 2024-2)
Con $P(x)$: perro, $G(x)$: gato, $R(x, y)$: «$x$ persigue a $y$», escriba: (c) todo animal es perro o gato, pero no ambos; (d) todo gato persigue a lo más a dos perros.

> [!example]- Solución
> (c) $\forall x\,\big((P(x) \vee G(x)) \wedge \neg(P(x) \wedge G(x))\big)$. (d) «A lo más dos» se expresa diciendo que entre tres perros perseguidos por el mismo gato hay dos iguales: $\forall x\,\forall y_1\,\forall y_2\,\forall y_3\,\big[(G(x) \wedge P(y_1) \wedge P(y_2) \wedge P(y_3) \wedge R(x, y_1) \wedge R(x, y_2) \wedge R(x, y_3)) \to (y_1 = y_2 \vee y_2 = y_3 \vee y_1 = y_3)\big]$.

## Preguntas de repaso

> [!question]- ¿Cómo se decide entre demostrar y buscar un contramodelo al ver una «equivalencia»?
> Primero se intenta construir un contramodelo pequeño (dominio de dos elementos). Si cada intento falla y la estructura de las fórmulas sugiere que sí se reparten, se demuestra con una interpretación arbitraria en ambas direcciones.

> [!question]- ¿Cómo se expresa «hay a lo más $k$» y «hay al menos $k$» sin contar?
> «Al menos $k$»: $k$ variables existenciales con todas las desigualdades por pares. «A lo más $k$»: $\forall$ sobre $k+1$ variables, diciendo que dos de ellas coinciden.

> [!question]- ¿Qué trampa común hay al escribir cláusulas «para todo par $x, y$»?
> Olvidar los casos $x = y$ o el orden relativo de $x$ e $y$, de modo que la fórmula queda falsa en pares que el enunciado no pretendía excluir.
