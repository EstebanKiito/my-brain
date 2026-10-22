---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[01 - Hilos y procesos: el módulo threading]]"
---

# Sincronización con join y ciclo de vida de hilos daemon

Cuando lanzamos hilos secundarios, estos se ejecutan de manera asíncrona e independiente. Sin embargo, con frecuencia el hilo principal necesita esperar los resultados de dichos hilos antes de continuar, o requiere tareas de soporte en segundo plano que no impidan la salida del programa al cerrar.

## El método join: sincronización por espera

El método **`join()`** bloquea el hilo que lo invoca hasta que el hilo objetivo sobre el cual se llama haya finalizado su ejecución:

```python
import threading
import time

def calcular_subtotal(tienda: str, segundos: float) -> None:
    time.sleep(segundos)
    print(f"[{tienda}] Cálculo completado")

t1 = threading.Thread(target=calcular_subtotal, args=("Norte", 0.05))
t2 = threading.Thread(target=calcular_subtotal, args=("Sur", 0.02))

t1.start()
t2.start()

# MainThread espera a que ambos completen
t1.join()
t2.join()
print("[Principal] Ambos subtotales listos. Consolidando balance...")
```

```
[Sur] Cálculo completado
[Norte] Cálculo completado
[Principal] Ambos subtotales listos. Consolidando balance...
```

![Sincronización de hilos con join](adjuntos/Sincronizaci%C3%B3n%20de%20hilos%20con%20join.png)

> [!example]- Transcripción de la imagen
> - Diagrama temporal de sincronización:
>   - El hilo principal (`Main Thread`) lanza `T1` y `T2`.
>   - Al invocar `T1.join()`, el hilo principal suspende su ejecución esperando el fin de `T1`.
>   - Una vez terminado `T1`, se invoca `T2.join()`. Si `T2` ya completó, continúa de inmediato.

Es posible pasar un parámetro opcional `timeout` (por ejemplo `t1.join(timeout=2.0)`). Si el tiempo expira sin que el hilo termine, la ejecución continúa; el estado se puede consultar luego mediante `t1.is_alive()`.

> [!warning] La trampa de alternar start() y join() inmediatamente
> Si ejecutas `t1.start(); t1.join(); t2.start(); t2.join()`, el segundo hilo nunca arrancará hasta que el primero termine. Esto destruye toda concurrencia y convierte el programa en una ejecución estrictamente secuencial. Siempre inicia todos los hilos concurrentes primero con `.start()` y solo después espéralos con `.join()`.

## Hilos demonio (daemons) y terminación del programa

Por defecto, los hilos en Python son **no daemon** (*non-daemon*): el intérprete de Python espera a que todos ellos terminen antes de finalizar el proceso completo.

Un **hilo daemon** (*daemon thread*) es un hilo secundario de soporte (como un recolector de métricas o un monitor de red) que **no impide que el programa finalice**. En el instante en que todos los hilos no-daemon terminan, el proceso de Python finaliza inmediatamente, cortando de forma abrupta cualquier hilo daemon que siga en ejecución.

![Ciclo de vida de hilos daemon](adjuntos/Ciclo%20de%20vida%20de%20hilos%20daemon.png)

> [!example]- Transcripción de la imagen
> - Comparación de finalización:
>   - Hilo daemon: el programa termina en cuanto el hilo principal finaliza, interrumpiendo al daemon a mitad de camino.

![Ciclo de vida de hilos no daemon](adjuntos/Ciclo%20de%20vida%20de%20hilos%20no%20daemon.png)

> [!example]- Transcripción de la imagen
> - Hilo no daemon: el programa permanece vivo esperando a que el hilo secundario complete todo su trabajo antes de cerrar.

![Terminación abrupta de hilos daemon](adjuntos/Terminaci%C3%B3n%20abrupta%20de%20hilos%20daemon.png)

> [!example]- Transcripción de la imagen
> - Terminal de ejecución: se observa la interrupción abrupta de la impresión del hilo daemon al morir el hilo principal.

### Configuración de hilos daemon

Se configura pasando `daemon=True` al constructor o asignando `t.daemon = True` **antes** de llamar a `start()`:

```python
import threading
import time

def monitor_red():
    while True:
        time.sleep(0.5)
        print("Sondeando servidor...")

t = threading.Thread(target=monitor_red, daemon=True)
t.start()
print("Hilo principal terminando...")
```

```
Hilo principal terminando...
```

> [!tip] Regla de oro para hilos daemon
> Usa hilos daemon solo para tareas accesorias que puedan cortarse abruptamente sin corromper datos. Nunca uses un hilo daemon para guardar archivos en disco, transacciones de base de datos o liberar recursos críticos.

## Preguntas de repaso

> [!question]- ¿Qué problema ocurre si se llama a `t.daemon = True` después de haber llamado a `t.start()`?
> Python arroja una excepción `RuntimeError`, porque el tipo de hilo debe quedar fijado ante el sistema operativo antes de su inicialización activa.

> [!question]- ¿Por qué no se debe usar un hilo daemon para escribir un archivo de registro en disco?
> Porque al terminar los hilos no daemon el proceso finaliza de inmediato, cortando el hilo daemon a mitad de una escritura y dejando el archivo corrupto o incompleto.

> [!question]- ¿Qué diferencia existe entre llamar a `join()` sin argumentos versus `join(timeout=1.5)`?
> Sin argumentos, la llamada es indefinidamente bloqueante hasta que el hilo termine; con `timeout`, el hilo invocador se desbloquea tras ese número de segundos aunque el hilo continúe activo.

> [!question]- ¿Cuál es la diferencia entre el comportamiento de un hilo normal y uno daemon al finalizar el hilo principal?
> El hilo normal mantiene el programa Python vivo hasta que termine su función objetivo; el hilo daemon es terminado abruptamente por el intérprete en el instante en que no quedan hilos normales activos.

