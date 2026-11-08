---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/matrices
  - origen/complemento
prerrequisitos:
  - "[[01 - Operaciones con matrices]]"
---

# Inversa de una matriz

Con números, $ax = b$ se resuelve dividiendo: $x = a^{-1}b$, siempre que $a \neq 0$. Con matrices no existe la división, pero algunas matrices cuadradas tienen una **inversa** que cumple el mismo papel. Cuando existe, resuelve cualquier sistema $A\mathbf x = \mathbf b$ de una vez y permite despejar en ecuaciones matriciales.

## Definición

> [!tip] Definición
> Una matriz $A$ de $n \times n$ es **invertible** (o no singular) si existe $C$ de $n \times n$ tal que
> $$CA = I_n \qquad\text{y}\qquad AC = I_n .$$
> Esa $C$ es única, se llama la **inversa** de $A$ y se denota $A^{-1}$. Una matriz sin inversa es **singular**.

La unicidad es fácil: si $B$ y $C$ son inversas, $B = BI = B(AC) = (BA)C = IC = C$.

**Ejemplo.** $C = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}$ es la inversa de $A = \begin{bmatrix} 2 & 5 \\ -3 & -7 \end{bmatrix}$: al multiplicar se obtiene $AC = CA = I$.

Solo las matrices **cuadradas** pueden tener inversa (de ambos lados). Una matriz de $3 \times 5$ puede tener una "inversa por un lado", pero no una inversa en este sentido.

## El caso $2 \times 2$

> [!tip] Teorema
> Sea $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. Si $ad - bc \neq 0$, $A$ es invertible y
> $$A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.$$
> Si $ad - bc = 0$, $A$ no es invertible.

La receta: intercambiar la diagonal, cambiar el signo de la otra diagonal y dividir por $ad - bc$, que es el **determinante** de $A$ (tema siguiente). Por ejemplo,

$$
\begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix}^{-1} = \frac{1}{18 - 20}\begin{bmatrix} 6 & -4 \\ -5 & 3 \end{bmatrix} = \begin{bmatrix} -3 & 2 \\ \tfrac52 & -\tfrac32 \end{bmatrix}.
$$

## Inversa y sistemas

> [!tip] Teorema
> Si $A$ es invertible de $n \times n$, para cada $\mathbf b \in \mathbb{R}^n$ el sistema $A\mathbf x = \mathbf b$ tiene la **solución única** $\mathbf x = A^{-1}\mathbf b$.

Existe porque $A(A^{-1}\mathbf b) = \mathbf b$, y es única porque si $A\mathbf u = \mathbf b$, multiplicando por $A^{-1}$ a la izquierda se obtiene $\mathbf u = A^{-1}\mathbf b$.

**Ejemplo.** $3x_1 + 4x_2 = 3$, $5x_1 + 6x_2 = 7$: $\mathbf x = \begin{bmatrix} -3 & 2 \\ \tfrac52 & -\tfrac32 \end{bmatrix}\begin{bmatrix}3\\7\end{bmatrix} = \begin{bmatrix}5\\-3\end{bmatrix}$.

En la práctica, para **un** sistema es más barato escalonar que calcular $A^{-1}$. La inversa conviene en razonamientos y cuando hay muchos lados derechos (aunque para eso la factorización LU es todavía mejor).

## Propiedades

> [!tip] Teorema
> Si $A$ y $B$ son invertibles de $n \times n$:
> 1. $A^{-1}$ es invertible y $(A^{-1})^{-1} = A$.
> 2. $AB$ es invertible y $(AB)^{-1} = B^{-1}A^{-1}$ (orden inverso).
> 3. $A^T$ es invertible y $(A^T)^{-1} = (A^{-1})^T$.

La 2 se comprueba multiplicando: $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AA^{-1} = I$. Es como ponerse y quitarse calcetines y zapatos: lo último que se puso es lo primero que se quita. Se generaliza: $(A_1A_2\cdots A_k)^{-1} = A_k^{-1}\cdots A_1^{-1}$.

## Despejar en ecuaciones matriciales

Se multiplica **por el mismo lado** en ambos miembros, solo por matrices invertibles, y se usan las reglas de transpuesta e inversa.

**Ejemplo.** Si $A, B$ son invertibles y $B^TX^TA^{-1} = I$, se multiplica a la derecha por $A$: $B^TX^T = A$. A la izquierda por $(B^T)^{-1}$: $X^T = (B^T)^{-1}A = (B^{-1})^TA$. Transponiendo: $X = A^TB^{-1}$, y entonces $X^{-1} = (B^{-1})^{-1}(A^T)^{-1} = B(A^{-1})^T$.

> [!warning] Errores típicos al despejar
> - Escribir $\frac{B}{A}$: no existe; $A^{-1}B$ y $BA^{-1}$ son distintos.
> - "Pasar" una matriz de un lado al otro sin respetar el lado: de $AX = B$ sale $X = A^{-1}B$, no $X = BA^{-1}$.
> - Usar $(AB)^{-1} = A^{-1}B^{-1}$ o $(AB)^T = A^TB^T$: ambas van en orden inverso.
> - $(A + B)^{-1} \neq A^{-1} + B^{-1}$; ni siquiera hay garantía de que $A + B$ sea invertible.

## Preguntas de repaso

> [!question]- Calcule la inversa de $\begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$ y úsela para resolver $2x + y = 1$, $5x + 3y = 4$.
> $ad - bc = 1$, así que la inversa es $\begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}$ y $\mathbf x = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}\begin{bmatrix}1\\4\end{bmatrix} = \begin{bmatrix}-1\\3\end{bmatrix}$.

> [!question]- Si $P^2 = P$ y $R = 2P - I$, ¿es $R$ invertible?
> Sí: $R^2 = 4P^2 - 4P + I = I$, así que $R^{-1} = R$.

> [!question]- Si $B^2 - 2B - 3I = 0$, ¿es $B$ invertible? ¿Cuál es su inversa?
> Sí. $B(B - 2I) = 3I$, así que $B\cdot\tfrac13(B - 2I) = I$ y, como el factor conmuta con $B$, también por la izquierda. $B^{-1} = \tfrac13(B - 2I)$.

> [!question]- Despeje $X$ de $A^{-1}XB^T = A^{-1}(B^2)^T$, con $A$ y $B$ invertibles.
> A la izquierda por $A$: $XB^T = (B^2)^T = B^TB^T$. A la derecha por $(B^T)^{-1}$: $X = B^T$.

> [!question]- ¿Por qué $(AB)^{-1}$ es $B^{-1}A^{-1}$ y no $A^{-1}B^{-1}$?
> Porque al multiplicar $AB$ por $B^{-1}A^{-1}$, la $B$ queda pegada a $B^{-1}$ y se cancela, y después $A$ con $A^{-1}$. Con $A^{-1}B^{-1}$ las matrices quedan intercaladas ($ABA^{-1}B^{-1}$) y, como no conmutan, no se cancelan.
