---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[03 - Máximo común divisor y algoritmo de Euclides]]"
---

# Identidad de Bézout y algoritmo de Euclides extendido

El algoritmo de Euclides dice cuánto vale el MCD, pero no dice **cómo se construye** a partir de $a$ y $b$. Llevando la cuenta de los pasos se obtiene además dos enteros $s, t$ con $\operatorname{MCD}(a, b) = sa + tb$. Esa combinación es la herramienta que da inversos modulares, resuelve congruencias y demuestra que un primo que divide a un producto divide a un factor.

## Identidad de Bézout

> [!tip] Identidad de Bézout
> Para todo $a, b \in \mathbb{N}\setminus\{0\}$ existen $s, t \in \mathbb{Z}$ tales que $\operatorname{MCD}(a, b) = sa + tb$.

La demostración es el propio algoritmo: se muestra por inducción que **cada resto** que aparece es combinación lineal de $a$ y $b$, y el último resto no nulo es el MCD.

## Algoritmo de Euclides extendido

Se definen los restos $r_0 = a$, $r_1 = b$, $r_{i+1} = r_{i-1} \bmod r_i$ y, junto con ellos, coeficientes tales que $r_i = s_i a + t_i b$:

$$s_0 = 1,\ t_0 = 0; \qquad s_1 = 0,\ t_1 = 1; \qquad s_{i+1} = s_{i-1} - q_i s_i,\ \ t_{i+1} = t_{i-1} - q_i t_i,$$

con $q_i = \lfloor r_{i-1} / r_i \rfloor$. La fórmula sale de $r_{i+1} = r_{i-1} - q_i r_i$ reemplazando $r_{i-1}$ y $r_i$ por sus combinaciones. Se detiene cuando $r_k = 0$; entonces $\operatorname{MCD}(a, b) = r_{k-1} = s_{k-1} a + t_{k-1} b$.

## Ejemplo: $a = 8$, $b = 5$

| $i$ | $q_i$ | $r_i$ | $s_i$ | $t_i$ | combinación |
|---|---|---|---|---|---|
| 0 | | 8 | 1 | 0 | $8 = 1\cdot 8 + 0\cdot 5$ |
| 1 | | 5 | 0 | 1 | $5 = 0\cdot 8 + 1\cdot 5$ |
| 2 | 1 | 3 | $1 - 1\cdot 0 = 1$ | $0 - 1\cdot 1 = -1$ | $3 = 1\cdot 8 - 1\cdot 5$ |
| 3 | 1 | 2 | $0 - 1\cdot 1 = -1$ | $1 - 1\cdot(-1) = 2$ | $2 = -1\cdot 8 + 2\cdot 5$ |
| 4 | 1 | 1 | $1 - 1\cdot(-1) = 2$ | $-1 - 1\cdot 2 = -3$ | $1 = 2\cdot 8 - 3\cdot 5$ |
| 5 | 2 | 0 | | | |

El primer resto nulo aparece en $i = 5$, y el anterior es $1$: $\operatorname{MCD}(8, 5) = 1 = 2 \cdot 8 + (-3) \cdot 5$. Comprobación: $16 - 15 = 1$.

Otro ejemplo: para $a = 403$ y $b = 156$ el algoritmo entrega $\operatorname{MCD} = 13$ con $s = -5$ y $t = 13$, y se verifica que $-5 \cdot 403 + 13 \cdot 156 = -2015 + 2028 = 13$.

```python
def euclides_ext(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0      # mcd, s, t
```

## Consecuencias de Bézout

- **Lema de Euclides.** Si $\operatorname{MCD}(a, b) = 1$ y $a \mid bc$, entonces $a \mid c$. Con $sa + tb = 1$, multiplicando por $c$: $c = sac + t(bc)$, y $a$ divide a ambos sumandos.
- **Primo que divide a un producto.** Si $p$ es primo y $p \mid ab$, entonces $p \mid a$ o $p \mid b$ (si $p \nmid a$, entonces $\operatorname{MCD}(p, a) = 1$ y se aplica el lema anterior). De aquí sale la **unicidad de la factorización prima**.
- **Ecuaciones diofánticas.** $ax + by = c$ tiene solución entera si y solo si $\operatorname{MCD}(a, b) \mid c$ (ver [[05 - Inversos modulares y congruencias lineales]]).

> [!warning] Los coeficientes no son únicos
> $2 \cdot 8 - 3 \cdot 5 = 1$ y $-3 \cdot 8 + 5 \cdot 5 = 1$ son ambas combinaciones válidas: si $(s, t)$ sirve, también $(s + kb', t - ka')$ con $a' = a/d$, $b' = b/d$. El algoritmo entrega una en particular.

## Preguntas de repaso

> [!question]- ¿Por qué el último resto no nulo es combinación lineal de $a$ y $b$?
> Porque $r_0$ y $r_1$ lo son por definición, y cada nuevo resto es $r_{i-1} - q_i r_i$, una combinación de dos que ya lo son.

> [!question]- Dado $\operatorname{MCD}(a, b) = 1 = sa + tb$, ¿qué es $s$ respecto de $a$ módulo $b$?
> Un inverso: $sa = 1 - tb \equiv 1 \pmod b$.

> [!question]- ¿Cómo se deduce que $p \mid ab$ implica $p \mid a$ o $p \mid b$?
> Si $p \nmid a$, como $p$ es primo $\operatorname{MCD}(p, a) = 1$, y por el lema de Euclides $p \mid b$.

> [!question]- Encuentre $s, t$ con $\operatorname{MCD}(240, 46) = 240 s + 46 t$.
> El algoritmo da $\operatorname{MCD} = 2$ con $s = -9$ y $t = 47$: $-2160 + 2162 = 2$.
