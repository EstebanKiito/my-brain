---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/tlb
  - origen/apuntes
prerrequisitos:
  - "[[01 - Fundamentos de paginación, marcos y tabla de páginas]]"
---

# Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo

Para resolver la duplicación en el tiempo de acceso que impone consultar la tabla de páginas en RAM, la MMU incorpora una memoria caché asociativa de hardware ultrarrápida denominada Translation Lookaside Buffer (TLB).

## Aceleración con TLB y cálculo de rendimiento (mis apuntes)

> [!note] Apuntes de clase
> Solucion: Para acelerar acceso a memoria: fully associative caché de direcciones en MMU.
> Para esto utilizaremos un CACHE llamado TLB.
>
> **TLB Translation look-aside buffer (TLB):**
> - Traducciones de VPN → PFN
> - Se almacenara dentro de la memoria de la cpu, y no dentro de la memoria principal
> - TLB HIT: Encontramos traduccion
> - TLB Miss: Traducción no esta en caché
>
> Con esto, los accesos a memorias se verían asi:
> Con esto, si obtenemos un TLB Miss → Nos demorariamos mas, porque tenemos que buscar las mismas operaciones que antes (buscar en page table y physical memory) sumado a buscar en la tlb y no encontrar, si tenemos un tbl hit, nos ahorramos buscar en la page table, tlb es mucho mas rapido de buscar (no es significiativo realmente si hay tlb miss).
>
> **EJEMPLO DE TLB:**
> ```c
> int sum = 0;
> for (i = 0; i<10; i++){
> 	sum += a[i];
> }
> ```
>
> Si solo hacemos accesos a memoria sin tlb:
> Tenemos que hacer las 2 operaciones por cada acceso a memoria a[i].
> Por lo tanto son 10*2 = 20 Accesos a memoria.
>
> Con TLB, primero veamos como esta almacenado en la memoria del programa:
> Esto, dado que el espacio virtual de 8 bit, con paginas de 16B, almacenando un arreglo de 10 int (4B):
> - Sum = 0 → 4B
> - a[0] → 4B
> - a[1] → 4B
> - a[2] → 4B
> Ahi ya tenemos 16B, por lo que saltamos a otra pagina.
> a[3], a[4], a[5], a[6] caen en la siguiente pagina, y asi…
>
> Notemos que, cada vez que acceda a un valor por pagina, suponiendo que no estaba en la cache, nos da un miss, pero los siguientes, ya estan cargados en la tlb, por lo tanto, son hits:
> Asi tenemos Miss*3 , Hit*7 → 70% TLB Hit Rate (7 de 10 accesos ahorrados).
> Con paginas mas grandes → El Hit Rate Aumenta!!!
>
> TIEMPO ACCESOO PROMEDIO: T(hit) * Hit_Rate(%) + T(miss)* ( 1 - hit_rate )
> ej: tiempo del ejemplo de acceso: 101ns x 0,7 + 201ns x 0,3 = 131 ns

> [!warning] Posible error
> En los apuntes aparece la errata tipográfica "TIEMPO ACCESOO PROMEDIO" por TIEMPO DE ACCESO PROMEDIO.

![Arquitectura de TLB y flujo de aciertos y fallos](adjuntos/Arquitectura%20de%20TLB%20y%20flujo%20de%20aciertos%20y%20fallos.png)

> [!example]- Transcripción de la imagen
> Flujo de hardware en la MMU con TLB:
> 1. La CPU genera una dirección virtual con VPN y Offset.
> 2. Se consulta en paralelo el VPN en la TLB:
>    - **TLB Hit:** La traducción a PFN está presente. Se toma el PFN en $\sim 1\text{ ns}$ y se accede directamente a la RAM física. Total: 1 acceso a RAM.
>    - **TLB Miss:** La traducción no está en la TLB. Se consulta la Tabla de Páginas en memoria RAM (o hardware walker), se carga la traducción en la TLB y luego se accede al dato físico. Total: 2 accesos a RAM.

