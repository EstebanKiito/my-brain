---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/scheduling
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Sistemas de archivos/02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)\|02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)]]"
---

# Algoritmos de planificación de disco (Disk Scheduling)

El sistema operativo reordena las solicitudes de entrada/salida pendientes en la cola del controlador para minimizar los desplazamientos mecánicos del brazo lector (*seek time*) y optimizar el rendimiento global del disco.

## Planificación de solicitudes de disco (mis apuntes)

- Schedulling de Accesos
- Para minimizar los movimientos a la hora de buscar informacion en el disco
- El S.O solicita datos del disco especificando:
- Lectura? o Escritura?
- Direccion del Disco → CHS o LBA
- Direccion de memoria fisica (Buffer)
- El orden de atencion → Determina el seek time de la transferencia
- Numeros de secotres a transferir
- Objetivo: Minimizar la latencia de escritura (movimientos en un disco duro)
- SCHEDULING FCFS (FIFO)
- Primero en llegar, primero en ser atendido
- Justo, pero no necesariamente el de mejor servicio
- Este es el movimiento del brazo
- Si contamos en total las distancias que recorrio:
- Desplazamiento de 640
- FCFS dependemos mucho del orden de acceso → No podemos asumir nada
- SCHEDULING SSTF : (Shortest Seek Time First)
- Busca moverse lo menos posible → Busca en minimos locales los mas cercanos
- Desplazamiento de 208 (mucho menos)
- No es optimo → Posible inanicion
- 😭 Mientras estamos leyendo, pueden llegar peticiones cercanas, y provoca inanicion en los lejanos!
- SCHEDULING SCAN
- Elevador → Se va a ir moviendo completamente hacia un lado, y luego hacia el otro
- Lee todo lo que encuentre en el camino
- Tiempo de respuesta menos variado que SSTF
- El brazo lector no se desgasta tanto → No tiene que cambiar de direccion
- Pero es ineficiente igualmente, probablemente mas que los anteriores
- C-SCAN: Lo mismo pero va hasta la orilla y lee en una direccion (no lee entremedio, se dirige hasta la esquina y de ahi empieza a leer hacia adelante)
- LOOK y C-LOOK → Es SCAN pero sin llegar a los extremos

> [!warning] Posible error
> En los apuntes se escribe `Schedulling` con doble 'L' (scheduling) y `Numeros de secotres a transferir` (error tipográfico por sectores).

> [!tip] Complemento: Comparación de políticas de planificación
> Las solicitudes hacia el disco se formulan típicamente usando direccionamiento LBA (*Logical Block Addressing*) o históricamente CHS (*Cylinder-Head-Sector*). Para una cola de solicitudes sobre un disco de 200 cilindros ($0\text{ a }199$) con cola `98, 183, 37, 122, 14, 124, 65, 67` e inicio en el cilindro 53:
>
> 1. **FCFS (*First-Come, First-Served*):**
>    ![Planificación de disco First In First Out FCFS](adjuntos/Planificación%20de%20disco%20First%20In%20First%20Out%20FCFS.png)
>    > [!example]- Transcripción de la imagen
>    > Diagrama de movimiento de cabezal FCFS: orden exacto de llegada $53 \to 98 \to 183 \to 37 \to 122 \to 14 \to 124 \to 65 \to 67$.
>    > Desplazamiento total del brazo = 640 cilindros.
>
> 2. **SSTF (*Shortest Seek Time First*):**
>    ![Planificación de disco Shortest Seek Time First SSTF](adjuntos/Planificación%20de%20disco%20Shortest%20Seek%20Time%20First%20SSTF.png)
>    > [!example]- Transcripción de la imagen
>    > Diagrama SSTF: selecciona la solicitud con mínima distancia al cilindro actual.
>    > Recorrido: $53 \to 65 \to 67 \to 37 \to 14 \to 98 \to 122 \to 124 \to 183$.
>    > Desplazamiento total = 208 cilindros. Vulnerable a inanición (*starvation*) si continúan llegando solicitudes locales.
>
> 3. **SCAN (Elevador):**
>    ![Planificación de disco SCAN elevador](adjuntos/Planificación%20de%20disco%20SCAN%20elevador.png)
>    > [!example]- Transcripción de la imagen
>    > Diagrama SCAN: el brazo se desplaza en una dirección (hacia 0) atendiendo solicitudes ($53 \to 37 \to 14 \to 0$), rebota en el extremo y barre en sentido opuesto ($0 \to 65 \to 67 \to 98 \to 122 \to 124 \to 183$).
>
> 4. **C-SCAN (*Circular SCAN*) y F-SCAN:**
>    ![Planificación de disco C-SCAN y F-SCAN elevador circular](adjuntos/Planificación%20de%20disco%20C-SCAN%20y%20F-SCAN%20elevador%20circular.png)
>    > [!example]- Transcripción de la imagen
>    > Diagrama C-SCAN: barre en una sola dirección ($53 \to 183 \to 199$). Al llegar al final viaja rápidamente hasta 0 sin atender solicitudes intermedias, garantizando tiempos de espera más uniformes.
>    > F-SCAN congela la cola al iniciar el barrido para atender las nuevas solicitudes en una pasada posterior.
>
> 5. **LOOK y C-LOOK:**
>    ![Planificación de disco LOOK y C-LOOK](adjuntos/Planificación%20de%20disco%20LOOK%20y%20C-LOOK.png)
>    > [!example]- Transcripción de la imagen
>    > Diagrama LOOK/C-LOOK: idéntico a SCAN/C-SCAN pero el cabezal solo viaja hasta la solicitud más extrema en cada sentido ($183$ y $14$), sin gastar seek hasta los extremos físicos $199$ y $0$.

## Preguntas de repaso

> [!question]- ¿Por qué el algoritmo SSTF puede provocar inanición (*starvation*) en ciertas solicitudes?
> Porque al atender siempre la petición más cercana al cabezal actual, si un flujo continuo de nuevas solicitudes se concentra en cilindros cercanos, las solicitudes lejanas ubicadas en los extremos del disco pueden posponerse indefinidamente.

> [!question]- ¿Qué ventaja fundamental introduce C-SCAN respecto a SCAN convencional?
> Proporciona un tiempo de espera mucho más uniforme entre cilindros. En SCAN, cuando el cabezal rebota en un extremo, los sectores recién visitados tienen muy poca probabilidad de tener solicitudes, mientras que los sectores del otro extremo llevan el doble de tiempo esperando. C-SCAN elimina esa asimetría barriendo siempre en el mismo sentido.

> [!question]- ¿Cuál es la diferencia práctica entre SCAN y LOOK?
> SCAN desplaza obligatoriamente el cabezal hasta el extremo físico final del disco ($0$ o $N-1$) antes de cambiar de sentido, mientras que LOOK solo se mueve hasta la última petición pendiente en esa dirección y cambia de sentido inmediatamente.

