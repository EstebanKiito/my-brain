---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/complejos
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Producto, potencias y raíces de complejos]]"
  - "[[03 - Inversas trigonométricas]]"
  - "[[04 - Ecuaciones trigonométricas]]"
---

# Ejercicios de prueba de complejos, inversas y ecuaciones

Preguntas de interrogaciones anteriores. Cada prueba de este tema mezcla una pregunta de inversas o ecuaciones trigonométricas con una de complejos. En las ecuaciones, el método es casi siempre **factorizar** (con ángulo doble o prostaféresis) y resolver cada factor por separado; en complejos, **pasar a forma polar** y usar De Moivre.

## Ejercicios

### 1. Suma de arcotangentes
Demuestre que $\arctan 2 + \arctan 3 = \frac{3\pi}{4}$.

> [!example]- Solución
> Con $\alpha = \arctan 2$, $\beta = \arctan 3$: $\tan(\alpha + \beta) = \frac{2 + 3}{1 - 2 \cdot 3} = -1$. Como $\tan\frac{\pi}{4} = 1 < 2 < 3$, ambos ángulos están en $(\frac{\pi}{4}, \frac{\pi}{2})$ y $\alpha + \beta \in (\frac{\pi}{2}, \pi)$. En ese intervalo la tangente es inyectiva y vale $-1$ solo en $\frac{3\pi}{4}$.

### 2. Ángulo doble de una arcotangente
Demuestre que para $x \in (-1, 1)$, $2\arctan x = \arctan\frac{2x}{1 - x^2}$.

> [!example]- Solución
> Sea $\alpha = \arctan x$. Como $|x| < 1$, $\alpha \in (-\frac{\pi}{4}, \frac{\pi}{4})$ y $2\alpha \in (-\frac{\pi}{2}, \frac{\pi}{2})$, el rango del arcotangente. Además $\tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha} = \frac{2x}{1 - x^2}$. Un ángulo de $(-\frac{\pi}{2}, \frac{\pi}{2})$ con esa tangente es exactamente $\arctan\frac{2x}{1-x^2}$, así que $2\alpha$ lo es.

### 3. Seno del doble de un arcoseno
Calcule $\sin\left(2\arcsin\frac{3}{4}\right)$ y $(1 + i)^3$.

> [!example]- Solución
> Con $\theta = \arcsin\frac{3}{4} \in [-\frac{\pi}{2}, \frac{\pi}{2}]$, el coseno es no negativo: $\cos\theta = \sqrt{1 - \frac{9}{16}} = \frac{\sqrt 7}{4}$. Luego $\sin 2\theta = 2 \cdot \frac{3}{4} \cdot \frac{\sqrt 7}{4} = \frac{3\sqrt 7}{8}$.
> $1 + i = \sqrt 2\operatorname{cis}\frac{\pi}{4}$, así que $(1+i)^3 = 2\sqrt 2\operatorname{cis}\frac{3\pi}{4} = 2\sqrt 2\left(-\frac{\sqrt 2}{2} + \frac{\sqrt 2}{2}i\right) = -2 + 2i$.

### 4. Tres ecuaciones que se factorizan
Resuelva: (a) $\sin x = \sin 3x$ en $[0, 2\pi]$; (b) $\cos x = \sin 2x$ en $\mathbb{R}$; (c) $\sin x\sec^2 x - 2\sin x = 0$ en $\mathbb{R}$.

> [!example]- Solución
> (a) Prostaféresis: $\sin 3x - \sin x = 2\cos 2x\sin x = 0$. $\sin x = 0$ da $0, \pi, 2\pi$; $\cos 2x = 0$ da $2x = \frac{\pi}{2} + k\pi$, o sea $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$.
> (b) $\cos x = 2\sin x\cos x \iff \cos x(1 - 2\sin x) = 0$. $\cos x = 0$: $x = \frac{\pi}{2} + k\pi$. $\sin x = \frac{1}{2}$: $x = \frac{\pi}{6} + 2k\pi$ o $x = \frac{5\pi}{6} + 2k\pi$.
> (c) $\sin x(\sec^2 x - 2) = 0$. $\sin x = 0$: $x = k\pi$. $\sec^2 x = 2 \iff \tan^2 x = 1$: $x = \frac{\pi}{4} + \frac{k\pi}{2}$. En todos los casos $\cos x \neq 0$, así que la secante está definida.

### 5. Potencia y una ecuación cuadrática en $\mathbb{C}$
(a) Determine la parte real e imaginaria de $(\sqrt 3 - i)^{10}$. (b) Resuelva $(z + i)^2 = (\sqrt 3 + i)^3$.

