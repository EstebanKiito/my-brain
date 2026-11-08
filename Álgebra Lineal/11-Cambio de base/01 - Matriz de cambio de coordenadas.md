---
ramo: "Álgebra Lineal"
tema: "Cambio de base"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[01 - Sistemas de coordenadas]]"
  - "[[02 - Dimensión]]"
---

# Matriz de cambio de coordenadas

Un mismo vector tiene coordenadas distintas según la base que se use, igual que un punto del plano se describe distinto en ejes rotados. Muchas veces el problema está planteado en una base y es más fácil resolverlo en otra (más adelante, la base de vectores propios hace que una matriz se vuelva diagonal). La **matriz de cambio de coordenadas** traduce de una base a otra con una sola multiplicación.

![Dos sistemas de coordenadas en el mismo espacio](adjuntos/Dos%20sistemas%20de%20coordenadas%20en%20el%20mismo%20espacio.png)

> [!example]- Transcripción de la imagen
> El mismo vector $\mathbf x$ dibujado sobre dos cuadrículas distintas del plano, correspondientes al ejemplo de esta nota. (a) Con la base $\{\mathbf b_1, \mathbf b_2\}$: el paralelogramo sombreado muestra $\mathbf x = 3\mathbf b_1 + \mathbf b_2$. (b) Con la base $\{\mathbf c_1, \mathbf c_2\}$, de cuadrícula más fina: el mismo $\mathbf x$ es $6\mathbf c_1 + 4\mathbf c_2$. El punto es el mismo; los números que lo describen cambian.

## Idea con un ejemplo

Sean $\mathcal B = \{\mathbf b_1, \mathbf b_2\}$ y $\mathcal C = \{\mathbf c_1, \mathbf c_2\}$ bases de $V$ con
$$\mathbf b_1 = 4\mathbf c_1 + \mathbf c_2, \qquad \mathbf b_2 = -6\mathbf c_1 + \mathbf c_2,$$
y $\mathbf x = 3\mathbf b_1 + \mathbf b_2$, es decir, $[\mathbf x]_{\mathcal B} = \langle 3, 1\rangle$. Por linealidad de las coordenadas:

$$
[\mathbf x]_{\mathcal C} = 3[\mathbf b_1]_{\mathcal C} + 1[\mathbf b_2]_{\mathcal C} = \begin{bmatrix} 4 & -6 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \end{bmatrix}.
$$

La matriz que apareció tiene como columnas las **$\mathcal C$-coordenadas de los vectores de $\mathcal B$**.

## El teorema

> [!tip] Teorema
> Sean $\mathcal B = \{\mathbf b_1, \dots, \mathbf b_n\}$ y $\mathcal C = \{\mathbf c_1, \dots, \mathbf c_n\}$ bases de $V$. Existe una única matriz $P_{\mathcal C \leftarrow \mathcal B}$ de $n \times n$ tal que
> $$[\mathbf x]_{\mathcal C} = P_{\mathcal C \leftarrow \mathcal B}\,[\mathbf x]_{\mathcal B} \quad \text{para todo } \mathbf x \in V,$$
> y es
> $$P_{\mathcal C \leftarrow \mathcal B} = \big[\,[\mathbf b_1]_{\mathcal C}\ \ [\mathbf b_2]_{\mathcal C}\ \ \cdots\ \ [\mathbf b_n]_{\mathcal C}\,\big].$$

**Cómo recordar la notación.** $P_{\mathcal C \leftarrow \mathcal B}$ "recibe" coordenadas en $\mathcal B$ por la derecha y "entrega" coordenadas en $\mathcal C$. Las columnas son los vectores de la base **de partida** ($\mathcal B$) escritos en la base **de llegada** ($\mathcal C$).

![Diagrama de la matriz de cambio de coordenadas](adjuntos/Diagrama%20de%20la%20matriz%20de%20cambio%20de%20coordenadas.png)

> [!example]- Transcripción de la imagen
> Arriba, el espacio $V$ con un vector $\mathbf x$. Dos flechas bajan a dos copias de $\mathbb{R}^n$: una calcula $[\mathbf x]_{\mathcal C}$ y la otra $[\mathbf x]_{\mathcal B}$. Una flecha horizontal, "multiplicación por $P_{\mathcal C \leftarrow \mathcal B}$", va de $[\mathbf x]_{\mathcal B}$ a $[\mathbf x]_{\mathcal C}$. El triángulo conmuta: da lo mismo calcular directamente $[\mathbf x]_{\mathcal C}$ o pasar por $[\mathbf x]_{\mathcal B}$ y multiplicar.

## Inversa

Las columnas de $P_{\mathcal C \leftarrow \mathcal B}$ son LI (son las coordenadas de una base, y el isomorfismo conserva la independencia), así que la matriz es invertible, y deshacer el cambio es ir en el otro sentido:

> [!tip] Propiedad
> $$\left(P_{\mathcal C \leftarrow \mathcal B}\right)^{-1} = P_{\mathcal B \leftarrow \mathcal C}.$$

> [!warning] El sentido del cambio
> Es fácil confundir $P_{\mathcal C \leftarrow \mathcal B}$ con su inversa. Antes de usarla, conviene verificar con un vector de la base: $P_{\mathcal C \leftarrow \mathcal B}[\mathbf b_1]_{\mathcal B} = P_{\mathcal C \leftarrow \mathcal B}\mathbf e_1$ es la primera columna, y debe ser $[\mathbf b_1]_{\mathcal C}$.

## Preguntas de repaso

> [!question]- Si $\mathbf b_1 = \mathbf c_1 + 2\mathbf c_2$ y $\mathbf b_2 = 3\mathbf c_2$, ¿cuál es $P_{\mathcal C \leftarrow \mathcal B}$ y cuánto vale $[\mathbf x]_{\mathcal C}$ si $[\mathbf x]_{\mathcal B} = \langle 1, -1\rangle$?
> $P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & 0 \\ 2 & 3 \end{bmatrix}$ (columnas $[\mathbf b_1]_{\mathcal C}$ y $[\mathbf b_2]_{\mathcal C}$). $[\mathbf x]_{\mathcal C} = \langle 1, 2 - 3\rangle = \langle 1, -1\rangle$.

> [!question]- ¿Por qué toda matriz de cambio de base es invertible?
> Porque sus columnas son las coordenadas de los $n$ vectores de una base, que son LI; en coordenadas siguen siendo $n$ vectores LI de $\mathbb{R}^n$. Además, el cambio inverso existe y es $P_{\mathcal B \leftarrow \mathcal C}$.

> [!question]- Si $\mathcal B = \mathcal C$, ¿cuál es $P_{\mathcal C \leftarrow \mathcal B}$?
> La identidad: cada $\mathbf b_j$ tiene coordenadas $\mathbf e_j$ en su propia base.

> [!question]- V o F: si $[\mathbf x]_{\mathcal B_2}$ no es un vector canónico, entonces $[\mathbf x]_{\mathcal B_1}$ tampoco, con $\mathcal B_1 = \{\mathbf u, \mathbf v\}$ y $\mathcal B_2 = \{\mathbf u + 3\mathbf v, 2\mathbf u + 4\mathbf v\}$.
> Falso. Con $\mathbf x = \mathbf v$: $[\mathbf x]_{\mathcal B_1} = \langle 0, 1\rangle$ es canónico, pero $\mathbf v = (\mathbf u + 3\mathbf v) - \tfrac12(2\mathbf u + 4\mathbf v)$, así que $[\mathbf x]_{\mathcal B_2} = \langle 1, -\tfrac12\rangle$ no lo es.
