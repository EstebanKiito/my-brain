---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Teorema de los ceros racionales]]"
  - "[[04 - Número de raíces y raíces complejas]]"
  - "[[05 - Gráfica de polinomios]]"
---

# Ejercicios de prueba de raíces de polinomios

Preguntas de interrogaciones y exámenes anteriores. El patrón casi siempre es el mismo: conseguir **una** raíz (por el teorema de los ceros racionales, porque la dan o porque se conoce una compleja y con ella su conjugada), dividir para bajar el grado, y repetir hasta llegar a cuadráticas. La otra variante es leer el polinomio desde su gráfico.

## Ejercicios

### 1. Una cuártica con raíces racionales
Resuelva $4x^4 - 4x^3 - 5x^2 + x + 1 = 0$.

> [!example]- Solución
> Candidatos racionales $\frac{p}{q}$ con $p \mid 1$ y $q \mid 4$: $\pm 1, \pm\frac{1}{2}, \pm\frac{1}{4}$. Se verifica que $P\left(\frac{1}{2}\right) = P\left(-\frac{1}{2}\right) = 0$, así que $\left(x - \frac{1}{2}\right)\left(x + \frac{1}{2}\right) = x^2 - \frac{1}{4}$ divide a $P$. Dividiendo, $P(x) = \left(x^2 - \frac{1}{4}\right)(4x^2 - 4x - 4) = 4\left(x^2 - \frac{1}{4}\right)(x^2 - x - 1)$. Las soluciones son $\pm\frac{1}{2}$ y $\frac{1 \pm \sqrt 5}{2}$.

### 2. Factorizar y graficar
Determine las raíces de $P(x) = 3x^4 + 4x^3 - 17x^2 - 6x$, factorícelo y describa su gráfico.

> [!example]- Solución
> $P(x) = x(3x^3 + 4x^2 - 17x - 6)$, así que $0$ es raíz. Para la cúbica, los candidatos son $\pm 1, \pm 2, \pm 3, \pm 6, \pm\frac{1}{3}, \pm\frac{2}{3}$, y $x = 2$ funciona. Dividiendo: $3x^3 + 4x^2 - 17x - 6 = (x - 2)(3x^2 + 10x + 3) = (x - 2)(x + 3)(3x + 1)$. Entonces
> $$P(x) = 3x(x - 2)(x + 3)\left(x + \tfrac{1}{3}\right),$$
> con raíces $-3, -\frac{1}{3}, 0, 2$, todas simples (cruza el eje en las cuatro). Grado par y coeficiente principal positivo: ambos extremos suben.

### 3. Leer el polinomio desde su gráfico
El gráfico de un polinomio $Q$ de grado $3$ es el siguiente. Determine $Q$.

![Gráfico de un polinomio de grado 3 con raíz doble en 2](adjuntos/Gr%C3%A1fico%20de%20un%20polinomio%20de%20grado%203%20con%20ra%C3%ADz%20doble%20en%202.png)

> [!example]- Transcripción de la figura
> Ejes $X$ (de $-2$ a $2{,}5$) e $Y$ (de $-2$ a $3$). La curva baja desde la izquierda arriba, cruza el eje $X$ en $x = -1$, tiene un mínimo en $(0, -2)$, sube hasta tocar el eje $X$ en $x = 2$ sin cruzarlo y vuelve a bajar hacia la derecha.

> [!example]- Solución
> - $x = -1$: cruza, raíz simple.
> - $x = 2$: toca y rebota, multiplicidad par; con grado $3$, es doble.
> - $Q(0) = -2$, y $Q \to -\infty$ cuando $x \to +\infty$ (coeficiente principal negativo).
>
> Entonces $Q(x) = c(x + 1)(x - 2)^2$ y $Q(0) = 4c = -2$, así que $c = -\frac{1}{2}$: $Q(x) = -\frac{1}{2}(x + 1)(x - 2)^2$. El signo negativo de $c$ es consistente con que la curva baje a la derecha.

### 4. Un cúbico con condiciones
Determine el polinomio $p$ de grado $3$ con raíces $1$ y $-2$, tal que $p(-1) = 4$ y $p(2) = 28$.

> [!example]- Solución
> $p(x) = (x - 1)(x + 2)(ax + b)$. Entonces $p(-1) = (-2)(1)(-a + b) = 4$ da $a - b = 2$, y $p(2) = (1)(4)(2a + b) = 28$ da $2a + b = 7$. Resolviendo, $a = 3$, $b = 1$: $p(x) = (x - 1)(x + 2)(3x + 1)$.