> [!example]- Solución
> (a) $\sqrt 3 - i = 2\operatorname{cis}\left(-\frac{\pi}{6}\right)$, así que $(\sqrt 3 - i)^{10} = 2^{10}\operatorname{cis}\left(-\frac{10\pi}{6}\right) = 1024\operatorname{cis}\frac{\pi}{3} = 512 + 512\sqrt 3\, i$. Parte real $512$, imaginaria $512\sqrt 3$.
> (b) $\sqrt 3 + i = 2\operatorname{cis}\frac{\pi}{6}$, así que el lado derecho es $8\operatorname{cis}\frac{\pi}{2} = 8i$. Las raíces cuadradas de $8i$ son $2\sqrt 2\operatorname{cis}\frac{\pi}{4} = 2 + 2i$ y $2\sqrt 2\operatorname{cis}\frac{5\pi}{4} = -2 - 2i$. Entonces $z = 2 + i$ o $z = -2 - 3i$.

### 6. Raíces cúbicas de la unidad
(a) Encuentre las raíces cúbicas de $1$ y un polinomio cuadrático real que tenga dos de ellas como raíces. (b) Si $w \neq 1$ es raíz cúbica de la unidad, calcule $w^2 + w^{-2}$.

> [!example]- Solución
> (a) $\operatorname{cis}\frac{2k\pi}{3}$: $1$, $-\frac{1}{2} + \frac{\sqrt 3}{2}i$, $-\frac{1}{2} - \frac{\sqrt 3}{2}i$. Las dos no reales suman $-1$ y su producto es $1$: el polinomio es $x^2 + x + 1$.
> (b) Con $w = \operatorname{cis}\frac{2k\pi}{3}$ ($k = 1, 2$): $w^2 + w^{-2} = \operatorname{cis}\frac{4k\pi}{3} + \operatorname{cis}\left(-\frac{4k\pi}{3}\right) = 2\cos\frac{4k\pi}{3} = -1$ en ambos casos.

### 7. Una ecuación con el conjugado
Con $z = r\operatorname{cis}\theta$, encuentre todas las soluciones ($r > 0$, $\theta \in [0, 2\pi)$) de $\frac{z^5 + \overline{z}^{\,5}}{2} = -32$.

> [!example]- Solución
> $\overline{z} = r\operatorname{cis}(-\theta)$, así que $z^5 + \overline{z}^{\,5} = r^5[\operatorname{cis}5\theta + \operatorname{cis}(-5\theta)] = 2r^5\cos 5\theta$. La ecuación es $r^5\cos 5\theta = -32$.
> - Con $r = 2$ hace falta $\cos 5\theta = -1$: $5\theta = \pi + 2k\pi$, y en $[0, 2\pi)$, $\theta = \frac{\pi}{5}, \frac{3\pi}{5}, \pi, \frac{7\pi}{5}, \frac{9\pi}{5}$. Es la respuesta de la pauta.
> - Pero $\cos 5\theta = -\frac{32}{r^5}$ también tiene solución para cualquier $r > 2$ (el lado derecho queda en $(-1, 0)$), y no tiene ninguna para $r < 2$. El conjunto completo es entonces $\{r\operatorname{cis}\theta : r \ge 2,\ \cos 5\theta = -32/r^5\}$, una familia infinita; las cinco de arriba son las de módulo mínimo.

### 8. Condiciones sobre $z$
(a) Si $|z + 1| = |z - 1|$, demuestre que $\operatorname{Re}(z) = 0$. (b) Si $z \neq 0$ y $\frac{z}{\overline{z}} \in \mathbb{R}$, demuestre que $z$ es real o imaginario puro.

> [!example]- Solución
> (a) Con $z = a + bi$: $(a+1)^2 + b^2 = (a-1)^2 + b^2 \iff 4a = 0$.
> (b) $\frac{z}{\overline{z}} = \frac{z^2}{|z|^2} = \frac{a^2 - b^2 + 2abi}{a^2 + b^2}$. Es real si y solo si $ab = 0$: $b = 0$ (real) o $a = 0$ (imaginario puro).

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 2 se exige $|x| < 1$?
> Para que $2\arctan x$ caiga en $(-\frac{\pi}{2}, \frac{\pi}{2})$, el rango del arcotangente. Si $|x| > 1$, $2\arctan x$ sale de ese rango y la igualdad falla por $\pm\pi$.

> [!question]- Al resolver $\cos x = \sin 2x$, ¿qué error típico hace perder soluciones?
> Dividir por $\cos x$: se pierden todas las soluciones con $\cos x = 0$. Hay que factorizar.

> [!question]- ¿Cuántas soluciones tiene $(z + i)^2 = 8i$ y por qué?
> Dos: $z + i$ es una raíz cuadrada de $8i$, y todo complejo no nulo tiene exactamente dos.
