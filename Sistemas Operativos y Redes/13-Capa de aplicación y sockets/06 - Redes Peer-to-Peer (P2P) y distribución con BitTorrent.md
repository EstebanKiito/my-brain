---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - p2p
  - bittorrent
  - dht
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación|01 - Arquitecturas de aplicación y modelos de comunicación]]"
---

# Redes Peer-to-Peer (P2P) y distribución con BitTorrent

En una red **P2P** (*peer-to-peer*), los clientes forman una red entre ellos y **no dependen de un servidor**. Eso les da **mejor escalabilidad**, porque cada miembro aporta capacidad, pero también un problema nuevo: los miembros entran y salen todo el tiempo, y la red **debe manejar la pertenencia y el abandono de miembros**. La comparación con cliente-servidor está en [[13-Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación|arquitecturas de aplicación]].

## BitTorrent

BitTorrent reparte un archivo grande **por pedazos** (*chunks*). Si quiero descargar, por ejemplo, un juego, cada host de la red me puede prestar una parte, y yo a la vez comparto las partes que ya tengo. Así se pueden distribuir archivos muy grandes sin un servidor que los entregue completos a todos.

Para unirse:

1. Se consulta a un **tracker**, un servidor que conoce a los pares que participan en la red de ese archivo, y se obtiene una **lista de pares**.
2. Se conecta con algunos de esos pares y empieza el **intercambio de pedazos**: descarga lo que le falta y sube lo que tiene.

![Arquitectura de redes peer to peer P2P y protocolo BitTorrent](adjuntos/Arquitectura%20de%20redes%20peer%20to%20peer%20P2P%20y%20protocolo%20BitTorrent.png)

> [!example]- Transcripción de la imagen
> *Alice* se conecta al *Tracker* para *Obtain list of peers* (flecha azul). Luego intercambia pedazos (*Trading chunks*) con varios *Peer*, todos conectados entre sí con flechas en ambas direcciones.

En BitTorrent, los pares que ya tienen el archivo completo y solo suben se suelen llamar *seeds*, y los que todavía descargan, *leechers*. Para que nadie solo descargue sin aportar, cada par prioriza subirle a quienes le suben más rápido.

## DHT: P2P sin tracker

Una **DHT** (*Distributed Hash Table*) es un **método de direccionamiento para redes P2P estructuradas**:

- **cada miembro posee una identificación única**;
- se construye una **red superpuesta** (*overlay network*) entre los miembros, una red lógica sobre Internet;
- **los miembros se encargan de enrutar los mensajes**: no hace falta un servidor central que sepa quién tiene qué.

Cada clave (por ejemplo, el identificador de un archivo) queda a cargo de un miembro determinado. En el anillo de la figura, una convención habitual es que el responsable de una clave sea el primer miembro con identificador mayor o igual a ella.

![Distribución de archivos por fragmentos y tablas hash distribuidas](adjuntos/Distribuci%C3%B3n%20de%20archivos%20por%20fragmentos%20y%20tablas%20hash%20distribuidas.png)

> [!example]- Transcripción de la imagen
> "Método de direccionamiento para redes P2P estructuradas. Cada miembro posee una identificación única. Se construye una *overlay network* entre miembros. Miembros se encarga de enrutar mensajes". Dos anillos con los nodos 1, 3, 4, 5, 8, 10, 12 y 15. En el izquierdo, cada nodo apunta solo a su sucesor, y el nodo 3 pregunta "*Who is responsible for key 11?*". En el derecho, además del anillo, cada nodo tiene atajos hacia nodos lejanos.

```python
NODOS = sorted([1, 3, 4, 5, 8, 10, 12, 15])     # identificadores del anillo

def responsable(clave):
    """El primer nodo con id >= clave; si no hay, se da la vuelta al anillo."""
    for n in NODOS:
        if n >= clave:
            return n
    return NODOS[0]

def buscar(clave, desde):
    """Cada nodo solo conoce a su sucesor: la consulta avanza por el anillo."""
    i, saltos = NODOS.index(desde), [desde]
    while NODOS[i] != responsable(clave):
        i = (i + 1) % len(NODOS)
        saltos.append(NODOS[i])
    return saltos

print(responsable(11), buscar(11, 3))   # 12 [3, 4, 5, 8, 10, 12]
```

Si cada nodo conoce solo a su sucesor, la consulta da la vuelta paso a paso (5 saltos en el ejemplo). Los **atajos** del anillo derecho permiten llegar en muchos menos saltos.

## Preguntas de repaso

> [!question]- ¿Qué ventaja y qué desafío tiene una red P2P frente a cliente-servidor?
> Escala mejor, porque cada miembro aporta capacidad y no depende de un servidor. El desafío es manejar la entrada y salida constante de miembros.

> [!question]- ¿Para qué sirve el tracker en BitTorrent?
> Para que un nuevo par obtenga la lista de pares que están compartiendo el archivo y pueda conectarse con ellos para intercambiar pedazos.

> [!question]- ¿Qué es una DHT y qué problema resuelve?
> Una tabla hash distribuida: cada miembro tiene un identificador y es responsable de ciertas claves, y los miembros enrutan las consultas entre ellos. Permite encontrar quién tiene un recurso sin un servidor central.

> [!question]- En el anillo de la figura, ¿qué nodo es responsable de la clave 11 y por qué ayudan los atajos?
> El nodo 12, el primero con identificador mayor o igual a 11. Sin atajos, una consulta desde el nodo 3 recorre 3 → 4 → 5 → 8 → 10 → 12; con atajos, se salta por encima de varios nodos y se llega antes.
