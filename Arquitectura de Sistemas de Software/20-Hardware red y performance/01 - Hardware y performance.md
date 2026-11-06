---
ramo: "Arquitectura de Sistemas de Software"
tema: "Hardware red y performance"
tags:
  - arquisis/performance
  - origen/complemento
prerrequisitos:
  - "[[03 - Tácticas de performance de Bass y Kazman]]"
---

# Hardware y performance

La táctica "incrementar recursos" solo sirve si se sabe **qué recurso** limita. Cada componente de hardware afecta un aspecto distinto: la CPU el cómputo, la RAM cuántos datos se procesan en memoria, el disco el I/O. Algunos componentes, como GPU, TPU o ASIC, solo valen la pena en contextos específicos. El impacto es a nivel de máquina, y su uso depende de la aplicación.

![Tabla de tipos de instancia m6i de AWS](adjuntos/Tipos%20de%20instancia%20m6i%20de%20AWS.png)

> [!example]- Transcripción de la imagen
> | Instancia | vCPU | Memoria (GiB) | Almacenamiento | Red (Gbps) | EBS (Gbps) |
> |---|---|---|---|---|---|
> | m6i.large | 2 | 8 | Solo EBS | Hasta 12,5 | Hasta 10 |
> | m6i.xlarge | 4 | 16 | Solo EBS | Hasta 12,5 | Hasta 10 |
> | m6i.2xlarge | 8 | 32 | Solo EBS | Hasta 12,5 | Hasta 10 |
> | m6i.4xlarge | 16 | 64 | Solo EBS | Hasta 12,5 | Hasta 10 |
> | m6i.8xlarge | 32 | 128 | Solo EBS | 12,5 | 10 |

En la nube, "escalar verticalmente" es literalmente subir de fila en esa tabla: pasar de `m6i.large` a `m6i.2xlarge` cuadruplica las vCPU y la memoria. La red y el ancho de banda de disco (EBS) no crecen en la misma proporción, así que no todo cuello de botella se resuelve con una instancia más grande.

## CPU

- **Arquitectura del núcleo:** predictor de saltos, conjunto de instrucciones y módulos específicos (por ejemplo, instrucciones de cifrado AES).
- **Núcleos e hilos:** algunas aplicaciones se benefician de tener más núcleos. Otras primero hay que paralelizarlas para que puedan usarlos.
- **Reloj:** la frecuencia está en proceso de *capping*, porque la relación térmica limita seguir subiéndola. Por eso la mejora viene de más núcleos y procesadores especializados.
- Los transistores siguen escalando (Intel proyecta un billón por paquete hacia 2030), los procesadores de propósito específico mejoran y hay cambios de arquitectura como AMD64 → ARM64.

## RAM

Determina cuántos datos se pueden mantener para procesar, hoy medidos en GB o TB. Importan la **generación**, la **cantidad**, la **latencia** y los **canales**. La demanda es fuerte por la IA y las GPU.

| Generación | Velocidad (MT/s) | Ancho de banda (GB/s) | Voltaje (V) | Prefetch (bits) | Año |
|---|---|---|---|---|---|
| DDR | 200-400 | 1,6-3,2 | 2,5 | 2 | 2000 |
| DDR2 | 400-1066 | 3,2-8,5 | 1,8 | 4 | 2003 |
| DDR3 | 800-2133 | 6,4-17,0 | 1,5 | 8 | 2007 |
| DDR4 | 1600-6400 | 12,8-51,2 | 1,2 | 8 | 2014 |
| DDR5 | 4800-8400+ | 38,4-67,2+ | 1,1 | 16 | 2020 |

## Almacenamiento masivo

Es de alta densidad y perdurable, pero **más lento que la RAM**: las aplicaciones que dependen de él son **I/O bound**. Puede beneficiarse de arquitecturas como RAID o Hadoop.

| Tipo | Capacidad | Velocidad | Costo | Uso típico |
|---|---|---|---|---|
| HDD | Hasta 20 TB | 50-150 MB/s | Bajo | Almacenamiento general, respaldos |
| SSD | Hasta 8 TB | 200-3.500 MB/s | Moderado | Sistema operativo, aplicaciones, bases de datos |
| SSD NVMe | Hasta 8 TB | 1.000-7.000 MB/s | Alto | Alto rendimiento, cargas intensivas en datos |
| USB / SD | Hasta 2 TB | 10-400 MB/s | Bajo-moderado | Portátil, cámaras |
| Óptico | Hasta 128 GB | 1,3-72 MB/s | Bajo | Distribución, archivo (solo acceso secuencial) |

## Procesadores especializados

