---
ramo: "Álgebra Lineal"
tema: "Vectores en Rⁿ"
tags:
  - algebra-lineal/vectores
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto punto, norma y distancia]]"
---

# Ángulo, ortogonalidad y teorema de Pitágoras

En el plano, el ángulo entre dos flechas se mide con un transportador. En $\mathbb{R}^n$ no hay transportador, pero el producto punto hace ese trabajo: su signo y su tamaño, comparados con las normas, dicen cuánto "se parecen" las direcciones de dos vectores. Con eso se define el ángulo en cualquier dimensión y, sobre todo, la **ortogonalidad**, que es el concepto que más se usa del capítulo.

## Desigualdad de Cauchy-Schwarz

> [!tip] Teorema (Cauchy-Schwarz)
> Para todo $\mathbf u, \mathbf v \in \mathbb{R}^n$,
> $$|\mathbf u \cdot \mathbf v| \leq \|\mathbf u\|\,\|\mathbf v\|,$$
> con igualdad si y solo si uno de los vectores es múltiplo del otro.

Garantiza que el cociente $\dfrac{\mathbf u \cdot \mathbf v}{\|\mathbf u\|\|\mathbf v\|}$ siempre está entre $-1$ y $1$, así que se le puede asignar un ángulo cuyo coseno sea ese número. Además sirve como control de cordura: si un enunciado dice que dos vectores unitarios tienen producto punto $5$, el enunciado es imposible, porque $|\mathbf u \cdot \mathbf v| \leq 1 \cdot 1$.

## Ángulo entre vectores

> [!tip] Definición
> Para $\mathbf u, \mathbf v$ no nulos, el ángulo $\theta \in [0, \pi]$ entre ellos cumple
> $$\cos\theta = \frac{\mathbf u \cdot \mathbf v}{\|\mathbf u\|\,\|\mathbf v\|} \qquad\Longleftrightarrow\qquad \mathbf u \cdot \mathbf v = \|\mathbf u\|\,\|\mathbf v\|\cos\theta .$$

En $\mathbb{R}^2$ y $\mathbb{R}^3$ esta fórmula coincide con el ángulo geométrico (sale del teorema del coseno aplicado al triángulo de lados $\mathbf u$, $\mathbf v$ y $\mathbf u - \mathbf v$). En $\mathbb{R}^n$ se toma como definición. Solo el **signo** del producto punto ya dice mucho:

| $\mathbf u \cdot \mathbf v$ | Ángulo | Lectura |
|---|---|---|
| $> 0$ | agudo, $\theta < \pi/2$ | apuntan "hacia el mismo lado" |
| $= 0$ | recto, $\theta = \pi/2$ | perpendiculares |
| $< 0$ | obtuso, $\theta > \pi/2$ | apuntan "hacia lados opuestos" |

**Ejemplo.** Con $\mathbf u = \langle 1, 0, 1\rangle$ y $\mathbf v = \langle 0, 1, 1\rangle$: $\mathbf u \cdot \mathbf v = 1$ y $\|\mathbf u\| = \|\mathbf v\| = \sqrt2$, así que $\cos\theta = \frac{1}{2}$ y $\theta = \pi/3$.

## Ortogonalidad

> [!tip] Definición
> $\mathbf u$ y $\mathbf v$ son **ortogonales** si $\mathbf u \cdot \mathbf v = 0$.

Para vectores no nulos significa que forman un ángulo recto. La definición no excluye al vector cero, que es ortogonal a todos, incluso a sí mismo; es el único vector con esa propiedad.

**Ejemplo.** $\langle 1, 1, -2\rangle \cdot \langle 3, 1, 2\rangle = 3 + 1 - 4 = 0$, así que son ortogonales.

Una consecuencia útil de la distributividad: si $\mathbf n$ es ortogonal a $\mathbf u$ y a $\mathbf v$, es ortogonal a cualquier combinación $a\mathbf u + b\mathbf v$, porque $\mathbf n \cdot (a\mathbf u + b\mathbf v) = a\,\mathbf n \cdot \mathbf u + b\,\mathbf n \cdot \mathbf v = 0$. Es decir, un vector ortogonal a dos direcciones lo es a todo el plano que generan. Esta es la idea detrás del vector normal de un plano.

