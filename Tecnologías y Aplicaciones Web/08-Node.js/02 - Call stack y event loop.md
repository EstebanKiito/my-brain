---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Node.js"
tags:
  - web
  - nodejs
  - event-loop
  - asincronia
  - origen/complemento
prerrequisitos:
  - "[[01 - Node.js como runtime de JavaScript]]"
  - "[[03 - Pilas y colas]]"
---

# Call stack y event loop

JavaScript ejecuta **una sola línea a la vez**, y sin embargo un servidor en Node atiende miles de requests sin quedarse congelado. La explicación está en dos estructuras y un ciclo: la **pila de llamadas** (*call stack*), la **cola de mensajes** y el **event loop** que las conecta. Entenderlas explica por qué `setTimeout(f, 0)` no se ejecuta de inmediato y por qué un cálculo pesado bloquea todo el servidor.

## CPU frente a I/O, bloqueante frente a no bloqueante

- **I/O**: transferir datos desde o hacia el computador (leer archivos, red). **CPU**: calcular valores.
- **Bloqueante** (*blocking*): la operación detiene la ejecución de las demás hasta que termina. **No bloqueante** (*non-blocking*): no detiene la ejecución del código.

Node.js es **lento en operaciones de CPU** (corre en un solo hilo) pero **muy bueno en I/O**, que maneja de forma no bloqueante sin extras.

## Call stack: código bloqueante

JavaScript es *single-threaded*: ejecuta una pieza de código a la vez, línea por línea. Para saber dónde va usa una **pila** (LIFO):

```javascript
function ejemplo() {
  console.log('Hello');
  for (let i = 0; i < 2 * 1000000000; i += 1) {
    // ...
  }
  console.log('Bye');
}
ejemplo();
```

1. Se apila `main()`, que representa la ejecución del archivo completo.
2. Se llama a `ejemplo()` y se apila sobre `main()`.
3. Se apila `console.log('Hello')`; al terminar, se desapila.
4. El `for` corre dentro de `ejemplo()`. Mientras dura, **nada más puede ejecutarse**.
5. Se apila y desapila `console.log('Bye')`, luego se desapila `ejemplo()` y por último `main()`.

## Código no bloqueante y la cola

¿Qué pasa con una operación que no se sabe cuánto va a tardar?

```javascript
setTimeout(() => {
  console.log('Pasaron 3 segundos');
}, 3000);
```

1. Se apilan `main()` y `setTimeout()`.
2. `setTimeout` solo **registra** el temporizador en un componente externo (el runtime) y termina de inmediato: se desapila.
3. `main()` termina y la pila queda vacía. Durante 3 segundos no se ejecuta ninguna línea de JavaScript.
4. Cuando el temporizador vence, el componente externo pone el **callback** en la cola. Como la pila está vacía, el callback pasa a la pila, llama a `console.log` y luego se desapila.

## Event loop

![Call stack, cola de mensajes y event loop](adjuntos/Call%20stack%2C%20cola%20de%20mensajes%20y%20event%20loop.png)

> [!example]- Transcripción de la imagen
> Tres cajas: *Call stack* (con `main()`), *External* (con un `timeout`) y *Message queue* (con `callback()`). Unas flechas circulares (el event loop) mueven elementos de la cola a la pila. Los pasos:
> 1. Las llamadas asíncronas las manejan **componentes externos**.
> 2. Los componentes externos **agregan llamadas a una cola**.
> 3. El hilo principal **continúa ejecutando código**.
> 4. **Cuando se vacía el call stack**, se toman elementos de la cola y se ejecutan.
> 5. La ejecución es en el **orden en que fueron encolados**.

```javascript
console.log('A');
setTimeout(() => console.log('C'), 0);
console.log('B');
// A, B, C: aunque el plazo sea 0, el callback espera a que la pila se vacíe
```

## El modelo de Node.js

Node usa una arquitectura *single-threaded with event loop*, inspirada en el modelo de eventos del navegador. Solo una línea de JavaScript se ejecuta en cada momento: V8 es síncrono. Libuv mantiene hilos adicionales que esperan el resultado de las operaciones de I/O que sí son bloqueantes, y avisa al event loop cuando terminan.

![Event loop de Node.js con libuv](adjuntos/Event%20loop%20de%20Node.js%20con%20libuv.png)

> [!example]- Transcripción de la imagen
> *Application* le entrega JavaScript a **V8**, que se comunica con los **Node.js Bindings (Node API)**. Estos dejan los eventos en la *Event Queue* de **libuv**, desde donde los toma el **Event Loop**. Las operaciones bloqueantes (*blocking ops*) van a una *Task Queue* atendida por un **Worker Thread Pool**. Las no bloqueantes (*non-blocking ops*) van a **I/O Polling** del sistema operativo (epoll, kqueue, etc.). Los resultados vuelven al event loop y de ahí al código.

> [!tip] Una metáfora: Node recibiendo pedidos
> Node es quien atiende el teléfono de un restaurante. Recibe un pedido, lo pasa a la cocina y sigue atendiendo llamadas mientras se cocina. Cuando un pedido está listo, el repartidor lo entrega. Los platos complejos tardan más en la cocina, los simples salen antes, y nadie deja de atender el teléfono.

> [!warning] Un cálculo pesado bloquea a todos
> Como hay un solo hilo de JavaScript, un ciclo largo (como el `for` de dos mil millones de vueltas) detiene el event loop: ninguna otra request se atiende hasta que termine. En Node, el trabajo intensivo de CPU debe moverse a *worker threads* u otro servicio.

## Preguntas de repaso

> [!question]- ¿Por qué `setTimeout(f, 0)` no ejecuta `f` inmediatamente?
> Porque el callback va a la cola y el event loop solo lo pasa a la pila cuando esta queda vacía, es decir, después de que termine todo el código síncrono en curso.

> [!question]- Si JavaScript tiene un solo hilo, ¿cómo atiende Node muchas requests de I/O a la vez?
> Porque el I/O no se ejecuta en ese hilo: libuv lo delega al sistema operativo o a su pool de hilos. Mientras tanto, el hilo de JavaScript sigue atendiendo otros eventos, y los resultados vuelven como callbacks por la cola.

> [!question]- ¿Por qué Node no es buena opción para tareas intensivas de CPU?
> Porque el cálculo ocupa el único hilo de JavaScript y bloquea el event loop: mientras dura, el servidor no puede responder ninguna otra request.
