---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[01 - Espacios vectoriales]]"
---

# Subespacios

La mayoría de los espacios que aparecen en la práctica viven **dentro** de otros más grandes: un plano por el origen dentro de $\mathbb{R}^3$, los polinomios que se anulan en 1 dentro de $\mathbb{P}_2$, las matrices simétricas dentro de $M_{n \times n}$, las soluciones de $A\mathbf x = \mathbf 0$ dentro de $\mathbb{R}^n$. Para saber si uno de esos subconjuntos es un espacio vectorial no hace falta revisar los diez axiomas: basta con tres condiciones.

## Definición y criterio

> [!tip] Definición
> Un **subespacio** de un espacio vectorial $V$ es un subconjunto $H \subseteq V$ que es espacio vectorial con la misma suma y el mismo producto por escalar. $H$ es subespacio si y solo si:
> 1. el vector cero de $V$ está en $H$;
> 2. $H$ es **cerrado bajo la suma**: si $\mathbf u, \mathbf v \in H$, entonces $\mathbf u + \mathbf v \in H$;
> 3. $H$ es **cerrado bajo el producto por escalar**: si $\mathbf u \in H$ y $c \in \mathbb{R}$, entonces $c\mathbf u \in H$.

Los otros axiomas (conmutatividad, asociatividad, etc.) se heredan de $V$, porque las operaciones son las mismas. El opuesto también: $-\mathbf u = (-1)\mathbf u \in H$ por la condición 3.

**Ejemplos inmediatos.** $\{\mathbf 0\}$ y $V$ son subespacios de $V$. $\mathbb{P}_n$ es subespacio de $\mathbb{P}$. El plano $x_1x_2$, $\{\langle s, t, 0\rangle\}$, es un subespacio de $\mathbb{R}^3$: contiene a $\mathbf 0$, y sumar o escalar vectores con tercera componente 0 da tercera componente 0. Ojo: este plano **no es** $\mathbb{R}^2$ (sus vectores tienen tres componentes), aunque se parece.

![Recta que no pasa por el origen no es subespacio](adjuntos/Recta%20que%20no%20pasa%20por%20el%20origen%20no%20es%20subespacio.png)

> [!example]- Transcripción de la imagen
> Una recta $H$ en el plano $x_1x_2$ que corta los ejes lejos del origen. No contiene a $\mathbf 0$, así que no es un subespacio de $\mathbb{R}^2$.

> [!warning] Lo primero que se revisa: el cero
> Un plano o una recta que **no pasa por el origen** nunca es subespacio. Más en general, si $\mathbf 0 \notin H$, no hay nada más que revisar. Por ejemplo, $\{\langle x, y, z, w\rangle : x + y + z + w + 1 = 0\}$ no es subespacio de $\mathbb{R}^4$ porque $\mathbf 0$ da $1 \neq 0$.

## Los generados son subespacios

> [!tip] Teorema
> Si $\mathbf v_1, \dots, \mathbf v_p \in V$, entonces $\operatorname{Gen}\{\mathbf v_1, \dots, \mathbf v_p\}$ es un subespacio de $V$, llamado **subespacio generado**.

La suma de dos combinaciones lineales es otra combinación (se suman los pesos) y un múltiplo de una combinación también (se escalan los pesos); el cero es la combinación con pesos nulos.

Este teorema da la **forma más rápida de probar que algo es subespacio**: escribirlo como un generado.

**Ejemplo.** $H = \{\langle a - 3b,\ b - a,\ a,\ b\rangle : a, b \in \mathbb{R}\}$. Separando por parámetros,
$$
\langle a - 3b, b - a, a, b\rangle = a\langle 1, -1, 1, 0\rangle + b\langle -3, 1, 0, 1\rangle,
$$
así que $H = \operatorname{Gen}\{\langle 1, -1, 1, 0\rangle, \langle -3, 1, 0, 1\rangle\}$, un subespacio de $\mathbb{R}^4$.

## Subespacios en otros espacios

El criterio se aplica igual con matrices y polinomios.

- **Matrices simétricas** $\{A : A^T = A\}$ en $M_{n \times n}$: $0^T = 0$; si $A^T = A$ y $B^T = B$, $(A + B)^T = A + B$ y $(cA)^T = cA$. Es subespacio.
- **Matrices de determinante cero** en $M_{2 \times 2}$: $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ y $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ tienen determinante 0, pero su suma es $I$. No es cerrado bajo la suma: **no** es subespacio.
- **Polinomios con $p(1) = 0$** en $\mathbb{P}_2$: el nulo cumple; $(q + r)(1) = q(1) + r(1) = 0$; $(cq)(1) = cq(1) = 0$. Es subespacio.
- **Matrices que conmutan con una fija $N$**, $\{A : AN = NA\}$: $0N = N0$; si $AN = NA$ y $BN = NB$, $(A + B)N = AN + BN = NA + NB = N(A + B)$; igual con $cA$. Es subespacio.

Las condiciones definidas por **ecuaciones lineales homogéneas** (igualdades que valen para el cero y se preservan al sumar y escalar) dan subespacios. Las que tienen términos constantes, productos o desigualdades suelen no darlos.

## Preguntas de repaso

> [!question]- ¿Es subespacio de $\mathbb{R}^3$ el conjunto $\{\langle x, y, z\rangle : x = 2y\}$? ¿Y $\{\langle x, y, z\rangle : x = 2y + 1\}$?
> El primero sí: es $\operatorname{Gen}\{\langle 2, 1, 0\rangle, \langle 0, 0, 1\rangle\}$, un plano por el origen. El segundo no: $\mathbf 0$ no cumple $0 = 1$.

> [!question]- ¿Es subespacio de $\mathbb{R}^2$ la unión de los dos ejes coordenados?
> No. Contiene a $\mathbf e_1$ y a $\mathbf e_2$, pero no a su suma $\langle 1, 1\rangle$. Contener al cero y ser cerrado por escalares no basta.

> [!question]- Escriba $W = \{\langle 2s + 4t, 2s, 2s - 3t, 5t\rangle\}$ como generado y concluya que es subespacio.
> $W = \operatorname{Gen}\{\langle 2, 2, 2, 0\rangle, \langle 4, 0, -3, 5\rangle\}$. Todo conjunto generado es subespacio.

> [!question]- ¿Por qué no hace falta verificar la conmutatividad de la suma en un subespacio?
> Porque los vectores de $H$ son vectores de $V$ con la misma suma, y en $V$ la suma ya es conmutativa. Solo hay que verificar lo que puede fallar: que las operaciones no saquen de $H$.
