---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - origen/complemento
prerrequisitos:
  - "[[01 - Sumatorias y sus propiedades]]"
---

# Sumas telescópicas

Hay sumas que no están en la tabla de sumas conocidas pero se calculan en una línea porque **casi todo se cancela**: cada término es la diferencia de dos valores consecutivos de una misma sucesión. Se llaman telescópicas porque la suma se "pliega" como un catalejo.

## La propiedad telescópica

> [!tip] Propiedad telescópica
> Para cualquier sucesión $(a_k)$:
> $$\sum_{k=1}^{n} (a_{k+1} - a_k) = a_{n+1} - a_1, \qquad \text{y en general} \qquad \sum_{k=m}^{n} (a_{k+1} - a_k) = a_{n+1} - a_m.$$

La razón se ve al escribir la suma: $(a_2 - a_1) + (a_3 - a_2) + \dots + (a_{n+1} - a_n)$. Cada $a_k$ intermedio aparece una vez con $+$ y otra con $-$; solo sobreviven el último y el primero.

> [!warning] Cuidado con el orden
> Si el término es $a_k - a_{k+1}$ (al revés), el resultado es $a_1 - a_{n+1}$. Conviene escribir los dos primeros y el último término para ver qué sobrevive.

## Cómo detectar una telescópica

El término general casi nunca viene escrito como diferencia; hay que llevarlo a esa forma. Las tres maniobras típicas:

**1. Fracciones parciales.** $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$, así que
$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}.$$

**2. Racionalizar.** $\frac{1}{\sqrt{k} + \sqrt{k+1}} = \frac{\sqrt{k+1} - \sqrt{k}}{(k+1) - k} = \sqrt{k+1} - \sqrt{k}$, así que
$$\sum_{k=1}^{n} \frac{1}{\sqrt{k} + \sqrt{k+1}} = \sqrt{n+1} - 1.$$

**3. Logaritmos o productos.** $\log\left(1 + \frac{1}{k}\right) = \log(k+1) - \log k$, así que $\sum_{k=1}^{n} \log\left(1 + \frac{1}{k}\right) = \log(n+1)$.

## Deducir sumas conocidas

La telescópica también sirve para **obtener** fórmulas. Como $(k+1)^2 - k^2 = 2k + 1$:
$$(n+1)^2 - 1 = \sum_{k=1}^{n} \left[(k+1)^2 - k^2\right] = 2\sum_{k=1}^{n} k + n,$$
y despejando, $\sum_{k=1}^{n} k = \frac{(n+1)^2 - 1 - n}{2} = \frac{n(n+1)}{2}$. Con $(k+1)^3 - k^3 = 3k^2 + 3k + 1$ se obtiene, del mismo modo, la suma de cuadrados.

## Preguntas de repaso

> [!question]- Calcule $\sum_{k=1}^{10} \frac{1}{k(k+1)}$.
> $1 - \frac{1}{11} = \frac{10}{11}$.

> [!question]- ¿Qué vale $\sum_{k=1}^{n} (a_k - a_{k+1})$?
> $a_1 - a_{n+1}$: es la telescópica con el signo invertido.

> [!question]- Descomponga $\frac{1}{(2k-1)(2k+1)}$ para que la suma sea telescópica.
> $\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\left(\frac{1}{2k-1} - \frac{1}{2k+1}\right)$, así que la suma hasta $n$ vale $\frac{1}{2}\left(1 - \frac{1}{2n+1}\right) = \frac{n}{2n+1}$.

> [!question]- ¿Por qué se dice que solo "sobreviven" dos términos?
> Porque cada valor intermedio $a_2, \dots, a_n$ aparece sumado en un término y restado en el siguiente, y se cancela.
