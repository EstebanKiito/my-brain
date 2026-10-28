---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Complejidad algorítmica"
tags:
  - algoritmos/complejidad
  - algoritmos/notacion-asintotica
  - origen/complemento
prerrequisitos:
  - "[[01 - Contar operaciones|Contar operaciones]]"
---

# Crecimiento y notación asintótica

Un algoritmo puede hacer pocas operaciones para entradas pequeñas y muchas para entradas grandes. La **notación asintótica** describe ese comportamiento "en el largo plazo": qué pasa cuando $n$ crece mucho, sin preocuparse de las constantes ni de los términos pequeños.

## Por qué mirar el largo plazo

Comparemos dos funciones de costo:

- $20n + 1000$
- $n^2$

Para $n = 10$, la primera vale 1200 y la segunda 100; la primera es más cara. Pero para $n = 100$, la primera vale 3000 y la segunda 10.000; y para $n = 1000$, la primera vale 21.000 y la segunda 1.000.000.

![Comparación del crecimiento de 20n + 1000 y n²](adjuntos/Crecimiento%20de%20las%20funciones.png)

> [!example]- Transcripción de la imagen
> - El eje horizontal es el tamaño de la entrada $n$ (de 0 a 100).
> - El eje vertical es el número de operaciones (de 0 a 10.000).
> - La línea continua es $20n + 1000$; la línea segmentada es $n^2$.
> - Para $n$ pequeño, $20n + 1000$ puede ser mayor; para $n$ grande, $n^2$ crece mucho más rápido.

> [!tip] La idea central
> Para entradas grandes, el término de mayor crecimiento domina. Por eso $20n + 1000$ se considera $O(n)$ y $n^2$ se considera $O(n^2)$: las constantes y los términos menores dejan de importar.

## La notación O

Se escribe $f(n) = O(g(n))$ cuando, para $n$ suficientemente grande, $f$ crece a lo más como $g$, salvo una constante. En la práctica:

- Se eliminan las constantes multiplicativas: $5n$ es $O(n)$.
- Se eliminan los términos de menor grado: $n^2 + 3n + 1$ es $O(n^2)$.
- Se conserva el término que más crece.

## Tasas de crecimiento

| Notación | Nombre | Ejemplo típico |
|---|---|---|
| $O(1)$ | Constante | Acceder a `lista[0]` |
| $O(\log n)$ | Logarítmica | Búsqueda binaria |
| $O(n)$ | Lineal | Recorrer una lista |
| $O(n \log n)$ | Cuasilineal | Ordenar con mergesort |
| $O(n^2)$ | Cuadrática | Dos ciclos anidados sobre $n$ |
| $O(n^3)$ | Cúbica | Tres ciclos anidados |
| $O(2^n)$ | Exponencial | Probar todos los subconjuntos |
| $O(n!)$ | Factorial | Probar todas las permutaciones |

## Ejemplos con ciclos

- **Un ciclo de $n$ vueltas con 10 operaciones adentro:** $10n$, que es $O(n)$.
- **Dos ciclos anidados de $n$ vueltas:** $n \times n = n^2$, que es $O(n^2)$.
- **Un ciclo triangular:** $1 + 2 + \dots + n = n(n+1)/2$, que también es $O(n^2)$.
- **Búsqueda binaria:** en cada paso se descarta la mitad, así que el número de pasos es $\log_2 n$, $O(\log n)$.

> [!warning] La notación O no dice el tiempo exacto
> Un algoritmo $O(n)$ puede ser más lento que uno $O(n^2)$ para entradas pequeñas si tiene constantes grandes. La notación describe el crecimiento, no el tiempo en un caso concreto.

> [!tip] Para profundizar
> La definición formal de $O$, $\Omega$ y $\Theta$ está en [[03 - Notación asintótica O, Omega y Theta|Notación asintótica O, Omega y Theta]] de Estructuras de Datos. Aquí basta con la idea de crecimiento.

## Preguntas de repaso

> [!question]- ¿Por qué $20n + 1000$ se considera $O(n)$?
> Porque para $n$ grande el término $20n$ domina y la constante 1000 deja de importar. El crecimiento es lineal.

> [!question]- ¿Qué notación tiene un algoritmo con dos ciclos anidados de $n$ vueltas?
> $O(n^2)$, cuadrática: el número de operaciones crece con el cuadrado de $n$.

> [!question]- ¿Qué notación tiene la búsqueda binaria y por qué?
> $O(\log n)$, porque en cada paso descarta la mitad de los elementos. El número de pasos crece con el logaritmo de $n$.

> [!question]- ¿Un algoritmo $O(n)$ siempre es más rápido que uno $O(n^2)$?
> No siempre. Para entradas pequeñas, las constantes pueden hacer que el $O(n)$ sea más lento. La ventaja aparece cuando $n$ crece.
