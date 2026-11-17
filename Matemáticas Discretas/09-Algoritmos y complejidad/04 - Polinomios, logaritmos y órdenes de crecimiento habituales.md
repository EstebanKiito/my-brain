---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[03 - Notaciones O, Ω y Θ]]"
---

# Polinomios, logaritmos y órdenes de crecimiento habituales

Con las definiciones de [[03 - Notaciones O, Ω y Θ]] se demuestran dos hechos que ahorran trabajo en casi todo análisis: en un polinomio **manda el mayor exponente** y en un logaritmo **la base no importa**. Con ellos se arma la lista de órdenes habituales.

## Constantes y términos menores

Para $f(n) = 60n^2$: es $\Theta(n^2)$ con $c = d = 60$. Para $f(n) = 60n^2 + 5n + 1$: si $n \ge 1$, $5n \le 5n^2$ y $1 \le n^2$, luego

$$60n^2 \le 60n^2 + 5n + 1 \le 66\,n^2,$$

así que $f \in \Theta(n^2)$ con $c = 60$, $d = 66$, $n_0 = 1$. Las constantes y los términos de menor grado no influyen.

> [!tip] Teorema del polinomio
> Si $f(n) = a_k n^k + \dots + a_1 n + a_0$ con $a_i \in \mathbb{R}$ y $a_k > 0$, entonces $f \in \Theta(n^k)$.

**Cota superior.** Como $x \le |x|$ y $n^i \le n^k$ para $n \ge 1$ e $i \le k$:
$f(n) \le \sum_i |a_i|\, n^i \le \big(\sum_i |a_i|\big)\, n^k$. Sirven $n_0 = 1$ y $c = \sum_i |a_i|$.

**Cota inferior.** Se toma $c = a_k / 2$ y se busca $n_0$ desde el cual $\tfrac{a_k}{2} n^k \le f(n)$. Esto equivale a $\tfrac{a_k}{2} n^k \ge -\sum_{i<k} a_i n^i$, y alcanza con $\tfrac{a_k}{2} n^k \ge \sum_{i<k} |a_i|\, n^i$. Dividiendo por $n^{k-1}$ y usando $n^{i-(k-1)} \le 1$, basta con $\tfrac{a_k}{2}\, n \ge \sum_{i<k} |a_i|$, o sea

$$n \ge n_0 = \frac{2}{a_k} \sum_{i=0}^{k-1} |a_i|.$$

## La base del logaritmo no importa

> [!tip] Teorema del logaritmo
> Si $a, b > 1$, entonces $\log_a n \in \Theta(\log_b n)$.

Sean $x = \log_a n$ e $y = \log_b n$. Entonces $a^x = n = b^y$; aplicando $\log_a$ se obtiene $x = y \cdot \log_a b$, es decir

$$\log_a n = \log_a(b) \cdot \log_b n \quad (n \ge 1).$$

Con $c = \log_a b$ (una constante) valen ambas desigualdades, así que $\log_2 n \in \Theta(\log_3 n)$ y en general se escribe simplemente $\Theta(\log n)$. Numéricamente, $\log_2 n = \log_2 3 \cdot \log_3 n \approx 1{,}585 \log_3 n$.

## Órdenes habituales

![Tabla de órdenes de crecimiento y sus nombres](adjuntos/Órdenes%20de%20crecimiento%20habituales.png)

> [!example]- Transcripción de la imagen
> Tabla de dos columnas, notación y nombre: $\Theta(1)$ constante; $\Theta(\log n)$ logarítmico; $\Theta(n)$ lineal; $\Theta(n \log n)$ "$n \log n$"; $\Theta(n^2)$ cuadrático; $\Theta(n^3)$ cúbico; $\Theta(n^k)$ polinomial; $\Theta(m^n)$ exponencial; $\Theta(n!)$ factorial. La nota al pie indica $k \ge 0$ y $m \ge 2$.

La lista va de menor a mayor crecimiento: $1 \prec \log n \prec n \prec n \log n \prec n^2 \prec n^3 \prec n^k \prec m^n \prec n!$. Para decidir qué algoritmo escala mejor basta comparar sus órdenes: uno cuadrático supera a uno $n \log n$ para $n$ suficientemente grande aunque tenga constante menor.

> [!warning] Las bases sí importan en exponenciales
> $\log_a n$ y $\log_b n$ son del mismo orden, pero $2^n$ **no** es $O(1{,}5^n)$, y $2^{2n} = 4^n \notin O(2^n)$. La equivalencia de bases es exclusiva de los logaritmos.

## Preguntas de repaso

> [!question]- ¿Por qué en $60n^2 + 5n + 1$ "manda" $n^2$?
> Porque para $n \ge 1$ los términos $5n$ y $1$ están acotados por múltiplos de $n^2$, de modo que la función queda entre $60n^2$ y $66n^2$.

> [!question]- ¿Por qué se puede escribir $\Theta(\log n)$ sin indicar base?
> Porque cambiar de base multiplica por una constante positiva ($\log_a b$), y $\Theta$ absorbe constantes.

> [!question]- ¿Por qué $n_0$ en la cota inferior del polinomio depende de los coeficientes?
> Porque debe ser lo bastante grande para que $\tfrac{a_k}{2} n$ supere la suma de coeficientes negativos y menores; con coeficientes grandes, el término líder tarda más en dominar.

> [!question]- ¿$n \log n$ es del orden de $n^2$?
> No. Es $O(n^2)$ pero no $\Omega(n^2)$: el cociente $\tfrac{n \log n}{n^2} = \tfrac{\log n}{n}$ tiende a $0$.
