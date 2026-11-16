---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Cómo hallar el dominio de una función]]"
---

# Cómo hallar el recorrido de una función

El recorrido es más difícil de hallar que el dominio: no se lee de la fórmula, hay que descubrir qué valores $y$ se alcanzan. El método estándar, que las pruebas exigen cuando piden "calcular por definición", consiste en **despejar $x$ en función de $y$** y ver para qué $y$ ese despeje produce un $x$ válido (en el dominio).

## El método

> [!tip] Recorrido por definición
> $y \in \operatorname{Rec}(f) \iff (\exists\, x \in \operatorname{Dom}(f))\ \ f(x) = y.$
> 1. Plantear la ecuación $f(x) = y$ y despejar $x$ (o reducirla a una ecuación en $x$ con parámetro $y$).
> 2. Encontrar las condiciones sobre $y$ para que esa ecuación tenga solución.
> 3. **Comprobar** que la solución $x$ cae en el dominio y que realmente satisface $f(x) = y$ (elevar al cuadrado puede introducir soluciones falsas).

## Ejemplo 1: una raíz desplazada

$f : [1, \infty) \to \mathbb{R}$, $f(x) = \sqrt{x - 1} + 3$. De $\sqrt{x - 1} + 3 = y$ se obtiene $\sqrt{x - 1} = y - 3$, y elevando al cuadrado, $x = (y - 3)^2 + 1$. Ese $x$ es siempre $\ge 1$, pero hay que comprobar que $f(x) = y$:
$$f\big((y - 3)^2 + 1\big) = \sqrt{(y - 3)^2} + 3 = |y - 3| + 3,$$
que es igual a $y$ **solo si** $y \ge 3$. Luego $\operatorname{Rec}(f) = [3, \infty)$.

## Ejemplo 2: un cociente con discriminante

$f(x) = \dfrac{x}{x^2 + 1}$ en $\mathbb{R}$. Se plantea $y = \dfrac{x}{x^2 + 1}$, que equivale a $yx^2 - x + y = 0$. Si $y = 0$, la ecuación da $x = 0$: sirve. Si $y \neq 0$ es una cuadrática en $x$ con solución real si y solo si su discriminante es $\ge 0$: $1 - 4y^2 \ge 0 \iff -\tfrac{1}{2} \le y \le \tfrac{1}{2}$. Como $y = 0$ ya está incluido, $\operatorname{Rec}(f) = \left[-\tfrac{1}{2}, \tfrac{1}{2}\right]$.

## Ejemplo 3: suma de un número y su inverso

$f(x) = x + \dfrac{1}{x}$ con $x \neq 0$. De $y = x + \tfrac{1}{x}$ se obtiene $x^2 - yx + 1 = 0$, que tiene solución real si y solo si $y^2 - 4 \ge 0 \iff |y| \ge 2$. Además esa solución nunca es $x = 0$ (en $x = 0$ la cuadrática vale $1 \neq 0$), así que no hay que descartar nada. $\operatorname{Rec}(f) = (-\infty, -2] \cup [2, \infty)$. Lo mismo ocurre con $\dfrac{x^2 + 1}{x}$.

## Ejemplo 4: una cuadrática (vértice)

$f(x) = 3x^2 + 6x + 1 = 3(x + 1)^2 - 2$ es una parábola que abre hacia arriba con vértice en $(-1, -2)$, luego $\operatorname{Rec}(f) = [-2, \infty)$. En general, para $ax^2 + bx + c$ el vértice está en $x_v = -\tfrac{b}{2a}$ y el recorrido es $[f(x_v), \infty)$ si $a > 0$ y $(-\infty, f(x_v)]$ si $a < 0$.

## Ejemplo 5: raíz de una cuadrática y condición del signo

$f(x) = \sqrt{2x - x^2}$ tiene dominio $[0, 2]$. Si $y = \sqrt{2x - x^2}$, entonces $y \ge 0$ y $y^2 = 2x - x^2$, es decir $x^2 - 2x + y^2 = 0$. Esa ecuación tiene solución si $4 - 4y^2 \ge 0$, o sea $-1 \le y \le 1$; con $y \ge 0$ queda $y \in [0, 1]$, y para esos valores $x = 1 - \sqrt{1 - y^2} \in [0, 1]$ está en el dominio. $\operatorname{Rec}(f) = [0, 1]$. Geométricamente $y^2 + (x - 1)^2 = 1$ es la semicircunferencia superior de centro $(1, 0)$.

## Lo que muestra el gráfico

El gráfico permite **verificar** o intuir el resultado: la proyección sobre el eje $y$ es el recorrido.

![Dominio y recorrido sobre los ejes de la gráfica](adjuntos/Dominio%20y%20recorrido%20sobre%20los%20ejes%20de%20la%20gráfica.png)

> [!example]- Transcripción de la figura (clase 9)
> Una curva $y = f(x)$ con un punto de inicio y uno final. Una franja azul sobre el eje $x$ marca el **dominio** (la proyección horizontal de la curva) y una franja violeta sobre el eje $y$ marca el **recorrido** (la proyección vertical). Líneas punteadas unen los extremos de la curva con ambas franjas.

Un caso típico es $f(x) = \sqrt{4 - x^2}$: de $y = \sqrt{4 - x^2}$ se obtiene $x^2 + y^2 = 4$ con $y \ge 0$, la semicircunferencia superior de radio $2$.

![Gráfica de la raíz de 4 menos x al cuadrado](adjuntos/Gráfica%20de%20la%20raíz%20de%204%20menos%20x%20al%20cuadrado.png)

> [!example]- Transcripción de la figura (clase 9)
> Una semicircunferencia roja sobre el eje $x$, de centro el origen y radio $2$, que une los puntos $(-2, 0)$ y $(2, 0)$ pasando por $(0, 2)$. Una llave inferior indica $\text{Dominio} = [-2, 2]$ y una llave a la derecha indica $\text{Rango} = [0, 2]$.

> [!warning] Una prueba no se justifica solo con el dibujo
> Las pautas de varias pruebas dicen explícitamente que deducir el recorrido a partir del gráfico "no tiene puntaje" cuando piden calcularlo por definición. El gráfico sirve para saber qué respuesta esperar y comprobarla.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejemplo 1 hay que verificar $f(x) = y$ después de despejar?
> Porque al elevar al cuadrado se pierde el signo: el $x$ obtenido cumple $\sqrt{x - 1} = |y - 3|$, que coincide con $y - 3$ solo si $y \ge 3$.

> [!question]- ¿Cómo se prueba que $x + \tfrac{1}{x}$ nunca toma valores en $(-2, 2)$?
> Porque $y = x + \frac{1}{x}$ implica $x^2 - yx + 1 = 0$, con discriminante $y^2 - 4$. Para $|y| < 2$ es negativo y no hay solución real.

> [!question]- ¿Cuál es el recorrido de $f(x) = \frac{1}{x}$ y por qué falta el $0$?
> Es $\mathbb{R} \setminus \{0\}$: de $y = \frac{1}{x}$ se despeja $x = \frac{1}{y}$, que existe si y solo si $y \neq 0$.

> [!question]- ¿Qué recorrido tiene una parábola $f(x) = ax^2 + bx + c$?
> Si $a > 0$, $[f(x_v), \infty)$; si $a < 0$, $(-\infty, f(x_v)]$, donde $x_v = -\frac{b}{2a}$ es la abscisa del vértice.
