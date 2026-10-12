---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de paginación, marcos y tabla de páginas]]"
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
---

# Sobrecarga de tablas lineales y compromiso de fragmentación interna

La paginación elimina la fragmentación externa, pero trae un costo nuevo: la tabla de páginas tiene una entrada **por cada página posible** del espacio virtual, y eso, en una arquitectura real, es mucha memoria. Agrandar las páginas achica la tabla, pero crea otro tipo de desperdicio: la **fragmentación interna**.

## El problema: tablas de páginas muy grandes

Tomemos una arquitectura con direcciones virtuales de **32 bits** y páginas de **4 KB**:

1. $2^{32}$ direcciones $= 2^{32}$ bytes $= 2^2 \cdot 2^{30} = 4$ GB de memoria virtual como máximo.
2. Páginas de 4 KB $= 2^{12}$ B → **12 bits de offset** y $32 - 12 = $ **20 bits para la página**.
3. Cantidad de páginas: $4\text{ GB} / 4\text{ KB} = 2^{32}/2^{12} = 2^{20}$. Coincide con los 20 bits de VPN.
4. La tabla tiene una PTE por página: $2^{20}$ PTE. Cada PTE (PFN + metadatos) mide unos 32 bits = 4 B.
5. Tamaño de la tabla: $2^{20} \times 2^2\text{ B} = 4$ MB.

4 MB no parece tanto, pero **hay una tabla por proceso**. Con 100 procesos corriendo, el SO gasta **400 MB solo en tablas de páginas**. Es demasiado.

## ¿Páginas más grandes? Fragmentación interna

Si las páginas son más grandes, hay menos páginas y la tabla es más chica:

| Tamaño de página | Bits de VPN | PTE | Tamaño de la tabla (PTE de 4 B) |
|---|---|---|---|
| 4 KB | 20 | $2^{20}$ | 4 MB |
| 16 KB | 18 | $2^{18}$ | 1 MB |
| 1 MB | 12 | $2^{12}$ | 16 KB |

Pero no es una solución fiable. Si un proceso usa solo un poquito de una página, igual se le asigna la página completa, y queda mucho **espacio sobreasignado**: memoria asignada que nadie usa. Eso es la **fragmentación interna**. Con páginas de 1 MB:

- un proceso de un número entero de MB recibe exactamente lo que necesita;
- un proceso de **16 KB recibe 1 MB** (1008 KB desperdiciados);
- un proceso de **1025 KB recibe 2 MB** (1023 KB desperdiciados).

![Fragmentación interna por asignación de páginas grandes](adjuntos/Fragmentaci%C3%B3n%20interna%20por%20asignaci%C3%B3n%20de%20p%C3%A1ginas%20grandes.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano: a la izquierda, un espacio virtual dividido en páginas, con la primera muy usada (rayado rojo grueso) y la segunda apenas usada (una franja roja delgada). Flechas las llevan a dos frames de la memoria física de la derecha. El primer frame queda lleno; del segundo solo se usa una franja, y el resto del frame queda asignado pero vacío.

> [!tip] Dos fragmentaciones que no hay que confundir
> - **Fragmentación externa:** espacios libres **no contiguos** entre bloques. Aparece con asignación de tamaño variable; la **paginación** la elimina.
> - **Fragmentación interna:** espacio **sobreasignado** *dentro* de un bloque, porque lo pedido no llena el bloque completo. Aparece con bloques de tamaño fijo, como las páginas.

## El compromiso del tamaño de página

- **Páginas muy grandes** → tablas pequeñas, pero mucha fragmentación interna.
- **Páginas muy pequeñas** → poca fragmentación interna, pero tablas enormes y, al cargar un proceso, muchas más páginas que traer y muchas más traducciones que cargar en la TLB: es más costoso.

Hay que encontrar un tamaño que equilibre ambos mundos. Linux, por ejemplo, usa páginas de 4 KB en x86 y de 8 KB en Alpha AXP. Para achicar las tablas sin agrandar las páginas existen otras estrategias: [[05 - Arquitectura de segmentos paginados|segmentos paginados]] y [[06 - Paginación multinivel y tablas de páginas invertidas|tablas multinivel e invertidas]].

## Preguntas de repaso

> [!question]- ¿Cuánto mide una tabla de páginas lineal con direcciones de 32 bits, páginas de 4 KB y PTE de 4 B?
> Hay $2^{32}/2^{12} = 2^{20}$ páginas, así que $2^{20}$ PTE de 4 B: $2^{22}$ B = 4 MB por proceso.

> [!question]- ¿Por qué 4 MB por tabla es un problema?
> Porque hay una tabla por proceso. Con 100 procesos son 400 MB de memoria ocupados solo en tablas de páginas.

> [!question]- ¿Qué es la fragmentación interna y por qué aparece con páginas grandes?
> Es memoria asignada a un proceso que este no usa, dentro de su última página. Mientras más grande la página, más espacio puede quedar sin usar: un proceso de 16 KB con páginas de 1 MB desperdicia 1008 KB.

> [!question]- ¿Qué fragmentación elimina la paginación y cuál introduce?
> Elimina la externa, porque cualquier frame libre sirve para cualquier página. Introduce la interna, porque la última página de un proceso casi nunca se usa entera.
