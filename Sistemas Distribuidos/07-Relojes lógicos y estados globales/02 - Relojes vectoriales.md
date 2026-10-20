---
ramo: "Sistemas Distribuidos"
tema: "Relojes lógicos y estados globales"
tags:
  - sd/relojes
  - origen/complemento
prerrequisitos:
  - "[[01 - Relojes lógicos de Lamport]]"
---

# Relojes vectoriales

El reloj de Lamport tiene un límite: un contador menor no prueba que un evento ocurrió antes. El **reloj vectorial** lo resuelve guardando, en vez de un solo número, **un contador por cada proceso**: lo que cada proceso sabe del avance de los demás. Con esa información sí se puede decidir si un evento causó a otro o si son **concurrentes**.

## La estructura

![Definición de reloj vectorial](adjuntos/Definici%C3%B3n%20de%20reloj%20vectorial.png)

> [!example]- Transcripción de la imagen
> Cada proceso $P_i$ tiene su propio vector $V_i$, en el que guarda tanto el estado de su reloj lógico como el de los demás procesos al momento de comunicarse. $V_i[i]$ es el estado del reloj lógico de $P_i$; $V_i[z]$ es la última actualización del reloj lógico de $P_z$ de la que tiene constancia $P_i$. $V_i = V_k$ si $V_i[x] = V_k[x]$ para $x = 1, \dots, N$; $V_i \le V_k$ si $V_i[x] \le V_k[x]$ para todo $x$; $V_i < V_k$ si $V_i \le V_k$ y $V_i \ne V_k$.

Un vector son muchos relojes lógicos juntos: cada proceso tiene su posición fija ($P_1$ es la primera componente, $P_2$ la segunda…). Las comparaciones son **componente a componente**:

- $[1,1,1] = [1,1,1]$.
- $[1,1,0] < [1,1,1]$: todas las componentes son menores o iguales y al menos una es menor.
- $[2,0,0]$ y $[0,0,1]$ **no son comparables**: ninguno es menor o igual que el otro.

## Reglas

![Reglas del reloj vectorial](adjuntos/Reglas%20del%20reloj%20vectorial.png)

> [!example]- Transcripción de la imagen
> Cuando pasa un evento en el proceso $P_i$, se aumenta en una unidad $V_i[i]$. Un evento es algo ocurrido únicamente en el proceso, el envío de un mensaje a otro proceso o la recepción de un mensaje. Cuando $P_i$ recibe un vector $V_z$, primero aumenta en una unidad $V_i[i]$ y luego actualiza $V_i[x] = \max(V_i[x], V_z[x])$ para $x = 1, \dots, N$.

- Cada evento (local, envío o recepción) suma 1 **solo a la componente propia**.
- Al recibir, se suma 1 a la propia y luego se toma el **máximo componente a componente** con el vector recibido. A las componentes ajenas **no** se les suma nada: solo se copian si son mayores.

## Comparar eventos

![Comparar eventos con relojes vectoriales](adjuntos/Comparar%20eventos%20con%20relojes%20vectoriales.png)

> [!example]- Transcripción de la imagen
> Con esto se pueden comparar dos eventos $a$ y $b$ según sus vectores: si $V^a_i < V^b_k$, el evento $b$ en $P_k$ ocurrió después que el evento $a$ en $P_i$. En otro caso, $a$ y $b$ son "concurrentes".

> [!tip] Regla de comparación
> $V(a) < V(b) \iff a \rightarrow b$. Si ni $V(a) < V(b)$ ni $V(b) < V(a)$, los eventos son **concurrentes**. A diferencia de Lamport, aquí la implicación vale en **ambas direcciones**.

## Ejemplo

Es el mismo escenario de tres procesos de [[01 - Relojes lógicos de Lamport|Lamport]], con vectores $[K, A, T]$.

![Primeros vectores del ejemplo](adjuntos/Primeros%20vectores%20del%20ejemplo.png)

> [!example]- Transcripción de la imagen
> Una línea verde marca el tiempo actual. Hasta ese punto: K tiene a = [1,0,0] y b = [2,0,0]; A tiene e = [0,1,0]; T tiene h = [0,0,1]. Los demás eventos aún no tienen vector.

![Vectores completos del ejemplo](adjuntos/Vectores%20completos%20del%20ejemplo.png)

> [!example]- Transcripción de la imagen
> K: a = [1,0,0], b = [2,0,0], c = [3,0,0], d = [4,0,1]. A: e = [0,1,0], f = [2,2,0], g = [2,3,0]. T: h = [0,0,1], i = [2,3,2], j = [2,3,3].

| Evento | Cálculo | Vector |
|---|---|---|
| $f$ (A recibe de $b$) | $[0,1,0] \to [0,2,0]$; máx con $[2,0,0]$ | $[2,2,0]$ |
| $d$ (K recibe de $h$) | $[3,0,0] \to [4,0,0]$; máx con $[0,0,1]$ | $[4,0,1]$ |
| $i$ (T recibe de $g$) | $[0,0,1] \to [0,0,2]$; máx con $[2,3,0]$ | $[2,3,2]$ |
| $j$ (T recibe de $a$) | $[2,3,2] \to [2,3,3]$; máx con $[1,0,0]$ | $[2,3,3]$ |

Si después de $j$ el proceso T tuviera un evento $k$ ($[2,3,4]$) que envía un mensaje a K, K pasaría de $[4,0,1]$ a $[5,0,1]$ y luego, con el máximo, a $[5,3,4]$.

![Concurrencia y causalidad con vectores](adjuntos/Concurrencia%20y%20causalidad%20con%20vectores.png)

> [!example]- Transcripción de la imagen
> "¿Qué podemos decir del evento h vs c? **Son concurrentes.** ¿Y del evento a vs i? **a ocurre antes que i.**"

- $h = [0,0,1]$ y $c = [3,0,0]$: ninguno es menor que el otro, así que son **concurrentes**. Con Lamport, $h$ (1) parecía anterior a $c$ (3).
- $a = [1,0,0] < i = [2,3,2]$: $a$ ocurre antes que $i$ (a través de $b \to f \to g \to i$).

Todos los vectores y comparaciones se verificaron con una simulación en Python. La ventaja del vector es que en cada evento se sabe **qué eventos de cada proceso vinieron antes**.

> [!warning] El costo
> Cada mensaje lleva un vector de $N$ enteros, y cada proceso guarda $N$ contadores. Con muchos procesos, el tamaño crece. Si dos eventos concurrentes necesitan un orden arbitrario, se desempata con el PID.

## Preguntas de repaso

> [!question]- ¿Qué información tiene un reloj vectorial que no tiene uno de Lamport?
> Cuánto sabe cada proceso del avance de cada uno de los demás. Con eso se distingue "ocurrió antes" de "concurrente", cosa imposible con un solo contador.

> [!question]- ¿Son comparables $[2,3,0]$ y $[4,0,1]$? ¿Qué significa?
> No: la primera componente de $[2,3,0]$ es menor, pero la segunda es mayor. Ninguno es menor o igual que el otro, así que los eventos ($g$ y $d$) son concurrentes.

> [!question]- Al recibir, ¿por qué no se suma 1 a las componentes de los otros procesos?
> Porque esas componentes registran eventos que ocurrieron en otros procesos; el receptor solo copia lo último que sabe de ellos. El único evento nuevo es la recepción, que ocurre en el propio proceso.
