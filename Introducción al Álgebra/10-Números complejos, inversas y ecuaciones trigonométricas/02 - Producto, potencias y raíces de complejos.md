---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/complejos
  - origen/complemento
prerrequisitos:
  - "[[01 - Forma polar de un número complejo]]"
---

# Producto, potencias y raíces de complejos

En forma polar, multiplicar complejos es sumar ángulos y multiplicar módulos. De ahí salen el **teorema de Moivre** (para potencias) y la fórmula de las **raíces n-ésimas**, que reparte las raíces de forma simétrica en el plano.

## Producto en forma polar

> [!tip] Producto y potencia
> Si $z_1 = r_1\operatorname{cis}(\theta_1)$ y $z_2 = r_2\operatorname{cis}(\theta_2)$, entonces
> $$z_1 z_2 = r_1 r_2 \operatorname{cis}(\theta_1 + \theta_2).$$
> Repitiendo, $z^n = r^n\operatorname{cis}(n\theta)$ (teorema de Moivre: $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$).

**Ejemplo.** Calcule $(1 + i)^{10}$. Como $1 + i = \sqrt2\operatorname{cis}(\pi/4)$,

$$
(1+i)^{10} = (\sqrt2)^{10}\operatorname{cis}(10\cdot\tfrac{\pi}{4}) = 32\operatorname{cis}(\tfrac{5\pi}{2}) = 32\operatorname{cis}(\tfrac{\pi}{2}) = 32i.
$$

## Raíces n-ésimas

> [!tip] Raíces n-ésimas
> Si $\omega = r\operatorname{cis}(\theta)$, entonces $\omega$ tiene exactamente $n$ raíces n-ésimas:
> $$z_k = \sqrt[n]{r}\,\operatorname{cis}\!\left(\frac{\theta + 2k\pi}{n}\right), \qquad k = 0, 1, \dots, n-1.$$

**Ejemplo.** Resuelva $z^3 + 27 = 0$, es decir, $z^3 = -27 = 27\operatorname{cis}(\pi)$.

$$
z_k = 3\operatorname{cis}\!\left(\frac{\pi + 2k\pi}{3}\right), \quad k = 0,1,2,
$$

que dan $z_0 = 3\operatorname{cis}(\pi/3) = \tfrac32 + \tfrac{3\sqrt3}{2}i$, $z_1 = 3\operatorname{cis}(\pi) = -3$ y $z_2 = 3\operatorname{cis}(5\pi/3) = \tfrac32 - \tfrac{3\sqrt3}{2}i$.

> [!warning] Hay $n$ raíces, no una
> En $\mathbb{C}$ la ecuación $z^n = \omega$ tiene $n$ soluciones (para $\omega \neq 0$), repartidas simétricamente: todas con el mismo módulo $\sqrt[n]{r}$ y ángulos separados $2\pi/n$.

## Raíces de la unidad

Las soluciones de $z^n = 1$ son $\omega_k = \operatorname{cis}\frac{2k\pi}{n}$, $k = 0, \dots, n-1$. Para $n = 3$: $1$ y $-\frac{1}{2} \pm \frac{\sqrt 3}{2}i$. Las dos no reales son conjugadas, así que son raíces de un polinomio real: $(x - \omega_1)(x - \omega_2) = x^2 + x + 1$ (de hecho $z^3 - 1 = (z - 1)(z^2 + z + 1)$).

## Conjugado y módulo

Con $z = a + bi$ y $\overline{z} = a - bi$:
- $z\,\overline{z} = |z|^2$, $z + \overline{z} = 2\operatorname{Re}(z)$ y $\overline{z^n} = \overline{z}^{\,n}$.
- En forma polar, $\overline{r\operatorname{cis}\theta} = r\operatorname{cis}(-\theta)$, así que $z^n + \overline{z}^{\,n} = 2r^n\cos(n\theta)$.
- Para dividir, se amplifica por el conjugado del denominador: $\frac{z}{\overline{z}} = \frac{z^2}{|z|^2}$.

Las condiciones sobre módulos se resuelven elevando al cuadrado: $|z + 1| = |z - 1|$ da $(a+1)^2 + b^2 = (a-1)^2 + b^2$, es decir, $a = 0$ (los puntos equidistantes de $1$ y $-1$ forman el eje imaginario).

## Preguntas de repaso

> [!question]- ¿Qué le hace el producto en forma polar a los módulos y a los ángulos?
> Multiplica los módulos y suma los ángulos: $z_1 z_2 = r_1 r_2 \operatorname{cis}(\theta_1 + \theta_2)$.

> [!question]- Enuncie el teorema de Moivre.
> $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$ para todo $n \in \mathbb{N}$: la potencia eleva el ángulo.

> [!question]- ¿Cuántas raíces cúbicas tiene un complejo no nulo y dónde están?
> Tres. Tienen el mismo módulo (la raíz cúbica del módulo) y sus ángulos difieren en $2\pi/3$, formando un triángulo equilátero centrado en el origen.

> [!question]- Calcule las raíces cúbicas de $1$.
> $1 = \operatorname{cis}(0)$, así que $z_k = \operatorname{cis}(2k\pi/3)$ con $k = 0,1,2$: $1$, $-\tfrac12 + \tfrac{\sqrt3}{2}i$ y $-\tfrac12 - \tfrac{\sqrt3}{2}i$.
