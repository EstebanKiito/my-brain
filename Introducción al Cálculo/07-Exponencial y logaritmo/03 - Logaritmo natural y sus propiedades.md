---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - origen/complemento
prerrequisitos:
  - "[[02 - Desigualdad fundamental y propiedades de la exponencial]]"
  - "[[05 - Función inversa]]"
---

# Logaritmo natural y sus propiedades

Como la exponencial es biyectiva de $\mathbb{R}$ en $(0, \infty)$, tiene una inversa: el logaritmo natural. Con ella se despeja un exponente, y sus propiedades convierten productos en sumas, cocientes en restas y potencias en productos.

## Definición

> [!tip] Logaritmo natural
> $\ln : (0, \infty) \to \mathbb{R}$ es la inversa de $\exp$:
> $$y = \ln(x) \iff e^y = x.$$

De la definición de inversa se obtienen las identidades básicas:

- $e^{\ln x} = x$ para todo $x > 0$, y $\ln(e^x) = x$ para todo $x \in \mathbb{R}$.
- $\ln(1) = 0$ y $\ln(e) = 1$.
- $\ln$ es **estrictamente creciente** (inversa de una función estrictamente creciente) y su único cero es $x = 1$.
- Su gráfico es el reflejo del de $e^x$ respecto de la recta $y = x$: pasa por $(1, 0)$, tiene la recta $x = 0$ como asíntota vertical y crece lentamente.

## Relación con las rectas de pendiente 1

Como $\ln$ es el reflejo de $\exp$ respecto de $y = x$, el mismo argumento de la pendiente de $e^x$ vale para el logaritmo: la secante entre $(1, 0)$ y $(1 + h, \ln(1 + h))$ tiene pendiente $\dfrac{\ln(1 + h) - \ln 1}{h} = \dfrac{\ln(1 + h)}{h} \approx 1$ si $h \approx 0$. Con $h = \tfrac{1}{m}$, esto dice que $m\ln\!\left(1 + \tfrac{1}{m}\right) \approx 1$ para $m$ grande, es decir, $\left(1 + \tfrac{1}{m}\right)^m \approx e$.

![Exponencial y logaritmo con rectas paralelas a y igual x](adjuntos/Exponencial%20y%20logaritmo%20con%20rectas%20paralelas%20a%20y%20igual%20x.png)

> [!example]- Transcripción de la figura (cuaderno, clase 18)
> En azul $y = e^x$, que pasa por $(0, 1)$, y en verde $y = \ln x$, que pasa por $(1, 0)$ y marca el punto $1 + h$ en el eje. Tres rectas grises paralelas, $y = x + 1$, $y = x$ e $y = x - 1$, tocan a las curvas en esos puntos: cerca de ellos, ambas curvas se parecen a una recta de pendiente $1$.

## Propiedades algebraicas

> [!tip] Leyes del logaritmo
> Para $x, y > 0$ y $z \in \mathbb{R}$:
> 1. $\ln(xy) = \ln x + \ln y$.
> 2. $\ln\!\left(\dfrac{x}{y}\right) = \ln x - \ln y$.
> 3. $\ln(x^z) = z \ln x$.

*Demostración de 1.* Sean $u = \ln x$ y $w = \ln y$, es decir $e^u = x$ y $e^w = y$. Entonces $\ln(xy) = \ln(e^u e^w) = \ln(e^{u + w}) = u + w = \ln x + \ln y$.
*Demostración de 3.* Con $u = \ln x$, $\ln(x^z) = \ln((e^u)^z) = \ln(e^{zu}) = zu = z\ln x$. La 2 sale de la 1 y la 3 con $z = -1$ aplicada a $y$.

> [!warning] Los logaritmos de una suma no se separan
> $\ln(x + y) \neq \ln x + \ln y$ y $\ln(x - y) \neq \ln x - \ln y$. Solo el producto y el cociente se convierten. Además $(\ln x)^2 \neq \ln(x^2)$: el primero es el cuadrado del logaritmo; el segundo es $2\ln x$.

## Desigualdad fundamental del logaritmo

> [!tip] Cotas del logaritmo
> Para todo $x > 0$: $\ 1 - \dfrac{1}{x} \le \ln x \le x - 1.$

*Demostración de la cota superior.* Por $e^z \ge 1 + z$ y por ser $\ln$ creciente, $z = \ln(e^z) \ge \ln(1 + z)$. Con $z = x - 1$ queda $x - 1 \ge \ln x$. La cota inferior sale de aplicar la superior a $\tfrac{1}{x}$: $\ln\tfrac{1}{x} \le \tfrac{1}{x} - 1$, o sea $-\ln x \le \tfrac{1}{x} - 1$. $\blacksquare$

Estas cotas acotan al logaritmo entre dos funciones sencillas y se usan para calcular límites (se verán en los temas de sucesiones).

## Expandir y combinar

Las leyes se aplican de izquierda a derecha para **expandir** una expresión en logaritmos simples y de derecha a izquierda para **combinarla** en uno solo.

**Expandir.** $\ln\!\left(x^2\sqrt{\tfrac{x - 1}{x + 1}}\right) = 2\ln x + \tfrac{1}{2}\ln(x - 1) - \tfrac{1}{2}\ln(x + 1)$.

**Combinar.** $4\ln x - \tfrac{1}{3}\ln(x^2 + 1) + 2\ln(x - 1) = \ln\!\left(\dfrac{x^4 (x - 1)^2}{\sqrt[3]{x^2 + 1}}\right)$.

> [!warning] Los dominios al combinar
> La expresión de la izquierda exige $x > 0$ y $x > 1$ (por $\ln x$ y $\ln(x - 1)$), mientras que el logaritmo combinado a la derecha podría estar definido en más puntos. Al **resolver ecuaciones** hay que comprobar el dominio de la ecuación original, no el de la combinada.

## Preguntas de repaso

> [!question]- ¿Por qué $\ln(e^x) = x$ y $e^{\ln x} = x$?
> Porque $\ln$ es la inversa de $\exp$: aplicar una y luego la otra deja el número igual, en el dominio correspondiente ($x \in \mathbb{R}$ en el primer caso, $x > 0$ en el segundo).

> [!question]- Exprese $\ln\!\left(\frac{x^3}{y^2}\right)$ con logaritmos simples.
> $3\ln x - 2\ln y$, por las leyes del cociente y de la potencia.

> [!question]- ¿Cuál es el dominio de $\ln(4 - x^2)$?
> Se necesita $4 - x^2 > 0$, es decir $x^2 < 4$: el intervalo $(-2, 2)$.

> [!question]- ¿Cómo se deduce $\ln x \le x - 1$ de la desigualdad de la exponencial?
> De $e^z \ge 1 + z$ y la monotonía del logaritmo: $z \ge \ln(1 + z)$. Con $z = x - 1$ queda $x - 1 \ge \ln x$.
