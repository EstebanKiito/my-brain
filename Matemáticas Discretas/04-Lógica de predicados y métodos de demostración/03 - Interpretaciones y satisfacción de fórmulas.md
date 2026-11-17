---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[02 - Cuantificadores, variables libres y fórmulas de primer orden]]"
---

# Interpretaciones y satisfacción de fórmulas

Una fórmula como $\forall x\,\exists y\,(x \le y)$ no es verdadera ni falsa mientras no se diga qué es el dominio y qué significa $\le$. Una **interpretación** fija esas dos cosas y permite preguntar si la fórmula se cumple. Es el análogo de una valuación en lógica proposicional, pero mucho más rica.

## Símbolos, predicados e interpretaciones

Se distingue el **símbolo de predicado** $P$ (una etiqueta con una aridad) del **predicado sobre $D$**, $P^D$ (una relación concreta sobre el dominio $D$). Una **interpretación** $I$ para los símbolos $P_1, \dots, P_m$ consta de:

- un dominio $I(\text{dom}) = D$, y
- para cada símbolo $P_i$, un predicado $I(P_i) = P_i^D$ sobre ese dominio.

Una interpretación junto con su dominio también se llama **estructura**. Ejemplo con dos símbolos, $P$ unario y $O$ binario:

| | $I_1$ | $I_2$ |
|---|---|---|
| dominio | $\mathbb{N}$ | $\mathbb{Z}$ |
| $I(P)(x)$ | $x \ne 1$ | $x < 0$ |
| $I(O)(x, y)$ | $y$ es múltiplo de $x$ | $x + y = 0$ |

## Satisfacción

> [!tip] Definición de satisfacción
> $I$ **satisface** $\varphi(x_1, \dots, x_n)$ sobre $a_1, \dots, a_n \in I(\text{dom})$, y se escribe $I \models \varphi(a_1, \dots, a_n)$, si $\varphi(a_1, \dots, a_n)$ es verdadera al interpretar cada símbolo según $I$. En caso contrario se escribe $I \not\models \varphi(a_1, \dots, a_n)$. Para una oración basta $I \models \varphi$.

El símbolo $\models$ aquí habla de satisfacción por una interpretación; no es la valuación de la lógica proposicional.

Se evalúa $\varphi := \forall x\,\exists y\,(P(y) \wedge O(x, y))$ en las dos interpretaciones:

- **$I_1 \models \varphi$.** Para cada $x \in \mathbb{N}$ sirve $y = 0$: $0$ es múltiplo de cualquier $x$ ($0 = x \cdot 0$) y $0 \ne 1$ cumple $P$.
- **$I_2 \not\models \varphi$.** Para $x = -1$ el único $y$ con $O(-1, y)$ es $y = 1$, pero $P(1)$ pide $1 < 0$, falso. Basta este $x$ para refutar el $\forall$.

Una interpretación **satisface un conjunto** $\Sigma$ si satisface cada fórmula de $\Sigma$. Si ninguna interpretación satisface $\Sigma$, el conjunto es inconsistente (insatisfacible).

## Una misma fórmula, distintas interpretaciones

La pregunta «¿son equivalentes $\forall x\,\exists y\,(x \le y)$ y $\exists x\,\forall y\,(x \le y)$?» se resuelve eligiendo interpretaciones:

- en $\mathbb{N}$ con el orden usual, ambas son verdaderas ($y = x$ en la primera, $x = 0$ en la segunda);
- en $\mathbb{Z}$ la primera es verdadera y la segunda falsa (no hay un mínimo).

Una sola interpretación que satisfaga una y no la otra prueba que **no** son equivalentes.

## Interpretaciones que distinguen estructuras

Un uso clásico es escribir oraciones que sean verdaderas en una estructura y falsas en otra. Sobre el símbolo $<$:

| Estructura | $\exists x\,\forall y\,(x < y \vee x = y)$ (hay mínimo) | $\forall x\,\forall y\,(x < y \to \exists z\,(x < z \wedge z < y))$ (denso) |
|---|---|---|
| $(\mathbb{N}, <)$ | verdadera | falsa |
| $(\mathbb{Z}, <)$ | falsa | falsa |
| $(\mathbb{Q}, <)$ | falsa | verdadera |
| $(\mathbb{Q} \cap [0, 1], <)$ | verdadera | verdadera |

Con las dos propiedades (y sus negaciones) se obtiene una oración que identifica cada fila.

> [!warning] Dominio finito engaña
> En un dominio finito muchos cuantificadores se vuelven listas finitas de casos, y un mismo conjunto de oraciones puede comportarse distinto que en un dominio infinito. Al refutar una fórmula, el dominio finito más pequeño que sirva suele ser la mejor herramienta; al probar, hay que razonar para dominios arbitrarios.

## Preguntas de repaso

> [!question]- ¿Qué significa $I \not\models \varphi$ y es lo mismo que $I \models \neg\varphi$?
> $I \not\models \varphi$ significa que la fórmula no se satisface en esa interpretación. Para una oración es equivalente a $I \models \neg\varphi$, porque cada oración es verdadera o falsa en $I$. Con variables libres hay que fijar los valores $a_1, \dots, a_n$.

> [!question]- ¿Por qué basta una interpretación para probar que dos fórmulas no son equivalentes?
> La equivalencia exige coincidir en **todas** las interpretaciones. Una sola donde una fórmula se cumple y la otra no refuta esa exigencia; es el análogo del contraejemplo.

> [!question]- ¿Por qué $\forall x\,\exists y\,(P(y) \wedge O(x, y))$ falla en $I_2$ pero se cumple en $I_1$?
> Porque en $I_2$ el significado de $O$ ($x + y = 0$) fuerza a $y = -x$, que no siempre es negativo; en $I_1$ el significado de $O$ (múltiplo) deja libre el $y = 0$, que sí cumple $P$.
