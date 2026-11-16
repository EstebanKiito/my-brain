---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - origen/complemento
prerrequisitos:
  - "[[05 - Función inversa]]"
---

# El número e y la función exponencial

La función exponencial es la que describe todo lo que crece o decae en proporción a su tamaño: poblaciones, intereses, enfriamientos. Se construye a partir de un número especial, $e$, que no se define con una fórmula cerrada sino como el valor al que se acerca una sucesión.

## El número e

Para $n$ cada vez más grande, el valor de $\left(1 + \tfrac{1}{n}\right)^n$ se acerca a un número fijo:

| $n$ | $\left(1 + \tfrac{1}{n}\right)^n$ |
|---|---|
| $1$ | $2$ |
| $5$ | $2{,}48832$ |
| $10$ | $2{,}59374$ |
| $100$ | $2{,}70481$ |
| $10\,000$ | $2{,}71815$ |
| $1\,000\,000$ | $2{,}71828$ |

> [!tip] La constante de Euler
> $$e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n \approx 2{,}718281828459\ldots$$
> Es un número **irracional**: no se puede escribir exactamente como decimal.

Esa lista de valores es una **sucesión** $a_n = \left(1 + \tfrac{1}{n}\right)^n$, una función $a : \mathbb{N} \to \mathbb{R}$ (se escribe $a_n$ en vez de $a(n)$). Que sus valores se acerquen a $e$ significa que la sucesión **converge** a $e$; las sucesiones y los límites se estudian con detalle más adelante.

## La función exponencial

> [!tip] Función exponencial
> $\exp : \mathbb{R} \to \mathbb{R}$, $\exp(x) = e^x$.

Cumple $e^{x + y} = e^x e^y$, $e^0 = 1$ y $e^{-x} = \tfrac{1}{e^x}$. Su dominio es $\mathbb{R}$, es siempre positiva, estrictamente creciente (se demuestra en la [[02 - Desigualdad fundamental y propiedades de la exponencial|nota siguiente]]) y su recorrido es $(0, \infty)$.

![Gráfica de la exponencial y la recta y igual a x más 1](adjuntos/Gráfica%20de%20la%20exponencial%20y%20la%20recta%20y%20igual%20a%20x%20más%201.png)

> [!example]- Transcripción de la figura (clase 16)
> En azul, la curva $y = e^x$: pegada al eje $x$ por la izquierda (tiende a $0$ pero nunca lo toca), pasa por el punto $(0, 1)$ y crece cada vez más rápido hacia la derecha. En rojo, la recta $y = x + 1$, que corta el eje $y$ también en $(0, 1)$ y queda **por debajo** de la curva en todo punto salvo en $x = 0$, donde se tocan.

La recta $y = x + 1$ es justamente la desigualdad fundamental $e^x \ge 1 + x$.

## Gráficos a partir de $e^x$

Con las transformaciones de funciones se obtienen otros gráficos:

- $g(x) = e^{-x}$ es la reflexión de $e^x$ respecto del eje $y$: decae hacia $0$ cuando $x \to \infty$ y crece sin cota hacia la izquierda.
- $h(x) = \dfrac{10}{1 + e^{-x}}$ es una curva **logística** (en forma de S). Como $e^{-x} > 0$, el denominador está en $(1, \infty)$ y $0 < h(x) < 10$. Cuando $x \to -\infty$, $e^{-x} \to \infty$ y $h \to 0$; cuando $x \to \infty$, $e^{-x} \to 0$ y $h \to 10$. Pasa por $h(0) = 5$ y es estrictamente creciente. Tiene dos asíntotas horizontales, $y = 0$ e $y = 10$.

## Un modelo: una epidemia (clase 16)

El número de personas contagiadas $t$ días después del inicio en una ciudad de $10\,000$ habitantes es $v(t) = \dfrac{10\,000}{5 + 1245\,e^{-0{,}97t}}$.

- **Contagiados al inicio:** $v(0) = \dfrac{10\,000}{5 + 1245} = 8$ personas.
- **Comportamiento:** para $t$ grande, $e^{-0{,}97t} \to 0$ y $v(t) \to \dfrac{10\,000}{5} = 2000$. El número de contagiados crece de $8$ hacia $2000$, de forma lenta al principio, rápida en la mitad y lenta al final (curva logística), sin llegar nunca a $2000$.

> [!warning] $e^x$ no es una potencia como $x^e$
> En $e^x$ la variable está en el **exponente** y la base es constante; en $x^2$ o $x^e$ es al revés. Por eso $e^x$ crece más rápido que cualquier potencia de $x$ y nunca vale $0$ ni negativo.

## Preguntas de repaso

> [!question]- ¿Qué significa que $\left(1 + \frac{1}{n}\right)^n$ converge a $e$?
> Que al hacer $n$ arbitrariamente grande los términos de la sucesión se acercan tanto como se quiera al número $e \approx 2{,}71828$.

> [!question]- ¿Cuál es el recorrido de $e^x$ y por qué no incluye al $0$?
> $(0, \infty)$. La exponencial se acerca a $0$ cuando $x \to -\infty$ pero $e^x > 0$ siempre, así que $0$ no se alcanza.

> [!question]- ¿Cuánto vale $\lim_{x \to \infty} \frac{10}{1 + e^{-x}}$?
> $10$: $e^{-x} \to 0$ y el cociente tiende a $\frac{10}{1}$. Es la asíntota horizontal superior de la curva logística.

> [!question]- ¿Por qué el gráfico de $e^x$ queda sobre el de $x + 1$?
> Porque $e^x \ge 1 + x$ para todo real, con igualdad solo en $x = 0$.
