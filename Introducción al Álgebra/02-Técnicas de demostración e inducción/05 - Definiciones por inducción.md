---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[04 - Plantilla de inducción y cambio de caso base]]"
---

# Definiciones por inducción

La inducción no solo demuestra propiedades: también **define** objetos, como la suma de una sucesión o una sucesión dada por recurrencia. Una definición por inducción da un caso base (qué significa el símbolo en $n=1$) y un paso (qué significa en $k+1$ en términos de $k$).

## La sumatoria definida recursivamente

Dada una sucesión $a_1, a_2, \dots$, la suma $\sum_{\ell=1}^{n} a_\ell$ se define por inducción:

$$
\sum_{\ell=1}^{1} a_\ell = a_1, \qquad
\sum_{\ell=1}^{k+1} a_\ell = \left(\sum_{\ell=1}^{k} a_\ell\right) + a_{k+1} \quad (k \ge 1).
$$

El caso base fija la suma de un solo término y el paso "agrega" un término a la suma anterior. Desenrollando el paso repetidamente, $\sum_{\ell=1}^{n} a_\ell = a_1 + a_2 + \dots + a_n$.

> [!tip] Definición por inducción
> Un objeto definido por inducción tiene **dos piezas**: el valor en el caso base y una regla que construye el valor $k+1$ a partir del valor $k$. Ambas juntas determinan el objeto para todo $n$.

## Ejemplo: la suma de los primeros naturales

Pruebe que $\displaystyle\sum_{\ell=1}^{n} \ell = \frac{n(n+1)}{2}$ para todo $n \in \mathbb{N}$.

**Demostración por inducción sobre $n$.**

- **Caso base** ($n=1$): $\sum_{\ell=1}^{1} \ell = 1 = \frac{1 \cdot 2}{2}$.
- **Paso inductivo:** supongamos $\sum_{\ell=1}^{k} \ell = \frac{k(k+1)}{2}$. Entonces, por la definición recursiva de la suma,

$$
\sum_{\ell=1}^{k+1} \ell = \sum_{\ell=1}^{k} \ell + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{(k+1)(k+2)}{2}.
$$

Por inducción, la fórmula vale para todo $n \in \mathbb{N}$.

## Ejemplo: una sucesión por recurrencia

Sea $u_0 = 0$ y $u_{k+1} = 3u_k + 3^k$ para $k \ge 0$. Pruebe que $u_n = n\,3^{n-1}$ para todo entero $n \ge 0$.

**Demostración por inducción.**

- **Caso base** ($n=0$): $u_0 = 0 = 0 \cdot 3^{-1}$.
- **Paso inductivo:** supongamos $u_k = k\,3^{k-1}$. Entonces

$$
u_{k+1} = 3u_k + 3^k = 3 \cdot k\,3^{k-1} + 3^k = k\,3^k + 3^k = (k+1)\,3^k,
$$

que es exactamente $(k+1)\,3^{(k+1)-1}$. Por inducción, $u_n = n\,3^{n-1}$ para todo $n \ge 0$.

> [!warning] Recurrencia y fórmula cerrada son cosas distintas
> La recurrencia $u_{k+1} = 3u_k + 3^k$ *define* la sucesión paso a paso, pero no dice de una vez cuánto vale $u_{100}$. La **fórmula cerrada** $u_n = n\,3^{n-1}$ sí lo dice, y la inducción es el puente que demuestra que ambas coinciden.

## Preguntas de repaso

> [!question]- ¿Qué dos piezas tiene la definición inductiva de una sumatoria?
> El caso base ($\sum_{\ell=1}^{1} a_\ell = a_1$) y el paso ($\sum_{\ell=1}^{k+1} a_\ell = \sum_{\ell=1}^{k} a_\ell + a_{k+1}$). Con ambas, la suma queda determinada para cualquier $n$.

> [!question]- En la suma de los naturales, ¿qué permite pasar de $\frac{k(k+1)}{2} + (k+1)$ a $\frac{(k+1)(k+2)}{2}$?
> Sacar factor común $k+1$: $\frac{k(k+1)}{2} + (k+1) = (k+1)\left(\frac{k}{2} + 1\right) = (k+1)\frac{k+2}{2}$.

> [!question]- ¿Cuál es la ventaja de la fórmula cerrada frente a la recurrencia?
> La fórmula cerrada permite calcular $u_n$ directamente, sin recorrer $u_1, u_2, \dots, u_{n-1}$ uno por uno.

> [!question]- ¿Qué se asume sobre $u_k$ en el paso inductivo del ejemplo de la recurrencia?
> Que $u_k = k\,3^{k-1}$ (la hipótesis de inducción). Con eso, $u_{k+1} = 3u_k + 3^k$ se reduce a $(k+1)\,3^k$.
