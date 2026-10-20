---
ramo: "Sistemas Distribuidos"
tema: "Procesos e hilos en Python"
tags:
  - sd/procesos-e-hilos
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - Procesos y comunicación entre procesos]]"
---

# Threads y su programación en Python

Crear un proceso por cada tarea es caro y obliga a comunicarse por mensajes. Un **thread** es la alternativa liviana: vive dentro de un proceso y comparte todo con sus hermanos. Esa misma ventaja es su mayor riesgo, porque un thread que se equivoca puede dañar a todos los demás.

## Qué es un thread

Un **thread** (hilo) es un **proceso ligero**: un subproceso pequeño que el sistema operativo puede ejecutar y que se crea **dentro** de un proceso. Todos los threads de un proceso comparten su memoria, su espacio de direcciones y sus recursos, lo que facilita que se comuniquen.

## Ventaja y riesgo

- **Más liviano de crear:** no hay que asignar un nuevo espacio de direcciones ni configurar todos los recursos, como sí ocurre con un proceso.
- **Falla compartida:** si un thread falla, puede afectar a los demás o a todo el proceso. Por ejemplo, puede:
  - borrar una lista que todos usan,
  - modificar mal un valor compartido,
  - levantar una excepción que detiene el proceso.

> [!tip] El intercambio central
> Los procesos están **aislados pero son caros**; los threads son **baratos pero comparten el destino**. Al compartir memoria, los threads necesitan mecanismos de sincronización.

## Crear threads en Python

La forma directa es `threading.Thread` con una función objetivo. Los argumentos se pasan por posición (`args`) o por nombre (`kwargs`), y `name` le da un nombre al thread.

![Crear threads con threading.Thread](adjuntos/Crear%20threads%20con%20threading.Thread.png)

> [!example]- Transcripción de la imagen
> ```python
> import threading
>
> def presentar(personaje: str, edad: int):
>     nombre_thread = threading.current_thread().name
>     print("Thread:", nombre_thread)
>     print("Personaje:", personaje)
>     print("Edad:", edad)
>
>
> t1 = threading.Thread(target=presentar, name="Boby Jackson",
>                       args=("Shinichi Kudo", 17))
>
> t2 = threading.Thread(target=presentar, name="Carlos Guzman",
>                       kwargs={"personaje": "Kogoro Mouri", "edad": 38})
> t1.start()
> t2.start()
> ```

La otra forma es **heredar** de `threading.Thread` y sobrescribir `run`, que es lo que ejecuta `start()`:

![Thread como subclase de threading.Thread](adjuntos/Thread%20como%20subclase%20de%20threading.Thread.png)

> [!example]- Transcripción de la imagen
> ```python
> import threading
>
> class Presentador(threading.Thread):
>     def __init__(self, nombre_thread: str, personaje: str, edad: int):
>         super().__init__(name=nombre_thread)
>         self.personaje = personaje
>         self.edad = edad
>
>     def run(self):
>         print("Thread:", threading.current_thread().name)
>         print("Personaje:", self.personaje)
>         print("Edad:", self.edad)
>
> Presentador("Boby Jackson", "Shinichi Kudo", 17).start()
> Presentador("Carlos Guzman", "Kogoro Mouri", 38).start()
> ```

> [!warning] `start()` y no `run()`
> Llamar a `run()` directamente ejecuta el código en el thread actual, sin crear uno nuevo. Solo `start()` lanza el thread.

## Árbol de threads

Un thread puede crear otros, y estos a su vez más, formando un **árbol de threads**. En el ejemplo, cada `Presentador` lanza un thread que muestra la edad después de un segundo:

![Thread que crea otro thread](adjuntos/Thread%20que%20crea%20otro%20thread.png)

> [!example]- Transcripción de la imagen
> ```python
> import threading, time
>
> class Presentador(threading.Thread):
>     def __init__(self, nombre_thread: str, personaje: str, edad: int):
>         super().__init__(name=nombre_thread)
>         self.personaje = personaje
>         self.edad = edad
>
>     def mostrar_edad(self):
>         time.sleep(1)
>         print("Edad:", self.edad)
>
>     def run(self):
>         print("Thread:", threading.current_thread().name)
>         threading.Thread(target=self.mostrar_edad).start()
>         print("Personaje:", self.personaje)
>
> Presentador("Boby Jackson", "Shinichi Kudo", 17).start()
> Presentador("Carlos Guzman", "Kogoro Mouri", 38).start()
> ```

Una ejecución posible muestra que el orden **no está garantizado** entre threads, y que las edades llegan al final por el `sleep`:

```text
Thread: Boby Jackson
Thread: Carlos Guzman
Personaje: Kogoro Mouri
Personaje: Shinichi Kudo
Edad: 17
Edad: 38
```

La versión en C con POSIX threads está en [[02 - Programación con POSIX Threads y ciclo de vida|Programación con POSIX Threads]].

## Preguntas de repaso

> [!question]- ¿Por qué crear un thread es más barato que crear un proceso?
> Porque el thread usa el espacio de direcciones y los recursos del proceso que lo crea; no hay que reservar memoria nueva ni configurar recursos propios.

> [!question]- En el árbol de threads, ¿por qué "Personaje" se imprime antes que "Edad"?
> Porque `run` lanza `mostrar_edad` en otro thread y sigue de inmediato con su `print`. El thread nuevo duerme un segundo antes de imprimir la edad.

> [!question]- ¿Qué afirmación es correcta: "los threads siempre son más eficientes porque trabajan en paralelo" o "los threads son más livianos de crear porque comparten el espacio de memoria del proceso que los creó"?
> La segunda. La primera es falsa: los threads no siempre corren en paralelo (dependen de los núcleos y, en Python, del GIL), y compartir memoria trae costos de sincronización.
