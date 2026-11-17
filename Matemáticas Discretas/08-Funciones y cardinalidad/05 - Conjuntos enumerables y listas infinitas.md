---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/cardinalidad
  - origen/complemento
prerrequisitos:
  - "[[04 - Equinumerosidad, conjuntos finitos y principio del palomar]]"
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Conjuntos enumerables y listas infinitas

Con la biyección como medida, aparece un hecho que contradice la intuición: un conjunto infinito puede ser equinumeroso con una parte propia suya. Los conjuntos infinitos "más pequeños" son los que se pueden poner en una lista, y resultan ser sorprendentemente abundantes.

## Definición: tantos como los naturales

Un conjunto $A$ es **enumerable** (o **numerable**) si $A \approx \mathbb{N}$, es decir, si $\lvert A \rvert = \lvert \mathbb{N} \rvert$. Es lo mismo que poder escribir todos sus elementos en una **lista infinita** $(a_0, a_1, a_2, \dots)$ en la que cada elemento aparece exactamente una vez: la biyección es $n \mapsto a_n$ (y su inversa $a_i \mapsto i$).

> [!tip] Enumerar es listar
> Para probar que $A$ es enumerable basta un criterio sin fórmulas: describir un procedimiento que, esperando lo suficiente, imprima cada elemento de $A$ una sola vez. Para probar que **no** lo es hay que mostrar que ninguna lista puede completarse.

## Los pares y los enteros

Los naturales pares $P = \{2k \mid k \in \mathbb{N}\}$ son una parte propia de $\mathbb{N}$, y sin embargo $f(n) = 2n$ es una biyección $\mathbb{N} \to P$: hay tantos pares como naturales. Lo mismo ocurre con los impares ($n \mapsto 2n + 1$).

Para $\mathbb{Z}$ se alternan los signos, enviando los pares a los enteros no negativos y los impares a los negativos:

$$f(n) = \begin{cases} n/2 & n \text{ par} \\ -(n+1)/2 & n \text{ impar} \end{cases} \qquad (0, 1, 2, 3, 4, \dots \mapsto 0, -1, 1, -2, 2, \dots)$$

Es inyectiva y sobreyectiva, así que $\lvert \mathbb{Z} \rvert = \lvert \mathbb{N} \rvert$.

![Biyección entre Z y los enteros pares](adjuntos/Biyecci%C3%B3n%20entre%20Z%20y%20los%20enteros%20pares.png)

> [!example]- Transcripción de la imagen
> Dos óvalos con puntos conectados por flechas horizontales: a la izquierda $\mathbb{Z}$ ($\dots, 3, 2, 1, 0, -1, -2, -3, \dots$) y a la derecha $2\mathbb{Z}$ ($\dots, 6, 4, 2, 0, -2, -4, -6, \dots$); la flecha $H$ lleva cada $n$ a $2n$. Muestra que cada entero tiene un par distinto y que todo par es imagen de alguien.

![Contar los enteros alternando signo](adjuntos/Contando%20los%20enteros%20alternando%20signo.png)

> [!example]- Transcripción de la imagen
> Sobre la recta de los enteros $\dots, -5, -4, \dots, 4, 5, \dots$ cada uno lleva debajo el orden en que se "cuenta": $0$ es el primero, $1$ el segundo, $-1$ el tercero, $2$ el cuarto, $-2$ el quinto, y así. Los arcos con flechas muestran el vaivén que alterna positivos y negativos.

## Pares de naturales, racionales y tuplas

Listar $\mathbb{N} \times \mathbb{N}$ por filas o por columnas no sirve (nunca se termina la primera fila). La solución es recorrer la tabla infinita **por diagonales**, agrupando los pares cuya suma es $0, 1, 2, \dots$ (cada grupo es finito):

$$(0,0),\ (0,1), (1,0),\ (0,2), (1,1), (2,0),\ (0,3), \dots$$

El par $(i, j)$ queda en la posición $\tfrac{(i+j)(i+j+1)}{2} + i$ de la lista, una biyección explícita con $\mathbb{N}$.

![Recorrido en diagonal de la tabla de fracciones](adjuntos/Recorrido%20en%20diagonal%20de%20las%20fracciones.png)

> [!example]- Transcripción de la imagen
> Tabla infinita con la fracción $\tfrac{i}{j}$ en la fila $i$ y la columna $j$ (primera fila $\tfrac11, \tfrac12, \tfrac13, \dots$; primera columna $\tfrac11, \tfrac21, \tfrac31, \dots$). Flechas azules recorren las diagonales en zigzag, empezando en $\tfrac11$; las fracciones ya contadas, como $\tfrac22$ o $\tfrac24$, se saltan.

- **Racionales.** Cada $a/b$ aparece repetido ($\tfrac12 = \tfrac24$). Se recorre la misma tabla pero solo se anota cada fracción **irreducible**: $0, \tfrac11, \tfrac12, \tfrac21, \tfrac13, \tfrac31, \tfrac14, \tfrac23, \dots$ (con los negativos intercalados como en $\mathbb{Z}$). Así $\mathbb{Q} \approx \mathbb{N}$, aunque entre dos racionales siempre haya otro.
- **Tuplas $\mathbb{N}^n$.** Por inducción en $n$: la base es $\mathbb{N}^2$; si $\mathbb{N}^n$ tiene lista $(a_0, a_1, \dots)$, los elementos de $\mathbb{N}^{n+1} = \mathbb{N}^n \times \mathbb{N}$ son pares $(a_i, k)$ y se recorren por diagonales ($i + k$ creciente).
- **Programas y textos.** Todas las cadenas finitas sobre un alfabeto finito se listan por largo creciente, y dentro de cada largo, de cualquier manera; se filtran las que son programas válidos. Por eso hay solo una cantidad enumerable de programas en cualquier lenguaje.

## Unión y subconjuntos

- Si $A$ y $B$ son enumerables y disjuntos, con listas $(a_i)$ y $(b_i)$, la lista $a_0, b_0, a_1, b_1, \dots$ enumera $A \cup B$ (si no fueran disjuntos se omiten los repetidos).
- Todo subconjunto infinito de un conjunto enumerable es enumerable: se recorre la lista original y se conservan solo los elementos del subconjunto, en el orden en que aparecen.

> [!warning] Enumerable no es "con una fórmula bonita"
> Existen conjuntos enumerables cuya lista no puede generarla ningún programa; para probar enumerabilidad basta que la lista exista, aunque en la práctica casi siempre se describe un procedimiento.

## Preguntas de repaso

> [!question]- ¿Por qué no sirve listar $\mathbb{N} \times \mathbb{N}$ fila por fila?
> Porque la primera fila ya es infinita: la lista nunca llegaría a $(1, 0)$. Recorrer por diagonales asegura que cada par aparezca tras un número finito de pasos.

> [!question]- ¿Cómo se pasa de $\mathbb{N} \times \mathbb{N}$ a $\mathbb{Q}$?
> Cada racional es un par $a/b$ y se recorre la misma tabla; para que cada número aparezca una sola vez se omiten las fracciones no reducidas y se intercalan los signos como en $\mathbb{Z}$.

> [!question]- ¿Qué muestra la biyección $n \mapsto 2n$ sobre la intuición de "la parte es menor que el todo"?
> Que vale para finitos pero no para infinitos: $\mathbb{N}$ es equinumeroso con una parte propia suya, los pares. En conjuntos infinitos el tamaño no se mide por inclusión sino por biyecciones.
