---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - productor-consumidor
  - bounded-buffer
  - mutex
  - origen/complemento
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
---

# Problema del productor-consumidor y buffer acotado

Piensa en una tienda donde se está vendiendo y reponiendo al mismo tiempo: alguien agrega productos al estante mientras otro los retira. Si ambos actualizan el inventario sin coordinarse, el número deja de ser confiable. El **problema del productor-consumidor** (o del *bounded buffer*) modela exactamente esa situación, y es el problema clásico con que se ponen a prueba las herramientas de sincronización.

## El problema

- Hay un **buffer circular de tamaño limitado $N$**: la lista donde se van guardando las cosas.
- Hay **dos threads**: el **productor** agrega elementos y el **consumidor** los saca.
- **Todos los elementos producidos deben ser consumidos, en orden.**

![Problema del productor consumidor y buffer circular](adjuntos/Problema%20del%20productor%20consumidor%20y%20buffer%20circular.png)

> [!example]- Transcripción de la imagen
> Un **Producer** con una flecha *Insert item* hacia un **Buffer** de casillas, cuatro de ellas ocupadas (sombreadas) y el resto marcadas como *Empty slots*. Desde la primera casilla ocupada sale una flecha *Remove item* hacia el **Consumer**.

Hay que resolver **dos necesidades** a la vez:

1. **Exclusión mutua:** que productor y consumidor no actualicen el contador compartido al mismo tiempo.
2. **Esperar por una condición:** el productor no puede insertar si el buffer está **lleno**, y el consumidor no puede sacar si está **vacío**.

## Versión 1: sin sincronización

La cantidad de elementos se lleva en una variable compartida `stock`, y los índices `in` y `out` rotan con módulo $N$.

![Condición de carrera en variable stock compartida](adjuntos/Condici%C3%B3n%20de%20carrera%20en%20variable%20stock%20compartida.png)

> [!example]- Transcripción de la imagen
> `int stock = 0; T storage[N];`. **Productor:** `int in = 0; while('p') { item = produce(); while (stock == N); // Storage full  storage[in] = item; in = ++in%N; // rotate index  stock++; }`. **Consumidor:** `int out = 0; while('c') { while(!stock); // Wait for new items  item = storage[out]; out = ++out%N; stock--; consume(item); }`.

`stock++` y `stock--` son **la sección crítica**: cada uno es *leer, modificar, escribir*. En ensamblador x86, `stock++` queda como `MOV EAX, [stock]`, `ADD EAX, 1` y `MOV [stock], EAX`, y un cambio de contexto puede ocurrir entre cualquiera de esas instrucciones. Si se intercalan, se pierde una actualización y `stock` queda con un valor incorrecto.

## Versión 2: locks en stock

Como `stock` es la sección crítica, se protege con un lock:

![Protección de variable stock con locks](adjuntos/Protecci%C3%B3n%20de%20variable%20stock%20con%20locks.png)

> [!example]- Transcripción de la imagen
> "Podemos agregar locks en stock". El mismo productor y consumidor, pero `stock++` y `stock--` quedan entre `lock.acquire();` y `lock.release();`. Al pie: "¿Cómo eliminamos busy waiting?".

Ahora el contador es correcto, pero los dos `while (stock == N);` y `while (!stock);` **giran gastando CPU** mientras esperan: es *busy waiting*.

## Versión 3: dormir y despertar

Para eliminar la espera activa, cada thread **duerme** (`sleep()`) cuando no puede avanzar y el otro lo **despierta** (`wakeup()`): *"si no hay comida, mándame a dormir; si hay comida, despiértame"*. El productor despierta al consumidor cuando el stock pasa a 1, y el consumidor despierta al productor cuando se libera un espacio. El código está en [[04 - Mutex locks y el dilema de busy waiting versus dormir|mutex y sleep/wakeup]].

> [!warning] ¿Y si el consumidor es interrumpido antes de dormir?
> El consumidor ve `stock == 0` y decide dormir, pero antes de llegar a ejecutar `sleep()` lo interrumpen. El productor agrega un elemento, ve `stock == 1` y llama a `wakeup(consumer)`… sobre alguien que **todavía no duerme**: el aviso se pierde. Luego el consumidor duerme y nadie lo despertará. Revisar la condición y dormirse deberían ser una sola operación, y eso es lo que resuelven los [[06 - Semáforos de Dijkstra y tipos de semáforos|semáforos]] y las [[07 - Variables de condición y monitores|variables de condición]].

| Versión | Contador correcto | Sin busy waiting | Sin avisos perdidos |
|---|---|---|---|
| Sin sincronización | ✗ | ✗ | — |
| Locks en `stock` | ✓ | ✗ | — |
| `sleep` / `wakeup` | ✓ | ✓ | ✗ |
| Semáforos o variables de condición | ✓ | ✓ | ✓ |

## Preguntas de repaso

> [!question]- ¿Cuál es la sección crítica del productor-consumidor y por qué?
> La actualización de `stock` (`stock++` y `stock--`), porque ambos threads la modifican y cada operación es leer, modificar y escribir. Si se intercalan, se pierde una actualización.

> [!question]- ¿Basta un lock para resolver el problema completo?
> No. El lock garantiza la exclusión mutua sobre `stock`, pero los threads siguen esperando con *busy waiting* cuando el buffer está lleno o vacío. Falta un mecanismo eficiente para esperar una condición.

> [!question]- ¿Qué problema tiene la solución con `sleep()` y `wakeup()`?
> Si el consumidor decide dormir pero es interrumpido antes de hacerlo, el `wakeup` del productor llega antes de que duerma y se pierde. Después el consumidor se duerme para siempre.

> [!question]- ¿Qué dos condiciones de espera impone el buffer acotado?
> El productor debe esperar si el buffer está lleno ($N$ elementos) y el consumidor debe esperar si está vacío (0 elementos).
