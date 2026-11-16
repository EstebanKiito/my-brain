---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones, dominio, recorrido y gráfico]]"
  - "[[03 - Cómo hallar el recorrido de una función]]"
---

# Funciones inyectivas y el test de la recta horizontal

Una función puede asignar el mismo valor a entradas distintas, o no. Las que **no** lo hacen se llaman inyectivas, y son las únicas que se pueden "deshacer": para recuperar $x$ a partir de $f(x)$ hace falta que cada salida provenga de una sola entrada. La inyectividad es el primer requisito para tener una inversa.

## Definición

> [!tip] Función inyectiva
> $f : A \to B$ es **inyectiva** si
> $$(\forall x_1, x_2 \in A)\ (x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)),$$
> o, por contrarrecíproca, si $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$.

La segunda forma es la que se usa para **demostrar** que una función es inyectiva: se supone $f(x_1) = f(x_2)$ y se despeja hasta llegar a $x_1 = x_2$. Para **refutar** la inyectividad basta un contraejemplo: dos entradas distintas con la misma imagen.

## El test de la recta horizontal

Si una recta horizontal corta el gráfico en más de un punto, hay $x_1 \neq x_2$ con la misma altura $f(x_1) = f(x_2)$.

![Dos puntos con la misma imagen cortados por una recta horizontal](adjuntos/Dos%20puntos%20con%20la%20misma%20imagen%20cortados%20por%20una%20recta%20horizontal.png)

> [!example]- Transcripción de la figura (clase 13)
> Una curva azul $y = f(x)$ en forma de colina, cortada por una recta horizontal roja en dos puntos, uno con abscisa $x_1$ (a la izquierda del máximo) y otro con $x_2$ (a la derecha). Líneas punteadas violetas bajan hasta el eje $x$ y suben hasta los valores $f(x_1)$ y $f(x_2)$, que coinciden.

> [!tip] Test de la recta horizontal
> Una función es inyectiva si y solo si **ninguna recta horizontal** corta su gráfico más de una vez.

Es el análogo del test de la recta vertical, que decide si una curva es gráfico de una función. Sirve para decidir con el dibujo; en una prueba "demuestre algebraicamente" exige el argumento con $f(x_1) = f(x_2)$.

## Ejemplos

**Un gráfico por tramos que falla el test (clase 13).** $f(x) = \begin{cases} 3x^2 + 1 & -1 \le x < 0 \\ \tfrac{x}{2} & 0 \le x \le 3 \end{cases}$.

![Gráfico de una función por tramos que no es inyectiva](adjuntos/Gráfico%20de%20una%20función%20por%20tramos%20que%20no%20es%20inyectiva.png)

> [!example]- Transcripción de la figura (clase 13)
> El primer tramo es un arco de parábola que baja desde el punto $(-1, 4)$ hasta un punto vacío en $(0, 1)$; el segundo es un segmento recto que sube desde $(0, 0)$ hasta $(3, \tfrac{3}{2})$. Una línea punteada horizontal a la altura $\tfrac{3}{2}$ une ambos tramos.

Los recorridos de los tramos son $(1, 4]$ y $\left[0, \tfrac{3}{2}\right]$, que se traslapan en $\left(1, \tfrac{3}{2}\right]$. Por ejemplo $f\!\left(-\tfrac{1}{\sqrt{6}}\right) = \tfrac{3}{6} + 1 = \tfrac{3}{2} = f(3)$, con $-\tfrac{1}{\sqrt{6}} \neq 3$: no es inyectiva.

**Un cociente.** $f(x) = \dfrac{x + 1}{x^2 + 1}$ no es inyectiva: $f(0) = 1 = f(1)$.

**Una cúbica con un cociente (demostración algebraica).** $h(x) = \dfrac{x^3}{1 + x^3}$ en $\mathbb{R} \setminus \{-1\}$ sí lo es. Si $h(x_1) = h(x_2)$, entonces $x_1^3(1 + x_2^3) = x_2^3(1 + x_1^3)$, que se reduce a $x_1^3 = x_2^3$, es decir $x_1 = x_2$ (la función $t \mapsto t^3$ es inyectiva).

**Una función de Möbius.** $f(x) = \dfrac{x + 3}{x - 1}$ en $\mathbb{R} \setminus \{1\}$: se reescribe $f(x) = 1 + \dfrac{4}{x - 1}$ y de $f(x_1) = f(x_2)$ sigue $\dfrac{4}{x_1 - 1} = \dfrac{4}{x_2 - 1}$, luego $x_1 = x_2$. En general las funciones $\tfrac{ax + b}{cx + d}$ con $ad \neq bc$ son inyectivas.

## Cómo conseguir inyectividad

> [!tip] Restringir el dominio
> Si $f$ no es inyectiva siempre se puede **restringir el dominio** a un conjunto donde lo sea. Por ejemplo, $x \mapsto x^2$ no es inyectiva en $\mathbb{R}$, pero sí en $[0, \infty)$. El mayor dominio en que $f$ es inyectiva no es único en general; en un problema se pide el "mayor" y se justifica que no se puede agrandar.

> [!warning] Una función constante en un tramo no es inyectiva
> Si $f$ es constante en un intervalo, como $f(x) = -1$ para todo $x < 0$ en $\frac{x+1}{|x|-1}$, hay infinitos pares con la misma imagen. Hay que recortar ese tramo.

## Preguntas de repaso

> [!question]- ¿Por qué $f(x) = x^2$ no es inyectiva en $\mathbb{R}$ pero sí en $[0, \infty)$?
> En $\mathbb{R}$, $f(-2) = f(2) = 4$. En $[0, \infty)$ no hay dos números distintos con el mismo cuadrado, pues $a^2 = b^2$ con $a, b \ge 0$ implica $a = b$.

> [!question]- ¿Cómo se demuestra que $f(x) = 2x + 5$ es inyectiva?
> Si $2x_1 + 5 = 2x_2 + 5$, restando $5$ y dividiendo por $2$ resulta $x_1 = x_2$.

> [!question]- ¿Qué muestra el test de la recta horizontal si una recta corta el gráfico tres veces?
> Que hay tres entradas distintas con la misma imagen, así que $f$ no es inyectiva.

> [!question]- ¿Es inyectiva $g(x) = |x|$ en $\mathbb{R}$? ¿Y en $[0, \infty)$?
> No en $\mathbb{R}$ ($g(-1) = g(1) = 1$); sí en $[0, \infty)$, donde $|x| = x$.
