---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/encapsulamiento
  - redes/switches
  - redes/routers
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física\|05 - Capas de transporte, red, enlace y física]]"
---

# Proceso de encapsulamiento y flujo de datos en la red

El encapsulamiento y desencapsulamiento sucesivo de cabeceras permite que los datos viajen a través de nodos intermediarios con diferentes profundidades en la pila de protocolos.

## Encapsulamiento y recorrido de paquetes (mis apuntes)

- ENCAPSULAMIENTO
- Tecnica para envio de mensajes
- El mensaje se divide en varios segmentos
- La capa de trasnporte les pone headers, info relevante para capa de transporte
- La capa de transporte se lo pasa a la capa de red, como PAQUETE de Red o Datagrama → Se le agrega un header de la capa de red
- La capa de enlace, le agrega su header (link header)
- Al final la capa fisica se encarga de transmitirlo
- Cuando el paquete fue enviado y llega a un switch, al ser un dispoisitvo de CAPA DE ENLACE
- SOLO TIENE 2 CAPAS: Enlace y fisica
- El enlace toma el mensaje, se lo transfiere a la capa fisica y este se lo envia a la siguiente dispositivo
- Llega al router, EL ROUTER Tiene 3 CAPAS: Red , Enlace y Fisica
- Aca llega a la parte fisica, lo pasa a la parte de enlace, en la parte de enlace se le QUITA EL HEADER, Y en la capa de red, analiza su HEADER, y decide que hacer → Borrar modificar etc
- Devuelta al las capas hacia abajo, hasta llegar a enviar al computador de destino, y subir en capas hasta la ultima
- EJEMPLO VISUAL

> [!warning] Posible error
> En los apuntes aparecen erratas en `trasnporte` (transporte) y `dispoisitvo` (dispositivo).

> [!tip] Complemento: Ciclo de encapsulamiento y desencapsulamiento
> ![Proceso de encapsulamiento y recorrido a través de capas de red](adjuntos/Proceso%20de%20encapsulamiento%20y%20recorrido%20a%20través%20de%20capas%20de%20red.png)
>
> > [!example]- Transcripción de la imagen
> > **Diagrama de flujo de datos y niveles de procesamiento en nodos de red:**
> > 1. **Host emisor (5 capas):**
> >    - Aplicación: genera el mensaje de datos $M$.
> >    - Transporte: encapsula en un segmento agregando la cabecera de transporte $H_t$ (puertos origen/destino).
> >    - Red: encapsula en un datagrama agregando la cabecera IP $H_n$ (IPs origen/destino).
> >    - Enlace: encapsula en una trama agregando la cabecera de enlace $H_l$ (MACs origen/destino) y un trailer de chequeo CRC.
> >    - Física: transmite los bits sobre el medio físico.
> > 2. **Switch de enlace (dispositivo de 2 capas):**
> >    - Procesa únicamente las capas Física y de Enlace.
> >    - Lee la cabecera de enlace $H_l$ para aprender o consultar la tabla MAC y conmutar la trama hacia el puerto correspondiente sin modificar el datagrama IP ni la cabecera de transporte.
> > 3. **Router de red (dispositivo de 3 capas):**
> >    - Procesa capas Física, Enlace y Red.
> >    - Desencapsula la trama retirando $H_l$, analiza la cabecera IP $H_n$ (decrementa el campo TTL y recalcula la suma de comprobación), consulta su tabla de reenvío, y encapsula el datagrama en una **nueva cabecera de enlace** $H_l'$ adecuada a la tecnología del siguiente salto.
> > 4. **Host receptor (5 capas):**
> >    - El paquete asciende por las capas retirando sucesivamente $H_l$, $H_n$ y $H_t$ hasta entregar el mensaje original $M$ al proceso de aplicación de destino.

## Preguntas de repaso

> [!question]- ¿Por qué la cabecera de enlace ($H_l$) cambia en cada salto entre routers mientras que la cabecera de red ($H_n$) permanece constante de origen a fin?
> Porque la cabecera de enlace contiene las direcciones físicas MAC válidas exclusivamente para el enlace local inmediato entre dos interfaces vecinas. La cabecera de red contiene las direcciones IP de origen y destino finales que identifican a los dos hosts de extremo a extremo a través de toda la Internet.

> [!question]- ¿Qué capas de la pila de protocolos implementa internamente un switch de capa 2?
> Un switch convencional implementa únicamente la capa física (Capa 1) y la capa de enlace de datos (Capa 2), siendo transparente para los protocolos de red y transporte.

> [!question]- ¿Qué modificación obligatoria realiza un router sobre la cabecera IP de red antes de reenviar un paquete al siguiente salto?
> Decrementa en 1 el campo de tiempo de vida (TTL, *Time to Live*) del paquete para evitar que circule indefinidamente en caso de bucles de enrutamiento, y recalcula la suma de comprobación de la cabecera (*Header Checksum*). Si el TTL llega a cero, el router descarta el paquete y emite un mensaje ICMP *Time Exceeded* al emisor.

