---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[01 - Algoritmos, pseudocódigo e invariantes de ciclo]]"
---

# Notaciones O, Ω y Θ

Que un algoritmo sea correcto no dice si sirve en la práctica: hay que saber cuánto tarda. El tiempo exacto depende del lenguaje, del compilador y del hardware, así que se estudia cómo **crece** el tiempo al aumentar el tamaño de la entrada. La notación asintótica da el lenguaje para eso.

## Funciones de costo

Se trabaja con funciones $f : \mathbb{N} \to \mathbb{R}^+$. El dominio es el **tamaño de la entrada** $n$ y el valor es el tiempo (o la cantidad de operaciones relevantes) que el algoritmo necesita. Lo que importa es la forma de la curva para $n$ grande, no el valor puntual.

## Las tres definiciones

Para $f : \mathbb{N} \to \mathbb{R}^+$ se definen tres conjuntos de funciones:

$$O(f) = \{\, g \mid \exists c > 0\ \exists n_0\ \forall n \ge n_0:\ g(n) \le c \cdot f(n) \,\}$$

$$\Omega(f) = \{\, g \mid \exists c > 0\ \exists n_0\ \forall n \ge n_0:\ g(n) \ge c \cdot f(n) \,\}$$

$$\Theta(f) = O(f) \cap \Omega(f)$$

> [!tip] Cómo leerlas
> $g \in O(f)$: $g$ crece **a lo más** como $f$ (cota superior). $g \in \Omega(f)$: crece **al menos** como $f$ (cota inferior). $g \in \Theta(f)$: crece **igual** que $f$, salvo una constante. Se escribe $g \in O(f)$ o "$g$ es $O(f)$".

Las constantes $c$ y $n_0$ se eligen una sola vez, antes de tomar $n$: "para $n$ grande" quiere decir desde un $n_0$ fijo en adelante.

## Θ con dos constantes

$g \in \Theta(f)$ si y solo si existen $c, d > 0$ y $n_0$ tales que

$$\forall n \ge n_0:\quad c \cdot f(n) \le g(n) \le d \cdot f(n).$$

En efecto, $g \in O(f)$ aporta $d$ y $n_1$, $g \in \Omega(f)$ aporta $c$ y $n_2$; basta tomar $n_0 = \max\{n_1, n_2\}$. Es decir, $g$ queda **encerrada** entre dos múltiplos de $f$.

## Ejemplo resuelto

Se quiere $g(n) = 3n + 10 \in O(n)$. Con $c = 4$ y $n_0 = 10$: para $n \ge 10$, $3n + 10 \le 3n + n = 4n$. Por otra parte, $3n + 10 \ge 3n$ para todo $n$, así que con $c = 3$ también $g \in \Omega(n)$ y por lo tanto $g \in \Theta(n)$.

Para refutar $n^2 \in O(n)$: si existieran $c, n_0$ con $n^2 \le cn$ para todo $n \ge n_0$, dividir por $n$ da $n \le c$, falso para $n > c$.

## Resultados útiles que siguen de la definición

| Propiedad | Idea de la demostración |
|---|---|
| $\Theta$ es **reflexiva**: $f \in \Theta(f)$ | $c = d = 1$ |
| $\Theta$ es **simétrica**: $f \in \Theta(g) \Rightarrow g \in \Theta(f)$ | de $c g \le f \le d g$ sale $\tfrac{1}{d} f \le g \le \tfrac{1}{c} f$ |
| $\Theta$ es **transitiva** | se multiplican las constantes: $c_1 c_2 h \le f \le d_1 d_2 h$ |
| Si $f_1 \in O(g_1)$ y $f_2 \in O(g_2)$, entonces $f_1 + f_2 \in O(\max\{g_1, g_2\})$ | con $C = c_1 + c_2$ y $n_0 = \max$ de los umbrales |

Las tres primeras muestran que $f \sim g \iff f \in \Theta(g)$ es una relación de equivalencia entre funciones: las clases agrupan funciones que "crecen igual".

> [!warning] "Crece más lento o igual" no es "menor"
> $g \in O(f)$ no significa $g(n) \le f(n)$; admite una constante $c$ arbitrariamente grande y solo desde un $n_0$. Por ejemplo $1000n \in O(n)$ aunque $1000n > n$ siempre.

## Preguntas de repaso

> [!question]- ¿Por qué la definición de $O$ tiene $\exists c\ \exists n_0$ antes de $\forall n$?
> Porque las constantes deben ser fijas, independientes de $n$. Si pudieran depender de $n$, toda función sería $O$ de toda otra.

> [!question]- ¿Es cierto que $g \in \Theta(f)$ implica $g \in O(f)$ y $f \in O(g)$?
> Sí. De $c f \le g \le d f$ se obtiene $g \le d f$ y también $f \le \tfrac{1}{c} g$, lo que muestra la simetría de $\Theta$.

> [!question]- ¿Por qué se ignoran los valores de $g$ para $n < n_0$?
> Porque el interés es el comportamiento al crecer la entrada; un número finito de casos iniciales no cambia la forma de la curva y se absorbe en el $n_0$.

> [!question]- ¿Qué se concluye si $f \in O(g)$ y $g \in O(f)$?
> Que $f \in \Theta(g)$: cada una es cota superior de la otra, y eso da las dos desigualdades de la definición con constantes $d$ y $1/c$.
