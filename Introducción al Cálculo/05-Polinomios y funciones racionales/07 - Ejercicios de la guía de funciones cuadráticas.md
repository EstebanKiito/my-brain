---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Problemas de máximos y mínimos con cuadráticas]]"
---

# Ejercicios de la guía de funciones cuadráticas

Los cuatro ejercicios de la Guía 6: dos problemas de optimización y dos de forma normal. Todos se resuelven con el vértice.

## Ejercicios

### 1. El canal de agua lluvia
Un canal se forma doblando hacia arriba los lados de una lámina metálica rectangular de $28$ cm de ancho. ¿Cuál es el área máxima de la sección transversal?

> [!example]- Solución
> Si se doblan $x$ cm de cada lado, la sección es un rectángulo de base $28 - 2x$ y altura $x$: $A(x) = x(28 - 2x) = -2x^2 + 28x$. Es una cuadrática con $a < 0$: el máximo está en $x = -\tfrac{28}{2(-2)} = 7$, con $A(7) = 7 \cdot 14 = 98\ \text{cm}^2$.

### 2. El precio del boleto
Un equipo de hockey juega en una cancha de $15\,000$ espectadores. Con boleto a $14$ dólares, la asistencia promedio es $9\,500$; por cada dólar que baje el precio, aumenta en $1\,000$. Encuentre el precio que maximiza el ingreso.

> [!example]- Solución
> Si el precio baja $t$ dólares, el ingreso es $I(t) = (14 - t)(9\,500 + 1\,000t) = -1\,000t^2 + 4\,500t + 133\,000$. El vértice está en $t = \tfrac{4\,500}{2\,000} = 2{,}25$. Precio: $14 - 2{,}25 = 11{,}75$ dólares. La asistencia sería $11\,750 \le 15\,000$, admisible, y el ingreso máximo $11{,}75 \cdot 11\,750 = 138\,062{,}5$ dólares.

### 3. Graficar una cuadrática
Grafique $f(x) = 5x^2 - 30x + 49$.

> [!example]- Solución
> Forma normal: $f(x) = 5(x^2 - 6x) + 49 = 5(x - 3)^2 - 45 + 49 = 5(x - 3)^2 + 4$. Vértice $(3, 4)$, abre hacia arriba. Como $\Delta = 900 - 980 = -80 < 0$, no corta el eje $x$. Corta el eje $y$ en $(0, 49)$ (y por simetría pasa también por $(6, 49)$). Es la parábola $y = x^2$ trasladada $3$ a la derecha y $4$ hacia arriba, con alargamiento vertical en factor $5$. Mínimo $4$, recorrido $[4, \infty)$.

### 4. El vértice
Determine el vértice de la parábola $f(x) = -6x^2 + 2x - 4$.

> [!example]- Solución
> $x_v = -\tfrac{b}{2a} = -\tfrac{2}{-12} = \tfrac{1}{6}$ y $y_v = f\!\left(\tfrac{1}{6}\right) = -\tfrac{6}{36} + \tfrac{2}{6} - 4 = -\tfrac{1}{6} + \tfrac{1}{3} - 4 = -\tfrac{23}{6}$. El vértice es $\left(\tfrac{1}{6}, -\tfrac{23}{6}\right)$. Como $a < 0$, es un máximo.

## Preguntas de repaso

> [!question]- ¿Por qué el ingreso del ejercicio 2 se maximiza en el vértice y no en un extremo?
> Porque $I(t)$ es una cuadrática con coeficiente principal negativo, que crece hasta el vértice y decrece después. El vértice $t = 2{,}25$ está dentro del rango permitido por la capacidad de la cancha.

> [!question]- ¿Cómo se ve en el ejercicio 3 que $f$ no tiene raíces reales?
> $f(x) = 5(x - 3)^2 + 4 \ge 4 > 0$ para todo $x$: nunca se anula.

> [!question]- ¿Qué área tiene el canal si se doblan $5$ cm por lado?
> $A(5) = 5 \cdot 18 = 90\ \text{cm}^2$, menor que el máximo $98$.
