---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[03 - Área de un triángulo]]"
---

# Teorema del seno y del coseno

Para "resolver" un triángulo (hallar sus lados y ángulos desconocidos) no basta el teorema de Pitágoras, que solo sirve para triángulos rectángulos. El **teorema del seno** y el **teorema del coseno** generalizan la resolución a cualquier triángulo.

## Teorema del seno

> [!tip] Teorema del seno
> En todo triángulo $ABC$,
> $$\frac{\sin\alpha}{a} = \frac{\sin\beta}{b} = \frac{\sin\gamma}{c},$$
> donde $\alpha$ es el ángulo opuesto al lado $a$, $\beta$ al lado $b$ y $\gamma$ al lado $c$.

**Demostración.** El área es $\tfrac12 ab\sin\gamma = \tfrac12 ac\sin\beta = \tfrac12 bc\sin\alpha$. Igualando y dividiendo por $abc$ se obtiene la cadena de razones.

Se usa cuando se conoce un lado y su ángulo opuesto (junto con otro dato): permite hallar el otro ángulo y, de ahí, el resto.

## Teorema del coseno

> [!tip] Teorema del coseno
> En todo triángulo $ABC$:
> $$a^2 = b^2 + c^2 - 2bc\cos\alpha, \qquad b^2 = a^2 + c^2 - 2ac\cos\beta, \qquad c^2 = a^2 + b^2 - 2ab\cos\gamma.$$

Generaliza Pitágoras: cuando el ángulo opuesto es recto, su coseno es $0$ y queda $a^2 = b^2 + c^2$.

Se usa cuando se conocen **dos lados y el ángulo comprendido** (para hallar el tercer lado) o los **tres lados** (para hallar un ángulo).

> [!warning] Cuándo usar cada uno
> **Seno:** un lado con su ángulo opuesto, y otro dato. **Coseno:** dos lados y el ángulo entre ellos, o los tres lados. Confundirlos lleva a cuentas sin sentido.

## El caso ambiguo del seno

Al despejar un ángulo con el teorema del seno se obtiene $\sin\alpha = k$, y en $(0^\circ, 180^\circ)$ hay **dos** ángulos con ese seno: $\alpha$ y $180^\circ - \alpha$. Hay que revisar cuál es compatible con los otros ángulos (la suma debe ser menor que $180^\circ$).

**Ejemplo.** Con $c = 5\sqrt 2$, $a = 5$ y $\gamma = 45^\circ$: $\sin\alpha = \frac{a\sin\gamma}{c} = \frac{5 \cdot \frac{\sqrt 2}{2}}{5\sqrt 2} = \frac{1}{2}$, así que $\alpha = 30^\circ$ o $150^\circ$. Pero $150^\circ + 45^\circ > 180^\circ$, y solo queda $\alpha = 30^\circ$. Con el teorema del coseno se llega a lo mismo: $50 = 25 + b^2 - 5\sqrt 2\, b$ tiene una sola raíz positiva, $b = \frac{5\sqrt 2 + 5\sqrt 6}{2}$.

> [!warning] Las pautas puntúan el descarte
> Escribir las dos opciones y justificar por qué una no sirve vale puntaje aparte. Si las dos son compatibles, hay dos triángulos distintos con esos datos.

## Problemas con ángulos de elevación

Cuando dos observadores ven el mismo punto alto con ángulos distintos, hay dos caminos:

1. **Con dos triángulos rectángulos:** se llama $h$ a la altura y $x$ a una distancia horizontal, se escribe $\tan(\text{ángulo}) = \frac{h}{\text{distancia}}$ para cada observador y se resuelve el sistema.
2. **Con el triángulo oblicuo:** el triángulo formado por los dos observadores y la cima tiene ángulos conocidos (el exterior es la suma de los dos interiores no adyacentes), así que el teorema del seno da la distancia a la cima, y luego $h = \text{distancia} \cdot \sin(\text{ángulo})$.

## Preguntas de repaso

> [!question]- ¿Qué relaciona el teorema del seno?
> Los cocientes $\sin\alpha/a$, $\sin\beta/b$ y $\sin\gamma/c$, que son iguales entre sí: cada ángulo va con su lado opuesto.

> [!question]- ¿Cómo se relaciona el teorema del coseno con el de Pitágoras?
> El coseno generaliza Pitágoras: con el ángulo opuesto de $90^\circ$, $\cos = 0$ y $c^2 = a^2 + b^2 - 2ab\cos\gamma$ se reduce a $c^2 = a^2 + b^2$.

> [!question]- ¿Qué datos conviene tener para usar el teorema del seno?
> Un lado y su ángulo opuesto, más otro lado o ángulo. Con eso se despeja el ángulo (o lado) que falta por proporción.

> [!question]- ¿Cómo se halla un ángulo si se conocen los tres lados?
> Con el teorema del coseno: por ejemplo, $\cos\gamma = \frac{a^2 + b^2 - c^2}{2ab}$, despejando el coseno del ángulo buscado.
