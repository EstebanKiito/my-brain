---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[03 - Inversas trigonométricas]]"
---

# Ecuaciones trigonométricas

En una ecuación trigonométrica la incógnita aparece dentro del seno, coseno o tangente. Por la periodicidad, si hay una solución hay infinitas: basta encontrar las **soluciones básicas** en $[0, 2\pi)$ y sumarles el período.

## Soluciones generales

Usando la circunferencia unitaria se deducen los conjuntos solución de las tres ecuaciones básicas:

- $\sin x = a$: $S = \{k\pi + (-1)^k \alpha \mid k \in \mathbb{Z}\}$, con $\alpha$ una solución básica en el primer o cuarto cuadrante.
- $\cos x = b$: $S = \{2k\pi \pm \alpha \mid k \in \mathbb{Z}\}$, con $\alpha$ en el primer o segundo cuadrante.
- $\tan x = c$: $S = \{k\pi + \gamma \mid k \in \mathbb{Z}\}$, con $\gamma$ en el primer o cuarto cuadrante.

![Soluciones básicas de sen x igual a a](adjuntos/Soluciones%20b%C3%A1sicas%20de%20sen%20x%20igual%20a%20a.png)

> [!example]- Transcripción de la figura
> Circunferencia unitaria cortada por la recta horizontal $y = a$ en dos puntos. Los radios rojos a esos puntos forman los ángulos $\alpha$ (primer cuadrante) y $\pi - \alpha$ (segundo cuadrante): los dos ángulos de $[0, 2\pi)$ con seno $a$.

![Soluciones básicas de cos x igual a b](adjuntos/Soluciones%20b%C3%A1sicas%20de%20cos%20x%20igual%20a%20b.png)

> [!example]- Transcripción de la figura
> Circunferencia unitaria cortada por la recta vertical $x = b$ (con $b < 0$) en dos puntos, uno arriba y otro abajo del eje. Los radios rojos forman los ángulos $\alpha$ (segundo cuadrante) y $2\pi - \alpha$ (tercer cuadrante): los dos ángulos de $[0, 2\pi)$ con coseno $b$, simétricos respecto del eje $x$.

> [!tip] De básica a general
> Encuentre primero una (o dos) soluciones en $[0, 2\pi)$ y luego "repítalas" sumando el período ($2\pi$ para seno y coseno, $\pi$ para tangente) con el patrón correspondiente.

## Ejemplo

Resuelva $\sin x = \cos x$.

Dividiendo por $\cos x$ (que no se anula donde $\sin = \cos$): $\tan x = 1$. La solución básica es $\gamma = \pi/4$, así que $S = \{\pi/4 + k\pi \mid k \in \mathbb{Z}\}$.

**Otro ejemplo.** Resuelva $\sin x = \sin 2x$.

Con $\sin 2x = 2\sin x\cos x$, la ecuación es $\sin x = 2\sin x\cos x$, o sea $\sin x\,(1 - 2\cos x) = 0$. Luego $\sin x = 0$ (da $x = k\pi$) o $\cos x = 1/2$ (da $x = \pm\pi/3 + 2k\pi$).

> [!warning] No cancelar $\sin x$ a ciegas
> En $\sin x = 2\sin x\cos x$, dividir por $\sin x$ perdería las soluciones $\sin x = 0$. Se factoriza y se usa que un producto es cero si lo es alguno de sus factores.

## Preguntas de repaso

> [!question]- ¿Por qué una ecuación trigonométrica tiene infinitas soluciones?
> Por la periodicidad: si $x_0$ es solución, también lo es $x_0 + 2k\pi$ (o $x_0 + k\pi$ para la tangente). Por eso se buscan las básicas y se les suma el período.

> [!question]- Escriba el conjunto solución de $\sin x = 1/2$.
> Las básicas son $\pi/6$ y $5\pi/6$. En forma compacta, $S = \{k\pi + (-1)^k \pi/6 \mid k \in \mathbb{Z}\}$.

> [!question]- Resuelva $\cos x = 0$.
> $\cos x = 0$ en $\pi/2$ y $3\pi/2$, es decir, $S = \{\pi/2 + k\pi \mid k \in \mathbb{Z}\}$ (o $x = (2k+1)\pi/2$).

> [!question]- ¿Cuándo conviene factorizar en vez de dividir?
> Cuando aparece un factor que puede anularse (como $\sin x$ o $\cos x$). Factorizar conserva todas las soluciones; dividir puede descartar las que anulan ese factor.
