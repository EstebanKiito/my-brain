---
ramo: "Sistemas Distribuidos"
tema: "Fundamentos de sistemas distribuidos"
tags:
  - sd/fundamentos
  - origen/complemento
prerrequisitos: []
---

# Qué es un sistema distribuido

Cuando un usuario abre `google.cl` ve un único sitio, pero detrás no hay un computador sino miles, repartidos por el mundo, que se coordinan para responder como si fueran uno. Ese es el objeto de estudio del ramo: cómo lograr que muchas máquinas independientes se comporten como un solo sistema ordenado, y qué problemas aparecen al intentarlo.

## Definición

El libro guía del curso (van Steen y Tanenbaum, *Distributed Systems*, 4.ª ed.) da dos definiciones que se complementan:

- Un **sistema distribuido** es una colección de sistemas informáticos en red donde los procesos y los recursos se extienden entre varias computadoras, con el fin de mejorar el rendimiento de un sistema individual en **fiabilidad**, **escalabilidad** y **eficiencia**.
- Vista desde el usuario: es una colección de computadoras independientes que **aparecen ante el usuario como una única computadora**.

La primera dice *para qué* se reparte el sistema; la segunda, *qué debe percibir* quien lo usa. Si una parte se cae, el usuario debería poder seguir usando el servicio sin enterarse.

> [!tip] La idea central
> Muchos nodos sin memoria compartida, conectados solo por mensajes, que cooperan para verse como un sistema único y más fiable que cualquiera de sus partes.

## El objetivo: orden entre muchos componentes

Las slides ilustran el problema con un servicio de fotos de viaje: el usuario pide sus fotos y el sistema, con siete servidores, no sabe cuál las tiene, así que responde "No hay fotos". Un sistema distribuido debe evitar ese caos y conseguir un orden interno. Para eso tiene que responder preguntas que en un solo computador no existen:

- ¿Los computadores están en un mismo lugar o repartidos por el mundo?
- ¿Cómo se ponen de acuerdo sobre una operación?
- ¿Cómo se coordina el tiempo si unos relojes son mejores que otros?
- ¿Cómo se evita que dos nodos se traslapen en una operación crítica?
- ¿Qué se hace ante la caída de nodos o una partición de la red?
- ¿Cómo se garantiza que los datos no se pierdan?

Cada pregunta corresponde a una unidad del ramo: comunicación, sincronización de relojes, consenso, exclusión mutua, tolerancia a fallos y replicación.

## Por qué importa hoy

Casi todos los servicios masivos son sistemas distribuidos:

- **Google** tiene pocos data centers, pero miles de **nodos de borde** (*edge nodes*) cerca de los usuarios, para que cada uno se conecte a un nodo próximo y la latencia sea baja.
- **Cloudflare** y **AWS** mantienen infraestructura en decenas de regiones.
- Un servicio de IA que genera imágenes recibe la petición en un nodo, que reparte el trabajo entre muchos computadores que trabajan por detrás.

![Data centers frente a edge nodes de Google](adjuntos/Data%20centers%20frente%20a%20edge%20nodes%20de%20Google.png)

> [!example]- Transcripción de la imagen
> Dos mapas del mundo. A la izquierda, *Data Centers*: unas treinta ubicaciones, concentradas en Estados Unidos y Europa, más algunas en Asia y una en Chile. A la derecha, *Edge Nodes*: miles de puntos amarillos que cubren casi todos los continentes. Fuente: Google Peering.

Entender estos sistemas permite evaluarlos con preguntas concretas: ¿estará siempre disponible?, ¿es confiable?, ¿qué pasa con los datos entre nodos?, ¿la información que entrega es consistente?

## Cada servicio prioriza algo distinto

| Ejemplo | Qué prioriza | Consecuencia |
|---|---|---|
| Dar *like* en Instagram desde el celular | Velocidad | El *like* puede tardar en aparecer en el computador |
| Transferencia bancaria | Consistencia | No puede haber desincronización entre sucursales |
| Buscacursos UC (vacantes) | No mentir | Funciona centralizado y es lento, pero las vacantes son exactas |

Esta tensión entre rapidez y consistencia reaparece en todo el ramo y se formaliza en [[04 - Escalamiento y teorema CAP|el teorema CAP]].

> [!warning] Distribuido no significa P2P
> Las redes [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) son un tipo de sistema distribuido conocido (ver [[06 - Redes Peer-to-Peer (P2P) y distribución con BitTorrent|Redes P2P y BitTorrent]]), pero no el único: un sistema distribuido también puede tener nodos servidores y clientes.

## Preguntas de repaso

> [!question]- ¿Por qué la definición insiste en que el sistema "aparezca como una única computadora"?
> Porque el usuario no debería tener que saber cuántos nodos hay ni a cuál se conectó. Si la distribución se nota (fotos que no aparecen, errores al caer un nodo), el sistema falla en su objetivo aunque internamente funcione.

> [!question]- ¿Qué gana Google al tener edge nodes además de sus data centers?
> Reduce la latencia: el usuario se conecta a un nodo cercano en vez de cruzar el mundo hasta un data center, y la carga se reparte entre muchos puntos.

> [!question]- ¿Por qué Buscacursos puede permitirse ser lento y un *like* de Instagram no necesita ser exacto?
> Porque priorizan cosas distintas: las vacantes son una variable concurrente donde mentir tiene costo real, así que se sacrifica velocidad por exactitud; un *like* retrasado no daña a nadie, así que se prioriza la rapidez.
