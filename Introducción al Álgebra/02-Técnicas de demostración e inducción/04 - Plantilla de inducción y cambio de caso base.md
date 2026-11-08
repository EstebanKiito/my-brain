---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[03 - Principio de inducción matemática]]"
---

# Plantilla de inducción y cambio de caso base

Escribir bien una inducción evita errores: conviene fijar primero el enunciado $P(n)$ y luego seguir una plantilla con caso base, paso inductivo y conclusión. La misma idea funciona si el caso base no es $1$ sino cualquier entero $n_0$.

## La plantilla

Primero se identifica $P(n)$ y se aclara qué dicen $P(1)$, $P(k)$ y $P(k+1)$. Luego se escribe:

> [!tip] Plantilla de inducción
> **Caso base:** demostrar $P(1)$.
> **Paso inductivo:** suponer $P(k)$ verdadera (hipótesis de inducción) y deducir $P(k+1)$.
> **Conclusión:** por inducción, $P(n)$ vale para todo $n \in \mathbb{N}$.

## Ejemplo: $n^2 + n$ es par

Pruebe que $n^2 + n$ es par para todo $n \in \mathbb{N}$.

**Demostración.** Sea $P(n)$: "$n^2 + n$ es par".

- **Caso base** ($n=1$): $1^2 + 1 = 2$, que es par.
- **Paso inductivo:** supongamos que $k^2 + k$ es par, es decir, $k^2 + k = 2m$ para algún entero $m$. Entonces

$$
(k+1)^2 + (k+1) = k^2 + 2k + 1 + k + 1 = (k^2 + k) + 2k + 2 = 2m + 2(k+1) = 2(m + k + 1),
$$

que es par. Luego $P(k+1)$ es verdadera.

Por inducción, $n^2 + n$ es par para todo $n \in \mathbb{N}$.

## Cambiar el caso base

La inducción también parte de un entero arbitrario $n_0$ (positivo, negativo o cero) para probar $P(n)$ para todo $n \ge n_0$. El caso base es ahora $P(n_0)$ y el paso inductivo es $P(k) \Rightarrow P(k+1)$ para $k \ge n_0$.

**Ejemplo.** Pruebe que $n^2 \le 2^n$ para todo natural $n \ge 4$.

**Demostración.**

- **Caso base** ($n=4$): $4^2 = 16 = 2^4$, así que $4^2 \le 2^4$.
- **Paso inductivo:** supongamos $k^2 \le 2^k$ con $k \ge 4$. Entonces

$$
(k+1)^2 = k^2 + 2k + 1 \le 2^k + 2k + 1 \le 2^k + 2^k = 2^{k+1},
$$

porque $2k + 1 \le 2^k$ para $k \ge 4$ (en $k=4$, $9 \le 16$, y $2^k$ crece más rápido). Luego $P(k+1)$ vale.

Por inducción, $n^2 \le 2^n$ para todo $n \ge 4$.

> [!warning] El caso base debe cubrir el punto de arranque
> Si el enunciado vale desde $n \ge 4$, el caso base es $P(4)$, no $P(1)$ (que aquí ni siquiera se cumple: $1^2 \le 2$ sí, pero $3^2 = 9 \not\le 8$). La inducción demuestra solo lo que el caso base "enciende".

## Preguntas de repaso

> [!question]- ¿En qué orden conviene escribir una inducción para no perderse?
> Primero se define $P(n)$ con precisión, después el caso base, luego el paso inductivo (usando explícitamente la hipótesis de inducción) y al final la conclusión.

> [!question]- En $n^2 + n$ par, ¿qué se hace con la hipótesis de inducción?
> Se escribe $k^2 + k = 2m$ y se reemplaza dentro de $(k+1)^2 + (k+1)$, dejando todo como $2(m + k + 1)$, que es par.

> [!question]- ¿Por qué $2k + 1 \le 2^k$ para $k \ge 4$?
> En $k = 4$ vale $9 \le 16$. Al pasar de $k$ a $k+1$, $2k+1$ crece en $2$ mientras $2^k$ se duplica, así que la desigualdad se mantiene.

> [!question]- ¿Qué cambia al usar un caso base $n_0 \neq 1$?
> Solo el punto de partida: el caso base es $P(n_0)$ y el paso inductivo exige $k \ge n_0$. La conclusión es $P(n)$ para todo $n \ge n_0$.
