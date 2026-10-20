---
ramo: "Sistemas Distribuidos"
tema: "Comunicación indirecta"
tags:
  - sd/comunicacion-indirecta
  - python
  - origen/complemento
prerrequisitos:
  - "[[01 - Comunicación indirecta y sus mecanismos]]"
---

# Colas de mensajes

Una **cola de mensajes** es el intermediario más simple: un buzón donde los productores dejan mensajes y los consumidores los retiran cuando pueden. Como la cola guarda los mensajes, productor y consumidor no necesitan conocerse ni estar activos al mismo tiempo. Es el mecanismo detrás del procesamiento en segundo plano de muchos sistemas grandes.

## Funcionamiento

![Cola de mensajes con send, receive, poll y notify](adjuntos/Cola%20de%20mensajes%20con%20send,%20receive,%20poll%20y%20notify.png)

> [!example]- Transcripción de la imagen
> A la izquierda, dos productores hacen *Send* de mensajes hacia un intermediario con tres colas. A la derecha, tres consumidores las usan de formas distintas: uno hace *Receive* sobre la primera cola (con tres mensajes), otro hace *Poll* sobre la segunda (con uno) y el tercero recibe un *Notify* desde la tercera cola cuando le llega un mensaje.

- El proceso **productor** envía mensajes a una cola.
- El proceso **consumidor** obtiene los mensajes de la cola.
- Una vez extraído, el mensaje **generalmente se elimina** de la cola. No siempre: hay implementaciones que lo conservan, por ejemplo con un contador de cuántos consumidores lo leyeron, y lo borran después.
- Por defecto asegura **desacoplamiento temporal**, porque la cola **persiste** los mensajes.

## Operaciones básicas

| Operación | Qué hace | ¿Bloquea? |
|---|---|---|
| `send` | Añade un mensaje a la cola | No |
| `receive` | Espera hasta que haya un mensaje y lo extrae | Sí |
| `poll` | Revisa si hay mensaje y, si lo hay, lo obtiene | No |
| `notify` | Instala un controlador que se llama cuando llega un mensaje, para avisar al consumidor | No (el aviso llega después) |

`receive` es cómodo pero deja al consumidor detenido; `poll` no bloquea, pero obliga a preguntar una y otra vez; `notify` invierte el control y es la cola la que avisa: "mándame un mensaje cuando llegue algo".

## Ejemplo en Python

`queue.Queue` es una cola en memoria entre threads. No persiste en disco, pero muestra el desacoplamiento: el consumidor llega tarde y los mensajes lo esperan.

```python
import queue, threading, time

cola = queue.Queue()                    # el intermediario: guarda los mensajes

def productor():
    for i in range(3):
        cola.put(f"pedido {i}")         # send: no sabe quién lo consumirá
    print("productor terminó")

def consumidor():
    time.sleep(0.5)                     # llega después: los mensajes siguen ahí
    while True:
        try:
            msg = cola.get(timeout=0.1) # receive con plazo; get_nowait() sería poll
        except queue.Empty:
            break
        print("consumí", msg)

threading.Thread(target=productor).start()
c = threading.Thread(target=consumidor); c.start(); c.join()
```

La salida muestra `productor terminó` antes que los tres `consumí pedido …`: el productor ya no existe cuando se consumen sus mensajes. Es el mismo patrón que [[05 - Problema del productor-consumidor y buffer acotado|productor-consumidor]] de Sistemas Operativos, pero con el buffer convertido en un servicio.

## Un caso real: WebSphere MQ de IBM

![Colas de WebSphere MQ con proxy y stub](adjuntos/Colas%20de%20WebSphere%20MQ%20con%20proxy%20y%20stub.png)

> [!example]- Transcripción de la imagen
> Un *Client* usa un *Proxy* que, por un *Client channel*, se conecta a un *Stub* dentro del *Queue manager*. El stub deposita los mensajes en una de varias colas, y los *Services* de la derecha consumen cada una.

El cliente no habla con los servicios. Su **proxy** da formato al mensaje y lo envía al **stub** del administrador de colas, que decide en qué cola dejarlo; cada servicio consume su cola a su ritmo. Que el mensaje se borre al entregarse o no depende de cómo esté configurado el intermediario.

> [!tip] Cuándo usar una cola
> Cuando el trabajo puede hacerse **después** y por **quien esté disponible**: enviar correos, procesar pagos, generar reportes. La cola absorbe los picos de carga y desacopla a quien pide de quien hace. Ver [[01 - Aplicaciones a gran escala|Aplicaciones a gran escala]].

## Preguntas de repaso

> [!question]- ¿Por qué una cola de mensajes logra desacoplamiento temporal?
> Porque persiste los mensajes: el productor los deja y puede desconectarse, y el consumidor los retira cuando se conecte. Ninguno necesita estar activo al mismo tiempo que el otro.

> [!question]- ¿Qué diferencia hay entre `receive`, `poll` y `notify` para el consumidor?
> `receive` lo bloquea hasta que haya un mensaje; `poll` revisa sin bloquear y retorna vacío si no hay nada; `notify` registra un controlador para que la cola le avise cuando llegue un mensaje, sin que tenga que preguntar.

> [!question]- Si varios consumidores leen la misma cola y los mensajes se eliminan al extraerse, ¿qué recibe cada uno?
> Cada mensaje lo procesa un solo consumidor, el que lo extrae primero. Así se reparte el trabajo entre ellos, a diferencia de publish-subscribe, donde cada suscriptor interesado recibe su copia.
