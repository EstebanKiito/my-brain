---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[01 - Hilos y procesos: el módulo threading]]"
  - "[[02 - Sincronización con join y ciclo de vida de hilos daemon]]"
---

# Concurrencia condiciones de carrera y locks

Dado que todos los hilos de un mismo proceso comparten el mismo espacio de memoria, pueden acceder y alterar las mismas variables simultáneamente. Sin una coordinación estricta, los accesos simultáneos a datos compartidos provocan inconsistencias severas conocidas como condiciones de carrera.

## Condiciones de carrera (race conditions)

Una **condición de carrera** (*race condition*) ocurre cuando dos o más hilos intentan leer y modificar un recurso compartido al mismo tiempo y el resultado final depende del orden no determinista en que el sistema operativo calendariza dichos hilos.

El bloque de código que accede o modifica el recurso compartido se denomina **sección crítica** (*critical section*). Una operación en apariencia sencilla como `contador += 1` no es atómica: Python debe (1) leer el valor actual, (2) sumar 1 y (3) escribir el nuevo valor. Si el sistema operativo suspende al hilo entre el paso 1 y el 3 para darle turno a otro hilo, las actualizaciones se solapan y se pierden datos.

## Exclusión mutua mediante threading.Lock

Para resolver las condiciones de carrera implementamos **exclusión mutua**: garantizar que **solo un hilo a la vez** pueda entrar a la sección crítica. La herramienta básica para lograrlo es **`threading.Lock`**.

Un cerrojo o cerrojo binario (*lock*) posee dos estados: **libre** (*unlocked*) y **adquirido** (*locked*). Cuando un hilo invoca `lock.acquire()`, si el lock está libre pasa a bloqueado y el hilo continúa; si ya estaba adquirido por otro hilo, el hilo entrante se suspende en espera hasta que el poseedor ejecute `lock.release()`.

![Exclusión mutua con Lock](adjuntos/Exclusi%C3%B3n%20mutua%20con%20Lock.png)

> [!example]- Transcripción de la imagen
> - Diagrama de exclusión mutua:
>   - El Hilo 1 adquiere el cerrojo (`acquire`) y accede en exclusiva a la sección crítica.
>   - El Hilo 2 intenta adquirir el cerrojo ocupado y queda bloqueado en espera.
>   - Al terminar, el Hilo 1 libera el cerrojo (`release`), permitiendo que el Hilo 2 se desbloquee y ejecute su sección crítica.

### Uso con context manager: with lock

Llamar manualmente a `acquire()` y `release()` es propenso a errores: si ocurre una excepción dentro de la sección crítica, `release()` podría no ejecutarse nunca, dejando a todos los demás hilos congelados. Por ello, la convención en Python es usar la sentencia **`with lock:`**:

```python
import threading

class CuentaBancaria:
    def __init__(self, saldo_inicial: int):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def depositar(self, monto: int):
        with self.lock:
            # Sección crítica protegida
            saldo_actual = self.saldo
            self.saldo = saldo_actual + monto

cuenta = CuentaBancaria(100)

def cliente():
    for _ in range(500):
        cuenta.depositar(1)

hilos = [threading.Thread(target=cliente) for _ in range(4)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

print(f"Saldo final garantizado: {cuenta.saldo}")
```

```
Saldo final garantizado: 2100
```

> [!warning] El lock debe ser compartido entre los hilos
> Si cada hilo crea su propia instancia independiente de `Lock()` (por ejemplo dentro de su método `run()`), cada uno cerrará su propio cerrojo privado y ninguno esperará a los demás. El cerrojo debe ser una **única instancia compartida** (como atributo del recurso compartido o argumento común).

> [!tip] Regla de oro para secciones críticas
> Mantén el código dentro de `with lock:` lo más breve posible. Ejecutar cálculos pesados, peticiones de red o llamadas de entrada/salida dentro del lock serializa innecesariamente a todos los hilos y anula el beneficio de la concurrencia.

## Preguntas de repaso

> [!question]- ¿Por qué la sentencia `x += 1` en Python puede generar una condición de carrera si no se usa un lock?
> Porque a nivel de bytecode no es una instrucción atómica; requiere leer el valor, calcular la suma y almacenarlo. Un cambio de contexto entre esas etapas hace que dos hilos lean el mismo valor inicial y uno sobreescriba al otro.

> [!question]- ¿Qué ventaja ofrece usar `with lock:` por sobre llamar a `lock.acquire()` y `lock.release()` manualmente?
> El bloque `with` implementa el protocolo de context manager y garantiza que `release()` se ejecute automáticamente al salir del bloque, incluso si se levanta una excepción no controlada dentro de la sección crítica.

> [!question]- ¿Qué sucede si dos hilos comparten una variable global pero cada uno crea su propio `lock = threading.Lock()` localmente?
> Ambos adquirirán su propio candado sin bloquearse mutuamente, lo que deja la variable compartida desprotegida y reproduce la condición de carrera.

> [!question]- ¿Cuál es la consecuencia de incluir operaciones lentas (como descargas de archivos) dentro de un bloque `with lock:`?
> Todos los demás hilos que necesiten acceder a ese lock quedarán suspendidos esperando, eliminando la concurrencia y degradando severamente el rendimiento general.
