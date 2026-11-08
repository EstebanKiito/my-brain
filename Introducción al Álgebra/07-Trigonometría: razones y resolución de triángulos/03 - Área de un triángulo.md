---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[01 - Razones trigonométricas]]"
---

# Área de un triángulo

El área de un triángulo se puede calcular sin conocer la altura, usando dos lados y el ángulo entre ellos. Esta fórmula es el puente hacia el teorema del seno, porque el área se puede calcular de tres formas distintas.

## La fórmula del área

> [!tip] Área con seno
> El área de un triángulo $ABC$ es
> $$A(\triangle ABC) = \tfrac12\,ab\,\sin(\gamma),$$
> donde $a$ y $b$ son dos lados y $\gamma$ es el ángulo **comprendido** entre ellos.

**Por qué funciona.** Si $\gamma$ es agudo, la altura sobre el lado $b$ es $h = a \sin\gamma$, y el área es $\tfrac12 \cdot \text{base} \cdot \text{altura} = \tfrac12 b \cdot a \sin\gamma$. Si $\gamma$ no es agudo, se usa $\sin(180^\circ - \gamma) = \sin\gamma$ y se llega al mismo resultado.

> [!warning] El ángulo entre los lados
> La fórmula usa el ángulo **comprendido** entre $a$ y $b$. Usar otro ángulo del triángulo da un resultado incorrecto: cada par de lados va con su ángulo intermedio.

## Preguntas de repaso

> [!question]- ¿Qué datos se necesitan para calcular el área con la fórmula del seno?
> Dos lados y el ángulo comprendido entre ellos. Por ejemplo, $a$, $b$ y $\gamma$ (el ángulo entre $a$ y $b$).

> [!question]- ¿Por qué la altura sobre $b$ es $a\sin\gamma$ cuando $\gamma$ es agudo?
> Porque en el triángulo rectángulo formado por la altura, $\sin\gamma = \text{opuesto}/\text{hipotenusa} = h/a$, de donde $h = a\sin\gamma$.

> [!question]- ¿Qué ocurre si $\gamma = 90^\circ$?
> Entonces $\sin\gamma = 1$ y la fórmula da $\tfrac12 ab$, el área usual de un triángulo rectángulo con catetos $a$ y $b$.

> [!question]- ¿De cuántas formas se puede escribir el área del mismo triángulo?
> De tres: $\tfrac12 ab\sin\gamma = \tfrac12 ac\sin\beta = \tfrac12 bc\sin\alpha$. Este hecho es la clave de la demostración del teorema del seno.
