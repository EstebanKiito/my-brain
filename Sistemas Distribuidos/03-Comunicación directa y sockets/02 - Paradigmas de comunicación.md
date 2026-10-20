---
ramo: "Sistemas Distribuidos"
tema: "Comunicación directa y sockets"
tags:
  - sd/comunicacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Persistencia, sincronía y acoplamiento]]"
---

# Paradigmas de comunicación

Los procesos de un sistema distribuido se comunican de tres maneras, según cuánto se interponga entre ellos: nada (directa), un intermediario (indirecta) o una capa que hace parecer local una operación remota (invocación remota). Los paradigmas no son excluyentes y los sistemas reales suelen mezclarlos. Cada uno se estudia en su propio tema.

![Paradigmas de comunicación directa, indirecta y remota](adjuntos/Paradigmas%20de%20comunicaci%C3%B3n%20directa,%20indirecta%20y%20remota.png)

> [!example]- Transcripción de la imagen
> - **Directa:** la forma más simple de comunicación entre procesos, a través del paso de mensajes. Ligera, eficiente y minimalista. Hay acoplamiento referencial.
> - **Indirecta:** la comunicación se realiza **a través de un intermediario distinto al sistema operativo**. Sin acoplamiento directo entre emisor y receptor. Según cómo sea el intermediario, los mensajes pueden ser persistentes o transitorios.
> - **Remota:** se incluyen componentes o protocolos para comunicar procesos ubicados en distintas máquinas conectadas en red. Generalmente se encapsula el paso de mensajes para garantizar los protocolos.

## Directa

El emisor envía mensajes al receptor sin nadie entre medio, típicamente con **sockets**. Por eso:

- Necesita saber **a quién** comunicarse (dirección y puerto): hay acoplamiento referencial.
- En general necesita que **ambos estén vivos** a la vez.

Es la opción más liviana y la base de las otras dos. Ver [[05 - Sockets TCP en Python|Sockets TCP en Python]].

## Indirecta

La comunicación pasa por un **intermediario** que no es el sistema operativo: una cola de mensajes, un broker *publish-subscribe*, un servidor de correo. El emisor entrega el mensaje al intermediario y este lo hace llegar, así que emisor y receptor no se conocen directamente. Si el intermediario guarda los mensajes, también se desacoplan en el tiempo.

Una VPN funciona de manera parecida: el cliente se comunica con el servidor de la VPN, que reenvía el tráfico al servicio final.

## Invocación remota

Se agregan componentes y reglas para que un proceso **invoque operaciones o métodos que se ejecutan en otra máquina**, como si fueran locales. El paso de mensajes queda encapsulado: alguien empaqueta la petición en un formato acordado y otro la desempaqueta (*parsea*) del otro lado.

El ejemplo típico es una **API REST**: las reglas dicen que la respuesta trae un código de estado y un cuerpo en JSON, y el intermediario (la biblioteca HTTP) se encarga de serializar y parsear. El programador solo ve "llamé a la operación y obtuve un resultado".

| Paradigma | ¿Intermediario? | Acoplamiento típico | Ejemplos |
|---|---|---|---|
| Directa | No | Temporal y referencial | Sockets, MPI |
| Indirecta | Sí, distinto al SO | Desacoplado (según el intermediario) | Colas de mensajes, publish-subscribe |
| Invocación remota | Capa que encapsula los mensajes | Referencial | REST, RPC, gRPC |

> [!tip] Se combinan
> Una invocación remota corre sobre sockets (comunicación directa), y un sistema puede publicar eventos en una cola (indirecta) a la vez que expone una API REST (remota). Clasificar ayuda a razonar, pero no hay que elegir uno solo.

## Preguntas de repaso

> [!question]- ¿Por qué la comunicación directa implica acoplamiento referencial?
> Porque el emisor debe indicar explícitamente el destino (dirección y puerto del receptor). Sin conocer al receptor no puede enviarle nada.

> [!question]- ¿Qué gana un sistema al usar comunicación indirecta?
> Desacopla a emisor y receptor: no necesitan conocerse y, si el intermediario almacena los mensajes, tampoco necesitan estar activos al mismo tiempo. Así se pueden agregar o reemplazar receptores sin tocar al emisor.

> [!question]- ¿Qué encapsula la invocación remota respecto de la comunicación directa?
> El paso de mensajes: el formato de la petición, la serialización de los datos y el parseo de la respuesta. El programador invoca una operación y la capa se encarga de transformarla en mensajes por la red.