![Distribución de un arreglo en páginas virtuales](adjuntos/Distribuci%C3%B3n%20de%20un%20arreglo%20en%20p%C3%A1ginas%20virtuales.png)

> [!example]- Transcripción de la imagen
> Mapeo del arreglo de 10 enteros (4 bytes c/u) en páginas de 16 bytes:
> - **Página 0:** `sum` (bytes 0-3), `a[0]` (bytes 4-7), `a[1]` (bytes 8-11), `a[2]` (bytes 12-15).
> - **Página 1:** `a[3]` (bytes 16-19), `a[4]` (bytes 20-23), `a[5]` (bytes 24-27), `a[6]` (bytes 28-31).
> - **Página 2:** `a[7]` (bytes 32-35), `a[8]` (bytes 36-39), `a[9]` (bytes 40-43).

![Cálculo de tasa de aciertos de TLB en bucle secuencial](adjuntos/C%C3%A1lculo%20de%20tasa%20de%20aciertos%20de%20TLB%20en%20bucle%20secuencial.png)

> [!example]- Transcripción de la imagen
> Secuencia de aciertos y fallos:
> - `a[0]`: Miss (primer acceso a Página 0, carga en TLB).
> - `a[1]`, `a[2]`: Hit, Hit.
> - `a[3]`: Miss (primer acceso a Página 1, carga en TLB).
> - `a[4]`, `a[5]`, `a[6]`: Hit, Hit, Hit.
> - `a[7]`: Miss (primer acceso a Página 2, carga en TLB).
> - `a[8]`, `a[9]`: Hit, Hit.
> Total: 3 fallos (Misses) y 7 aciertos (Hits) en 10 referencias $\implies \text{Hit Rate} = 70\%$.

> [!tip] Complemento: EAT (Effective Access Time)
> Si el acceso a TLB toma $1\text{ ns}$ y el acceso a RAM toma $100\text{ ns}$:
> - $T_{\text{hit}} = 1\text{ ns} (\text{TLB}) + 100\text{ ns} (\text{RAM}) = 101\text{ ns}$.
> - $T_{\text{miss}} = 1\text{ ns} (\text{TLB}) + 100\text{ ns} (\text{Tabla}) + 100\text{ ns} (\text{Dato}) = 201\text{ ns}$.
> Con un $70\%$ de aciertos: $EAT = 101 \times 0.7 + 201 \times 0.3 = 131\text{ ns}$. Con tasas reales del $99\%$: $EAT = 101 \times 0.99 + 201 \times 0.01 = 102\text{ ns}$, casi idéntico al acceso directo sin paginación.

## Preguntas de repaso

> [!question]- ¿Qué ocurre a nivel de hardware cuando se produce un TLB Miss?
> La MMU (o una rutina de interrupción de software según la arquitectura) debe suspender la traducción rápida, consultar la tabla de páginas en memoria RAM física para obtener la PTE, actualizar una entrada de la TLB con el par VPN $\to$ PFN recién obtenido y reintentar la instrucción.

> [!question]- ¿Cómo se calcula el Tiempo de Acceso Efectivo (*Effective Access Time* - EAT)?
> Mediante la fórmula de esperanza matemática ponderada:
> $$EAT = \text{Hit Rate} \times T_{\text{hit}} + (1 - \text{Hit Rate}) \times T_{\text{miss}}$$
> donde $T_{\text{hit}}$ incluye la consulta a TLB más el acceso al dato en RAM, y $T_{\text{miss}}$ añade el acceso a la tabla de páginas.

> [!question]- ¿Por qué aumentar el tamaño de página incrementa directamente la tasa de aciertos (*Hit Rate*) de la TLB?
> Porque caben más variables consecutivas dentro de una misma página física. Por tanto, el primer acceso que causa un fallo amortiza su costo sobre una mayor cantidad de accesos subsiguientes antes de cruzar la frontera de página.

