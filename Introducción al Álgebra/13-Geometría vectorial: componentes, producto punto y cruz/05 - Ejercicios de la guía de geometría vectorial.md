---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto punto y ángulo entre vectores]]"
  - "[[04 - Producto cruz, paralelismo y área]]"
---

# Ejercicios de la guía de geometría vectorial

Preguntas de la guía y de las clases sobre componentes, producto punto y producto cruz. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Vectores ortogonales
Demuestre que $\mathbf v = (2, 6, -2)$ y $\mathbf w = (5, -3, -4)$ son ortogonales.

> [!example]- Solución
> $\mathbf v \cdot \mathbf w = 2\cdot 5 + 6\cdot(-3) + (-2)\cdot(-4) = 10 - 18 + 8 = 0$. Como el producto punto es cero, son ortogonales.

### 2. Distancia y punto medio
Calcule la distancia entre $(2, -3, 5)$ y $(-2, 5, -4)$, y el punto medio del segmento.

> [!example]- Solución
> La distancia es $\sqrt{(-4)^2 + 8^2 + (-9)^2} = \sqrt{16 + 64 + 81} = \sqrt{161}$. El punto medio es $\left(\frac{2-2}{2}, \frac{-3+5}{2}, \frac{5-4}{2}\right) = (0, 1, \tfrac12)$.

### 3. Producto punto con el ángulo
Si $\mathbf a$ y $\mathbf b$ tienen longitudes $4$ y $6$ y el ángulo entre ellos es $\pi/3$, calcule $\mathbf a \cdot \mathbf b$.

> [!example]- Solución
> $\mathbf a \cdot \mathbf b = \|\mathbf a\|\,\|\mathbf b\|\cos(\pi/3) = 4 \cdot 6 \cdot \tfrac12 = 12$.

### 4. Ángulo entre vectores
Determine el ángulo entre $\mathbf a = (2, 2, -1)$ y $\mathbf b = (5, -3, 2)$.

> [!example]- Solución
> $\mathbf a \cdot \mathbf b = 10 - 6 - 2 = 2$, $\|\mathbf a\| = 3$ y $\|\mathbf b\| = \sqrt{25 + 9 + 4} = \sqrt{38}$. Entonces $\cos\theta = \frac{2}{3\sqrt{38}}$, y $\theta = \arccos\!\left(\frac{2}{3\sqrt{38}}\right) \approx 83.8^\circ$.

### 5. Vector perpendicular y área
Encuentre un vector perpendicular al plano por $P(1, 4, 6)$, $Q(-2, 5, -1)$ y $R(1, -1, 1)$, y el área del triángulo.

> [!example]- Solución
> $\overrightarrow{PQ} = (-3, 1, -7)$ y $\overrightarrow{PR} = (0, -5, -5)$. Su producto cruz es
> $$\overrightarrow{PQ} \times \overrightarrow{PR} = (1(-5) - (-7)(-5),\ (-7)(0) - (-3)(-5),\ (-3)(-5) - 1(0)) = (-40, -15, 15).$$
> Este vector (o $(-8, -3, 3)$) es perpendicular al plano. El área del triángulo es $\tfrac12\|\overrightarrow{PQ} \times \overrightarrow{PR}\| = \tfrac12\sqrt{1600 + 225 + 225} = \tfrac12\sqrt{2050} = \tfrac{5\sqrt{82}}{2}$.

## Preguntas de repaso

> [!question]- ¿Qué condición algebraica expresa ortogonalidad?
> $\mathbf a \cdot \mathbf b = 0$. Es la forma de comprobar perpendicularidad sin dibujar.

> [!question]- ¿Cómo se obtiene un vector perpendicular a otros dos?
> Con el producto cruz: $\mathbf a \times \mathbf b$ es perpendicular a ambos, y su magnitud es el área del paralelogramo.

> [!question]- En el ejercicio 5, ¿por qué el área del triángulo es la mitad del producto cruz?
> Porque $\|\mathbf a \times \mathbf b\|$ es el área del paralelogramo; el triángulo es exactamente la mitad de ese paralelogramo.
