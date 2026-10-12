---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/segmentacion
  - so/paginacion
  - origen/complemento
prerrequisitos:
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
  - "[[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna]]"
---

# Arquitectura de segmentos paginados

Una tabla de páginas lineal tiene una entrada para **cada** página posible del espacio virtual, aunque el proceso use muy pocas. La mayor parte del espacio entre heap y stack nunca se usa, y sus entradas igual ocupan memoria. Los **segmentos paginados** combinan segmentación y paginación para no gastar entradas en esos huecos.

## El problema: entradas vacías

Los procesos no suelen ocupar todas sus páginas. Con un espacio virtual de **16 páginas** y un proceso que **efectivamente usa 4**, quedan **12 entradas vacías (75%)** en la tabla de páginas. Bastaría con tener entradas solo para las páginas usadas.

## La idea: una tabla de páginas por segmento

**Cada segmento tiene su propia tabla de páginas.** La dirección virtual se divide en tres partes:

![Esquema de segmentos paginados con tablas independientes](adjuntos/Esquema%20de%20segmentos%20paginados%20con%20tablas%20independientes.png)

> [!example]- Transcripción de la imagen
> Una dirección virtual de 32 bits: **Seg** en los bits 31-30, **VPN** en los bits 29-12 y **Offset** en los bits 11-0.

- **Bits de segmento** (los primeros 2): indican uno de **4 segmentos posibles**.
- **VPN**: la página **dentro del segmento**.
- **Offset**: el byte dentro de la página.

Para cada segmento, la MMU guarda un par **base / límite** con otro significado que en la segmentación pura:

- **base**: la dirección de la **tabla de páginas** del segmento;
- **límite**: cuántas **páginas** tiene ese segmento.

Así, la tabla de cada segmento solo tiene entradas para las páginas que el segmento realmente usa, y desaparecen las entradas vacías del hueco entre heap y stack.

![Reducción de entradas vacías en segmentos paginados](adjuntos/Reducci%C3%B3n%20de%20entradas%20vac%C3%ADas%20en%20segmentos%20paginados.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano: una tabla dividida en bloques de distinto tamaño marcados **S0**, **S1**, **S2** y **S3**. El bloque S0 se subdivide en entradas **VPN0**, **VPN1**, … Cada segmento tiene su propia porción de entradas, de su propio tamaño.

## Traducción paso a paso

1. Con los bits de segmento se elige la base y el límite del segmento.
2. Se verifica que el **VPN < límite**. Si no, la dirección no pertenece al segmento: *segmentation fault*.
3. Se lee la PTE en la posición VPN de la tabla del segmento y se obtiene el PFN.
4. Dirección física = PFN seguido del offset.

```python
SEG_SHIFT, VPN_SHIFT = 30, 12
VPN_MASK, OFFSET_MASK = 0x3FFFF000, 0xFFF

# Una tabla de páginas por segmento; "limit" = cuántas páginas tiene de verdad
SEGMENTOS = {
    0: {"tabla": [7, 3],    "limit": 2},   # código: 2 páginas
    1: {"tabla": [12],      "limit": 1},   # heap: 1 página
    3: {"tabla": [20, 21],  "limit": 2},   # stack: 2 páginas
}

def traducir(va):
    seg = va >> SEG_SHIFT                       # bits 31-30
    vpn = (va & VPN_MASK) >> VPN_SHIFT          # bits 29-12
    off = va & OFFSET_MASK                      # bits 11-0
    s = SEGMENTOS.get(seg)
    if s is None or vpn >= s["limit"]:
        return "segmentation fault"
    return (s["tabla"][vpn] << VPN_SHIFT) | off

print(hex(traducir(0x00001010)))   # seg 0, VPN 1 -> 0x3010
print(traducir(0x40005000))        # seg 1, VPN 5 >= límite 1 -> segmentation fault
```

En este ejemplo hay 5 entradas en total, en vez de las $2^{20}$ que tendría una tabla lineal de 32 bits con páginas de 4 KB.

> [!warning] Vuelve la fragmentación externa
> Las tablas de páginas de cada segmento tienen **tamaños distintos** y cada una debe quedar contigua en memoria. Con eso **vuelve la fragmentación externa**, ahora entre tablas de páginas. Además, un segmento muy disperso (por ejemplo, un heap grande y poco usado) igual desperdicia entradas. Las [[06 - Paginación multinivel y tablas de páginas invertidas|tablas multinivel]] atacan esto sin depender de segmentos.

## Preguntas de repaso

> [!question]- ¿Qué problema de las tablas lineales resuelven los segmentos paginados?
> El de las entradas vacías: una tabla lineal tiene entradas para todas las páginas posibles, aunque el proceso use pocas. Con una tabla por segmento solo hay entradas para las páginas de cada segmento.

> [!question]- ¿Cómo se divide una dirección virtual en segmentos paginados?
> En bits de segmento (cuál de los 4 segmentos), VPN (la página dentro del segmento) y offset (el byte dentro de la página).

> [!question]- ¿Qué significan base y límite en este esquema?
> La base es la dirección de la tabla de páginas del segmento, y el límite, la cantidad de páginas del segmento. Si el VPN no es menor que el límite, el acceso es un segmentation fault.

> [!question]- ¿Por qué vuelve la fragmentación externa?
> Porque cada segmento tiene una tabla de páginas de tamaño distinto que debe ocupar memoria contigua, y entre esas tablas pueden quedar huecos difíciles de reutilizar.
