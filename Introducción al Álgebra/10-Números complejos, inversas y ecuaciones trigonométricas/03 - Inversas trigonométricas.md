---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Seno y coseno en la circunferencia unitaria]]"
---

# Inversas trigonométricas

Las funciones seno, coseno y tangente no son inyectivas en todo $\mathbb{R}$, así que para invertirlas se restringe su dominio a un tramo donde sí lo sean. Las inversas resultantes, $\arcsin$, $\arccos$ y $\arctan$, devuelven un ángulo en ese tramo.

## Arcoseno, arcocoseno y arcotangente

| Función | Dominio restringido | Inversa |
|---|---|---|
| $\sin x$ | $[-\pi/2, \pi/2]$ | $\arcsin y = x \iff \sin x = y \wedge -\pi/2 \le x \le \pi/2$ |
| $\cos x$ | $[0, \pi]$ | $\arccos y = x \iff \cos x = y \wedge 0 \le x \le \pi$ |
| $\tan x$ | $(-\pi/2, \pi/2)$ | $\arctan y = x \iff \tan x = y \wedge -\pi/2 < x < \pi/2$ |

> [!tip] El rango es clave
> $\arcsin$ devuelve ángulos en $[-\pi/2, \pi/2]$, $\arccos$ en $[0, \pi]$ y $\arctan$ en $(-\pi/2, \pi/2)$. El valor de la inversa **siempre** cae en ese rango, aunque el ángulo original no estuviera ahí.

![Gráfico del arcoseno](adjuntos/Gr%C3%A1fico%20del%20arcoseno.png)

> [!example]- Transcripción de la figura
> Curva roja $y = \arcsin(x)$, creciente, definida de $x = -1$ a $x = 1$: parte en $(-1, -\frac{\pi}{2})$, pasa por el origen y termina en $(1, \frac{\pi}{2})$. Es la gráfica del seno restringido a $[-\frac{\pi}{2}, \frac{\pi}{2}]$ reflejada en la recta $y = x$.

![Gráfico del arcocoseno](adjuntos/Gr%C3%A1fico%20del%20arcocoseno.png)

> [!example]- Transcripción de la figura
> Curva roja $y = \arccos(x)$, decreciente, de $(-1, \pi)$ a $(1, 0)$, pasando por $(0, \frac{\pi}{2})$.

![Tangente restringida y arcotangente](adjuntos/Tangente%20restringida%20y%20arcotangente.png)

> [!example]- Transcripción de la figura
> A la izquierda, $y = \tan(x)$ con asíntotas verticales discontinuas en $\pm\frac{\pi}{2}$ y $\pm\frac{3\pi}{2}$; la rama central, entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$, está en rojo (es el tramo que se invierte) y las otras en azul. A la derecha, $y = \arctan(x)$: curva roja creciente definida en todo $\mathbb{R}$, que pasa por el origen y se acerca a las asíntotas horizontales $y = \pm\frac{\pi}{2}$ sin tocarlas.

**Ejemplo.** $\arcsin(\sin(\pi/3)) = \pi/3$, pero $\arcsin(\sin(2\pi/3)) = \pi/3$, no $2\pi/3$: como $2\pi/3 \notin [-\pi/2, \pi/2]$, la inversa devuelve el ángulo de igual seno que sí está en el rango.

## Componer inversas con funciones

**Ejemplo.** Exprese $\cos(\arctan x)$ en términos de $x$. Sea $\theta = \arctan x$, así $\tan\theta = x$ y $\theta \in (-\pi/2, \pi/2)$. En ese rango el coseno es positivo, y $\cos\theta = \frac{1}{\sqrt{1 + \tan^2\theta}} = \frac{1}{\sqrt{1 + x^2}}$.

**Ejemplo.** Exprese $\sin(2\arccos x)$. Sea $\theta = \arccos x$, con $\cos\theta = x$ y $\theta \in [0,\pi]$ (donde $\sin\theta \ge 0$). Entonces $\sin(2\theta) = 2\sin\theta\cos\theta = 2x\sqrt{1 - x^2}$.

> [!warning] No "cancelar" a ciegas
> $\arcsin(\sin x) = x$ solo si $x \in [-\pi/2, \pi/2]$. Fuera de ese rango, la inversa devuelve otro ángulo con el mismo seno.

## Igualdades entre inversas

Para probar algo como $\arctan 2 + \arctan 3 = \frac{3\pi}{4}$ se hacen dos cosas:

1. Calcular una función trigonométrica de **ambos lados**: con $\alpha = \arctan 2$ y $\beta = \arctan 3$, $\tan(\alpha + \beta) = \frac{2 + 3}{1 - 6} = -1 = \tan\frac{3\pi}{4}$.
2. **Ubicar** los ángulos en un intervalo donde esa función sea inyectiva: como $2, 3 > 1$, $\alpha, \beta \in (\frac{\pi}{4}, \frac{\pi}{2})$, así que $\alpha + \beta \in (\frac{\pi}{2}, \pi)$, donde la tangente es inyectiva. Ahí el único ángulo con tangente $-1$ es $\frac{3\pi}{4}$.

> [!warning] El paso 2 no es opcional
> $\tan(\alpha + \beta) = -1$ también lo cumple $-\frac{\pi}{4}$. Sin ubicar $\alpha + \beta$, la igualdad no está demostrada.

## Preguntas de repaso

> [!question]- ¿Por qué hay que restringir el dominio para definir $\arcsin$?
> Porque $\sin$ no es inyectiva en $\mathbb{R}$ (muchos ángulos comparten seno). Restringida a $[-\pi/2, \pi/2]$ sí lo es, y ahí se define su inversa.

> [!question]- ¿Cuánto vale $\arccos(\cos(-\pi/3))$?
> $\cos(-\pi/3) = 1/2$, y $\arccos(1/2) = \pi/3$ (que es el ángulo en $[0,\pi]$ con coseno $1/2$).

> [!question]- Demuestre que $\arcsin x + \arccos x = \pi/2$.
> Sea $\theta = \arcsin x$, con $\sin\theta = x$ y $\theta \in [-\pi/2, \pi/2]$. Entonces $\cos(\pi/2 - \theta) = \sin\theta = x$ y $\pi/2 - \theta \in [0, \pi]$, así que $\arccos x = \pi/2 - \theta$. Sumando, $\arcsin x + \arccos x = \pi/2$.

> [!question]- ¿Cuál es el rango de $\arctan$?
> $(-\pi/2, \pi/2)$, abierto: la tangente tiende a $\pm\infty$ en los extremos y nunca se alcanzan.
