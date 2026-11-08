---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[03 - Gráficas de las funciones trigonométricas]]"
---

# Identidades de suma y resta

La identidad central del tema es la del **coseno de una diferencia**; de ella se deducen todas las fórmulas de suma y resta de seno, coseno y tangente. Sirven para calcular valores exactos y simplificar expresiones.

## Coseno de una diferencia

> [!tip] Fórmula central
> $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$.

Se demuestra colocando en la circunferencia unitaria los puntos $P = (\cos\beta, \sin\beta)$, $Q = (\cos(\alpha-\beta), \sin(\alpha-\beta))$ y $R = (\cos\alpha, \sin\alpha)$: los ángulos $\angle AOQ$ y $\angle POR$ son iguales, así que subtienden cuerdas iguales, $d(A, Q) = d(P, R)$. Elevando al cuadrado ambas distancias e igualando se despeja la fórmula.

## Suma y resta de seno y coseno

Sustituyendo $\beta$ por $-\beta$ y usando $\cos(-\beta) = \cos\beta$, $\sin(-\beta) = -\sin\beta$:

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta, \qquad
\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta,
$$

$$
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta.
$$

## Tangente de suma y resta

$$
\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}, \qquad
\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}.
$$

> [!warning] El signo cambia
> En $\cos(\alpha + \beta)$ el término del producto de senos lleva **menos**; en $\cos(\alpha - \beta)$ lleva **más**. En la tangente, el signo del numerador y del denominador van cruzados.

## Preguntas de repaso

> [!question]- Escriba $\sin(\alpha + \beta)$.
> $\sin\alpha\cos\beta + \cos\alpha\sin\beta$: "seno por coseno más coseno por seno".

> [!question]- ¿Cómo se obtiene $\cos(\alpha + \beta)$ a partir de $\cos(\alpha - \beta)$?
> Escribiendo $\alpha + \beta = \alpha - (-\beta)$ y usando la paridad: $\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$.

> [!question]- Calcule $\cos(75^\circ)$ usando $\cos(45^\circ + 30^\circ)$.
> $\cos45^\circ\cos30^\circ - \sin45^\circ\sin30^\circ = \tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2} - \tfrac{\sqrt2}{2}\cdot\tfrac12 = \tfrac{\sqrt6 - \sqrt2}{4}$.

> [!question]- ¿Cuál es el denominador de $\tan(\alpha + \beta)$ y qué significa que se anule?
> $1 - \tan\alpha\tan\beta$. Si se anula, la tangente de la suma no está definida, lo que ocurre cuando $\alpha + \beta = \pi/2 + k\pi$.
