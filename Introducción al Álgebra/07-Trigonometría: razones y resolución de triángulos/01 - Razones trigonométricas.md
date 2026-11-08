---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Contraejemplos]]"
---

# Razones trigonométricas

En un triángulo rectángulo, las **razones trigonométricas** relacionan cada ángulo agudo con los cocientes entre sus lados. Como dependen solo del ángulo (y no del tamaño del triángulo), permiten "traducir" ángulos a longitudes y viceversa.

## Las seis razones

Dado un triángulo rectángulo con ángulo agudo $\alpha$, cateto opuesto $a$, cateto adyacente $b$ e hipotenusa $c$:

$$
\sin(\alpha) = \frac{a}{c}, \qquad \cos(\alpha) = \frac{b}{c}, \qquad \tan(\alpha) = \frac{a}{b},
$$

$$
\csc(\alpha) = \frac{c}{a}, \qquad \sec(\alpha) = \frac{c}{b}, \qquad \cot(\alpha) = \frac{b}{a}.
$$

![Triángulo rectángulo de razones trigonométricas](adjuntos/triangulo%20rectangulo%20de%20razones%20trigonometricas.png)

> [!example]- Transcripción de la imagen
> Un triángulo rectángulo con el ángulo agudo $\alpha$ en el vértice inferior izquierdo. El cateto horizontal (adyacente a $\alpha$) mide $b$, el cateto vertical (opuesto a $\alpha$) mide $a$ y la hipotenusa mide $c$. El ángulo recto está en el vértice inferior derecho.

Las tres últimas son las recíprocas de las tres primeras.

## Identidades fundamentales

> [!tip] Identidades básicas
> $\csc\alpha = \frac{1}{\sin\alpha}$, $\sec\alpha = \frac{1}{\cos\alpha}$, $\cot\alpha = \frac{1}{\tan\alpha}$, y $\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$.

Además, del teorema de Pitágoras $a^2 + b^2 = c^2$ se obtiene la identidad central:

$$
\sin^2\alpha + \cos^2\alpha = 1,
$$

porque $\sin^2\alpha + \cos^2\alpha = (a/c)^2 + (b/c)^2 = (a^2 + b^2)/c^2 = 1$. Dividiéndola por $\cos^2\alpha$ o por $\sin^2\alpha$ se llega a

$$
\tan^2\alpha + 1 = \sec^2\alpha, \qquad \cot^2\alpha + 1 = \csc^2\alpha.
$$

**Ejemplo.** Si en un triángulo rectángulo $\tan(\alpha) = \frac{3}{\sqrt5}$ y $c = \sqrt{70}$, halle el cateto $a$.

De $\tan\alpha = a/b = 3/\sqrt5$ sale $b = a\sqrt5/3$. Con $a^2 + b^2 = 70$: $a^2 + 5a^2/9 = 70$, o sea $14a^2/9 = 70$, luego $a^2 = 45$ y $a = 3\sqrt5$.

> [!warning] Opuesto vs. adyacente
> $\sin$ usa el cateto **opuesto** al ángulo y $\cos$ el **adyacente**. Son distintos para un ángulo dado y coinciden solo en $\alpha = 45^\circ$.

## Preguntas de repaso

> [!question]- En el triángulo de la definición, ¿qué cateto usa $\sin\alpha$ y cuál usa $\cos\alpha$?
> $\sin\alpha$ usa el cateto opuesto $a$; $\cos\alpha$ usa el cateto adyacente $b$. Ambos se dividen por la hipotenusa $c$.

> [!question]- ¿Cómo se deduce $\sin^2\alpha + \cos^2\alpha = 1$?
> Escribiendo $\sin^2 + \cos^2 = (a/c)^2 + (b/c)^2 = (a^2 + b^2)/c^2$, y usando Pitágoras $a^2 + b^2 = c^2$.

> [!question]- ¿Qué relación hay entre $\sec\alpha$ y $\cos\alpha$?
> Son recíprocas: $\sec\alpha = 1/\cos\alpha$. Lo mismo pasa con $\csc$ y $\sin$, y con $\cot$ y $\tan$.

> [!question]- Si $\sin\alpha = 3/5$ y $\alpha$ es agudo, halle $\cos\alpha$.
> De $\sin^2 + \cos^2 = 1$: $\cos^2\alpha = 1 - 9/25 = 16/25$, así que $\cos\alpha = 4/5$ (positivo por ser agudo).
