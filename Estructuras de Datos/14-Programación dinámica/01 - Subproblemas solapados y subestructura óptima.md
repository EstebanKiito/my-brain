---
ramo: "Estructuras de Datos"
tema: "Programación dinámica"
tags:
  - edd
  - programacion-dinamica
  - optimizacion
  - recurrencias
  - origen/complemento
prerrequisitos:
  - "[[02 - Mochila fraccional y contraejemplos]]"
  - "[[02 - Mergesort y su recurrencia]]"
---

# Subproblemas solapados y subestructura óptima

Backtracking resuelve optimización, pero es lento. Un algoritmo codicioso es rápido, pero solo funciona si existe un buen criterio, y muchas veces no existe. La **programación dinámica** (PD) combina ideas de **dividir para conquistar** y de backtracking: descompone el problema en subproblemas, explora las dos opciones de cada decisión ("con" y "sin" un elemento) y, sobre todo, **recuerda** lo que ya calculó. Así no repite trabajo y puede llegar a ser lineal.

> [!tip] Las dos condiciones
> - **Subestructura óptima:** la solución óptima del problema se construye con soluciones óptimas de subproblemas más pequeños.
> - **Subproblemas solapados:** los subproblemas se repiten, es decir, comparten sub-subproblemas. Esa es la diferencia con dividir para conquistar, donde los subproblemas son **disjuntos**.
>
> "La clave de la programación dinámica es **recordar** las soluciones a los subproblemas".

> [!example] Intuición: la barcaza
> Se suben autos a una barcaza sin pasar su peso máximo, y cada ticket tiene un valor. La PD toma el primer auto y evalúa las dos ramas, **con** y **sin** él; en cada rama hace lo mismo con el segundo, y así sucesivamente. El árbol de posibilidades es enorme, pero muchas configuraciones (mismo auto pendiente, misma capacidad restante) se **repiten** en distintas ramas. La PD calcula cada una una sola vez y la reutiliza.

## Ejemplo: charlas con ganancias

![Problema de asignar charlas con ganancias](adjuntos/Problema%20de%20asignar%20charlas%20con%20ganancias.png)

> [!example]- Transcripción de la imagen
> Se quieren asignar charlas en una misma sala. Hay $n$ charlas; la charla $i$ tiene hora de inicio $s_i$ y de término $f_i$, es decir, el intervalo $[s_i, f_i)$. Solo se puede realizar una charla a la vez y, además, la charla $i$ produce una ganancia $v_i$. "¿Qué charlas asignar de manera que maximicemos la ganancia?".

![Instancia de 6 charlas con ganancias](adjuntos/Instancia%20de%206%20charlas%20con%20ganancias.png)

> [!example]- Transcripción de la imagen
> $i = 1$: $[0, 5)$, $v_1 = 2$; $i = 2$: $[1, 7)$, $v_2 = 4$; $i = 3$: $[6, 9)$, $v_3 = 4$; $i = 4$: $[2, 11)$, $v_4 = 7$; $i = 5$: $[9, 12)$, $v_5 = 2$; $i = 6$: $[10, 13)$, $v_6 = 1$. Debajo, las seis barras en una línea de tiempo.

Sin ganancias, elegir siempre la charla que **termina primero** maximiza la cantidad de charlas. Con ganancias, ese criterio codicioso falla:

![La estrategia codiciosa no es óptima con ganancias](adjuntos/La%20estrategia%20codiciosa%20no%20es%20%C3%B3ptima%20con%20ganancias.png)

> [!example]- Transcripción de la imagen
> Instancia con tres charlas: $i = 1$ con $v_1 = 1$, $i = 2$ con $v_2 = 4$ (que se superpone con las otras dos) e $i = 3$ con $v_3 = 2$. La estrategia codiciosa elige $\{1, 3\}$ con ganancia 3; la óptima es $\{2\}$, con ganancia 4. "Nuestra estrategia codiciosa no es óptima en el caso general del problema con ganancias".

