---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/apuntes]
prerrequisitos: ["[[Proceso de desarrollo de software]]", "[[Modelo en cascada]]"]
---
# Procesos iterativos

En un proceso iterativo el software se desarrolla en **ciclos repetidos (iteraciones)** y cada ciclo refina el producto según el feedback del usuario, hasta acercarse gradualmente al objetivo.

## Características
- Con cada **entrega**, esperamos el **feedback del usuario** para decidir los siguientes pasos a seguir.
- Aproximación **gradual** al objetivo.
- **Desarrollo modificable**.

![Procesos iterativos - analogía de la Mona Lisa](adjuntos/Procesos%20iterativos%20-%20analogía%20de%20la%20Mona%20Lisa.png)

> [!note]- Qué muestra la imagen
> La persona tiene una idea vaga ("woman in pastoral setting"). Primero hace un boceto completo (1), luego lo colorea a grandes rasgos (2) y finalmente lo refina hasta la obra terminada (3). En **cada iteración está el cuadro completo**, cada vez con más detalle.

## Modelos iterativos que vimos
1. [[Modelo en espiral]]
2. [[Modelo de prototipos]]
3. [[Proceso unificado (RUP)]]

> [!tip] Complemento (libro del curso, cap. 2.3, y slides "Procesos de Desarrollo de Software")
> - Las actividades avanzan como una **secuencia de iteraciones** que se acercan gradualmente al objetivo.
> - **Ojo:** una iteración **no siempre** genera código nuevo ni un incremento visible y útil. Puede ser, por ejemplo, una iteración de análisis de riesgo o de prototipo. Esa es la diferencia con los [[Procesos iterativos e incrementales]], donde cada iteración sí entrega valor usable.
> - **Orígenes:** las ideas iterativas vienen de mucho antes que el software. Las slides citan a Larman y Basili (2003, *"Iterative and Incremental Development: A Brief History"*), que relacionan estos procesos con el ciclo **Plan–Do–Study–Act** (Shewhart, años 1930; Deming, años 1940).
>
> ![Slide - enfoque iterativo](adjuntos/Slide%20-%20enfoque%20iterativo.png)
> *Analogía de las slides: se rellena la zanja con un bloque aproximado y se va tallando en cada iteración hasta que calza.*

> [!tip] Complemento — iterativo vs. incremental
> | | Iterativo | [[Procesos incrementales\|Incremental]] |
> |---|---|---|
> | Qué cambia en cada ciclo | Se **mejora** lo que ya existe | Se **agrega** una pieza nueva |
> | Producto en cada ciclo | Completo pero tosco | Parcial pero terminado |
> | Analogía | Boceto → color → detalle | Pintar el cuadro por partes |

## Preguntas de repaso

1. ¿Qué caracteriza a un proceso iterativo?
> [!question]- Respuesta
> El desarrollo avanza en ciclos. Después de cada entrega se usa el feedback del usuario para decidir los siguientes pasos y así se llega gradualmente al objetivo, con un desarrollo modificable.

2. ¿Qué tres modelos iterativos vimos en el curso?
> [!question]- Respuesta
> El modelo en espiral, el modelo de prototipos y el Proceso Unificado (RUP).

3. ¿Cuál es la diferencia entre un proceso iterativo y uno iterativo incremental? (pregunta de las slides)
> [!question]- Respuesta
> En el iterativo, cada ciclo refina el producto pero no necesariamente entrega funcionalidad nueva usable. En el iterativo incremental, cada ciclo además agrega funcionalidades nuevas listas para usar y mejora las existentes.

4. En la analogía de la Mona Lisa, ¿cómo se ve el proceso iterativo?
> [!question]- Respuesta
> Se pinta el cuadro completo desde el principio (boceto) y en cada iteración se refina: color y luego detalle.
