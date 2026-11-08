---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Seno y coseno en la circunferencia unitaria]]"
---

# Gráficas de las funciones trigonométricas

Reuniendo los valores y las propiedades (periodicidad, paridad, recorrido) se obtienen las gráficas de seno y coseno: ondas que se repiten cada $2\pi$. De ellas se derivan la tangente y las recíprocas, cada una con su dominio y sus asíntotas.

## Seno y coseno

Las gráficas de $\sin$ y $\cos$ son la misma onda desplazada: el coseno es el seno corrido $\pi/2$ a la izquierda. Ambas tienen **período** $2\pi$ y recorrido $[-1, 1]$.

![Gráfico de seno y coseno](adjuntos/grafico%20de%20seno%20y%20coseno.png)

> [!example]- Transcripción de la imagen
> Sobre los ejes se dibujan dos ondas de período $2\pi$. La curva del coseno (azul) parte de $1$ en $t = 0$; la del seno (roja) parte de $0$, sube a $1$ en $\pi/2$ y vuelve a $0$ en $\pi$. Ambas oscilan entre $-1$ y $1$ y se repiten cada $2\pi$.

## Tangente y recíprocas

> [!tip] Dominios
> - $\tan t = \frac{\sin t}{\cos t}$, con dominio $\mathbb{R}\setminus\{(2n+1)\frac{\pi}{2}\}$ (donde $\cos t = 0$).
> - $\cot t = \frac{\cos t}{\sin t}$, con dominio $\mathbb{R}\setminus\{n\pi\}$ (donde $\sin t = 0$).
> - $\sec t = \frac{1}{\cos t}$ (mismo dominio que la tangente) y $\csc t = \frac{1}{\sin t}$ (mismo que la cotangente).

La tangente tiene asíntotas verticales en los múltiplos impares de $\pi/2$ (donde el coseno se anula), y su gráfica se repite con **período** $\pi$.

![Gráfico de la tangente](adjuntos/grafico%20de%20la%20tangente.png)

> [!example]- Transcripción de la imagen
> La curva de la tangente (naranja) cruza el origen, crece y se dispara hacia $+\infty$ al acercarse a la asíntota vertical en $\pi/2$ (línea punteada), reaparece desde $-\infty$ al otro lado, y se repite cada $\pi$. Hay asíntotas en $\pi/2$ y $3\pi/2$.

> [!warning] Período de la tangente
> La tangente tiene período $\pi$, no $2\pi$: como $\tan(t + \pi) = \tan t$, su onda se repite el doble de rápido que la del seno.

## Preguntas de repaso

> [!question]- ¿Cuál es la relación entre las gráficas de seno y coseno?
> Son la misma onda desplazada: $\cos t = \sin(t + \pi/2)$, así que el coseno es el seno corrido $\pi/2$ a la izquierda. Ambas tienen período $2\pi$.

> [!question]- ¿Dónde tiene asíntotas la tangente y por qué?
> En $t = (2n+1)\pi/2$, porque allí $\cos t = 0$ y $\tan t = \sin t / \cos t$ no está definida.

> [!question]- ¿Qué período tienen la tangente y la cotangente?
> $\pi$ (la mitad que el seno y el coseno), porque $\tan(t + \pi) = \tan t$.

> [!question]- ¿Por qué $\sec t$ tiene el mismo dominio que $\tan t$?
> Porque ambas dividen por $\cos t$ (la secante es $1/\cos t$), así que ambas fallan exactamente donde $\cos t = 0$.
