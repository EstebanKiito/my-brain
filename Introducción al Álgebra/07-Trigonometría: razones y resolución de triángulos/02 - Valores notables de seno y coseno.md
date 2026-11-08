---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[01 - Razones trigonométricas]]"
---

# Valores notables de seno y coseno

Para los ángulos de $30^\circ$, $45^\circ$ y $60^\circ$ los valores de seno y coseno se deducen de dos triángulos conocidos y se memorizan en una tabla. Son los valores que más aparecen en ejercicios y evaluaciones.

## Deducción con un triángulo equilátero

Tomando un triángulo equilátero de lado $2$ y trazando su altura, queda dividido en dos triángulos rectángulos $30^\circ$-$60^\circ$-$90^\circ$. Sus lados son: hipotenusa $2$, cateto menor $1$ (opuesto a $30^\circ$) y cateto mayor $\sqrt{3}$ (opuesto a $60^\circ$).

![Triángulos para los ángulos de 30, 45 y 60 grados](adjuntos/Tri%C3%A1ngulos%20para%20los%20%C3%A1ngulos%20de%2030,%2045%20y%2060%20grados.png)

> [!example]- Transcripción de la imagen
> Izquierda: un cuadrado de lado $1$ cortado por su diagonal, que mide $\sqrt2$; cada mitad es un triángulo rectángulo isósceles con dos ángulos de $45^\circ$. Derecha: un triángulo equilátero de lado $2$ con la altura $BD$ trazada; la mitad izquierda $ABD$ tiene hipotenusa $AB = 2$, cateto $AD = 1$ (junto al ángulo de $60^\circ$ en $A$) y altura $BD = \sqrt3$ (junto al ángulo de $30^\circ$ en $B$).

De ahí salen $\sin 60^\circ = \sqrt3/2$, $\cos 60^\circ = 1/2$, y por simetría $\sin 30^\circ = 1/2$, $\cos 30^\circ = \sqrt3/2$. Para $45^\circ$ se usa un triángulo rectángulo isósceles de catetos $1$ e hipotenusa $\sqrt2$.

## Tabla de valores

| $\alpha$ | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|---|---|---|---|---|
| $\sin\alpha$ | $0$ | $\tfrac12$ | $\tfrac{\sqrt2}{2}$ | $\tfrac{\sqrt3}{2}$ | $1$ |
| $\cos\alpha$ | $1$ | $\tfrac{\sqrt3}{2}$ | $\tfrac{\sqrt2}{2}$ | $\tfrac12$ | $0$ |
| $\tan\alpha$ | $0$ | $\tfrac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | no definida |

> [!tip] Cómo recordarla
> La fila del seno es $0, \frac12, \frac{\sqrt2}{2}, \frac{\sqrt3}{2}, 1$ (crece de $0$ a $1$), y la del coseno es la misma leída al revés. La tangente es seno entre coseno.

> [!warning] El seno no es lineal
> $\sin(\alpha + \beta) \neq \sin\alpha + \sin\beta$. Por ejemplo, $\sin(30^\circ + 30^\circ) = \sin 60^\circ = \sqrt3/2$, pero $\sin30^\circ + \sin30^\circ = 1$. No se "distribuye".

## Preguntas de repaso

> [!question]- ¿De qué triángulo se deducen los valores de $30^\circ$ y $60^\circ$?
> De un triángulo equilátero de lado $2$ partido por su altura, que da un triángulo $30^\circ$-$60^\circ$-$90^\circ$ con catetos $1$ y $\sqrt3$ e hipotenusa $2$.

> [!question]- ¿Cuánto valen $\sin 45^\circ$ y $\cos 45^\circ$?
> Ambos $\tfrac{\sqrt2}{2}$, porque el triángulo rectángulo isósceles tiene los dos catetos iguales.

> [!question]- ¿Por qué $\tan 90^\circ$ no está definida?
> Porque $\tan\alpha = \sin\alpha/\cos\alpha$ y $\cos 90^\circ = 0$; no se puede dividir por cero.

> [!question]- ¿Cuánto vale $\sin^2 30^\circ + \cos^2 30^\circ$?
> $1$, por la identidad fundamental $\sin^2\alpha + \cos^2\alpha = 1$, que vale para cualquier ángulo.
