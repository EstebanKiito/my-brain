---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[06 - Ecuaciones de recurrencia y búsqueda binaria]]"
---

# Funciones armónicas y notación asintótica condicional

Resolver una recurrencia con $n = b^k$ es fácil, pero luego hay que extenderla a todo $n$. En lugar de repetir una inducción con constantes adivinadas cada vez, existe un teorema que hace el paso general siempre que se cumplan tres condiciones de regularidad.

## Dos propiedades de regularidad

Una función $f : \mathbb{N} \to \mathbb{R}^+$ es **asintóticamente no decreciente** si
$\exists n_0\ \forall n \ge n_0:\ f(n) \le f(n+1)$. Lo son, por ejemplo, $\log_2 n$, $n$, $n^k$ y $2^n$.

Dado un natural $b > 1$, $f$ es **$b$-armónica** si $f(b \cdot n) \in O(f)$: multiplicar el argumento por $b$ solo multiplica el valor por una constante. Lo son $\log_2 n$, $n$ y $n^k$ para todo $b$, pero **$2^n$ no es 2-armónica**: $2^{2n} \le c \cdot 2^n$ equivale a $2^n \le c$, que falla para $n$ grande.

## El teorema

Sea $\text{POTENCIA}_b = \{ b^i \mid i \in \mathbb{N} \}$.

> [!tip] Teorema de extensión
> Si $f$ y $g$ son asintóticamente no decrecientes, $g$ es $b$-armónica y $f \in O(g \mid \text{POTENCIA}_b)$, entonces $f \in O(g)$.

**Idea de la demostración.** Hay constantes que cumplen: $c, n_2$ para $f \le c\,g$ sobre las potencias de $b$, y $d, n_3$ para $g(bn) \le d\,g(n)$. Dado $n$ grande, existe $k$ con $b^k \le n < b^{k+1}$. Se encadena

$$f(n) \le f(b^{k+1}) \le c\, g(b^{k+1}) \le c\, g(b n) \le c\,d\, g(n).$$

Cada paso usa una hipótesis: $f$ no decreciente (y $n < b^{k+1}$), la cota sobre potencias, $g$ no decreciente (y $b^{k+1} \le b \cdot n$ por $b^k \le n$) y $g$ $b$-armónica. Así, $f \le (cd)\, g$ para todo $n$ desde un $n_4$ que es el máximo de todos los umbrales.

## Aplicación a BinarySearch

Con $T(1) = 3$ y $T(n) = T(\lfloor n/2 \rfloor) + 4$:

- Ya se sabe que $T \in O(\log_2 n \mid \text{POTENCIA}_2)$ (la solución $4 \log_2 n + 3$).
- $\log_2 n$ es asintóticamente no decreciente y 2-armónica.
- Falta mostrar que **$T$ es asintóticamente no decreciente**, que se hace por inducción.

Se prueba el resultado más fuerte: $\forall n \ge 2\ \forall m \text{ con } 2 \le m \le n:\ T(m) \le T(n)$, por inducción fuerte sobre $n$.

- **Base** ($n = 2$): el único $m$ es $2$, trivial.
- **Paso:** de $2 \le m \le n$ sale $1 \le \lfloor m/2 \rfloor \le \lfloor n/2 \rfloor < n$. Si $\lfloor m/2 \rfloor = 1$, entonces $T(\lfloor m/2 \rfloor) = 3 \le T(\lfloor n/2 \rfloor)$ porque todo valor de $T$ es al menos $3$. Si $\lfloor m/2 \rfloor \ge 2$, la HI aplicada a $\lfloor n/2 \rfloor < n$ da $T(\lfloor m/2 \rfloor) \le T(\lfloor n/2 \rfloor)$. En ambos casos, sumando $4$: $T(m) \le T(n)$.

Con eso, el teorema da $T \in O(\log n)$ sin buscar $c$ ni $n_0$.

> [!example]- Comprobación numérica
> $T(1..8) = 3, 7, 7, 11, 11, 11, 11, 15$: es no decreciente, y $T(n) \le 7\log_2 n$ para todo $n \ge 2$ hasta $5000$ (verificado por cálculo).

## Cuándo falla

> [!warning] Sin armonía no hay extensión
> Si $g = 2^n$ (no 2-armónica) y $f$ se conoce solo sobre potencias de $2$, el teorema no se aplica: entre $2^k$ y $2^{k+1}$ la función $2^n$ cambia por un factor no acotado. Esa es la razón de exigir $g(bn) \in O(g)$.

## Preguntas de repaso

> [!question]- ¿Por qué hace falta que $f$ sea asintóticamente no decreciente?
> Para poder acotar $f(n)$ por $f(b^{k+1})$, el valor en la potencia de $b$ siguiente. Sin monotonía, $f$ podría tener picos entre potencias que la cota sobre potencias no ve.

> [!question]- ¿Qué se gana con el teorema en vez de la inducción directa?
> No hay que adivinar $c$ y $n_0$; solo se verifican propiedades cualitativas de $g$ (monótona y $b$-armónica) y se prueba la monotonía de $T$.

> [!question]- ¿Es $n^2$ 3-armónica?
> Sí: $(3n)^2 = 9n^2 \in O(n^2)$. En general $n^k$ es $b$-armónica para todo $b$.

> [!question]- ¿Dónde se usa que $n < b^{k+1}$ y que $b^k \le n$?
> $n < b^{k+1}$ permite $f(n) \le f(b^{k+1})$ y $b^k \le n$ da $b^{k+1} \le b \cdot n$, que permite $g(b^{k+1}) \le g(bn)$.
