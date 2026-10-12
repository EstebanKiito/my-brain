---
ramo: "Sistemas Operativos y Redes"
tema: "Memoria virtual"
tags:
  - so/memoria
  - so/memoria-virtual
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady]]"
  - "[[03 - Localidad de referencia y gestión de TLB con ASID en cambios de contexto]]"
---

# Algoritmo LRU e implementaciones con hardware y software

El algoritmo **Least Recently Used (LRU)** aproxima el comportamiento del algoritmo óptimo basándose en el principio de localidad temporal: si el pasado reciente refleja fielmente el futuro próximo, la página que no ha sido utilizada durante el mayor tiempo es la candidata idónea para el reemplazo.

## Principio de funcionamiento y comparación con OPT y FIFO

> [!tip] Regla de LRU
> Desalojar la página que no ha sido referenciada durante el período de tiempo más largo en el pasado.

![Algoritmo de reemplazo Least Recently Used LRU](adjuntos/Algoritmo%20de%20reemplazo%20Least%20Recently%20Used%20LRU.png)

> [!example]- Transcripción de la imagen
> Diapositiva oficial del curso (`Contenido_6_Memoria.pdf`, p. 59):
> - Algoritmo LRU sobre la secuencia de referencias `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1` con 3 marcos.
> - Al momento de un fallo, se inspecciona el historial pasado para identificar la página menos recientemente leída o escrita.
> - LRU produce tasas de acierto muy cercanas a OPT (y muy superiores a FIFO), y pertenece a la familia de algoritmos de pila, garantizando inmunidad total frente a la anomalía de Bélády.

## Comportamiento bajo diferentes cargas de trabajo (workloads)

El rendimiento relativo de LRU depende estrictamente del patrón de acceso a la memoria:

1. **Carga sin localidad (aleatoria pura):** Ninguna política heurística puede predecir el comportamiento; LRU, FIFO y Random ofrecen rendimientos idénticos.
2. **Carga con distribución 80-20 (localidad típica):** El 80% de los accesos se concentra en el 20% de las páginas activas (*hot pages*). LRU retiene las páginas calientes en memoria física y descarta las frías (*cold pages*), logrando un rendimiento casi óptimo.
3. **Carga con bucle secuencial (*looping sequential*):** Un programa itera sobre $N+1$ páginas disponiendo únicamente de $N$ marcos (por ejemplo, un bucle de 50 páginas con 40 marcos). LRU y FIFO sufren su caso patológico más severo: en cada paso expulsan justamente la página que el bucle necesitará en la siguiente iteración, arrojando una **tasa de aciertos del 0%**. En este escenario extremo, una política puramente aleatoria (Random) resulta superior.

## El dilema de la implementación exacta de LRU

Implementar LRU exacto en software o hardware puro resulta prohibitivo:

- **Enfoque de marcas de tiempo (*Timestamps*):** El procesador incrementa un contador en cada ciclo y escribe el valor en la PTE en *cada* acceso a memoria. Al producirse un fallo, el sistema operativo debe examinar exhaustivamente todas las entradas para hallar el valor mínimo.
- **Enfoque de lista enlazada o pila (*Stack implementation*):** Mantiene una lista doblemente enlazada donde cada acceso a una página mueve su nodo al tope de la lista. Esto exigiría actualizar hasta 6 punteros en memoria en cada lectura o escritura de datos, degradando catastróficamente la velocidad del procesador.

Debido a esta sobrecarga masiva, los sistemas operativos comerciales no implementan LRU exacto, sino algoritmos aproximados de bajo costo asistidos por hardware.

## Preguntas de repaso

> [!question]- ¿Por qué el algoritmo LRU está matemáticamente exento de sufrir la anomalía de Bélády?
> Porque LRU es un algoritmo de pila (*stack algorithm*). El conjunto de las $N$ páginas más recientemente usadas en cualquier instante temporal está rigurosamente contenido dentro del conjunto de las $N+1$ páginas más recientemente usadas.

> [!question]- ¿Qué ocurre cuando un proceso ejecuta un bucle secuencial sobre un conjunto de páginas que supera la capacidad de marcos físicos disponibles?
> Se genera una falla cíclica sistemática donde cada página desalojada por LRU es requerida inmediatamente después en la siguiente iteración, provocando un fallo de página en cada acceso individual (tasa de aciertos del 0%).

> [!question]- ¿Por qué no es viable en la práctica mantener una lista enlazada exacta de LRU en memoria RAM?
> Porque requeriría interceptar cada instrucción de la CPU que lea o escriba en memoria para reorganizar punteros de la lista, lo que multiplicaría por diez la latencia de acceso a la RAM e inutilizaría el paralelismo de la caché de la CPU.

