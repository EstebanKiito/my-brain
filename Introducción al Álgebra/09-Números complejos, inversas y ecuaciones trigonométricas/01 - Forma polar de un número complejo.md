---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/complejos
  - origen/complemento
prerrequisitos:
  - "[[02 - Seno y coseno en la circunferencia unitaria]]"
---

# Forma polar de un número complejo

Todo número complejo $z = a + bi$ se puede ver como un punto $(a, b)$ del plano. La **forma polar** lo describe en cambio por su distancia al origen (el módulo) y el ángulo que forma con el eje real (el argumento). Esa forma vuelve trivial multiplicar y potenciar.

## Módulo y argumento

La función $\varphi(z) = (\mathrm{Re}\,z, \mathrm{Im}\,z)$ identifica $\mathbb{C}$ con el plano. En forma polar,

$$
z = r(\cos\theta + i\sin\theta), \qquad r = |z| = \sqrt{a^2 + b^2}, \qquad \tan\theta = \frac{b}{a}.
$$

$r$ es el **módulo** y $\theta$ el **argumento**. Se abrevia $\cos\theta + i\sin\theta$ como $\operatorname{cis}(\theta)$.

![Gráfico polar de dos números complejos](adjuntos/Gr%C3%A1fico%20polar%20de%20dos%20n%C3%BAmeros%20complejos.png)

> [!example]- Transcripción de la imagen
> Dos planos complejos con eje real ($Re$) e imaginario ($Im$). (a) El punto $z_1 = 1 + i$, unido al origen por un segmento de largo $|z_1| = \sqrt2$, con el ángulo $\tfrac{\pi}{4}$ marcado desde el eje real. (b) El punto $z_2 = -1 + \sqrt3\,i$, en el segundo cuadrante, con módulo $2$ y el ángulo $\tfrac{2\pi}{3}$ marcado desde el eje real positivo: el argumento se mide siempre desde ahí, aunque el punto esté a la izquierda.

## El argumento según el cuadrante

Como $\tan^{-1}(b/a)$ devuelve valores en $(-\pi/2, \pi/2)$, su valor no sirve en el segundo ni tercer cuadrante. El argumento se ajusta así:

$$
\theta = \begin{cases}
\tan^{-1}(b/a), & (a,b) \text{ en cuadrante I o IV},\\
\tan^{-1}(b/a) + \pi, & (a,b) \text{ en cuadrante II o III},\\
\pi/2, & a = 0,\ b > 0,\\
-\pi/2, & a = 0,\ b < 0.
\end{cases}
$$

**Ejemplos.** $1 + i = \sqrt2\operatorname{cis}(\pi/4)$; $-1 + \sqrt3\,i = 2\operatorname{cis}(2\pi/3)$; $-4\sqrt3 - 4i = 8\operatorname{cis}(7\pi/6)$.

> [!warning] El argumento no es solo $\tan^{-1}(b/a)$
> $\tan^{-1}$ da un ángulo en $(-\pi/2,\pi/2)$, que deja fuera el segundo y tercer cuadrante. Hay que sumar $\pi$ cuando el punto está a la izquierda del eje imaginario.

## Preguntas de repaso

> [!question]- ¿Qué son el módulo y el argumento de $z = a + bi$?
> El módulo es $r = \sqrt{a^2 + b^2}$ (distancia al origen) y el argumento $\theta$ es el ángulo entre $z$ y el eje real positivo, dado por $\tan\theta = b/a$ (con el cuadrante correcto).

> [!question]- Escriba $z = 1 + i$ en forma polar.
> $r = \sqrt{1 + 1} = \sqrt2$ y $\theta = \tan^{-1}(1) = \pi/4$, así que $1 + i = \sqrt2\operatorname{cis}(\pi/4)$.

> [!question]- ¿Por qué hay que ajustar el argumento en el segundo cuadrante?
> Porque $\tan^{-1}$ devuelve ángulos en $(-\pi/2, \pi/2)$, siempre en el primer o cuarto cuadrante. En el segundo o tercero se suma $\pi$.

> [!question]- ¿Qué es $\operatorname{cis}(\theta)$?
> Una abreviatura de $\cos\theta + i\sin\theta$, muy usada para escribir la forma polar de forma compacta.
