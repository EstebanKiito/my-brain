---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[03 - Concurrencia condiciones de carrera y locks]]"
  - "[[04 - Colas FIFO y deques de doble extremo]]"
---

# Colas sincronizadas y el patrón productor-consumidor

En sistemas concurrentes reales, desacoplar los componentes que generan información de aquellos que la procesan es esencial para mantener la estabilidad del sistema. El patrón productor-consumidor modela esta interacción utilizando colas de mensajes sincronizadas y seguras ante concurrencia.

## El patrón productor-consumidor

El patrón **productor-consumidor** (*producer-consumer*) separa dos roles complementarios:

- **Productores (*producers*):** generan datos (por ejemplo capturar paquetes de red o solicitudes web) y los depositan en un búfer de almacenamiento compartido.
- **Consumidores (*consumers*):** extraen los elementos del búfer y ejecutan el procesamiento correspondiente a su propio ritmo.

Si implementamos el búfer usando una estructura de datos estándar (como `collections.deque`), debemos proteger cada inserción y extracción con un cerrojo manual (`Lock`):

![Estructura deque protegida con Lock](adjuntos/Estructura%20deque%20protegida%20con%20Lock.png)

> [!example]- Transcripción de la imagen
> - Diagrama de arquitectura con deque y Lock:
>   - Múltiples hilos productores y consumidores compiten por acceder a un `deque` central protegido mediante un `Lock` explícito.
>   - Si el deque está vacío, el consumidor debe liberar el cerrojo, esperar un instante y volver a consultar, provocando sondeo repetitivo.

El gran inconveniente del enfoque manual es la **espera activa** (*busy waiting*): el consumidor despierta continuamente a verificar si la cola tiene elementos, desperdiciando ciclos de CPU.

## Colas seguras para hilos: el módulo queue

Python resuelve este problema de manera nativa con la clase **`queue.Queue`**, una cola FIFO (*First In, First Out*) diseñada específicamente para ser compartida entre múltiples hilos (**thread-safe**). `Queue` incluye internamente todos los cerrojos y variables de condición necesarios:

- **`put(item)`:** inserta un elemento. Si la cola tiene capacidad máxima definida y está llena, bloquea al productor eficientemente hasta que se libere espacio.
- **`get()`:** extrae y retorna un elemento. **Si la cola está vacía, suspende automáticamente al hilo consumidor** hasta que un productor inserte un elemento, sin gastar CPU.
- **`task_done()`:** avisa que el elemento recién extraído terminó de procesarse.
- **`join()`:** bloquea hasta que todos los elementos encolados hayan sido procesados (es decir, cuando cada `get()` tuvo su respectivo `task_done()`).

![Cola sincronizada thread-safe con queue](adjuntos/Cola%20sincronizada%20thread-safe%20con%20queue.png)

> [!example]- Transcripción de la imagen
> - Arquitectura con `queue.Queue`:
>   - El búfer gestiona internamente la sincronización y la suspensión de hilos.
>   - Los hilos interactúan mediante `put()` y `get()` de forma directa y atómica.

```python
import threading
import queue
import time

cola_pedidos = queue.Queue()

def cocinero():
    for plato in ["Pizza", "Pasta", "Ensalada"]:
        time.sleep(0.02)
        cola_pedidos.put(plato)
        print(f"[Cocinero] Preparó: {plato}")

def mesero():
    for _ in range(3):
        # Bloquea eficientemente hasta que haya un plato disponible
        plato = cola_pedidos.get()
        print(f"[Mesero] Entregando a mesa: {plato}")
        cola_pedidos.task_done()

t_cocina = threading.Thread(target=cocinero)
t_mesero = threading.Thread(target=mesero)

t_mesero.start()
t_cocina.start()

t_cocina.join()
t_mesero.join()
```

```
[Cocinero] Preparó: Pizza
[Mesero] Entregando a mesa: Pizza
[Cocinero] Preparó: Pasta
[Mesero] Entregando a mesa: Pasta
[Cocinero] Preparó: Ensalada
[Mesero] Entregando a mesa: Ensalada
```

## Temporizadores con threading.Timer

La clase **`threading.Timer`** es una subclase especializada de `Thread` que ejecuta una acción únicamente tras haber transcurrido un intervalo de tiempo especificado:

```python
import threading

def alarma(mensaje: str):
    print(f"[Alarma] Recordatorio: {mensaje}")

# Ejecuta alarma luego de 0.05 segundos
temporizador = threading.Timer(0.05, alarma, args=("Revisar horno",))
temporizador.start()
temporizador.join()
```

```
[Alarma] Recordatorio: Revisar horno
```

Si antes de que expire el tiempo se invoca **`temporizador.cancel()`**, el temporizador se desactiva y la función objetivo no llegará a ejecutarse jamás.

> [!tip] Prefiere queue.Queue sobre listas o deques con locks
> `queue.Queue` encapsula la sincronización y la suspensión de hilos en llamadas atómicas limpias. Siempre que comuniques datos entre hilos de trabajo, úsala en lugar de inventar estructuras manuales con cerrojos.

## Preguntas de repaso

> [!question]- ¿Por qué `queue.Queue.get()` es superior a inspeccionar continuamente el tamaño de una lista en un bucle?
> Porque suspende el hilo consumidor en el sistema operativo hasta que llegue un nuevo dato, eliminando por completo el consumo innecesario de procesador por espera activa (*busy waiting*).

> [!question]- ¿Cuál es la función del método `task_done()` y cómo se relaciona con `cola.join()`?
> `task_done()` notifica a la cola que un elemento extraído con `get()` ya fue completamente procesado. `cola.join()` bloquea la ejecución hasta que cada elemento insertado haya recibido su `task_done()`.

> [!question]- ¿Qué ocurre si un hilo productor intenta ejecutar `cola.put(item)` en una cola con `maxsize=5` que ya tiene 5 elementos?
> El hilo productor se suspende de forma bloqueante hasta que un consumidor retire un elemento mediante `get()` y libere espacio.

> [!question]- ¿Qué utilidad práctica ofrece el método `cancel()` de la clase `threading.Timer`?
> Permite abortar la ejecución de una tarea diferida si el suceso detonante fue resuelto o anulado antes de que transcurriera el tiempo de espera programado.

