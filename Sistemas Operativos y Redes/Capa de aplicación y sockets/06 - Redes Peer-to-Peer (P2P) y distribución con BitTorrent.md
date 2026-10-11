---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - p2p
  - bittorrent
  - dht
prerrequisitos:
  - "[[Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación|01 - Arquitecturas de aplicación y modelos de comunicación]]"
---

# Redes Peer-to-Peer (P2P) y distribución con BitTorrent

Las arquitecturas entre pares (*Peer-to-Peer*, P2P) distribuyen el almacenamiento y la carga computacional entre nodos autónomos (*peers*) de igual jerarquía, sin depender de servidores centrales permanentes. Protocolos como BitTorrent y las Tablas Hash Distribuidas (DHT) permiten la transferencia eficiente y altamente escalable de archivos de gran tamaño.

---

## Redes P2P y protocolo BitTorrent (mis apuntes)

RED P2P
- Mejor escalabilidad
- Deben maneja pertenencia y abandono de miembros
- Redes entre pares de clientes (NO DEPENDEN DE UN SERVER)

![Arquitectura de redes peer to peer P2P y protocolo BitTorrent](adjuntos/Arquitectura%20de%20redes%20peer%20to%20peer%20P2P%20y%20protocolo%20BitTorrent.png)

> [!example]- Transcripción de la imagen
> Arquitectura de BitTorrent:
> - Enjambre (*swarm*): Conjunto de todos los pares que participan en la descarga o subida de un archivo específico.
> - Rastreador (*tracker*): Nodo o servicio que registra la lista de pares actualmente activos en el enjambre y entrega un subconjunto aleatorio de IPs a nuevos participantes.
> - *Leechers* (descargando) y *Seeds* (pares que poseen el archivo completo y continúan subiendo fragmentos).

Cuando me quiero conectar a una red p2p: consulto al servidor un tracker → Como conectarme a los otros clientes que estan participando de la red
Por ejemplo otro protocolo BitTorrent → Si quiero descargar un juego, cada uno de los host, me puede prestar una parte del juego (archivos por pedazos) para abarcar juegos mas grandes por ejemplo
Se construye una red a base de una HASH TABLE

![Distribución de archivos por fragmentos y tablas hash distribuidas](adjuntos/Distribución%20de%20archivos%20por%20fragmentos%20y%20tablas%20hash%20distribuidas.png)

> [!example]- Transcripción de la imagen
> Fragmentación y Tablas Hash Distribuidas (DHT):
> - Los archivos se dividen en fragmentos (*chunks* o bloques) de tamaño fijo (típicamente 256 KB).
> - Algoritmo *Rarest First*: los pares solicitan primero los fragmentos más escasos en el enjambre para maximizar la diversidad de bloques.
> - *Tit-for-Tat*: un par envía fragmentos a los 4 pares que actualmente le proveen la mayor tasa de descarga (*unchoked*), reservando un optimista (*optimistic unchoking*) para descubrir nuevos pares rápidos.
> - DHT (e.g. Kademlia): Permite operar sin *trackers* centralizados (*trackerless*), distribuyendo el mapeo clave-valor sobre el espacio de identificadores de los nodos.

> [!tip] Complemento de clase: Churn en redes P2P
> El dinamismo de entrada y salida arbitraria de pares se denomina *churn*. Las redes P2P deben ser tolerantes a fallos y reconfigurar sus rutas o redistribuir fragmentos cuando nodos abandonan la red sin previo aviso.

---

## Preguntas de repaso

> [!question]- ¿Por qué la estrategia *Rarest First* es fundamental para la supervivencia de un enjambre BitTorrent?
> Porque asegura que los fragmentos menos comunes se repliquen rápidamente entre múltiples pares; si un par con un fragmento único se desconecta antes de compartirlo, el archivo quedaría incompleto para todo el enjambre.

> [!question]- ¿Qué incentivo proporciona el algoritmo *Tit-for-Tat* frente al problema del usuario parásito (*free rider*)?
> Cada nodo prioriza subir datos a los pares que le están devolviendo datos a mayor velocidad. Un usuario que bloquea sus subidas o limita su ancho de banda es penalizado (*choked*) por sus vecinos, reduciendo drásticamente su velocidad de descarga.

> [!question]- ¿Cómo reemplaza una DHT (Distributed Hash Table) al *tracker* centralizado en BitTorrent?
> Asigna a cada archivo un hash infohash de 160 bits e indexa los pares responsables de cada clave en una red superpuesta (*overlay network*), permitiendo que los nodos encuentren otros pares mediante consultas estructuradas nodo a nodo sin necesidad de un servidor único.

