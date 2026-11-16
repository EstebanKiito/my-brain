---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[04 - Axioma del supremo y propiedad arquimediana]]"
  - "[[03 - Vecindades e intervalos con valor absoluto]]"
---

# Definición de límite de una sucesión

Decir que los términos de una sucesión "se acercan cada vez más" a un número $L$ es una idea intuitiva; el cálculo la vuelve precisa con una definición con $\varepsilon$ y $N$. Esa definición es la base de todo lo que sigue (álgebra de límites, sándwich, series, derivadas), y aprender a **usarla** es una habilidad que se evalúa explícitamente.

## La idea

Una sucesión es una función con dominio $\mathbb{N}$, así que su gráfico es una nube de puntos aislados $(1, a_1), (2, a_2), \ldots$ Por ejemplo, $a_n = \tfrac{n}{n + 1}$ da los valores $\tfrac{1}{2}, \tfrac{2}{3}, \tfrac{3}{4}, \ldots$ que suben y se acercan a $1$.

![Gráfica de la sucesión n sobre n más 1](adjuntos/Gráfica%20de%20la%20sucesión%20n%20sobre%20n%20más%201.png)

> [!example]- Transcripción de la figura (clase 21)
> Puntos rojos aislados sobre las abscisas $1, 2, 3, \ldots$ que van subiendo y se acercan a la recta punteada horizontal $a_n = 1$ sin tocarla. Una llave marca el valor $a_7 = \tfrac{7}{8}$ con un segmento naranja desde el eje hasta el punto.

La distancia entre $a_n$ y $1$ es $|1 - a_n| = \left|1 - \tfrac{n}{n + 1}\right| = \tfrac{1}{n + 1}$, que se hace cada vez más pequeña al crecer $n$. Eso se escribe $\displaystyle\lim_{n \to \infty}\frac{n}{n + 1} = 1$.

## La definición

> [!tip] Límite de una sucesión
> $\displaystyle\lim_{n \to \infty} a_n = L$ si
> $$(\forall \varepsilon > 0)(\exists N \in \mathbb{N})\ \big(n > N \Rightarrow |a_n - L| < \varepsilon\big).$$
> Una sucesión que tiene límite se llama **convergente**; en caso contrario, **divergente**.

Se lee: para cualquier error $\varepsilon > 0$ que se quiera tolerar, existe un índice $N$ a partir del cual **todos** los términos están a distancia menor que $\varepsilon$ de $L$.

Como $|a_n - L| < \varepsilon \iff -\varepsilon < a_n - L < \varepsilon \iff L - \varepsilon < a_n < L + \varepsilon$, el límite dice que, a partir de $N$, todos los términos caen en la **franja** $(L - \varepsilon, L + \varepsilon)$, la vecindad de radio $\varepsilon$ ([[03 - Vecindades e intervalos con valor absoluto|nota de vecindades]]).

![Franja de ancho 2 epsilon alrededor del límite](adjuntos/Franja%20de%20ancho%202%20epsilon%20alrededor%20del%20límite.png)

> [!example]- Transcripción de la figura (clase 21)
> Una nube de puntos rojos que sube, pasa por encima de la franja y se asienta dentro de ella. Tres rectas horizontales: $y = L + \varepsilon$ y $y = L - \varepsilon$ (naranjas) y $y = L$ (azul) en el centro. A partir de la marca $N$ en el eje horizontal, todos los puntos quedan entre las dos rectas naranjas, mientras que algunos puntos anteriores quedan fuera.

> [!tip] Un $\varepsilon$ más pequeño pide un $N$ más grande
> Cuanto más estrecha la franja, más tarde entra la sucesión en ella: $N$ **depende** de $\varepsilon$. Probar que $\lim a_n = L$ es dar una receta que, para cada $\varepsilon$, produzca un $N$.

## El principio de Arquímedes: de donde sale $N$

Para encontrar $N$ casi siempre se despeja $n$ de la condición $|a_n - L| < \varepsilon$, y se necesita saber que existe un natural mayor que cualquier número real dado:

> [!tip] Principio de Arquímedes y consecuencia
> $\mathbb{N}$ no está acotado superiormente: dado un real $a > 0$, existe $n \in \mathbb{N}$ con $a < n$. En consecuencia, para todo $\varepsilon > 0$ existe $n$ con $0 < \tfrac{1}{n} < \varepsilon$.

(Se demostró desde el [[04 - Axioma del supremo y propiedad arquimediana|axioma del supremo]].) De ahí sale, por ejemplo, el límite fundamental $\displaystyle\lim_{n \to \infty}\frac{1}{n} = 0$: dado $\varepsilon > 0$ se toma $N$ con $\tfrac{1}{N} < \varepsilon$, y si $n > N$, $\left|\tfrac{1}{n} - 0\right| = \tfrac{1}{n} < \tfrac{1}{N} < \varepsilon$.

## Dos límites inmediatos

- **Sucesión constante:** si $a_n = c$ para todo $n$, entonces $\lim a_n = c$, porque $|a_n - c| = 0 < \varepsilon$ para todo $n$ (basta cualquier $N$).
- **$\tfrac{1}{n}$:** $\lim \tfrac{1}{n} = 0$, recién visto.

> [!warning] Errores frecuentes con la definición
> - **Escoger $N$ antes que $\varepsilon$.** El orden es: primero $\varepsilon > 0$ cualquiera, después $N$ (que puede depender de $\varepsilon$).
> - **Exigir $|a_n - L| < \varepsilon$ para algunos $n$.** Debe valer para **todos** los $n > N$.
> - **Confundir "se acerca" con "llega".** Los términos no necesitan valer $L$: $\tfrac{n}{n + 1}$ nunca es $1$, pero converge a $1$.

## Preguntas de repaso

> [!question]- ¿Qué dice $\lim a_n = L$ en palabras?
> Que para cualquier margen de error $\varepsilon > 0$, desde algún índice $N$ en adelante todos los términos están a distancia menor que $\varepsilon$ de $L$.

> [!question]- ¿Por qué $N$ depende de $\varepsilon$?
> Porque al achicar el margen de error hay que esperar más términos hasta que la sucesión entre y se quede en la franja más angosta.

> [!question]- ¿Converge $a_n = \frac{n}{n + 1}$ y a qué?
> A $1$: $|a_n - 1| = \frac{1}{n + 1}$ se hace menor que cualquier $\varepsilon$ para $n$ grande.

> [!question]- ¿Cuál es el papel del principio de Arquímedes en estas demostraciones?
> Garantiza que existe un natural $N$ mayor que el número real que resulta de despejar $n$ (por ejemplo $\frac{1}{\varepsilon}$), de modo que el $N$ pedido siempre existe.
