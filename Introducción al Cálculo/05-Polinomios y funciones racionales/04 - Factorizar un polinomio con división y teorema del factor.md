---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[03 - Gráfica de polinomios, ceros y multiplicidad]]"
---

# Factorizar un polinomio con división y teorema del factor

Para encontrar los ceros de un polinomio de grado $\ge 3$ y graficarlo hay que factorizarlo. La herramienta es siempre la misma: encontrar una raíz, dividir por el factor correspondiente y repetir con el cociente. Esta nota junta la técnica con el formato exacto de las interrogaciones, que casi siempre piden dividir, verificar con el teorema del resto y concluir con el teorema del factor. La teoría detallada está en [[02 - División de polinomios|División de polinomios]], [[03 - Teorema del resto|Teorema del resto]] y [[01 - Raíces y el teorema del factor|Raíces y el teorema del factor]].

## Las herramientas

> [!tip] Teorema del resto y teorema del factor
> - **Resto:** el resto de dividir $P(x)$ por $x - c$ es $P(c)$. (Para dividir por $ax - b$, el resto es $P(b/a)$.)
> - **Factor:** $x - c$ es factor de $P$ si y solo si $P(c) = 0$, es decir, si $c$ es una raíz.

> [!tip] División sintética (regla de Ruffini)
> Para dividir por $x - c$: se escriben los coeficientes (con ceros en los grados que faltan), se baja el primero, se multiplica por $c$ y se suma al siguiente, y así sucesivamente. El último número es el resto y los anteriores son los coeficientes del cociente.

## Ejemplo 1: dividir, verificar y factorizar (I1, 2025-1)

Sea $P(x) = x^5 - x^4 - 2x^3 - x^2 + x + 2$.

**(a) División por $x - 2$.** Con $c = 2$ y coeficientes $1, -1, -2, -1, 1, 2$:

| | $1$ | $-1$ | $-2$ | $-1$ | $1$ | $2$ |
|---|---|---|---|---|---|---|
| $c = 2$ | | $2$ | $2$ | $0$ | $-2$ | $-2$ |
| | $1$ | $1$ | $0$ | $-1$ | $-1$ | $0$ |

El cociente es $Q(x) = x^4 + x^3 - x - 1$ y el resto es $0$.

**(b) Teorema del resto.** $P(2) = 32 - 16 - 16 - 4 + 2 + 2 = 0$, que coincide con el resto.

**(c) Teorema del factor.** $P(-1) = -1 - 1 + 2 - 1 - 1 + 2 = 0$, así que $x + 1$ es factor.

**(d) Factorización completa.** Como $x - 2$ y $x + 1$ son factores, $(x - 2)(x + 1) = x^2 - x - 2$ también lo es. Dividiendo, $P(x) = (x^2 - x - 2)(x^3 - 1)$ y como $x^3 - 1 = (x - 1)(x^2 + x + 1)$,
$$P(x) = (x - 2)(x + 1)(x - 1)(x^2 + x + 1).$$
El factor $x^2 + x + 1$ tiene discriminante $1 - 4 < 0$: no se factoriza más sobre los reales. Los ceros reales son $2$, $-1$ y $1$.

## Ejemplo 2: un divisor que no es mónico (I1, 2026-1)

Sea $P(x) = 4x^6 + 2x^5 - 2x^4 - 4x^3 + 3x - 1$ (coeficientes $4, 2, -2, -4, 0, 3, -1$; el de $x^2$ es cero).

**(a) División por $2x - 1$.** Se usa la raíz $c = \tfrac{1}{2}$ de $2x - 1 = 2\left(x - \tfrac{1}{2}\right)$ y al final se divide por $2$:

| | $4$ | $2$ | $-2$ | $-4$ | $0$ | $3$ | $-1$ |
|---|---|---|---|---|---|---|---|
| $c = \tfrac{1}{2}$ | | $2$ | $2$ | $0$ | $-2$ | $-1$ | $1$ |
| | $4$ | $4$ | $0$ | $-4$ | $-2$ | $2$ | $0$ |

