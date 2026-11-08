---
ramo: "Álgebra Lineal"
tema: "Cholesky y descomposición en valores singulares"
tags:
  - algebra-lineal/factorizaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Formas cuadráticas]]"
  - "[[05 - Factorización LU]]"
---

# Factorización de Cholesky

Las matrices simétricas definidas positivas son las que aparecen en mínimos cuadrados ($A^TA$ con columnas LI), en estadística (covarianzas) y en optimización. Para ellas existe una versión de la LU especialmente simple y barata: $A = R^TR$, con un solo factor triangular. Es la **factorización de Cholesky**, que se usa para resolver sistemas con esas matrices en la mitad de operaciones que la LU.

## Definición y existencia

> [!tip] Definición
> Una **factorización de Cholesky** de $A$ es $A = R^TR$ con $R$ **triangular superior**, invertible y con **diagonal positiva**.

> [!tip] Teorema
> $A$ tiene factorización de Cholesky si y solo si $A$ es **simétrica y definida positiva**.

**Por qué es necesario.** Si $A = R^TR$, entonces $A^T = R^TR = A$ (simétrica) y $\mathbf x^TA\mathbf x = \mathbf x^TR^TR\mathbf x = \|R\mathbf x\|^2 > 0$ para $\mathbf x \neq \mathbf 0$, porque $R$ es invertible (definida positiva).

**Por qué es suficiente.** Con $A = PDP^T$ y todos los $\lambda_i > 0$, sea $B = D^{1/2}P^T$ (con $D^{1/2}$ la diagonal de las raíces). Entonces $A = B^TB$ y $B$ tiene columnas LI. Factorizando $B = QR$: $A = R^TQ^TQR = R^TR$.

## Cómo calcularla

**Opción 1: igualar entradas.** Se escribe $R$ con incógnitas, se multiplica $R^TR$ y se iguala a $A$ entrada por entrada, de arriba a abajo. Funciona bien en $2 \times 2$.

**Opción 2: escalonar.**

> [!tip] Algoritmo
> 1. Llevar $A$ a forma escalonada $U$ usando **solo reemplazos** (sin intercambios ni escalamientos).
> 2. Dividir cada fila de $U$ por la **raíz cuadrada de su pivote**. El resultado es $R$.

Funciona porque $A = LU$ y, para $A$ simétrica, $U = DL^T$ con $D$ la diagonal de pivotes; entonces $A = LDL^T = (D^{1/2}L^T)^T(D^{1/2}L^T)$, y $R = D^{1/2}L^T = D^{-1/2}U$: cada fila de $U$ dividida por la raíz de su pivote.

**Ejemplo.** $A = \begin{bmatrix} 4 & 8 & -4 \\ 8 & 17 & -5 \\ -4 & -5 & 17 \end{bmatrix}$. $F_2 - 2F_1$ da $[0\ 1\ 3]$; $F_3 + F_1$ da $[0\ 3\ 13]$; $F_3 - 3F_2$ da $[0\ 0\ 4]$:
$$U = \begin{bmatrix} 4 & 8 & -4 \\ 0 & 1 & 3 \\ 0 & 0 & 4 \end{bmatrix} \quad\Longrightarrow\quad R = \begin{bmatrix} 2 & 4 & -2 \\ 0 & 1 & 3 \\ 0 & 0 & 2 \end{bmatrix}$$
(filas divididas por $\sqrt4$, $\sqrt1$ y $\sqrt4$). Se comprueba que $R^TR = A$.

**Ejemplo con raíces.** $A = \begin{bmatrix} 6 & -2 & -1 \\ -2 & 6 & -1 \\ -1 & -1 & 5 \end{bmatrix}$ (valores propios 8, 6, 3: definida positiva). Escalonando sin escalar, los pivotes son $6$, $\tfrac{16}{3}$ y $\tfrac92$, y
$$R = \begin{bmatrix} \sqrt6 & -\frac{\sqrt6}{3} & -\frac{\sqrt6}{6} \\ 0 & \frac{4\sqrt3}{3} & -\frac{\sqrt3}{3} \\ 0 & 0 & \frac{3\sqrt2}{2} \end{bmatrix}.$$

> [!warning] Si aparece un pivote negativo o cero
> Entonces $A$ **no** es definida positiva y no tiene Cholesky. El algoritmo sirve también como prueba: una simétrica es definida positiva si y solo si al escalonarla sin intercambios todos los pivotes son positivos.

## Preguntas de repaso

> [!question]- ¿Tiene factorización de Cholesky $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$?
> No. Es simétrica, pero sus valores propios son 3 y $-1$: no es definida positiva. Al escalonar, el segundo pivote es $1 - 4 = -3 < 0$.

> [!question]- Encuentre la factorización de Cholesky de $\begin{bmatrix} 9 & 3 \\ 3 & 5 \end{bmatrix}$.
> $F_2 - \tfrac13F_1$ da $U = \begin{bmatrix} 9 & 3 \\ 0 & 4 \end{bmatrix}$, y dividiendo por $3$ y $2$: $R = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$. Comprobación: $R^TR = \begin{bmatrix} 9 & 3 \\ 3 & 5 \end{bmatrix}$.

> [!question]- ¿Por qué el algoritmo prohíbe escalar filas durante la eliminación?
> Porque el paso final divide por la raíz de cada pivote; si los pivotes se alteraron escalando, $U$ deja de ser $DL^T$ y el resultado no cumple $R^TR = A$.

> [!question]- Si $A$ tiene columnas LI, ¿tiene Cholesky la matriz $A^TA$?
> Sí: es simétrica, y $\mathbf x^TA^TA\mathbf x = \|A\mathbf x\|^2 > 0$ para $\mathbf x \neq \mathbf 0$ porque $A\mathbf x \neq \mathbf 0$.
