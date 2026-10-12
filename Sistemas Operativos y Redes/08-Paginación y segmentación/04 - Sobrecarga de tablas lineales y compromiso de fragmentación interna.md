---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/apuntes
prerrequisitos:
  - "[[01 - Fundamentos de paginación, marcos y tabla de páginas]]"
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
---

# Sobrecarga de tablas lineales y compromiso de fragmentación interna

Una tabla de páginas lineal simple impone una sobrecarga de memoria inasumible en sistemas con espacios de direcciones de 32 o 64 bits. Intentar mitigar este tamaño incrementando el tamaño de página introduce el problema de la fragmentación interna.

## Sobrecarga de memoria y compromiso de diseño (mis apuntes)

> [!note] Apuntes de clase
> **PROBLEMA: Tablas de paginas muy grandes**
> Una Arquitectura con:
> - Espacio de direcciones virtuales de 32 bit
> - 32 bit → 2**32 Direcciones posibles → 2**32 Bytes
> - 2**32 Bytes = 2**2 * 2**30 Bytes = 4 * 1GB = 4GB Maximo de memoria Virtual!
> - Paginas de 4KB. 20 bit para pagina, 12 para offset
> - 4GB/4KB = 2**2 * 2**30/2**2 * 2**10 = 2**20 Paginas
> - Cuantas paginas caben en la memoria virtual:
>   - Si tengo 2**20 paginas → ¿Cuantos bits? = 20 bits para VPN
>   - Se cumple que son 20!!!
> - La tabla de paginas almacena 1 entrada: que almacena la traduccion de 1 pag a cierto frame
> - Por lo tanto: 2**20 pag → 2**20 PTE’s (page table entry) (entrada) → Guarda PFN + metadatos (32 bits aprox : 4B)
> - Tamaño Tabla paginas: 2*20 x 2**2B = 4MB (no es tanto)
> - Consideran que hay 1 tabla de paginas por cada proceso
> - Y suponiendo que tenemos corriendo 100 procesos → 400MB del S.O Solo en Tablas de PAG
>
> Conclusion: ES DEMASIADO!!!!
>
> **SOLUCION (NO FIABLE): Usar Paginas MAS GRANDES!!!**
> Si usamos paginas mas grandes, en lugar de usar Pag de 4KB, usamos paginas de 16KB:
> - 4GB/ 16KB: 2**2 * 2**30 / 2**4 ** 2**10 = 2**16
> - 2**16 es mucho menos que 2**20 !! Reducimos la cantidad de entradas de la pagina (PTE)
> - 2**16 PTES necesarias
>
> PROBLEMA CON ESTO: Como las paginas son muy grandes, y por ejemplo un proceso uso un poquito de una, tendremos mucho Espacio SobreAsignado.
> Por lo tanto, NO ES UNA SOLUCION FIABLE !!!!!
> A este problema se le llama FRAGMENTACION INTERNA!
>
> ```text
> Importante saberse:
> 1. Fragmentacion Externa: Espacios libres NO CONTIGUOS (sol: PAGINACION)
> 2. Fragmentacion Interna: Espacios Sobreasignados!
> ```
>
> Si utilizamos Paginas muy grandes → Tendremos Fragmentacion Interna.
> Si utlizamos Paginas muy pequeñas → Cada vez que tenga que cargar un proceso, tengo que cargar muchas traducciones en la TLB, y cargar mas paginas : Mas costoso! NEcesito un tamaño ideal que combine ambos mundos.
> Que solucione la fragmentacion interna, y que a la vez no tenga que cargar tantas paginas en memoria cuando quiero cargar un proceso.
> Necesito encontontrar un Trade Off que tenga un equilibrio.
> En LINUX: Se usan paginas de 8KB (en alpha AXP) y 4KB (en sistema intel x86).
>
> ESTRATEGIAS PARA SOLUCIONAR EL TAMAÑO DE TABLA DE PAG

> [!warning] Posible error
> En los apuntes figura la errata tipográfica "2*20 x 2**2B" donde se pretendía expresar $2^{20} \times 2^2\text{ bytes} = 2^{22}\text{ bytes} = 4\text{ MB}$. Asimismo, se leen "Consideran que hay", "utlizamos" y "encontontrar".

![Fragmentación interna por asignación de páginas grandes](adjuntos/Fragmentaci%C3%B3n%20interna%20por%20asignaci%C3%B3n%20de%20p%C3%A1ginas%20grandes.png)

> [!example]- Transcripción de la imagen
> Fenómeno de fragmentación interna:
> - Si un proceso requiere almacenar únicamente 100 bytes y el tamaño de página es de 16 KB, el sistema operativo debe asignarle un marco completo de 16 KB.
> - Los $16\,384 - 100 = 16\,284\text{ bytes}$ restantes quedan totalmente desaprovechados (*espacio sobreasignado*), atrapados dentro del marco sin que ningún otro proceso pueda utilizarlos.

> [!tip] Complemento: Comparativa formal de fragmentaciones
> - **Fragmentación Externa:** Ocurre con asignación de tamaño variable (particiones dinámicas, segmentación pura). Hay memoria física libre suficiente en total, pero dispersa en huecos no contiguos.
> - **Fragmentación Interna:** Ocurre con asignación de tamaño fijo (paginación). La memoria se desperdicia dentro de los bloques asignados porque el requerimiento del proceso no es múltiplo exacto del tamaño de bloque.

## Preguntas de repaso

> [!question]- ¿Por qué una tabla de páginas lineal de 4 MB por proceso es inviable en un servidor con cientos de procesos activos?
> Porque en un sistema con 500 procesos activos, las tablas lineales consumirían $500 \times 4\text{ MB} = 2\text{ GB}$ de memoria RAM física fija exclusivamente en estructuras de traducción del kernel, sin haber ejecutado todavía el código útil de las aplicaciones.

> [!question]- ¿Qué compromiso de diseño (*trade-off*) existe al seleccionar el tamaño de página de una arquitectura?
> Páginas muy pequeñas reducen la fragmentación interna pero disparan el tamaño de la tabla de páginas y causan saturación de la TLB. Páginas muy grandes reducen el tamaño de la tabla de páginas y maximizan la tasa de aciertos de la TLB, pero causan un desperdicio severo de memoria física por fragmentación interna.

> [!question]- ¿Cuál es el tamaño de página estándar adoptado en la mayoría de las arquitecturas comerciales (x86, ARM)?
> 4 Kilobytes ($4096\text{ bytes}$), determinado empíricamente como el punto de equilibrio óptimo entre fragmentación interna y sobrecarga de tablas y TLB.

