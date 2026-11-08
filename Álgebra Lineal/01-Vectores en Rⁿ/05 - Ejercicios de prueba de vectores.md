---
ramo: "Álgebra Lineal"
tema: "Vectores en Rⁿ"
tags:
  - algebra-lineal/vectores
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Combinaciones lineales y conjunto generado]]"
  - "[[04 - Ángulo, ortogonalidad y teorema de Pitágoras]]"
---

# Ejercicios de prueba de vectores

Preguntas de interrogaciones anteriores sobre vectores, producto punto y ángulos, ordenadas de menor a mayor dificultad. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Verdadero o falso: norma de una suma
Si $\mathbf u, \mathbf v \in \mathbb{R}^2$, entonces $\|\mathbf u + \mathbf v\| = \|\mathbf u\| + \|\mathbf v\|$.

> [!example]- Solución
> **Falso.** Basta un contraejemplo: $\mathbf u = \langle 1, 0\rangle$ y $\mathbf v = \langle 0, 1\rangle$ dan $\|\mathbf u + \mathbf v\| = \|\langle 1, 1\rangle\| = \sqrt2$, mientras que $\|\mathbf u\| + \|\mathbf v\| = 2$. En un V/F, un solo contraejemplo concreto basta para justificar el "falso".

### 2. Producto punto a partir del ángulo
Sean $\mathbf u, \mathbf v$ con $\|\mathbf u\| = 3$, $\|\mathbf v\| = 5$ y ángulo $\pi/3$ entre ellos. Calcule $\mathbf u \cdot \mathbf v$ y $\|\mathbf u + \mathbf v\|$.

> [!example]- Solución
> $\mathbf u \cdot \mathbf v = \|\mathbf u\|\|\mathbf v\|\cos\frac{\pi}{3} = 15 \cdot \tfrac12 = \tfrac{15}{2}$. Luego
> $$\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + 2\,\mathbf u \cdot \mathbf v + \|\mathbf v\|^2 = 9 + 15 + 25 = 49,$$
> así que $\|\mathbf u + \mathbf v\| = 7$.

### 3. Triángulo isósceles
Verifique que el triángulo de vértices $A(3, 7, 5)$, $B(3, 4, 8)$ y $C(4, 4, 5)$ es isósceles.

> [!example]- Solución
> Se calculan los tres lados como normas de diferencias:
> - $\overrightarrow{AB} = \langle 0, -3, 3\rangle$, $\|\overrightarrow{AB}\| = \sqrt{18}$.
> - $\overrightarrow{AC} = \langle 1, -3, 0\rangle$, $\|\overrightarrow{AC}\| = \sqrt{10}$.
> - $\overrightarrow{BC} = \langle 1, 0, -3\rangle$, $\|\overrightarrow{BC}\| = \sqrt{10}$.
>
> Como $d(A, C) = d(B, C) = \sqrt{10}$, tiene dos lados iguales y es isósceles.

### 4. Puntos colineales con parámetro
Encuentre, si existen, todos los $k$ tales que $P(1, 3, 7)$, $Q(2, 0, 1)$ y $R(-3, 1 - k, k)$ son colineales.

> [!example]- Solución
> Son colineales si y solo si $\overrightarrow{PR}$ es paralelo a $\overrightarrow{PQ}$, es decir, $\overrightarrow{PR} = \lambda\overrightarrow{PQ}$ para algún $\lambda$:
> $$\langle -4,\ -2 - k,\ k - 7\rangle = \lambda\langle 1, -3, -6\rangle .$$
> La primera componente obliga a $\lambda = -4$. Entonces la segunda da $-2 - k = 12$, o sea $k = -14$, y la tercera da $k - 7 = 24$, o sea $k = 31$. Las dos condiciones se contradicen, así que **no existe ningún $k$**: $R$ nunca está en la recta $PQ$.

### 5. Ángulos iguales implican perpendicularidad
Sean $\mathbf u, \mathbf v, \mathbf w \in \mathbb{R}^n$ no nulos, de igual norma, tales que el ángulo entre $\mathbf u$ y $\mathbf v$ es igual al ángulo entre $\mathbf w$ y $\mathbf v$. Demuestre que $\mathbf u - \mathbf w$ y $\mathbf v$ son perpendiculares.

