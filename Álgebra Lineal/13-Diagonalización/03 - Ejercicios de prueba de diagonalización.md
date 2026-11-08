---
ramo: "Álgebra Lineal"
tema: "Diagonalización"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Diagonalización]]"
---

# Ejercicios de prueba de diagonalización

Preguntas de interrogaciones y exámenes anteriores. El paso decisivo casi siempre es el mismo: para cada valor propio **repetido**, comparar $\dim E_\lambda$ (variables libres de $A - \lambda I$) con su multiplicidad.

## Ejercicios

### 1. Una que no se puede
Diagonalice, si es posible, $A = \begin{bmatrix} 4 & 0 & -1 \\ 0 & 4 & -1 \\ 1 & 0 & 2 \end{bmatrix}$.

> [!example]- Solución
> Desarrollando por la columna 2: $\det(A - \lambda I) = (4 - \lambda)\big[(4 - \lambda)(2 - \lambda) + 1\big] = (4 - \lambda)(\lambda - 3)^2$.
> $E_4 = \operatorname{Gen}\{\langle 0, 1, 0\rangle\}$. Para $\lambda = 3$: $A - 3I = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 1 & 0 & -1 \end{bmatrix}$ tiene dos pivotes, así que $E_3 = \operatorname{Gen}\{\langle 1, 1, 1\rangle\}$ tiene dimensión $1 < 2$. **No es diagonalizable.**

### 2. Triangular con valores distintos
¿Es diagonalizable $A = \begin{bmatrix} 2 & -3 & 7 \\ 0 & 5 & 1 \\ 0 & 0 & -1 \end{bmatrix}$? Si lo es, diagonalícela.

> [!example]- Solución
> Es triangular con valores propios $2, 5, -1$, distintos: **sí**. Vectores propios: $\lambda = 2$, $\langle 1, 0, 0\rangle$; $\lambda = 5$, de $-3x_1 - 3x_2 = 0$, $\langle -1, 1, 0\rangle$; $\lambda = -1$, de $6x_2 + x_3 = 0$ y $3x_1 - 3x_2 + 7x_3 = 0$, $\langle -15, -1, 6\rangle$.
> $$P = \begin{bmatrix} 1 & -1 & -15 \\ 0 & 1 & -1 \\ 0 & 0 & 6 \end{bmatrix}, \qquad D = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & -1 \end{bmatrix}.$$

### 3. Valor propio doble que sí alcanza
$A = \begin{bmatrix} 2 & 2 & -1 \\ 1 & 3 & -1 \\ -1 & -2 & 2 \end{bmatrix}$ tiene a 1 como valor propio. ¿Es diagonalizable?

> [!example]- Solución
> $A - I = \begin{bmatrix} 1 & 2 & -1 \\ 1 & 2 & -1 \\ -1 & -2 & 1 \end{bmatrix}$ tiene rango 1, así que $\dim E_1 = 2$: $E_1 = \operatorname{Gen}\{\langle -2, 1, 0\rangle, \langle 1, 0, 1\rangle\}$. La traza es 7, así que el tercer valor propio es $7 - 1 - 1 = 5$, con $E_5 = \operatorname{Gen}\{\langle -1, -1, 1\rangle\}$. **Sí**:
> $$P = \begin{bmatrix} -2 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix}, \qquad D = \operatorname{diag}(1, 1, 5).$$

### 4. Diagonalizable según parámetros
¿Para qué $s, t$ es diagonalizable $A = \begin{bmatrix} -1 & s & t \\ 0 & 1 & 0 \\ 0 & -2 & -1 \end{bmatrix}$?

> [!example]- Solución
> Desarrollando por la primera columna, $\det(A - \lambda I) = (-1 - \lambda)^2(1 - \lambda)$: $\lambda = -1$ doble y $\lambda = 1$ simple. Se necesita $\dim E_{-1} = 2$, o sea, $\operatorname{rango}(A + I) = 1$ con $A + I = \begin{bmatrix} 0 & s & t \\ 0 & 2 & 0 \\ 0 & -2 & 0 \end{bmatrix}$. Las filas 2 y 3 son proporcionales a $\langle 0, 1, 0\rangle$; la fila 1 es proporcional a ellas si y solo si $t = 0$. **Diagonalizable si y solo si $t = 0$**, con $s$ cualquiera.

### 5. Una potencia enorme
Diagonalice $A = \begin{bmatrix} 3 & 2 \\ -4 & -3 \end{bmatrix}$ y calcule $A^{911}$.

