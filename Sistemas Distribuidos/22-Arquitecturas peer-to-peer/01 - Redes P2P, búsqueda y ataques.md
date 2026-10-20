---
ramo: "Sistemas Distribuidos"
tema: "Arquitecturas peer-to-peer"
tags:
  - sd/p2p
  - origen/complemento
prerrequisitos:
  - "[[02 - Sistemas centralizados, descentralizados y distribuidos]]"
  - "[[02 - Métodos de ataque y medidas de seguridad]]"
---

# Redes P2P, búsqueda y ataques

En una red **peer-to-peer** no hay servidor: cada nodo es cliente y servidor a la vez. Eso elimina el punto único de falla y abarata la infraestructura, pero obliga a resolver sin coordinador lo que antes resolvía el servidor: **dónde está** cada dato y **en quién confiar**.

## Definición y características

Una red P2P es una arquitectura distribuida donde **cada nodo actúa como cliente y servidor**, y comparte recursos directamente con otros nodos, sin un servidor centralizado.

- No hay organización global; cada usuario aporta recursos y aliviana la carga.
- Al crecer la red, cada nodo se conecta solo con un **subconjunto** de nodos, elegidos por proximidad o al azar.
- Alta tolerancia a la entrada y salida de nodos.
- Más barata en costos.
- Ejemplos: BitTorrent, GTA Online. Ver también [[06 - Redes Peer-to-Peer (P2P) y distribución con BitTorrent|Redes P2P y BitTorrent]].

## Desafíos

- **Distribución de carga:** equilibrar trabajo y disponibilidad sin sobrecargas.
- **Volatilidad:** los nodos (y sus datos) no están siempre encendidos ni conectados.
- **Datos mutables:** para objetos que cambian, se necesitan servidores de confianza adicionales que gestionen las versiones.
- **Búsqueda:** sin servidor central, nadie sabe qué nodo tiene qué; hay que buscar.

## Búsqueda en redes no estructuradas

| Estrategia | Cómo funciona | Ventaja | Costo |
|---|---|---|---|
| **Flooding** ("gritar y que todos griten") | BFS: cada nodo reenvía la consulta a todos sus vecinos, con un **TTL** que limita su vida | Encuentra rápido | Explosión exponencial de mensajes y ancho de banda |
| **Diffusion** ("susurrar") | BFS con un retraso aleatorio antes de cada reenvío | Más escalable: no congestiona la red de golpe; con el mismo TTL algunas consultas llegan más lejos | La respuesta puede tardar más |
| **Random walk** ("buscar a ciegas") | DFS aleatorio: se consulta a un vecino al azar, que a su vez elige a otro | Muy bajo consumo simultáneo de red | Alta latencia; puede no encontrar un dato aunque esté cerca |

![Búsqueda por inundación](adjuntos/B%C3%BAsqueda%20por%20inundaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Flooding: BFS que reenvía masivamente a todos los vecinos, y cada vecino reenvía a todos; se define un *Time-To-Live* (TTL), el tiempo que una consulta puede existir antes de declararse fallida; la explosión exponencial de mensajes consume mucho ancho de banda. A la derecha, un ícono de ondas expandiéndose con "deterministic transmission delays".

## Seguridad

Sin servidor, el atacante tiene dificultades:

- no sabe qué nodo tiene la información que busca;
- comprometer un nodo no afecta al sistema global;
- cada nodo puede tener defensas propias (cifrado, firewall, IDS/IPS), lo que impide una estrategia uniforme;
- si la información está fragmentada o replicada, debe coordinar ataques contra muchos nodos.

A cambio, la libertad total de conexiones y búsquedas hace que la comunicación sea lenta, ruidosa y poco eficiente. Además aparecen ataques propios de P2P:

**Ataque Sybil (multiplicar identidades):** el atacante crea muchas identidades falsas para manipular votaciones o reputación. Contramedidas:

- **Proof of Work:** obtener un identificador exige un cálculo costoso.
- **Verificación de identidad:** llaves públicas verificadas por una autoridad descentralizada (web of trust, blockchain) o por quórum.
- **Topologías reforzadas:** restringir con quién puede conectarse un nodo.
- **Restricción geográfica o de latencia:** exigir características verificables (por ejemplo, IP geográficamente consistentes).

**Ataque Eclipse (aislar para controlar):** el atacante rodea a un nodo con vecinos maliciosos y controla todo lo que ve. Contramedidas:

- **Chequeo cruzado** por múltiples caminos, consultando nodos más lejanos.
- **Múltiples fuentes independientes:** vecinos geográficamente dispares.
- **Limitar conexiones entrantes por IP o subred.**
- **Rotación periódica de vecinos** y verificación de la información.

> [!tip] Ninguna basta sola
> Las contramedidas no son perfectas por separado, pero combinadas son muy robustas.

> [!example] Pregunta de aplicación
> En una red P2P de cámaras de vigilancia, un vecino dice sufrir un ataque Eclipse. La explicación que lo justifica: **sus cámaras enviaban alertas de un robo, pero los demás vecinos no recibían la notificación**. Su nodo estaba aislado. Cámaras que de pronto ven muchas vecinas inexistentes sería un ataque Sybil, y un colapso por solicitudes masivas, un DDoS.

## Preguntas de repaso

> [!question]- ¿Qué limita el TTL en la búsqueda por inundación?
> Cuánto vive la consulta antes de declararse fallida, lo que acota hasta dónde se propaga y evita que circule para siempre.

> [!question]- ¿Por qué Proof of Work dificulta un ataque Sybil?
> Porque crear cada identidad cuesta cómputo: crear miles de identidades falsas se vuelve muy caro.

> [!question]- ¿Qué diferencia un ataque Sybil de uno Eclipse?
> Sybil multiplica identidades falsas para ganar peso en la red; Eclipse aísla a un nodo específico rodeándolo de vecinos maliciosos para controlar lo que ve.
