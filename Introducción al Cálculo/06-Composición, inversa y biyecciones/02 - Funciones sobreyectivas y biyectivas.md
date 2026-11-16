---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones inyectivas y el test de la recta horizontal]]"
---

# Funciones sobreyectivas y biyectivas

La inyectividad dice que cada salida viene de a lo más una entrada; la sobreyectividad pide que **toda** posible salida (todo elemento del conjunto de llegada) se alcance. Una función con ambas propiedades, una biyección, establece una correspondencia uno a uno entre dominio y codominio, y es exactamente la que admite inversa.

## Sobreyectividad

> [!tip] Función sobreyectiva (o epiyectiva)
> $f : A \to B$ es **sobreyectiva** si $\operatorname{Rec}(f) = B$; es decir,
> $$(\forall y \in B)(\exists x \in A)\ f(x) = y.$$
> En términos de ecuaciones: para todo $y \in B$, la ecuación $f(x) = y$ tiene al menos una solución en $A$.

Para decidirlo se calcula el recorrido con el [[03 - Cómo hallar el recorrido de una función|método por definición]] y se compara con el codominio $B$ que **declara** el enunciado.

**$f : \mathbb{R} \to \mathbb{R}$, $f(x) = \dfrac{x}{x^2 + 1}$.** Ya se vio que $\operatorname{Rec}(f) = \left[-\tfrac{1}{2}, \tfrac{1}{2}\right] \neq \mathbb{R}$: no es sobreyectiva (por ejemplo, $f(x) = 1$ no tiene solución).

**$f : \mathbb{R} \to [-2, \infty)$, $f(x) = x^2 - 6x + 7$.** De $x^2 - 6x + (7 - y) = 0$ se obtiene $x = 3 \pm \sqrt{2 + y}$, que existe si y solo si $y \ge -2$. Luego $\operatorname{Rec}(f) = [-2, \infty)$ y $f$ **sí** es sobreyectiva.

> [!tip] Cambiar el codominio
> Una función siempre se puede hacer sobreyectiva **cambiando el codominio** a su recorrido: $f : A \to \operatorname{Rec}(f)$ es sobreyectiva por construcción. Es lo que piden los enunciados con "determine $B$ para que $f$ sea sobreyectiva".

## Biyecciones

> [!tip] Función biyectiva
> $f : X \to Y$ es **biyectiva** si es inyectiva y sobreyectiva; equivalentemente,
> $$(\forall y \in Y)(\exists!\, x \in X)\ f(x) = y.$$
> Es decir, para todo $b \in Y$ la ecuación $f(x) = b$ tiene **una única** solución en $X$.

**$f : (-\infty, 1] \to (-\infty, 2]$, $f(x) = -x^2 + 4x - 1$** (clase 13). Su forma normal es $f(x) = -(x - 2)^2 + 3$: en $(-\infty, 1]$ la parábola, que abre hacia abajo con vértice en $x = 2$, es estrictamente creciente, y $f(1) = 2$. Es inyectiva (estrictamente creciente) y su recorrido es $(-\infty, 2]$, el codominio dado: **sí es biyectiva**.

**$f : \mathbb{R} \to \mathbb{R}$, $f(x) = -\sqrt{x^2 + 4}$** (clase 13). Es par, con $f(-1) = f(1)$, así que no es inyectiva; y su recorrido es $(-\infty, -2]$, no todo $\mathbb{R}$, así que tampoco es sobreyectiva. **No es biyectiva**.

## Receta: de una función cualquiera a una biyección

1. Calcular $\operatorname{Dom}(f)$.
2. Decidir la inyectividad; si falla, **restringir el dominio** a un conjunto $A$ donde sea inyectiva.
3. Calcular el recorrido de $f|_A$ y tomar $B = f(A)$ como codominio.
4. Entonces $f : A \to B$ es biyectiva.

Ejemplo (I5, 2026-1): $f(x) = \dfrac{x + 1}{|x| - 1}$ en $\mathbb{R} \setminus \{-1, 1\}$. Para $x < 0$ vale $-1$ (constante, no inyectiva); para $x \ge 0$ es $\tfrac{x + 1}{x - 1}$, inyectiva. Los mayores $A$, $B$ con $f : A \to B$ biyectiva son $A = [0, 1) \cup (1, \infty)$ y $B = (-\infty, -1] \cup (1, \infty)$.

## Propiedades útiles

- Una función de $A$ en $B$ con $A$ y $B$ finitos solo puede ser biyección si $|A| = |B|$. Por eso no existe una biyección entre $\{1, 2, 3, 4\}$ y $\{1, 2\}$.
- $f : \mathbb{N} \to \mathbb{N}$, $f(n) = n^2$ es inyectiva pero no sobreyectiva ($3$ no es cuadrado de ningún natural).
- Hay biyecciones entre conjuntos infinitos "de distinto tamaño aparente", como $\mathbb{N} \to \mathbb{Z}$ con $f(n) = \tfrac{n}{2}$ si $n$ es par y $f(n) = -\tfrac{n - 1}{2}$ si $n$ es impar.

> [!warning] El codominio importa
> La misma regla $f(x) = x^2$ es sobreyectiva como $\mathbb{R} \to [0, \infty)$ pero no como $\mathbb{R} \to \mathbb{R}$. Para decidir sobreyectividad hay que mirar el codominio que dice el enunciado, no solo la fórmula.

## Preguntas de repaso

> [!question]- ¿Cómo se decide si $f : A \to B$ es sobreyectiva?
> Se calcula $\operatorname{Rec}(f)$ y se compara con $B$: es sobreyectiva si y solo si son iguales.

> [!question]- ¿Cómo se hace biyectiva una función que no lo es?
> Restringiendo el dominio hasta que sea inyectiva y reemplazando el codominio por el recorrido resultante.

> [!question]- ¿Por qué $f(x) = \frac{x}{x^2 + 1}$ restringida a $[-1, 1]$ y con codominio $\left[-\frac{1}{2}, \frac{1}{2}\right]$ es biyectiva?
> En $[-1, 1]$ es estrictamente creciente, así que es inyectiva, y su recorrido ahí es exactamente $\left[-\frac{1}{2}, \frac{1}{2}\right]$.

> [!question]- ¿Cuántas funciones biyectivas hay entre dos conjuntos finitos de $n$ elementos?
> $n!$: es el número de formas de emparejar cada elemento del primer conjunto con uno distinto del segundo.
