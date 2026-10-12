---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - go-back-n
  - selective-repeat
  - pipelining
  - ventana-deslizante
prerrequisitos:
  - "[[14-Capa de transporte/04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)|04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)]]"
---

# Protocolos de canalización: Go-Back-N y Selective Repeat

Para superar la ineficiencia del modelo *Stop-and-Wait*, los protocolos de transporte modernos implementan canalización (*pipelining*), permitiendo transmitir múltiples paquetes consecutivos sin esperar confirmaciones intermedias. Los dos enfoques fundamentales de ventana deslizante son **Go-Back-N (GBN)**, que utiliza confirmaciones acumulativas y retransmisión de grupo, y **Selective Repeat (SR)**, que gestiona confirmaciones individuales y almacenamiento en búfer receptor.

---

## Modelos de canalización (mis apuntes)

En la practica, no se manda solo un paquete, los protocolos funcionan con un modo STOP-WAIT
Envia una SERIE DE PAQUETES, en modo PIPELINED y ahi ver si uno falla, ver cuanto retrocedo
Usamos buffers, si se pierde un intermedio → Generara problemas

GO-BACK-N
Emisor puede mantener hasta N paquetes sin ACK
Receptor envia ACK por el ultimo paquete recibido CORRECTamente
Emisor usa un TIMER para parquete mas ANTIGUO SIN ACK
- Si el timer expira, se retrasmite → TODO EL GRUPO SIN ACK
- Base : El paquete mas antiguo sin ACK
- nextseqnum: Proximo numero de secuencia a usar
- Ejemplo con N = 4
- N es un WINDOW SIZE

![Protocolo de canalización Go-Back-N con ventana deslizante en emisor](adjuntos/Protocolo%20de%20canalización%20Go-Back-N%20con%20ventana%20deslizante%20en%20emisor.png)

> [!example]- Transcripción de la imagen
> Ventana deslizante en Go-Back-N (GBN):
> - `base`: Secuencia del paquete más antiguo transmitido y aún no confirmado.
> - `nextseqnum`: Próximo número de secuencia disponible para transmitir.
> - Tamaño de ventana $N$: Límite máximo de paquetes en vuelo sin confirmar (`[base, base + N - 1]`).

![Diagrama de flujo y ventana deslizante en protocolo Go-Back-N](adjuntos/Diagrama%20de%20flujo%20y%20ventana%20deslizante%20en%20protocolo%20Go-Back-N.png)

> [!example]- Transcripción de la imagen
> Flujo de paquetes en GBN: Si un paquete (ej. pkt2) se pierde, el receptor descarta silenciosamente los paquetes posteriores fuera de orden (pkt3, pkt4, pkt5) y reenvía repetidamente el ACK del último paquete consecutivo (ACK 1). Al expirar el timer de la base, el emisor retransmite todos los paquetes desde la base (`pkt2, pkt3, pkt4, pkt5`).

- Fijate que los Acks que devuelven el receptor, es 1 porque todavia no recibe el pkt2 (paquete 2), hasta que no lo reciba, no va a dar otro ACK

SELECTED-REPEAT
Tiene una ventana tanto en el emisor como en el Receptor
Recpetor No va a hacer avanzar la ventana, hasta que haya recibido todos los paquetes enviados del emisor

![Protocolo Selective Repeat con ventanas en emisor y receptor](adjuntos/Protocolo%20Selective%20Repeat%20con%20ventanas%20en%20emisor%20y%20receptor.png)

> [!example]- Transcripción de la imagen
> Ventanas en Selective Repeat (SR): Tanto el emisor como el receptor mantienen ventanas de tamaño $N$. El receptor almacena en búfer los paquetes que llegan fuera de orden en lugar de descartarlos, esperando los faltantes para entregar los datos en orden a la capa de aplicación.

- Emisor puede mantener hasta N paquetes sin ACK
- Receptor envia ACK para cada paquete Individual!

![Diagrama de eventos y buffers en protocolo Selective Repeat](adjuntos/Diagrama%20de%20eventos%20y%20buffers%20en%20protocolo%20Selective%20Repeat.png)

> [!example]- Transcripción de la imagen
> Flujo de Selective Repeat: Cada paquete tiene su propio temporizador lógico en el emisor. Al expirar un timeout, únicamente se retransmite el paquete específico no confirmado. Cuando el paquete rezagado llega, el receptor avanza su ventana y entrega todo el bloque consecutivo.

- Emisor cuando recibe el ACK 0, avanza la ventana hacia el 1
- Receptor no mueve la ventana si no recibe cierto paquete
- Cuando se perdio el 2, el 3 4 y 5 ya habian sido enviados, por ende cuando lo reciba, la ventana avanza 2 3 4 5 → 6 7 8 9
- En caso de timer expirado → SOLO SE RETRANSMITEN PAQUETES SIN ACK
- (NO TODOS)!!!
- Emisor usa TIMER para paquete mas antiguo
Implementando estas cosas → Nace TCP

> [!tip] Complemento de clase: Tamaño de ventana y espacio de secuencias en SR
> En Selective Repeat, para evitar ambigüedades entre paquetes nuevos y duplicados con el mismo número de secuencia circular, el tamaño de ventana $N$ debe satisfacer $N \le \frac{1}{2} \cdot \text{Espacio de Secuencia}$. Si se usan números de secuencia módulo $K$, entonces $N \le K/2$.

---

## Preguntas de repaso

> [!question]- ¿Por qué Go-Back-N descarta los paquetes recibidos fuera de orden aunque no tengan errores de bit?
> Porque el receptor GBN no mantiene búfer de recepción; al no poder almacenar paquetes fuera de orden, simplifica el diseño del receptor exigiendo únicamente recordar el número de secuencia del próximo paquete esperado.

> [!question]- ¿Cuál es la principal ventaja de Selective Repeat frente a Go-Back-N en enlaces con alta tasa de pérdida?
> La eficiencia de ancho de banda: solo retransmite los paquetes individuales que realmente se perdieron, evitando el reenvío redundante de decenas de paquetes que el receptor ya había recibido correctamente.

> [!question]- ¿Cómo se compara el mecanismo de confirmación de TCP con GBN y Selective Repeat?
> TCP es un híbrido: utiliza confirmaciones acumulativas (*Cumulative ACKs*) y un solo temporizador como GBN, pero almacena paquetes fuera de orden en un búfer receptor y soporta confirmaciones selectivas (SACK, RFC 2018) similar a Selective Repeat.

