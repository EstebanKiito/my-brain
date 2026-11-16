---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[05 - Traslaciones, alargamientos y contracciones]]"
---

# Reflexiones y transformaciones sucesivas

Las dos transformaciones que faltan son las reflexiones en los ejes. Con ellas se puede armar cualquier gráfico de la forma $y = a\,f(b(x - h)) + k$, a condición de aplicar las transformaciones **de una en una y en el orden correcto**. Las pruebas piden justamente eso: "identifique, en orden, las transformaciones y grafique cada paso".

## Reflexiones

> [!tip] Reflexiones en los ejes
> - $y = -f(x)$ refleja el gráfico de $y = f(x)$ respecto del eje $x$ (cambia el signo de las alturas).
> - $y = f(-x)$ refleja el gráfico de $y = f(x)$ respecto del eje $y$ (cambia el signo de las abscisas).

![Reflexiones en los ejes](adjuntos/Reflexiones%20en%20los%20ejes.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, una curva azul $y = f(x)$ y su imagen roja $y = -f(x)$, simétrica respecto del eje $x$. A la derecha, una curva azul creciente $y = f(x)$ en el lado derecho del eje $y$ y su imagen roja $y = f(-x)$ en el lado izquierdo, simétrica respecto del eje $y$.

Ejemplos: $f(x) = -x^2$ es la parábola que abre hacia abajo; $f(x) = \sqrt{-x}$ es la raíz reflejada, definida para $x \le 0$.

## El orden de las transformaciones

> [!tip] Regla para $g(x) = a\,f\big(b(x - h)\big) + k$
> Se aplican **de adentro hacia afuera**, una a la vez:
> 1. Escala y reflexión horizontal: $f(bx)$ (y $f(-x)$ si $b < 0$).
> 2. Traslación horizontal por $h$: $f(b(x - h))$.
> 3. Escala y reflexión vertical: $a\,f(\cdot)$.
> 4. Traslación vertical por $k$: $+ k$.

La clave de la parte horizontal es **factorizar $b$ antes de ver el desplazamiento**. Por ejemplo, $f(-x + 3) = f(-(x - 3))$: primero se refleja ($-x$) y después se traslada $3$ a la **derecha**, no a la izquierda. Del mismo modo $f(2x - 6) = f(2(x - 3))$ desplaza $3$, no $6$.

## Ejemplo completo: cinco pasos (clase 10)

Sea $f : [-2, 4] \to [-2, 2]$ la función de gráfico poligonal siguiente, y $g(x) = 2 - \tfrac{1}{2}f(-x + 3)$. Se pide las transformaciones y el dominio y recorrido de $g$.

![Función de partida del ejemplo de transformaciones sucesivas](adjuntos/Función%20de%20partida%20del%20ejemplo%20de%20transformaciones%20sucesivas.png)

> [!example]- Transcripción de la figura (clase 10)
> Una cuadrícula con una línea poligonal roja que parte del punto $(-2, -2)$, sube hasta el origen, baja hasta $(2, -2)$ y vuelve a subir hasta $(4, 2)$.

Se escribe $g(x) = -\tfrac{1}{2}f\big(-(x - 3)\big) + 2$ y se aplican, en este orden:

| Paso | Función | Transformación |
|---|---|---|
| 1 | $r(x) = f(-x)$ | reflexión respecto del eje $y$ |
| 2 | $h(x) = r(x - 3)$ | traslación $3$ unidades a la derecha |
| 3 | $\ell(x) = \tfrac{1}{2}h(x)$ | contracción vertical (factor $\tfrac{1}{2}$) |
| 4 | $m(x) = -\ell(x)$ | reflexión respecto del eje $x$ |
| 5 | $n(x) = m(x) + 2$ | traslación $2$ unidades hacia arriba |

Así $n(x) = -\tfrac{1}{2}f(-(x - 3)) + 2 = g(x)$.

![Función original y su reflexión en el eje Y](adjuntos/Función%20original%20y%20su%20reflexión%20en%20el%20eje%20Y.png)

> [!example]- Transcripción de la figura (clase 10)
> Dos gráficos en cuadrícula. A la izquierda, $y = f(x)$ (la poligonal con extremos $(-2, -2)$ y $(4, 2)$). A la derecha, $y = r(x) = f(-x)$: la misma poligonal reflejada respecto del eje $y$, con extremos $(2, -2)$ y $(-4, 2)$.

![Traslación y alargamiento vertical](adjuntos/Traslación%20y%20alargamiento%20vertical.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, $y = h(x) = r(x - 3)$: la poligonal reflejada, corrida $3$ unidades a la derecha. A la derecha, $y = \ell(x) = \tfrac{1}{2}h(x)$: la misma forma con todas las alturas reducidas a la mitad.

![Reflexión en el eje X y traslación final](adjuntos/Reflexión%20en%20el%20eje%20X%20y%20traslación%20final.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, $y = m(x) = -\ell(x)$: la poligonal anterior reflejada respecto del eje $x$. A la derecha, $y = n(x) = m(x) + 2 = g(x)$: esa poligonal subida $2$ unidades; es el gráfico final.

**Dominio y recorrido de $g$.** $f(-x + 3)$ está definida cuando $-2 \le -x + 3 \le 4$, es decir $-1 \le x \le 5$: $\operatorname{Dom}(g) = [-1, 5]$. Como $f$ toma valores en $[-2, 2]$, $\tfrac{1}{2}f$ los toma en $[-1, 1]$, $-\tfrac{1}{2}f$ también en $[-1, 1]$ y al sumar $2$ queda $\operatorname{Rec}(g) = [1, 3]$.

## Ejemplo con una raíz: $y = -1 - \sqrt{2 - x}$

Se parte de $\sqrt{x}$. Una secuencia válida es: (1) $\sqrt{-x}$ por reflexión en el eje $y$; (2) $\sqrt{-(x - 2)} = \sqrt{2 - x}$ al correr $2$ a la derecha; (3) $-\sqrt{2 - x}$ por reflexión en el eje $x$; (4) $-\sqrt{2 - x} - 1$ al bajar una unidad. También sirve invertir el orden de las reflexiones (1) y (3), pues una horizontal y una vertical conmutan; lo que **no** se puede es trasladar antes de reflejar horizontalmente.

> [!warning] Dónde se equivoca la gente
> - Trasladar "$-x + 3$" hacia la izquierda: hay que factorizar $-(x - 3)$.
> - Aplicar $-$ antes de la raíz cuando va después ($-\sqrt{x}$ no es $\sqrt{-x}$): lo primero refleja en el eje $x$, lo segundo en el eje $y$.
> - Olvidar que el dominio y el recorrido también se transforman: el nuevo dominio sale de la parte horizontal y el recorrido de la vertical.

## Preguntas de repaso

> [!question]- ¿Cuántas unidades y hacia dónde se traslada el gráfico de $f(2x - 6)$ respecto de $f(2x)$?
> Se factoriza $f(2(x - 3))$: se traslada $3$ unidades a la derecha respecto de $f(2x)$, no $6$.

> [!question]- ¿Qué transformaciones convierten el gráfico de $\sqrt{x}$ en el de $-1 - \sqrt{2 - x}$?
> Reflexión en el eje $y$, traslación $2$ a la derecha, reflexión en el eje $x$ y traslación $1$ hacia abajo (dominio $(-\infty, 2]$ y recorrido $(-\infty, -1]$).

> [!question]- ¿Por qué el dominio de $g(x) = 2 - \tfrac{1}{2}f(-x + 3)$ sale de resolver $-2 \le -x + 3 \le 4$?
> Porque $g(x)$ solo existe si $f$ está definida en $-x + 3$, es decir, si ese número pertenece al dominio $[-2, 4]$ de $f$.

> [!question]- ¿Conmutan una reflexión horizontal y una vertical? ¿Y una reflexión con una traslación del mismo eje?
> Una reflexión horizontal y una vertical sí conmutan (actúan sobre variables distintas). Una reflexión y una traslación del mismo eje **no**: $f(-(x - 3)) \neq f(-x - 3)$.
