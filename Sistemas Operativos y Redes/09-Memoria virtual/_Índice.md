# Memoria virtual — índice

Principios teóricos y políticas algorítmicas de la memoria virtual basada en paginación por demanda (*demand paging*). Análisis de la brecha de rendimiento entre memoria principal (RAM) y almacenamiento secundario de respaldo (*swap space*), y gestión de páginas anónimas frente a páginas respaldadas por archivos. Estudio comparativo de algoritmos clásicos y modernos de reemplazo de páginas: el algoritmo Óptimo de Bélády (OPT / MIN) como cota superior inalcanzable, la política First-In First-Out (FIFO) y la demostración matemática de la anomalía de Bélády. Fundamentación de Least Recently Used (LRU) a partir del principio de localidad temporal, análisis frente a diversas cargas de trabajo (*workloads* sin localidad, sesgados 80-20 y bucles secuenciales patológicos), e inasumibilidad de su implementación exacta en hardware. Soluciones prácticas en kernels de producción mediante el algoritmo del reloj (*Clock* / segunda oportunidad), técnicas de envejecimiento (*Aging*), priorización mediante el bit de modificación (*Dirty Bit*), y prevención del colapso del sistema por hiperpaginación (*Thrashing*) mediante el modelo de conjunto de trabajo (*Working Set*).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 9 de los apuntes originales de Sistemas Operativos, complementadas exhaustivamente con las diapositivas oficiales de `Contenido_6_Memoria.pdf` y la literatura estándar de sistemas operativos (Silberschatz et al., OSTEP, Tanenbaum).

## Orden de estudio

1. [[01 - Fundamentos de memoria virtual y espacio de intercambio (swap)|Fundamentos de memoria virtual y espacio de intercambio (swap)]]: concepto de memoria virtual, almacenamiento en disco como memoria extendida (*swap space*), penalización de latencia entre RAM y almacenamiento secundario, y justificación de las políticas de reemplazo.
2. [[02 - Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady|Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady]]: algoritmo óptimo de Belady (OPT/MIN) con conocimiento del futuro, política FIFO, y demostración de la anomalía de Belady donde añadir memoria física incrementa los fallos de página.
3. [[03 - Algoritmo LRU e implementaciones con hardware y software|Algoritmo LRU e implementaciones con hardware y software]]: aproximación heurística a OPT basada en localidad temporal, rendimiento bajo cargas aleatorias, sesgadas 80-20 y bucles secuenciales, y barreras de implementación práctica con marcas de tiempo o listas enlazadas.
4. [[04 - Algoritmo del reloj (Clock) y aproximaciones prácticas de LRU|Algoritmo del reloj (Clock) y aproximaciones prácticas de LRU]]: algoritmo del reloj (*Clock*) con bit de referencia ($R$), registros de envejecimiento (*Aging*), clasificación eficiente con bit sucio ($M$), caracterización de la hiperpaginación (*Thrashing*) y regulación por conjunto de trabajo (*Working Set*).

