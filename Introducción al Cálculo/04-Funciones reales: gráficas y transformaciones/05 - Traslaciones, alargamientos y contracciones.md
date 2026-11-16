---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[04 - Funciones elementales y funciones por tramos]]"
---

# Traslaciones, alargamientos y contracciones

Con un catálogo corto de funciones y cuatro tipos de modificación se obtienen las gráficas de casi cualquier fórmula. Esta nota cubre las cuatro modificaciones que **no** dan vuelta el gráfico: mover y estirar, vertical y horizontalmente. La regla de oro es que lo que se hace **dentro** del paréntesis (a la $x$) actúa al revés de lo que parece, y lo que se hace **fuera** (a la $y$) actúa tal cual.

## Desplazamientos verticales

> [!tip] Traslación vertical
> Para $c > 0$: $y = f(x) + c$ sube el gráfico $c$ unidades; $y = f(x) - c$ lo baja $c$ unidades.

![Desplazamientos verticales de una gráfica](adjuntos/Desplazamientos%20verticales%20de%20una%20gráfica.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, una curva ondulada azul $y = f(x)$ y la misma curva en rojo, $y = f(x) + c$, desplazada hacia arriba una distancia $c$. A la derecha, $y = f(x)$ en azul y $y = f(x) - c$ en rojo, desplazada hacia abajo.

Ejemplos con $f(x) = x^2$: $g(x) = x^2 + 3$ es la parábola con vértice en $(0, 3)$; $h(x) = x^2 - 2$, con vértice en $(0, -2)$.

## Desplazamientos horizontales

> [!tip] Traslación horizontal
> Para $c > 0$: $y = f(x - c)$ mueve el gráfico $c$ unidades a la **derecha**; $y = f(x + c)$ lo mueve $c$ unidades a la **izquierda**.

La razón: $f(x - c)$ toma en $x = c$ el valor que $f$ toma en $0$. El punto donde "pasa lo mismo" se corrió a la derecha.

![Desplazamientos horizontales de una gráfica](adjuntos/Desplazamientos%20horizontales%20de%20una%20gráfica.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, $y = f(x)$ (azul) y $y = f(x - c)$ (roja), que es la misma curva corrida hacia la derecha. A la derecha, $y = f(x)$ (azul) y $y = f(x + c)$ (roja), corrida hacia la izquierda. Una flecha celeste marca la distancia $c$.

Ejemplos con $f(x) = x^2$: $g(x) = (x + 4)^2$ es la parábola con vértice en $(-4, 0)$ y $h(x) = (x - 2)^2$, con vértice en $(2, 0)$. Combinando: $f(x) = \sqrt{x - 1} + 3$ es la raíz $\sqrt{x}$ corrida $1$ unidad a la derecha y $3$ hacia arriba; su dominio es $[1, \infty)$ y su recorrido $[3, \infty)$.

## Alargamiento y contracción verticales

> [!tip] Escala vertical
> Para $y = c\, f(x)$ con $c > 0$: si $c > 1$ el gráfico se **alarga** verticalmente en un factor $c$; si $0 < c < 1$ se **contrae** en un factor $c$. Los puntos sobre el eje $x$ (donde $f = 0$) no se mueven.

![Alargamiento y contracción verticales](adjuntos/Alargamiento%20y%20contracción%20verticales.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, para $c > 1$, la curva roja $y = c\,f(x)$ es más "alta" que la azul $y = f(x)$ (misma forma, picos y valles más pronunciados). A la derecha, para $0 < c < 1$, la roja $y = c\,f(x)$ es más baja y plana que la azul. Ambas curvas cruzan el eje $x$ en los mismos puntos.

Con $f(x) = x^2$: $g(x) = 3x^2$ es una parábola más cerrada (sube más rápido) y $h(x) = \tfrac{1}{3}x^2$ es más abierta.

## Alargamiento y contracción horizontales

> [!tip] Escala horizontal
> Para $y = f(cx)$ con $c > 0$: si $c > 1$ el gráfico se **contrae** horizontalmente en un factor $\tfrac{1}{c}$; si $0 < c < 1$ se **alarga** horizontalmente en un factor $\tfrac{1}{c}$.

El efecto es contrario al de la escala vertical: multiplicar la $x$ por $2$ hace que la función "recorra su gráfico al doble de velocidad", así que el dibujo se comprime a la mitad. Los puntos sobre el eje $y$ (donde $x = 0$) no se mueven.

![Alargamiento y contracción horizontales](adjuntos/Alargamiento%20y%20contracción%20horizontales.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, para $c > 1$, la curva roja $y = f(cx)$ está comprimida horizontalmente: oscila más rápido que la azul $y = f(x)$. A la derecha, para $0 < c < 1$, la roja $y = f(cx)$ está estirada: oscila más lento. Ambas cortan el eje $y$ en el mismo punto.

## Ejemplo: una función con picos

Sea $f$ una función "en dientes de sierra" con picos de altura $1$ en cada entero impar y valores $0$ en cada par. Entonces:

![Función con picos del ejemplo de contracción horizontal](adjuntos/Función%20con%20picos%20del%20ejemplo%20de%20contracción%20horizontal.png)

> [!example]- Transcripción de la figura (clase 10)
> Una línea quebrada roja en zigzag que sube a $1$ y baja a $0$ de manera periódica; los puntos suspensivos indican que continúa hacia ambos lados.

- $y = f(2x)$ comprime el gráfico a la mitad: los picos aparecen cada media unidad, el doble de seguido.
- $y = f\!\left(\tfrac{1}{2}x\right)$ lo alarga al doble: los picos quedan separados por $2$ unidades.

![Contracción y alargamiento horizontales de la función con picos](adjuntos/Contracción%20y%20alargamiento%20horizontales%20de%20la%20función%20con%20picos.png)

> [!example]- Transcripción de la figura (clase 10)
> A la izquierda, $y = f(2x)$: el zigzag se repite el doble de rápido, con picos en múltiplos de $\tfrac{1}{2}$ y marcas en $\tfrac{1}{2}$ y $1$ sobre el eje $x$. A la derecha, $y = f\!\left(\tfrac{1}{2}x\right)$: el zigzag es más ancho, con picos en $-1$ y $1$ y valores $0$ en $-2$, $0$ y $2$.

## Efecto sobre el dominio y el recorrido

Si $f$ tiene dominio $D$ y recorrido $R$, entonces $y = c\,f(x - h) + k$ (con $c > 0$) tiene dominio $D + h$ y recorrido $c R + k$. Los desplazamientos mueven los intervalos; los alargamientos los estiran.

## Preguntas de repaso

> [!question]- ¿Hacia dónde se mueve el gráfico de $y = f(x + 5)$ y por qué?
> Hacia la **izquierda** $5$ unidades. El valor que $f$ toma en $0$ ahora aparece en $x = -5$ (porque $f(-5 + 5) = f(0)$).

> [!question]- ¿Qué diferencia hay entre $y = 3f(x)$ y $y = f(3x)$?
> $3f(x)$ multiplica las alturas por $3$ (alargamiento vertical, el eje $x$ queda fijo). $f(3x)$ comprime el gráfico horizontalmente a un tercio (el eje $y$ queda fijo).

> [!question]- ¿Cuál es el dominio y recorrido de $y = \sqrt{x - 1} + 3$?
> Dominio $[1, \infty)$ (se desplaza $1$ a la derecha) y recorrido $[3, \infty)$ (se desplaza $3$ hacia arriba).

> [!question]- Si $f$ tiene recorrido $[-1, 2]$, ¿qué recorrido tiene $2f(x) + 1$?
> $[2(-1) + 1,\ 2(2) + 1] = [-1, 5]$: se multiplica y luego se suma.
