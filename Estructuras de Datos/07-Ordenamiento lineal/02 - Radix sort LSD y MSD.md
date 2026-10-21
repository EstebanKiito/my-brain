---
ramo: "Estructuras de Datos"
tema: "Ordenamiento lineal"
tags:
  - edd
  - ordenamiento
  - radix-sort
  - orden-lineal
  - origen/complemento
prerrequisitos:
  - "[[01 - Ordenar sin comparar y counting sort]]"
---

# Radix sort LSD y MSD

[[01 - Ordenar sin comparar y counting sort|Counting sort]] solo sirve si el rango de valores es pequeño. Números de muchos dígitos, patentes de autos o direcciones IP tienen rangos enormes. **Radix sort** resuelve eso ordenando **por dígitos** (o caracteres): cada dígito tiene un rango chico, como 0–9 o una letra, y se ordena con counting sort. Es decir, se ordena **por columnas**. Antes de los computadores se hacía mecánicamente con tarjetas perforadas.

## LSD: del dígito menos significativo al más

Se ordena por el dígito **menos significativo** (las unidades), después por las decenas, y así. Después de ordenar $k$ dígitos, los datos están ordenados si solo se miran esos $k$ últimos dígitos. Basta con $d$ pasadas para un número de $d$ dígitos.

```
RadixSort(A, d):
    for j = 0 ... d-1:
        StableSort(A, j)        // por ejemplo counting sort sobre el dígito j: O(n + k)
// total O(d (n + k)); con d constante y k en O(n), O(n)
```

![Radix sort LSD por unidad, decena y centena](adjuntos/Radix%20sort%20LSD%20por%20unidad,%20decena%20y%20centena.png)

> [!example]- Transcripción de la imagen
> Cuatro columnas. "Arreglo inicial": 064, 008, 216, 512, 027, 729, 000, 001, 343, 125. "Ordenado por unidad": 000, 001, 512, 343, 064, 125, 216, 027, 008, 729. "Ordenado por decena": 000, 001, 008, 512, 216, 125, 027, 729, 343, 064. "Ordenado por centena": 000, 001, 008, 027, 064, 125, 216, 343, 512, 729. En cada columna, el dígito por el que se ordenó está en negrita.

> [!warning] La estabilidad es obligatoria
> Al ordenar por decenas, dos números con la misma decena deben conservar el orden que dejaron las unidades. Si el algoritmo interno no fuera estable, la pasada anterior se perdería. Por eso se usa **counting sort**, que es estable y lineal.

```python
def radix_lsd(A, d, base=10):
    for j in range(d):
        A = counting_sort(A, base - 1, lambda x: (x // base**j) % base)
    return A

print(radix_lsd([64, 8, 216, 512, 27, 729, 0, 1, 343, 125], 3))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

![Complejidad de radix sort](adjuntos/Complejidad%20de%20radix%20sort.png)

> [!example]- Transcripción de la imagen
> Si $A$ tiene $n$ datos naturales de $d$ dígitos y se usa un algoritmo estable lineal, y cada dígito puede tomar $k$ valores distintos, RadixSort toma tiempo $\Theta(d \cdot (n + k))$. Si $d$ es constante y $k \in \mathcal{O}(n)$, RadixSort es $\Theta(n)$.

Radix LSD **no es recursivo**. Con counting sort no es in place. Se podría usar un ordenamiento in place y estable como insertion sort, pero entonces cada pasada sería $O(n^2)$ y se perdería la linealidad.

## MSD: del más significativo, para largos distintos

LSD necesita que todos los datos tengan el **mismo largo** (patentes, IP, teléfonos), y conviene si ese largo es pequeño. Con strings de largo variable se usa **MSD**: se ordena por el **primer** carácter con counting sort y después, **recursivamente**, cada grupo por el carácter siguiente (excluyendo el primero, que dentro del grupo es igual para todos). Igual que en quicksort, los grupos se ordenan de forma independiente.

![Radix sort MSD sobre palabras](adjuntos/Radix%20sort%20MSD%20sobre%20palabras.png)

> [!example]- Transcripción de la imagen
> Columnas sucesivas sobre "she sells seashells by the sea shore the shells she sells are surely seashells". La primera pasada agrupa por la primera letra (are, by, she, sells, seashells, …, the, the) y cuadros punteados marcan el grupo de la "s", que se ordena recursivamente por la segunda letra, y luego el de "se" por la tercera. La última columna queda: are, by, sea, seashells, seashells, sells, sells, she, she, shells, shore, surely, the, the.

> [!tip] Cuidados con MSD
> - Si un string es **prefijo** de otro, va primero: she < shells. Las palabras que se acaban se colocan antes que el resto del grupo.
> - El alfabeto define $k$: binario, minúsculas, mayúsculas + minúsculas + dígitos, ASCII o Unicode. Con alfabetos grandes, cada counting sort es más caro.
> - Para subgrupos pequeños (por ejemplo, $\le 10$), conviene cambiar a insertion sort, sabiendo que los primeros caracteres ya son iguales.

> [!example] Aplicación: tráfico anormal entre direcciones IP
> Para detectar tráfico anormal desde IPs externas hacia una interna, se pueden ordenar millones de direcciones IP en **tiempo lineal** con radix sort LSD, porque todas tienen el mismo largo (4 bytes). Así, las direcciones de un mismo rango quedan juntas.

## Preguntas de repaso

> [!question]- ¿Por qué radix LSD empieza por el dígito menos significativo?
> Porque cada pasada estable conserva el orden de las anteriores. Al terminar con el más significativo, este decide el orden final, y entre los empatados manda lo que dejaron los dígitos menores.

> [!question]- ¿Qué pasa si el algoritmo interno de radix sort no es estable?
> Cada pasada podría desordenar lo logrado por las pasadas anteriores entre elementos con el mismo dígito, y el resultado final no quedaría ordenado.

> [!question]- ¿Cuándo conviene MSD en vez de LSD?
> Cuando los datos tienen largos distintos, como palabras. MSD ordena por el primer carácter y recursa en cada grupo, manejando de forma natural los prefijos.

> [!question]- ¿Cuál es la complejidad de radix sort y cuándo es lineal?
> $\Theta(d(n + k))$, con $d$ el número de dígitos y $k$ los valores por dígito. Es lineal cuando $d$ es constante y $k \in O(n)$.