### 5. Sin factores lineales y multiplicidad
(a) Demuestre que $q(x) = x^4 - x^2 + 1$ no tiene factores lineales en $\mathbb{Q}[x]$. (b) Encuentre $n$ tal que $(x - 1)^n q(x) = (x^2 - 1)(x^3 - 1)(x^6 - 5x + 1)$ para algún $q$ con $q(1) \neq 0$.

> [!example]- Solución
> (a) Un factor lineal en $\mathbb{Q}[x]$ daría una raíz racional, y los únicos candidatos son $\pm 1$. Pero $q(1) = q(-1) = 1 \neq 0$.
> (b) $x^2 - 1 = (x - 1)(x + 1)$ y $x^3 - 1 = (x - 1)(x^2 + x + 1)$, mientras que $x^6 - 5x + 1$ vale $-3$ en $1$. Entonces el producto es $(x - 1)^2 (x + 1)(x^2 + x + 1)(x^6 - 5x + 1)$, y $q(1) = 2 \cdot 3 \cdot (-3) \neq 0$. Luego $n = 2$.

### 6. Raíz compleja con parámetro
Sea $P(x) = x^5 - x^4 + ax^3 - ax^2 + 4x - 4$. (a) Demuestre que $P(2i) = 0$ si y solo si $a = 5$. (b) Para ese $a$, factorice $P$ en irreducibles reales (hay una raíz entera).

> [!example]- Solución
> (a) Con $i^2 = -1$: $P(2i) = 32i - 16 - 8ai + 4a + 8i - 4 = (4a - 20) + (40 - 8a)i$. Es $0$ si y solo si ambas partes son $0$, es decir, $a = 5$.
> (b) $P(1) = 0$, y como $2i$ es raíz de un polinomio real, $-2i$ también: $(x^2 + 4)(x - 1)$ divide a $P$. Dividiendo sale $x^2 + 1$, irreducible. Factorización: $P(x) = (x - 1)(x^2 + 1)(x^2 + 4)$.

### 7. Factorizar sobre $\mathbb{C}$
Verifique que $2 + i$ es raíz de $P(z) = z^4 - 3z^3 + 2z^2 + z + 5$ y factorice $P$ sobre $\mathbb{C}$.

> [!example]- Solución
> $(2+i)^2 = 3 + 4i$, $(2+i)^3 = 2 + 11i$, $(2+i)^4 = -7 + 24i$, y $P(2+i) = (-7 + 24i) - 3(2 + 11i) + 2(3 + 4i) + (2 + i) + 5 = 0$. Por conjugadas, $(z - (2+i))(z - (2-i)) = z^2 - 4z + 5$ divide a $P$, y $P(z) = (z^2 - 4z + 5)(z^2 + z + 1)$. Las raíces de $z^2 + z + 1$ son $-\frac{1}{2} \pm \frac{\sqrt 3}{2}i$, así que
> $$P(z) = (z - 2 - i)(z - 2 + i)\left(z + \tfrac{1}{2} - \tfrac{\sqrt 3}{2}i\right)\left(z + \tfrac{1}{2} + \tfrac{\sqrt 3}{2}i\right).$$

### 8. Coeficientes para una raíz compleja
Determine $m, n \in \mathbb{R}$ para que $1 + i$ sea raíz de $P(x) = x^5 + mx^3 + n$.

> [!example]- Solución
> $(1+i)^2 = 2i$, así que $(1+i)^3 = 2i(1+i) = -2 + 2i$ y $(1+i)^5 = (2i)^2(1+i) = -4 - 4i$. Entonces $P(1+i) = (-4 - 2m + n) + (-4 + 2m)i = 0$ exige $m = 2$ y $n = 8$. (También se puede pasar a forma polar, $1 + i = \sqrt 2\,\operatorname{cis}\frac{\pi}{4}$, y usar De Moivre.)

## Preguntas de repaso

> [!question]- Si se conoce una raíz compleja no real de un polinomio real, ¿cuánto baja el grado?
> Dos: la raíz y su conjugada dan el factor real $x^2 - 2\operatorname{Re}(\alpha)x + |\alpha|^2$, por el que se divide.

> [!question]- En un gráfico, ¿cómo se distingue una raíz doble de una simple?
> En la doble la curva toca el eje y rebota sin cambiar de signo; en la simple lo cruza.

> [!question]- ¿Por qué "no tiene factores lineales en $\mathbb{Q}[x]$" se prueba revisando solo $\pm 1$ en el ejercicio 5?
> Porque factor lineal racional equivale a raíz racional, y el teorema de los ceros racionales limita los candidatos a $\pm 1$ (coeficiente principal y término constante iguales a $1$).
