---
ramo: "Álgebra Lineal"
tema: "Sistemas de ecuaciones lineales"
tags:
  - algebra-lineal/sistemas
  - origen/complemento
prerrequisitos:
  - "[[03 - Posición relativa, intersecciones e hiperplanos]]"
---

# Ecuaciones lineales e intersección de planos

Una ecuación lineal en $\mathbb{R}^3$ es un plano. Por eso resolver un **sistema de ecuaciones lineales** (SEL) equivale a encontrar los puntos comunes a varios planos o, en $\mathbb{R}^n$, a varios hiperplanos. Esta lectura geométrica explica de inmediato por qué un sistema lineal solo puede tener ninguna, una o infinitas soluciones, y por qué los métodos de eliminación funcionan.

## Ecuación lineal

> [!tip] Definición
> Una **ecuación lineal** en las variables $x_1, \dots, x_n$ es una igualdad de la forma
> $$a_1x_1 + a_2x_2 + \dots + a_nx_n = b,$$
> con **coeficientes** $a_i$ y **término independiente** $b$ reales. Es **homogénea** si $b = 0$.

Cada variable aparece a la primera potencia, multiplicada solo por una constante. $-3x + y - 2z = 9$ es lineal; $3x^2 + xy - z + 2x = 1$ no lo es (tiene un cuadrado y un producto de variables), y tampoco lo son $\sqrt{x} + y = 1$ o $\sin x = y$.

Geométricamente, la misma forma describe objetos distintos según el espacio:

| Ecuación | Espacio | Objeto |
|---|---|---|
| $-3x = 9$ | $\mathbb{R}$ | un punto ($x = -3$) |
| $-3x + y = 9$ | $\mathbb{R}^2$ | una recta |
| $-3x + y - 2z = 9$ | $\mathbb{R}^3$ | un plano |
| $-3x_1 + x_2 - 2x_3 + \dots + 3x_8 = 9$ | $\mathbb{R}^8$ | un hiperplano |

Una ecuación homogénea describe un hiperplano **que pasa por el origen** ($\mathbf 0$ la cumple); una no homogénea, un hiperplano desplazado.

## Sistema de ecuaciones lineales

> [!tip] Definición
> Un **sistema de ecuaciones lineales** es una colección de $m$ ecuaciones lineales en las mismas variables $x_1, \dots, x_n$:
> $$\begin{cases} a_{11}x_1 + \dots + a_{1n}x_n = b_1 \\ \quad\vdots \\ a_{m1}x_1 + \dots + a_{mn}x_n = b_m \end{cases}$$
> Una **solución** es un vector $\mathbf s = \langle s_1, \dots, s_n\rangle$ que satisface **todas** las ecuaciones a la vez. El **conjunto solución** reúne todas las soluciones. El sistema es **consistente** si tiene al menos una, e **inconsistente** si no tiene ninguna.

Dos sistemas son **equivalentes** si tienen el mismo conjunto solución.

**Ejemplo.** La intersección de $3x - 2y + z = 1$ y $x + y - 3z = 2$ es una recta. Eliminando variables se llega a $x = 1 + z$ e $y = 1 + 2z$, con $z$ libre. Llamando $t = z$:

$$
\begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}1\\1\\0\end{bmatrix} + t\begin{bmatrix}1\\2\\1\end{bmatrix}, \qquad t \in \mathbb{R}.
$$

Cada valor de $t$ da una solución distinta. El director $\langle 1, 2, 1\rangle$ es perpendicular a ambos normales, como debe ser.

## Por qué la eliminación no cambia la intersección

Al resolver se reemplazan ecuaciones por otras: se multiplica una ecuación por un número no nulo o se le suma un múltiplo de otra. La segunda operación **cambia el plano** que representa esa ecuación (lo hace girar en torno a la intersección), pero **no cambia los puntos comunes**: si un punto cumple ambas ecuaciones, cumple cualquier combinación de ellas, y la operación se puede deshacer. Por eso la eliminación produce sistemas equivalentes cada vez más simples hasta que la solución se lee directamente.

## Posiciones relativas y número de soluciones

Dos planos en $\mathbb{R}^3$ pueden cortarse en una recta (infinitas soluciones con un parámetro), ser paralelos distintos (ninguna) o coincidir (infinitas, todo un plano). Dos planos nunca comparten exactamente dos puntos: si comparten dos, comparten la recta que los une.

