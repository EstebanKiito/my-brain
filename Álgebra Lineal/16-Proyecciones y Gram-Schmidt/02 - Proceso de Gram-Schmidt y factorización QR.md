---
ramo: "Álgebra Lineal"
tema: "Proyecciones y Gram-Schmidt"
tags:
  - algebra-lineal/ortogonalidad
  - algebra-lineal/factorizaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Proyección ortogonal]]"
---

# Proceso de Gram-Schmidt y factorización QR

Las proyecciones necesitan una base **ortogonal**, pero los subespacios suelen venir dados con bases cualesquiera. El **proceso de Gram-Schmidt** fabrica una base ortogonal a partir de cualquier base: toma los vectores uno a uno y a cada uno le resta su sombra sobre los anteriores. Escrito con matrices, el proceso es la **factorización QR**, otra factorización clave del curso.

## La idea con dos vectores

$W = \operatorname{Gen}\{\mathbf x_1, \mathbf x_2\}$ con $\mathbf x_1 = \langle 3, 6, 0\rangle$ y $\mathbf x_2 = \langle 1, 2, 2\rangle$, que no son ortogonales. Se deja $\mathbf v_1 = \mathbf x_1$ y a $\mathbf x_2$ se le quita su componente en la dirección de $\mathbf v_1$:

$$
\mathbf v_2 = \mathbf x_2 - \operatorname{proy}_{\mathbf v_1}\mathbf x_2 = \langle 1, 2, 2\rangle - \frac{15}{45}\langle 3, 6, 0\rangle = \langle 0, 0, 2\rangle .
$$

$\mathbf v_2$ sigue en $W$ (es combinación de $\mathbf x_1$ y $\mathbf x_2$) y es ortogonal a $\mathbf v_1$: $\{\mathbf v_1, \mathbf v_2\}$ es una base ortogonal de $W$. Ahora se puede proyectar: para $\mathbf y = \langle 0, 4, 2\rangle$, $\operatorname{proy}_W\mathbf y = \frac{24}{45}\mathbf v_1 + \frac44\mathbf v_2 = \langle \tfrac85, \tfrac{16}{5}, 2\rangle$.

![Primer paso de Gram-Schmidt](adjuntos/Primer%20paso%20de%20Gram-Schmidt.png)

> [!example]- Transcripción de la imagen
> En $\mathbb{R}^3$, el plano $W$ generado por $\mathbf x_1$ y $\mathbf x_2$. Sobre la dirección de $\mathbf v_1 = \mathbf x_1$ se marca $\mathbf p$, la proyección de $\mathbf x_2$. El vector $\mathbf v_2 = \mathbf x_2 - \mathbf p$ sale del origen dentro del plano, perpendicular a $\mathbf v_1$.

## El proceso general

> [!tip] Proceso de Gram-Schmidt
> Dada una base $\{\mathbf x_1, \dots, \mathbf x_p\}$ de $W$, se definen
> $$\begin{aligned} \mathbf v_1 &= \mathbf x_1 \\ \mathbf v_2 &= \mathbf x_2 - \frac{\mathbf x_2 \cdot \mathbf v_1}{\mathbf v_1 \cdot \mathbf v_1}\mathbf v_1 \\ \mathbf v_3 &= \mathbf x_3 - \frac{\mathbf x_3 \cdot \mathbf v_1}{\mathbf v_1 \cdot \mathbf v_1}\mathbf v_1 - \frac{\mathbf x_3 \cdot \mathbf v_2}{\mathbf v_2 \cdot \mathbf v_2}\mathbf v_2 \\ &\ \ \vdots \\ \mathbf v_p &= \mathbf x_p - \operatorname{proy}_{\operatorname{Gen}\{\mathbf v_1, \dots, \mathbf v_{p-1}\}}\mathbf x_p . \end{aligned}$$
> Entonces $\{\mathbf v_1, \dots, \mathbf v_p\}$ es una base ortogonal de $W$, y además $\operatorname{Gen}\{\mathbf v_1, \dots, \mathbf v_k\} = \operatorname{Gen}\{\mathbf x_1, \dots, \mathbf x_k\}$ para cada $k$.

Para una base **ortonormal**, se normaliza al final: $\mathbf u_k = \mathbf v_k / \|\mathbf v_k\|$.

> [!tip] Trucos de cálculo
> - Se puede **escalar** cualquier $\mathbf v_k$ apenas se obtiene (por ejemplo, para eliminar fracciones): la ortogonalidad no cambia y las proyecciones siguientes tampoco.
> - Cada $\mathbf x_k$ se proyecta sobre los $\mathbf v$ ya obtenidos, **no** sobre los $\mathbf x$ anteriores.

