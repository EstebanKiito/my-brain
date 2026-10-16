---
ramo: "Estructuras de Datos"
tema: "Quicksort"
tags:
  - edd
  - quicksort
  - complejidad
  - caso-promedio
  - origen/complemento
prerrequisitos:
  - "[[04 - Partition in place y correctitud de quicksort]]"
---

# Complejidad y mejoras de quicksort

Partition cuesta $O(n)$. El costo total de quicksort depende de **dónde cae cada pivote**: si divide al medio, el árbol de recursión es balanceado como el de mergesort; si cae en un extremo, el árbol es una línea de largo $n$.

## Mejor y peor caso

![Mejor y peor caso de quicksort](adjuntos/Mejor%20y%20peor%20caso%20de%20quicksort.png)

> [!example]- Transcripción de la imagen
> **Mejor caso**: Partition genera sub-secuencias del mismo tamaño; la recurrencia es $T(n) = n + 2T(n/2)$, igual que en mergesort, y la complejidad es $\mathcal{O}(n \log n)$. **Peor caso**: Partition genera sub-secuencias de tamaño $0$ y $n-1$; la recurrencia es $T(n) = n + T(n-1)$ y la complejidad es $\mathcal{O}(n^2)$.

![Árbol de recursión del peor y mejor caso](adjuntos/Pizarra%20-%20%C3%A1rbol%20de%20recursi%C3%B3n%20del%20peor%20y%20mejor%20caso.png)

> [!example]- Transcripción de la imagen
> Foto de pizarra. Arriba, un arreglo dividido en celdas. Abajo a la izquierda, un triángulo rectángulo con altura $n$ (peor caso: cada nivel quita un solo elemento). Al centro, un triángulo isósceles invertido con altura $\log(n)$ (mejor caso: divisiones al medio). A la derecha, una partición con el pivote $P$ y flechas hacia los menores y los mayores.

## Caso promedio: $O(n \log n)$

Si el pivote termina en la posición $q$, Partition hace $n-1$ comparaciones y los llamados recursivos aportan $C(q) + C(n-q-1)$:

![Comparaciones según la posición del pivote](adjuntos/Comparaciones%20de%20quicksort%20seg%C3%BAn%20la%20posici%C3%B3n%20del%20pivote.png)

> [!example]- Transcripción de la imagen
> Junto al pseudocódigo de Partition: en la primera llamada se hacen $n-1$ comparaciones ($i = 0$, $f = n-1$). Si Partition deja el pivote en $A[q]$, las llamadas recursivas se hacen sobre $q$ elementos a la izquierda y $n-q-1$ a la derecha, y aportan $C(q) + C(n-q-1)$.

Como el pivote es aleatorio, cada $q$ tiene probabilidad $1/n$. Al promediar:

![Recurrencia del caso promedio](adjuntos/Recurrencia%20del%20caso%20promedio%20de%20quicksort.png)

> [!example]- Transcripción de la imagen
> $C(n) = n - 1 + \frac{1}{n}\sum_{q=0}^{n-1}(C(q) + C(n-q-1))$. Como $\sum_{q=0}^{n-1} C(n-q-1) = \sum_{q=0}^{n-1} C(q)$, queda la regla simplificada $C(n) = n - 1 + \frac{2}{n}\sum_{q=0}^{n-1} C(q)$.

![Cota del caso promedio](adjuntos/Cota%20del%20caso%20promedio%20de%20quicksort.png)

> [!example]- Transcripción de la imagen
> Final de la cota: $\le \frac{C(1)}{2} + \sum_{k=2}^{n}\frac{2}{k+1} \le \sum_{k=1}^{n}\frac{2}{k} \le \int_1^n \frac{2}{x}\,dx = 2\log(n)$. "Concluimos que una cota superior para el número de comparaciones es $C(n) \le 2(n+1)\log(n)$". "Quicksort es $\mathcal{O}(n\log(n))$ en el caso promedio".

El truco del final es acotar la suma armónica por una **integral**, que da un logaritmo. En la práctica:

```python
# comparaciones de quicksort (n = 2000) contra n(n-1)/2 = 1999000 y 2 n ln n ≈ 30404
# ordenado, pivote fijo al final:   1999000   <- peor caso exacto
# ordenado, pivote aleatorio:         ~26700
# al azar, pivote aleatorio:          ~24900
```

## Resumen y mejoras

![Tabla de complejidad antes de quicksort](adjuntos/Tabla%20de%20complejidad%20antes%20de%20quicksort.png)

> [!example]- Transcripción de la imagen
> La tabla de complejidad con selection, insertion y merge sort completos, y quick sort y heap sort con "?" en todas las columnas.

![Tabla de complejidad con quicksort](adjuntos/Tabla%20de%20complejidad%20con%20quicksort.png)

> [!example]- Transcripción de la imagen
> La misma tabla, ahora con quick sort: mejor caso $\mathcal{O}(n\log n)$, caso promedio $\mathcal{O}(n\log n)$, peor caso $\mathcal{O}(n^2)$, memoria adicional $\mathcal{O}(1)$. Heap sort sigue con "?".

> [!warning] La memoria $O(1)$ no cuenta la recursión
> Quicksort no usa memoria extra para los datos, pero la pila de llamadas recursivas ocupa $O(\log n)$ en promedio y $O(n)$ en el peor caso.

Mejoras habituales:

- **No usar quicksort en tramos pequeños:** bajo cierto tamaño, insertion sort es más rápido porque no paga recursión.
- **Mediana de tres:** tomar como pivote la mediana de tres elementos $A[k_1], A[k_2], A[k_3]$. Se calcula en $O(1)$ y hace muy improbable un pivote extremo.
- **Partición en tres:** separar en **menores, iguales y mayores**. Con muchos repetidos, los iguales quedan listos de una vez y no se vuelven a procesar.

## Preguntas de repaso

> [!question]- Escribir las recurrencias del mejor y del peor caso de quicksort y sus soluciones.
> Mejor caso: $T(n) = n + 2T(n/2)$, que da $O(n \log n)$. Peor caso: $T(n) = n + T(n-1)$, que da $O(n^2)$.

> [!question]- ¿Por qué en el caso promedio cada posición $q$ del pivote tiene probabilidad $1/n$?
> Porque el pivote se elige uniformemente al azar entre los $n$ elementos, y su posición final es su rango en la secuencia ordenada.

> [!question]- ¿Qué problema resuelve la partición en tres (menores, iguales, mayores)?
> El de los datos con muchos repetidos: con dos grupos, los iguales al pivote se vuelven a particionar una y otra vez. Con tres, quedan ubicados de una sola vez.

> [!question]- ¿Por qué se dice que quicksort es $O(1)$ en memoria si es recursivo?
> Porque no copia los datos a estructuras auxiliares. La pila de recursión sí ocupa espacio: $O(\log n)$ en promedio y $O(n)$ en el peor caso.
