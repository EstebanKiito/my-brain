---
ramo: "Álgebra Lineal"
tema: "Vectores en Rⁿ"
tags:
  - algebra-lineal/vectores
  - origen/complemento
prerrequisitos:
  - "[[01 - Vectores y sus operaciones]]"
---

# Combinaciones lineales y conjunto generado

Con suma y producto por escalar se pueden fabricar vectores nuevos a partir de unos pocos "ingredientes". La pregunta central de todo el curso aparece aquí por primera vez: **¿qué vectores se pueden fabricar con un conjunto dado?** Responderla lleva a los sistemas de ecuaciones, a la independencia lineal, a las bases y a la dimensión.

## Combinación lineal

> [!tip] Definición
> $\mathbf v$ es **combinación lineal** de $\mathbf u_1, \dots, \mathbf u_k$ si existen escalares $c_1, \dots, c_k$, llamados **pesos**, tales que
> $$\mathbf v = c_1\mathbf u_1 + c_2\mathbf u_2 + \dots + c_k\mathbf u_k .$$

Los pesos pueden ser cualquier número real, incluso cero o negativos. El vector cero siempre es combinación lineal de cualquier conjunto (todos los pesos iguales a cero).

**Ejemplo.** Sean $\mathbf v = \langle 2, 3, 0\rangle$ y $\mathbf u = \langle -3, 1, 0\rangle$.

- $2\mathbf v + \mathbf u = \langle 1, 7, 0\rangle$ es una combinación lineal de ellos (hay infinitas, una por cada par de pesos).
- ¿Es $\langle 5, -3, 2\rangle$ combinación lineal de $\mathbf v$ y $\mathbf u$? No: cualquier $a\mathbf v + b\mathbf u$ tiene tercera componente $a \cdot 0 + b \cdot 0 = 0$, y el vector buscado tiene un $2$ ahí. No hace falta resolver nada más.

Esa observación es geométrica: todas las combinaciones de $\mathbf v$ y $\mathbf u$ viven en el plano $z = 0$, y $\langle 5, -3, 2\rangle$ está fuera de él.

## Decidir si un vector es combinación lineal

En general, preguntar si $\mathbf b$ es combinación de $\mathbf u_1, \dots, \mathbf u_k$ es preguntar si una **ecuación vectorial** $x_1\mathbf u_1 + \dots + x_k\mathbf u_k = \mathbf b$ tiene solución. Igualando componente a componente, esa ecuación es un **sistema de ecuaciones lineales** cuyas incógnitas son los pesos.

**Ejemplo.** ¿Pertenece $\langle 3, 1\rangle$ a las combinaciones de $\langle 1, 0\rangle$ y $\langle 1, 2\rangle$?

$$
c_1\begin{bmatrix}1\\0\end{bmatrix} + c_2\begin{bmatrix}1\\2\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}
\iff
\begin{cases} c_1 + c_2 = 3 \\ 2c_2 = 1 \end{cases}
$$

De la segunda ecuación, $c_2 = \tfrac12$, y de la primera, $c_1 = \tfrac52$. Sí pertenece: $\langle 3, 1\rangle = \tfrac52\langle 1, 0\rangle + \tfrac12\langle 1, 2\rangle$.

> [!warning] Existencia frente a cálculo
> La pregunta "¿es combinación lineal?" se responde con sí o no, según si el sistema tiene **alguna** solución. Encontrar pesos concretos es un paso extra. Si el sistema es inconsistente, la respuesta es no aunque cada ecuación por separado se pueda cumplir.

## Conjunto generado

> [!tip] Definición
> El **conjunto generado** por $S = \{\mathbf u_1, \dots, \mathbf u_k\}$ es el conjunto de **todas** sus combinaciones lineales:
> $$\operatorname{Gen}(S) = \operatorname{Gen}\{\mathbf u_1, \dots, \mathbf u_k\} = \{c_1\mathbf u_1 + \dots + c_k\mathbf u_k : c_1, \dots, c_k \in \mathbb{R}\}.$$

Así, "$\mathbf b$ es combinación lineal de los $\mathbf u_i$" y "$\mathbf b \in \operatorname{Gen}\{\mathbf u_1, \dots, \mathbf u_k\}$" dicen exactamente lo mismo. El conjunto generado siempre contiene a $\mathbf 0$ y a cada $\mathbf u_i$.

¿Qué forma tiene geométricamente?