- **GPU:** procesamiento **paralelo masivo** con shaders y pipelines. Hoy tiene módulos adicionales (tensor cores, ray tracing) y es la base de la IA.
- **TPU:** unidad de procesamiento de **tensores**, ideal para operaciones vectoriales de redes neuronales, tanto en entrenamiento como en inferencia. Es muy popular y muy cara.
- **ASIC** (*Application Specific Integrated Circuit*): un circuito diseñado para una sola tarea, como minar criptomonedas o cifrar con AES. Es el más rápido para esa tarea e inútil para otras.
- **FPGA** (*Field Programmable Gate Array*): lógica combinatoria reprogramable. Puede superar a una CPU en ciertas configuraciones, y se ha integrado junto a CPUs (Intel Skylake con FPGA).

![Rendimiento de una GPU frente a una CPU en inferencia y entrenamiento](adjuntos/Rendimiento%20de%20GPU%20frente%20a%20CPU%20en%20inferencia%20y%20entrenamiento.png)

> [!example]- Transcripción de la imagen
> - **Inference Performance**, una GPU NVIDIA Tesla T4 frente a un servidor con dos CPU Xeon Gold 6140: GNMT 36×, ResNet-50 27× y DeepSpeech2 21× más rápido que la CPU (que vale 1×).
> - **Training Performance**, dos GPU T4 frente al mismo servidor: ResNet-50 9,3× más rápido.

## Código, algoritmos y estructuras

El hardware no compensa un mal diseño. Hay que evitar las malas prácticas: mal uso de la orientación a objetos, código innecesario, falta de testing, un stack sobrepoblado y **abstracciones innecesarias**, siempre con ojo en la cohesión, la connascence y el acoplamiento. También hay que **escoger la estructura de datos correcta**: buscar en una lista es $O(n)$ y en un hash es $O(1)$, y esa diferencia no la arregla ninguna CPU.

> [!warning] Más hardware para un problema de I/O o de algoritmo
> Si una consulta hace un recorrido completo de una tabla de 10 millones de filas, duplicar las vCPU casi no ayuda: el problema es el I/O y la falta de un índice. Antes de escalar el hardware hay que identificar si la aplicación es CPU bound, memory bound o I/O bound.

## Preguntas de repaso

> [!question]- ¿Por qué la frecuencia de reloj de las CPU dejó de crecer y qué consecuencia tiene para el software?
> Porque la disipación térmica limita subir la frecuencia. Las mejoras vienen ahora de más núcleos y de procesadores especializados, así que el software tiene que ser concurrente o paralelizable para aprovecharlas.

> [!question]- ¿Qué significa que una aplicación sea I/O bound y qué hardware la ayuda?
> Que su tiempo se va esperando lecturas o escrituras de disco o de red, no calculando. La ayuda un almacenamiento más rápido (SSD NVMe), más RAM para cachear, o arquitecturas que reparten el I/O (RAID, Hadoop). Una CPU más rápida casi no la ayuda.

> [!question]- Diferencie ASIC y FPGA.
> El ASIC es un circuito fijo diseñado para una sola tarea: máximo rendimiento en ella, pero no se puede reprogramar. La FPGA es lógica reprogramable: más flexible y a veces más rápida que una CPU, pero menos eficiente que un ASIC en su tarea específica.

> [!question]- Según la comparación de inferencia, ¿cuántas veces más rápida es una GPU T4 que un servidor con dos CPU en ResNet-50? ¿Por qué tanta diferencia?
> Unas 27 veces. Porque la inferencia de redes neuronales son operaciones matriciales masivamente paralelas, justo lo que hacen bien los miles de núcleos simples de una GPU.

> [!question]- Al pasar de m6i.large a m6i.4xlarge, ¿qué recursos crecen y cuáles no? ¿Qué implica?
> Las vCPU (2 → 16) y la memoria (8 → 64 GiB) crecen 8 veces, pero el ancho de banda de red se mantiene "hasta 12,5 Gbps" y el de EBS "hasta 10 Gbps". Si el cuello de botella es la red o el disco, una instancia más grande no lo resuelve.

> [!question]- V o F: "Si una búsqueda es lenta, la primera medida debe ser contratar una instancia con más CPU".
> Falso. Primero hay que medir para saber si el problema es de CPU, memoria, I/O o del algoritmo. Una búsqueda lineal donde se necesitaba un índice o un hash no se arregla con más CPU.

> [!question]- ¿Por qué las abstracciones innecesarias son un problema de performance y no solo de legibilidad?
> Cada capa extra agrega llamadas, conversiones de datos y a veces copias o viajes por la red. Además aumentan el acoplamiento y la connascence, lo que hace más difícil optimizar el camino crítico.
