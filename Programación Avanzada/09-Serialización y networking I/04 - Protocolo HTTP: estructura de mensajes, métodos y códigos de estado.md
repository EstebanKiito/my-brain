---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/http
  - origen/complemento
prerrequisitos:
  - "[[02 - Fundamentos de redes: arquitectura cliente-servidor, sockets y puertos]]"
  - "[[03 - Modelo de capas y protocolos de transporte: TCP frente a UDP]]"
---

# Protocolo HTTP: estructura de mensajes, métodos y códigos de estado

La World Wide Web y la gran mayoría de las APIs modernas operan sobre **HTTP** (*Hypertext Transfer Protocol*). Es un protocolo de la capa de aplicación, cliente-servidor y sin estado (*stateless*), que estandariza el intercambio de recursos digitales mediante mensajes de texto estructurados.

## Anatomía de una URL

Para localizar un recurso en internet, el cliente utiliza un localizador uniforme de recursos o **URL** (*Uniform Resource Locator*):

$$\overbrace{\text{https}}^{\text{Esquema}}://\overbrace{\text{api.ejemplo.com}}^{\text{Host / Dominio}}:\underbrace{443}_{\text{Puerto}}/\overbrace{\text{v1/usuarios}}^{\text{Ruta (Path)}}?\overbrace{\text{rol=admin\&orden=desc}}^{\text{Parámetros de consulta (Query)}}#\underbrace{\text{resumen}}_{\text{Fragmento}}$$

- **Esquema:** protocolo de acceso (`http`, `https`).
- **Host y Puerto:** máquina destino y puerto de escucha (80 para HTTP, 443 para HTTPS por defecto).
- **Ruta (*Path*):** ruta jerárquica del recurso en el servidor.
- **Parámetros (*Query string*):** pares clave-valor que filtran o parametrizan la consulta a partir del signo `?`.

## Estructura de los mensajes HTTP

La comunicación HTTP se realiza mediante transacciones individuales de **Petición** (*Request*) y **Respuesta** (*Response*):

![Estructura de un mensaje HTTP](adjuntos/Estructura%20de%20un%20mensaje%20de%20petici%C3%B3n%20y%20respuesta%20HTTP.png)

> [!example]- Transcripción de la imagen
> - Anatomía de mensajes HTTP:
>   - Petición: Línea de solicitud (método, ruta, versión), cabeceras (*headers*), línea en blanco y cuerpo opcional (*body*).
>   - Respuesta: Línea de estado (versión, código, mensaje de estado), cabeceras, línea en blanco y cuerpo con datos (JSON/HTML).

1. **Línea inicial:** indica la acción solicitada (ejemplo `GET /perfil HTTP/1.1`) o el resultado (ejemplo `HTTP/1.1 200 OK`).
2. **Cabeceras (*Headers*):** metadatos clave-valor que describen la petición (tipo de cliente en `User-Agent`, formato en `Content-Type: application/json`, credenciales en `Authorization`).
3. **Línea vacía:** separador estricto (`\r\n`) que delimita el fin de las cabeceras.
4. **Cuerpo (*Body* / *Payload*):** datos transmitidos en formato texto (JSON, XML) o binario.

## Métodos HTTP fundamentales (Verbos)

Los métodos definen la semántica de la operación solicitada:

- **`GET`:** solicita la representación de un recurso existente. Es una operación **segura e idempotente**: solo consulta datos y no debe modificar el estado del servidor.
- **`POST`:** envía datos al servidor en el cuerpo del mensaje para crear un recurso nuevo o ejecutar una acción que altera el estado del sistema.
- **`PUT` / `PATCH`:** actualizan un recurso existente (`PUT` reemplaza el objeto completo de forma idempotente; `PATCH` aplica modificaciones parciales).
- **`DELETE`:** elimina el recurso especificado en el servidor.

## Códigos de estado HTTP

La respuesta del servidor incluye un código numérico de 3 dígitos agrupado por categorías:

```
+-----------+-------------------------+-------------------------------------------------------------+
| Rango     | Categoría               | Códigos más comunes y significado                           |
+-----------+-------------------------+-------------------------------------------------------------+
| 2xx       | Éxito (Success)         | 200 OK (éxito habitual), 201 Created (recurso nuevo creado) |
| 3xx       | Redirección             | 301 Moved Permanently (recurso reubicado de forma definitiva)|
| 4xx       | Error del Cliente       | 400 Bad Request (sintaxis inválida), 401 Unauthorized       |
|           |                         | 403 Forbidden (sin permisos), 404 Not Found (no existe)     |
|           |                         | 429 Too Many Requests (límite de peticiones excedido)       |
| 5xx       | Error del Servidor      | 500 Internal Server Error (excepción no controlada en back) |
|           |                         | 503 Service Unavailable (servidor saturado o caído)         |
+-----------+-------------------------+-------------------------------------------------------------+
```

> [!tip] La regla de la idempotencia
> Una operación es **idempotente** si ejecutarla una sola vez produce el mismo efecto en el sistema que ejecutarla diez veces consecutivas (`GET`, `PUT`, `DELETE`). En cambio, repetir una petición `POST` suele crear múltiples recursos duplicados.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que el protocolo HTTP es un protocolo sin estado (*stateless*)?
> Porque el servidor procesa cada petición de forma aislada e independiente; no recuerda ni mantiene información de peticiones previas realizadas por el mismo cliente.

> [!question]- ¿Cuál es la diferencia semántica entre un método `GET` y un método `POST`?
> `GET` es una operación de solo lectura para consultar recursos sin provocar efectos colaterales en el servidor, mientras que `POST` transporta datos en su cuerpo para generar cambios o crear nuevos recursos.

> [!question]- ¿Qué información separa la línea en blanco obligatoria dentro de un mensaje HTTP?
> Separa el bloque de metadatos de las cabeceras (*headers*) del contenido de datos real ubicado en el cuerpo (*body*).

> [!question]- ¿En qué se diferencian conceptualmente los errores de la familia 4xx frente a los de la familia 5xx?
> Los errores 4xx indican que la causa del problema provino del cliente (ruta errónea, falta de permisos o datos inválidos), mientras que los 5xx indican que el servidor falló internamente al procesar una petición válida.

