---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - origen/complemento
prerrequisitos:
  - "[[03 - Logaritmo natural y sus propiedades]]"
---

# Exponencial y logaritmo en otras bases

Con $e$ y $\ln$ se definen las exponenciales y logaritmos de cualquier base positiva. La definición se apoya en la ya conocida $e^x$, y de ella salen las mismas propiedades que se conocen de la escuela, además de la fórmula de cambio de base que se usa para resolver ecuaciones.

## La función $a^x$

> [!tip] Potencia de base $a$
> Para $a > 0$, $a \neq 1$: $a^x = \exp(x \ln a) = e^{x \ln a}$.

Propiedades:
- Dominio $\mathbb{R}$ y valores siempre positivos.
- Es **estrictamente monótona**: creciente si $a > 1$ (porque $\ln a > 0$) y decreciente si $0 < a < 1$ (porque $\ln a < 0$). En particular es inyectiva.
- $a^x : \mathbb{R} \to (0, \infty)$ es **biyectiva**, con inversa dada por $a^x = y \iff x = \dfrac{\ln y}{\ln a}$.

Las leyes usuales de los exponentes ($a^{x + y} = a^x a^y$, $(a^x)^y = a^{xy}$) se deducen de las de $e^x$.

## El logaritmo en base $a$

> [!tip] Logaritmo de base $a$
> $\log_a(x) = \dfrac{\ln x}{\ln a}$ para $x > 0$. Es la inversa de $a^x$: $\ \log_a(x) = y \iff a^y = x$.

La definición es también la **fórmula de cambio de base**: cualquier logaritmo se calcula con $\ln$. Y las leyes del logaritmo natural valen para todas las bases: $\log_a(xy) = \log_a x + \log_a y$, $\log_a(x/y) = \log_a x - \log_a y$, $\log_a(x^z) = z \log_a x$.

> [!tip] Convención en el curso
> $\log$ sin base significa $\log_{10}$ (así lo aclaran las pautas: "recuerde que $\log := \log_{10}$"). Así, $\log(10x) = 1 + \log x$ y $\log 100 = 2$.

## Despejar un exponente

Para resolver $a^x = y$ se aplica $\ln$ a ambos lados: $x \ln a = \ln y$, luego $x = \tfrac{\ln y}{\ln a}$.

**Ejemplo (clase 17).** $3^{x + 2} = 7 \Rightarrow (x + 2)\ln 3 = \ln 7 \Rightarrow x = \dfrac{\ln 7}{\ln 3} - 2 \approx -0{,}228$.

## Gráfico de $a^x - 5$

La Guía 8 pide graficar $2^x - 5$: es $2^x$ trasladada $5$ unidades hacia abajo. Pasa por $(0, -4)$, tiene la asíntota horizontal $y = -5$ (en lugar de $y = 0$), corta el eje $x$ en $x = \log_2 5 \approx 2{,}32$ y su recorrido es $(-5, \infty)$.

## Logaritmos de base variable

Un truco muy usado: como $\log_x a = \tfrac{\ln a}{\ln x}$, un logaritmo de base **variable** se vuelve una fracción de logaritmos naturales con la incógnita solo en $\ln x$. Y $\log_{x^2} b = \dfrac{\ln b}{2\ln x}$.

> [!warning] Restricciones de la base
> La base de una potencia o de un logaritmo debe ser positiva y distinta de $1$. Si la base es la incógnita ($\log_x a$), hay que imponer $x > 0$ y $x \neq 1$.

## Preguntas de repaso

> [!question]- ¿Por qué $a^x$ es decreciente cuando $0 < a < 1$?
> Porque $a^x = e^{x \ln a}$ y $\ln a < 0$: el exponente decrece al aumentar $x$ y la exponencial es estrictamente creciente, así que $a^x$ decrece.

> [!question]- Calcule $\log_2 8$ con la fórmula de cambio de base.
> $\frac{\ln 8}{\ln 2} = \frac{3\ln 2}{\ln 2} = 3$.

> [!question]- ¿Cuánto vale $\log 1000$ y cuánto $\log(10x)$ en función de $\log x$?
> $\log 1000 = 3$ y $\log(10x) = 1 + \log x$.

> [!question]- ¿Cuál es la inversa de $f(x) = 3^x$?
> $f^{-1}(y) = \log_3 y = \frac{\ln y}{\ln 3}$, definida para $y > 0$.
