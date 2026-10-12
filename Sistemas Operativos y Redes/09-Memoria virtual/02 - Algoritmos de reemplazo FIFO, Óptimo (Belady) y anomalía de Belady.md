---
ramo: "Sistemas Operativos y Redes"
tema: "Memoria virtual"
tags:
  - so/memoria
  - so/memoria-virtual
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de memoria virtual y espacio de intercambio (swap)]]"
  - "[[07 - Introducción al intercambio por demanda y ciclo de fallos de página]]"
---

# Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady

Cuando ocurre un fallo de página y todos los marcos físicos de la memoria RAM están ocupados, el sistema operativo debe seleccionar una página residente para desalojarla hacia el espacio swap. La política elegida determina la tasa de fallos de página del sistema.

## El algoritmo óptimo de Belady (OPT / MIN)

Propuesto formalmente por László Bélády en 1966, el algoritmo **Óptimo** (denominado **OPT** o **MIN**) establece la cota superior teórica de rendimiento para cualquier política de reemplazo:

> [!tip] Regla del algoritmo óptimo
> Desalojar aquella página cuya próxima referencia en el tiempo ocurrirá más lejos en el futuro (o que nunca volverá a ser referenciada).

![Algoritmo de reemplazo óptimo de Belady](adjuntos/Algoritmo%20de%20reemplazo%20%C3%B3ptimo%20de%20Belady.png)

> [!example]- Transcripción de la imagen
> Diapositiva oficial del curso (`Contenido_6_Memoria.pdf`, p. 55):
> - Planteado por Laszlo A. Belady, 1966.
> - Ejemplo con sistema de 3 frames físicos para un proceso.
> - Secuencia de referencias: `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1`.
> - En cada fallo de página, se examinan las páginas residentes y se desaloja la que se usará más tarde en la traza futura.
> - Es el mejor algoritmo posible, pero imposible de implementar en un sistema operativo real porque requiere conocer el futuro de las instrucciones del programa. Se utiliza exclusivamente como patrón de referencia (*benchmark*).

## Algoritmo First-In, First-Out (FIFO)

La política **FIFO** asocia a cada página el instante en que fue cargada en memoria, organizando los marcos en una cola circular simple:

> [!tip] Regla de FIFO
> Desalojar la página más antigua que reside en memoria (la primera que entró).

![Algoritmo de reemplazo First In First Out FIFO](adjuntos/Algoritmo%20de%20reemplazo%20First%20In%20First%20Out%20FIFO.png)

> [!example]- Transcripción de la imagen
> Diapositiva oficial del curso (`Contenido_6_Memoria.pdf`, p. 56):
> - Algoritmo FIFO sobre la secuencia de referencias `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1` con 3 marcos.
> - Tasa de aciertos (*Hit Rate*) = 0.364 (significativamente inferior a MIN).
> - Desventaja fundamental: Una página cargada al inicio puede contener una variable global crítica o una biblioteca frecuentemente consultada; FIFO la expulsará reiteradamente solo por ser antigua.

## La anomalía de Bélády

Intuitivamente se esperaría que al otorgar más marcos físicos a un proceso, la cantidad de fallos de página siempre disminuya o se mantenga igual. Sin embargo, en algoritmos como FIFO ocurre la **Anomalía de Bélády**:

> [!warning] Anomalía de Bélády
> Fenómeno por el cual incrementar el número de marcos de memoria física asignados a un proceso provoca un **aumento** en la cantidad total de fallos de página para una traza de referencias determinada.
>
> Para la cadena de accesos `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`:
> - Con **3 marcos**, FIFO genera **9 fallos de página**.
> - Con **4 marcos**, FIFO genera **10 fallos de página**.

Este comportamiento anómalo se debe a que FIFO no cumple la *propiedad de inclusión de la pila* (*stack algorithm property*), según la cual el conjunto de páginas residentes en un sistema con $N$ marcos es siempre un subconjunto estricto del conjunto de páginas residentes en un sistema con $N+1$ marcos.

## Preguntas de repaso

> [!question]- ¿Por qué el algoritmo óptimo de Belady no puede implementarse en un sistema operativo de propósito general?
> Porque requiere conocer de antemano la secuencia completa de todas las futuras direcciones virtuales que el procesador referenciará, lo cual viola el principio de no determinismo y la dependencia de entradas de usuario de las aplicaciones reales.

> [!question]- ¿Por qué la política FIFO presenta un desempeño deficiente en cargas con datos compartidos o bibliotecas base?
> Porque FIFO evalúa exclusivamente el tiempo que la página lleva residente en RAM, ignorando si está siendo intensamente leída o escrita. Si una página muy activa fue cargada al arrancar el programa, FIFO la desalojará forzando un fallo de página inmediato.

> [!question]- ¿Qué propiedad matemática previene que un algoritmo de reemplazo sufra de la anomalía de Bélády?
> La condición de ser un **algoritmo de pila** (*stack algorithm*), donde el conjunto de páginas residentes con $m$ marcos está garantizado de estar contenido dentro del conjunto residente con $m+1$ marcos para cualquier instante temporal (propiedad que cumplen OPT y LRU, pero no FIFO).

