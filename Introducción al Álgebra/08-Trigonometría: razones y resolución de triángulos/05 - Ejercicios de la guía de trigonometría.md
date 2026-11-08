---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Razones trigonométricas]]"
  - "[[04 - Teorema del seno y del coseno]]"
---

# Ejercicios de la guía de trigonometría

Preguntas de la guía sobre razones trigonométricas, identidades y resolución de triángulos. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Identidades con secante y tangente
Si $u = \sec\alpha$ y $v = 3\tan^2\alpha$, calcule $3u^2 - v$.

> [!example]- Solución
> $3u^2 - v = 3\sec^2\alpha - 3\tan^2\alpha = 3(\sec^2\alpha - \tan^2\alpha)$. Como $\tan^2\alpha + 1 = \sec^2\alpha$, se tiene $\sec^2\alpha - \tan^2\alpha = 1$, así que $3u^2 - v = 3$.

### 2. Simplificar un producto
Calcule $\dfrac{\tan^2\alpha}{1 + \tan^2\alpha} \cdot \dfrac{1 + \cot^2\alpha}{\cot^2\alpha}$.

> [!example]- Solución
> $\frac{\tan^2\alpha}{1 + \tan^2\alpha} = \frac{\tan^2\alpha}{\sec^2\alpha} = \sin^2\alpha$, y $\frac{1 + \cot^2\alpha}{\cot^2\alpha} = \frac{\csc^2\alpha}{\cot^2\alpha} = \frac{1/\sin^2\alpha}{\cos^2\alpha/\sin^2\alpha} = \frac{1}{\cos^2\alpha} = \sec^2\alpha$. El producto es $\sin^2\alpha \cdot \sec^2\alpha = \tan^2\alpha$.

### 3. Expresar en términos de $p$ y $q$
Si $\alpha$ es agudo y $\tan\alpha = \dfrac{2pq}{p^2 - q^2}$, exprese $\cos\alpha$ y $\csc\alpha$ en términos de $p$ y $q$.

> [!example]- Solución
> Piense en un triángulo rectángulo con cateto opuesto $2pq$ y adyacente $p^2 - q^2$. Su hipotenusa es
> $$\sqrt{(2pq)^2 + (p^2 - q^2)^2} = \sqrt{4p^2q^2 + p^4 - 2p^2q^2 + q^4} = \sqrt{(p^2 + q^2)^2} = p^2 + q^2.$$
> Luego $\cos\alpha = \frac{p^2 - q^2}{p^2 + q^2}$ y $\csc\alpha = \frac{p^2 + q^2}{2pq}$.

### 4. Un asta sobre un edificio
Un asta está clavada verticalmente en lo alto de un edificio. A $12$ m de distancia, los ángulos de elevación de la punta del asta y de la parte superior del edificio son $60^\circ$ y $30^\circ$. Halle la longitud del asta.

> [!example]- Solución
> Sea $h$ la altura del edificio y $L$ la del asta. Entonces $\tan30^\circ = h/12$ y $\tan60^\circ = (h + L)/12$. Como $\tan30^\circ = 1/\sqrt3$ y $\tan60^\circ = \sqrt3$, se tiene $h = 12/\sqrt3 = 4\sqrt3$ y $h + L = 12\sqrt3$. La longitud del asta es $L = 12\sqrt3 - 4\sqrt3 = 8\sqrt3$ m.

### 5. Despejar la tangente
Si $a\cos^2\alpha + b\sin^2\alpha = c$, demuestre que $\tan^2\alpha = \dfrac{c - a}{b - c}$.

> [!example]- Solución
> Dividiendo la igualdad por $\cos^2\alpha$: $a + b\tan^2\alpha = c\sec^2\alpha = c(1 + \tan^2\alpha)$. Reordenando, $a + b\tan^2\alpha = c + c\tan^2\alpha$, de donde $(b - c)\tan^2\alpha = c - a$, es decir, $\tan^2\alpha = \frac{c - a}{b - c}$.

## Preguntas de repaso

> [!question]- ¿Qué identidad usa el ejercicio 1?
> $\tan^2\alpha + 1 = \sec^2\alpha$, que equivale a $\sec^2\alpha - \tan^2\alpha = 1$. Es la versión "dividida por $\cos^2$" de la identidad fundamental.

> [!question]- En el ejercicio 3, ¿cómo se interpreta $\tan\alpha = 2pq/(p^2 - q^2)$?
> Como un triángulo rectángulo de cateto opuesto $2pq$ y adyacente $p^2 - q^2$. La hipotenusa es $p^2 + q^2$ por el teorema de Pitágoras.

> [!question]- En el ejercicio 4, ¿por qué la tangente sirve para resolver el problema?
> Porque relaciona el ángulo de elevación con el cociente entre la altura y la distancia horizontal ($\tan = \text{opuesto}/\text{adyacente}$), que es justo lo que se conoce y lo que se busca.