> [!example]- Solución
> $\det(A - \lambda I) = (3 - \lambda)(-3 - \lambda) + 8 = \lambda^2 - 1$: valores propios $1$ y $-1$. $E_1 = \operatorname{Gen}\{\langle 1, -1\rangle\}$ y $E_{-1} = \operatorname{Gen}\{\langle 1, -2\rangle\}$. $A = PDP^{-1}$ con $P = \begin{bmatrix} 1 & 1 \\ -1 & -2 \end{bmatrix}$ y $D = \operatorname{diag}(1, -1)$.
> Como 911 es impar, $D^{911} = D$, así que $A^{911} = PDP^{-1} = A$.

### 6. Diagonalizar sin ver la matriz
$A$ es de $2 \times 2$, $A\langle 1, -3\rangle = \langle -2, 6\rangle$ y $\langle 1, 2\rangle \in \operatorname{Nul} A$. (a) Dé bases de $\operatorname{Nul} A$ y $\operatorname{Col} A$. (b) Diagonalice $A$. (c) Calcule $A^9$.

> [!example]- Solución
> $A\langle 1, -3\rangle = -2\langle 1, -3\rangle$ y $A\langle 1, 2\rangle = 0\langle 1, 2\rangle$: dos vectores propios LI con valores $-2$ y $0$.
> (a) $\operatorname{Nul} A = E_0 = \operatorname{Gen}\{\langle 1, 2\rangle\}$ (tiene dimensión 1, porque $A \neq 0$). $\operatorname{Col} A$ tiene dimensión $2 - 1 = 1$ y contiene a $\langle -2, 6\rangle$: base $\{\langle -2, 6\rangle\}$.
> (b) $P = \begin{bmatrix} 1 & 1 \\ -3 & 2 \end{bmatrix}$, $D = \operatorname{diag}(-2, 0)$, que da $A = \frac15\begin{bmatrix} -4 & 2 \\ 12 & -6 \end{bmatrix}$.
> (c) $A^9 = P\operatorname{diag}((-2)^9, 0)P^{-1} = (-2)^8A = 256A$.

### 7. Diagonalizar a partir de espacios propios
$A$ es de $3 \times 3$ con valores propios 1 y $-2$, $E_1 = \operatorname{Gen}\{\langle 1, -1, 1\rangle\}$ y $E_{-2} = \{\langle x, y, z\rangle : x + y + z = 0\}$. ¿Es diagonalizable?

> [!example]- Solución
> **Sí**: $\dim E_1 + \dim E_{-2} = 1 + 2 = 3$. Una base de $E_{-2}$ es $\{\langle 1, 0, -1\rangle, \langle 0, 1, -1\rangle\}$, y
> $$P = \begin{bmatrix} 1 & 1 & 0 \\ -1 & 0 & 1 \\ 1 & -1 & -1 \end{bmatrix}, \qquad D = \operatorname{diag}(1, -2, -2).$$

### 8. Dos V o F
(a) Si $A = \begin{bmatrix} a & b \\ 0 & c \end{bmatrix}$ con $b \neq 0$, $A$ es diagonalizable. (b) Si $A\langle 1, 1, 1\rangle = \langle 2, 2, 2\rangle$ y $A\langle 1, 1, 2\rangle = A\langle 0, 1, 0\rangle = \mathbf 0$, $A$ es diagonalizable.

> [!example]- Solución
> (a) **Falso.** Con $a = c = 0$, $b = 1$: $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ tiene solo $\lambda = 0$ (doble) y $\dim E_0 = 1$. (Si $a \neq c$, en cambio, sí sería diagonalizable.)
> (b) **Verdadero.** Son tres vectores propios ($\lambda = 2, 0, 0$) y son LI: $\det\begin{bmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 0 \end{bmatrix} = -1 \neq 0$.

## Preguntas de repaso

> [!question]- ¿Qué atajo se usó en el ejercicio 3 para obtener el tercer valor propio sin factorizar?
> La traza: la suma de los valores propios es la suma de la diagonal. Conociendo dos de ellos (el valor doble), el tercero sale restando.

> [!question]- En el ejercicio 4, ¿por qué no importa el valor de $s$?
> Porque la fila $\langle 0, s, 0\rangle$ (con $t = 0$) es siempre proporcional a $\langle 0, 2, 0\rangle$, así que el rango de $A + I$ sigue siendo 1.

> [!question]- ¿Por qué en el ejercicio 6 no hizo falta encontrar $A$ para calcular $A^9$?
> Porque $A^9 = PD^9P^{-1}$ y $D^9 = \operatorname{diag}((-2)^9, 0) = (-2)^8 D$, así que $A^9 = 256\,PDP^{-1} = 256A$.
