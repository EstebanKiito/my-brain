---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - origen/complemento
prerrequisitos:
  - "[[04 - Álgebra y composición de funciones]]"
  - "[[03 - Funciones monótonas]]"
---

# Función inversa

La inversa de una función es la que "deshace" lo que la función hizo: si $f$ lleva $x$ a $y$, la inversa lleva $y$ de vuelta a $x$. Solo existe para funciones biyectivas, y calcularla es resolver la ecuación $y = f(x)$ para $x$, que en las pruebas se pide casi siempre junto con la demostración de que $f$ es biyectiva.

## Definición

> [!tip] Función inversa
> Si $f : A \to B$ es biyectiva, su **inversa** es la función $f^{-1} : B \to A$ determinada por
> $$(\forall x \in A)(\forall y \in B)\quad f^{-1}(y) = x \iff y = f(x).$$

Sus propiedades fundamentales son:
- $f^{-1}(f(x)) = x$ para todo $x \in A$, es decir $f^{-1} \circ f = \mathrm{id}_A$.
- $f(f^{-1}(y)) = y$ para todo $y \in B$, es decir $f \circ f^{-1} = \mathrm{id}_B$.
- $f^{-1}$ es biyectiva y $(f^{-1})^{-1} = f$.

> [!tip] Un criterio de recíproco
> Sean $f : A \to B$ y $g : B \to A$. De las tres condiciones (1) $g \circ f = \mathrm{id}_A$, (2) $f \circ g = \mathrm{id}_B$, (3) $g$ biyectiva, si se cumplen **dos cualesquiera**, entonces $f$ es biyectiva y $g = f^{-1}$.

Este criterio es una forma de demostrar biyectividad **sin** probar inyectividad y sobreyectividad por separado: se propone una candidata a inversa y se verifica que compone bien en ambos sentidos.

## Cómo calcular la inversa

> [!tip] Método
> 1. Escribir $y = f(x)$.
> 2. **Despejar $x$** en función de $y$ (si $f$ es biyectiva, hay una única solución en $A$).
> 3. Esa expresión es $f^{-1}(y)$. Si se quiere la fórmula con la variable habitual, se intercambian los nombres: $f^{-1}(x)$.

Al despejar se descubre también el dominio de la inversa, que es el codominio $B$ (el recorrido de $f$). Y cuando el despeje da dos soluciones (por una raíz cuadrada), se elige la que pertenece a $A$.

## Gráfica de la inversa

Como $(a, b)$ está en el gráfico de $f$ si y solo si $(b, a)$ está en el de $f^{-1}$, y $(b, a)$ es el reflejo de $(a, b)$ en la recta $y = x$:

> [!tip] Gráfica de $f^{-1}$
> El gráfico de $f^{-1}$ se obtiene **reflejando el de $f$ respecto de la recta $y = x$**.

![Gráfica de la inversa como reflexión en la recta y igual a x](adjuntos/Gráfica%20de%20la%20inversa%20como%20reflexión%20en%20la%20recta%20y%20igual%20a%20x.png)

> [!example]- Transcripción de la figura (clase 15)
> A la izquierda, la recta naranja $y = x$ con dos curvas simétricas respecto de ella: una azul $y = f(x)$, por debajo, y una roja $y = f^{-1}(x)$, por encima, que es su reflejo. A la derecha, la recta $y = x$ con los puntos $(a, b)$ y $(b, a)$ unidos por un segmento perpendicular a la recta, con marcas que indican que están a igual distancia de ella.

## Ejemplos resueltos

**Una raíz cuarta (clase 15).** $h : [0, \infty) \to (-\infty, -2]$, $h(x) = -\sqrt{x^4 + 4}$. Es biyectiva: $x^4 + 4$ es estrictamente creciente en $[0, \infty)$ con recorrido $[4, \infty)$, de modo que $h$ es estrictamente decreciente con recorrido $(-\infty, -2]$. De $y = -\sqrt{x^4 + 4}$ se obtiene $y^2 = x^4 + 4$ y, como $x \ge 0$, $x = \sqrt[4]{y^2 - 4}$. Así $h^{-1} : (-\infty, -2] \to [0, \infty)$, $h^{-1}(y) = \sqrt[4]{y^2 - 4}$.

**Una función por tramos (clase 15).** $f(x) = \begin{cases} -3x^2 + 1 & x < 0 \\ 3x + 2 & x \ge 0 \end{cases}$. El primer tramo es estrictamente creciente con recorrido $(-\infty, 1)$ y el segundo con recorrido $[2, \infty)$; los recorridos no se traslapan, así que $f$ es inyectiva, pero su recorrido no es $\mathbb{R}$ (no toma valores en $[1, 2)$). Con $B = (-\infty, 1) \cup [2, \infty)$ es biyectiva y
$$f^{-1}(y) = \begin{cases} -\sqrt{\tfrac{1 - y}{3}} & y < 1 \\ \tfrac{y - 2}{3} & y \ge 2 \end{cases}$$

