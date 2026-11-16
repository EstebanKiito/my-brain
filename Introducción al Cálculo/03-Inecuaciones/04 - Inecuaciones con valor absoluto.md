---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades del valor absoluto y desigualdad triangular]]"
  - "[[03 - Inecuaciones racionales y restricciones]]"
---

# Inecuaciones con valor absoluto

Con valor absoluto, la inecuación mezcla casos de signo. Hay tres métodos que dan el mismo resultado y conviene elegir el más corto según la forma del enunciado: elevar al cuadrado cuando hay un valor absoluto en cada lado, usar las propiedades del valor absoluto cuando hay uno solo y partir en casos por puntos críticos cuando hay varios sumados.

## Método 1: elevar al cuadrado

Si ambos lados son no negativos, $A \le B \iff A^2 \le B^2$, y $|t|^2 = t^2$ elimina las barras. Es el camino directo para $|f| < |g|$.

Resolver $2|x| < |x - 1|$. Ambos lados son $\ge 0$, luego
$$4x^2 < (x - 1)^2 \iff 3x^2 + 2x - 1 < 0 \iff (x + 1)(3x - 1) < 0.$$
Con puntos críticos $-1$ y $\tfrac{1}{3}$:

![Tabla de signos de (−3x+1)(x+1)](adjuntos/Tabla%20de%20signos%20de%20una%20inecuación%20con%20valor%20absoluto.png)

> [!example]- Transcripción de la tabla (clase 6)
> Dos factores, $-3x + 1$ y $x + 1$, en los intervalos $(-\infty, -1)$, $(-1, \tfrac{1}{3})$ y $(\tfrac{1}{3}, \infty)$. Signos de $-3x + 1$: $+, +, -$. De $x + 1$: $-, +, +$. Producto: $-, +, -$. La clase resuelve $0 < (x + 1)(-3x + 1)$, que es positivo solo en el intervalo central.

El producto $(x + 1)(1 - 3x)$ es positivo en el intervalo central: $S = \left(-1, \tfrac{1}{3}\right)$.

## Método 2: propiedades del valor absoluto

Se usa $|u| < v \iff -v < u < v$ y $|u| > v \iff u < -v \ \text{ó}\ u > v$ (con $v$ cualquier expresión). Para $2|x| < |x - 1|$: $-|x - 1| < 2x < |x - 1|$, y cada lado se desarma otra vez. Llega al mismo resultado, pero el método 1 es más corto cuando hay un valor absoluto a cada lado.

## Método 3: casos por puntos críticos

Se marcan los valores donde cada expresión interior cambia de signo, se parte la recta en tramos y en cada tramo se quitan las barras con el signo conocido. La solución es la unión de las soluciones de cada tramo, **intersecadas con el tramo**.

Para $2|x| < |x - 1|$ los puntos críticos son $0$ y $1$:

| Tramo | $\lvert x \rvert$ | $\lvert x - 1 \rvert$ | Inecuación | Solución en el tramo |
|---|---|---|---|---|
| $(-\infty, 0]$ | $-x$ | $1 - x$ | $-2x < 1 - x$, o sea $x > -1$ | $(-1, 0]$ |
| $(0, 1]$ | $x$ | $1 - x$ | $2x < 1 - x$, o sea $x < \tfrac{1}{3}$ | $\left(0, \tfrac{1}{3}\right)$ |
| $(1, \infty)$ | $x$ | $x - 1$ | $2x < x - 1$, o sea $x < -1$ | $\varnothing$ |

La unión es $\left(-1, \tfrac{1}{3}\right)$, igual que con el método 1.

> [!tip] Cuál elegir
> Un solo valor absoluto o un cociente: propiedades del valor absoluto o casos. Dos valores absolutos igualados por $<,\le$: elevar al cuadrado. Tres o más sumados, o anidados como $|x^2 - |3 + 2x||$: casos por puntos críticos, resolviendo de adentro hacia afuera.

## Un problema con contexto: el guardia

La posición de un guardia es $x(t) = \tfrac{40t}{t^2 + 16}$ ($t$ en horas desde la medianoche). Una persona en $x = 1$ recibió un disparo entre las 4:00 y las 7:00 a.m., y el perito dice que el culpable estaba a no más de $3$ metros. ¿Es inocente el guardia?

Estar a distancia $\le 3$ de $x = 1$ significa $|x(t) - 1| \le 3$, es decir $-3 \le \tfrac{40t - t^2 - 16}{t^2 + 16} \le 3$ (con $t \ge 0$). La desigualdad izquierda vale siempre para $t \ge 0$; la derecha, $\tfrac{40t - t^2 - 16}{t^2 + 16} \le 3$, equivale a $4t^2 - 40t + 64 \ge 0$, es decir $(t - 2)(t - 8) \ge 0$, o sea $t \le 2$ ó $t \ge 8$. Así el guardia estaba a distancia $\le 3$ solo en $[0, 2]$ y desde $t = 8$. Como el disparo fue en $[4, 7]$, **no pudo** ser el culpable.

## Preguntas de repaso

> [!question]- ¿Cuándo es válido elevar al cuadrado ambos lados de una desigualdad?
> Cuando ambos lados son no negativos: entonces $A \le B \iff A^2 \le B^2$. Con $|f| < |g|$ siempre se cumple, porque ambos lados son valores absolutos.

> [!question]- ¿Qué se hace en cada tramo del método por casos?
> Se quita el valor absoluto con el signo que tiene la expresión en ese tramo, se resuelve la inecuación sin barras y se intersecta la solución con el tramo.

> [!question]- ¿Por qué se intersecta con el tramo en el método de casos?
> Porque la forma simplificada de la inecuación solo vale mientras $x$ esté en ese tramo; una solución fuera de él pertenece a otra versión de la inecuación.

> [!question]- ¿Cómo se plantea que alguien está a distancia a lo más $3$ de la posición $1$?
> Como $|x - 1| \le 3$, que equivale a $-3 \le x - 1 \le 3$, es decir $-2 \le x \le 4$.
