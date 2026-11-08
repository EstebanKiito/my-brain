---
ramo: "Álgebra Lineal"
tema: "Proyecciones y Gram-Schmidt"
tags:
  - algebra-lineal/ortogonalidad
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Proceso de Gram-Schmidt y factorización QR]]"
---

# Ejercicios de prueba de proyecciones y Gram-Schmidt

Preguntas de exámenes e interrogaciones anteriores. El esquema se repite: verificar si la base es ortogonal (si no, Gram-Schmidt), proyectar sumando proyecciones y, si se pide distancia, calcular la norma de $\mathbf y - \hat{\mathbf y}$.

## Ejercicios

### 1. Descomposición respecto de un plano y distancia
$\mathbf y = \langle 5, -9, 5\rangle$, $\mathbf u_1 = \langle -3, -5, 1\rangle$, $\mathbf u_2 = \langle -3, 2, 1\rangle$ y $P = \operatorname{Gen}\{\mathbf u_1, \mathbf u_2\}$. (a) Escriba $\mathbf y$ como suma de un vector de $P$ y otro de $P^\perp$. (b) Encuentre la distancia de $\mathbf y$ a $P$.

> [!example]- Solución
> $\mathbf u_1 \cdot \mathbf u_2 = 9 - 10 + 1 = 0$: base ortogonal.
> (a) $\frac{\mathbf y \cdot \mathbf u_1}{\mathbf u_1 \cdot \mathbf u_1} = \frac{-15 + 45 + 5}{35} = 1$ y $\frac{\mathbf y \cdot \mathbf u_2}{\mathbf u_2 \cdot \mathbf u_2} = \frac{-15 - 18 + 5}{14} = -2$. Entonces $\hat{\mathbf y} = \mathbf u_1 - 2\mathbf u_2 = \langle 3, -9, -1\rangle \in P$ y $\mathbf z = \mathbf y - \hat{\mathbf y} = \langle 2, 0, 6\rangle \in P^\perp$.
> (b) $\|\mathbf z\| = \sqrt{4 + 36} = 2\sqrt{10}$.

### 2. Proyección y distancia en un hiperplano de $\mathbb{R}^4$
$W = \{\langle x, y, z, t\rangle : x - y - z = 0\}$ tiene la base ortogonal $\{\langle 1, 1, 0, 0\rangle, \langle 0, 0, 0, 1\rangle, \langle 1, -1, 2, 0\rangle\}$. (a) Proyecte $\mathbf x = \langle 1, 1, 1, 1\rangle$ sobre $W$. (b) Encuentre la distancia de $\mathbf x$ a $W$.

> [!example]- Solución
> (a) Los coeficientes son $\tfrac22 = 1$, $\tfrac11 = 1$ y $\tfrac{1 - 1 + 2}{6} = \tfrac13$:
> $$\operatorname{proy}_W\mathbf x = \langle 1, 1, 0, 0\rangle + \langle 0, 0, 0, 1\rangle + \tfrac13\langle 1, -1, 2, 0\rangle = \langle \tfrac43, \tfrac23, \tfrac23, 1\rangle .$$
> (b) $\mathbf x - \operatorname{proy}_W\mathbf x = \langle -\tfrac13, \tfrac13, \tfrac13, 0\rangle$, de norma $\tfrac{\sqrt3}{3}$.
> Atajo: $W^\perp = \operatorname{Gen}\{\langle 1, -1, -1, 0\rangle\}$, y la distancia es la norma de la proyección sobre ese vector: $\frac{|1 - 1 - 1|}{\sqrt3} = \tfrac{1}{\sqrt3}$.

### 3. Proyección sobre un subespacio de $\mathbb{R}^4$
(a) Pruebe que $\mathbf u_1 = \langle 0, 1, 0, -1\rangle$, $\mathbf u_2 = \langle 1, 1, 1, 1\rangle$ y $\mathbf u_3 = \langle -1, 0, 1, 0\rangle$ son ortogonales. (b) Proyecte $\mathbf v = \langle 4, -2, -3, 2\rangle$ sobre $W = \operatorname{Gen}\{\mathbf u_1, \mathbf u_2, \mathbf u_3\}$.

> [!example]- Solución
> (a) $\mathbf u_1 \cdot \mathbf u_2 = 0 + 1 + 0 - 1 = 0$, $\mathbf u_1 \cdot \mathbf u_3 = 0$ y $\mathbf u_2 \cdot \mathbf u_3 = -1 + 0 + 1 + 0 = 0$.
> (b) Coeficientes: $\frac{-2 - 2}{2} = -2$, $\frac{4 - 2 - 3 + 2}{4} = \tfrac14$ y $\frac{-4 - 3}{2} = -\tfrac72$:
> $$\operatorname{proy}_W\mathbf v = -2\mathbf u_1 + \tfrac14\mathbf u_2 - \tfrac72\mathbf u_3 = \langle \tfrac{15}{4}, -\tfrac74, -\tfrac{13}{4}, \tfrac94\rangle .$$

### 4. Gram-Schmidt y vector más cercano
$W = \operatorname{Gen}\{\langle 1, 2, 0\rangle, \langle 2, 3, 1\rangle\}$. (a) Encuentre una base ortonormal de $W$. (b) Encuentre el vector de $W$ más cercano a $\mathbf y = \langle 1, 0, 1\rangle$.

