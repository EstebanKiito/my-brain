---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[01 - Hilos y procesos: el módulo threading]]"
  - "[[03 - Concurrencia condiciones de carrera y locks]]"
---

# El GIL de Python: concurrencia IO-bound frente a CPU-bound

Muchos programadores asumen que lanzar diez hilos en una máquina de diez núcleos acelerará cualquier cálculo diez veces. En Python (específicamente en CPython, la implementación estándar), esto no ocurre debido al Cerrojo Global del Intérprete o GIL.

## El GIL (Global Interpreter Lock)

El **GIL** (*Global Interpreter Lock*) es un cerrojo a nivel de intérprete que impide que más de un hilo ejecute instrucciones de *bytecode* de Python al mismo tiempo, sin importar cuántos núcleos físicos posea el procesador.

El GIL existe por una razón de diseño histórica: la gestión de memoria interna de CPython se basa en el **conteo de referencias** (*reference counting*). Para evitar condiciones de carrera catastróficas al incrementar o decrementar referencias de objetos compartidos, CPython protege todas las estructuras internas con este candado maestro.

## Concurrencia frente a paralelismo

Es fundamental distinguir dos conceptos clave:

- **Concurrencia (*concurrency*):** gestionar múltiples tareas que progresan de forma intercalada en el tiempo (ilusión de simultaneidad mediante cambios rápidos de turno).
- **Paralelismo (*parallelism*):** ejecutar físicamente múltiples tareas en el **mismo instante** exacto sobre distintos núcleos físicos.

En Python, el módulo `threading` ofrece **concurrencia**, pero no paralelismo de cálculo en código Python puro.

## Tareas I/O-bound frente a CPU-bound

El impacto práctico del GIL depende enteramente de la naturaleza de la tarea:

### 1. Tareas limitadas por Entrada/Salida (I/O-bound)
Pasan la mayor parte del tiempo esperando respuestas externas: peticiones HTTP en la red, lecturas de disco o consultas a bases de datos. Cuando un hilo ejecuta una operación de I/O o duerme con `time.sleep()`, **CPython libera el GIL automáticamente**, permitiendo que otros hilos utilicen la CPU mientras tanto.

> En tareas I/O-bound, `threading` es **altamente eficiente** y reduce drásticamente el tiempo total de respuesta.

```python
import threading
import time

def peticion_simulada(sitio: str):
    # Durante sleep/I-O, el GIL se libera
    time.sleep(0.04)
    print(f"Descargado: {sitio}")

sitios = ["sitioA.cl", "sitioB.cl", "sitioC.cl"]
hilos = [threading.Thread(target=peticion_simulada, args=(s,)) for s in sitios]

for h in hilos:
    h.start()
for h in hilos:
    h.join()
```

```
Descargado: sitioA.cl
Descargado: sitioB.cl
Descargado: sitioC.cl
```

### 2. Tareas limitadas por Procesador (CPU-bound)
Consisten en cálculos matemáticos continuos en bucles de Python sin pausas de I/O. Los hilos compiten ferozmente por el GIL; la sobrecarga por cambios de contexto (*context switching*) hace que la versión multihilo sea **incluso más lenta** que la versión secuencial con un solo hilo.

```
+--------------------+-----------------------+-----------------------+
| Criterio           | threading (Hilos)     | multiprocessing       |
+--------------------+-----------------------+-----------------------+
| Espacio de memoria | Compartido            | Aislado por proceso   |
| Afectado por GIL   | Sí (1 solo núcleo)    | No (1 núcleo c/u)     |
| Ideal para         | Tareas I/O-bound      | Tareas CPU-bound      |
| Costo de creación  | Ligero                | Más pesado            |
| Comunicación       | Variables / queue     | IPC / Pipes / Queues  |
+--------------------+-----------------------+-----------------------+
```

> [!warning] La ilusión de paralelizar bucles pesados con threading
> Nunca utilices `threading.Thread` para acelerar cálculos algebraicos pesados o procesamiento masivo de datos en Python. Para aprovechar todos los núcleos de CPU en tareas CPU-bound, utiliza el módulo **`multiprocessing`**, que genera procesos del sistema operativo independientes, cada uno con su propio intérprete y su propio GIL.

> [!tip] Regla de decisión rápida
> Si tu programa espera al exterior (red, disco, usuario) $\rightarrow$ usa **`threading`** o `asyncio`. Si tu programa hace trabajar al procesador al 100% calculando números $\rightarrow$ usa **`multiprocessing`**.

## Preguntas de repaso

> [!question]- ¿Por qué CPython implementó el GIL en lugar de proteger cada objeto con un candado individual?
> Porque un único cerrojo global simplificó enormemente la integración con librerías nativas en C y ofreció un rendimiento de ejecución monofilo mucho más rápido que gestionar millones de micro-candados por objeto.

> [!question]- ¿Por qué un programa multihilo para descargar 50 páginas web sí experimenta una gran mejora de velocidad a pesar del GIL?
> Porque al realizar llamadas de red (I/O) el hilo se bloquea esperando los paquetes y libera voluntariamente el GIL, permitiendo que los otros 49 hilos inicien sus descargas en paralelo.

> [!question]- ¿Qué ocurre si ejecutamos un bucle de cálculo pesado con dos hilos en una máquina con 8 núcleos?
> Solo un núcleo ejecutará instrucciones a la vez debido al GIL. Los dos hilos alternarán su turno en el mismo cerrojo, resultando en un tiempo de ejecución igual o ligeramente mayor que sin hilos.

> [!question]- ¿Cómo logra el módulo `multiprocessing` sortear la limitación del GIL para tareas CPU-bound?
> Crea procesos del sistema operativo independientes en lugar de hilos. Cada proceso posee su propia instancia aislada del intérprete de Python y su propio GIL, ejecutándose de forma verdaderamente paralela en núcleos físicos separados.