## La recurrencia

Se ordenan las charlas por hora de término y se define $b(i)$, la última charla compatible antes de $i$:

![Definición de b(i)](adjuntos/Definici%C3%B3n%20de%20b%28i%29.png)

> [!example]- Transcripción de la imagen
> Dadas las charlas $\{1, \dots, 6\}$ ordenadas por $f_i$, $b(i) := j$ si $j$ es la charla que termina más tarde antes de $s_i$, o $0$ si no hay tal charla. En la instancia: $b(1) = 0$, $b(2) = 0$, $b(3) = 1$, $b(4) = 0$, $b(5) = 3$, $b(6) = 3$.

![Subestructura óptima de las charlas](adjuntos/Subestructura%20%C3%B3ptima%20de%20las%20charlas.png)

> [!example]- Transcripción de la imagen
> Instancia con charlas $\{1, \dots, n\}$ ordenadas por $f_i$ y una solución óptima $\Omega$. Se considera la última charla, $n$, y hay dos opciones. Si $n \notin \Omega$, $\Omega$ es solución del **subproblema** con las charlas $\{1, \dots, n-1\}$. Si $n \in \Omega$, ninguna charla $r$ con $b(n) < r < n$ está en $\Omega$, y además $\Omega$ contiene una solución óptima al **subproblema** con charlas $\{1, \dots, b(n)\}$. "Para encontrar la solución a un problema, necesitamos las soluciones a problemas más pequeños".

![Pizarra - la charla n está o no está en la solución](adjuntos/Pizarra%20-%20la%20charla%20n%20est%C3%A1%20o%20no%20est%C3%A1%20en%20la%20soluci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Foto de pizarra: el problema $[1 \dots n]$ se divide en dos ramas. Si $n$ está, queda $[1 \dots b(n)]$, porque se tacha la zona entre $b(n)$ y $n$ que choca con la charla $n$. Si $n$ no está, queda $[1 \dots n-1]$.

![Recurrencia opt(j)](adjuntos/Recurrencia%20opt%28j%29.png)

> [!example]- Transcripción de la imagen
> Sea $\Omega_j$ la solución al problema con charlas $\{1, \dots, j\}$ y $opt(j)$ su ganancia total; el objetivo es $\Omega_n$ con valor $opt(n)$. Para cada $1 \le j \le n$: si $j \in \Omega_j$, $opt(j) = v_j + opt(b(j))$; si $j \notin \Omega_j$, $opt(j) = opt(j - 1)$. Para decidir se comparan ambas: $opt(j) = \max\{v_j + opt(b(j)),\ opt(j-1)\}$ (★).

$$opt(j) = \max\{\,v_j + opt(b(j)),\ opt(j-1)\,\}, \qquad opt(0) = 0$$

Plantear esta **ecuación de recurrencia** es el corazón de la PD: decidir si el último elemento está o no, y expresar cada caso con subproblemas más chicos.

## Preguntas de repaso

> [!question]- ¿Qué diferencia la programación dinámica de dividir para conquistar?
> En dividir para conquistar los subproblemas son disjuntos, así que no hay nada que recordar. En PD los subproblemas se solapan, y guardar sus soluciones evita recalcularlas.

> [!question]- ¿Por qué el criterio "la que termina primero" deja de ser óptimo con ganancias?
> Porque maximiza la cantidad de charlas, no la ganancia. Una sola charla larga y muy valiosa puede valer más que varias cortas que se le superponen.

> [!question]- ¿Qué significa $b(j)$ y por qué aparece en la recurrencia?
> Es la última charla que termina antes de que empiece $j$. Si $j$ se incluye, todas las charlas entre $b(j)$ y $j$ chocan con ella, así que el resto de la solución es un óptimo de $\{1, \dots, b(j)\}$.

> [!question]- ¿Qué es la subestructura óptima?
> La propiedad de que la solución óptima de un problema contiene soluciones óptimas de sus subproblemas. Es lo que permite escribir la recurrencia.
