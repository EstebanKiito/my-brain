---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[05 - Inecuaciones con raíces cuadradas]]"
---

# Funciones, dominio, recorrido y gráfico

Una función es una regla que a cada elemento de un conjunto le asigna **exactamente uno** de otro conjunto. Todo el cálculo trabaja con ellas, y para hablar con precisión hace falta distinguir tres cosas que a menudo se confunden: dónde está definida (dominio), dónde puede tomar valores (codominio) y qué valores toma de verdad (recorrido).

## Definición

> [!tip] Función
> Una función $f : A \to B$ consta de un conjunto $A$ (**dominio**), un conjunto $B$ (**codominio**, donde cae la función) y una regla que a cada $x \in A$ le asocia un único $f(x) \in B$. En símbolos:
> $$(\forall x \in A)(\exists!\, y \in B)\ (y = f(x)).$$

La variable $x$ se llama independiente y $y = f(x)$, la imagen de $x$ (variable dependiente). Una regla como "a cada real $x > 0$ asociarle el triángulo de área $x$" **no** es función: hay infinitos triángulos de esa área, de modo que la imagen no está determinada.

> [!tip] Recorrido (o imagen)
> El **recorrido** de $f$ es el conjunto de valores que efectivamente toma:
> $$\operatorname{Rec}(f) = \{\, y \in \mathbb{R} \mid \exists\, x \in A \text{ tal que } y = f(x) \,\} \subseteq B.$$

En las clases a veces se llama "recorrido" al codominio $B$. Cuando se da solo la regla y no se dice $B$, se entiende que $B$ es justamente el recorrido: el menor conjunto que contiene a todos los valores. Las pruebas piden "recorrido (o rango, o conjunto imagen)" en este último sentido y exigen calcularlo **por definición**, no solo mirando el gráfico.

## Igualdad de funciones

Dos funciones son iguales si y solo si tienen el mismo dominio, el mismo codominio y la misma regla.

> [!warning] Misma fórmula no es misma función
> $f(x) = \dfrac{(x - 1)(x + 2)}{x - 1}$ y $g(x) = x + 2$ parecen iguales, pero no lo son: $\operatorname{Dom}(f) = \mathbb{R} \setminus \{1\}$ y $\operatorname{Dom}(g) = \mathbb{R}$. Simplificar un factor no autoriza a ignorar el valor $x = 1$.

## El gráfico y la prueba de la recta vertical

> [!tip] Gráfico
> El gráfico de $f : A \to B$ es el conjunto de pares $G(f) = \{(x, y) \in A \times B \mid y = f(x)\}$, una curva en $\mathbb{R}^2$. Dos funciones son iguales si y solo si tienen el mismo gráfico.

Como cada $x$ tiene una sola imagen, una curva del plano es el gráfico de una función si y solo si **ninguna recta vertical la corta más de una vez**.

![Curva que es gráfica de una función y curva que no lo es](adjuntos/Curva%20que%20es%20gráfica%20de%20una%20función%20y%20curva%20que%20no%20lo%20es.png)

> [!example]- Transcripción de la figura (clase 8)
> A la izquierda, una curva ondulada que la recta vertical punteada $x = a$ corta en un solo punto $(a, b)$: es la gráfica de una función. A la derecha, una curva con forma de lazo que la misma recta $x = a$ corta en dos puntos, $(a, b)$ y $(a, c)$: a un mismo $x = a$ le corresponderían dos valores, así que no es gráfica de una función.

## Dominio y recorrido en el gráfico

Proyectar el gráfico sobre el eje $x$ da el dominio y sobre el eje $y$ da el recorrido. Esto sirve para intuir, pero en una prueba el recorrido debe justificarse algebraicamente (ver [[03 - Cómo hallar el recorrido de una función|el método por definición]]).

## Preguntas de repaso

> [!question]- ¿Por qué $x^2 + y^2 = 4$ no es el gráfico de una función de $x$?
> Porque a $x = 0$ le corresponden dos valores, $y = 2$ e $y = -2$: la recta vertical $x = 0$ corta la circunferencia dos veces.

> [!question]- ¿Qué diferencia hay entre codominio y recorrido?
> El codominio $B$ es el conjunto declarado donde la función toma valores; el recorrido $\operatorname{Rec}(f) \subseteq B$ es el conjunto de valores que realmente alcanza. Por ejemplo, $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$ tiene codominio $\mathbb{R}$ y recorrido $[0, \infty)$.

> [!question]- ¿Por qué $f(x) = \frac{x^2 - 1}{x - 1}$ y $g(x) = x + 1$ son funciones distintas?
> Porque no tienen el mismo dominio: $f$ no está definida en $x = 1$ y $g$ sí. Coinciden en todos los puntos del dominio de $f$, pero eso no basta.

> [!question]- Si una regla asigna a cada persona sus hermanos, ¿es una función de personas a personas?
> No: una persona puede tener cero, uno o varios hermanos, y la definición exige exactamente una imagen.