Esto divide por $x - \tfrac{1}{2}$ con cociente $4x^5 + 4x^4 - 4x^2 - 2x + 2$; al dividir por $2$ para pasar a $2x - 1$ queda $Q(x) = 2x^5 + 2x^4 - 2x^2 - x + 1$ y resto $0$.

**(b)** $P\!\left(\tfrac{1}{2}\right) = \tfrac{4}{64} + \tfrac{2}{32} - \tfrac{2}{16} - \tfrac{4}{8} + \tfrac{3}{2} - 1 = 0$, de acuerdo con el resto.

**(c)** $P(-1) = 4 - 2 - 2 + 4 - 3 - 1 = 0$, luego $x + 1$ es factor.

**(d)** $(2x - 1)(x + 1) = 2x^2 + x - 1$ divide a $P$ y el cociente es $2x^4 - 2x + 1$:
$$P(x) = (2x - 1)(x + 1)(2x^4 - 2x + 1).$$
El último factor no tiene raíces racionales (los candidatos $\pm 1, \pm\tfrac{1}{2}$ no la anulan), así que la pauta se detiene ahí.

## Ejemplo 3: un factor cuadrático con raíces irracionales (I1, 2026-1)

$P(a) = 4a^3 + 4a^2 - 19a + 6$. Se verifica $P\!\left(\tfrac{3}{2}\right) = \tfrac{27}{2} + 9 - \tfrac{57}{2} + 6 = 0$. Dividiendo por $2a - 3$ queda $P(a) = (2a - 3)(2a^2 + 5a - 2)$. El factor cuadrático tiene discriminante $25 + 16 = 41$ y raíces $\tfrac{-5 \pm \sqrt{41}}{4}$, de modo que la factorización completa sobre $\mathbb{R}$ es
$$P(a) = (2a - 3) \cdot 2\left(a - \tfrac{-5 + \sqrt{41}}{4}\right)\left(a - \tfrac{-5 - \sqrt{41}}{4}\right).$$

## Estrategia general

1. **Candidatos racionales:** si $P$ tiene coeficientes enteros, las raíces racionales $\tfrac{p}{q}$ cumplen que $p$ divide al término constante y $q$ al coeficiente principal (ver [[02 - Teorema de los ceros racionales|ceros racionales]]).
2. **Probar con el teorema del resto** (evaluar $P(c)$) hasta dar con una raíz.
3. **Dividir** y repetir con el cociente, que tiene grado menor.
4. Cuando quede un factor cuadrático, se usa la fórmula cuadrática o el discriminante para decidir si se factoriza sobre $\mathbb{R}$.

> [!warning] Errores frecuentes
> - Olvidar los ceros en los grados que faltan al armar la tabla de Ruffini (por ejemplo, $x^2$ en $4x^6 + \dots + 3x - 1$).
> - Dividir por $2x - 1$ y no corregir el factor $2$: Ruffini con $c = \tfrac{1}{2}$ divide por $x - \tfrac{1}{2}$.
> - Dar por factorizado un polinomio que aún tiene factores cuadráticos reducibles.

## Preguntas de repaso

> [!question]- ¿Cómo se verifica con el teorema del resto que $x - 2$ divide a $x^5 - x^4 - 2x^3 - x^2 + x + 2$?
> Se evalúa en $2$: $P(2) = 0$, y por el teorema del factor eso equivale a que $x - 2$ sea factor.

> [!question]- ¿Qué resto se obtiene al dividir $P(x)$ por $2x - 1$?
> $P\!\left(\tfrac{1}{2}\right)$, porque $2x - 1 = 2\left(x - \tfrac{1}{2}\right)$ tiene la misma raíz que $x - \tfrac{1}{2}$.

> [!question]- Si $x - 2$ y $x + 1$ son factores de $P$, ¿por qué lo es también $(x - 2)(x + 1)$?
> Porque son coprimos (sin raíces en común): las raíces $2$ y $-1$ son distintas, y $P$ es divisible por cada factor lineal, luego por su producto.

> [!question]- ¿Cuándo se detiene la factorización sobre los reales?
> Cuando todos los factores son lineales o cuadráticos con discriminante negativo (irreducibles sobre $\mathbb{R}$).
