---
ramo: "Sistemas Distribuidos"
tema: "Procesos e hilos en Python"
tags:
  - sd/procesos-e-hilos
  - python
  - origen/complemento
prerrequisitos:
  - "[[04 - Threads y su programación en Python]]"
---

# Mecanismos de sincronización entre threads

Como los threads comparten memoria, dos de ellos pueden modificar el mismo dato a la vez y dejarlo inconsistente. Para coordinar el acceso a recursos compartidos y garantizar la integridad de los datos existen cuatro mecanismos básicos: **locks**, **semáforos**, **eventos** y **join**. Python implementa todos en el módulo `threading`; se elige según el contexto.

## El problema: una condición de carrera

`saldo = saldo + 1` parece una sola operación, pero son tres (leer, sumar, escribir). Si dos threads leen el mismo valor antes de que el otro escriba, se pierde un depósito. En este experimento cuatro threads depositan 1000 veces cada uno, y `time.sleep(0)` fuerza el cambio de thread entre la lectura y la escritura:

```python
import threading, time

saldo = 0
lock = threading.Lock()

def depositar(n, usar_lock):
    global saldo
    for _ in range(n):
        if usar_lock:
            with lock:              # adquiere y libera aunque haya una excepción
                actual = saldo
                time.sleep(0)       # cede la CPU a otro thread
                saldo = actual + 1
        else:
            actual = saldo          # leer, sumar y escribir no es atómico
            time.sleep(0)
            saldo = actual + 1
```

Sin lock el saldo final fue 1048 (y 1238 en otra ejecución); con lock fue siempre 4000. Ver [[01 - Condiciones de carrera y el problema de la sección crítica|Condiciones de carrera]].

## Locks o mutex

Un **lock** (o **mutex**) deja pasar a **un solo thread a la vez**, que se vuelve **dueño** del lock. **Solo el dueño puede liberarlo**, y entonces otro thread que esperaba puede tomarlo.

> [!warning] Morir con el candado
> Si el thread dueño muere sin liberar el lock, los demás quedan esperando para siempre y los datos pueden quedar a medio modificar. Por eso en Python se usa `with lock:`, que libera el lock aunque ocurra una excepción.

## Semáforos

![Semáforo con cuatro threads y recursos compartidos](adjuntos/Sem%C3%A1foro%20con%20cuatro%20threads%20y%20recursos%20compartidos.png)

> [!example]- Transcripción de la imagen
> **Semáforos.** Más de un thread puede acceder y no existe un sistema de propiedad: cualquier thread puede manipular el semáforo, incluso uno que no solicitó acceso. Funciona con un contador: *wait* (la acción para entrar) lo disminuye y *release* lo aumenta; si el contador es 0, *wait* bloquea. En el diagrama, cuatro threads hacen *Wait or Release* sobre un semáforo que protege tres recursos compartidos.

A diferencia del lock, un **semáforo** permite **varios recursos** a la vez (el contador indica cuántos quedan) y **no tiene dueño**: cualquier thread puede hacer *release*. Eso le da más poder a un thread malicioso o con errores, que puede alterar el contador sin haber entrado.

```python
impresoras = threading.Semaphore(2)     # 2 recursos disponibles

def imprimir(i):
    with impresoras:                    # wait: contador - 1 (bloquea si es 0)
        ...                             # usa una impresora
                                        # release al salir: contador + 1
```

Con seis threads, nunca hubo más de 2 dentro a la vez. Ver [[06 - Semáforos de Dijkstra y tipos de semáforos|Semáforos de Dijkstra]].

## Eventos

![Evento que libera a los threads que esperan](adjuntos/Evento%20que%20libera%20a%20los%20threads%20que%20esperan.png)

> [!example]- Transcripción de la imagen
> Línea de tiempo: Thread 2 y Thread 3 llaman a `E.wait()` y quedan esperando (reloj de arena) mientras el evento vale `False`. Thread 1 sigue trabajando y, más adelante, llama a `E.set()`: el evento pasa a `True` y Thread 2 y Thread 3 continúan.

Un **evento** es una señal externa que un thread usa para **avisar** a los demás. Cualquier thread puede esperarlo (`wait()`) y cualquiera puede activarlo (`set()`).

```python
listo = threading.Event()               # parte en False

def esperar(nombre):
    listo.wait()                        # bloquea hasta que alguien haga set()
    print(nombre, "continúa")
```

## Join

![Join con y sin timeout](adjuntos/Join%20con%20y%20sin%20timeout.png)

> [!example]- Transcripción de la imagen
> Thread 1 llama a `T2.join()` y espera hasta que Thread 2 termina; luego llama a `T3.join(timeout=N)` y espera N segundos. Como Thread 3 no termina en ese plazo, Thread 1 deja de esperar y sigue; Thread 3 termina después por su cuenta.

**Join** hace que un thread espere a que **otro termine**, o un tiempo máximo con `timeout`. Cada `join` espera a un solo thread a la vez. Tras un `join` con timeout hay que revisar `is_alive()` para saber si el otro terminó o si solo se acabó el plazo.

| Mecanismo | Cuántos pasan | ¿Tiene dueño? | Uso típico |
|---|---|---|---|
| Lock | 1 | Sí | Proteger una sección crítica |
| Semáforo | $k$ (contador) | No | Limitar el uso de $k$ recursos |
| Evento | Todos al activarse | No | Avisar que algo ocurrió |
| Join | – | – | Esperar que otro thread termine |

## Preguntas de repaso

> [!question]- ¿Por qué un semáforo es más riesgoso que un lock ante un thread con errores?
> Porque no tiene dueño: cualquier thread puede hacer *release* aunque no haya entrado, y así aumentar el contador y dejar pasar a más threads de los permitidos. En un lock solo el dueño puede liberar.

> [!question]- ¿Qué diferencia hay entre esperar con un evento y con `join`?
> `join` espera a que un thread específico **termine**. Un evento espera a que **alguien** indique que ocurrió algo, aunque el thread que lo activa siga vivo.

> [!question]- Después de `t.join(timeout=1)`, ¿cómo se sabe si `t` terminó?
> Con `t.is_alive()`: `join` retorna igual cuando se cumple el plazo, así que no indica por sí solo si el thread terminó.
