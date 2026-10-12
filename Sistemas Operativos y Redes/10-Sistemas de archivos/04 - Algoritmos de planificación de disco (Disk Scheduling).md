---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/scheduling
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)\|02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)]]"
---

# Algoritmos de planificación de disco (Disk Scheduling)

En un [[02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)|disco duro]], lo más caro es mover el brazo (*seek time*). Si hay varias solicitudes pendientes, el orden en que se atienden determina cuánto se mueve el brazo. Por eso el SO **encola y ordena** las solicitudes: el objetivo es minimizar los movimientos del brazo al buscar la información.

## Qué pide el SO al disco

Cada solicitud especifica: si es **lectura o escritura**, la **dirección en el disco** (CHS, *cylinder-head-sector*, o LBA, *logical block address*), la **dirección de memoria física** del buffer y el **número de sectores** a transferir. La métrica para comparar algoritmos es el **desplazamiento total del brazo**, medido en cilindros.

Todos los ejemplos usan la cola `98, 183, 37, 122, 14, 124, 65, 67`, con el cabezal partiendo en el cilindro **53** (cilindros 0 a 199).

## FCFS (FIFO)

Atiende en **orden de llegada**: es **justo, pero no necesariamente el de mejor servicio**, y depende totalmente del orden en que llegan las solicitudes. Desplazamiento: **640**.

![Planificación de disco First In First Out FCFS](adjuntos/Planificaci%C3%B3n%20de%20disco%20First%20In%20First%20Out%20FCFS.png)

> [!example]- Transcripción de la imagen
> "queue = 98, 183, 37, 122, 14, 124, 65, 67; head starts at 53". Eje de cilindros 0 a 199. El recorrido zigzaguea en el orden de llegada: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67. Encima hay trazos a mano.

## SSTF (*Shortest Seek Time First*)

Atiende siempre la solicitud **más cercana** a la posición actual: busca moverse lo menos posible. Para este ejemplo, el material indica un desplazamiento de **208**; sumando el recorrido de la figura, da 236. En ambos casos es mucho menos que FCFS.

- **No es óptimo**: elegir siempre el más cercano (un mínimo local) no garantiza el menor total.
- **Posible inanición**: mientras se atiende una zona pueden seguir llegando pedidos cercanos, y los sectores alejados esperan indefinidamente.

![Planificación de disco Shortest Seek Time First SSTF](adjuntos/Planificaci%C3%B3n%20de%20disco%20Shortest%20Seek%20Time%20First%20SSTF.png)

> [!example]- Transcripción de la imagen
> La misma cola y el mismo inicio. Recorrido: 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183.

## SCAN (el elevador) y sus variantes

| Algoritmo | Cómo se mueve | Recorrido en el ejemplo |
|---|---|---|
| **SCAN** | Va de un extremo al otro, como un ascensor, atendiendo todo lo que encuentra en el camino; luego vuelve | 53 → 37 → 14 → **0** → 65 → … → 183 |
| **C-SCAN** | Atiende en un solo sentido; al llegar al extremo, salta al extremo opuesto sin atender nada y sigue en el mismo sentido | 53 → 65 → … → 183 → **199** → **0** → 14 → 37 |
| **LOOK / C-LOOK** | Como SCAN / C-SCAN, pero no llegan hasta los extremos del disco si no es necesario: se devuelven en la última solicitud | C-LOOK: 53 → … → 183 → 14 → 37 |
| **F-SCAN** | Elevador "congelado": no atiende solicitudes nuevas hasta terminar la cola actual | — |

SCAN da tiempos de respuesta **menos variados** que SSTF, y el brazo cambia de dirección menos veces. Pero las solicitudes que llegan **justo después de que el brazo pasó** esperan mucho: tienen que aguardar el viaje de ida y de vuelta. C-SCAN lo corrige barriendo siempre en el mismo sentido.

![Planificación de disco SCAN elevador](adjuntos/Planificaci%C3%B3n%20de%20disco%20SCAN%20elevador.png)

> [!example]- Transcripción de la imagen
> SCAN con la misma cola: desde 53 baja a 37, 14 y el extremo 0, y luego sube atendiendo 65, 67, 98, 122, 124 y 183.

![Planificación de disco C-SCAN y F-SCAN elevador circular](adjuntos/Planificaci%C3%B3n%20de%20disco%20C-SCAN%20y%20F-SCAN%20elevador%20circular.png)

> [!example]- Transcripción de la imagen
> "SCHEDULING C-SCAN. *C-SCAN. Elevador circular.* Las solicitudes que llegan justo después que el brazo ha pasado, llevan más tiempo esperando. Llega a un extremo y se mueve completamente al extremo opuesto. Continúa en el mismo sentido." Recorrido: 53 → 65 → … → 183 → 199, salto a 0 → 14 → 37. Al pie: "No atiende solicitudes nuevas hasta haber acabado con la cola. *F-SCAN. Elevador congelado.*"

![Planificación de disco LOOK y C-LOOK](adjuntos/Planificaci%C3%B3n%20de%20disco%20LOOK%20y%20C-LOOK.png)

> [!example]- Transcripción de la imagen
> "SCHEDULING LOOK Y C-LOOK. Similares a SCAN y C-SCAN, pero no se mueven hasta los extremos si no es necesario." Recorrido C-LOOK: 53 → 65 → … → 183, salto a 14 → 37.

```python
COLA, INICIO = [98, 183, 37, 122, 14, 124, 65, 67], 53

def recorrido(orden, pos=INICIO):
    total = 0
    for c in orden:
        total += abs(c - pos); pos = c
    return total

def sstf(cola, pos=INICIO):
    pendientes, orden = list(cola), []
    while pendientes:
        c = min(pendientes, key=lambda x: abs(x - pos))   # el más cercano
        orden.append(c); pendientes.remove(c); pos = c
    return orden

print(recorrido(COLA))          # FCFS: 640
print(recorrido(sstf(COLA)))    # SSTF: 236
```

## Preguntas de repaso

> [!question]- ¿Qué datos especifica el SO en cada solicitud al disco?
> Si es lectura o escritura, la dirección en el disco (CHS o LBA), la dirección de memoria física del buffer y cuántos sectores transferir.

> [!question]- ¿Por qué SSTF puede causar inanición?
> Porque siempre atiende la solicitud más cercana; si siguen llegando pedidos cerca del brazo, los lejanos se postergan indefinidamente.

> [!question]- ¿Qué problema de SCAN corrige C-SCAN?
> Que las solicitudes que llegan justo detrás del brazo esperan el viaje de ida y vuelta. C-SCAN barre siempre en un mismo sentido y salta al otro extremo, lo que hace las esperas más parejas.

> [!question]- ¿En qué se diferencian SCAN y LOOK?
> SCAN llega hasta el extremo del disco antes de devolverse; LOOK se devuelve en la última solicitud pendiente de esa dirección, sin recorrer cilindros vacíos.
