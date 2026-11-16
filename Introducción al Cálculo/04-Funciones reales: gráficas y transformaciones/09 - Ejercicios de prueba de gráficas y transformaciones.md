---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Reflexiones y transformaciones sucesivas]]"
  - "[[08 - Ejercicios de prueba de dominio y recorrido]]"
---

# Ejercicios de prueba de gráficas y transformaciones

Preguntas de interrogaciones de 2020 a 2026 que piden **graficar**: funciones por tramos, valores absolutos de cuadráticas y secuencias de transformaciones a partir de una función conocida. Las pautas puntúan cada transformación y cada gráfico intermedio, con los puntos de corte con los ejes marcados. Solo se permite una transformación por paso.

## Ejercicios

### 1. Una raíz con dos reflexiones (I3, 2022-1; I3, 2023-1)
La gráfica de $f(x) = -1 - \sqrt{2 - x}$ se obtiene de $g(x) = \sqrt{x}$ por transformaciones. Indíquelas en orden y grafique cada paso, con los cortes con los ejes.

> [!example]- Solución
> Una secuencia válida (la pauta de 2022 usa esta; la de 2023 intercambia las dos reflexiones):
> 1. $h(x) = g(-x) = \sqrt{-x}$: reflexión respecto del eje $y$. Dominio $(-\infty, 0]$; corta en $(0, 0)$.
> 2. $\ell(x) = h(x - 2) = \sqrt{2 - x}$: traslación $2$ unidades a la derecha. Cortes: $(2, 0)$ y $(0, \sqrt{2})$.
> 3. $\varphi(x) = -\ell(x) = -\sqrt{2 - x}$: reflexión respecto del eje $x$. Cortes: $(2, 0)$ y $(0, -\sqrt{2})$.
> 4. $f(x) = \varphi(x) - 1 = -1 - \sqrt{2 - x}$: traslación una unidad hacia abajo. **No corta el eje $x$** (porque $-1 - \sqrt{2 - x} \le -1 < 0$) y corta el eje $y$ en $(0, -1 - \sqrt{2})$. Dominio $(-\infty, 2]$ y recorrido $(-\infty, -1]$.

### 2. La hipérbola desplazada (I4, 2025-1)
La gráfica de $f(x) = -1 - \dfrac{1}{2 - x}$ se obtiene de $g(x) = \dfrac{1}{x}$ por transformaciones. Identifíquelas y grafique cada paso, indicando los cortes con los ejes.

> [!example]- Solución
> Se reescribe $f(x) = \dfrac{1}{x - 2} - 1$, porque $-\dfrac{1}{2 - x} = \dfrac{1}{x - 2}$. La forma más corta es: (1) $g(x - 2) = \dfrac{1}{x - 2}$, traslación $2$ a la derecha; (2) restar $1$, traslación una unidad hacia abajo. La pauta también acepta la versión larga (reflejar en $y$, reflejar en $x$, trasladar), en la que las dos reflexiones se cancelan porque $\tfrac{1}{x}$ es impar: $-g(-x) = g(x)$.
> Resultado: asíntota vertical $x = 2$ y horizontal $y = -1$. Corte con el eje $x$: $\tfrac{1}{x - 2} = 1 \Rightarrow x = 3$, el punto $(3, 0)$. Corte con el eje $y$: $f(0) = -\tfrac{1}{2} - 1 = -\tfrac{3}{2}$, el punto $\left(0, -\tfrac{3}{2}\right)$.

### 3. Un triángulo reescalado y reflejado (I3, 2020-1)
Sea $f : [0, 2] \to \mathbb{R}$ con $f(x) = x$ si $x \in [0, 1]$ y $f(x) = 2 - x$ si $x \in (1, 2]$. (a) Grafique $f$. (b) Grafique $g(x) = 3f(1 - 2x)$ detallando el razonamiento.

> [!example]- Solución
> (a) Dos segmentos: de $(0, 0)$ a $(1, 1)$ y de $(1, 1)$ a $(2, 0)$: un triángulo de altura $1$ y base $[0, 2]$.
> (b) Se factoriza $f(1 - 2x) = f\!\left(-2\left(x - \tfrac{1}{2}\right)\right)$ y se aplican, en orden: reflexión respecto del eje $y$, contracción horizontal en factor $\tfrac{1}{2}$, traslación $\tfrac{1}{2}$ a la derecha y alargamiento vertical en factor $3$. El resultado es un triángulo de base $\left[-\tfrac{1}{2}, \tfrac{1}{2}\right]$ (se exige $0 \le 1 - 2x \le 2$) y altura $3$ en $x = 0$: $g(-\tfrac{1}{2}) = 3f(2) = 0$, $g(0) = 3f(1) = 3$, $g(\tfrac{1}{2}) = 3f(0) = 0$. $\operatorname{Dom}(g) = \left[-\tfrac{1}{2}, \tfrac{1}{2}\right]$ y $\operatorname{Rec}(g) = [0, 3]$.

