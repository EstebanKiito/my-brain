---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[01 - Divisibilidad y división con resto]]"
---

# Máximo común divisor y algoritmo de Euclides

Para simplificar fracciones, decidir si un número tiene inverso modular o resolver ecuaciones de congruencia hay que saber qué divisores comparten dos números. Factorizar es caro; el algoritmo de Euclides, de hace más de dos mil años, entrega la respuesta sin factorizar nada.

## Definición

El **máximo común divisor** $\operatorname{MCD}(a, b)$ (en inglés $\gcd$) es el mayor natural $n$ tal que $n \mid a$ y $n \mid b$. Si $\operatorname{MCD}(a, b) = 1$, se dice que $a$ y $b$ son **primos relativos** o **coprimos**: no comparten ningún factor salvo el $1$. Por ejemplo $\operatorname{MCD}(12, 18) = 6$ y $\operatorname{MCD}(8, 5) = 1$.

Calcularlo listando divisores funciona con números chicos, pero es inviable con cientos de dígitos. Se necesita una idea mejor.

## El teorema clave

> [!tip] Reducción de Euclides
> Si $a, b \in \mathbb{Z}\setminus\{0\}$, entonces $\operatorname{MCD}(a, b) = \operatorname{MCD}(b, a \bmod b)$.

**Por qué:** se escribe $a = kb + (a \bmod b)$. Si $c$ divide a $a$ y a $b$, divide a $a - kb = a \bmod b$. Y si $c$ divide a $b$ y a $a \bmod b$, divide a $kb + (a \bmod b) = a$. Entonces los divisores comunes de $(a, b)$ y de $(b, a \bmod b)$ son exactamente los mismos, y por tanto también su máximo.

## El algoritmo

Aplicar la reducción hasta que el segundo argumento sea $0$:

$$\operatorname{MCD}(a, b) = \begin{cases} a & \text{si } b = 0 \\ \operatorname{MCD}(b, a \bmod b) & \text{si } b > 0. \end{cases}$$

Termina porque el segundo argumento es un natural que decrece estrictamente en cada paso (siempre $a \bmod b < b$).

**Ejemplo, $\operatorname{MCD}(403, 156)$:**

| Paso | $a$ | $b$ | $a \bmod b$ |
|---|---|---|---|
| 1 | 403 | 156 | 91 |
| 2 | 156 | 91 | 65 |
| 3 | 91 | 65 | 26 |
| 4 | 65 | 26 | 13 |
| 5 | 26 | 13 | 0 |

El último resto no nulo es $13$, así que $\operatorname{MCD}(403, 156) = 13$. En efecto $403 = 13 \cdot 31$ y $156 = 13 \cdot 12$, y $31$ y $12$ no comparten factores.

```python
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

## Eficiencia y consecuencias útiles

Cada dos pasos el resto se reduce al menos a la mitad, de modo que el número de pasos es del orden de $\log b$; con números de 600 dígitos son unas pocas miles de divisiones. Esa eficiencia es lo que hace práctico generar claves en [[09 - RSA: construcción, correctitud e implementación]].

Dos consecuencias frecuentes:

- Si $a \equiv b \pmod m$, entonces $\operatorname{MCD}(a, m) = \operatorname{MCD}(b, m)$, porque $a \bmod m = b \bmod m$ y ambos MCD son $\operatorname{MCD}(m, a \bmod m)$.
- $\operatorname{MCD}(a, b)$ divide a toda combinación $xa + yb$; la sección siguiente muestra que además **es** la menor combinación positiva ([[04 - Identidad de Bézout y algoritmo de Euclides extendido]]).

> [!warning] Orden y signos
> El algoritmo funciona aunque $a < b$ (el primer paso solo intercambia los argumentos, pues $a \bmod b = a$). Además $\operatorname{MCD}(a, 0) = a$, no $0$.

## Preguntas de repaso

> [!question]- ¿Por qué $\operatorname{MCD}(a, b) = \operatorname{MCD}(b, a \bmod b)$?
> Porque ambos pares tienen los mismos divisores comunes: cualquier divisor de $a$ y $b$ divide a $a - kb$, y cualquier divisor de $b$ y $a \bmod b$ divide a $kb + (a \bmod b)$.

> [!question]- ¿Por qué el algoritmo siempre termina?
> El segundo argumento es un natural que disminuye estrictamente en cada paso, y no puede bajar de $0$.

> [!question]- Calcule $\operatorname{MCD}(240, 46)$.
> $240 \bmod 46 = 10$, $46 \bmod 10 = 6$, $10 \bmod 6 = 4$, $6 \bmod 4 = 2$, $4 \bmod 2 = 0$; luego el MCD es $2$.

> [!question]- ¿Qué relación hay entre MCD y números coprimos?
> Dos números son coprimos justamente cuando su MCD es $1$; esa condición decide si existe inverso modular.
