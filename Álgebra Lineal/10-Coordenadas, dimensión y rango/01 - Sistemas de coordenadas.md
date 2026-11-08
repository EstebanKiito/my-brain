---
ramo: "Álgebra Lineal"
tema: "Coordenadas, dimensión y rango"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[03 - Independencia lineal y bases]]"
---

# Sistemas de coordenadas

Una base no solo genera un espacio sin redundancia: también permite **ponerle coordenadas**. Igual que los ejes cartesianos asignan a cada punto del plano un par de números, una base $\mathcal B$ asigna a cada vector de $V$ (sea un polinomio, una matriz o un vector de un plano dentro de $\mathbb{R}^3$) una lista de números en $\mathbb{R}^n$. Con eso, cualquier problema sobre $V$ se convierte en un problema en $\mathbb{R}^n$, donde ya se sabe escalonar.

## Representación única

> [!tip] Teorema (representación única)
> Si $\mathcal B = \{\mathbf b_1, \dots, \mathbf b_n\}$ es una base de $V$, cada $\mathbf x \in V$ se escribe de **una única** forma como
> $$\mathbf x = c_1\mathbf b_1 + \dots + c_n\mathbf b_n .$$

Existe porque $\mathcal B$ genera $V$. Es única porque, si hubiera dos escrituras, restándolas se obtendría $(c_1 - d_1)\mathbf b_1 + \dots + (c_n - d_n)\mathbf b_n = \mathbf 0$, y por independencia todos los $c_i - d_i$ serían cero.

> [!tip] Definición
> Los pesos $c_1, \dots, c_n$ son las **coordenadas de $\mathbf x$ respecto de $\mathcal B$**, y el **vector de coordenadas** es
> $$[\mathbf x]_{\mathcal B} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} \in \mathbb{R}^n .$$

El orden de la base importa: $\{\mathbf b_1, \mathbf b_2\}$ y $\{\mathbf b_2, \mathbf b_1\}$ dan vectores de coordenadas con las componentes intercambiadas.

## Coordenadas en $\mathbb{R}^n$

**De coordenadas a vector:** se arma la combinación. Con $\mathbf b_1 = \langle 1, 0\rangle$, $\mathbf b_2 = \langle 1, 2\rangle$ y $[\mathbf x]_{\mathcal B} = \langle -2, 3\rangle$: $\mathbf x = -2\mathbf b_1 + 3\mathbf b_2 = \langle 1, 6\rangle$.

**De vector a coordenadas:** se resuelve un sistema. En $\mathbb{R}^n$ conviene la **matriz de cambio de coordenadas** $P_{\mathcal B} = [\mathbf b_1 \cdots \mathbf b_n]$:

$$
\mathbf x = P_{\mathcal B}[\mathbf x]_{\mathcal B}, \qquad [\mathbf x]_{\mathcal B} = P_{\mathcal B}^{-1}\mathbf x .
$$

Por ejemplo, con $\mathbf b_1 = \langle 2, 1\rangle$, $\mathbf b_2 = \langle -1, 1\rangle$ y $\mathbf x = \langle 4, 5\rangle$: resolver $2c_1 - c_2 = 4$, $c_1 + c_2 = 5$ da $[\mathbf x]_{\mathcal B} = \langle 3, 2\rangle$.

![Coordenadas de x en la base B](adjuntos/Coordenadas%20de%20x%20en%20la%20base%20B.png)

> [!example]- Transcripción de la imagen
> El plano cubierto por una cuadrícula inclinada formada por los vectores $\mathbf b_1$ y $\mathbf b_2$ (en vez de los ejes usuales). El punto $\mathbf x$ queda en un nodo de esa cuadrícula: se llega a él avanzando un número entero de pasos en la dirección de $\mathbf b_1$ y otro en la de $\mathbf b_2$. Esos números son las coordenadas $[\mathbf x]_{\mathcal B}$.

## Coordenadas en un subespacio

