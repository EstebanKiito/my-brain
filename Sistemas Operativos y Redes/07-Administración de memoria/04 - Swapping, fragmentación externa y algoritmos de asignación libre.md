---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/complemento
prerrequisitos:
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
  - "[[01 - Niveles de planificación y ciclo de ráfagas CPU-IO]]"
---

# Swapping, fragmentación externa y algoritmos de asignación libre

¿Cuántos procesos caben en memoria y qué pasa si se llena? Con [[03 - Relocalización, protección de memoria y registros base y límite|base y límite]], cada proceso ocupa un bloque contiguo. Cuando la RAM no alcanza, se mueven procesos completos al disco, y ese ir y venir deja la memoria llena de huecos. Esta nota trata de ambas cosas: el **swapping** y qué hacer con los **huecos**.

## Swapping

El **espacio swap** es una zona del disco (memoria secundaria) que se usa como extensión de la memoria principal cuando esta se acaba. Hay dos operaciones:

- **swap-out**: la memoria de un proceso se copia de la RAM al disco (al espacio swap);
- **swap-in**: la memoria del proceso se copia del disco de vuelta a la RAM.

El encargado es el [[01 - Niveles de planificación y ciclo de ráfagas CPU-IO|scheduler de mediano plazo]]. Gracias a la relocalización con base y límite, el proceso puede volver a un **lugar distinto** del que tenía: basta cambiar su registro base.

![Mecanismo de swapping y generación de huecos de memoria](adjuntos/Mecanismo%20de%20swapping%20y%20generaci%C3%B3n%20de%20huecos%20de%20memoria.png)

> [!example]- Transcripción de la imagen
> "Procesos pueden ser cargados y descargados de la memoria". Siete estados de la memoria en el tiempo, (a) a (g), con el *Operating system* siempre abajo: (a) se carga A; (b) se carga B; (c) se carga C; (d) sale A y deja un hueco; (e) entra D en parte de ese hueco; (f) sale B; (g) A vuelve, pero en otra posición (entre D y C). Las zonas rayadas son memoria libre. "Memoria del sistema queda con huecos. ¿Qué hacer con los huecos?"

## El problema de los huecos: fragmentación externa

Como los procesos entran y salen, **quedan espacios libres** entre ellos. Puede ocurrir que la suma de los huecos alcance para un proceso nuevo, pero que **ningún hueco individual sea lo bastante grande**: eso es la **fragmentación externa**.

> [!warning] Compactar: posible, pero no se hace
> La **compactación** junta toda la memoria ocupada y fusiona los huecos en uno solo. Requiere copiar la memoria de los procesos a otras direcciones y actualizar los registros base y límite de cada uno, lo que es **muy caro**. En la práctica no se hace: es mejor asignar los espacios de manera que no haga falta compactar.

![Compactación de memoria para fusionar huecos libres](adjuntos/Compactaci%C3%B3n%20de%20memoria%20para%20fusionar%20huecos%20libres.png)

> [!example]- Transcripción de la imagen
> Dos memorias de 0 a 64 KB con el *Operating System* en 0-16 KB. **Not Compacted:** *not in use* (16-24), *Allocated* (24-32), *not in use* (un trozo pequeño cerca de 32-36), *Allocated* (hasta 40), *not in use* (40-56), *Allocated* (56-64). **Compacted:** *Allocated* contiguo de 16 a 40 KB y *not in use* contiguo de 40 a 64 KB.

## Estrategias de asignación

Para elegir dónde poner un proceso nuevo, con la idea de desperdiciar la menor cantidad de memoria posible:

| Estrategia | Elige | Idea |
|---|---|---|
| **First fit** | El **primer** hueco donde quepa | Rápida: no revisa toda la lista |
| **Best fit** | El hueco donde cabe y que **deja menos espacio** sobrante (el más pequeño posible) | No "gastar" huecos grandes en pedidos chicos |
| **Worst fit** | El hueco que **deja más espacio** libre (el más grande) | Que lo que sobre sea lo bastante grande para que quepa otro programa |

