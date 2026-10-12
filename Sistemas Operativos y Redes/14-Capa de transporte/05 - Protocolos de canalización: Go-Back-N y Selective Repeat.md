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
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)|04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)]]"
---

# Protocolos de canalización: Go-Back-N y Selective Repeat

[[14-Capa de transporte/04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)|rdt 3.0]] funciona, pero envía un paquete a la vez y espera su ACK (*stop-and-wait*), así que desperdicia casi todo el enlace. La solución es enviar **una serie de paquetes seguidos**, en modo ***pipeline***, sin esperar cada ACK. Eso exige más:

- números de secuencia **incrementales** (ya no basta 1 bit);
- **buffers** en el emisor y en el receptor;
- una política para cuando se pierde un paquete intermedio: **cuánto retroceder**. Hay dos enfoques, Go-Back-N y Selective Repeat.

## La ventana

El emisor puede tener hasta **N paquetes sin ACK**: $N$ es el **tamaño de la ventana** (*window size*).

- **base**: el número de secuencia más antiguo sin ACK;
- **nextseqnum**: el próximo número de secuencia a usar.

La ventana cubre los números $[base,\ base + N - 1]$.

![Protocolo de canalización Go-Back-N con ventana deslizante en emisor](adjuntos/Protocolo%20de%20canalizaci%C3%B3n%20Go-Back-N%20con%20ventana%20deslizante%20en%20emisor.png)

> [!example]- Transcripción de la imagen
> Una fila de números de secuencia. A la izquierda, en verde, los que ya tienen *ACK recibidos*. Desde **base** ("Núm. Sec. más antiguo sin ACK"), en amarillo, los de *ACK pendientes*. Desde **nextseqnum** ("Próximo número de secuencia a usar"), en azul, los *usables, aún no enviados*. Los de la derecha, en blanco, son *no usables*. Entre base y el final de los azules está el *tamaño de ventana N*.

## Go-Back-N

- El receptor envía un **ACK por el último paquete recibido correctamente en orden** (ACK acumulativo); descarta los que llegan fuera de orden.
- El emisor usa **un timer**, para el paquete **más antiguo sin ACK**.
- Si el timer expira, **retransmite todo el grupo sin ACK**: vuelve atrás N.

![Diagrama de flujo y ventana deslizante en protocolo Go-Back-N](adjuntos/Diagrama%20de%20flujo%20y%20ventana%20deslizante%20en%20protocolo%20Go-Back-N.png)

> [!example]- Transcripción de la imagen
> Con N = 4: el emisor envía pkt0, pkt1, pkt2 (se pierde, *X loss*) y pkt3, y espera. El receptor confirma pkt0 y pkt1 (ACK0, ACK1), pero al recibir pkt3 lo descarta y reenvía ACK1. Al recibir ACK0 y ACK1, el emisor envía pkt4 y pkt5, que también se descartan con ACK1. Al expirar el timeout de pkt2, el emisor reenvía pkt2, pkt3, pkt4 y pkt5, que ahora se entregan (ACK2, ACK3…).

Los ACK que devuelve el receptor siguen siendo **ACK 1** mientras no reciba pkt2: hasta que no lo reciba, no confirma nada nuevo.

## Selective Repeat

- **Emisor y receptor** tienen ventana.
- El receptor envía **ACK por cada paquete individual** y **guarda en buffer** los que llegan fuera de orden.
- El emisor tiene **un timer por cada paquete sin ACK** y, si expira, **solo retransmite ese paquete** (no todos).
- El receptor **no avanza su ventana** hasta recibir el paquete que falta; cuando llega, entrega todo el bloque.

![Protocolo Selective Repeat con ventanas en emisor y receptor](adjuntos/Protocolo%20Selective%20Repeat%20con%20ventanas%20en%20emisor%20y%20receptor.png)

