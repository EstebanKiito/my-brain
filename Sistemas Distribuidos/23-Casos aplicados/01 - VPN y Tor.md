---
ramo: "Sistemas Distribuidos"
tema: "Casos aplicados"
tags:
  - sd/seguridad
  - sd/p2p
  - origen/complemento
prerrequisitos:
  - "[[03 - Protocolos híbridos y TLS 1.3]]"
  - "[[01 - Redes P2P, búsqueda y ataques]]"
---

# VPN y Tor

Una **VPN** y **Tor** prometen lo mismo a primera vista: navegar de forma más privada. Pero se construyen de forma opuesta: la VPN confía en **un** proveedor que ve todo, y Tor reparte la confianza entre **varios** nodos voluntarios para que ninguno sepa a la vez quién es el usuario y a dónde va. Ambas son **redes superpuestas de seguridad** (*security overlay networks*).

## VPN (red privada virtual)

- Crea un **túnel seguro y privado** por Internet entre el usuario y el destino.
- **Cifra** los datos con protocolos VPN y **oculta la IP y la ubicación** del usuario.
- Ayuda a eludir censura, bloqueos de contenido y restricciones de sitios.
- Es una **overlay network**: construye una red virtual sobre la red subyacente, con protocolos de cifrado propios (IPsec, WireGuard) y funciones que la red base no tiene.

| Tipo | Uso |
|---|---|
| **Remote access** | Un usuario individual se conecta desde cualquier lugar a una red (con un cliente VPN); acceso seguro a recursos internos desde redes públicas |
| **Site-to-site** | Conecta dos o más redes completas (por ejemplo, dos sucursales) como si fueran una sola red privada |

Ver también [[08 - Navegación privada, VPN y proxy|Navegación privada, VPN y proxy]].

## Tor (*The Onion Router*)

- Red **P2P de anonimato** formada por nodos voluntarios.
- Usa **onion routing**: el mensaje se cifra en varias capas.
- Circuito de **3 nodos**: entrada → medio → salida. Cada nodo quita una capa y solo conoce al anterior y al siguiente.

![Onion routing en Tor](adjuntos/Onion%20routing%20en%20Tor.png)

> [!example]- Transcripción de la imagen
> Al igual que una VPN, Tor es una *security overlay network* que usa varias capas de cifrado (onion routing), de modo que ningún nodo tiene toda la información sobre el origen, el destino y el contenido. El diagrama muestra a Bob enviando un mensaje a Alice a través de tres nodos; el paquete lleva tres capas de cifrado (morada, verde y roja) que se van quitando en cada salto hasta que llega el dato sin cifrar al destino.

**Dos tipos de acceso:**

- A sitios normales (.cl, .com): el usuario es anónimo, pero el servidor es conocido.
- A sitios **.onion**: anonimato mutuo dentro de la red Tor (Facebook, por ejemplo, tiene una dirección .onion).

**Ventajas:** cifrado fuerte y alto anonimato. **Problemas:** el **nodo de salida** puede ver el tráfico si no está cifrado (HTTP), es más lento por la cantidad de saltos y es objetivo de vigilancia en algunos contextos.

## VPN frente a Tor

| Aspecto | VPN | Tor |
|---|---|---|
| Punto de falla | Único: el servidor VPN | Múltiples nodos independientes |
| Conexión | Directa entre cliente y servidor VPN | Circuito de 3 nodos |
| Riesgo | Confiar en el proveedor | Nodo de salida malicioso |
| Anonimato | El proveedor ve todo; el servidor final no | Alto: IP y ruta anónimas |
| Velocidad | Alta | Baja (varios saltos cifrados) |
| Escalabilidad | Limitada por el proveedor | Alta (P2P) |
| Uso | Navegación segura, contenido bloqueado | Anonimato, acceso a sitios .onion |

> [!warning] No se excluyen, ni lo tapan todo
> VPN y Tor se pueden combinar. Y una VPN no elimina el monitoreo: solo traslada la confianza al proveedor, que puede ver el tráfico.

## Preguntas de repaso

> [!question]- ¿Por qué en Tor ningún nodo conoce a la vez el origen y el destino?
> Porque cada nodo del circuito solo quita su capa de cifrado y ve al nodo anterior y al siguiente. El de entrada conoce al usuario pero no el destino; el de salida conoce el destino pero no al usuario.

> [!question]- ¿Cuál es el principal riesgo de una VPN?
> Tener que confiar en el proveedor: el servidor VPN ve todo el tráfico del usuario y es un punto único de falla.

> [!question]- ¿Por qué el nodo de salida de Tor puede ser peligroso?
> Porque descifra la última capa: si el usuario se conecta a un sitio sin TLS, el nodo de salida ve el contenido en claro.
