---
ramo: "Introducción al Álgebra"
tema: "Cónicas: parábola, elipse e hipérbola"
tags:
  - intro-algebra/conicas
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - La elipse]]"
  - "[[03 - La hipérbola]]"
---

# Ejercicios de prueba de cónicas

Preguntas de interrogaciones anteriores. Son de dos tipos: pasar de la forma general a la canónica (completando cuadrados) para leer centro, focos y excentricidad, o al revés, construir la ecuación a partir de focos, vértices o ejes. Una tercera variante, la tangencia, se resuelve pidiendo que una ecuación cuadrática tenga discriminante cero.

## Ejercicios

### 1. Una elipse con parámetro
Considere $x^2 + kx + 4y^2 - 16y + 21 = 0$. (a) ¿Para qué $k$ es una elipse? (b) Para $k = 6$, dé el centro, los focos y la excentricidad, y dibújela.

> [!example]- Solución
> (a) Completando cuadrados: $\left(x + \frac{k}{2}\right)^2 + 4(y - 2)^2 = \frac{k^2}{4} - 5$. Es elipse si el lado derecho es positivo: $k^2 > 20$, es decir, $k > \sqrt{20}$ o $k < -\sqrt{20}$.
> (b) Con $k = 6$: $(x + 3)^2 + 4(y - 2)^2 = 4$, o sea $\frac{(x+3)^2}{4} + (y - 2)^2 = 1$. Centro $(-3, 2)$, $a = 2$, $b = 1$, $c = \sqrt{4 - 1} = \sqrt 3$. Focos $(-3 \pm \sqrt 3, 2)$ y excentricidad $e = \frac{\sqrt 3}{2}$.
>
> ![Elipse centrada en -3 2 con sus focos](adjuntos/Elipse%20centrada%20en%20-3%202%20con%20sus%20focos.png)
>
> > [!example]- Transcripción de la figura
> > Plano con cuadrícula, $x$ de $-6$ a $1$ e $y$ de $-1$ a $4$. Elipse horizontal centrada en $(-3, 2)$ que va de $x = -5$ a $x = -1$ y de $y = 1$ a $y = 3$. Los focos $F_1$ y $F_2$ están marcados sobre la recta $y = 2$, cerca de $x \approx -4{,}7$ y $x \approx -1{,}3$.

### 2. Ecuación general desde los datos
Encuentre $A, B, C, D, E$ para que $Ax^2 + By^2 + Cx + Dy + E = 0$ sea: (a) la parábola con vértice $(1, 0)$ y foco $(2, 0)$; (b) la elipse con eje mayor $10$ y focos $(1, 5)$ y $(1, -3)$.

> [!example]- Solución
> (a) Foco a la derecha del vértice, a distancia $p = 1$: parábola horizontal que abre a la derecha, $y^2 = 4p(x - 1) = 4(x - 1)$. Es decir, $y^2 - 4x + 4 = 0$: $A = 0$, $B = 1$, $C = -4$, $D = 0$, $E = 4$.
> (b) Centro en el punto medio de los focos, $(1, 1)$; $c = 4$ (mitad de la distancia $8$), $a = 5$ y $b^2 = 25 - 16 = 9$. Focos alineados verticalmente, así que el eje mayor es vertical: $\frac{(x-1)^2}{9} + \frac{(y-1)^2}{25} = 1$. Multiplicando por $225$ y expandiendo: $25x^2 + 9y^2 - 50x - 18y - 191 = 0$.

### 3. Una hipérbola que intercambia focos y vértices con una elipse
Dada la elipse $4x^2 + y^2 = 1$, encuentre la hipérbola con el mismo centro, cuyos vértices son los focos de la elipse y cuyos focos son los vértices de la elipse.

> [!example]- Solución
> La elipse es $\frac{x^2}{1/4} + y^2 = 1$: vertical, $a = 1$, $b = \frac{1}{2}$, $c = \sqrt{1 - \frac{1}{4}} = \frac{\sqrt 3}{2}$. Focos $\left(0, \pm\frac{\sqrt 3}{2}\right)$ y vértices $(0, \pm 1)$.
> La hipérbola es vertical, $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$, con $a = \frac{\sqrt 3}{2}$ y $c = 1$, así que $b^2 = c^2 - a^2 = \frac{1}{4}$. Ecuación: $\frac{4y^2}{3} - 4x^2 = 1$, o sea $4y^2 - 12x^2 = 3$.

### 4. Tangentes a una hipérbola con pendiente dada
Determine, si existen, las rectas tangentes a $x^2 - \frac{y^2}{4} = 1$ con pendiente $\sqrt 5$.

> [!example]- Solución
> Se busca $b$ tal que $y = \sqrt 5\,x + b$ corte a la hipérbola en un solo punto. Reemplazando y multiplicando por $4$: $4x^2 - (\sqrt 5 x + b)^2 - 4 = 0$, es decir, $-x^2 - 2\sqrt 5\, bx - (b^2 + 4) = 0$. Discriminante cero: $20b^2 - 4(b^2 + 4) = 0$, así que $b^2 = 1$. Tangentes: $y = \sqrt 5\,x + 1$ e $y = \sqrt 5\,x - 1$.

### 5. Dos circunferencias
(a) Determine $F$ para que $x^2 + y^2 - 4x + 5y = F$ sea una circunferencia de radio $2$, y dé su centro. (b) Encuentre la circunferencia de centro $(1, 1)$ tangente a $x + y = 0$.

> [!example]- Solución
> (a) $(x - 2)^2 + \left(y + \frac{5}{2}\right)^2 = F + 4 + \frac{25}{4}$. Radio $2$ exige $F + \frac{41}{4} = 4$, así que $F = -\frac{25}{4}$; centro $\left(2, -\frac{5}{2}\right)$.
> (b) El radio es la distancia del centro a la recta: $\frac{|1 + 1|}{\sqrt 2} = \sqrt 2$. Ecuación: $(x - 1)^2 + (y - 1)^2 = 2$.

## Preguntas de repaso

> [!question]- ¿Cómo se decide si el eje mayor de una elipse es horizontal o vertical?
> Por el denominador mayor en la forma canónica (va con $a^2$), o, si el dato son los focos, por la dirección en que están alineados.

> [!question]- ¿Qué diferencia hay entre la relación de $a, b, c$ en la elipse y en la hipérbola?
> En la elipse $c^2 = a^2 - b^2$ (los focos están dentro, $c < a$); en la hipérbola $c^2 = a^2 + b^2$ (los focos están más lejos que los vértices, $c > a$).

> [!question]- ¿Por qué la condición de tangencia es "discriminante cero"?
> Porque al reemplazar la recta en la cónica queda una cuadrática cuyas raíces son las abscisas de los puntos de corte; tangencia significa un único punto, es decir, una raíz doble.
