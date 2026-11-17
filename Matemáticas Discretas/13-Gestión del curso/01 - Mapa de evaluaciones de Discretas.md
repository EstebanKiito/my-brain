---
ramo: "Matemáticas Discretas"
tema: "Gestión del curso"
tags:
  - discretas/gestion
  - origen/complemento
prerrequisitos: []
---

# Mapa de evaluaciones de Discretas

El curso IIC1253 recorre los fundamentos discretos de la computación: inducción, lógica, conjuntos, relaciones, funciones, algoritmos, grafos y teoría de números. Esta nota dice qué se evalúa, cómo se calcula la nota y en qué orden aparecen los temas en las pruebas, para saber qué estudiar para cada una.

## Por qué "matemáticas discretas"

Las matemáticas continuas (cálculo, ecuaciones diferenciales) trabajan con conjuntos como $\mathbb{R}$; las discretas estudian objetos que se pueden representar en un computador: conjuntos finitos o infinitos enumerables ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}$) y estructuras construidas con ellos. El ejemplo motivador es el de los puentes de Königsberg: ¿existe un recorrido que cruce cada puente exactamente una vez? Probar todos los caminos es inviable (con 420 puentes hay más caminos que átomos en el universo), pero el teorema de Euler responde mirando solo los grados de los nodos: debe haber a lo más dos con grado impar. Esa diferencia entre buscar a ciegas y razonar con una propiedad es el tema del curso.

## Formato de evaluación

| Evaluación | Contenido | Detalle |
|---|---|---|
| Tareas | 6 durante el semestre, escritas en LaTeX | Se descarta la peor nota; una prórroga de 4 días por semestre (cupón) |
| Interrogación 1 | Inducción y lógica (proposicional y de primer orden) | A mediados de septiembre |
| Interrogación 2 | Conjuntos, relaciones, funciones y cardinalidad | A inicios de noviembre |
| Examen | Todo el curso, con más peso en la segunda mitad (funciones, grafos, teoría de números) | A comienzos de diciembre |

En semestres anteriores hubo una tercera interrogación (algoritmos, complejidad y teoría de números) y controles; el reparto por semestre cambia, pero el orden de los temas se mantiene.

## Cálculo de la nota

Sea $\mathrm{AVG}_n$ el promedio de las $n$ notas más altas de una lista.

- Tareas: $PT = \mathrm{AVG}_5(T_1, \dots, T_6)$.
- Interrogaciones y examen: $PE = \mathrm{AVG}_3(I_1, I_2, E, E)$, de modo que el examen cuenta doble y reemplaza a la peor nota.
- Nota final: $NF = 0{,}3\,PT + 0{,}7\,PE$.

> [!tip] Condiciones de aprobación
> Se aprueba si $PT \ge 2{,}95$, $PE \ge 3{,}95$ y $NF \ge 3{,}95$. Si no, la nota final es $\min\{NF, 3{,}9\}$.

> [!warning] Reemplazo de una interrogación
> Faltar a una sola interrogación no requiere justificación: su nota se reemplaza por la del examen. En cambio, faltar al examen exige justificativo oficial y se rinde al inicio del semestre siguiente.

## Qué entra en cada prueba

| Tema | Interrogación 1 | Interrogación 2 | Interrogación 3 (si hay) | Examen |
|---|---|---|---|---|
| Inducción | ✓ | | ✓ | ✓ |
| Lógica proposicional | ✓ | | | ✓ |
| Lógica de primer orden y demostraciones | ✓ | | | ✓ |
| Conjuntos | ✓ (a veces) | ✓ | | ✓ |
| Relaciones, equivalencia y órdenes | | ✓ | | ✓ |
| Funciones y cardinalidad | | ✓ | ✓ | ✓ |
| Algoritmos y complejidad | | | ✓ | ✓ |
| Grafos y árboles | | | | ✓ |
| Teoría de números | | | ✓ | ✓ |

En el banco de preguntas históricas, la I1 reparte sus preguntas entre lógica proposicional (la más frecuente), lógica de primer orden e inducción; la I2 se concentra en relaciones, órdenes, funciones y cardinalidad; y el examen toma al menos una pregunta de casi todos los temas.

## Preguntas de repaso

> [!question]- ¿Qué pasa con la nota si el examen es mucho mejor que las interrogaciones?
> El examen cuenta dos veces en $PE = \mathrm{AVG}_3(I_1, I_2, E, E)$: en la práctica entra dos veces y desplaza a la peor nota entre $I_1$, $I_2$ y $E$ repetido.

> [!question]- ¿Por qué se descarta la peor nota de las tareas?
> Para que un mal resultado aislado no pese demasiado: $PT$ promedia las 5 mejores de 6.

> [!question]- ¿Qué enseña el ejemplo de los puentes de Königsberg sobre el curso?
> Que muchos problemas computacionales tienen una solución exponencial ingenua y otra eficiente basada en una propiedad estructural (aquí, los grados de los nodos).
