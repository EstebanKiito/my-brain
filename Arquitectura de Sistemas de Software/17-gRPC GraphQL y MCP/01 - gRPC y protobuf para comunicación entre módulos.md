---
ramo: "Arquitectura de Sistemas de Software"
tema: "gRPC GraphQL y MCP"
tags:
  - arquisis/integracion
  - arquisis/grpc
  - origen/complemento
prerrequisitos:
  - "[[05 - OpenAPI y límites de REST]]"
  - "[[04 - gRPC y Protocol Buffers]]"
---

# gRPC y protobuf para comunicación entre módulos

REST es lento para la comunicación intensa entre servicios: mensajes en texto, headers repetidos y un recurso completo por petición. **gRPC** resuelve eso volviendo a la idea de **llamar funciones remotas** como si fueran locales, con mensajes **binarios y tipados**. Es la respuesta esperada cuando el enunciado pide latencia mínima o mucha comunicación entre módulos.

## Qué es

**gRPC** es la implementación de RPC (*Remote Procedure Call*) de Google:
- **El servidor define funciones y el cliente las llama** como objetos nativos de su lenguaje.
- Funciona **sobre HTTP/2**. En el navegador se usa a través de gRPC-Web o Connect, porque no es web-nativo.
- Usa **Protocol Buffers (protobuf)** para **serializar** los datos en binario y para definir **APIs estrictamente tipadas**.
- Privilegia la **velocidad y la eficiencia** por sobre la legibilidad.
- Ofrece **streams** y **comunicación bidireccional**: el servidor puede enviar varias respuestas a una sola petición, y ambos lados pueden enviar mensajes a la vez.

El contrato se escribe en un archivo `.proto` y se compila para cada lenguaje:

