---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Identidades de suma y resta]]"
  - "[[05 - Ángulo doble, medio y prostaféresis]]"
---

# Ejercicios de prueba de identidades trigonométricas

Preguntas de interrogaciones anteriores. Hay tres familias: demostrar una identidad (a veces la misma fórmula de suma o de prostaféresis), calcular un valor exacto usando cuadrantes y fórmulas de suma, y problemas geométricos donde una figura obliga a usar la tangente o el coseno de una suma.

## Ejercicios

### 1. Identidades directas
Demuestre: (a) $3\sin^3 x\csc x + \cos^2 x + 2\cos(-x)\cos x = 3$. (b) $(\sin\alpha + \csc\alpha)^2 + (\cos\alpha + \sec\alpha)^2 = \tan^2\alpha + \cot^2\alpha + 7$.

> [!example]- Solución
> (a) Con $\csc x = \frac{1}{\sin x}$ y $\cos(-x) = \cos x$ (coseno par): $3\sin^2 x + \cos^2 x + 2\cos^2 x = 3(\sin^2 x + \cos^2 x) = 3$.
> (b) Expandiendo, $\sin\alpha\csc\alpha = 1$ y $\cos\alpha\sec\alpha = 1$:
> $$\sin^2\alpha + 2 + \csc^2\alpha + \cos^2\alpha + 2 + \sec^2\alpha = 5 + \csc^2\alpha + \sec^2\alpha = 5 + (1 + \cot^2\alpha) + (1 + \tan^2\alpha).$$

### 2. Producto a suma
Demuestre que para todo $\alpha, \beta$: (a) $\sin\beta\cos\alpha = \frac{\sin(\alpha+\beta) - \sin(\alpha-\beta)}{2}$; (b) $\cos\alpha\cos\beta = \frac{\cos(\alpha+\beta) + \cos(\alpha-\beta)}{2}$.

> [!example]- Solución
> (a) $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \sin\beta\cos\alpha$; al restar, $\sin(\alpha+\beta) - \sin(\alpha-\beta) = 2\sin\beta\cos\alpha$.
> (b) $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$; al sumar, $\cos(\alpha+\beta) + \cos(\alpha-\beta) = 2\cos\alpha\cos\beta$.

### 3. Prostaféresis y una ecuación
(a) Demuestre que $\cos a + \cos b = 2\cos\frac{a+b}{2}\cos\frac{a-b}{2}$. (b) Úselo para resolver $1 + \cos x + \cos 2x + \cos 3x = 0$ en $\mathbb{R}$.

> [!example]- Solución
> (a) Es el ejercicio 2(b) con $x = \frac{a+b}{2}$ e $y = \frac{a-b}{2}$, que cumplen $x + y = a$ y $x - y = b$.
> (b) Agrupando $1 = \cos 0$ con $\cos 2x$, y $\cos x$ con $\cos 3x$:
> $$[\cos 0 + \cos 2x] + [\cos x + \cos 3x] = 2\cos^2 x + 2\cos x\cos 2x = 2\cos x(\cos x + \cos 2x) = 4\cos x\cos\tfrac{x}{2}\cos\tfrac{3x}{2}.$$
> Se anula si $\cos x = 0$, $\cos\frac{x}{2} = 0$ o $\cos\frac{3x}{2} = 0$, es decir, $x = (2k+1)\frac{\pi}{2}$, $x = (2k+1)\pi$ o $x = (2k+1)\frac{\pi}{3}$, con $k \in \mathbb{Z}$.

### 4. Seno de una diferencia con cuadrantes
Calcule $\sin(\alpha - \beta)$ si $\alpha$ está en el tercer cuadrante con $\cos\alpha = -\frac{1}{3}$, y $\beta$ en el segundo con $\sin\beta = \frac{2}{\sqrt 5}$.

> [!example]- Solución
> En el tercer cuadrante el seno es negativo: $\sin\alpha = -\sqrt{1 - \frac{1}{9}} = -\frac{2\sqrt 2}{3}$. En el segundo el coseno es negativo: $\cos\beta = -\sqrt{1 - \frac{4}{5}} = -\frac{1}{\sqrt 5}$. Entonces
> $$\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta = \frac{2\sqrt 2}{3\sqrt 5} + \frac{2}{3\sqrt 5} = \frac{2\sqrt 2 + 2}{3\sqrt 5}.$$

### 5. Despejar con la identidad pitagórica
Si $a\cos^2\alpha + b\sin^2\alpha = c$, demuestre que $\tan^2\alpha = \frac{c - a}{b - c}$. Además, calcule $\tan\left(-\frac{5\pi}{3}\right)$.

> [!example]- Solución
> Reemplazando $\cos^2\alpha = 1 - \sin^2\alpha$: $a + (b - a)\sin^2\alpha = c$, así que $\sin^2\alpha = \frac{c-a}{b-a}$. Reemplazando $\sin^2\alpha = 1 - \cos^2\alpha$: $\cos^2\alpha = \frac{c-b}{a-b} = \frac{b-c}{b-a}$. Dividiendo, $\tan^2\alpha = \frac{c-a}{b-c}$.
> Como $-\frac{5\pi}{3} = -2\pi + \frac{\pi}{3}$ y la tangente tiene período $\pi$ (en particular $2\pi$), $\tan\left(-\frac{5\pi}{3}\right) = \tan\frac{\pi}{3} = \sqrt 3$.

