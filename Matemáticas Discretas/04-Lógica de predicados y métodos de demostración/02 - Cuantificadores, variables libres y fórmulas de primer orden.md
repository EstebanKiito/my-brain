---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Predicados, dominio y valuación]]"
---

# Cuantificadores, variables libres y fórmulas de primer orden

Un predicado con variables libres sigue siendo «abierto». Los **cuantificadores** lo cierran diciendo sobre cuántos objetos del dominio se afirma: sobre todos ($\forall$) o sobre al menos uno ($\exists$). Con ellos se escriben enunciados como «todo número tiene un sucesor mayor».

## Cuantificador universal y existencial

Sea $P(x, y_1, \dots, y_n)$ un predicado sobre un dominio $D$. Cuantificar $x$ produce un predicado nuevo que ya no depende de $x$, sólo de las variables $y_i$ que quedan libres.

> [!tip] Semántica de los cuantificadores
> $\forall x\,P(x, \bar b)$ vale $1$ si $P(a, \bar b) = 1$ para **todo** $a \in D$. $\exists x\,P(x, \bar b)$ vale $1$ si existe **al menos un** $a \in D$ con $P(a, \bar b) = 1$. En cualquier otro caso valen $0$.

Sobre $\mathbb{N}$, con $O(x, y) := x \le y$ y $P(x) := x$ es par:

- $\forall x\,O(x, 2)$ es el predicado «todo natural es menor o igual a $y$» evaluado en $y = 2$: es falso (el $3$ lo viola).
- $\exists x\,O(x, 2)$ es verdadero (sirve $x = 0$).
- $\forall x\,(P(x) \vee \neg P(x))$ es verdadero siempre: es una tautología.
- $\forall x\,P(x)$ es falso (el $1$ no es par) y $\exists x\,P(x)$ es verdadero.

## Variables libres y ligadas

En $\forall x\,O(x, y)$ la variable $x$ está **ligada** (cuantificada) y $y$ sigue **libre**: la fórmula es un predicado de $y$, y se puede evaluar en $y = 2$. Una fórmula sin variables libres se llama **oración** (o sentencia) y es verdadera o falsa por sí sola, una vez fijado el dominio y la interpretación.

> [!warning] El nombre de la variable ligada no importa
> $\forall x\,O(x, y)$ y $\forall z\,O(z, y)$ dicen lo mismo. Pero hay que evitar que una variable ligada «capture» una libre: en $\forall x\,(P(x) \to \exists x\,Q(x))$ el segundo $x$ no tiene relación con el primero; conviene renombrarlo.

## Combinar cuantificadores: el orden importa

Con dos variables se pueden anidar cuantificadores. Sobre $\mathbb{Z}$ con $O(x, y) := x \le y$:

| Fórmula | Significado | Valor |
|---|---|---|
| $\forall x\,\forall y\,O(x, y)$ | todo par está ordenado | falso |
| $\exists x\,\exists y\,O(x, y)$ | hay un par ordenado | verdadero |
| $\forall x\,\exists y\,O(x, y)$ | todo número tiene uno mayor o igual | verdadero (tomar $y = x$) |
| $\exists x\,\forall y\,O(x, y)$ | hay un número menor o igual a todos | falso en $\mathbb{Z}$ (no hay mínimo) |

Cambiar $\forall\exists$ por $\exists\forall$ cambia el significado: en $\forall x\,\exists y$ el $y$ puede **depender** de $x$; en $\exists x\,\forall y$ un único $x$ debe servir para todos los $y$. Con la relación $R = \{(a, b), (b, a)\}$ sobre $\{a, b\}$ se ve: $\forall x\,\exists y\,R(x, y)$ es verdadera (cada uno tiene a quién apuntar) pero $\exists x\,\forall y\,R(x, y)$ es falsa (ninguno apunta a todos, ni a sí mismo).

## Sintaxis completa: fórmulas de primer orden

Una **fórmula** (o predicado compuesto) es, recursivamente:

1. un predicado básico $P(x_1, \dots, x_n)$;
2. la negación $\neg\varphi$ de una fórmula;
3. $\varphi \wedge \psi$, $\varphi \vee \psi$, $\varphi \to \psi$ o $\varphi \leftrightarrow \psi$, con $\varphi, \psi$ fórmulas sobre el mismo dominio;
4. $\forall x\,\varphi$ o $\exists x\,\varphi$, con $\varphi$ una fórmula.

La valuación sigue la misma recursión, ahora incluyendo los cuantificadores. Los dos patrones de traducción más comunes del lenguaje natural:

> [!tip] Traducción estándar
> «Todo $P$ es $Q$» se escribe $\forall x\,(P(x) \to Q(x))$. «Algún $P$ es $Q$» se escribe $\exists x\,(P(x) \wedge Q(x))$. Mezclar los conectivos (por ejemplo $\forall x\,(P(x) \wedge Q(x))$ para «todo $P$ es $Q$») dice algo distinto: que **todo** objeto es $P$ y $Q$.

Con la igualdad $=$ se cuentan objetos: «hay al menos dos $P$» es $\exists x\,\exists y\,(x \ne y \wedge P(x) \wedge P(y))$, y «hay a lo más uno» es $\forall x\,\forall y\,((P(x) \wedge P(y)) \to x = y)$.

## Preguntas de repaso

> [!question]- ¿Por qué «todo gato es negro» se escribe con $\to$ y no con $\wedge$?
> Porque sólo afirma algo de los gatos. Con $\forall x\,(G(x) \to N(x))$ los objetos que no son gatos hacen verdadero el condicional y no molestan; con $\wedge$ se estaría diciendo que todo objeto del dominio es gato y es negro.

> [!question]- ¿Qué diferencia hay entre $\forall x\,\exists y\,R(x, y)$ y $\exists y\,\forall x\,R(x, y)$?
> En la primera el $y$ puede cambiar con cada $x$; en la segunda hay un único $y$ que sirve para todos los $x$. La segunda implica la primera, pero no al revés.

> [!question]- ¿Cuándo una fórmula es una oración?
> Cuando todas sus variables están ligadas por algún cuantificador. Entonces, fijados dominio e interpretación, tiene un valor de verdad definido sin necesidad de asignar valores a variables.
