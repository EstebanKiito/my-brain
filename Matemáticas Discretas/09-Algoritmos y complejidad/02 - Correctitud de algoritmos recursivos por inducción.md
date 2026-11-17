---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[01 - Algoritmos, pseudocódigo e invariantes de ciclo]]"
  - "[[03 - Inducción fuerte]]"
---

# Correctitud de algoritmos recursivos por inducción

En un algoritmo recursivo no hay ciclo que invariar: la propia llamada recursiva es la hipótesis inductiva. Por eso basta probar la propiedad deseada por inducción, casi siempre sobre el tamaño de la entrada.

## Por qué no hace falta separar terminación

Cada llamada recursiva trabaja sobre una entrada de tamaño estrictamente menor, y el caso base no llama a nadie. Esa es exactamente la estructura de una inducción: probar el caso base y suponer que las llamadas más chicas son correctas. Si la inducción funciona, el algoritmo no puede recursar para siempre porque el tamaño es natural y decrece.

> [!tip] Receta
> 1. Enunciar $P(i)$: "la llamada con entrada de tamaño $i$ devuelve lo correcto".
> 2. **Base:** el tamaño mínimo (la rama sin recursión) cumple $P$.
> 3. **Paso:** una llamada de tamaño mayor hace llamadas de tamaño menor; por HI estas son correctas, y se argumenta que la combinación (el `if`, el `return`) también lo es, con un análisis por casos.

## Ejemplo: máximo de un arreglo

Se pide $m = \max(A)$ para $A = [a_0, \dots, a_{n-1}]$ con $n \ge 1$.

![Algoritmo recursivo RecMax](adjuntos/Algoritmo%20recursivo%20RecMax.png)

> [!example]- Transcripción de la imagen
> - Entrada: arreglo $A = [a_0,\dots,a_{n-1}]$ y largo $n \ge 1$; salida $m = \max(A)$.
> - `RecMax(A, n)`: si $n = 1$ devuelve $a_0$; si no, `k ← RecMax(A, n−1)` y luego, si $a_{n-1} \ge k$ devuelve $a_{n-1}$, y en caso contrario devuelve $k$.
> - Aclaración: `RecMax(A, i)` solo considera el tramo $[a_0,\dots,a_{i-1}]$.

El invariante sobre el número de elementos considerados es

$$P(i):\ \text{RecMax}(A, i) \ge a_0, a_1, \dots, a_{i-1}$$

es decir, el valor devuelto es mayor o igual que cada uno de los $i$ primeros elementos (y además es uno de ellos, por construcción, lo que lo hace el máximo).

- **Base** ($i = 1$): devuelve $a_0 \ge a_0$.
- **HI:** `RecMax(A, i)` $\ge a_0, \dots, a_{i-1}$.
- **Paso:** con $i + 1$ elementos no se está en el caso base, así que se llama a `RecMax(A, i)` y se guarda en $k$; por HI $k \ge a_0,\dots,a_{i-1}$. Hay dos casos en el `if`:
  - $a_i \ge k$: se devuelve $a_i$, que por transitividad es $\ge a_0, \dots, a_{i-1}$ y también $\ge a_i$.
  - $a_i < k$: se devuelve $k$, que es $\ge a_0,\dots,a_{i-1}$ por HI y $\ge a_i$ por el caso.

En ambos casos el valor devuelto domina a los $i + 1$ elementos y es uno de ellos: $P(i+1)$.

## Cuándo usar inducción fuerte

Si la llamada recursiva se hace sobre una fracción de la entrada (por ejemplo, la mitad en una búsqueda binaria), $P(n)$ depende de $P(\lfloor n/2 \rfloor)$ y no de $P(n-1)$. Ahí corresponde inducción fuerte, como en [[03 - Inducción fuerte]]: se supone la propiedad para todos los tamaños menores a $n$.

> [!warning] El caso base también es parte del algoritmo
> En `RecMax` la rama $n = 1$ evita acceder a un arreglo vacío. Una demostración correcta debe cubrir todas las ramas de terminación del código, no solo la más obvia.

## Preguntas de repaso

> [!question]- ¿Por qué en recursión basta la inducción y no hace falta probar terminación aparte?
> Porque la inducción sobre el tamaño ya usa que las llamadas son sobre entradas menores, que es lo que impide la recursión infinita.

> [!question]- ¿Qué papel juega la hipótesis inductiva en `RecMax`?
> Garantiza que `k`, devuelto por la llamada sobre los primeros $i$ elementos, ya es mayor o igual que todos ellos; el paso solo compara $k$ con el elemento nuevo.

> [!question]- ¿Cuándo se necesita inducción fuerte en vez de simple?
> Cuando la llamada recursiva no es sobre $n-1$ sino sobre otros tamaños menores (mitades, divisores), de modo que la HI debe cubrir todos los valores menores.

> [!question]- ¿Qué falla si el código tuviera `>` en vez de `>=` en la comparación de `RecMax`?
> Nada: con elementos iguales devuelve $k$ en vez de $a_{n-1}$, pero ambos valen lo mismo, así que el máximo es correcto. El invariante solo exige $\ge$.
