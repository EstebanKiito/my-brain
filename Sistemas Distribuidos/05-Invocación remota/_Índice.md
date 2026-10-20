# Invocación remota — índice

Cómo un proceso le pide a otro, en otra máquina, que ejecute una operación: el protocolo request-reply, los enfoques REST y RPC, el rol de los stubs, RPC y RMI en Python con `xmlrpc`, y la versión moderna con gRPC y Protocol Buffers.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (comunicación remota, request-reply, ejemplo de Twitch, REST, RPC, stubs, REST frente a RPC, servidor y cliente RPC, RMI, gRPC y Protocol Buffers) y completado con las slides de la clase "Comunicación entre nodos II" (REST en la bibliografía, servidor RMI, ejemplo de Protocol Buffers y la pregunta del sistema de vigilancia). El código se ejecutó con Python 3.13 y `grpcio-tools`.

## Orden de estudio
1. [[01 - Invocación remota y REST|Invocación remota y REST]]: qué es invocar una operación remota, request-reply y REST.
2. [[02 - RPC y stubs|RPC y stubs]]: transparencia, client stub y server stub, y diferencias con REST.
3. [[03 - RPC y RMI en Python con xmlrpc|RPC y RMI en Python con xmlrpc]]: servidor, cliente, estado y objetos remotos.
4. [[04 - gRPC y Protocol Buffers|gRPC y Protocol Buffers]]: HTTP/2, esquemas `.proto` y serialización binaria.

Las imágenes de esta carpeta están en `adjuntos/`.