> [!example]- Solución
> Ángulos iguales significa cosenos iguales:
> $$\frac{\mathbf u \cdot \mathbf v}{\|\mathbf u\|\|\mathbf v\|} = \frac{\mathbf w \cdot \mathbf v}{\|\mathbf w\|\|\mathbf v\|}.$$
> Como $\|\mathbf u\| = \|\mathbf w\|$, los denominadores son iguales (y no nulos) y queda $\mathbf u \cdot \mathbf v = \mathbf w \cdot \mathbf v$. Por distributividad, $(\mathbf u - \mathbf w) \cdot \mathbf v = 0$, que es la definición de ortogonalidad.

### 6. Vector unitario a partir de sus ángulos
Un vector unitario $\mathbf u = \langle u_1, u_2, u_3\rangle$ forma ángulos $\pi/3$, $\pi/2$ y $\pi/3$ con $\mathbf a = \langle 5, 0, 0\rangle$, $\mathbf b = \langle \sqrt2, 1, 0\rangle$ y $\mathbf c = \langle 0, 0, \sqrt2\rangle$, respectivamente. Encuentre $\mathbf u$.

> [!example]- Solución
> Cada ángulo da una ecuación $\mathbf u \cdot \mathbf x = \|\mathbf u\|\|\mathbf x\|\cos\theta$ con $\|\mathbf u\| = 1$:
> - Con $\mathbf a$ ($\|\mathbf a\| = 5$): $5u_1 = 5 \cdot \tfrac12$, así que $u_1 = \tfrac12$.
> - Con $\mathbf b$ (ángulo recto): $\sqrt2\,u_1 + u_2 = 0$, así que $u_2 = -\tfrac{\sqrt2}{2}$.
> - Con $\mathbf c$ ($\|\mathbf c\| = \sqrt2$): $\sqrt2\,u_3 = \sqrt2 \cdot \tfrac12$, así que $u_3 = \tfrac12$.
>
> $\mathbf u = \left\langle \tfrac12, -\tfrac{\sqrt2}{2}, \tfrac12\right\rangle$. Se comprueba que es unitario: $\tfrac14 + \tfrac12 + \tfrac14 = 1$.

### 7. Norma de una combinación de unitarios
Sean $\mathbf v_1, \mathbf v_2, \mathbf v_3 \in \mathbb{R}^3$ unitarios, con $\mathbf v_1$ ortogonal a $\mathbf v_2$ y a $\mathbf v_3$, y $\mathbf v_2 \cdot \mathbf v_3 = 5$. Calcule $\|3\mathbf v_1 - 2\mathbf v_2 + 2\mathbf v_3\|^2$.

> [!example]- Solución
> Se expande el producto punto del vector consigo mismo. Los términos con $\mathbf v_1 \cdot \mathbf v_2$ y $\mathbf v_1 \cdot \mathbf v_3$ se anulan, y $\mathbf v_i \cdot \mathbf v_i = 1$:
> $$\|3\mathbf v_1 - 2\mathbf v_2 + 2\mathbf v_3\|^2 = 9 + 4 + 4 + 2(-2)(2)\,\mathbf v_2 \cdot \mathbf v_3 = 17 - 8 \cdot 5 = -23 .$$
> Una norma al cuadrado no puede ser negativa: el resultado delata que **los datos son imposibles**. Por Cauchy-Schwarz, dos vectores unitarios cumplen $|\mathbf v_2 \cdot \mathbf v_3| \leq 1$, así que nunca puede valer 5. El procedimiento de expansión es el que se evalúa, pero conviene revisar siempre que el resultado tenga sentido.

## Preguntas de repaso

> [!question]- ¿Qué estrategia común tienen los ejercicios 2, 5 y 7?
> Traducir todo a productos punto, expandir con distributividad y reemplazar los datos. Las normas se manejan al cuadrado para evitar raíces.

> [!question]- ¿Cómo se prueba que tres puntos son colineales, y qué error es fácil cometer?
> Se pide que $\overrightarrow{PR}$ sea múltiplo de $\overrightarrow{PQ}$ con **un mismo** $\lambda$ en todas las componentes. El error típico es resolver cada componente por separado sin exigir que el $\lambda$ (o el parámetro) coincida.

> [!question]- ¿Qué control rápido detecta un resultado imposible en problemas de normas?
> Una norma al cuadrado nunca es negativa, y $|\mathbf u \cdot \mathbf v| \leq \|\mathbf u\|\|\mathbf v\|$. Si un cálculo viola alguna de las dos, hay un error de cuentas o los datos son inconsistentes.