```protobuf
syntax = "proto3";
service Inventario {
  rpc Reservar (ReservaRequest) returns (ReservaResponse);          // unaria
  rpc VigilarStock (ProductoId) returns (stream NivelStock);        // streaming del servidor
}
message ReservaRequest { string producto_id = 1; int32 cantidad = 2; }
message ReservaResponse { bool ok = 1; string reserva_id = 2; }
message ProductoId { string id = 1; }
message NivelStock { string id = 1; int32 disponible = 2; }
```

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inventario.proto
```

La compilación genera los mensajes y los **stubs**. El ejemplo mínimo típico tiene tres archivos: `unary.proto` (el contrato y cómo compilarlo), `unary_server.py` (implementa la función) y `unary_client.py` (la llama a través del stub). El servidor implementa `Reservar` y el cliente llama `stub.Reservar(...)` como si fuera una función local. Como el contrato está en protobuf, un servidor escrito en C++ puede atender clientes en Ruby, Java o Python sin que nadie escriba código de serialización.

![Servidor gRPC en C++ con clientes en Ruby y Android-Java](adjuntos/Servidor%20gRPC%20con%20clientes%20en%20otros%20lenguajes.png)

> [!example]- Transcripción de la imagen
> - Un **gRPC Server** dentro de un **C++ Service**.
> - Dos clientes, un **Ruby Client** y un **Android-Java Client**, cada uno con su **gRPC Stub**.
> - Cada stub envía un **Proto Request** al servidor. El cliente Ruby recibe un **Proto Response**, y el cliente Android recibe **Proto Response(s)**, en plural, porque la llamada es de streaming.

## Pros y contras

| Pros | Contras |
|---|---|
| **Velocidad**: binario, conexiones HTTP/2 persistentes y multiplexadas | **Atado a RPC y no web-nativo**: el navegador necesita un proxy o adaptador |
| **Llamadas versátiles**: unarias, 1-n y streaming bidireccional | **Protocolo no humano**: no se puede leer ni probar con un navegador o un `curl` simple |
| **Múltiples lenguajes** desde un mismo `.proto` | **Pobre con mensajes grandes** (megabytes o más) |
| **Tipado estricto**: errores de contrato en compilación | **Curva de aprendizaje** y coordinación para compartir y versionar los `.proto` |

## Dónde usarlo

- **Comunicación entre módulos de alta velocidad**: dentro de un bounded context grande o en un cúmulo de microservicios del mismo equipo.
- Requisitos de **latencia mínima**.
- Necesidad de **serialización eficiente** (mucho volumen de mensajes pequeños, dispositivos con poco ancho de banda).

> [!tip] Regla: dentro del contexto, eficiencia; entre contextos, independencia
> Dentro de un contexto, los módulos pertenecen al mismo equipo y comparten el modelo, así que gRPC compra velocidad a un costo bajo de acoplamiento. Entre contextos importa más la independencia: un contrato REST/OpenAPI o eventos en un MOM permiten que cada equipo evolucione a su ritmo. Compartir `.proto` entre contextos funciona como un Shared Kernel.

> [!warning] gRPC no es "REST más rápido" para todo
> Para una API pública consumida por terceros o navegadores, REST sigue siendo más adecuado: es legible, web-nativo y tiene caché HTTP. gRPC se justifica por **latencia, volumen o streaming**, y hay que decirlo explícitamente en la respuesta.

## Preguntas de repaso

> [!question]- ¿Qué aporta protobuf a gRPC?
> Serialización binaria compacta, que es más rápida y liviana que JSON, y un contrato tipado en el archivo `.proto` desde el cual se generan los mensajes y los stubs en cada lenguaje. Eso permite que servidor y clientes en lenguajes distintos se entiendan sin escribir código de serialización.

> [!question]- Alternativas: ¿qué diferencia entre REST, GraphQL y gRPC es correcta? a) GraphQL solo permite lecturas · b) gRPC permite comunicación bidireccional mientras que REST y GraphQL son unidireccionales · c) gRPC es exclusivo para navegadores · d) REST obliga al cliente a definir exactamente qué datos quiere
> b). a) es falsa porque GraphQL tiene mutaciones. c) es al revés, porque gRPC no es web-nativo. d) describe a GraphQL, no a REST. Nota: GraphQL tiene suscripciones en tiempo real, pero el modelo de petición-respuesta de ambos es unidireccional frente al streaming bidireccional de gRPC.

> [!question]- Mini caso: cámaras de una tienda envían eventos continuos a un servicio central y no pueden perder detecciones. REST resulta lento. ¿Qué propone y por qué?
> gRPC con streaming del cliente o bidireccional: conexión HTTP/2 persistente, mensajes binarios livianos y contrato tipado que expone solo las funciones necesarias. Se puede sumar TLS. Hay que justificar con latencia y volumen, y mencionar como costo que no es legible y exige coordinar los `.proto`.

> [!question]- ¿Por qué gRPC encaja dentro de un bounded context y es más discutible entre contextos?
> Dentro del contexto, los módulos son del mismo equipo y comparten el modelo, así que el acoplamiento del `.proto` compartido es barato y se gana velocidad. Entre contextos, compartir `.proto` acopla los releases de equipos distintos, como un Shared Kernel, y la independencia vale más que la eficiencia.

> [!question]- Nombre tres desventajas de gRPC.
> No es web-nativo (el navegador necesita gRPC-Web o un proxy), su protocolo binario no es legible por humanos y maneja mal mensajes grandes. Además requiere una curva de aprendizaje y coordinar los contratos `.proto`.

> [!question]- ¿Qué diferencia hay entre una llamada unaria y una de streaming del servidor? Dé un ejemplo de cada una.
> En la unaria, una petición recibe una respuesta, por ejemplo `Reservar(producto, cantidad)`. En el streaming del servidor, una petición recibe una secuencia de respuestas a lo largo del tiempo, por ejemplo `VigilarStock(producto)`, que envía cada cambio de stock mientras la conexión esté abierta.

> [!question]- V o F: "Como gRPC usa HTTP/2, un navegador puede llamarlo directamente igual que a una API REST".
> Falso. El navegador no expone el control de HTTP/2 que gRPC necesita, así que se usa gRPC-Web o Connect a través de un proxy. Por eso se dice que gRPC no es web-nativo.
