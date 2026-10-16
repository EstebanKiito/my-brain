---
ramo: "Estructuras de Datos"
tema: "Análisis de algoritmos"
tags:
  - edd
  - complejidad
  - notacion-asintotica
  - origen/complemento
prerrequisitos:
  - "[[02 - Correctitud de algoritmos]]"
---

# Notación asintótica O, Ω y Θ

Un algoritmo correcto puede ser inútil si con un millón de datos tarda años. Para comparar algoritmos sin depender del computador ni del lenguaje, se describe cómo **crece** su costo en función del tamaño del input $n$. La notación asintótica mide así el tiempo, la memoria y la **escalabilidad**, ignorando constantes y valores pequeños de $n$.

## Las tres cotas

**Notación O: cota superior.** $f \in O(g)$ si existen $c > 0$ y $n_0 \in \mathbb{N}$ tales que $f(n) \le c \cdot g(n)$ para todo $n \ge n_0$. Se lee "$f$ crece a lo más como $g$". Que un tiempo de ejecución sea $O(n)$ significa que, para $n$ suficientemente grande, hace **a lo más** del orden de $n$ pasos.

![Cota superior O](adjuntos/Gr%C3%A1fico%20de%20la%20cota%20superior%20O.png)

> [!example]- Transcripción de la imagen
> Gráfico con $n$ en el eje horizontal. La curva $f(n)$ oscila al principio y en algunos tramos supera a $c\,g(n)$, pero desde la línea punteada $n_0$ queda siempre bajo $c\,g(n)$. Leyenda: $f(n) = O(g(n))$.

**Notación Ω: cota inferior.** $f \in \Omega(g) \iff g \in O(f)$. Es decir, existen $c > 0$ y $n_0$ con $f(n) \ge c \cdot g(n)$ para todo $n \ge n_0$. Se lee "$f$ crece al menos como $g$". $\Omega(n)$ significa **a lo menos** del orden de $n$ pasos.

![Cota inferior Omega](adjuntos/Gr%C3%A1fico%20de%20la%20cota%20inferior%20Omega.png)

> [!example]- Transcripción de la imagen
> Gráfico con $f(n)$ y $c\,g(n)$. Antes de $n_0$ las curvas se cruzan; desde $n_0$, $f(n)$ queda siempre por encima de $c\,g(n)$. Leyenda: $f(n) = \Omega(g(n))$.

**Notación Θ: cota ajustada.** $f \in \Theta(g) \iff f \in O(g) \wedge f \in \Omega(g)$. Hay constantes $c_1, c_2 > 0$ y un $n_0$ con $c_1 g(n) \le f(n) \le c_2 g(n)$ para $n \ge n_0$: $f$ y $g$ **crecen igual**. Para demostrar que una función está en $\Theta(g)$ hay que encontrar **dos** constantes y mostrar que la acotan por ambos lados.

![Cota ajustada Theta](adjuntos/Gr%C3%A1fico%20de%20la%20cota%20ajustada%20Theta.png)

> [!example]- Transcripción de la imagen
> Tres curvas: $c_2\,g(n)$ arriba, $f(n)$ al medio y $c_1\,g(n)$ abajo. Antes de $n_0$, $f(n)$ se sale de la franja; desde $n_0$ queda siempre entre ambas. Leyenda: $f(n) = \Theta(g(n))$.

> [!warning] El $n_0$ importa
> Las definiciones solo hablan de lo que pasa **desde** $n_0$. Antes, $f$ puede quedar fuera de la cota (los gráficos lo muestran a propósito). Por eso un algoritmo $O(n^2)$ puede ganarle a uno $O(n \log n)$ con pocos datos.

## Ejemplo: $3n^2 + 5n \in \Theta(n^2)$

Con $c_1 = 3$ la cota inferior vale siempre: $3n^2 \le 3n^2 + 5n$. Para la superior se elige $c_2 = 4$, y $3n^2 + 5n \le 4n^2 \iff 5n \le n^2 \iff n \ge 5$, así que $n_0 = 5$.

```python
f = lambda n: 3 * n**2 + 5 * n
g = lambda n: n**2
c1, c2, n0 = 3, 4, 5
print(all(c1 * g(n) <= f(n) <= c2 * g(n) for n in range(n0, 10**5)))  # True
print([n for n in range(1, n0) if f(n) > c2 * g(n)])                   # [1, 2, 3, 4]
```

La segunda línea muestra que antes de $n_0$ la cota superior efectivamente falla.

## Cómo se calcula la complejidad de un algoritmo

Interesan dos funciones del tamaño del input: el **tiempo** $T(n)$ y la **memoria adicional** $M(n)$. El tiempo suele ser la prioridad, pero siempre se cumple $T \in \Omega(M)$, porque usar memoria exige al menos escribirla.

- **Etapas sucesivas se suman:** si un algoritmo hace una etapa $O(n)$ y después otra $O(n^2)$, el total es $O(n + n^2)$.
- **Un paso repetido se multiplica:** un paso de costo $O(n)$ que se repite $n$ veces aporta $O(n^2)$.
- **Al sumar, domina el término que crece más rápido:** $O(n + n^2) = O(n^2)$.

> [!tip] Para recordar
> O = techo ("a lo más"), Ω = piso ("a lo menos"), Θ = las dos a la vez ("exactamente ese orden").

> [!warning] O no es lo mismo que "peor caso"
> El peor, mejor y caso promedio son **situaciones de input**; O, Ω y Θ son **cotas de funciones**. Se puede dar una cota Θ del peor caso (por ejemplo, $\Theta(n^2)$ para insertion sort) y otra distinta del mejor caso ($\Theta(n)$).

## Preguntas de repaso

> [!question]- ¿Por qué la notación asintótica ignora las constantes multiplicativas?
> Porque dependen del hardware, del lenguaje y de la implementación, mientras que la forma de crecimiento depende solo del algoritmo. Para $n$ grande, la diferencia entre $n^2$ y $n \log n$ supera cualquier constante.

> [!question]- ¿Qué hay que exhibir para demostrar que $f \in \Theta(g)$?
> Dos constantes positivas $c_1$ y $c_2$ y un $n_0$ tales que $c_1 g(n) \le f(n) \le c_2 g(n)$ para todo $n \ge n_0$. Equivale a probar a la vez $f \in O(g)$ y $f \in \Omega(g)$.

> [!question]- ¿Por qué el tiempo de un algoritmo es siempre Ω de su memoria adicional?
> Porque cada celda de memoria adicional que se usa hay que escribirla al menos una vez, y cada escritura cuesta tiempo. Un algoritmo no puede usar $M(n)$ memoria en menos de $\Omega(M(n))$ pasos.

> [!question]- Un algoritmo hace un ciclo de $n$ iteraciones con un paso $O(1)$ y después ordena con un método $O(n \log n)$. ¿Cuál es su complejidad?
> Las etapas se suman: $O(n) + O(n \log n) = O(n \log n)$, porque domina el término que crece más rápido.
