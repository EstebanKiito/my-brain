---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/tlb
  - origen/complemento
prerrequisitos:
  - "[[02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo]]"
  - "[[04 - Cambio de contexto y tipos de procesos]]"
---

# Localidad de referencia y gestión de TLB con ASID en cambios de contexto

En el ejemplo del arreglo, la [[02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo|TLB]] logró un 70% de aciertos. En sistemas reales el *hit rate* ronda el 99%. ¿Por qué funciona tan bien una caché tan pequeña? Por la **localidad de referencia**. Y como la TLB es una sola para todos los procesos, hay que resolver qué pasa con ella en cada **cambio de contexto**.

## Localidad de referencia

| Tipo | Idea | Ejemplo | Efecto en la TLB |
|---|---|---|---|
| **Espacial** | Después de acceder a una dirección $x$, el programa probablemente accederá a direcciones **cercanas** a $x$ | Recorrer un arreglo, que se guarda contiguo en memoria | Luego de un miss y de guardar la PTE en la TLB, vendrán muchos hits |
| **Temporal** | Una dirección recién accedida probablemente se **volverá a acceder** pronto | Una variable usada en cada vuelta de un ciclo | Una PTE recién guardada volverá a usarse pronto |

El comportamiento real depende de cada programa, pero la mayor parte del tiempo los programas manifiestan localidad, espacial o temporal. Por eso la TLB acierta casi siempre.

## La TLB en un cambio de contexto

Un cambio de contexto cambia el espacio de memoria en uso: de pasar del proceso A al proceso B, las traducciones de A **no le sirven** a B. Si la TLB tiene la entrada "página 0 → frame 255", ¿de qué proceso es? Hay que tener en cuenta que:

- **La TLB no se almacena** en la memoria del SO (como la tabla de páginas) **ni en el PCB**: está en la MMU.
- Lo que sí cambia en cada cambio de contexto es el **PTBR** (*page table base register*), que apunta a la tabla de páginas del proceso que entra.
- Las PTE de un proceso no sirven al siguiente.

Hay dos soluciones:

1. **Vaciar la TLB** (*flush*): marcar todos los bits de validez **V** en 0. Es simple, pero el proceso que vuelve a entrar parte con la TLB vacía y sufre muchos misses.
2. **Etiquetar cada entrada con un ASID** (*Address Space Identifier*), que funciona como un PID:
   - cada proceso tiene su propio ASID, guardado en su PCB;
   - el campo ASID permite que **coexistan entradas de distintos procesos** en la TLB.

Con ASID, cuando un proceso sale de la CPU no pierde sus traducciones, y al volver puede reutilizarlas sin tantos misses. En x86, por ejemplo, cambiar de tabla de páginas (recargar el registro `CR3`) vaciaba la TLB; el soporte posterior de PCID (el equivalente a ASID) permite evitarlo. ARM y MIPS usan ASID.

| VPN | PFN | V | ASID |
|---|---|---|---|
| 0 | 255 | 1 | 1 |
| 0 | 112 | 1 | 2 |

En este ejemplo, la página 0 del proceso con ASID 1 y la del proceso con ASID 2 coexisten en la TLB sin confundirse: la MMU solo usa las entradas cuyo ASID coincide con el del proceso en ejecución.

![Uso de ASID en la TLB para cambios de contexto](adjuntos/Uso%20de%20ASID%20en%20la%20TLB%20para%20cambios%20de%20contexto.png)

> [!example]- Transcripción de la imagen
> Formato de una entrada de TLB en dos filas de 32 bits (bits 0 a 31). Fila 1: **VPN** (bits 0-18), **G** (bit 19), una zona sin usar (20-23) y **ASID** (bits 24-31). Fila 2: una zona sin usar (0-1), **PFN** (bits 2-25), **C** (26-28), **D** (29), **V** (30) y otra zona sin usar (31). Es el formato de la TLB de MIPS: G marca páginas globales compartidas por todos los procesos, C son bits de coherencia de caché, D indica página modificada (*dirty*) y V entrada válida.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre localidad espacial y temporal?
> La espacial dice que, tras acceder a una dirección, probablemente se accederá a direcciones cercanas, como al recorrer un arreglo. La temporal dice que una dirección recién usada probablemente se volverá a usar pronto, como una variable dentro de un ciclo.

> [!question]- ¿Por qué el hit rate real de la TLB es cercano al 99%?
> Por la localidad: tras un miss, la PTE queda en la TLB y los accesos siguientes a la misma página (espacial) o a las mismas variables (temporal) aciertan.

> [!question]- ¿Por qué las entradas de la TLB de un proceso no sirven a otro?
> Porque cada proceso tiene su propio espacio de direcciones: la página 0 de A y la página 0 de B están en frames distintos. Usar la traducción de A para B accedería a la memoria equivocada.

> [!question]- ¿Qué ventaja tiene usar ASID frente a vaciar la TLB en cada cambio de contexto?
> Las traducciones de varios procesos conviven en la TLB, así que al volver a la CPU un proceso encuentra parte de sus traducciones y no parte desde cero con una racha de misses.
