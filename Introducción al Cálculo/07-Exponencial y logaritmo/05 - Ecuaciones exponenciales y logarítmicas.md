---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - origen/complemento
prerrequisitos:
  - "[[04 - Exponencial y logaritmo en otras bases]]"
  - "[[04 - Ecuaciones con valor absoluto]]"
---

# Ecuaciones exponenciales y logarítmicas

Resolver estas ecuaciones es combinar tres ideas: llevar todo a una forma $a^{(\cdot)} = b$ o $\log(\cdot) = \cdot$ para aplicar la función inversa, usar un cambio de variable cuando aparece $e^{2x}$ junto a $e^x$, y **verificar el dominio** al final. Aparecen en casi todas las interrogaciones 3 y 6 y en los exámenes.

## Exponenciales: aplicar $\ln$ o cambiar de variable

> [!tip] Estrategias
> - **Forma $a^{f(x)} = b$ ($b > 0$):** se aplica $\ln$ y queda $f(x)\ln a = \ln b$. Si $b \le 0$ no hay solución.
> - **Factor común:** si aparece $e^x$ (o $2^x$) en todos los términos, se saca factor y se usa que $e^x \neq 0$.
> - **Cuadrática en $e^x$:** con $u = e^x > 0$, la ecuación se vuelve polinomial en $u$. Se descartan los valores $u \le 0$.

**Ejemplo (I3, 2023-2): $e^{2x} - e^x - 6 = 0$.** Con $u = e^x$: $u^2 - u - 6 = (u - 3)(u + 2) = 0$, es decir $e^x = 3$ ó $e^x = -2$. La segunda no tiene solución porque $e^x > 0$. Luego $x = \ln 3$.

**Ejemplo (I6, 2022-1): $5^x - 25^x = -6$.** Como $25^x = (5^x)^2$, con $u = 5^x$: $u - u^2 = -6 \iff u^2 - u - 6 = 0 \iff (u - 3)(u + 2) = 0$. $5^x = -2$ es imposible; $5^x = 3$ da $x = \dfrac{\ln 3}{\ln 5}$.

**Ejemplo (Examen, 2026-1): $e^x + e^{-x} = 3$.** Multiplicando por $e^x$: $e^{2x} - 3e^x + 1 = 0$. Con $u = e^x$, $u = \dfrac{3 \pm \sqrt{5}}{2}$, ambos positivos. Las soluciones son $x = \ln\!\left(\dfrac{3 + \sqrt{5}}{2}\right)$ y $x = \ln\!\left(\dfrac{3 - \sqrt{5}}{2}\right)$, que son opuestas porque el producto de las raíces es $1$.

**Ejemplo (clase 17): $3xe^x + x^2e^x = 0$.** Se factoriza $x e^x(3 + x) = 0$; como $e^x \neq 0$, $x = 0$ ó $x = -3$. De igual modo $x^2 2^x - 2^x = 0$ da $2^x(x^2 - 1) = 0$, es decir $x = \pm 1$, y $x^2 e^x + xe^x - e^x = 0$ da $x^2 + x - 1 = 0$ y $x = \dfrac{-1 \pm \sqrt{5}}{2}$.

## Logarítmicas: combinar, aplicar $\exp$ y verificar

> [!tip] Estrategias
> - **Escribir cada lado como un solo logaritmo** (con las leyes) y usar que $\log$ es inyectiva: $\log A = \log B \iff A = B$ (con $A, B > 0$).
> - **Pasar a forma exponencial:** $\log A = c \iff A = 10^c$ (o $e^c$ si es $\ln$).
> - **Comprobar los argumentos:** cada logaritmo de la ecuación original debe tener argumento positivo.

**Ejemplo (clase 17): $\log(3x + 2) = \log(x - 4) + 1$.** Como $1 = \log 10$, queda $\log(3x + 2) = \log(10(x - 4))$, es decir $3x + 2 = 10x - 40$ y $x = 6$. Comprobación: $x - 4 = 2 > 0$ y $3x + 2 = 20 > 0$. Solución: $x = 6$.

**Ejemplo (I3, 2023-2): $\log(x + 1) - \log(x - 1) = 2$.** Se combina: $\log\dfrac{x + 1}{x - 1} = 2 \iff \dfrac{x + 1}{x - 1} = 100 \iff x + 1 = 100x - 100 \iff x = \tfrac{101}{99}$. Comprobación: $x > 1$ (para que $\log(x - 1)$ exista) y $\tfrac{101}{99} > 1$. Solución: $x = \tfrac{101}{99}$.

**Ejemplo (Examen, 2026-1): $\log_x a + \log_{x^2} b = c$** (con $a, b, c > 0$). La base exige $x > 0$ y $x \neq 1$. Con $\log_x a = \tfrac{\ln a}{\ln x}$ y $\log_{x^2} b = \tfrac{\ln b}{2\ln x}$:
$$\frac{\ln a}{\ln x} + \frac{\ln b}{2\ln x} = c \iff \ln x = \frac{2\ln a + \ln b}{2c} \iff x = (a^2 b)^{1/(2c)}.$$
Esa solución es válida si $x \neq 1$, es decir si $a^2 b \neq 1$; si $a^2 b = 1$ la ecuación no tiene solución.

## Una inversa con logaritmos (clase 17)

$f(x) = \log_2\big(3\log(10x) - 2\big)$. Su dominio exige $10x > 0$ y $3\log(10x) - 2 > 0$, o sea $\log(10x) > \tfrac{2}{3}$, es decir $x > 10^{-1/3}$. Para hallar $f^{-1}$: $y = \log_2(3\log(10x) - 2) \iff 2^y = 3\log(10x) - 2 \iff \log(10x) = \tfrac{2^y + 2}{3} \iff 10x = 10^{(2^y + 2)/3}$, de donde
$$f^{-1}(y) = 10^{\frac{2^y - 1}{3}}, \qquad y \in \mathbb{R}.$$

> [!warning] Soluciones fuera del dominio
> Combinar logaritmos puede **ampliar** el dominio: $\log(x - 4) + \log(x + 1) = \log(x^2 - 3x - 4)$ está definido también para $x < -1$, pero la ecuación original no. Siempre se sustituye la solución en la ecuación original (o se verifica que todos los argumentos sean positivos).

## Preguntas de repaso

> [!question]- ¿Por qué se descarta $e^x = -2$ al resolver $e^{2x} - e^x - 6 = 0$?
> Porque la exponencial siempre es positiva: $e^x = -2$ no tiene solución real.

> [!question]- ¿Qué se comprueba al final de una ecuación logarítmica?
> Que todos los argumentos de los logaritmos de la ecuación original sean positivos para la solución encontrada.

> [!question]- ¿Cómo se resuelve $2^{x} = 5$?
> Aplicando $\ln$: $x\ln 2 = \ln 5$, luego $x = \frac{\ln 5}{\ln 2} = \log_2 5$.

> [!question]- ¿Por qué en $\log_x a + \log_{x^2} b = c$ hay que excluir $x = 1$?
> Porque la base de un logaritmo no puede ser $1$ ($\ln 1 = 0$ anularía el denominador de $\frac{\ln a}{\ln x}$).