### 6. La tangente de un ángulo en una figura
En la figura, el triángulo de la izquierda es equilátero de lado $a$ y el de la derecha es rectángulo con catetos $5$ y $3$. Calcule $\tan\gamma$ y simplifique.

![Figura para calcular la tangente de gamma](adjuntos/Figura%20para%20calcular%20la%20tangente%20de%20gamma.png)

> [!example]- Transcripción de la figura
> Una recta horizontal larga. A la izquierda, un triángulo equilátero de lados $a$ apoyado en ella; su lado derecho se prolonga hacia abajo cruzando la recta. A la derecha, un triángulo rectángulo con catetos $5$ (el inclinado) y $3$, con el ángulo recto arriba; su cateto $5$ se prolonga hacia abajo a la izquierda, cruzando la recta. Las dos prolongaciones se cortan bajo la recta en un vértice con ángulo $\gamma$.

> [!example]- Solución
> ![Ángulos auxiliares para la tangente de gamma](adjuntos/%C3%81ngulos%20auxiliares%20para%20la%20tangente%20de%20gamma.png)
>
> > [!example]- Transcripción de la figura
> > La misma figura con ángulos marcados: $\frac{\pi}{3}$ en los vértices de la base del equilátero y, opuesto por el vértice, $\frac{\pi}{3}$ bajo la recta; $\alpha$ en el cruce del cateto $5$ con la recta, a ambos lados (opuestos por el vértice).
>
> El triángulo de abajo tiene ángulos $\frac{\pi}{3}$, $\alpha$ y $\gamma$, donde $\alpha$ es el ángulo del triángulo rectángulo opuesto al cateto $3$, así que $\tan\alpha = \frac{3}{5}$. Entonces $\gamma = \frac{2\pi}{3} - \alpha$ y
> $$\tan\gamma = \frac{\tan\frac{2\pi}{3} - \tan\alpha}{1 + \tan\frac{2\pi}{3}\tan\alpha} = \frac{-\sqrt 3 - \frac{3}{5}}{1 - \frac{3\sqrt 3}{5}} = \frac{-5\sqrt 3 - 3}{5 - 3\sqrt 3} = \frac{(5\sqrt 3 + 3)(5 + 3\sqrt 3)}{27 - 25} = 30 + 17\sqrt 3.$$

### 7. Una distancia con coseno de una suma
En la figura, $OAC$ es rectángulo en $C$ y $B$ está sobre $AC$. Se conocen $OA = a$, $OB = b$ y el ángulo $\alpha \in \left(0, \frac{\pi}{2}\right)$ entre ellos; se busca $\ell = OC$. (a) Si $\varphi = \angle BOC$, demuestre que $\tan\varphi = \frac{a\cos\alpha - b}{a\sin\alpha}$. (b) Si $x \in \left(0, \frac{\pi}{2}\right)$ y $\tan x = \frac{p}{q}$, demuestre que $\cos x = \frac{|q|}{\sqrt{p^2 + q^2}}$. (c) Deduzca que $\ell = \frac{ab\sin\alpha}{\sqrt{a^2 + b^2 - 2ab\cos\alpha}}$.

![Triángulo rectángulo OAC con B sobre AC](adjuntos/Tri%C3%A1ngulo%20rect%C3%A1ngulo%20OAC%20con%20B%20sobre%20AC.png)

> [!example]- Transcripción de la figura
> Triángulo rectángulo con $O$ abajo a la izquierda, $C$ abajo a la derecha (ángulo recto) y $A$ arriba de $C$. El punto $B$ está sobre $AC$, entre $A$ y $C$. Desde $O$ salen $OA$, rotulado $a$, y $OB$, rotulado $b$; el ángulo entre ellos es $\alpha$.

> [!example]- Solución
> (a) En $OBC$: $\cos\varphi = \frac{\ell}{b}$. En $OAC$ el ángulo en $O$ es $\alpha + \varphi$: $\cos(\alpha + \varphi) = \frac{\ell}{a}$. Igualando $\ell$: $b\cos\varphi = a\cos\alpha\cos\varphi - a\sin\alpha\sin\varphi$, y dividiendo por $a\sin\alpha\cos\varphi$ se despeja $\tan\varphi$.
> (b) $\frac{p^2}{q^2} = \tan^2 x = \frac{1}{\cos^2 x} - 1$, así que $\cos^2 x = \frac{q^2}{p^2 + q^2}$, y como $x$ está en el primer cuadrante, $\cos x > 0$.
> (c) $\ell = b\cos\varphi$ con (b) aplicado a $p = a\cos\alpha - b$, $q = a\sin\alpha > 0$: $p^2 + q^2 = a^2 - 2ab\cos\alpha + b^2$, y sale la fórmula.

## Preguntas de repaso

> [!question]- Al calcular $\sin\alpha$ desde $\cos\alpha$, ¿qué decide el signo de la raíz?
> El cuadrante de $\alpha$: en el tercero y el cuarto el seno es negativo.

> [!question]- En el ejercicio 3, ¿por qué conviene agrupar $1$ con $\cos 2x$?
> Porque $1 = \cos 0$ y así cada par tiene la forma $\cos a + \cos b$; además los dos productos que resultan comparten el factor $\cos x$.

> [!question]- ¿Qué identidad liga $\tan$ con $\cos$ sin pasar por el seno?
> $1 + \tan^2 x = \sec^2 x = \frac{1}{\cos^2 x}$.
