---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - La circunferencia]]"
  - "[[03 - Tangentes a una circunferencia]]"
---

# Ejercicios de prueba de geometría analítica

Preguntas de la guía sobre distancias, circunferencias y tangentes. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Distancia de un punto a una recta
Halle la distancia del punto de intersección de $x - y - 1 = 0$ y $x - 2y + 1 = 0$ a la recta $5x + 12y - 13 = 0$.

> [!example]- Solución
> Resolviendo el sistema, el punto es $(3, 2)$. La distancia es $\frac{|5\cdot 3 + 12\cdot 2 - 13|}{\sqrt{25 + 144}} = \frac{26}{13} = 2$.

### 2. Circunferencia por un diámetro
Halle la ecuación de la circunferencia cuyos extremos de un diámetro son $A(-4, 6)$ y $B(2, 0)$.

> [!example]- Solución
> El centro es el punto medio $(-1, 3)$. El radio es la mitad de $d(A,B) = \sqrt{(-6)^2 + 6^2} = 6\sqrt2$, o sea $3\sqrt2$. La ecuación es $(x + 1)^2 + (y - 3)^2 = 18$.

### 3. Determinar la gráfica
Determine qué representa $5x^2 + 5y^2 - 14x + 7y - 24 = 0$.

> [!example]- Solución
> Dividiendo por $5$ y completando cuadrados: $(x - \tfrac75)^2 + (y + \tfrac7{10})^2 = \tfrac{29}{4}$. Es una circunferencia de centro $(\tfrac75, -\tfrac7{10})$ y radio $\tfrac{\sqrt{29}}{2}$.

### 4. Tangentes desde un punto exterior
Halle las tangentes trazadas desde $(1, -1)$ a $x^2 + y^2 + 2x - 6y - 6 = 0$.

> [!example]- Solución
> La familia por el punto es $y + 1 = m(x - 1)$. Sustituyendo en la circunferencia, exigir tangencia (discriminante cero) da $3m^2 - 4m = 0$, con $m = 0$ y $m = \tfrac43$. Las tangentes son $y = -1$ y $y + 1 = \tfrac43(x - 1)$.

### 5. Distancia entre rectas paralelas
Halle la distancia entre $2x - 3y = 3$ y $-4x + 6y = 3$.

> [!example]- Solución
> Reescribiendo: $2x - 3y - 3 = 0$ y $2x - 3y + \tfrac32 = 0$ (multiplicando la segunda por $-\tfrac12$). Son paralelas, y la distancia es $\frac{|-3 - \tfrac32|}{\sqrt{4 + 9}} = \frac{9/2}{\sqrt{13}} = \frac{9}{2\sqrt{13}}$.

## Preguntas de repaso

> [!question]- ¿Cómo se halla la distancia entre dos rectas paralelas?
> Se toma un punto de una de ellas y se calcula su distancia a la otra con la fórmula punto-recta. La diferencia de los términos constantes dividida por la norma da el resultado.

> [!question]- En el ejercicio 4, ¿qué garantiza que la recta sea tangente?
> Que la cuadrática resultante de sustituir tenga discriminante cero: una sola intersección, que es justo la tangencia.

> [!question]- ¿Qué información da completar cuadrados en la forma general de una circunferencia?
> El centro y el radio, y si la ecuación representa una circunferencia, un punto o el conjunto vacío.