**Con una raíz y un cociente (clase 15).** $f(x) = \dfrac{x}{2} + \sqrt{\dfrac{x^2}{4} - 1}$ tiene dominio $|x| \ge 2$. Con $f(-2) = -1$, $f(2) = 1$, la rama izquierda decrece de $0^-$ a $-1$ y la derecha crece de $1$ a $\infty$: $f$ es inyectiva y $\operatorname{Rec}(f) = [-1, 0) \cup [1, \infty)$. De $y - \tfrac{x}{2} = \sqrt{\tfrac{x^2}{4} - 1}$, elevando al cuadrado, $y^2 - xy + 1 = 0$, o sea $x = \tfrac{y^2 + 1}{y} = y + \tfrac{1}{y}$. Se comprueba que $y - \tfrac{x}{2} = \tfrac{y^2 - 1}{2y} \ge 0$ exactamente en $[-1, 0) \cup [1, \infty)$. Luego $f^{-1}(y) = y + \tfrac{1}{y}$.

**Inversa de una cúbica con raíces (clase 15).** $g(x) = \sqrt[3]{x + \sqrt{1 + x^2}} + \sqrt[3]{x - \sqrt{1 + x^2}}$. Con $a$ y $b$ las dos raíces cúbicas, $a^3 + b^3 = 2x$ y $ab = \sqrt[3]{x^2 - (1 + x^2)} = -1$. Si $y = a + b$, entonces $y^3 = a^3 + b^3 + 3ab(a + b) = 2x - 3y$, de modo que $x = \dfrac{y^3 + 3y}{2}$: $g^{-1}(y) = \dfrac{y^3 + 3y}{2}$. Se verifica $g(g^{-1}(y)) = y$ y $g^{-1}(g(x)) = x$ y se concluye que $g$ es biyectiva con el criterio del recíproco.

## Algunas inversas que aparecen en las pruebas

| Función | Inversa | Dominio de la inversa |
|---|---|---|
| $\dfrac{x + 1}{x - 1}$ | $\dfrac{y + 1}{y - 1}$ (es su propia inversa) | $y \neq 1$ |
| $\dfrac{3x - 2}{3 - 2x}$ | $\dfrac{2 + 3y}{3 + 2y}$ | $y \neq -\tfrac{3}{2}$ |
| $\dfrac{x^3}{1 + x^3}$ | $\sqrt[3]{\dfrac{y}{1 - y}}$ | $y \neq 1$ |
| $\dfrac{x}{\lvert x \rvert + 1}$ en $\mathbb{R} \to (-1, 1)$ | $\dfrac{y}{1 - \lvert y \rvert}$ | $(-1, 1)$ |
| $\sqrt{\dfrac{2x - 3}{x + 4}}$ | $\dfrac{4y^2 + 3}{2 - y^2}$ | $[0, \sqrt{2}) \cup (\sqrt{2}, \infty)$ |

> [!warning] Errores frecuentes
> - Calcular la inversa sin comprobar que la función es biyectiva (o sin restringir dominio y codominio primero).
> - Confundir $f^{-1}(x)$ con $\dfrac{1}{f(x)}$: no tienen relación.
> - Quedarse con la solución equivocada al despejar una raíz: se elige la que cae en el dominio $A$ de $f$ (por ejemplo, $x \le 1$ en vez de $x \ge 3$).

## Preguntas de repaso

> [!question]- ¿Por qué solo las funciones biyectivas tienen inversa?
> Para que $f^{-1}$ esté definida en todo $B$ hace falta que cada $y \in B$ tenga una preimagen (sobreyectividad), y para que sea una función hace falta que sea única (inyectividad).

> [!question]- ¿Cómo se obtiene el gráfico de $f^{-1}$ a partir del de $f$?
> Reflejándolo respecto de la recta $y = x$: cada punto $(a, b)$ pasa a $(b, a)$.

> [!question]- ¿Cuál es la inversa de $f(x) = -x^2 + 4x - 1$ con $f : (-\infty, 1] \to (-\infty, 2]$?
> De $y = -(x - 2)^2 + 3$ sale $x = 2 \pm \sqrt{3 - y}$; como $x \le 1$, se toma el signo menos: $f^{-1}(y) = 2 - \sqrt{3 - y}$ para $y \le 2$.

> [!question]- ¿Qué verifica el criterio del recíproco al proponer una candidata $g$?
> Que $g(f(x)) = x$ y $f(g(y)) = y$; con eso $f$ es biyectiva y $g = f^{-1}$, sin demostrar inyectividad y sobreyectividad por separado.
