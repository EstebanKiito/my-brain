---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - preemptive
  - batch
  - metricas
prerrequisitos:
  - "[[01 - Niveles de planificación y ciclo de ráfagas CPU-IO]]"
---

# Clasificación de planificadores y métricas de rendimiento

Los algoritmos de planificación de CPU se clasifican según **cómo interactúan con los procesos en ejecución** (grado de expropiación) y **cuál es el objetivo del entorno operativo** (lotes, interacción humana o restricciones temporales estrictas).

---

## EXISTEN MUCHOS SCHEDULLERS (mis apuntes)

> ![Clasificación de planificadores expropiativos y colaborativos](adjuntos/Clasificaci%C3%B3n%20de%20planificadores%20expropiativos%20y%20colaborativos.png)
> 
> Pregunta tipica: los mas usados som los expropiativos (Preemptive)
> → Dado que los colaborativos son casi inutiles, mejor expropiar que esperar a que un proceso termine por si solo
> 
> Otros
> 
> ![Objetivos de planificación batch interactiva y tiempo real](adjuntos/Objetivos%20de%20planificaci%C3%B3n%20batch%20interactiva%20y%20tiempo%20real.png)
> 
> Ej: Apenas pase una llamda, quiero transcribirla ahora
> Toma el que va llegando
> Usualmente se usa para cosas de urgencias → Como hospitales
> O Compras → Eligo el celular → nos llevan a webpay → esa solicitud tiene que ser en el momento
> Real tiem: en tiempo real se va produciendo
> 
> Ej: Esperar a la noche en cierto horario → Eligo el momento (no en tiempo real)
> Toma por ejemplo, un lote de 40 y transcribo
> Ej: Compro un celular → Se procesa mas tarde, y te lo envian a los dias
> Batch: En un momento mas tardio
> 
> Es una mezcla de ambos
> Se trata de interacutar con el usuario
> Interactivo: Minimizar el tiempo de respuesta
> 
> CONCEPTOS IMPORTANTEs
> 
> ![Conceptos y métricas clave de planificación](adjuntos/Conceptos%20y%20m%C3%A9tricas%20clave%20de%20planificaci%C3%B3n.png)
> 
> Throughput es importante → Es la : Cantidad de procesos / Tiempo (seg generalmente)

> [!warning] Posible error en apuntes
> * *"som"*: errata por "son".
> * *"Real tiem"*: errata por *Real Time* (tiempo real).
> * *"interacutar"*: errata por "interactuar".
> * *"Eligo"*: errata por "Elijo".
> * *"los colaborativos son casi inutiles"*: en sistemas modernos multiusuario e interactivos la falta de expropiación es inviable porque un proceso en bucle infinito colgaría el sistema; sin embargo, en sistemas embebidos simples sin temporizador de hardware o en corrutinas a nivel de aplicación (*cooperative multitasking*), los modelos colaborativos aún tienen vigencia.

---

> [!example]- Transcripción de la imagen: Clasificación de planificadores expropiativos y colaborativos.png
> **Por tipo de interrupción:**
> * **Preemptive (expropiativo):** Utiliza interrupciones de hardware (ej: interrupción de reloj o *timer*) para desalojar a un proceso de la CPU y devolverlo a la cola *Ready*, garantizando equidad.
> * **Non-Preemptive (colaborativo o no-expropiativo):** Permite que un proceso conserve la CPU hasta que:
>   1. El proceso cede voluntariamente la CPU (ej: mediante `yield`).
>   2. El proceso se bloquea esperando una operación de I/O.
>   3. El proceso finaliza su ejecución (*exit*).

> [!example]- Transcripción de la imagen: Objetivos de planificación batch interactiva y tiempo real.png
> **Por objetivo del sistema:**
> * **Batch (trabajo por lotes):** Sin interacción con el usuario. Objetivos: mantener la CPU lo más ocupada posible (alta utilización), minimizar el tiempo de retorno (*turnaround time*) y maximizar el rendimiento (*throughput*).
> * **Interactive (sistemas interactivos de escritorio/servidor):** Alta presencia de usuarios. Objetivos: minimizar el tiempo de respuesta (*response time*) y evitar retrasos perceptibles.
> * **Real Time (sistemas de tiempo real):** Entornos de control y misión crítica. Objetivos: tiempo de respuesta predecible y cumplimiento estricto de plazos (*deadlines*).

> [!example]- Transcripción de la imagen: Conceptos y métricas clave de planificación.png
> **Métricas fundamentales:**
> * **BATCH:** Proceso por lotes que se ejecuta en segundo plano sin intervención del usuario.
> * **Turnaround ($T_{\text{retorno}}$):** Tiempo total que un proceso permanece en el sistema (desde que llega hasta que finaliza: $T_{\text{término}} - T_{\text{llegada}}$).
> * **Throughput:** Cantidad de procesos completados por unidad de tiempo ($\text{procesos}/\text{segundo}$ o trabajos por hora).

---

> [!tip] Complemento: Las métricas formales de planificación
> Para comparar algoritmos de planificación se analizan formalmente las siguientes variables para un proceso $i$:
> 
> | Métrica | Definición | Fórmula | Objetivo típico |
> | :--- | :--- | :--- | :--- |
> | **Turnaround time** | Tiempo total en el sistema | $T_{\text{turnaround}} = T_{\text{término}} - T_{\text{llegada}}$ | Minimizar (Batch) |
> | **Response time** | Tiempo hasta recibir la primera atención de CPU | $T_{\text{response}} = T_{\text{primera\_ejecución}} - T_{\text{llegada}}$ | Minimizar (Interactivo) |
> | **Waiting time** | Tiempo total esperando en la cola *Ready* | $T_{\text{waiting}} = T_{\text{turnaround}} - T_{\text{burst}}$ | Minimizar |
> | **Throughput** | Tasa de finalización de procesos | $\text{Throughput} = \frac{N}{\Delta t}$ | Maximizar |
> | **CPU Utilization** | Porcentaje de tiempo que la CPU ejecuta trabajo útil | $\% \text{ Utilización} \in [0, 100\%]$ | Maximizar |

---

## Preguntas de repaso

> [!question]- ¿Por qué los sistemas operativos modernos utilizan planificación preemptive en lugar de cooperativa?
> Porque en un entorno colaborativo (*non-preemptive*), un programa malicioso o un error con un bucle infinito `while(1);` acapararía la CPU indefinidamente, congelando todo el sistema operativo. La expropiación basada en temporizadores de hardware (*timer interrupts*) asegura que ningún proceso monopolice el procesador.

> [!question]- ¿Cuál es la diferencia entre el Turnaround time y el Response time?
> El **Turnaround time** mide el tiempo total desde que el proceso ingresa a la cola hasta que termina completamente su ejecución. El **Response time** mide únicamente el tiempo desde que ingresa a la cola hasta que obtiene por primera vez el control de la CPU para responder al usuario.

> [!question]- ¿Cómo se relacionan los objetivos de un sistema Batch y uno Interactivo?
> En sistemas **Batch** no importa cuánto tarde un proceso en responder inicialmente siempre que el conjunto termine rápido y la CPU no esté ociosa (se prioriza *Turnaround* y *Throughput*). En sistemas **Interactivos** se prioriza la sensación de inmediatez para el usuario, sacrificando si es necesario el tiempo total de finalización a cambio de un bajísimo *Response time*.