> [!example]- Solución
> (a) $\mathbf v_1 = \langle 1, 2, 0\rangle$ y $\mathbf v_2 = \langle 2, 3, 1\rangle - \tfrac85\mathbf v_1 = \langle \tfrac25, -\tfrac15, 1\rangle$, que escalado es $\langle 2, -1, 5\rangle$. Normalizando: $\left\{\tfrac{1}{\sqrt5}\langle 1, 2, 0\rangle,\ \tfrac{1}{\sqrt{30}}\langle 2, -1, 5\rangle\right\}$.
> (b) Es $\operatorname{proy}_W\mathbf y = \tfrac15\langle 1, 2, 0\rangle + \tfrac{7}{30}\langle 2, -1, 5\rangle = \langle \tfrac23, \tfrac16, \tfrac76\rangle$ (los coeficientes son $\frac{1}{5}$ y $\frac{2 + 5}{30}$).

### 5. Completar a una base ortonormal de $\mathbb{R}^3$
Encuentre una base ortonormal de $\mathbb{R}^3$ a partir de $\mathbf v_1 = \langle 1, 2, 3\rangle$ y $\mathbf v_2 = \langle 0, 1, 0\rangle$.

> [!example]- Solución
> Gram-Schmidt: $\mathbf w_2 = \mathbf v_2 - \tfrac{2}{14}\mathbf v_1 = \langle -\tfrac17, \tfrac57, -\tfrac37\rangle$, o escalado $\langle -1, 5, -3\rangle$. Un tercer vector ortogonal a ambos está en $\operatorname{Nul}\begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 0 \end{bmatrix} = \operatorname{Gen}\{\langle -3, 0, 1\rangle\}$. Normalizando:
> $$\left\{\tfrac{1}{\sqrt{14}}\langle 1, 2, 3\rangle,\ \tfrac{1}{\sqrt{35}}\langle -1, 5, -3\rangle,\ \tfrac{1}{\sqrt{10}}\langle -3, 0, 1\rangle\right\}.$$

### 6. Base ortogonal de un plano y distancia de un punto
$\Pi$ es el plano $s\langle 5, -2, 1\rangle + t\langle 7, 2, -1\rangle$. (a) Encuentre una base ortogonal de $\Pi$. (b) Encuentre la distancia de $\mathbf p = (-1, -5, 10)$ a $\Pi$.

> [!example]- Solución
> (a) $\mathbf v_1 = \langle 5, -2, 1\rangle$ y $\mathbf v_2 = \langle 7, 2, -1\rangle - \tfrac{30}{30}\mathbf v_1 = \langle 2, 4, -2\rangle$.
> (b) $\operatorname{proy}_\Pi\mathbf p = \frac{-5 + 10 + 10}{30}\mathbf v_1 + \frac{-2 - 20 - 20}{24}\mathbf v_2 = \tfrac12\mathbf v_1 - \tfrac74\mathbf v_2 = \langle -1, -8, 4\rangle$. Entonces $\mathbf p - \operatorname{proy}_\Pi\mathbf p = \langle 0, 3, 6\rangle$, y la distancia es $\sqrt{45} = 3\sqrt5$.

### 7. Dos V o F
(a) Si $U$ es un subespacio de dimensión 1 en $\mathbb{R}^3$ y $P$ la matriz de proyección sobre $U$, $P$ es invertible. (b) La menor norma entre los vectores del hiperplano $x_1 + x_2 - x_4 = 1$ de $\mathbb{R}^4$ es 1.

> [!example]- Solución
> (a) **Falso.** $P$ tiene rango $\dim U = 1 < 3$; por ejemplo, para $U = \operatorname{Gen}\{\mathbf e_1\}$, $P = \operatorname{diag}(1, 0, 0)$.
> (b) **Falso.** El punto del hiperplano más cercano al origen está en la dirección del normal $\mathbf n = \langle 1, 1, 0, -1\rangle$: es $\frac{1}{\mathbf n \cdot \mathbf n}\mathbf n = \tfrac13\langle 1, 1, 0, -1\rangle$, de norma $\tfrac{1}{\sqrt3} \neq 1$.

## Preguntas de repaso

> [!question]- ¿Qué se verifica siempre antes de usar la fórmula de proyección como suma?
> Que la base sea ortogonal. Si no lo es, se aplica Gram-Schmidt primero.

> [!question]- En el ejercicio 2, ¿por qué el atajo con $W^\perp$ da la misma distancia?
> Porque $\mathbf x = \operatorname{proy}_W\mathbf x + \operatorname{proy}_{W^\perp}\mathbf x$, y la distancia a $W$ es la norma de la parte en $W^\perp$. Si $W^\perp$ es una recta, esa parte se calcula con un solo producto punto.

> [!question]- En el ejercicio 5, ¿por qué el tercer vector se buscó con un espacio nulo y no con Gram-Schmidt?
> Porque no había un tercer vector de partida. Lo ortogonal a $\mathbf v_1$ y $\mathbf v_2$ es el complemento de su generado, que se calcula como espacio nulo con ellos como filas.