Con los huecos de la figura (6, 14, 19, 11 y 13 KB) y un pedido de 12 KB:

| Estrategia | Hueco elegido | Sobran |
|---|---|---|
| First fit | 14 KB | 2 KB |
| Best fit | 13 KB | 1 KB |
| Worst fit | 19 KB | 7 KB |

![Estrategias de colocación contigua First Fit y Best Fit](adjuntos/Estrategias%20de%20colocaci%C3%B3n%20contigua%20First%20Fit%20y%20Best%20Fit.png)

> [!example]- Transcripción de la imagen
> A la izquierda, una memoria con zonas ocupadas (azul) y huecos de 6, 14, 19, 11 y 13 KB. A la derecha, **First fit**: el proceso de 12 KB (rojo) queda en el primer hueco donde cabe, el de 14 KB.

![Estrategia Worst Fit y fragmentación externa](adjuntos/Estrategia%20Worst%20Fit%20y%20fragmentaci%C3%B3n%20externa.png)

> [!example]- Transcripción de la imagen
> **Best fit**: la misma memoria, con el proceso de 12 KB (rojo) en el último hueco, el de 13 KB, que es el más ajustado.

Con **cualquier** estrategia pueden quedar espacios libres no contiguos. Los supuestos de este esquema son que los procesos se pueden reubicar en cualquier parte de la memoria, pero que deben ocupar **espacios contiguos**. En el ejemplo, un pedido de 20 KB no cabe en ningún hueco aunque haya 63 KB libres en total. Se ha observado (la "regla del 50%") que, con *first fit*, por cada $N$ bloques asignados se pierden del orden de $N/2$ por fragmentación. Por eso se buscaron esquemas que no exijan contigüidad: [[05 - Segmentación de memoria y prevención de segmentation fault|segmentación]] y, sobre todo, paginación.

```python
def elegir(huecos, pedido, estrategia):
    """huecos: tamaños en KB, en orden de memoria. Devuelve el índice elegido o None."""
    candidatos = [(i, h) for i, h in enumerate(huecos) if h >= pedido]
    if not candidatos:
        return None                                   # no cabe en ningún hueco contiguo
    if estrategia == "first":
        return candidatos[0][0]                       # el primero donde cabe
    if estrategia == "best":
        return min(candidatos, key=lambda c: c[1])[0] # el que deja menos sobrante
    if estrategia == "worst":
        return max(candidatos, key=lambda c: c[1])[0] # el que deja más sobrante

huecos = [6, 14, 19, 11, 13]
for e in ("first", "best", "worst"):
    i = elegir(huecos, 12, e)
    print(f"{e:5}: hueco de {huecos[i]} KB, sobran {huecos[i] - 12} KB")
print("pedido de 20 KB:", elegir(huecos, 20, "first"), "aunque hay", sum(huecos), "KB libres")
```

## Preguntas de repaso

> [!question]- ¿Qué hacen swap-out y swap-in, y quién los decide?
> Swap-out copia la memoria de un proceso de la RAM al disco y swap-in la trae de vuelta. Los decide el scheduler de mediano plazo, que regula cuántos procesos hay en memoria.

> [!question]- ¿Qué es la fragmentación externa?
> Es cuando la memoria libre total alcanzaría para un proceso, pero está repartida en huecos no contiguos, y ninguno es lo bastante grande por sí solo.

> [!question]- ¿Por qué no se compacta la memoria?
> Porque exige copiar la memoria de los procesos a otras direcciones y actualizar los registros base y límite de cada uno, lo que es muy caro.

> [!question]- Con huecos de 6, 14, 19, 11 y 13 KB, ¿dónde queda un proceso de 12 KB con cada estrategia?
> First fit, en el de 14 KB (el primero donde cabe). Best fit, en el de 13 KB (el que deja menos sobrante). Worst fit, en el de 19 KB (el que deja más).