**Ejemplo.** $\mathbf x_1 = \langle 1, 1, 1, 1\rangle$, $\mathbf x_2 = \langle 0, 1, 1, 1\rangle$, $\mathbf x_3 = \langle 0, 0, 1, 1\rangle$.
- $\mathbf v_1 = \langle 1, 1, 1, 1\rangle$.
- $\mathbf x_2 - \tfrac34\mathbf v_1 = \langle -\tfrac34, \tfrac14, \tfrac14, \tfrac14\rangle$; escalando por 4, $\mathbf v_2 = \langle -3, 1, 1, 1\rangle$.
- $\mathbf x_3 - \tfrac24\mathbf v_1 - \tfrac{2}{12}\mathbf v_2 = \langle 0, -\tfrac23, \tfrac13, \tfrac13\rangle$; escalando por 3, $\mathbf v_3 = \langle 0, -2, 1, 1\rangle$.

Se comprueba que los tres productos punto entre ellos son cero.

## Factorización QR

> [!tip] Teorema (factorización QR)
> Si $A$ es de $m \times n$ con columnas LI, entonces $A = QR$ donde
> - $Q$ es de $m \times n$ con columnas ortonormales que forman una base de $\operatorname{Col} A$;
> - $R$ es de $n \times n$, triangular superior, invertible y con diagonal positiva.

**Cómo se calcula.** $Q$ sale de Gram-Schmidt aplicado a las columnas de $A$, normalizado. Como $Q^TQ = I$, multiplicando $A = QR$ por $Q^T$:
$$R = Q^TA .$$
$R$ es triangular porque cada columna $\mathbf x_k$ de $A$ es combinación de $\mathbf u_1, \dots, \mathbf u_k$ solamente.

**Ejemplo.** Con las columnas del ejemplo anterior, normalizando $\mathbf v_1, \mathbf v_2, \mathbf v_3$ (de normas $2$, $\sqrt{12}$ y $\sqrt6$):
$$Q = \begin{bmatrix} \frac12 & -\frac{3}{\sqrt{12}} & 0 \\ \frac12 & \frac{1}{\sqrt{12}} & -\frac{2}{\sqrt6} \\ \frac12 & \frac{1}{\sqrt{12}} & \frac{1}{\sqrt6} \\ \frac12 & \frac{1}{\sqrt{12}} & \frac{1}{\sqrt6} \end{bmatrix}, \qquad R = Q^TA = \begin{bmatrix} 2 & \frac32 & 1 \\ 0 & \frac{3}{\sqrt{12}} & \frac{2}{\sqrt{12}} \\ 0 & 0 & \frac{2}{\sqrt6} \end{bmatrix}.$$

> [!warning] QR exige columnas independientes
> Si las columnas de $A$ son LD, en algún paso de Gram-Schmidt aparece $\mathbf v_k = \mathbf 0$ (no se puede normalizar) y $R$ no sería invertible. Eso indica que la columna $k$ sobraba.

## Preguntas de repaso

> [!question]- Aplique Gram-Schmidt a $\langle 1, 2, 0\rangle$ y $\langle 2, 3, 1\rangle$.
> $\mathbf v_1 = \langle 1, 2, 0\rangle$ y $\mathbf v_2 = \langle 2, 3, 1\rangle - \tfrac85\langle 1, 2, 0\rangle = \langle \tfrac25, -\tfrac15, 1\rangle$, o escalado, $\langle 2, -1, 5\rangle$.

> [!question]- ¿Por qué cada $\mathbf v_k$ de Gram-Schmidt sigue en $W$?
> Porque es $\mathbf x_k$ menos una combinación de $\mathbf v_1, \dots, \mathbf v_{k-1}$, que por inducción están en $\operatorname{Gen}\{\mathbf x_1, \dots, \mathbf x_{k-1}\} \subseteq W$.

> [!question]- Si ya se tiene $Q$, ¿cómo se obtiene $R$ sin despejar nada más?
> Con $R = Q^TA$, porque $Q^TQ = I$.

> [!question]- ¿Qué pasa si en Gram-Schmidt se proyecta $\mathbf x_3$ sobre $\mathbf x_1$ y $\mathbf x_2$ en vez de sobre $\mathbf v_1$ y $\mathbf v_2$?
> El resultado en general no es ortogonal a los anteriores, porque la fórmula de proyección como suma solo vale con una base ortogonal, y $\{\mathbf x_1, \mathbf x_2\}$ no lo es.
