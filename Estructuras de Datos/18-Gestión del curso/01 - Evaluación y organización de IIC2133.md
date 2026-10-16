---
ramo: "Estructuras de Datos"
tema: "Gestión del curso"
tags:
  - edd
  - gestion-del-curso
  - evaluaciones
  - origen/complemento
prerrequisitos: []
---
ss
# Evaluación y organización de IIC2133

**Estructuras de Datos y Algoritmos** estudia algoritmos y su implementación eficiente mediante estructuras de datos. Sus objetivos son tres: desarrollar el **pensamiento algorítmico**, estudiar y aplicar distintos tipos de **estructuras de datos** y estudiar y aplicar distintas **técnicas algorítmicas**.

## Contenidos

| Bloque | Temas |
|---|---|
| Estructuras fundamentales | Arreglos, listas ligadas, stacks, colas, tablas de hash |
| Árboles de búsqueda | Árboles binarios y balanceados, árboles 2-3 (y rojo-negro, B+) |
| Algoritmos de ordenación | Insertion sort, heapsort, quicksort, mergesort, counting sort (y radix) |
| Técnicas algorítmicas | Dividir para conquistar, backtracking, programación dinámica, algoritmos codiciosos |
| Algoritmos en grafos | Representación, exploración, orden topológico, componentes fuertemente conectadas, árboles de cobertura, rutas más cortas |

El curso usa **pseudocódigo** para describir algoritmos y supone como herramientas previas exponentes, logaritmos, series, aritmética modular, inducción, contradicción, contraejemplos y recursión.

## Evaluación (versión 2024)

- **Tareas:** cuatro tareas de programación **en C**, de unas 2 semanas cada una y con corrección automatizada. La T0 sirve de introducción al lenguaje (ver [[Programación en C/_Índice|Programación en C]]).
- **Interrogaciones:** tres pruebas escritas presenciales (I1, I2, I3).

$$NT = 0{,}2\,T0 + 0{,}3\,T1 + 0{,}25\,T2 + 0{,}25\,T3 \qquad NI = 0{,}35\,I1 + 0{,}35\,I2 + 0{,}3\,I3$$

$$NF = \begin{cases} \dfrac{NI + NT}{2} & \text{si } NI \ge 3{,}7 \text{ y } NT \ge 3{,}7 \\[4pt] \min(NF,\ 3{,}9) & \text{en otro caso} \end{cases}$$

> [!warning] Reglas que conviene tener presentes
> - **Atrasos en tareas:** hay 2 cupones en el semestre (cada uno posterga 1 día la entrega de T1, T2 o T3, no la T0). Sin cupón, se descuentan 5 décimas por hasta 3 horas de atraso y 2 puntos por hasta 24 horas. Con más de 1 día de atraso, la nota es 1,0.
> - **Inasistencia a la I1 o la I2:** se justifica ante la DIPRE para optar a preguntas adicionales en la I3 que reemplazan la nota faltante. Sin justificación no hay recuperativas.
> - **Código de honor:** la copia se sanciona con nota final 1,1.

## Comunicación y bibliografía

Los anuncios llegan por Canvas. Las clases, la guía de instalación de C, los enunciados y los repositorios de entrega están en el GitHub del curso, y las preguntas se hacen como *issues* de GitHub. La bibliografía principal es:

- T. Cormen, C. Leiserson, R. Rivest y C. Stein, *Introduction to Algorithms* (MIT Press, 3.ª ed., 2009).
- R. Sedgewick y K. Wayne, *Algorithms* (Addison-Wesley, 4.ª ed., 2011).
- M. Weiss, *Data Structures and Algorithm Analysis in C++* (Pearson, 4.ª ed., 2014).

> [!tip] Consejo del curso
> El curso mezcla teoría y práctica: no basta con revisar las slides ni con leer el enunciado de la tarea el día antes. Después de estudiar un concepto, conviene inventar un ejemplo propio para explicarlo y resolver problemas de la bibliografía, primero mirando soluciones y después sin ellas.

## Preguntas de repaso

> [!question]- ¿Qué condición hay que cumplir para que la nota final sea el promedio de tareas e interrogaciones?
> Tener promedio de interrogaciones $NI \ge 3{,}7$ y promedio de tareas $NT \ge 3{,}7$. Si no, la nota final queda limitada a un máximo de 3,9.

> [!question]- ¿Cómo se ponderan las tareas en la nota de tareas?
> $NT = 0{,}2\,T0 + 0{,}3\,T1 + 0{,}25\,T2 + 0{,}25\,T3$: la T0, introductoria, pesa menos y la T1 es la de mayor peso.

> [!question]- ¿En qué lenguaje se hacen las tareas y por qué importa para el estudio?
> En C. Además de entender los algoritmos, hay que saber implementarlos con punteros, structs y memoria dinámica, y manejar bien los errores de memoria.
