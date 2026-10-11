---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/tlb
  - origen/apuntes
prerrequisitos:
  - "[[02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo]]"
  - "[[04 - Cambio de contexto y tipos de procesos]]"
---

# Localidad de referencia y gestión de TLB con ASID en cambios de contexto

La altísima efectividad real de la caché TLB (tasas de acierto superiores al 99%) se fundamenta en el principio de localidad de referencia. Para mantener este rendimiento a través de cambios de contexto entre procesos, las arquitecturas introducen identificadores de espacio de direcciones (ASID).

## Principios de localidad y soporte para cambios de contexto (mis apuntes)

> [!note] Apuntes de clase
> **Clase 8**
> 09/09/2024
>
> Explicaciones de porqué TLB Hit Rate REALES! ~= 99%
>
> **Localidad Espacial:**
> Estamos escribiendo en un arreglo → Se guarda de forma contigua en memoria.
> Como el programa probablemente vaya a acceder a memoria cercana a la buscada (memoria espacialmente cercena).
> Luego de un miss → Vendrán muchos HITS.
>
> **Localidad Temporal:**
> Acceder a variables que ya habiamos accedido con anterioridad.
> Como el programa accedio a una variable, probablemente será accedida en un futuro.
>
> Ahora bien, como identificamos las traducciones? Sobre todo en los cambios de contexto:
> Recordatorio: Cambio contexto: Cambiar espacio de memoria que estoy utilizando, desde un proceso A a un proceso B.
> Porque la TLB NO! se almacena en memoria del S.O. (como la Tabla de Páginas), ni en el PCB.
> PTE’s de un proceso, no le sirven al siguiente!
> Si por ejemplo tuviera 0 (pag)→ 255 (frame), ¿A que proceso le pertenece esta traduccion? → Tenemos un ASID (funciona como un PID).
> - Cada proceso tiene su unico ASID (en su PCB)
> - Campo ASID permite que coexistan entradas de distintos procesos en la TLB
>
> ASID: Adress Space Identifier:
> V = Bit de validez: Si la entrada es valida o no
> Con esto:
> Si un proceso que ejecuta, sale de la cpu → En lugar d eperder traducciones, al volver a entrar, las puede reutilizar sin tener Tantos Miss’s.

> [!warning] Posible error
> En los apuntes figuran erratas de tipeo: "cercena" por cercana, "Adress Space Identifier" por *Address Space Identifier*, y "d eperder" por de perder.

![Uso de ASID en la TLB para cambios de contexto](adjuntos/Uso%20de%20ASID%20en%20la%20TLB%20para%20cambios%20de%20contexto.png)

> [!example]- Transcripción de la imagen
> Estructura de entradas en una TLB con soporte ASID:
> | VPN | PFN | Valid ($V$) | Prot | ASID |
> |---|---|---|---|---|
> | 10 | 100 | 1 | rwx | 1 |
> | 10 | 170 | 1 | r-x | 2 |
> | 50 | 204 | 1 | rw- | 1 |
> 
> Dos procesos diferentes (ASID 1 y ASID 2) pueden tener mapeada la misma página virtual (VPN 10) a distintos marcos físicos (PFN 100 y PFN 170) simultáneamente en la misma caché de hardware sin interferencia.

> [!tip] Complemento: Estrategias ante cambios de contexto
> En arquitecturas sin soporte ASID (como x86 original), el kernel debe vaciar completamente la TLB en cada cambio de contexto (*TLB Flush*, típicamente recargando el registro `CR3`). Esto provoca una ráfaga masiva de fallos (*cold-start misses*) tras cada conmutación de proceso. Con ASID (ARM, MIPS, y x86 moderno con PCID), la TLB no se vacía: el procesador simplemente compara el ASID de la entrada con el ASID del proceso actualmente en ejecución.

## Preguntas de repaso

> [!question]- ¿Qué diferencia existe entre localidad espacial y localidad temporal en la ejecución de un programa?
> La localidad espacial establece que si se referencia una posición de memoria, es muy probable que se referencien posiciones contiguas o cercanas en el futuro inmediato (e.g. recorrer un arreglo o instrucciones secuenciales). La localidad temporal establece que si se accede a una dirección, es muy probable que se vuelva a acceder a la misma dirección prontamente (e.g. contadores en bucles o funciones recursivas).

> [!question]- ¿Por qué una entrada de TLB válida para el Proceso A resultaría desastrosa si fuera utilizada por el Proceso B?
> Porque cada proceso posee su propio espacio de direcciones virtual independiente. El VPN 0 del Proceso A apunta a su propio código en RAM, mientras que el VPN 0 del Proceso B apunta a datos completamente distintos. Reutilizar la traducción rompería el aislamiento y causaría corrupción de memoria o fuga de seguridad.

> [!question]- ¿Qué ventaja de rendimiento ofrece el campo ASID frente a realizar un vaciado completo (*flush*) de la TLB?
> Permite conservar en la TLB las traducciones de múltiples procesos concurrentes. Cuando el planificador devuelve la CPU al Proceso A, muchas de sus entradas continúan residentes y válidas en la caché, evitando la penalización de tener que recargar todas las traducciones desde RAM con sucesivos TLB misses.
