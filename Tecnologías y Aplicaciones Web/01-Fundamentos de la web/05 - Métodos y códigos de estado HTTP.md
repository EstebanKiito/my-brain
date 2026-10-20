---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - http
  - origen/complemento
prerrequisitos:
  - "[[04 - Mensajes HTTP y versiones del protocolo]]"
---

# Métodos y códigos de estado HTTP

Una request y una response tienen que comunicar algo más que datos: la request tiene que decir **qué acción** se quiere hacer sobre el recurso, y la response, **cómo salió**. Para eso existen los métodos y los códigos de estado. Son el vocabulario que después usan todas las APIs del curso.

## Métodos

El método va al inicio de la request line e indica la acción deseada sobre el recurso que identifica la URL.

![Métodos HTTP principales](adjuntos/M%C3%A9todos%20HTTP%20principales.png)

> [!example]- Transcripción de la imagen
> "Los métodos HTTP permiten indicar la acción que se desea realizar":
> - **GET**: solicita la representación de un recurso.
> - **POST**: envía datos para ser procesados por un recurso (crea o modifica).
> - **PUT**: envía datos para actualizar la información de un recurso.
> - **DELETE**: destruye un recurso.

Existen otros métodos (`PATCH`, `HEAD`, `OPTIONS`…), pero estos cuatro son los más usados. La referencia completa está en [MDN: métodos HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods).

> [!tip] GET solo lee
> `GET` no debería modificar nada en el servidor: solo pide una representación del recurso. Por eso es seguro repetirlo, cachearlo o guardarlo en el historial. Las acciones que cambian datos usan `POST`, `PUT` o `DELETE`.

## Códigos de estado

Cada respuesta lleva un **código de estado** (*status code*) de tres dígitos. El código basta por sí solo para saber si la solicitud funcionó o por qué falló, y el primer dígito indica la familia:

| Familia | Significado | Ejemplos típicos |
|---|---|---|
| **1xx** | Informativa | `100 Continue` |
| **2xx** | Éxito: el "camino feliz" | `200 OK`, `201 Created`, `204 No Content` |
| **3xx** | Redirección; el navegador la sigue solo | `301 Moved Permanently`, `304 Not Modified` |
| **4xx** | Error del cliente | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` |
| **5xx** | Error del servidor | `500 Internal Server Error`, `503 Service Unavailable` |

Un 4xx significa que el cliente pidió algo incorrecto o sin permiso, como acceder a un documento protegido. Un 5xx es el peor caso desde el punto de vista del desarrollador: la request era válida y fue **el servidor** el que falló, así que el usuario no puede hacer nada para arreglarlo.

## Los códigos 1xx en la práctica

Los 1xx son poco comunes y HTTP/1.0 ni siquiera los definía. El más conocido es `100 Continue`: el servidor confirma que recibió la parte inicial de la request (los headers) y que quiere el resto. Es útil al subir un archivo muy grande. El cliente envía primero los headers y espera el `100` antes de mandar todo el archivo, para no transmitir gigabytes que el servidor rechazaría de todas formas.

> [!warning] El código y el body deben coincidir
> Una API que responde `200 OK` con un body `{"error": "no encontrado"}` confunde a cualquier cliente que confíe en el código. El código es la señal oficial del resultado: un recurso inexistente es un `404`.

## Preguntas de repaso

> [!question]- ¿Por qué un error 5xx es peor que un 4xx?
> En un 4xx el problema está en la request y el cliente puede corregirla (autenticarse, cambiar la URL). En un 5xx la request era válida y falló el servidor, así que el usuario no puede resolverlo y el problema queda en manos del equipo que mantiene el servicio.

> [!question]- ¿Por qué no debería usarse GET para borrar un recurso?
> Porque GET se considera de solo lectura: los navegadores, cachés y buscadores pueden repetirlo, precargarlo o cachearlo sin preguntar. Si borrara datos, una simple visita o un rastreador podría eliminarlos.

> [!question]- ¿En qué situación sirve `100 Continue`?
> Al subir un archivo grande: el cliente manda primero los headers y espera la confirmación del servidor antes de enviar el cuerpo completo, para no transmitirlo en vano si el servidor lo va a rechazar.
