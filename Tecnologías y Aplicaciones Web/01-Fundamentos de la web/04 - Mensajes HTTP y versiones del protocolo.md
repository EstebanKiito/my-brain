---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - http
  - origen/complemento
prerrequisitos:
  - "[[03 - Direcciones IP y DNS]]"
---

# Mensajes HTTP y versiones del protocolo

Con la IP del servidor en la mano, el navegador necesita un idioma común para pedir recursos. Ese idioma es **HTTP** (*Hypertext Transfer Protocol*): el protocolo para solicitar y entregar datos y recursos, como documentos HTML. Sigue el modelo **cliente-servidor**: el cliente (normalmente el navegador) hace una **petición** (*request*) y recibe una **respuesta** (*response*). Quien pide los datos es siempre quien los recibe.

## La request

Una request tiene tres partes:

1. **Request line** (obligatoria): el método, la URL o path y la versión de HTTP.
2. **Headers** (opcionales): metadatos en pares `Nombre: valor`, como el idioma aceptado, el navegador o la página de origen.
3. **Body** (opcional): datos enviados al servidor, por ejemplo un formulario.

![Estructura de una HTTP request](adjuntos/Estructura%20de%20una%20HTTP%20request.png)

> [!example]- Transcripción de la imagen
> - Izquierda: *Request line* (required), *Request header* (optional), *Request body* (optional).
> - Derecha, un ejemplo: la línea `GET http://www.kelley.indiana.edu/ardennis/home.htm HTTP/1.1` separa el comando (`GET`), la URL y la versión.
> - Headers: `Date: Mon 06 Aug 2001 17:35:46 GMT`, `User-Agent: Mozilla/6.0` (el navegador; Mozilla era el nombre en clave de Netscape) y `Referer: http://www.indiana.edu/~aisdept/faculty.htm` (la URL que contenía el link a la URL pedida).

## La response

La respuesta tiene la misma forma:

1. **Status line**: versión, código de estado y su frase (`HTTP/1.1 200 OK`).
2. **Headers**: fecha, servidor, tipo y largo del contenido, caché, etc.
3. **Body**: el recurso pedido, por ejemplo el HTML de la página.

```http
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT
Content-Length: 29769
Content-Type: text/html

<!DOCTYPE html... (aquí vienen los 29769 bytes de la página)
```

Esa respuesta corresponde a una request mínima: `GET / HTTP/1.1`, con los headers `Host: developer.mozilla.org` y `Accept-Language: fr`.

![Estructura de una HTTP response](adjuntos/Estructura%20de%20una%20HTTP%20response.png)

> [!example]- Transcripción de la imagen
> - Izquierda: *Response status* (marcado como optional), *Response header* (optional), *Response body* (marcado como required).
> - Derecha, un ejemplo: status `HTTP/1.1 200 OK`; headers `Date`, `Server: NCSA/1.3`, `Location: http://www.kelley.indiana.edu/adennis/home.htm` y `Content-type: text/html`; body con un documento HTML (título y un párrafo de bienvenida).

> [!warning] Qué es obligatorio en una response
> La figura marca el status como opcional y el body como obligatorio, pero es al revés: la **status line es obligatoria** (sin ella el cliente no sabe si la petición funcionó) y el **body es opcional**. Por ejemplo, una respuesta `204 No Content` o una redirección `301` no llevan cuerpo.

## Versiones de HTTP

| Versión | Qué introdujo |
|---|---|
| **HTTP/0.9** | La primera: solo el método `GET` y solo documentos HTML |
| **HTTP/1.0** | La versión del protocolo en el mensaje, headers con metadatos y otros tipos de documentos además de HTML |
| **HTTP/1.1** | Sigue en uso: reutiliza conexiones, responde por partes y permite alojar varios dominios en una misma IP gracias al header `Host` |
| **HTTP/2** | Protocolo **binario** (ya no texto), paralelismo de varias requests en una conexión, compresión de headers y mejor uso de la caché del cliente |
| **HTTP/3** | Mejor codificación (por paquete) y más velocidad, al usar **QUIC** en lugar de TCP |

> [!tip] Por qué importa el header `Host`
> Desde HTTP/1.1, un mismo servidor (una IP) puede alojar muchos sitios: el header `Host` le dice cuál de ellos pidió el cliente.

El formato de los mensajes visto desde la teoría de redes está en [[04 - Protocolo HTTP, formato de mensajes y estado con cookies|Protocolo HTTP y cookies]].

## Preguntas de repaso

> [!question]- ¿Por qué HTTP sigue el modelo cliente-servidor y qué implica para quien recibe los datos?
> Porque siempre hay una parte que pide (el cliente) y otra que responde (el servidor). Implica que el servidor no envía nada por iniciativa propia: solo responde a requests, y la respuesta vuelve a quien la pidió.

> [!question]- ¿Qué problema resolvió el header `Host` de HTTP/1.1?
> Antes, una IP equivalía a un sitio. Con `Host` el cliente dice qué dominio quiere, y un solo servidor con una IP puede atender muchos sitios distintos.

> [!question]- ¿Qué ganan HTTP/2 y HTTP/3 frente a HTTP/1.1?
> HTTP/2 pasa a binario, comprime headers y multiplexa varias requests en paralelo sobre una conexión. HTTP/3 reemplaza TCP por QUIC, lo que reduce la latencia y mejora la codificación por paquete.