### 4. Función por tramos y un valor absoluto (I4, 2026-1)
Determine el dominio, el recorrido y trace un gráfico cualitativo de (a) $f(x) = \begin{cases} (x + 2)^4 - 1 & x \le -2 \\ x + 1 & -2 < x \le 0 \\ \sqrt{1 - x^2} & x > 0 \end{cases}$ y (b) $g(x) = |x^2 - x - 1|$.

> [!example]- Solución
> (a) El último tramo exige $1 - x^2 \ge 0$, o sea $x \le 1$: $\operatorname{Dom}(f) = (-\infty, 1]$. Los tramos son: $x^4$ trasladado $2$ a la izquierda y $1$ hacia abajo (con mínimo $-1$ en $x = -2$), la recta $x + 1$ (de $-1$ a $1$) y el cuarto de circunferencia $\sqrt{1 - x^2}$ (de $1$ a $0$). Los tramos empalman en $x = -2$ (valor $-1$ en ambos) y en $x = 0$ (valor $1$). El primer tramo cubre $[-1, \infty)$, que contiene a los otros: $\operatorname{Rec}(f) = [-1, \infty)$.
>
> ![Gráfico cualitativo de una función definida por tramos](adjuntos/Gráfico%20cualitativo%20de%20una%20función%20definida%20por%20tramos.png)
>
> (b) $\operatorname{Dom}(g) = \mathbb{R}$. $g(x) = 0$ en $x = \tfrac{1 \pm \sqrt{5}}{2}$; fuera de ese intervalo la cuadrática es positiva y $g$ coincide con ella; dentro es negativa y $g = -(x^2 - x - 1)$ (se refleja respecto del eje $x$). El gráfico es una parábola con la parte central "doblada hacia arriba". $\operatorname{Rec}(g) = [0, \infty)$.
>
> ![Gráfico del valor absoluto de una cuadrática](adjuntos/Gráfico%20del%20valor%20absoluto%20de%20una%20cuadrática.png)

> [!example]- Transcripción de las dos figuras (pauta I4, 2026-1)
> Primera figura: una curva que baja desde arriba a la izquierda, corta el eje $x$ en $-3$, llega a un mínimo de $-1$ en $x = -2$, sube en línea recta (cortando el eje $x$ en $-1$) hasta $(0, 1)$ y desde ahí baja como un cuarto de circunferencia hasta $(1, 0)$. Segunda figura: una "W" suave: parte alta a la izquierda, baja hasta tocar el eje $x$ en $\approx -0{,}62$, sube hasta un máximo local de $\approx 1{,}25$ en $x = 0{,}5$, baja hasta tocar el eje $x$ en $\approx 1{,}62$ y sube de nuevo.

### 5. Una función por tramos con un hueco (I2, 2022-1)
Sea $f(x) = \begin{cases} x^3 & -1 \le x \le 1 \\ -x^2 + 2 & 1 < x < 2 \\ x - 1 & 2 < x \le 4 \end{cases}$. Grafique $f$ y determine su dominio y su recorrido.

> [!example]- Solución
> Tramos: la cúbica de $(-1, -1)$ a $(1, 1)$; la parábola $-x^2 + 2$ que empalma en $(1, 1)$ y baja hacia $(2, -2)$ con punto vacío; la recta $x - 1$ que parte de $(2, 1)$ (punto vacío) y sube hasta $(4, 3)$. El valor $x = 2$ no tiene imagen, así que $\operatorname{Dom}(f) = [-1, 2) \cup (2, 4]$.
> Recorridos de los tramos: $[-1, 1]$, $(-2, 1)$ y $(1, 3]$. Su unión es $\operatorname{Rec}(f) = (-2, 3]$: el $-2$ no se alcanza (extremo vacío) y el $1$ lo toma el primer tramo.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 2 las dos reflexiones "se cancelan"?
> Porque $g(x) = \frac{1}{x}$ es impar: $g(-x) = -g(x)$, y reflejar en $y$ y luego en $x$ devuelve el mismo gráfico: $-g(-x) = g(x)$.

> [!question]- ¿Cómo se obtiene el dominio de $g(x) = 3f(1 - 2x)$?
> Se exige que $1 - 2x$ pertenezca al dominio $[0, 2]$ de $f$: $0 \le 1 - 2x \le 2 \iff -\tfrac{1}{2} \le x \le \tfrac{1}{2}$.

> [!question]- ¿Qué distingue el gráfico de $|x^2 - x - 1|$ del de $x^2 - x - 1$?
> Donde la cuadrática es negativa (entre sus raíces) el valor absoluto la refleja respecto del eje $x$; fuera de ese intervalo coinciden. El resultado nunca baja del eje $x$.

> [!question]- ¿Por qué el recorrido del ejercicio 5 es $(-2, 3]$ y no $[-2, 3]$?
> Porque el valor $-2$ solo se acercaría con $x = 2$ por el segundo tramo, pero $2$ no pertenece al dominio: queda como extremo abierto.