- **Un vector no nulo** $\mathbf v$: $\operatorname{Gen}\{\mathbf v\} = \{t\mathbf v\}$ son todos sus múltiplos, una **recta que pasa por el origen**.
- **Dos vectores no paralelos** $\mathbf u, \mathbf v$ en $\mathbb{R}^3$: $\operatorname{Gen}\{\mathbf u, \mathbf v\}$ es un **plano que pasa por el origen**.
- **Dos vectores paralelos**: el segundo no aporta nada nuevo y el generado sigue siendo una recta.

![Conjunto generado por uno y dos vectores](adjuntos/Conjunto%20generado%20por%20uno%20y%20dos%20vectores.png)

> [!example]- Transcripción de la imagen
> - Izquierda: en $\mathbb{R}^3$, $\operatorname{Gen}\{\mathbf v\}$ es la recta que pasa por el origen y por la punta de $\mathbf v$.
> - Derecha: $\operatorname{Gen}\{\mathbf u, \mathbf v\}$ es un plano por el origen, cuadriculado por los múltiplos $\mathbf u, 3\mathbf u, 5\mathbf u$ en una dirección y $\mathbf v, 2\mathbf v, 3\mathbf v$ en la otra. Cada punto del plano se alcanza combinando un múltiplo de $\mathbf u$ con uno de $\mathbf v$.

En $\mathbb{R}^2$, dos vectores no paralelos generan **todo** el plano: cualquier $\langle a, b\rangle$ se alcanza. El ejemplo anterior con $\langle 1, 0\rangle$ y $\langle 1, 2\rangle$ funciona para cualquier lado derecho, porque el sistema siempre se puede resolver despejando primero $c_2 = b/2$.

> [!warning] Agregar vectores no siempre agranda el generado
> $\operatorname{Gen}\{\mathbf u, \mathbf v, \mathbf w\}$ es igual a $\operatorname{Gen}\{\mathbf u, \mathbf v\}$ cuando $\mathbf w$ ya es combinación de $\mathbf u$ y $\mathbf v$. Cuántos vectores "aportan algo" se estudia con la independencia lineal: tres vectores de $\mathbb{R}^3$ pueden generar todo el espacio, un plano o solo una recta.

## Preguntas de repaso

> [!question]- ¿Por qué el vector cero pertenece a cualquier conjunto generado?
> Porque basta tomar todos los pesos iguales a cero: $0\mathbf u_1 + \dots + 0\mathbf u_k = \mathbf 0$. Por eso un conjunto generado nunca es una recta o un plano que no pase por el origen.

> [!question]- ¿Es $\langle 1, 1, 1\rangle$ combinación lineal de $\langle 1, 0, 1\rangle$ y $\langle 0, 1, 0\rangle$? ¿Y $\langle 1, 1, 2\rangle$?
> El primero sí: $1\langle 1, 0, 1\rangle + 1\langle 0, 1, 0\rangle = \langle 1, 1, 1\rangle$. El segundo no: toda combinación $a\langle 1, 0, 1\rangle + b\langle 0, 1, 0\rangle = \langle a, b, a\rangle$ tiene la primera y la tercera componentes iguales, y $1 \neq 2$.

> [!question]- Describa geométricamente $\operatorname{Gen}\{\langle 1, 2, 3\rangle, \langle -2, -4, -6\rangle\}$.
> Es una recta por el origen con dirección $\langle 1, 2, 3\rangle$, porque el segundo vector es $-2$ veces el primero y no agrega direcciones nuevas.

> [!question]- V o F: si $\mathbf b \in \operatorname{Gen}\{\mathbf u, \mathbf v\}$, entonces $\operatorname{Gen}\{\mathbf u, \mathbf v, \mathbf b\} = \operatorname{Gen}\{\mathbf u, \mathbf v\}$.
> Verdadero. Toda combinación que use $\mathbf b$ se reescribe reemplazando $\mathbf b = a\mathbf u + c\mathbf v$, y queda como combinación de $\mathbf u$ y $\mathbf v$. La otra inclusión es inmediata (peso cero para $\mathbf b$).

> [!question]- ¿Qué tipo de problema hay que resolver para saber si $\mathbf b$ está en el generado de $k$ vectores de $\mathbb{R}^n$?
> Un sistema de $n$ ecuaciones lineales (una por componente) con $k$ incógnitas (los pesos). $\mathbf b$ está en el generado si y solo si ese sistema es consistente.
