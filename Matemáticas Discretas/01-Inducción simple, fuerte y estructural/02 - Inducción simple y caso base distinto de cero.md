---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - origen/complemento
prerrequisitos:
  - "[[01 - Naturales, axiomas de Peano y principio del buen orden]]"
---

# Inducción simple y caso base distinto de cero

Para demostrar que una propiedad vale para **todos** los naturales no se pueden revisar uno por uno. La inducción simple lo resuelve con dos verificaciones: que valga para el primer natural y que cada natural "contagie" la propiedad a su sucesor, como una fila de fichas de dominó.

## El principio

> [!tip] Principio de inducción simple (PIS)
> Sea $P$ una propiedad sobre $\mathbb{N}$. Si **(1)** $P(0)$ es verdadera y **(2)** para todo $n \in \mathbb{N}$, $P(n) \Rightarrow P(n+1)$, entonces $P(n)$ es verdadera para todo $n \in \mathbb{N}$.

En la formulación con conjuntos es equivalente: si $A \subseteq \mathbb{N}$, $0 \in A$ y ($n \in A \Rightarrow n + 1 \in A$), entonces $A = \mathbb{N}$. Las partes de una demostración tienen nombre fijo:

| Parte | Qué es |
|---|---|
| **Caso base (CB)** | Se verifica $P(0)$ a mano, de forma independiente |
| **Hipótesis de inducción (HI)** | Se *supone* $P(n)$ para un $n$ cualquiera |
| **Tesis de inducción (TI)** | Se demuestra $P(n+1)$ usando la HI |

> [!warning] La dirección importa
> La demostración se arma desde la HI hacia la tesis. No se puede partir de lo que se quiere probar ($P(n+1)$) y "llegar a algo verdadero".

## Ejemplo: suma de los primeros naturales

Se quiere probar $\displaystyle\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$.

- **CB** ($n = 0$): $\sum_{i=0}^{0} i = 0 = \frac{0 \cdot 1}{2}$.
- **HI:** se supone $\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$.
- **TI:** se separa el último término y se usa la HI:

$$\sum_{i=0}^{n+1} i = \sum_{i=0}^{n} i + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}.$$

Esa última expresión es justamente la fórmula con $n+1$ en lugar de $n$, así que la propiedad vale para todo $n$.

## Caso base distinto de cero

Hay propiedades falsas para los primeros naturales que se vuelven ciertas desde cierto $n_0$. Entonces el caso base es $P(n_0)$ y la conclusión vale para todo $n \ge n_0$.

> [!tip] PIS, tercera formulación
> Si $P(n_0)$ es verdadera y para todo $n \ge n_0$, $P(n) \Rightarrow P(n+1)$, entonces $P(n)$ vale para todo $n \ge n_0$.

**Ejemplo:** $n! > 2^n$ para todo $n \ge 4$. Es falso para $n = 3$ ($6 < 8$), por eso el caso base es $n = 4$: $4! = 24 > 16 = 2^4$. Para el paso, con $n \ge 4$:

$$(n+1)! = n!\,(n+1) > 2^n (n+1) \ge 2^n \cdot 5 > 2^{n+1}.$$

La primera desigualdad usa la HI; la segunda usa $n + 1 \ge 5$; la última, $5 > 2$.

## Preguntas de repaso

> [!question]- ¿Por qué el caso base debe verificarse aparte y no se obtiene del paso inductivo?
> Porque el paso inductivo solo dice "si vale para $n$, vale para $n+1$"; sin un primer valor verdadero nadie "empuja la primera ficha". Por ejemplo, $n = n + 1$ cumple el paso inductivo (suma $1$ a ambos lados) y es falsa para todo $n$.

> [!question]- En $n! > 2^n$, ¿por qué se parte en $n = 4$ y no en $n = 0$?
> Porque la propiedad es falsa para $n = 1, 2, 3$ y entonces el caso base en $0$ ni siquiera se verifica. La inducción solo propaga desde el caso base hacia arriba.

> [!question]- ¿Qué se asume y qué se demuestra en el paso inductivo?
> Se asume $P(n)$ (HI) y se demuestra $P(n+1)$ (tesis), usando la HI en algún momento del argumento.
