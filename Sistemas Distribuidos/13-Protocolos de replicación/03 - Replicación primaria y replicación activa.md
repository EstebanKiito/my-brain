---
ramo: "Sistemas Distribuidos"
tema: "Protocolos de replicación"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[02 - Replicación basada en quórum]]"
---

# Replicación primaria y replicación activa

Hay dos formas opuestas de decidir **quién** procesa cada operación. En la **replicación pasiva** (basada en primario), un solo nodo procesa todo y los demás copian el resultado. En la **replicación activa**, todos procesan todo, en el mismo orden. La primera es simple y consistente pero tiene un cuello de botella; la segunda no tiene un punto único de falla, pero coordina mucho.

## Basada en primario (replicación pasiva)

![Replicación basada en un primario](adjuntos/Replicaci%C3%B3n%20basada%20en%20un%20primario.png)

> [!example]- Transcripción de la imagen
> Un cliente hace `Write(A) = 5` y otro `Read(A)`; ambos se conectan solo al nodo primario, al centro, que a su vez está conectado con cinco réplicas secundarias.

- Un único **gestor primario** recibe todas las solicitudes de los clientes.
- El primario **ejecuta** las operaciones (sobre todo las escrituras) y **propaga el nuevo estado** a los secundarios (*backups*).
- Si el primario falla, se **elige** un secundario como nuevo primario.

**Consistencia:**

- Si leer y escribir pasa solo por el primario, hay **consistencia fuerte**.
- Tras una caída, se mantiene solo si el nuevo primario recibió y aplicó todas las actualizaciones previas a la falla.
- Si los clientes pueden leer de los secundarios (variante común), ya no es fuerte, pero sí **secuencial**.

| Ventajas | Desventajas |
|---|---|
| Escrituras consecutivas eficientes: se empaquetan y se envía solo el estado final | El primario es un **cuello de botella** |
| Relajando la consistencia, las lecturas van a los secundarios y alivian al primario | Tolerancia a fallos limitada |
| Maneja bien operaciones **no deterministas**: se ejecutan una vez y se replica el resultado | |

## Replicación activa (*replicated-write*)

![Replicación activa entre todos los nodos](adjuntos/Replicaci%C3%B3n%20activa%20entre%20todos%20los%20nodos.png)

> [!example]- Transcripción de la imagen
> Seis réplicas conectadas todas con todas. Un cliente hace `Write(A) = 5` en una réplica y otro hace `Read(A)` en otra.

- **Todas** las réplicas están activas y procesan las solicitudes de forma concurrente.
- Para que coincidan, se usa **Totally Ordered Multicast** (TOM): cada operación recibe un **número de secuencia global** (asignado por un coordinador o por consenso), y cada nodo ejecuta las operaciones en ese orden.
- Algunas variantes usan quórum para que no todas las réplicas tengan que aceptar cada operación.

**Consistencia:** el orden total no es necesariamente el del tiempo real en que los clientes hicieron sus solicitudes, así que **no** hay consistencia fuerte (con relojes físicos sincronizados se podría acercar, según la red). Si los clientes no se comunican entre sí mientras esperan, TOM garantiza consistencia **secuencial**.

| Ventajas | Desventajas |
|---|---|
| Alta tolerancia a fallos, sin punto único de falla | Costo de coordinación alto |
| Se pueden enviar solo los **cambios**, no el estado completo (como los commits de Git) | Escalabilidad limitada y latencia de escritura alta |
| | Muchos mensajes, varios redundantes |

> [!warning] Operaciones no deterministas
> Si una operación depende de la hora o de un servicio externo, cada réplica activa la ejecuta por su cuenta y puede obtener un resultado distinto. Por eso, de los cuatro protocolos, la replicación activa es la que **no** garantiza que el cliente obtenga la respuesta esperada; la basada en primario la ejecuta una sola vez.

## En la industria

| Sistema | Protocolo |
|---|---|
| pBFT | Se inspira en la replicación activa para aceptar o no un cambio |
| Azure SQL Database | Basado en primario, asíncrono, con hasta cuatro réplicas geográficas |
| MySQL Server | Basado en primario, asíncrono (responde antes de replicar) o síncrono (después) |
| Google File System | Basado en primario, pero exige que todas las réplicas completen la mutación antes de confirmar |
| Consul | Variante de gossip (SWIM) |
| Google Spanner | Quórum para escribir |
| Cassandra y Amazon Dynamo | Gossip para el estado de los nodos y quórum para las réplicas |

## Preguntas de repaso

> [!question]- ¿Por qué la replicación basada en primario maneja bien las operaciones no deterministas?
> Porque solo el primario ejecuta la operación y luego replica el **resultado**. Las réplicas no la vuelven a ejecutar, así que no pueden obtener valores distintos.

> [!question]- ¿Qué aporta el Totally Ordered Multicast a la replicación activa?
> Un número de secuencia global para cada operación, de modo que todas las réplicas las ejecutan en el mismo orden y terminan con el mismo estado.

> [!question]- Si en un sistema basado en primario los clientes leen de los secundarios, ¿qué consistencia se pierde y cuál queda?
> Se pierde la fuerte, porque un secundario puede no tener aún la última escritura. Queda la secuencial: todos ven las escrituras en el orden en que las aplicó el primario.
