---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/apuntes
prerrequisitos:
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
  - "[[01 - Niveles de planificación y ciclo de ráfagas CPU-IO]]"
---

# Swapping, fragmentación externa y algoritmos de asignación libre

Cuando la memoria física disponible es insuficiente para alojar todos los procesos activos, el sistema operativo recurre al almacenamiento secundario mediante intercambio (*swapping*). Este proceso continuo de entrada y salida genera huecos dispersos no contiguos en la RAM, dando origen al problema de la fragmentación externa.

## Swapping y gestión de particiones libres (mis apuntes)

> [!note] Apuntes de clase
> **SWAPPING:**
> - Espacio Swap: memoria secundaria que usaremos como memoria secundaria, si se acaba la principal usaremos la swap
> - Tendremos 2 operaciones:
>   - swap-out: Llevar la memoria de un proceso a la memoria secundaria (disco (memoria swap))
>   - swap-in: Llevarle memoria del programa de la memoria secundaria a la principal
> - El scheduler encargado de esto → MEDIUM-TERM Scheduler
>
> **SOLUCIONES A PROBLEMAS DE ESPACIOS LIBRES → Fragmentación Externa**
> Quedan espacios!!!
> Soluciones:
> - COMPACTACION: Juntar toda la memoria (Fusionar los huecos) → Es muy costoso, no es practico (necesito cambiar registros base y limit, por cada uno y no queremos hacer eso).
>   - Requiere copiar memoria a otras direcciones.
>   - Ventajas: Ninguna, es aleatorio.
> - First Fit: Encontrar el primer espacio que este disponible (donde quepa la memoria).
> - Intentar desperdiciar la menor cantidad de memoria posible.
> - Best Fit: El lugar donde cabe y que deja menos espacio (mas pequeño posible).
> - La gracia es que donde lo deje, haya mas probabilidad que caiga espacio para otro programa.
> - Worst Fit: El lugar que deja mas espacio libre (mas grande).

> [!warning] Posible error
> En los apuntes figura una redundancia textual: "memoria secundaria que usaremos como memoria secundaria". El espacio swap es una partición o archivo dedicado en el disco secundario para respaldar temporalmente procesos enteros o páginas de memoria. Asimismo, la frase "Ventajas: Ninguna, es aleatorio" refiere coloquialmente al costo elevado de la compactación.

![Mecanismo de swapping y generación de huecos de memoria](adjuntos/Mecanismo%20de%20swapping%20y%20generaci%C3%B3n%20de%20huecos%20de%20memoria.png)

> [!example]- Transcripción de la imagen
> Diagrama de intercambio (*swapping*):
> - La CPU ejecuta procesos en la memoria principal (RAM).
> - Cuando la memoria se satura, el planificador de mediano plazo (*medium-term scheduler*) expulsa un proceso inactivo mediante **swap-out** hacia el disco de respaldo (espacio swap).
> - Cuando el proceso vuelve a competir por la CPU, se realiza **swap-in** trayéndolo de regreso a la memoria principal.
> - A medida que distintos procesos entran y salen, la memoria física queda salpicada de huecos (*holes*) de tamaños desiguales.

![Compactación de memoria para fusionar huecos libres](adjuntos/Compactación%20de%20memoria%20para%20fusionar%20huecos%20libres.png)

> [!example]- Transcripción de la imagen
> Técnica de compactación de memoria:
> - Reubica todos los procesos activos hacia un extremo contiguo de la memoria física (hacia abajo).
> - Fusiona todos los huecos libres dispersos en un único bloque contiguo de gran tamaño.
> - Desventaja crítica: Incurre en un costo altísimo de I/O y CPU al tener que copiar megabytes o gigabytes enteros en RAM y reajustar los registros base de cada proceso relocalizado.

![Estrategias de colocación contigua First Fit y Best Fit](adjuntos/Estrategias%20de%20colocaci%C3%B3n%20contigua%20First%20Fit%20y%20Best%20Fit.png)

> [!example]- Transcripción de la imagen
> Comparación entre políticas de asignación contigua:
> - **First-Fit:** Recorre la lista de huecos libres y asigna el *primer* hueco cuyo tamaño sea suficiente. Es el algoritmo más veloz.
> - **Best-Fit:** Examina la lista completa y asigna el hueco que sea *más pequeño* entre los que satisfacen la solicitud, minimizando el remanente inmediato, aunque produce micro-huecos inutilizables.

![Estrategia Worst Fit y fragmentación externa](adjuntos/Estrategia%20Worst%20Fit%20y%20fragmentaci%C3%B3n%20externa.png)

> [!example]- Transcripción de la imagen
> Política Worst-Fit y fenómeno de fragmentación externa:
> - **Worst-Fit:** Asigna deliberadamente el hueco libre *más grande* disponible, bajo la premisa de que el espacio sobrante será lo bastante grande para albergar a un futuro proceso.
> - **Fragmentación externa:** Existe suficiente memoria total disponible en el sistema para satisfacer un requerimiento, pero se encuentra fragmentada en huecos dispersos no contiguos, impidiendo la asignación.

> [!tip] Complemento: Regla del 50%
> Los análisis empíricos y teóricos (como la regla del 50% de Knuth) demuestran que, independientemente de la política de asignación empleada (First-Fit o Best-Fit), por cada $N$ bloques asignados a procesos, aproximadamente $0.5 N$ bloques se pierden debido a la fragmentación externa, lo que motivó el abandono de la asignación puramente contigua en favor de esquemas no contiguos.

## Preguntas de repaso

> [!question]- ¿Qué planificador del sistema operativo coordina las operaciones de `swap-in` y `swap-out`?
> El planificador de mediano plazo (*Medium-Term Scheduler*), encargado de regular el grado de multiprogramación suspendiendo temporalmente procesos en disco cuando la memoria física se satura.

> [!question]- ¿En qué se diferencia la fragmentación externa de la fragmentación interna?
> La fragmentación externa ocurre cuando el total de memoria libre suma suficiente espacio pero está dividida en huecos no contiguos demasiado pequeños para albergar un proceso nuevo. La fragmentación interna ocurre cuando a un proceso se le asigna un bloque de tamaño fijo mayor al que realmente solicitó, desperdiciando espacio dentro del propio bloque.

> [!question]- ¿Por qué no se utiliza la compactación en sistemas operativos modernos?
> Porque requiere suspender la ejecución del sistema y copiar físicamente bloques masivos de memoria en tiempo de ejecución, lo que genera una latencia inaceptable. Los sistemas modernos eliminan este problema mediante paginación y segmentación, que no exigen contigüidad física.
