---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Valores notables de seno y coseno]]"
---

# Ángulos y radianes

Para definir el seno y el coseno como funciones de **números reales** (y no de ángulos), se mide cada ángulo por la longitud del arco que determina en la circunferencia unitaria. Esa medida es el **radián**, y convierte a cada ángulo en un número real.

## Medir ángulos

Un ángulo es la unión de dos segmentos con un extremo común, y su medida es la abertura que forman. En grados, el ángulo extendido mide $180^\circ$, y la vuelta completa $360^\circ$. Pero los grados no son números reales "naturales" para las funciones: se necesita una medida que asocie a cada ángulo un número real.

## El radián

Sobre la circunferencia unitaria $x^2 + y^2 = 1$, un punto $P$ determina el ángulo $\angle AOP$ (con $A = (1,0)$) y también el arco $AP$.

> [!tip] Radián
> La medida del ángulo $\angle AOP$ en **radianes** es la longitud del arco $AP$ sobre la circunferencia unitaria.

Como el perímetro de la circunferencia unitaria es $2\pi$, la vuelta completa ($360^\circ$) mide $2\pi$ radianes. El ángulo extendido ($180^\circ$) mide $\pi$ radianes, y de ahí la conversión:

$$
\frac{\text{radianes}}{\text{grados}} = \frac{2\pi}{360} \iff \text{radianes} = \text{grados}\cdot\frac{\pi}{180}.
$$

**Ejemplos.** $90^\circ = \pi/2$ rad, $60^\circ = \pi/3$ rad, $45^\circ = \pi/4$ rad, $30^\circ = \pi/6$ rad.

> [!warning] Grados vs. radianes
> El radián no es una unidad "inventada": es una longitud (de arco) y por eso es un número real puro. En cálculo y en la mayoría de fórmulas, los ángulos van **siempre** en radianes.

## Preguntas de repaso

> [!question]- ¿Qué es un radián?
> La longitud del arco que un ángulo determina en la circunferencia unitaria. Como es una longitud, es un número real.

> [!question]- ¿Cuántos radianes hay en $180^\circ$ y en $360^\circ$?
> $\pi$ y $2\pi$, respectivamente, porque el arco del ángulo extendido mide la mitad del perímetro de la circunferencia unitaria ($\pi$), y la vuelta completa el perímetro entero ($2\pi$).

> [!question]- Convierta $150^\circ$ a radianes.
> $150 \cdot \pi/180 = 5\pi/6$ radianes.

> [!question]- ¿Por qué se usa la circunferencia unitaria (radio 1)?
> Para que la longitud del arco coincida numéricamente con la medida del ángulo en radianes, y así cada ángulo sea un número real simple.
