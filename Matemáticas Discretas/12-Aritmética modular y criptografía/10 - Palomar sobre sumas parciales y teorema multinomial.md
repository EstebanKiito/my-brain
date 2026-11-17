---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/conteo
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos:
  - "[[02 - Congruencias módulo n y aritmética en Z_n]]"
---

# Palomar sobre sumas parciales y teorema multinomial

Dos herramientas de conteo que aparecen junto a la aritmética modular. El principio del palomar (ver [[04 - Equinumerosidad, conjuntos finitos y principio del palomar]]) se combina con restos para probar que existen ciertas sumas; el teorema multinomial generaliza el binomio y cuenta ordenamientos con repetición.

## Palomar y restos: una suma consecutiva divisible por $m$

> [!tip] Enunciado
> En toda secuencia de $m$ enteros $a_1, \dots, a_m$ existen uno o más términos **consecutivos** cuya suma es divisible por $m$.

**Idea:** se consideran las sumas parciales $S_i = a_1 + \dots + a_i$ para $i = 1, \dots, m$ y sus restos módulo $m$.

- Si algún $S_i \equiv 0$, los términos $a_1, \dots, a_i$ ya sirven.
- Si no, los $m$ restos caen en $\{1, \dots, m-1\}$, solo $m - 1$ casilleros. Por el principio del palomar hay $i < j$ con $S_i \equiv S_j$, y entonces $S_j - S_i = a_{i+1} + \dots + a_j \equiv 0 \pmod m$.

**Ejemplo con $m = 5$:** para $3, 1, 2, 2, 1$ las sumas parciales son $3, 4, 6, 8, 9$, con restos $3, 4, 1, 3, 4$ (ninguno es $0$). Los restos de $S_1$ y $S_4$ coinciden, y $a_2 + a_3 + a_4 = 1 + 2 + 2 = 5$ es divisible por $5$.

La garantía es de **existencia**: el argumento no dice cuál tramo es, solo que hay uno.

## Teorema multinomial

Para $n \ge 1$,

$$(x_1 + x_2 + \dots + x_m)^n = \sum_{n_1 + \dots + n_m = n} \frac{n!}{n_1!\, n_2! \cdots n_m!}\, x_1^{n_1} x_2^{n_2} \cdots x_m^{n_m}.$$

**Por qué:** al desarrollar el producto de $n$ factores $(x_1 + \dots + x_m)$ se elige un término de cada factor. El monomio $x_1^{n_1} \cdots x_m^{n_m}$ se forma escogiendo $x_1$ en $n_1$ de los $n$ factores, $x_2$ en $n_2$ de los restantes, etc., lo que se puede hacer de

$$\binom{n}{n_1}\binom{n - n_1}{n_2} \cdots \binom{n - n_1 - \dots - n_{m-1}}{n_m} = \frac{n!}{n_1! \cdots n_m!}$$

maneras. Con $m = 2$ se recupera el teorema del binomio.

**Ejemplos:**

- En $(x + y + z)^3$, el coeficiente de $xyz$ es $\frac{3!}{1!1!1!} = 6$ y el de $x^2 y$ es $\frac{3!}{2!1!0!} = 3$. Hay $\binom{5}{2} = 10$ monomios en total, y la suma de todos los coeficientes es $3^3 = 27$ (se evalúa en $x = y = z = 1$).
- Palabras que se forman reordenando las letras de MISSISSIPPI (1 M, 4 I, 4 S, 2 P): $\frac{11!}{1!\,4!\,4!\,2!} = 34650$.

> [!warning] Cantidad de términos frente a coeficiente
> $\frac{n!}{n_1! \cdots n_m!}$ es el **coeficiente** de un monomio; el número de monomios distintos es $\binom{n + m - 1}{m - 1}$ (soluciones de $n_1 + \dots + n_m = n$).

## Preguntas de repaso

> [!question]- ¿Por qué hay que mirar $m$ sumas parciales y no menos?
> Porque con $m$ sumas y solo $m - 1$ restos no nulos posibles el palomar fuerza una repetición; con menos sumas no hay garantía.

> [!question]- ¿Qué pasa si una suma parcial vale $0$ módulo $m$?
> Ese prefijo ya es el tramo buscado; el palomar solo se necesita cuando ningún resto es $0$.

> [!question]- ¿Cuál es el coeficiente de $x^2 y^2$ en $(x + y)^4$ y qué dice el multinomial?
> $\frac{4!}{2!2!} = 6$, igual al binomial $\binom{4}{2}$.

> [!question]- ¿Cuántos monomios tiene $(x_1 + x_2 + x_3)^3$?
> $\binom{5}{2} = 10$, uno por cada solución de $n_1 + n_2 + n_3 = 3$ en naturales.
