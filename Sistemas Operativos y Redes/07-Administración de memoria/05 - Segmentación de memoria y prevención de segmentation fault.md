---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/complemento
prerrequisitos:
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
---

# Segmentación de memoria y prevención de segmentation fault

Con [[03 - Relocalización, protección de memoria y registros base y límite|base y límite]], cada proceso ocupa un solo bloque grande y contiguo, que incluye el espacio vacío entre heap y stack. Eso hace difícil encontrarle lugar y agrava la [[04 - Swapping, fragmentación externa y algoritmos de asignación libre|fragmentación]]. La **segmentación** ataca ese problema dividiendo el proceso en trozos más pequeños.

## La idea

Las partes del espacio de direcciones ya tienen una interpretación propia: **código, heap, stack** (y datos). Un **segmento** es un espacio de direcciones contiguo con una de esas interpretaciones. En vez de guardar el programa como un bloque único en la memoria física, **cada segmento se guarda de forma independiente**. Al ser más pequeños, es más probable que quepan en huecos pequeños, y el espacio libre entre heap y stack ya no ocupa RAM.

![Partición del espacio de direcciones en segmentos independientes](adjuntos/Partici%C3%B3n%20del%20espacio%20de%20direcciones%20en%20segmentos%20independientes.png)

> [!example]- Transcripción de la imagen
> A la derecha, la *Virtual memory (Task A's)*: *Code* (0-2 KB), *Heap* (2-4 KB, crece hacia abajo), *Free* (4-14 KB) y *Stack* (14-16 KB, crece hacia arriba). A la izquierda, la *Physical memory (RAM)*: *OS* (0-4 KB), *Free* (4-8), *A's Code* (8-10), *Free* (10-12), *A's Stack* (12-14), *Free* (14-126) y *A's Heap* (126-128 KB). Las flechas unen cada segmento virtual con su lugar en la RAM, que no es contiguo ni sigue el mismo orden.

## Traducción con tabla de segmentos

Ahora hay varios espacios lineales de direcciones, y la MMU debe ser capaz de **traducir** cada uno: tiene una **tabla de segmentos** con la base física y el tamaño de cada segmento.

![Traducción con tabla de segmentos y MMU](adjuntos/Traducci%C3%B3n%20con%20tabla%20de%20segmentos%20y%20MMU.png)

> [!example]- Transcripción de la imagen
> Tabla *Segment / Base / Size*: `code`, 32768 (32 KB), 2048 (2 KB); `heap`, 34816 (34 KB), 2048 (2 KB); `stack`, 28672 (28 KB), 2048 (2 KB).

En el espacio virtual del proceso, el código empieza en 0 y el heap en 4096 (4 KB). La dirección virtual **100** está en el código, cuya base virtual es 0, así que: $32768 + 100 = 32868$.

![Verificación de límites en tabla de segmentos](adjuntos/Verificaci%C3%B3n%20de%20l%C3%ADmites%20en%20tabla%20de%20segmentos.png)

> [!example]- Transcripción de la imagen
> "Tabla de Segmentos: Dirección virtual (lógica): 100. Está en segmento code. Base + dirección = 32768+100 = 32868. Dirección física: 32868." Abajo, la memoria física de 0 a 64 KB (*Operating System* 0-16 KB; *Stack*, *Code* y *Heap* cerca de 28-36 KB; el resto *not in use*) y el espacio virtual de 0 a 16 KB (*Program Code* 0-2 KB, *Heap* 4-6 KB, *free* y *Stack* 14-16 KB). Una flecha roja a mano va del 100 virtual al segmento *Code* físico.

## El error: sumar la dirección virtual completa

¿Qué pasa con la dirección virtual **4200**, que está en el heap (4 KB = 4096 a 6 KB)? Si se suma tal cual a una base física, se sale del espacio del programa:

![Causa de segmentation fault por desborde de segmento](adjuntos/Causa%20de%20segmentation%20fault%20por%20desborde%20de%20segmento.png)

> [!example]- Transcripción de la imagen
> "Tabla de Segmentos: Dirección virtual (lógica): 4200 (offset). Está en segmento code. Base + dirección = 32768+4200 = 39016. Dirección física: 39016." En el dibujo, "Virtual" con el 100 en el código y el 4200 en el heap; la flecha azul del 4200 cae en una zona *not in use* de la memoria física. Nota al pie: "Espacio Libre: Espacio no asignado a este proceso produce segmentation fault".

Sumar 4200 a la base del código (la diapositiva anota 39016; la suma exacta es $32768 + 4200 = 36968$) da una dirección **fuera de todos los segmentos del proceso**: memoria que no le pertenece. Eso es un **segmentation fault**: el kernel detecta el acceso inválido y envía al proceso la señal `SIGSEGV`.

## La solución: usar el desplazamiento (offset)

La forma más simple de corregirlo es restar a la dirección virtual **la dirección virtual donde empieza su segmento**, lo que da el **desplazamiento** (*offset*) dentro del segmento, y sumarle eso a la base física del segmento:

$$\text{offset} = 4200 - 4096 = 104 \qquad \text{física} = 34816 + 104 = 34920$$

Así nunca se sale del segmento. Además, la MMU verifica que el offset sea **menor que el tamaño** del segmento: si no lo es, también es un *segmentation fault*. Como cada segmento tiene su propia entrada en la tabla, también se le pueden dar permisos distintos (por ejemplo, código de solo lectura). Eso sí, los segmentos tienen tamaños variables y siguen ocupando trozos contiguos, así que la fragmentación externa no desaparece del todo.

![Cálculo de desplazamiento relativo virtual en el heap](adjuntos/C%C3%A1lculo%20de%20desplazamiento%20relativo%20virtual%20en%20el%20heap.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano sobre la misma figura: el heap virtual ampliado, con el 4200 marcado a una distancia **X** de su inicio, y en la memoria física la anotación "B. Heap + X", es decir, la base física del heap más el desplazamiento.

```python
# Tabla de segmentos del ejemplo: nombre -> (base virtual, base física, tamaño)
SEGMENTOS = {
    "code": (0,    32768, 2048),
    "heap": (4096, 34816, 2048),
}

def traducir(virtual):
    for nombre, (base_v, base_f, tam) in SEGMENTOS.items():
        offset = virtual - base_v                 # desplazamiento dentro del segmento
        if 0 <= offset < tam:                     # ¿cae dentro del segmento?
            return f"{virtual} -> {nombre}, offset {offset} -> física {base_f + offset}"
    return f"{virtual} -> segmentation fault"

for v in (100, 4200, 5000, 3000):
    print(traducir(v))    # 32868, 34920, 35720 y segmentation fault (3000 está en el hueco)
```

Restar funciona, pero la MMU lo hace más rápido con lógica de bits: los primeros bits de la dirección indican el segmento y el resto el offset. Se ve en [[06 - Aritmética de bits y máscara de segmento en traducción de direcciones|máscaras de segmento]].

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene la segmentación frente a un solo bloque con base y límite?
> Cada segmento se ubica de forma independiente y es más pequeño, así que cabe en huecos más chicos, y el espacio vacío entre heap y stack no ocupa RAM.

> [!question]- ¿Qué guarda la tabla de segmentos?
> Para cada segmento (código, heap, stack…), su dirección base en la memoria física y su tamaño.

> [!question]- ¿Por qué sumar la dirección virtual 4200 a una base física produce un segmentation fault?
> Porque 4200 incluye la posición del heap dentro del espacio virtual (4096). Sumada completa, la dirección cae fuera de los segmentos del proceso, en memoria que no le pertenece.

> [!question]- Calcula la dirección física de la virtual 4200 con la tabla del ejemplo.
> Está en el heap, que empieza en 4096: offset $= 4200 - 4096 = 104$. Física $= 34816 + 104 = 34920$.