Las coordenadas también sirven para un plano dentro de $\mathbb{R}^3$. Con $\mathbf v_1 = \langle 3, 6, 2\rangle$, $\mathbf v_2 = \langle -1, 0, 1\rangle$, $H = \operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}$ y $\mathbf x = \langle 3, 12, 7\rangle$, se escalona $[\mathbf v_1\ \mathbf v_2 \mid \mathbf x]$ y se obtiene $c_1 = 2$, $c_2 = 3$ (sistema consistente). Entonces $\mathbf x \in H$ y $[\mathbf x]_{\mathcal B} = \langle 2, 3\rangle$: un vector de $\mathbb{R}^3$ con **dos** coordenadas, porque $H$ es un plano. Cualquier plano se comporta como $\mathbb{R}^2$ una vez fijada una base.

## El isomorfismo de coordenadas

> [!tip] Teorema
> Si $\mathcal B$ es una base de $V$ con $n$ vectores, la función $\mathbf x \mapsto [\mathbf x]_{\mathcal B}$ es una transformación **lineal, inyectiva y sobre** de $V$ en $\mathbb{R}^n$: $[\mathbf u + \mathbf v]_{\mathcal B} = [\mathbf u]_{\mathcal B} + [\mathbf v]_{\mathcal B}$ y $[c\mathbf u]_{\mathcal B} = c[\mathbf u]_{\mathcal B}$. Se llama **isomorfismo**.

Consecuencia práctica: **las preguntas de combinaciones lineales, independencia y generación en $V$ se responden con las coordenadas en $\mathbb{R}^n$**. Un conjunto es LI en $V$ si y solo si sus vectores de coordenadas son LI en $\mathbb{R}^n$.

**Ejemplos en $\mathbb{P}_n$** (base estándar $\{1, t, t^2, \dots\}$, cuyas coordenadas son los coeficientes):

- $3t^2 - 2t - 2 \in \mathbb{P}_3$ tiene coordenadas $\langle -2, -2, 3, 0\rangle$.
- $\{1 + 2t^2,\ 4 + t + 5t^2,\ 3 + 2t\}$: las coordenadas $\langle 1, 0, 2\rangle$, $\langle 4, 1, 5\rangle$, $\langle 3, 2, 0\rangle$ forman una matriz con solo dos pivotes. Los polinomios son **LD**; de hecho, $3 + 2t = -5(1 + 2t^2) + 2(4 + t + 5t^2)$.
- ¿$q = 3 + 12t + 7t^2$ está en $\operatorname{Gen}\{3 + 6t + t^2,\ t^2 - 1\}$? Las coordenadas son las del ejemplo del plano en $\mathbb{R}^3$: sí, $q = 2p_1 + 3p_2$.

## Preguntas de repaso

> [!question]- ¿Por qué las coordenadas exigen una base y no basta con un conjunto generador?
> Porque con un conjunto LD un mismo vector se escribe de varias formas, y las "coordenadas" no estarían bien definidas. La independencia garantiza la unicidad.

> [!question]- Con $\mathcal B = \{1 + t, 1 + t^2, t + t^2\}$, encuentre $[6 + 3t - t^2]_{\mathcal B}$.
> Se busca $a(1 + t) + b(1 + t^2) + c(t + t^2)$: $a + b = 6$, $a + c = 3$, $b + c = -1$. Sumando, $a + b + c = 4$, así que $c = -2$, $b = 1$, $a = 5$: $\langle 5, 1, -2\rangle$.

> [!question]- Si $H$ es un plano en $\mathbb{R}^3$ con base $\{\mathbf v_1, \mathbf v_2\}$, ¿en qué espacio viven los vectores de coordenadas de los puntos de $H$?
> En $\mathbb{R}^2$: dos coordenadas, una por vector de la base, aunque los puntos tengan tres componentes.

> [!question]- ¿Cómo se usa el isomorfismo de coordenadas para decidir si cuatro matrices de $2 \times 2$ son LI?
> Se escriben sus coordenadas en la base estándar (las cuatro entradas) como vectores de $\mathbb{R}^4$, se ponen como columnas y se cuentan los pivotes o se calcula el determinante.
