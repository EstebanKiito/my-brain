---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones cuadráticas, forma normal y vértice]]"
---

# Problemas de máximos y mínimos con cuadráticas

Muchos problemas de contexto piden "el valor que hace máxima (o mínima) una cantidad". Cuando esa cantidad depende de **una sola variable** de forma cuadrática, el problema se resuelve con el vértice: no hace falta derivar. El trabajo está en traducir el enunciado a una función de una incógnita.

## Método

> [!tip] Pasos
> 1. Elegir la variable y escribir las demás cantidades en términos de ella (usando la restricción del enunciado).
> 2. Escribir la cantidad a optimizar como una función $f$ de esa única variable.
> 3. Si $f$ es cuadrática, el óptimo está en el vértice $x = -\tfrac{b}{2a}$ (máximo si $a < 0$, mínimo si $a > 0$).
> 4. Comprobar que el valor obtenido es admisible (dentro de los límites del problema) y responder lo que se pregunta (a veces es la variable y a veces el valor de $f$).

## Ejemplo 1: el precio de un boleto (clase 11)

Un equipo de hockey juega en una cancha con capacidad para $15\,000$ espectadores. Con boleto a $14$ dólares, la asistencia promedio es $9\,500$; por cada dólar que baje el precio, sube en $1\,000$. ¿Qué precio maximiza el ingreso?

Sea $t$ los dólares que se baja el precio. El precio es $14 - t$ y la asistencia $9\,500 + 1\,000t$, luego el ingreso es
$$I(t) = (14 - t)(9\,500 + 1\,000t) = -1\,000t^2 + 4\,500t + 133\,000.$$
Es una cuadrática con $a < 0$: el máximo está en $t = -\tfrac{4\,500}{2(-1\,000)} = 2{,}25$. El precio es $14 - 2{,}25 = 11{,}75$ dólares, con asistencia $9\,500 + 2\,250 = 11\,750$ (menor que la capacidad, así que es admisible) e ingreso máximo $11{,}75 \cdot 11\,750 = 138\,062{,}5$ dólares.

## Ejemplo 2: el canal de agua lluvia (Guía 6)

Un canal se forma doblando hacia arriba los lados de una lámina metálica rectangular de $28$ cm de ancho. ¿Cuál es el área máxima de la sección transversal?

Si se doblan $x$ cm de cada lado, la sección es un rectángulo de base $28 - 2x$ y altura $x$: $A(x) = x(28 - 2x) = -2x^2 + 28x$, con $0 < x < 14$. El vértice está en $x = -\tfrac{28}{-4} = 7$ y $A(7) = 7 \cdot 14 = 98\ \text{cm}^2$.

## Ejemplo 3: el huerto con una división (I4, 2023-1)

Se dispone de $80$ m de cerca para un huerto rectangular, con un lado en el deslinde del vecino (sin cerca) y una división interior paralela a los lados que se miden $y$. El plano muestra $3$ segmentos de longitud $y$ y uno de longitud $x$: $80 = 3y + x$. El área es $xy$. Despejando $x = 80 - 3y$ queda $A(y) = (80 - 3y)y = -3y^2 + 80y$, y el máximo está en $y = \tfrac{40}{3}$, con $x = 40$ y área $\tfrac{1600}{3}\ \text{m}^2$. La pregunta original solo pedía **plantear** el problema de una incógnita, no resolverlo.

## Ejemplo 4: determinar un parámetro con el mínimo (I4, 2023-1)

Sea $f(x) = 3x^2 + \lambda x + 10$. Hallar los $\lambda$ para los que el valor mínimo de $f$ es $-2$.

Completando el cuadrado: $f(x) = 3\left(x + \tfrac{\lambda}{6}\right)^2 + 10 - \tfrac{\lambda^2}{12}$. El mínimo ($a = 3 > 0$) vale $10 - \tfrac{\lambda^2}{12}$ y se alcanza en $x = -\tfrac{\lambda}{6}$. Se plantea $10 - \tfrac{\lambda^2}{12} = -2 \iff \lambda^2 = 144 \iff \lambda = \pm 12$.

> [!warning] Dónde se pierden puntos
> - No comprobar que el óptimo cae en el rango permitido (por ejemplo, que la asistencia no pase de la capacidad de la cancha).
> - Responder con el valor de la variable auxiliar ($t = 2{,}25$) cuando se pregunta por el precio ($11{,}75$).
> - Olvidar que el signo de $a$ decide si el vértice es máximo o mínimo.

## Preguntas de repaso

> [!question]- ¿Por qué el ingreso del ejemplo 1 es una cuadrática en $t$?
> Es el producto de dos expresiones lineales en $t$ (precio y asistencia), que da un polinomio de grado $2$ con coeficiente principal negativo, así que tiene un máximo en el vértice.

> [!question]- ¿Qué variable conviene en el ejemplo 3, $x$ o $y$?
> Cualquiera: de $80 = 3y + x$ se despeja una en términos de la otra y se obtiene una cuadrática. Con $x$ queda $A(x) = \frac{x(80 - x)}{3}$, con el mismo óptimo.

> [!question]- Si el vértice de la cuadrática queda fuera del intervalo permitido, ¿dónde está el óptimo?
> En uno de los extremos del intervalo, porque la cuadrática es monótona a cada lado del vértice. Hay que evaluar la función en los extremos permitidos.
