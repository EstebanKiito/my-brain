---
ramo: "Sistemas Distribuidos"
tema: "Invocación remota"
tags:
  - sd/invocacion-remota
  - origen/complemento
prerrequisitos:
  - "[[02 - Paradigmas de comunicación]]"
  - "[[04 - Protocolos de aplicación DNS y HTTP]]"
---

# Invocación remota y REST

Enviar datos a otra máquina no es lo mismo que pedirle que **haga algo**. La invocación remota es el paradigma en que un proceso le pide a otro, en otra máquina, que ejecute una operación y le devuelva el resultado. Sus dos enfoques más conocidos son REST, sobre los estándares de HTTP, y RPC, que imita una llamada a función local.

## Comunicación remota e invocación remota

La **comunicación remota** abarca cualquier uso de componentes o protocolos para intercambiar datos entre procesos en distintas máquinas: transmitir información, enviar archivos o comunicarse con una API.

La **invocación remota** es un caso particular, con una característica clave: **el receptor ejecuta una acción solicitada por el emisor**. Se invocan operaciones o métodos que corren en otra máquina o proceso.

> [!example] Twitch
> Transmitir en vivo es comunicación remota: el streamer solo envía datos. Pagar una suscripción **gatilla una acción** en la transmisión (una alerta en pantalla): eso sí es invocación remota.

## El protocolo request-reply

![Protocolo request-reply](adjuntos/Protocolo%20request-reply.png)

> [!example]- Transcripción de la imagen
> Dos líneas de tiempo, cliente (C) y servidor (S). El cliente envía *operation* al servidor y queda en *wait for reply* (línea punteada) hasta que el servidor devuelve la *response*.

Por defecto, la invocación remota usa un protocolo **request-reply**: enviar un mensaje y esperar la respuesta. Por eso es **sincrónico** y **acoplado temporalmente**. Se puede volver asincrónico con otras herramientas, como threads o promesas, para que el cliente siga trabajando mientras espera.

## REST

**REST** (*Representational State Transfer*) es el primer enfoque:

- Usa **HTTP** y se alinea con sus estándares.
- Identifica los recursos o endpoints con **URLs** y los manipula con los **métodos HTTP** (`GET`, `POST`, etc.).
- Cada ejecución es **stateless**: el servidor no recuerda las peticiones anteriores, así que cada una trae todo lo necesario.
- Sus mensajes son **legibles por humanos**.

```http
GET /anime/detective-conan HTTP/1.1
Host: www3.animeflv.net
Accept: text/html
```

> [!tip] REST y la bibliografía
> Cuando se definió el concepto de invocación remota (años 70), REST no existía, por lo que la bibliografía no lo incluye. Sin embargo, sus características permiten considerarlo parte de este paradigma.

Los principios de REST y el diseño de endpoints CRUD están en [[02 - CRUD y principios REST|CRUD y principios REST]].

## Ejemplo: un diseño híbrido

Un sistema de vigilancia tiene cámaras que reportan datos en tiempo real **por RPC** a un servidor, y este reenvía los datos a distintos clientes **mediante colas**. ¿Qué ventaja aporta combinar ambos?

- La invocación remota es sincrónica y acoplada en el tiempo: sirve para que cada cámara entregue su dato y sepa que llegó.
- La cola desacopla en el tiempo: los clientes **reciben los datos cuando ellos quieran**, sin que el servidor tenga que esperarlos.

No disminuye la latencia (agrega un salto), no permite que las cámaras funcionen con el servidor caído ni asegura que todos reciban todo al mismo tiempo. Su ventaja clave es la flexibilidad temporal de los clientes.

## Preguntas de repaso

> [!question]- ¿Qué distingue la invocación remota del resto de la comunicación remota?
> Que el receptor ejecuta una acción pedida por el emisor y devuelve un resultado. Transmitir datos o enviar un archivo es comunicación remota, pero no invoca operaciones.

> [!question]- ¿Por qué el protocolo request-reply es acoplado temporalmente?
> Porque el cliente envía la petición y espera la respuesta: el servidor tiene que estar activo en ese momento para procesarla y contestar.

> [!question]- ¿Qué significa que REST sea stateless y qué ventaja trae?
> Que el servidor no guarda memoria de peticiones anteriores: cada una trae toda la información necesaria. Así cualquier réplica del servidor puede atender cualquier petición, lo que facilita escalar.
