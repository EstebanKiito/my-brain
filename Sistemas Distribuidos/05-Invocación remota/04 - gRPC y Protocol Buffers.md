---
ramo: "Sistemas Distribuidos"
tema: "Invocación remota"
tags:
  - sd/invocacion-remota
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - RPC y stubs]]"
---

# gRPC y Protocol Buffers

XML-RPC es fácil de leer, pero sus mensajes son grandes y lentos de procesar. Entre servicios que intercambian millones de llamadas eso pesa. **gRPC** es la implementación moderna de RPC creada por Google en 2015: mismo modelo de stubs, pero con un transporte más eficiente y una serialización binaria compacta, **Protocol Buffers**.

## Qué aporta gRPC

- Es una implementación específica de **RPC**, publicada por Google en 2015.
- Usa un protocolo de comunicación más rápido y eficiente: **HTTP/2**.
- Admite varios formatos de serialización: **Protocol Buffers** (el habitual), JSON y XML.
- Es abierto, y por eso lo adoptó gran parte de la industria para la comunicación entre microservicios.

![Arquitectura de gRPC entre dos servicios](adjuntos/Arquitectura%20de%20gRPC%20entre%20dos%20servicios.png)

> [!example]- Transcripción de la imagen
> Una *Client App* (web o móvil) se comunica con el *Order Service* usando JSON. El *Order Service* y el *Payment Service* tienen las mismas capas: aplicación, *Encoding/Decoding*, *gRPC Runtime* y *Transport*. Entre ellos, los datos viajan codificados en binario con ProtoBuf (*Binary Encoding - ProtoBuf*) sobre HTTP 2.

## Protocol Buffers en cuatro pasos

1. Se define la **estructura de los datos** en un archivo de esquema (`.proto`).
2. Protocol Buffers **genera código** en el lenguaje deseado, con la estructura lista para importar.
3. Se **instancian** los datos usando esa estructura.
4. Se **serializan** a binario para transmitirlos, y se **deserializan** al recibirlos.

```protobuf
// character.proto
syntax = "proto3";

message Character {
  string username = 1;
  string phrase = 2;
}
```

Los números `= 1` y `= 2` no son valores por defecto, sino **números de campo**: identifican cada campo en el binario, en lugar de escribir su nombre.

```bash
python -m grpc_tools.protoc -I. --python_out=. character.proto   # genera character_pb2.py
```

```python
import character_pb2   # módulo generado por protoc a partir de character.proto

character = character_pb2.Character()
character.username = "Anya"
character.phrase = "Waku Waku"

with open("data.anya", "wb") as file:
    file.write(character.SerializeToString())

character_new = character_pb2.Character()
with open("data.anya", "rb") as file:
    character_new.ParseFromString(file.read())
print(character_new.username, "-", character_new.phrase)   # Anya - Waku Waku
```

El archivo resultante pesa **17 bytes**: por cada campo, un byte con su número y su tipo, un byte con el largo y el texto. El mismo dato en JSON (`{"username": "Anya", "phrase": "Waku Waku"}`) ocupa más del doble.

> [!tip] Por qué es más rápido
> Los nombres de los campos no viajan (solo sus números), los datos van en binario y el código generado sabe exactamente cómo leerlos. Menos bytes por la red y menos trabajo al parsear.

> [!warning] El esquema es un contrato
> Ambos lados deben compartir el `.proto`. Cambiar el número de un campo rompe la compatibilidad con los mensajes antiguos; por eso los campos nuevos se agregan con números nuevos y los viejos no se reutilizan.

| | XML-RPC | gRPC |
|---|---|---|
| Transporte | HTTP/1.1 | HTTP/2 |
| Serialización | XML (texto) | Protocol Buffers (binario), JSON o XML |
| Contrato | Implícito (nombres de función) | Explícito (archivo `.proto`) |
| Legibilidad | Alta | Baja (binario) |

## Preguntas de repaso

> [!question]- ¿Para qué sirven los números de campo en un archivo `.proto`?
> Identifican cada campo dentro del mensaje binario. Gracias a ellos los nombres no viajan, lo que reduce el tamaño, y los mensajes siguen siendo compatibles mientras no se cambien los números.

> [!question]- ¿Qué ventajas tiene gRPC frente a XML-RPC, y qué se pierde?
> Gana velocidad y tamaño (HTTP/2 y serialización binaria) y un contrato explícito con generación de código. Pierde legibilidad: los mensajes no se pueden leer ni depurar a simple vista.

> [!question]- En la arquitectura de la imagen, ¿por qué la app cliente usa JSON y los servicios internos, ProtoBuf?
> Porque la app (navegador o móvil) se integra mejor con JSON sobre HTTP, mientras que entre servicios internos, que intercambian muchas llamadas y comparten el esquema, conviene el formato binario más eficiente.
