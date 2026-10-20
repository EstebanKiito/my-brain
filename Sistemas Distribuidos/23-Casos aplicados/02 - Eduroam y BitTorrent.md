---
ramo: "Sistemas Distribuidos"
tema: "Casos aplicados"
tags:
  - sd/seguridad
  - sd/p2p
  - origen/complemento
prerrequisitos:
  - "[[01 - VPN y Tor]]"
  - "[[02 - Tablas de hash distribuidas y Chord]]"
---

# Eduroam y BitTorrent

Dos sistemas cotidianos que resumen el ramo. **Eduroam** es una federación distribuida que autentica a millones de estudiantes en cualquier universidad del mundo; **BitTorrent** es una red P2P que reparte archivos enormes entre sus usuarios. Ambos combinan comunicación, coordinación, replicación y seguridad.

## Eduroam

- Red Wi-Fi internacional para instituciones educativas y de investigación.
- Es una **federación** de sistemas locales: cada institución es un componente independiente de la red distribuida.
- Separa dos roles:
  - **SP** (*Service Provider*): la institución **visitada**, que da el acceso físico a la red una vez autenticado el usuario.
  - **IdP** (*Identity Provider*): la institución **de origen**, que autentica a sus propios usuarios. Es un servidor de autenticación centralizado para su gente, pero distribuido a nivel global.
- Ambos se comunican con el protocolo **RADIUS**.

![Jerarquía RADIUS de Eduroam](adjuntos/Jerarqu%C3%ADa%20RADIUS%20de%20Eduroam.png)

> [!example]- Transcripción de la imagen
> El enrutamiento de las solicitudes RADIUS se basa en el nombre de usuario (`usuario@dominio`): el dominio (por ejemplo, `institución.tld`) dirige la solicitud al IdP correcto, de forma análoga a DNS. El diagrama muestra un servidor RADIUS de nivel superior (*eduroam top level*), servidores nacionales (`.home` y `.visit`) y los de cada institución; un usuario `john@institution.home` se conecta en la institución visitada y sus credenciales viajan en un túnel EAP-TTLS hasta su institución.

**Jerarquía RADIUS:**

1. **Servidor organizacional** (uc.cl, uchile.cl…): si el usuario es de la institución, lo autentica; si no, reenvía la solicitud.
2. **Federación nacional** (eduroam.cl en Chile): si reconoce el dominio, reenvía al servidor de esa institución; si no, sube al nivel global.
3. **Confederación global:** según el dominio (por ejemplo, @ox.ac.uk), envía la solicitud a la federación nacional que corresponde.

Como [[05 - Sistema de nombres de dominio (DNS) y resolución de consultas|DNS]], cada nivel solo sabe a quién preguntar después.

**Seguridad:**

- **Autenticación federada:** la autenticación ocurre en el IdP, no en el SP; una sola credencial sirve en todo el mundo, y el SP confía en el IdP.
- **Autorización:** autenticado el usuario, el SP le da acceso a la red y controla qué puede ver.
- **Confidencialidad:** las credenciales viajan cifradas en un túnel TLS, invisibles para el SP y los servidores RADIUS intermedios; solo el IdP las ve.
- **Monitoreo:** los RADIUS intermedios pueden registrar logs de autenticación, y el SP puede registrar tráfico, sin ver credenciales.

## BitTorrent

Red P2P para distribuir archivos grandes: se dividen en **piezas** pequeñas que los peers comparten directamente entre sí.

- **En sus inicios**, era P2P **no estructurado** con un **tracker** centralizado: un servidor que lleva la cuenta de qué peers tienen piezas del archivo.
- **Hoy es híbrido:** usa una **DHT** para que los peers encuentren otros peers sin depender del tracker (basta con encontrar uno activo), y **Peer Exchange** para intercambiar listas de peers. El tracker solo entrega los primeros contactos.

| Componente | Rol |
|---|---|
| **Archivo .torrent** | Metadatos: nombre y estructura, tamaño y **hash de cada pieza**, URL del tracker y otros campos |
| **Tracker** | Coordina: no transfiere archivos, solo informa qué peers comparten el mismo torrent |
| **Leechers** | Peers que descargan (y a la vez pueden subir piezas) |
| **Seeders** | Peers con el archivo completo, que solo lo comparten |
| **Swarm** | Todos los peers (leechers y seeders) de un mismo archivo, identificado por su hash |

**Riesgos:** un nodo malicioso puede enviar piezas corruptas (**peer poisoning**), sobre todo si el hash es débil; se pueden difundir archivos maliciosos "avalados" por muchos peers; y sin cifrado por defecto, los intermediarios pueden inspeccionar, limitar o censurar el tráfico.

**Defensas:**

- **Integridad por hash:** cada pieza se verifica con su hash.
- **Replicación** de las piezas en muchos nodos.
- **Incentivos:** con *choking/unchoking*, cada peer sube datos a quienes le corresponden (reciprocidad), lo que castiga a los *free-riders*; con el *optimistic unchoking*, cada tanto prueba un peer al azar para descubrir colaboradores.

| Propiedad | BitTorrent |
|---|---|
| Tolerancia a fallos | Alta: las piezas se replican en muchos nodos |
| Transparencia | Media: el usuario ve velocidad, peers, etc. |
| Acoplamiento | Temporal y referencial |
| Escalabilidad | Alta: los nodos entran y salen sin problema |
| Consistencia | Eventual: las piezas se propagan hasta que todos completan el archivo |

## Comparación final

![Comparación de VPN, Tor, Eduroam y BitTorrent](adjuntos/Comparaci%C3%B3n%20de%20VPN,%20Tor,%20Eduroam%20y%20BitTorrent.png)

> [!example]- Transcripción de la imagen
> | Aspecto | VPN | Tor | Eduroam | BitTorrent |
> |---|---|---|---|---|
> | Uso | Navegación segura | Navegación anónima | Acceso a Internet | Descarga de archivos |
> | Modelo | Cliente-servidor | P2P | Federación distribuida | P2P |
> | Cifrado | Canal cifrado hasta el servidor | Cifrado en capas (onion routing) | TLS | Parcial (en propuestas recientes) |
> | Autenticar | Proveedor VPN | No hay identidad visible | Autenticación federada (IdP) | No estándar, depende del cliente |
> | Privacidad | Media, el proveedor ve todo | Alta, no se conoce la IP del origen | Media, el SP ve el tráfico | Baja, sin cifrado por defecto |
> | Amenazas clave | Logging y servidor comprometido | Nodo de salida | Logs RADIUS | Peer poisoning, eavesdropping |

> [!warning] Afirmaciones falsas típicas
> "En Eduroam la autenticación y el servicio están centralizados en un solo servidor RADIUS": falso, están separados (IdP y SP) y la jerarquía es federada. "Tor y VPN son excluyentes": falso, se pueden combinar.

## Preguntas de repaso

> [!question]- ¿Por qué el SP de Eduroam no ve la contraseña del usuario visitante?
> Porque las credenciales viajan cifradas en un túnel TLS hasta el IdP de la institución de origen; el SP y los RADIUS intermedios solo reenvían el paquete.

> [!question]- ¿Cómo detecta BitTorrent una pieza corrupta?
> Comparando el hash de la pieza recibida con el que figura en el archivo .torrent; si no coincide, la descarta y la pide a otro peer.

> [!question]- ¿Qué aportó la DHT a BitTorrent?
> Encontrar peers sin depender del tracker: basta con conocer un peer activo para buscar al resto, lo que elimina el punto único de falla.