> [!example]- Transcripción de la imagen
> **a) Vista del transmisor**: desde *send_base* hasta *send_base + N*, mezcla de *ACK pendientes* (amarillo) y *con ACK recibidos* (verde, también dentro de la ventana), y luego *usable, aún no enviados* desde *nextseqnum*. **b) Vista del receptor**: desde *rcv_base*, el *esperado, aún no recibido* (gris), los *fuera de orden (almacenados) con ACK enviado* (rosado) y los *aceptables (en ventana)* (azul).

![Diagrama de eventos y buffers en protocolo Selective Repeat](adjuntos/Diagrama%20de%20eventos%20y%20buffers%20en%20protocolo%20Selective%20Repeat.png)

> [!example]- Transcripción de la imagen
> Con N = 4 y la ventana `0 1 2 3 4 5 6 7 8 9` sobre cada lado: se pierde pkt2. El receptor guarda pkt3, pkt4 y pkt5 (*buffered*) y envía ACK3, ACK4 y ACK5. Al expirar el timeout de pkt2, el emisor reenvía **solo pkt2**; cuando llega, el receptor entrega pkt2, pkt3, pkt4 y pkt5 juntos, y su ventana salta a 6-9. Al llegar ACK3, el emisor no envía nada nuevo (ya estaba confirmado).

```python
def simular(total, N, perdido, selectivo):
    """N paquetes en vuelo; 'perdido' se pierde la primera vez que se envía."""
    envios, aceptados = [], set()
    base, sig, ya_perdido = 0, 0, False
    while base < total:
        while sig < min(base + N, total):             # enviar mientras haya ventana
            envios.append(sig)
            if sig == perdido and not ya_perdido:
                ya_perdido = True                     # se pierde en el camino
            elif selectivo or sig == len(aceptados):  # GBN solo acepta en orden; SR guarda todo
                aceptados.add(sig)
            sig += 1
        if base in aceptados:                         # ACK de la base: la ventana se desliza
            base += 1
        elif selectivo:                               # timeout en SR: solo el que falta
            envios.append(base); aceptados.add(base)
        else:                                         # timeout en GBN: todo desde la base
            for p in range(base, sig):
                envios.append(p); aceptados.add(p)
    return envios

print(simular(10, 4, 2, selectivo=False))  # 0..5, luego 2 3 4 5, luego 6..9 -> 14 envíos
print(simular(10, 4, 2, selectivo=True))   # 0..5, luego solo 2, luego 6..9  -> 11 envíos
```

| | Go-Back-N | Selective Repeat |
|---|---|---|
| ACK | Acumulativo (último en orden) | Individual por paquete |
| Fuera de orden | Se descarta | Se guarda en buffer |
| Timers | Uno (el paquete más antiguo) | Uno por paquete |
| Al expirar | Reenvía todo desde la base | Reenvía solo ese paquete |

En Selective Repeat, si los números de secuencia se reutilizan módulo $K$, la ventana debe cumplir $N \le K/2$: si no, el receptor podría confundir un paquete nuevo con un duplicado viejo del mismo número.

Implementando estas ideas nace [[06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|TCP]], que combina ambos: ACK acumulativos como Go-Back-N, pero guardando en buffer lo que llega fuera de orden, y con la opción de ACK selectivos (SACK, RFC 2018).

## Preguntas de repaso

> [!question]- ¿Qué problema de rdt 3.0 resuelve el pipelining y qué exige?
> Que el emisor pase casi todo el tiempo esperando ACKs. Permite tener hasta N paquetes en vuelo, y para eso exige números de secuencia incrementales y buffers en emisor y receptor.

> [!question]- En Go-Back-N con N = 4, si se pierde pkt2, ¿qué se retransmite?
> Todo lo enviado desde la base: pkt2, pkt3, pkt4 y pkt5, porque el receptor descartó los que llegaron fuera de orden.

> [!question]- ¿Por qué Selective Repeat retransmite menos?
> Porque el receptor guarda los paquetes fuera de orden y confirma cada uno: el emisor solo reenvía el que no recibió ACK.

> [!question]- ¿Cuándo avanza la ventana del receptor en Selective Repeat?
> Solo cuando recibe el paquete esperado (el de la base); en ese momento entrega ese paquete y todos los que tenía guardados a continuación.
