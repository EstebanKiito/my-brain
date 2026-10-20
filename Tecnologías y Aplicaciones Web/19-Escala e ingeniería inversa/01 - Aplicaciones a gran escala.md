---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Escala e ingeniería inversa"
tags:
  - web
  - escalabilidad
  - arquitectura
  - origen/complemento
prerrequisitos:
  - "[[02 - Frontend, backend y frameworks web]]"
  - "[[04 - Caché, Cache API y CDN]]"
---

# Aplicaciones a gran escala

La aplicación del curso tiene un frontend en React, una API en Express y una base de datos: un servidor atiende a unos pocos clientes. ¿Qué cambia cuando son millones? Basta un ejercicio para notarlo. ¿Qué haría falta para que una persona suba una historia en Instagram y que sus seguidores la vean? Almacenar el video, procesarlo en varias resoluciones, avisar a los seguidores y servirlo rápido en todo el mundo. Nada de eso cabe en un solo servidor que responde requests de a una.

## De un servidor a muchos

![Muchos clientes, servidores y bases de datos](adjuntos/Muchos%20clientes%2C%20servidores%20y%20bases%20de%20datos.png)

> [!example]- Transcripción de la imagen
> Tres columnas: **Client** (muchos computadores, notebooks y celulares), **Server/App** (muchas copias apiladas de *Web Server / Web App*) y **Storage** (varias bases de datos, BD). Flechas en ambos sentidos entre cada columna.

A gran escala, cada capa se **replica**: muchas instancias de la aplicación y varias bases de datos, en vez de una sola de cada una. Eso genera problemas nuevos: cómo repartir las requests entre las instancias, qué hacer con el trabajo que tarda demasiado y cómo avisar a millones de clientes cuando algo cambia. La clase plantea tres herramientas para enfrentarlos.

## Colas de procesamiento

Una **cola de mensajes** (*message queue*) desacopla a quien pide un trabajo de quien lo ejecuta:

![Cola de mensajes entre productor y consumidores](adjuntos/Cola%20de%20mensajes%20entre%20productor%20y%20consumidores.png)

> [!example]- Transcripción de la imagen
> "Message Queue: consumers pull messages, process and remove". Un **Producer** deja mensajes numerados (1, 2, 3) en una cola; **Consumer A** y **Consumer B** los van sacando, los procesan y los eliminan de la cola cuando terminan.

- El **productor** (por ejemplo, la API que recibe la historia) deja un mensaje y responde de inmediato al usuario.
- Los **consumidores** (*workers*) sacan los mensajes y hacen el trabajo pesado, como transcodificar el video o enviar notificaciones, a su ritmo.
- Si llegan más mensajes de los que se alcanzan a procesar, la cola **absorbe el pico**, y se pueden agregar consumidores.

## Balanceadores de carga

![Balanceador de carga frente a varios servidores](adjuntos/Balanceador%20de%20carga%20frente%20a%20varios%20servidores.png)

> [!example]- Transcripción de la imagen
> Varios *clients (end users)* se conectan por Internet a un **Load Balancer**, que reparte las requests entre tres servidores de *Application Web Services*. Los tres usan la misma **Database**.

Un **balanceador de carga** recibe todas las requests y las **reparte** entre varias instancias de la aplicación (por turnos, por la que tenga menos carga, etc.). También deja de enviar tráfico a una instancia caída. Así se agrega capacidad sumando servidores (**escalamiento horizontal**) en vez de comprar uno más grande (**vertical**).

> [!warning] Escalar horizontalmente exige no guardar estado en el servidor
> Si la sesión de un usuario está en la memoria de la instancia A y el balanceador manda su siguiente request a la instancia B, B no lo reconoce. Por eso las sesiones van en un almacén compartido (como Redis) o en tokens: es la misma idea de *stateless* de REST.

## Bases de datos en tiempo real

Para mostrar cambios al instante a muchos clientes (un chat, un tablero colaborativo, los "visto por" de una historia) se usan bases de datos orientadas al tiempo real:

- **Redis**: datos en memoria, muy rápido, con publicación y suscripción (*pub/sub*) para avisar cambios.
- **Firebase**: una base de datos en la nube que **sincroniza** los datos con los clientes conectados, que reciben los cambios sin tener que preguntar.

> [!tip] Cada herramienta resuelve un cuello de botella
> El balanceador reparte las **requests**, la cola posterga el **trabajo pesado**, la caché y la CDN evitan **repetir respuestas**, y las bases en tiempo real **empujan los cambios** a los clientes.

El escalamiento y sus compromisos (consistencia, disponibilidad y particiones) se ven en [[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]].

## Preguntas de repaso

> [!question]- ¿Por qué la API que recibe una historia no la procesa entera antes de responder?
> Porque transcodificar el video y notificar a los seguidores toma mucho tiempo, y el usuario quedaría esperando. Con una cola, la API responde de inmediato y los workers hacen ese trabajo en segundo plano.

> [!question]- ¿Qué problema genera un balanceador de carga si la sesión se guarda en la memoria del servidor?
> Que requests sucesivas del mismo usuario pueden llegar a instancias distintas, y la que no tiene su sesión no lo reconoce. La sesión debe estar en un almacén compartido o en un token.

> [!question]- ¿Qué diferencia hay entre escalar vertical y horizontalmente?
> Vertical es darle más recursos a una sola máquina, y tiene un límite físico. Horizontal es sumar más máquinas que se reparten el trabajo, lo que requiere balanceo y que las instancias no guarden estado.
