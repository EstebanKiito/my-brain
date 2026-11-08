---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - origen/complemento
prerrequisitos:
  - "[[02 - La circunferencia]]"
---

# Familias de circunferencias y eje radical

Dadas dos circunferencias que se cortan en dos puntos, se puede construir toda una **familia** de circunferencias que pasan por esos dos puntos. Restando sus ecuaciones se obtiene el **eje radical**, la recta que une los puntos de corte.

## La familia de circunferencias

Sean $C_1 : x^2 + y^2 + D_1 x + E_1 y + F_1 = 0$ y $C_2 : x^2 + y^2 + D_2 x + E_2 y + F_2 = 0$ dos circunferencias que se cortan en $\{P, Q\}$. La familia de circunferencias por $P$ y $Q$ es

$$
C_\lambda : (x^2 + y^2 + D_1 x + E_1 y + F_1) + \lambda(x^2 + y^2 + D_2 x + E_2 y + F_2) = 0.
$$

Con $\lambda = -1$ se anulan los términos cuadráticos y queda una **recta**, el **eje radical**:

$$
(D_1 - D_2)x + (E_1 - E_2)y + (F_1 - F_2) = 0.
$$

> [!tip] Eje radical
> Es la recta que pasa por los puntos de intersección de las dos circunferencias. Se obtiene **restando** sus ecuaciones. Para hallar los puntos de corte, se resuelve el eje radical junto con una de las circunferencias.

## Posición relativa de dos circunferencias

Con centros $Q_1, Q_2$ y radios $r_1, r_2$:

- Si $d(Q_1, Q_2) > r_1 + r_2$: no se cortan ($C_1 \cap C_2 = \emptyset$).
- Si $d(Q_1, Q_2) = r_1 + r_2$: son tangentes (un punto).
- Si $d(Q_1, Q_2) < r_1 + r_2$: se cortan en dos puntos.

> [!warning] Restar cancela lo cuadrático
> Al restar dos ecuaciones de circunferencia, los términos $x^2 + y^2$ se cancelan y queda una recta. Esa recta no es una circunferencia "degenerada": es la recta de los puntos comunes.

## Preguntas de repaso

> [!question]- ¿Qué es el eje radical de dos circunferencias?
> La recta que pasa por sus puntos de intersección, obtenida restando las dos ecuaciones (con lo que desaparecen los términos $x^2 + y^2$).

> [!question]- ¿Cómo se describen todas las circunferencias que pasan por dos puntos dados?
> Como combinación $C_1 + \lambda C_2$ de dos circunferencias que pasen por esos puntos. Variando $\lambda$ se recorre la familia.

> [!question]- ¿Cómo se decide si dos circunferencias se cortan?
> Comparando la distancia entre sus centros con la suma de sus radios: mayor → no se cortan, igual → tangentes, menor → dos puntos.

> [!question]- ¿Qué pasa con $\lambda = -1$ en la familia $C_1 + \lambda C_2$?
> Se anulan los términos cuadráticos y la combinación deja de ser una circunferencia: es el eje radical, la recta por los puntos comunes.
