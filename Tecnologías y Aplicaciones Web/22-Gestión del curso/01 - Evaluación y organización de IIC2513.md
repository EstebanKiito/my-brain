---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Gestión del curso"
tags:
  - web
  - gestion-del-curso
  - evaluaciones
  - origen/complemento
prerrequisitos: []
---

# Evaluación y organización de IIC2513

**Tecnologías y Aplicaciones Web** busca que sus estudiantes conozcan la infraestructura tecnológica sobre la que se construye y opera la World Wide Web, y que sean capaces de construir sitios y desarrollar aplicaciones web con tecnologías actuales. La web es transversal a todas las áreas y personas, y hacerla funcionar requiere protocolos, estándares, diseño y conversación entre mucha gente. Por eso el curso mira las aplicaciones más allá del código: impactan a personas, abren oportunidades y son parte del mundo real.

## Competencias

1. Entender cómo interactúan las partes de la infraestructura de la web.
2. Discutir los estándares que hacen posible el funcionamiento de la WWW.
3. Inferir la arquitectura tecnológica de sitios y aplicaciones web.
4. Construir sitios con contenido dinámico.
5. Construir aplicaciones con las tecnologías y herramientas disponibles.
6. Integrar técnicas de desarrollo de software para construir aplicaciones web de alta calidad.
7. Encontrar posibles vulnerabilidades en aplicaciones web.
8. Evaluar los méritos de las nuevas tecnologías para el desarrollo web y de las que dan soporte a la WWW.

A grandes rasgos: entender cómo funciona la web, construir una aplicación web completa, evaluar tecnologías nuevas, conocer lo necesario para hacer aplicaciones de alta calidad y acercarse al mundo real (ciberseguridad, vida laboral, ética).

## Contenidos

| Bloque | Temas del vault |
|---|---|
| Fundamentos de la web | Fundamentos de la web, HTML y CSS, JavaScript, asincronía, DOM y eventos |
| Desarrollo de una aplicación web | React, APIs y REST, Node.js, servidores, API con Express, diseño web y CSS moderno |
| Gestión de datos | Cookies y sesiones, almacenamiento en el cliente |
| Software + web | Calidad, CI y CD; testing; tecnologías adicionales |
| Seguridad web | Autenticación y autorización; ingeniería inversa |
| El mundo real | Escala, IA para desarrolladores, privacidad y ética |

## Cómo se evalúa (versión 2025-2)

El curso combina entender los conceptos con ponerlos en práctica, mediante cuatro tipos de evaluaciones:

| Evaluación | Objetivo | Cantidad |
|---|---|---|
| **Actividades** | Incentivar la práctica de una técnica o elemento visto en clase; ejercicios cortos de código y pensamiento crítico | 6, con puntaje entre 0 y 1 |
| **Tareas** | Evaluar de forma individual la aplicación de contenidos específicos, como un laboratorio aislado | 2 (T1 y T2) |
| **Controles** | Evaluar de forma individual y teórica un conjunto de contenidos | 5 (C1 a C5) |
| **Proyecto** | Aplicar los contenidos en equipos de 3 personas, en una experiencia cercana al desarrollo real | 4 entregas: preliminar (E0) y tres de desarrollo |

$$A = 1 + A_1 + A_2 + \dots + A_6 \qquad T = \frac{T_1 + T_2 + A}{3} \qquad C = \frac{\sum_{i=1}^{5} C_i - \min_i C_i}{4}$$

$$P = 0{,}1\,E_0 + 0{,}25\,E_1 + 0{,}25\,E_2 + 0{,}4\,E_3 \qquad NC = 0{,}4\,T + 0{,}4\,P + 0{,}2\,C$$

$$NF = \begin{cases} NC & \text{si } T \ge 3{,}95 \text{ y } P \ge 3{,}95 \\ \min(NC;\ 3{,}9) & \text{en otro caso} \end{cases}$$

Las actividades suman a la nota de tareas como si fueran una tercera tarea, y el peor control se descarta. Todas las notas se calculan con dos decimales, salvo la final, que se reporta con uno.

El semestre tiene dos partes: primero las tareas individuales, para formar las habilidades, y después el proyecto grupal, cuando ya se sabe desarrollar cada parte. Los controles y las actividades se reparten a lo largo del semestre.

> [!tip] Evaluación de última instancia
> Si $NC > 3{,}95$ pero **una sola** de las condiciones de aprobación queda entre 3,80 y 3,94, se puede apelar a una evaluación oral en los últimos días del semestre sobre varios contenidos del curso. Si se aprueba, la nota final es 4,0.

## Integridad académica

> [!warning] Reglas que conviene tener presentes
> - Cualquier copia se sanciona con **1,1 final**, sin perjuicio de otras sanciones según la política de la Escuela, la Universidad y el DCC.
> - Se puede usar código encontrado en internet **indicando la fuente**. Si es material del curso, solo se permite el del equipo docente (clases y ayudantías), citado.
> - Todas las evaluaciones son individuales salvo que se indique lo contrario: compartir código es copia.
> - Las IAs (ChatGPT, Copilot, Gemini u otras) se pueden usar **solo si se entiende completamente el código**, porque se asume que se domina todo lo que hace, y **declarando su uso en el README**.

## Preguntas de repaso

> [!question]- ¿Qué condiciones hay que cumplir para que la nota final sea la nota del curso?
> Tener promedio de tareas $T \ge 3{,}95$ y promedio de proyecto $P \ge 3{,}95$. Si falla alguna, la nota final queda limitada a 3,9.

> [!question]- ¿Cómo influyen las actividades en la nota?
> Se suman en la nota $A$ (de 1 a 7), que entra en el promedio de tareas como si fuera una tercera tarea.

> [!question]- ¿Bajo qué condiciones se puede usar una IA en las evaluaciones?
> Solo si se entiende por completo el código que genera (se asume que se domina) y si se declara explícitamente su uso en el README.
