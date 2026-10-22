---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[03 - Concurrencia condiciones de carrera y locks]]"
---

# Deadlocks y coordinación de hilos con Event

El uso de múltiples cerrojos para evitar condiciones de carrera introduce un nuevo peligro: el bloqueo mutuo entre hilos. Además de proteger recursos con cerrojos, los programas concurrentes necesitan mecanismos para enviarse señales de aviso y coordinar etapas de ejecución sin incurrir en esperas activas ineficientes.

## Interbloqueo o abrazo mortal (deadlock)

Un **interbloqueo** o **abrazo mortal** (*deadlock*) se produce cuando dos o más hilos quedan permanentemente bloqueados porque cada uno retiene un recurso que el otro necesita para continuar:

1. El Hilo A adquiere el Cerrojo 1 y solicita el Cerrojo 2.
2. Simultáneamente, el Hilo B adquiere el Cerrojo 2 y solicita el Cerrojo 1.
3. Ninguno de los dos puede avanzar ni liberar su propio cerrojo: el programa queda congelado indefinidamente.

![Condición de interbloqueo o abrazo mortal](adjuntos/Condici%C3%B3n%20de%20interbloqueo%20o%20abrazo%20mortal.png)

> [!example]- Transcripción de la imagen
> - Diagrama de interbloqueo circular:
>   - El Hilo A tiene asignado el Recurso 1 y solicita el Recurso 2.
>   - El Hilo B tiene asignado el Recurso 2 y solicita el Recurso 1.
>   - Se forma un ciclo cerrado de dependencias sin posibilidad de escape.

![Analogía de tráfico vehicular para deadlock](adjuntos/Analog%C3%ADa%20de%20tr%C3%A1fico%20vehicular%20para%20deadlock.jpg)

> [!example]- Transcripción de la imagen
> - Fotografía de congestión urbana en cruz: cuatro vehículos ingresan simultáneamente a una intersección bloqueando cada uno el avance del siguiente en sentido circular.

### Prevención de deadlocks

Para que ocurra un deadlock deben cumplirse cuatro condiciones simultáneas (condiciones de Coffman): exclusión mutua, retención y espera, no apropiación y **espera circular**. La estrategia más efectiva para prevenirlos consiste en **romper la espera circular**:

- **Orden global de adquisición:** todos los hilos del sistema deben solicitar los cerrojos siempre en la misma secuencia estricta (por ejemplo primero Cerrojo A y luego Cerrojo B).
- **Adquisición con tiempo límite:** invocar `lock.acquire(timeout=2.0)` y liberar los cerrojos ya retenidos si no se logra adquirir el siguiente en el tiempo previsto.

## Señalización y coordinación con threading.Event

Cuando un hilo debe esperar a que ocurra un suceso específico antes de proceder (por ejemplo, que otro hilo termine de descargar o inicializar un archivo), usar un bucle `while not listo: time.sleep(0.1)` es ineficiente y tosco. La clase **`threading.Event`** proporciona una señal thread-safe basada en una bandera interna (*flag*):

- **`set()`:** activa la bandera interna (`True`) y despierta a todos los hilos suspendidos en `wait()`.
- **`clear()`:** desactiva la bandera interna (`False`).
- **`wait(timeout=None)`:** bloquea el hilo hasta que la bandera esté en `True`. Retorna `True` si se activó el evento o `False` si expiró el tiempo de espera.
- **`is_set()`:** consulta si la bandera está activa.

![Coordinación entre hilos mediante Event](adjuntos/Coordinaci%C3%B3n%20entre%20hilos%20mediante%20Event.png)

> [!example]- Transcripción de la imagen
> - Diagrama de coordinación mediante Event:
>   - Un hilo trabajador espera suspendido en `event.wait()`.
>   - Otro hilo finaliza su labor previa e invoca `event.set()`.
>   - El evento notifica al hilo suspendido, permitiéndole continuar su ejecución.

```python
import threading
import time

evento_datos_listos = threading.Event()

def cargador():
    print("[Cargador] Leyendo archivo pesado...")
    time.sleep(0.05)
    print("[Cargador] Datos listos en memoria. Emitiendo señal...")
    evento_datos_listos.set()

def procesador():
    print("[Procesador] Esperando señal de datos...")
    evento_datos_listos.wait()  # Espera eficiente sin consumir CPU
    print("[Procesador] Señal recibida. Procesando datos...")

t_carga = threading.Thread(target=cargador)
t_proc = threading.Thread(target=procesador)

t_proc.start()
t_carga.start()

t_proc.join()
t_carga.join()
```

```
[Procesador] Esperando señal de datos...
[Cargador] Leyendo archivo pesado...
[Cargador] Datos listos en memoria. Emitiendo señal...
[Procesador] Señal recibida. Procesando datos...
```

> [!tip] Event frente a Lock
> Usa un **`Lock`** cuando quieras asegurar que **solo un hilo ejecute código exclusivo**, y usa un **`Event`** cuando un hilo deba **notificar a otro** que una condición o etapa ya se cumplió.

## Preguntas de repaso

> [!question]- ¿Por qué establecer un orden global y uniforme de adquisición de cerrojos previene los deadlocks?
> Porque elimina la posibilidad de que se forme una cadena de espera circular: ningún hilo podrá retener un recurso de orden mayor mientras espera por uno de orden menor.

> [!question]- ¿Qué ocurre internamente cuando un hilo invoca `evento.wait()` si la bandera interna ya está en `True`?
> No se suspende; la llamada retorna de inmediato permitiendo al hilo continuar sin bloqueo.

> [!question]- ¿En qué se diferencia el método `clear()` del método `set()` en una instancia de `Event`?
> `set()` conmuta la bandera a `True` despertando a los hilos en espera, mientras que `clear()` restablece la bandera a `False` para obligar a futuros hilos a esperar de nuevo.

> [!question]- ¿Por qué `evento.wait()` es superior a un bucle `while not bandera: time.sleep(0.1)`?
> Porque `wait()` pone al hilo en estado de suspensión gestionado por el sistema operativo, liberando por completo el procesador y despertando en el instante exacto en que se emite la señal.

