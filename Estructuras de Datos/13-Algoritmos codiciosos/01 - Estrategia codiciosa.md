---
ramo: "Estructuras de Datos"
tema: "Algoritmos codiciosos"
tags:
  - edd
  - greedy
  - optimizacion
  - origen/complemento
prerrequisitos:
  - "[[04 - Podas, propagación y heurísticas]]"
---

# Estrategia codiciosa

Un **algoritmo codicioso** (*greedy*) está tan convencido de que su criterio es bueno que lo aplica **sin mirar atrás**: en cada paso toma la decisión que parece mejor y no la cambia nunca. En problemas de **optimización** suele ser mucho más rápido que backtracking, a veces lineal. El riesgo es que, si el criterio no es el adecuado, termina en un óptimo **local** y no en el **global**.

## Tipos de problemas

| Tipo | Pregunta | Ejemplo |
|---|---|---|
| Decisión | ¿Existe? Sí o no | ¿Tiene solución este sudoku? |
| Búsqueda | Encontrar una solución | Una ubicación válida de 8 reinas |
| Conteo | ¿Cuántas soluciones hay? | Backtracking cuenta las 92 de las 8 reinas |
| **Optimización** | La **mejor** solución | Llenar la mochila con la mayor ganancia |
| Función | Calcular un valor explícito | — |

Para optimizar, backtracking tendría que encontrar **todas** las soluciones y compararlas, lo que es carísimo. Y si las variables son **continuas** (por ejemplo, fracciones de un objeto), backtracking ni siquiera puede recorrer el dominio. Ahí entran los algoritmos codiciosos.

## El paradigma

![Paradigma de subconjuntos](adjuntos/Paradigma%20de%20subconjuntos.png)

> [!example]- Transcripción de la imagen
> Los **algoritmos codiciosos** plantean una estrategia basada en el paradigma de subconjuntos: 1. se tiene un conjunto $S = \{s_1, \dots, s_n\}$ con $n$ inputs; 2. se quiere un subconjunto $S' \subseteq S$ que satisfaga restricciones; 3. se quiere una solución factible que maximice o minimice una **función objetivo**. Un subconjunto que cumple las restricciones se llama **factible**, y uno que además optimiza se llama **óptimo**. "Esta es una concepción teórica. Veremos su aplicación a problemas concretos".

![Los algoritmos codiciosos trabajan en etapas](adjuntos/Los%20algoritmos%20codiciosos%20trabajan%20en%20etapas.png)

> [!example]- Transcripción de la imagen
> Los algoritmos codiciosos trabajan **en etapas**: consideran un input a la vez; una vez que se decide sobre un input, la decisión **es final**; ninguna decisión posterior cambia la actual. En el problema de la mochila, se trata de seleccionar un subconjunto de objetos y determinar la fracción $x_k$ de cada uno.

![Procedimiento de selección](adjuntos/Procedimiento%20de%20selecci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Para lograr el objetivo, los inputs se consideran en cierto orden, con un **procedimiento de selección**. Si incluir el próximo input en la solución parcial produce una solución infactible, no se considera; en otro caso, el input se agrega a la solución. "¿Qué diferencia hay con backtracking?".

La intuición es la del **método simplex** en optimización: desde la solución actual, avanzar siempre en la dirección en que la función objetivo crece más rápido. En la mochila, eso significa seguir al objeto que entrega más ganancia por unidad de peso.

## La plantilla

![Pseudocódigo de Greedy](adjuntos/Pseudoc%C3%B3digo%20de%20Greedy.png)

> [!example]- Transcripción de la imagen
> input: arreglo de inputs $A[0 \dots n-1]$, cantidad de inputs $n$. `Greedy(A, n)`: 1. `S ← ∅`; 2. `for i = 1...n:`; 3. `x ← Select(A)`; 4. `if Feasible(S, x):`; 5. `S ← Union(S, x)`; 6. `return S`.

- **`Select(A)`** no toma "el siguiente": toma el **mejor** input que queda, según el criterio codicioso. Es la heurística.
- **`Feasible(S, x)`** revisa si agregar $x$ mantiene la solución factible (las restricciones).
- El ciclo se ejecuta $n$ veces. Si `Select` es $O(1)$ (con los datos preordenados por el criterio), el algoritmo es $O(n)$, más el $O(n \log n)$ de ordenar. Si el criterio se mantiene en un [[01 - Colas de prioridad|heap]], cada selección cuesta $O(\log n)$.

> [!tip] Codicioso frente a backtracking
> 1. El algoritmo codicioso **toma decisiones y no se arrepiente**; backtracking puede deshacerlas y probar otras.
> 2. El algoritmo codicioso admite variables con **dominios continuos** (reales), y backtracking solo dominios discretos.
>
> Backtracking con una buena heurística y sin retroceder **es** un algoritmo codicioso.

## Preguntas de repaso

> [!question]- ¿Qué significa que en un algoritmo codicioso "la decisión es final"?
> Que una vez que se decide incluir (o no) un input, esa decisión no se revisa nunca más, aunque más adelante resulte inconveniente.

> [!question]- ¿Qué hace `Select` en la plantilla Greedy y por qué es lo más importante?
> Elige el mejor input disponible según el criterio codicioso. Todo el resultado depende de ese criterio: con uno bueno se llega al óptimo, y con uno malo, a un óptimo local.

> [!question]- ¿Por qué backtracking no sirve para la mochila con objetos fraccionables?
> Porque la fracción $x_k$ es un número real entre 0 y 1: el dominio es infinito y no se pueden enumerar sus valores.

> [!question]- ¿Cuál es la complejidad típica de un algoritmo codicioso?
> $O(n)$ iteraciones de la plantilla, más el costo de seleccionar: $O(n \log n)$ si se ordenan los inputs por el criterio al principio, o $O(\log n)$ por selección si se usa un heap.