## Teorema de Pitágoras

> [!tip] Teorema (Pitágoras)
> Si $\mathbf u \cdot \mathbf v = 0$, entonces $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2$.

**Demostración.** Se expande la norma al cuadrado con la distributividad:

$$
\|\mathbf u + \mathbf v\|^2 = (\mathbf u + \mathbf v)\cdot(\mathbf u + \mathbf v) = \|\mathbf u\|^2 + 2\,\mathbf u \cdot \mathbf v + \|\mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2 ,
$$

porque el término cruzado $2\,\mathbf u \cdot \mathbf v$ vale cero. $\blacksquare$

La demostración muestra algo más fuerte: la igualdad se cumple **si y solo si** $\mathbf u \cdot \mathbf v = 0$, porque el término cruzado es lo único que separa ambos lados.

> [!warning] La norma no es lineal
> En general $\|\mathbf u + \mathbf v\| \neq \|\mathbf u\| + \|\mathbf v\|$. Con $\mathbf u = \mathbf e_1$ y $\mathbf v = \mathbf e_2$ se obtiene $\sqrt2 \neq 2$. La igualdad solo se da cuando uno es múltiplo no negativo del otro. Para cualquier otra relación hay que pasar por $\|\cdot\|^2$ y expandir.

## Patrón de demostración

Casi todas las preguntas de demostración del tema se resuelven igual:

1. Escribir la condición geométrica como producto punto (ortogonal: $= 0$; ángulo: fórmula del coseno; longitud: $\|\mathbf x\|^2 = \mathbf x \cdot \mathbf x$).
2. Expandir con distributividad y conmutatividad.
3. Reemplazar los datos ($\mathbf v_i \cdot \mathbf v_i = 1$ si es unitario, $= 0$ si son ortogonales, normas iguales, etc.).

## Preguntas de repaso

> [!question]- Calcule $\mathbf u \cdot \mathbf v$ si $\|\mathbf u\| = 3$, $\|\mathbf v\| = 5$ y el ángulo entre ellos es $\pi/3$.
> $\mathbf u \cdot \mathbf v = 3 \cdot 5 \cdot \cos(\pi/3) = \tfrac{15}{2}$.

> [!question]- Encuentre todos los $k$ para que $\langle k, 2, -1\rangle$ y $\langle k, k, 3\rangle$ sean ortogonales.
> $k^2 + 2k - 3 = 0$, es decir, $(k + 3)(k - 1) = 0$. Son $k = 1$ y $k = -3$.

> [!question]- Demuestre que si $\mathbf u + \mathbf v$ y $\mathbf u - \mathbf v$ son ortogonales, entonces $\|\mathbf u\| = \|\mathbf v\|$. ¿Qué dice esto de un paralelogramo?
> $0 = (\mathbf u + \mathbf v)\cdot(\mathbf u - \mathbf v) = \|\mathbf u\|^2 - \mathbf u \cdot \mathbf v + \mathbf v \cdot \mathbf u - \|\mathbf v\|^2 = \|\mathbf u\|^2 - \|\mathbf v\|^2$, y como las normas no son negativas, son iguales. Las diagonales de un paralelogramo son perpendiculares solo si sus lados miden lo mismo, es decir, si es un rombo.

> [!question]- ¿Por qué Cauchy-Schwarz es necesario para definir el ángulo en $\mathbb{R}^n$?
> Porque $\arccos$ solo acepta valores en $[-1, 1]$. Cauchy-Schwarz asegura que $\frac{\mathbf u \cdot \mathbf v}{\|\mathbf u\|\|\mathbf v\|}$ cae en ese intervalo para cualquier par de vectores no nulos.

> [!question]- V o F: si $\mathbf u$ es ortogonal a $\mathbf v$ y $\mathbf v$ es ortogonal a $\mathbf w$, entonces $\mathbf u$ es ortogonal a $\mathbf w$.
> Falso. En $\mathbb{R}^3$, $\mathbf e_1 \perp \mathbf e_2$ y $\mathbf e_2 \perp \mathbf e_1$, pero $\mathbf e_1 \cdot \mathbf e_1 = 1 \neq 0$. La ortogonalidad no es transitiva.
