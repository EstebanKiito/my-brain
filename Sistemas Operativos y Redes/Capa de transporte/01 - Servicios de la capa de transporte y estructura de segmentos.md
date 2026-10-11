---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - capa-de-transporte
  - segmentos
  - multiplexacion
prerrequisitos:
  - "[[Capa de aplicación y sockets/_Índice|Capa de aplicación y sockets]]"
---

# Servicios de la capa de transporte y estructura de segmentos

La capa de transporte proporciona comunicación lógica directa entre procesos de aplicación que se ejecutan en diferentes sistemas finales (*hosts*). A diferencia de la capa de red, que enruta paquetes entre computadores físicos (*host-to-host*), la capa de transporte extiende la entrega de datos hasta el nivel de proceso (*process-to-process*) mediante la segmentación y multiplexación por puertos.

---

## Servicios y agentes de transporte (mis apuntes)

### CONTENIDO 10 → CAPA DE TRANSPORTE

CAPA TRANSPORTE : Transmision Origen - Destino
- Se encuentra entre la Capa de APLICACION y la de NETWORK
- NO VIVE en los SERVIDORES intermedios, el objetivo es que llegue de un emisor a un receptor

![Servicios y responsabilidades de la capa de transporte en sistemas finales](adjuntos/Servicios%20y%20responsabilidades%20de%20la%20capa%20de%20transporte%20en%20sistemas%20finales.png)

> [!example]- Transcripción de la imagen
> La capa de transporte en la arquitectura de red:
> - Reside exclusivamente en los hosts terminales (emisor y receptor); los conmutadores y enrutadores del núcleo de red solo procesan las capas física, de enlace y de red.
> - El emisor divide los mensajes de aplicación en segmentos y los entrega a la capa de red (IP).
> - El receptor reensambla los segmentos recibidos y entrega los mensajes a los procesos de aplicación.

Existen 2 Agentes importantes
- lo divide en SEGMENTOS
- Solicita a capa de RED que ENVÍE los segmentos al Receptor
- Emisor: Recibe un mensaje de CAPA APLICACION,
- los Ensambla para formar mensaje
- Lo entrega a la CAPA APLICACIÓN
- Receptor: Recibe Segmentos,

PROTOCOLOS
- Establecimiento de conexión.
- TCP: Entrega confiable y ordenada. Control de flujo.
- UDP: Entrega no confiable y desordenada. Más rápida.
- (información que quiero enviar desde la capa de aplicacion por ej un Html con cierto header que me va a llevar a ejecutar ciertas reglas que tenga en el protocolo)

![Estructura de un segmento de transporte con datos y cabeceras](adjuntos/Estructura%20de%20un%20segmento%20de%20transporte%20con%20datos%20y%20cabeceras.png)

> [!example]- Transcripción de la imagen
> Estructura genérica de una PDU de transporte (segmento):
> - Campos de cabecera (*header fields*): Puerto de origen, puerto de destino, números de secuencia/confirmación y flags de control.
> - Carga útil (*payload* o datos): Contiene el mensaje completo o fragmentado proveniente de la capa de aplicación.

- Se Transmiten Segmentos
- El protocolo solo lo ejecuta origen y destino (NO INTERMEDIARIOS como ROUTERS, etc)

SEGMENTOS
Segmentos se transmiten en paquetes IP, podemos identificarlos mensajes de sitntos procesos con Puertos
- Puerto → Permite identificar procesos del nodo emisor o receptor
- Multiplexar mensajes

![Proceso de multiplexación y desmultiplexación de segmentos mediante puertos](adjuntos/Proceso%20de%20multiplexación%20y%20desmultiplexación%20de%20segmentos%20mediante%20puertos.png)

> [!example]- Transcripción de la imagen
> Multiplexación y desmultiplexación:
> - Multiplexación en el emisor: Recopila datos de múltiples sockets de aplicación, añade los encabezados de transporte correspondientes y los pasa a la capa de red.
> - Desmultiplexación en el receptor: Examina los campos de puerto del encabezado de transporte para entregar los datos entrantes al socket correcto del proceso destinatario.

> [!tip] Complemento de clase: Relación entre transporte y red
> Mientras que la capa de red (IP) brinda un servicio de "mejor esfuerzo" (*best-effort*) no confiable entre hosts, los protocolos de transporte pueden construir garantías más estrictas por encima de IP (como la confiabilidad absoluta y control de congestión en TCP), o bien proporcionar una interfaz ligera y directa sin sobrecarga (UDP).

---

## Preguntas de repaso

> [!question]- ¿Por qué los routers del núcleo de red no ejecutan protocolos de la capa de transporte?
> Porque los routers solo requieren inspeccionar las cabeceras de la capa de red (direcciones IP) para enrutar paquetes; mantener estado de conexiones de transporte en los enrutadores saturaría la memoria y destruiría la escalabilidad de Internet.

> [!question]- ¿Cuál es la diferencia fundamental entre la entrega *host-to-host* y *process-to-process*?
> *Host-to-host* (capa de red) solo garantiza llevar paquetes desde una máquina física hacia otra; *process-to-process* (capa de transporte) identifica exactamente a cuál de los múltiples procesos o hilos que corren concurrentemente en la máquina receptora le corresponde la información.

> [!question]- ¿Qué campos mínimos debe incluir la cabecera de cualquier segmento de transporte para permitir la desmultiplexación?
> El número de puerto de origen (para saber a dónde responder) y el número de puerto de destino (para saber a qué socket local entregar el paquete en el receptor).