![Posiciones relativas de dos planos](adjuntos/Posiciones%20relativas%20de%20dos%20planos.png)

> [!example]- Transcripción de la imagen
> Tres paneles con dos planos $\pi_1$ y $\pi_2$: se cortan en una recta $r$ (resaltada); $\pi_2$ coincide con $\pi_1$ (dibujado dentro de él); $\pi_1$ y $\pi_2$ son paralelos y separados.

Con tres planos hay más casos:

| Configuración | Soluciones |
|---|---|
| se cortan en un único punto $P$ | una |
| comparten una recta $r$ (como las hojas de un libro) | infinitas (un parámetro) |
| los tres coinciden | infinitas (dos parámetros) |
| los tres paralelos, o dos paralelos distintos | ninguna |
| se cortan dos a dos en tres rectas paralelas (un "prisma") | ninguna |

![Posiciones relativas de tres planos](adjuntos/Posiciones%20relativas%20de%20tres%20planos.png)

> [!example]- Transcripción de la imagen
> Cinco paneles con los planos $\alpha$, $\beta$ y $\gamma$: (1) se cortan en un solo punto $P$; (2) los tres pasan por una misma recta $r$; (3) tres planos paralelos, $\alpha \parallel \beta \parallel \gamma$; (4) $\beta = \gamma$ y paralelos a $\alpha$; (5) dos casos sin punto común: tres planos que se cortan de a pares formando un prisma, y dos planos paralelos ($\beta \parallel \gamma$) cortados por un tercero.

> [!tip] Número de soluciones de un sistema lineal
> Todo sistema lineal tiene **ninguna**, **exactamente una** o **infinitas** soluciones. Nunca un número finito mayor que uno.

La razón algebraica: si $\mathbf s$ y $\mathbf r$ son soluciones distintas, todos los puntos $\mathbf s + t(\mathbf r - \mathbf s)$ de la recta que las une también lo son, así que hay infinitas.

**Ejemplo de clasificación.** Con las ecuaciones $x + y + z = 1$ y $2x - 3y + 4z = 1$:

- Si se agrega $2x - 3y + 4z = 2$, este plano es paralelo al segundo y distinto: **sin solución**.
- Si se agrega $3x + 5y - z = 2$, los normales no tienen relaciones especiales y la eliminación da el punto $\left(\tfrac{3}{16}, \tfrac{3}{8}, \tfrac{7}{16}\right)$: **solución única**.
- Si se agrega $10x + 25y + 4z = 1$, ningún par es paralelo, pero la eliminación lleva a $0 = 1$: es el **prisma**.

## Preguntas de repaso

> [!question]- ¿Qué significa geométricamente que en la ecuación de un plano no aparezca la variable $x$?
> El normal es $\langle 0, b, c\rangle$, perpendicular a $\mathbf e_1$. El plano es paralelo al eje $x$: si $(x, y, z)$ está en él, $(x + t, y, z)$ también, para todo $t$.

> [!question]- ¿Puede un sistema lineal tener exactamente dos soluciones? Justifique.
> No. Si $\mathbf s \neq \mathbf r$ son soluciones, cada $\mathbf s + t(\mathbf r - \mathbf s)$ también lo es, porque al reemplazar en $\mathbf a \cdot \mathbf x = b$ se obtiene $(1 - t)b + tb = b$. Esa recta aporta infinitas soluciones.

> [!question]- ¿Por qué sumarle a una ecuación un múltiplo de otra no cambia el conjunto solución, aunque cambie el plano?
> Todo punto que cumple las dos ecuaciones originales cumple su combinación, y la operación se deshace restando el mismo múltiplo. Así, ambos sistemas tienen exactamente las mismas soluciones, aunque uno de los planos haya girado en torno a la intersección.

> [!question]- Tres planos sin ningún par paralelo, ¿siempre tienen un punto en común?
> No. Pueden cortarse de a pares en tres rectas paralelas (un prisma) y no tener ningún punto común, o pasar los tres por una misma recta y tener infinitos.

> [!question]- ¿Qué objeto es el conjunto solución de un sistema homogéneo consistente en $\mathbb{R}^3$, y por qué nunca es vacío?
> Siempre contiene al origen, porque $\mathbf x = \mathbf 0$ cumple todas las ecuaciones con $b = 0$. Puede ser solo el origen, una recta o un plano por el origen, o todo $\mathbb{R}^3$.
