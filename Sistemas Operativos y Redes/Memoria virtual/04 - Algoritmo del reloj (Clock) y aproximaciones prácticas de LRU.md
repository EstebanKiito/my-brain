---
ramo: "Sistemas Operativos y Redes"
tema: "Memoria virtual"
tags:
  - so/memoria
  - so/memoria-virtual
  - origen/complemento
prerrequisitos:
  - "[[03 - Algoritmo LRU e implementaciones con hardware y software]]"
  - "[[02 - Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady]]"
---

# Algoritmo del reloj (Clock) y aproximaciones prácticas de LRU

Dado el costo intratable de mantener estructuras ordenadas exactas en cada ciclo de memoria, los sistemas operativos reales implementan aproximaciones eficientes de LRU utilizando el bit de referencia provisto por la MMU, destacando el **Algoritmo del Reloj** (*Clock* o *Second Chance*).

## El algoritmo del reloj y el bit de referencia

La MMU incluye en cada entrada de la tabla de páginas un **bit de referencia** ($R$). Cada vez que el procesador lee o escribe en una página, el hardware conmuta automáticamente $R = 1$ a costo cero.

> [!tip] Mecanismo del algoritmo del reloj
> Los marcos físicos se organizan en una lista circular con un puntero que avanza cíclicamente como la manecilla de un reloj:
> 1. Se examina la página apuntada por la manecilla.
> 2. Si $R = 1$: el proceso ha utilizado la página recientemente. El sistema le concede una **segunda oportunidad**, limpia el bit fijando $R = 0$, y avanza la manecilla al marco contiguo.
> 3. Si $R = 0$: la página no ha sido referenciada desde la última vuelta del reloj. Se selecciona como **página víctima** para ser desalojada al swap, y la manecilla avanza.

![Algoritmo del reloj Clock y bit de referencia](adjuntos/Algoritmo%20del%20reloj%20Clock%20y%20bit%20de%20referencia.png)

> [!example]- Transcripción de la imagen
> Diapositiva oficial del curso (`Contenido_6_Memoria.pdf`, p. 66):
> - Estructura circular con puntero horario.
> - Al momento de elegir víctima: si `reference bit == 1`, se resetea a 0 y pasa a la siguiente; si `reference bit == 0`, se elige inmediatamente esa página.
> - Aproxima el comportamiento de LRU con un costo de CPU despreciable.

## Variantes avanzadas: envejecimiento (*Aging*) y bit de modificación

### Registro de envejecimiento (*Aging*)
Para capturar una historia temporal más precisa que un único bit, el kernel asocia a cada marco un byte de historial (e.g. 8 bits). En cada interrupción periódica del reloj del sistema (*timer tick*), el contador se desplaza un bit a la derecha (`>> 1`) y el bit $R$ se inserta en el bit más significativo (MSB). La página con el menor valor entero es la menos recientemente accedida.

### Optimización con el bit modificado (*Dirty Bit*)
Las páginas que fueron modificadas en RAM (*dirty bit* $M = 1$) exigen escribirse a disco antes de desalojar el marco, mientras que las páginas limpias ($M = 0$) pueden descartarse instantáneamente porque su copia en disco o binario ya es idéntica. Se priorizan en 4 clases:
1. $(R=0, M=0)$: Mejor opción (no usada, limpia; desalojo inmediato sin I/O).
2. $(R=0, M=1)$: Segunda opción (no usada, sucia; requiere escritura a disco).
3. $(R=1, M=0)$: Usada recientemente, limpia.
4. $(R=1, M=1)$: Peor opción (usada recientemente y modificada).

## Hiperpaginación (*Thrashing*) y conjunto de trabajo

Cuando el grado de multiprogramación es excesivamente alto y la suma de las páginas activas de los procesos supera la memoria RAM física, se desencadena la **hiperpaginación** (*Thrashing*):

> [!warning] Hiperpaginación (*Thrashing*)
> Estado patológico en el cual los procesos pasan prácticamente el 100% del tiempo bloqueados esperando operaciones de E/S de disco para transferir páginas entre la RAM y el espacio swap, haciendo que la utilización útil de la CPU colapse a casi cero.

Para prevenir el thrashing, el sistema operativo monitorea el **Conjunto de Trabajo** (*Working Set*) de cada proceso (el conjunto de páginas referenciadas en una ventana de tiempo $\Delta$). Si la memoria física no puede albergar la suma de los working sets de todos los procesos activos, el planificador de mediano plazo debe suspender temporalmente procesos completos mediante *swap-out*, liberando marcos para que los restantes procesos progresen sin colapsar el canal de disco.

## Preguntas de repaso

> [!question]- ¿Qué ventaja presenta el algoritmo del reloj (*Clock*) frente a la implementación estricta de LRU?
> No requiere interceptar cada acceso a memoria ni actualizar costosas listas o marcas de tiempo. La marcación de uso la realiza el hardware en paralelo conmutando el bit $R$, y la búsqueda de víctima solo se ejecuta cuando ocurre un fallo de página mediante un recorrido circular simple.

> [!question]- ¿Por qué es preferible desalojar una página con estado $(R=0, M=0)$ antes que una con $(R=0, M=1)$?
> Porque la página con $M=0$ está limpia y su contenido en RAM es idéntico a la copia persistida en disco, permitiendo sobreescribir su marco de inmediato sin realizar ninguna operación de escritura en almacenamiento secundario.

> [!question]- ¿Cuál es la causa primaria del fenómeno de hiperpaginación (*Thrashing*) y cómo lo mitiga el kernel?
> La causa es la sobreasignación de memoria física cuando la suma de los conjuntos de trabajo (*working sets*) de todos los procesos supera la RAM disponible. El kernel lo mitiga reduciendo el grado de multiprogramación: suspende procesos enteros enviándolos temporalmente al swap hasta que la demanda de marcos vuelva a situarse dentro de la capacidad física del sistema.

