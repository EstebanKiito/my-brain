---
ramo: "Programación Avanzada"
tema: "Gestión del curso"
tags:
  - ramo/gestion
  - origen/complemento
prerrequisitos: []
---

# Programa del curso metodología y reglas de evaluación

El curso **Programación Avanzada (IIC2233)** de la Pontificia Universidad Católica de Chile profundiza en la creación de software modular, robusto y concurrente en Python. A diferencia de un curso introductorio centrado únicamente en la sintaxis, Avanzada enseña a diseñar sistemas a gran escala articulando arquitectura orientada a objetos, interfaces gráficas, comunicación en red y paralelismo.

## Metodología: Clase Invertida (Flipped Classroom)

El ramo opera bajo la metodología de **aula invertida** (*Flipped Classroom*), promoviendo el aprendizaje activo mediante el principio de "aprender haciendo":

1. **Estudio autónomo previo:** los contenidos teóricos y prácticos se publican en paquetes (*batches*) de notebooks interactivos en GitHub para ser revisados por el estudiante antes de la sesión presencial.
2. **Cátedras interactivas:** el horario de clase no se destina a dictar diapositivas, sino a resolver dudas conceptuales, analizar código y desarrollar **Actividades** evaluadas o **Experiencias** prácticas en conjunto con el equipo docente.
3. **Tareas de integración:** proyectos individuales de desarrollo a gran escala donde se aplican simultáneamente todos los contenidos del período.

## Componentes de evaluación y cálculo de notas

La calificación del curso pondera el trabajo continuo a lo largo del semestre a través de tres instrumentos:

### 1. Actividades prácticas ($AC$)
Se realizan 6 actividades breves de programación durante las cátedras (evaluadas de 0 a 4 puntos con baterías de pruebas automáticas):

$$AC = \frac{\sum_{i=1}^{6} A_i}{24} \cdot 6 + 1$$

### 2. Tareas de programación ($T$)
Se desarrollan 3 tareas individuales de software de complejidad progresiva:
- **T1 (10% de $T$):** algoritmos, estructuras de datos y POO (10 días hábiles).
- **T2 (60% de $T$):** interfaces gráficas con PyQt y threading; cuenta con entrega de avance obligatorio (18 días hábiles).
- **T3 (30% de $T$):** networking, serialización y sockets cliente-servidor (10 días hábiles).

$$T = \frac{1 \cdot T_1 + 6 \cdot T_2 + 3 \cdot T_3}{10}$$

### 3. Evaluaciones escritas ($EE$)
Dos pruebas individuales desarrolladas con lápiz y papel para validar fundamentos conceptuales y detección de errores de código:

$$EE = \frac{\text{Midterm} + \text{Examen}}{2}$$

### Nota de Cátedra ($NC$) y Requisitos de Aprobación

$$NC = 0.10 \cdot AC + 0.60 \cdot T + 0.30 \cdot EE$$

Para aprobar el curso es **estrictamente obligatorio** obtener calificación igual o superior a $3.95$ en cada una de las áreas críticas:

$$NF = \begin{cases} \min(NC, 7.0) & \text{si } T \ge 3.95 \land EE \ge 3.95 \land NC \ge 3.95 \\ \min(NC, 3.9) & \text{en cualquier otro caso (reprobado)} \end{cases}$$

## Política de atrasos y cupones de gracia

Las tareas poseen una ventana de entrega diferida con penalización sobre la nota máxima:

- **Hasta 24 horas de atraso:** nota máxima $6.0$.
- **Entre 24 y 48 horas de atraso:** nota máxima $4.0$.
- **Más de 48 horas:** la entrega no se acepta (calificación $1.0$).

Cada estudiante dispone de **2 cupones** en el semestre: cada cupón anula la penalización de un día de atraso (permitiendo optar a nota $7.0$ con 1 día de atraso, o nota $6.0$ con 2 días de atraso). Los cupones no extienden el plazo fatal de 48 horas.

> [!warning] La regla del reprobado independiente
> Aunque obtengas nota $7.0$ en todas las tareas, si tu promedio de evaluaciones escritas ($EE$) es inferior a $3.95$, la nota final del curso quedará congelada en $3.9$ de forma automática.

> [!tip] Décima de bonificación por ECA
> Completar 10 o más Encuestas de Carga Académica (ECA) durante el semestre bonifica con $+0.1$ décima directa a la Nota Final ($NF$) si cumples con todos los requisitos de aprobación.

## Preguntas de repaso

> [!question]- ¿Por qué la Tarea 2 posee una ponderación tan alta (60%) dentro del promedio de tareas?
> Porque es el proyecto integrador de mayor envergadura del curso, donde se diseña e implementa una aplicación completa combinando POO, interfaz gráfica con PyQt y concurrencia con hilos.

> [!question]- ¿Qué ocurre si un estudiante obtiene promedio de tareas $6.5$ y promedio de actividades $6.0$, pero obtiene $3.8$ en el promedio de evaluaciones escritas ($EE$)?
> Reprueba el curso con nota final máxima de $3.9$, ya que no cumplió con el requisito de aprobación independiente de $EE \ge 3.95$.

> [!question]- ¿Cómo opera el uso de los cupones de atraso en la entrega de tareas?
> Cada cupón anula un escalón de penalización por atraso (elimina 1 día de castigo), pero no posterga el límite máximo fatal de 48 horas tras el cual no se aceptan entregas.

> [!question]- ¿Cuál es el rol de las cátedras bajo la metodología de aula invertida (*flipped classroom*)?
> Resolver dudas puntuales y realizar actividades prácticas aplicadas, dado que los conceptos teóricos son estudiados previamente por el alumno en los notebooks de GitHub.
