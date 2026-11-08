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

![Gráficos de seno y coseno](adjuntos/Gr%C3%A1ficos%20de%20seno%20y%20coseno.png)

> [!example]- Transcripción de la imagen
> Dos gráficos sobre el intervalo de $-\pi$ a $4\pi$. Arriba, $y = \sin t$: vale $0$ en $t = 0$, sube a $1$ en $\tfrac{\pi}{2}$ y baja a $-1$ en $\tfrac{3\pi}{2}$. Abajo, $y = \cos t$: vale $1$ en $t = 0$. Ambos oscilan entre $-1$ y $1$, y una flecha marca el período $2\pi$ entre dos repeticiones.

## Tangente y recíprocas

> [!tip] Dominios
> - $\tan t = \frac{\sin t}{\cos t}$, con dominio $\mathbb{R}\setminus\{(2n+1)\frac{\pi}{2}\}$ (donde $\cos t = 0$).
> - $\cot t = \frac{\cos t}{\sin t}$, con dominio $\mathbb{R}\setminus\{n\pi\}$ (donde $\sin t = 0$).
> - $\sec t = \frac{1}{\cos t}$ (mismo dominio que la tangente) y $\csc t = \frac{1}{\sin t}$ (mismo que la cotangente).

La tangente tiene asíntotas verticales en los múltiplos impares de $\pi/2$ (donde el coseno se anula), y su gráfica se repite con **período** $\pi$.

![Gráficos de la tangente y la cotangente](adjuntos/Gr%C3%A1ficos%20de%20la%20tangente%20y%20la%20cotangente.png)

> [!example]- Transcripción de la imagen
> Dos gráficos con asíntotas verticales punteadas. (a) $y = \tan x$: crece en cada tramo, pasa por el origen y tiene asíntotas en $x = \pm\tfrac{\pi}{2}, \pm\tfrac{3\pi}{2}$, donde el coseno se anula. (b) $y = \cot x$: decrece en cada tramo y tiene asíntotas en $x = 0, \pm\pi$, donde el seno se anula. En ambas, cada tramo se repite cada $\pi$.

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
