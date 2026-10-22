---
ramo: "Programación Avanzada"
tema: "Threading"
tags:
  - programacion/concurrencia
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[01 - Repaso de Python: tipos, funciones y módulos]]"
  - "[[06 - Clases, objetos y variables de clase]]"
---

# Hilos y procesos: el módulo threading

Cuando un programa ejecuta una tarea lenta —como descargar un archivo pesado de internet o procesar un cálculo largo—, la ejecución secuencial habitual congela el resto de la aplicación. Para mantener la interfaz responsiva y realizar múltiples tareas en paralelo, recurrimos a los hilos de ejecución.

## Procesos vs Hilos (Threads)

En los sistemas operativos modernos existen dos unidades fundamentales de ejecución:

- **Proceso (*process*):** es una instancia independiente de un programa en ejecución. Posee su propio espacio de memoria virtual completamente aislado y sus propios recursos asignados por el sistema operativo. Si un proceso colapsa, no afecta directamente a otros procesos.
- **Hilo (*thread*):** es una línea de ejecución ligera que vive **dentro de un proceso**. Todos los hilos de un mismo proceso comparten el mismo espacio de memoria, las mismas variables globales y los mismos descriptores de archivos.

![Ejecución con hilos paralelos](adjuntos/Ejecuci%C3%B3n%20con%20hilos%20paralelos.png)

> [!example]- Transcripción de la imagen
> - Diagrama de ejecución en el tiempo:
>   - Arriba: ejecución secuencial monofilo donde la tarea 2 espera que la tarea 1 finalice por completo.
>   - Abajo: ejecución concurrente multihilo donde el hilo principal genera dos hilos secundarios que avanzan en paralelo en el tiempo.

## Creación de hilos con el módulo threading

En Python la concurrencia basada en hilos se implementa mediante el módulo estándar **`threading`**. Existen dos formas de crear un hilo:

### Forma 1: Pasando una función objetivo (target)

Es la forma más directa: se instancia la clase `Thread` indicando la función a ejecutar en el parámetro `target` y una tupla de argumentos en `args`:

```python
import threading
import time

def trabajador(nombre: str, duracion: float):
    print(f"[{nombre}] Iniciando labor...")
    time.sleep(duracion)
    print(f"[{nombre}] Labor completada.")

# Creación de hilos secundarios
t1 = threading.Thread(target=trabajador, args=("Hilo-1", 0.1))
t2 = threading.Thread(target=trabajador, args=("Hilo-2", 0.05))

t1.start()
t2.start()
```

```
[Hilo-1] Iniciando labor...
[Hilo-2] Iniciando labor...
[Hilo-2] Labor completada.
[Hilo-1] Labor completada.
```

### Forma 2: Heredando de threading.Thread

Para componentes con estado interno y lógica más compleja, se define una subclase de `Thread` y se sobrescribe el método **`run(self)`**:

```python
import threading
import time

class ContadorThread(threading.Thread):
    def __init__(self, nombre: str, limite: int):
        super().__init__()  # Obligatorio invocar al constructor base
        self.nombre = nombre
        self.limite = limite

    def run(self):
        """Lógica ejecutada al arrancar el hilo."""
        for i in range(1, self.limite + 1):
            time.sleep(0.02)
            print(f"[{self.nombre}] Cuenta: {i}")

c = ContadorThread("ContadorA", 3)
c.start()
```

```
[ContadorA] Cuenta: 1
[ContadorA] Cuenta: 2
[ContadorA] Cuenta: 3
```

> [!warning] La diferencia crucial entre start() y run()
> Para iniciar un hilo debes llamar siempre al método **`start()`**. Si llamas directamente a `run()`, Python ejecutará el código como una función normal en el **mismo hilo actual**, bloqueando la ejecución y perdiendo toda concurrencia. `start()` le solicita al sistema operativo crear el nuevo hilo e invocar a `run()` en él.

> [!tip] Identificar el hilo actual
> La función `threading.current_thread().name` retorna el nombre del hilo en el cual se está ejecutando la línea actual (por ejemplo `MainThread` para el hilo principal).

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia principal entre un proceso y un hilo en cuanto al manejo de memoria?
> Los procesos poseen espacios de memoria separados e independientes protegidos por el sistema operativo, mientras que los hilos residen dentro del mismo proceso y comparten el mismo espacio de memoria y variables.

> [!question]- ¿Qué ocurre si un programador ejecuta `mi_hilo.run()` en lugar de `mi_hilo.start()`?
> El método `run()` se ejecuta de forma síncrona y bloqueante dentro del hilo que hizo la llamada; no se crea ningún hilo nuevo en el sistema operativo y la concurrencia se pierde.

> [!question]- ¿Por qué es obligatorio llamar a `super().__init__()` al definir una subclase de `threading.Thread`?
> Porque la clase base `Thread` debe inicializar las estructuras internas de control del sistema operativo y los identificadores de hilo; omitirlo genera errores en el ciclo de vida del hilo.

> [!question]- ¿Cómo se entregan argumentos a la función objetivo en `Thread(target=f, args=...)`?
> Se deben entregar dentro de una tupla en el parámetro `args` (por ejemplo `args=("dato",)` con coma final si es un solo elemento).
