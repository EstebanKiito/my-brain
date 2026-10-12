---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - udp
  - datagramas
  - checksum
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/02 - Multiplexación y desmultiplexación de puertos en UDP y TCP|02 - Multiplexación y desmultiplexación de puertos en UDP y TCP]]"
---

# Protocolo UDP: datagramas, sobrecarga y checksum

**UDP** (*User Datagram Protocol*, definido en el RFC 768) es el protocolo de transporte más simple: agrega a IP poco más que los puertos. No promete nada, y precisamente por eso es rápido y liviano. Sirve cuando la aplicación prefiere la velocidad a la garantía de entrega, o cuando quiere controlar ella misma cómo envía.

## Qué ofrece (y qué no)

- Servicio de **"mejor esfuerzo"** (*best-effort*): los segmentos **pueden perderse** y **pueden llegar en distinto orden**.
- **No orientado a conexión** (*connection-less*): no se establece conexión previa y **no mantiene estado** de conexión. **Cada segmento se gestiona de forma independiente.**
- **Solo 8 bytes de overhead** por segmento.

Para llegar al host correcto se necesita la IP, pero de eso se encarga la capa de abajo (red); UDP solo agrega los puertos para llegar al proceso.

## El segmento UDP: 4 campos

![Proceso de multiplexación y desmultiplexación de segmentos mediante puertos](adjuntos/Proceso%20de%20multiplexaci%C3%B3n%20y%20desmultiplexaci%C3%B3n%20de%20segmentos%20mediante%20puertos.png)

> [!example]- Transcripción de la imagen
> Formato del segmento UDP, en filas de **32 bits**: *Source port #* y *Dest. port #*; *Length* y *Checksum*; y luego *Application data (message)*.

| Campo | Tamaño | Para qué sirve |
|---|---|---|
| Puerto de origen | 16 bits | A dónde responder |
| Puerto de destino | 16 bits | A qué proceso entregar |
| Longitud | 16 bits | Tamaño del segmento (header + datos) |
| Checksum | 16 bits | Detectar errores |

Cuatro campos de 2 bytes: **8 bytes** de header, frente a los **20 bytes** mínimos de TCP.

## ¿Por qué usar UDP?

- La **aplicación controla directamente** el envío: decide qué y cuándo enviar, sin que el protocolo retransmita o retenga datos.
- **No hay demora** en establecer conexión: menor overhead de tiempo.
- **No se reservan recursos** para mantener conexiones.
- **Menor overhead de espacio**: 8 bytes frente a 20.

Por eso lo usan, por ejemplo, DNS y el streaming de audio o video. Si una aplicación sobre UDP necesita confiabilidad, tiene que implementarla ella misma; es lo que hace QUIC, el protocolo bajo HTTP/3.

## El checksum

El **checksum** sirve simplemente para ver si el segmento llegó correcto. El emisor suma el segmento como palabras de 16 bits, sumando el acarreo al final (suma en complemento a 1), e invierte el resultado. El receptor suma todo, incluido el checksum: si da **todos unos**, no detectó errores. Si no coincide, **el segmento se descarta**: UDP no pide retransmisión.

```python
def checksum(palabras):
    """Suma en complemento a 1 de palabras de 16 bits, invertida."""
    s = 0
    for w in palabras:
        s += w
        s = (s & 0xFFFF) + (s >> 16)          # el acarreo se suma al final
    return ~s & 0xFFFF

datos = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
c = checksum(datos)
print(f"{c:016b}")                            # 1011010100111101

s = 0                                         # receptor: datos + checksum
for w in datos + [c]:
    s += w; s = (s & 0xFFFF) + (s >> 16)
print(f"{s:016b}")                            # 1111111111111111 -> sin errores
```

Si en el camino cambia un solo bit de los datos, la suma del receptor ya no da todos unos y el segmento se descarta.

## Preguntas de repaso

> [!question]- ¿Qué significa que UDP sea de "mejor esfuerzo" y sin conexión?
> Que no garantiza la entrega ni el orden de los segmentos, y que no establece conexión ni guarda estado: cada segmento se maneja por su cuenta.

> [!question]- ¿Qué campos tiene el header UDP y cuánto mide?
> Puerto de origen, puerto de destino, longitud y checksum, de 16 bits cada uno: 8 bytes en total.

> [!question]- ¿Por qué una aplicación elegiría UDP en vez de TCP?
> Porque no hay demora para establecer conexión, el overhead es menor (8 bytes frente a 20), no se reservan recursos y la aplicación controla directamente qué y cuándo enviar.

> [!question]- ¿Qué hace el receptor UDP si el checksum no coincide?
> Descarta el segmento; UDP no pide retransmisión.
