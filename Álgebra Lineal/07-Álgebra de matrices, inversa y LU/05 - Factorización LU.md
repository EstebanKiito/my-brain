---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/matrices
  - algebra-lineal/factorizaciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Matrices elementales y cálculo de la inversa]]"
---

# Factorización LU

En las aplicaciones es muy común resolver **muchos** sistemas con la misma matriz: $A\mathbf x = \mathbf b_1$, $A\mathbf x = \mathbf b_2$, etc. Escalonar desde cero cada vez repite el mismo trabajo, y calcular $A^{-1}$ es caro e inestable numéricamente. La **factorización LU** guarda el trabajo de escalonar $A$ una sola vez, en dos matrices triangulares, y después cada sistema se resuelve con dos sustituciones rápidas.

## Qué es

> [!tip] Definición
> Una **factorización LU** de $A$ ($m \times n$) es una escritura $A = LU$ donde
> - $L$ es de $m \times m$, **triangular inferior con unos en la diagonal** (unitaria);
> - $U$ es de $m \times n$ y es una **forma escalonada** de $A$ (triangular superior si $A$ es cuadrada).

$$
A = \underbrace{\begin{bmatrix} 1 & 0 & 0 & 0 \\ * & 1 & 0 & 0 \\ * & * & 1 & 0 \\ * & * & * & 1 \end{bmatrix}}_{L}\underbrace{\begin{bmatrix} \blacksquare & * & * & * & * \\ 0 & \blacksquare & * & * & * \\ 0 & 0 & 0 & \blacksquare & * \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}}_{U}
$$

## Cómo se usa para resolver

$A\mathbf x = \mathbf b$ es $L(U\mathbf x) = \mathbf b$. Llamando $\mathbf y = U\mathbf x$, se resuelven dos sistemas triangulares:

> [!tip] Resolver con LU
> 1. $L\mathbf y = \mathbf b$, por **sustitución hacia adelante** (de arriba hacia abajo).
> 2. $U\mathbf x = \mathbf y$, por **sustitución hacia atrás** (de abajo hacia arriba).

![Factorización LU del mapeo x a Ax](adjuntos/Factorizaci%C3%B3n%20LU%20del%20mapeo%20x%20a%20Ax.png)

> [!example]- Transcripción de la imagen
> Tres planos: $\mathbf x$ a la izquierda, $\mathbf y$ abajo al centro y $\mathbf b$ a la derecha. Una flecha directa "multiplicación por $A$" va de $\mathbf x$ a $\mathbf b$. El camino alternativo pasa por "multiplicación por $U$" de $\mathbf x$ a $\mathbf y$ y luego "multiplicación por $L$" de $\mathbf y$ a $\mathbf b$. Resolver $A\mathbf x = \mathbf b$ es recorrer ese camino al revés: primero se obtiene $\mathbf y$ desde $\mathbf b$ y luego $\mathbf x$ desde $\mathbf y$.

## Algoritmo

Supóngase que $A$ se puede escalonar usando **solo reemplazos** $F_i \to F_i - \ell_{ij}F_j$ con $i > j$ (restar a una fila un múltiplo de otra de **más arriba**), sin intercambios.

> [!tip] Algoritmo LU
> 1. Escalonar $A$ hasta $U$ solo con reemplazos hacia abajo, anotando cada **multiplicador** $\ell_{ij}$ de $F_i \to F_i - \ell_{ij}F_j$.
> 2. $L$ es la identidad con $\ell_{ij}$ en la posición $(i, j)$.

Se justifica con matrices elementales: $E_k\cdots E_1A = U$, así que $A = (E_1^{-1}\cdots E_k^{-1})U$, y ese producto de elementales triangulares inferiores es exactamente $L$, con los multiplicadores en su lugar (cambiados de signo respecto de las $E_i$).

**Ejemplo.** $A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & -6 & 0 \\ -2 & 7 & 2 \end{bmatrix}$.

- $F_2 \to F_2 - 2F_1$ ($\ell_{21} = 2$) y $F_3 \to F_3 - (-1)F_1$ ($\ell_{31} = -1$): filas $[0\ -8\ -2]$ y $[0\ 8\ 3]$.
- $F_3 \to F_3 - (-1)F_2$ ($\ell_{32} = -1$): fila $[0\ 0\ 1]$.

$$
L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}.
$$

Para $\mathbf b = \langle 5, -2, 9\rangle$: hacia adelante, $y_1 = 5$, $y_2 = -2 - 2 \cdot 5 = -12$, $y_3 = 9 + 5 - 12 = 2$. Hacia atrás, $x_3 = 2$, $-8x_2 - 4 = -12$ da $x_2 = 1$, y $2x_1 + 1 + 2 = 5$ da $x_1 = 1$. Solución: $\langle 1, 1, 2\rangle$.

> [!warning] El signo de los multiplicadores
> Si la operación es $F_i \to F_i - \ell F_j$, en $L$ va $+\ell$. Si se escribió como $F_i \to F_i + cF_j$, en $L$ va $-c$. Confundir el signo es el error más común; se detecta multiplicando $LU$ y comparando con $A$.

## Cuándo existe

La LU existe si la reducción no necesita **intercambios**. Eso ocurre, por ejemplo, cuando las submatrices principales de la esquina superior izquierda ($[a_{11}]$, el bloque de $2 \times 2$, etc.) son invertibles, porque entonces cada pivote aparece sin tener que intercambiar filas.

Si hace falta intercambiar, se ordenan primero las filas con una **matriz de permutación** $P$ (la identidad con sus filas reordenadas) y se factoriza $PA = LU$. Para resolver $A\mathbf x = \mathbf b$ se multiplica por $P$: $LU\mathbf x = P\mathbf b$.

**Datos útiles.**
- Las entradas de $A$ se leen del producto $LU$. Por ejemplo, la entrada $(3, 1)$ es $a_{31} = \ell_{31}u_{11} + \ell_{32}u_{21} + u_{31}$; como $U$ es escalonada, $u_{21} = u_{31} = 0$, así que $a_{31} = \ell_{31}u_{11}$. Si $\ell_{31} = 0$, la primera entrada de la tercera fila de $A$ es cero.
- Si $A = LU$, entonces $L^{-1}A = U$: $L^{-1}$ es una matriz triangular inferior $C$ que lleva $A$ a forma escalonada.

## Preguntas de repaso

> [!question]- ¿Por qué conviene la LU cuando hay muchos lados derechos?
> Porque el trabajo caro (escalonar $A$) se hace una sola vez. Cada $\mathbf b$ nuevo cuesta solo dos sustituciones triangulares, bastante menos que escalonar de nuevo o que multiplicar por una inversa calculada aparte.

> [!question]- Encuentre la LU de $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$.
> $F_2 \to F_2 - 3F_1$ da $U = \begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix}$ y $L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$.

> [!question]- ¿Tiene factorización LU la matriz $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$? ¿Qué se hace?
> No: la entrada $(1, 1)$ es cero y para escalonar hay que intercambiar filas. Se usa $PA = LU$ con $P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, y entonces $PA = I = I \cdot I$.

> [!question]- ¿Qué tipo de sustitución se usa en $L\mathbf y = \mathbf b$ y por qué es inmediata?
> Hacia adelante. La primera ecuación de un sistema triangular inferior con unos en la diagonal es $y_1 = b_1$, y cada ecuación siguiente agrega una sola incógnita nueva, que se despeja con las ya conocidas.
