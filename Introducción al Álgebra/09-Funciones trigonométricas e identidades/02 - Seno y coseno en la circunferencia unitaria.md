---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[01 - Ángulos y radianes]]"
---

# Seno y coseno en la circunferencia unitaria

Con los ángulos medidos en radianes, el seno y el coseno se definen como las coordenadas de un punto en la circunferencia unitaria. Esta definición extiende las razones del triángulo rectángulo a **cualquier** número real, no solo a ángulos agudos.

## La definición

Sea $t$ un número real y $P(x, y)$ el punto sobre la circunferencia unitaria determinado por el ángulo de $t$ radianes (medido desde $A = (1,0)$). Entonces

$$
\sin(t) = y, \qquad \cos(t) = x.
$$

![Punto P de la circunferencia unitaria determinado por t](adjuntos/Punto%20P%20de%20la%20circunferencia%20unitaria%20determinado%20por%20t.png)

> [!example]- Transcripción de la figura
> Circunferencia de radio $1$ centrada en el origen $O$, con ejes $x$ e $y$. Desde $A = (1, 0)$ sale un arco rojo en sentido antihorario hasta el punto $P(x, y)$, en el primer cuadrante. Un segmento discontinuo une $O$ con $P$ y forma con el eje $x$ el ángulo $t$, cuya medida en radianes es la longitud del arco $AP$.

Es decir, el coseno es la abscisa y el seno la ordenada del punto $P$.

## Propiedades fundamentales

> [!tip] Propiedades de seno y coseno
> 1. **Periodicidad:** $\sin(t + 2\pi k) = \sin t$ y $\cos(t + 2\pi k) = \cos t$ para todo entero $k$.
> 2. **Paridad:** $\cos(-t) = \cos t$ (par) y $\sin(-t) = -\sin t$ (impar).
> 3. **Identidad fundamental:** $\cos^2 t + \sin^2 t = 1$ (porque $P$ está en $x^2 + y^2 = 1$).
> 4. **Recorrido:** ambos toman valores en $[-1, 1]$.

**Ejemplo.** Calcule $\cos(2\pi/3)$, $\sin(19\pi/4)$ y $\cos(7\pi/4)$.

- $\cos(2\pi/3) = -\cos(\pi/3) = -\tfrac12$ (el ángulo $\tfrac{2\pi}{3}$ está en el segundo cuadrante).
- $\sin(19\pi/4) = \sin(19\pi/4 - 4\pi) = \sin(3\pi/4) = \tfrac{\sqrt2}{2}$ (restando períodos).
- $\cos(7\pi/4) = \cos(-\pi/4) = \cos(\pi/4) = \tfrac{\sqrt2}{2}$ (por paridad).

> [!warning] El signo depende del cuadrante
> En el segundo cuadrante el coseno es negativo y el seno positivo; en el tercero ambos negativos; en el cuarto coseno positivo y seno negativo. La circunferencia unitaria da los signos de un vistazo.

## Preguntas de repaso

> [!question]- ¿Qué son $\sin t$ y $\cos t$ en la circunferencia unitaria?
> La ordenada $y$ y la abscisa $x$ del punto $P$ de la circunferencia unitaria que determina el ángulo de $t$ radianes.

> [!question]- ¿Por qué $\cos$ es par y $\sin$ es impar?
> Porque reflejar el ángulo ($t \to -t$) mantiene la abscisa pero invierte la ordenada: $P(-t) = (\cos t, -\sin t)$.

> [!question]- ¿Cuál es el recorrido de seno y coseno, y por qué?
> $[-1, 1]$. Porque $P$ está sobre la circunferencia unitaria, así que sus coordenadas $x$ e $y$ están entre $-1$ y $1$.

> [!question]- Calcule $\sin(-\pi/2)$.
> $-\sin(\pi/2) = -1$ (el seno es impar).
