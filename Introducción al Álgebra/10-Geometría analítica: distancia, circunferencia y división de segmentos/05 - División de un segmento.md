---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - origen/complemento
prerrequisitos:
  - "[[01 - Distancia entre puntos y de un punto a una recta]]"
---

# División de un segmento

Fijado un origen, cada punto $A$ tiene un **vector de posición** $\vec a$. Con ellos, dividir un segmento $AB$ en una razón dada se vuelve una fórmula sobre vectores de posición, y el punto medio es su caso más simple.

## Vector de posición y relación fundamental

Con origen $O$, el vector de posición de $A$ es $\vec a = \overrightarrow{OA}$. La relación fundamental expresa el vector de $A$ a $B$ como la diferencia de sus vectores de posición:

$$
\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \vec b - \vec a.
$$

## El punto que divide un segmento

> [!tip] División de un segmento en razón $\lambda$
> Un punto $P$ divide al segmento $AB$ en la razón $\lambda$ (es decir, $AP = \lambda\, PB$) si y solo si su vector de posición es
> $$\vec p = \frac{\vec a + \lambda \vec b}{1 + \lambda}.$$

Se obtiene despejando de $AP = \lambda PB$: $\vec p - \vec a = \lambda(\vec b - \vec p)$, de donde $\vec p(1 + \lambda) = \vec a + \lambda \vec b$.

**Punto medio.** Con $\lambda = 1$ (mitad y mitad), el punto medio de $AB$ es

$$
\vec p = \frac{\vec a + \vec b}{2}.
$$

**Ejemplo.** El punto medio de $A(1, 2)$ y $B(5, 6)$ tiene coordenadas $\left(\frac{1+5}{2}, \frac{2+6}{2}\right) = (3, 4)$.

> [!warning] La razón tiene sentido
> $\lambda = 0$ pone a $P$ en $A$; $\lambda \to \infty$ lo pone en $B$; $\lambda = -1$ no da un punto finito (el denominador se anula). La fórmula solo sirve para $\lambda \neq -1$.

## Preguntas de repaso

> [!question]- ¿Qué es el vector de posición de un punto?
> El vector que va del origen $O$ al punto: $\overrightarrow{OA} = \vec a$. Con él, todo punto se representa por un vector.

> [!question]- ¿Cómo se expresa $\overrightarrow{AB}$ con vectores de posición?
> $\overrightarrow{AB} = \vec b - \vec a$ ("punta menos cola"): el vector de $B$ menos el de $A$.

> [!question]- ¿Cuál es el vector de posición del punto medio de $AB$?
> $\frac{\vec a + \vec b}{2}$, que es la fórmula de división con $\lambda = 1$.

> [!question]- ¿Qué significa que $P$ divida a $AB$ en razón $2 : 3$?
> Que $AP : PB = 2 : 3$, es decir, $AP = \tfrac23 PB$, con $\lambda = \tfrac23$. Su posición es $\vec p = \frac{\vec a + \frac23 \vec b}{1 + \frac23}$.
