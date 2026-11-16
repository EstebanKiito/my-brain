---
ramo: "Introducción al Cálculo"
tema: "Sucesiones, monotonía y axioma del supremo"
tags:
  - intro-calculo/sucesiones
  - origen/complemento
prerrequisitos:
  - "[[01 - Sucesiones y formas de definirlas]]"
  - "[[03 - Funciones monótonas]]"
---

# Sucesiones acotadas y monótonas

Dos propiedades describen el "aspecto" de una sucesión sin calcular su límite: si se mantiene dentro de una franja (acotada) y si siempre sube o siempre baja (monótona). Juntas, tienen una consecuencia profunda: una sucesión monótona y acotada **converge**. Por eso las interrogaciones piden, para sucesiones definidas por recurrencia, demostrar primero la monotonía y la cota.

![Gráfico de una sucesión como puntos aislados](adjuntos/Gr%C3%A1fico%20de%20una%20sucesi%C3%B3n%20como%20puntos%20aislados.png)

> [!example]- Transcripción de la figura (cuaderno, clase 24)
> Ejes cartesianos con puntos azules aislados sobre los enteros $1, 2, 3, \ldots$; algunos quedan sobre el eje horizontal y otros bajo él. Un punto está rotulado $(m, a_m)$: la sucesión es la nube de pares (índice, valor).

## Sucesiones acotadas

> [!tip] Acotación
> Una sucesión $\{a_n\}$ es **acotada superiormente** si existe $M$ con $a_n \le M$ para todo $n$; **acotada inferiormente** si existe $m$ con $m \le a_n$ para todo $n$; y **acotada** si cumple ambas, es decir, existe $K$ con $|a_n| \le K$ para todo $n$.

Esas cotas son para el **conjunto de valores** $\{a_n : n \in \mathbb{N}\}$, por lo que se pueden estudiar con las herramientas de [[03 - Cotas, supremo e ínfimo|cota superior, supremo e ínfimo]].

![Sucesión acotada entre menos K y K](adjuntos/Sucesi%C3%B3n%20acotada%20entre%20menos%20K%20y%20K.png)

> [!example]- Transcripción de la figura (cuaderno, clase 24)
> Dos rectas horizontales naranjas, $y = K$ y $y = -K$, y una nube de puntos azules que queda siempre entre ambas: $-K \le a_n \le K$ para todo $n$.

## Sucesiones monótonas

Como una sucesión es una función definida en $\mathbb{N}$, valen las mismas definiciones que para funciones, con la ventaja de que basta comparar términos **consecutivos**.

> [!tip] Monotonía
> $\{a_n\}$ es **creciente** si $a_n \le a_{n+1}$ para todo $n$ y **estrictamente creciente** si $a_n < a_{n+1}$. Es **decreciente** si $a_{n+1} \le a_n$ y **estrictamente decreciente** si $a_{n+1} < a_n$. Es **monótona** si es creciente o decreciente.

Basta comparar consecutivos porque la desigualdad se propaga: $a_1 \le a_2 \le a_3 \le \dots$ implica $a_i \le a_j$ para $i < j$.

## Cómo demostrar monotonía

1. **Diferencia:** estudiar el signo de $a_{n+1} - a_n$ (útil con fórmulas explícitas y con raíces, racionalizando).
2. **Cociente:** si $a_n > 0$, comparar $\tfrac{a_{n+1}}{a_n}$ con $1$ (útil con factoriales, potencias y productos).
3. **Inducción** (para recurrencias $a_{n+1} = f(a_n)$): se comprueba $a_1 \le a_2$ y se supone $a_n \le a_{n+1}$ para deducir $a_{n+1} \le a_{n+2}$ usando que $f$ preserva el orden.

**Ejemplo con la diferencia: $a_n = \sqrt{n^2 + n} - n$ (Guía 10).** Multiplicando por el conjugado, $a_n = \dfrac{n}{\sqrt{n^2 + n} + n} = \dfrac{1}{\sqrt{1 + 1/n} + 1}$. Como $\tfrac{1}{n}$ decrece, $\sqrt{1 + 1/n}$ decrece y el denominador decrece, luego $a_n$ **crece**. Además $\sqrt{1 + 1/n} > 1$ da $a_n < \tfrac{1}{2}$: está acotada por $\tfrac{1}{2}$.

**Ejemplo con el cociente: $a_n = \dfrac{1\cdot 3\cdot 5\cdots(2n - 1)}{2\cdot 4\cdot 6\cdots 2n}$ (Guía 10).** Cada término se obtiene del anterior multiplicando por $\tfrac{2n + 1}{2n + 2} < 1$, así que la sucesión (de términos positivos) es estrictamente decreciente y acotada inferiormente por $0$. Está acotada entre $0$ y $a_1 = \tfrac{1}{2}$.

## Un ejemplo con inducción: Fibonacci

La sucesión $F_1 = F_2 = 1$, $F_n = F_{n-1} + F_{n-2}$ (I6, 2024-1) tiene todos sus términos positivos (suma de positivos) y es **no decreciente**, pues $F_n = F_{n-1} + F_{n-2} \ge F_{n-1}$. Además la razón entre términos consecutivos queda acotada:
$$\frac{F_n}{F_{n-1}} = 1 + \frac{F_{n-2}}{F_{n-1}} \le 1 + 1 = 2 \quad (n \ge 3),$$
y como $\tfrac{F_{n-1}}{F_{n-2}} \le 2$ implica $\tfrac{F_{n-2}}{F_{n-1}} \ge \tfrac{1}{2}$, se obtiene $\tfrac{F_n}{F_{n-1}} \ge \tfrac{3}{2}$ para $n \ge 3$. Así los cocientes consecutivos quedan en $\left[\tfrac{3}{2}, 2\right]$.

## Monotonía y acotación dan convergencia

> [!tip] Teorema de la sucesión monótona
> Toda sucesión **creciente y acotada superiormente** converge (a su supremo); toda sucesión **decreciente y acotada inferiormente** converge (a su ínfimo).

Es consecuencia del axioma del supremo (se demuestra en el tema de límites de sucesiones, una vez definido el límite). Una sucesión que converge es acotada, pero una acotada **no** tiene por qué converger si no es monótona: $a_n = (-1)^n$ está acotada y oscila entre $-1$ y $1$.

> [!warning] Las dos condiciones a la vez
> Creciente **sin** cota superior no converge ($a_n = n$), y acotada **sin** monotonía tampoco necesariamente ($(-1)^n$). Las interrogaciones piden las dos partes por separado, y cada una puntúa.

## Preguntas de repaso

> [!question]- ¿Por qué basta comparar términos consecutivos para ver que una sucesión es creciente?
> Porque $a_1 \le a_2 \le \dots \le a_n$ encadena las desigualdades: por transitividad, $a_i \le a_j$ siempre que $i < j$.

> [!question]- ¿Es acotada la sucesión $a_n = n$? ¿Y $b_n = \frac{1}{n}$?
> $a_n$ no: no tiene cota superior (principio de Arquímedes). $b_n$ sí: $0 < \frac{1}{n} \le 1$.

> [!question]- ¿Qué técnica sirve para $a_n = \frac{n!}{3^n}$?
> El cociente: $\frac{a_{n+1}}{a_n} = \frac{n + 1}{3}$, que es $< 1$ solo para $n < 2$; de modo que $a_n$ decrece al comienzo y crece después, no es monótona.

> [!question]- Si $\{a_n\}$ es decreciente y acotada inferiormente por $2$, ¿qué se sabe?
> Que converge, y su límite es $\ge 2$ (es su ínfimo).
