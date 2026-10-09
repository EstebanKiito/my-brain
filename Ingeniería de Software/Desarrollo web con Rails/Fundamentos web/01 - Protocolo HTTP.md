---
ramo: Ingeniería de Software
tema: Fundamentos web
tags: [ingsoft/web, origen/complemento]
prerrequisitos: []
---
# Protocolo HTTP

> [!tip] Complemento — nota nueva (fuente: slides "RoR - First API" y libro del curso, cap. 12.1)
> **Qué es:** HTTP (*HyperText Transfer Protocol*) es el protocolo con el que un **cliente** (navegador, Postman, una app) pide recursos a un **servidor web** y recibe una respuesta. Todo lo que se hace en Rails es responder *requests* HTTP.
>
> **Por qué hace falta un protocolo (slides):** dos computadores se envían bits, por ejemplo `01001000 01101001`. Si A quiso decir "Hi" (los caracteres `H` = 72 e `i` = 105) pero B lo interpreta como un número, B entiende **18537**. Los bits `00110010 00110000 00110010 0011…` pueden ser los caracteres "2022" o números como 50 y 48. Ambos lados tienen que **acordar cómo interpretar el mensaje**: eso es un protocolo.
>
> ```mermaid
> sequenceDiagram
>   participant U as Navegador (cliente)
>   participant S as Servidor web
>   U->>S: HTTP Request (GET /hi)
>   S-->>U: HTTP Response (200 OK + "Hello World!")
> ```
>
> ## HTTP Request
> Tiene **Method, Target, Version, Headers y Body**:
> ```http
> POST /cgi-bin/process.cgi HTTP/1.1          ← método, target, versión
> User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
> Host: www.tutorialspoint.com                 ← headers
> Content-Type: application/x-www-form-urlencoded
> Content-Length: length
> Accept-Language: en-us
> Accept-Encoding: gzip, deflate
> Connection: Keep-Alive
>
> licenseID=string&content=string&/paramsXML=string   ← body
> ```
>
> ## HTTP Response
> Tiene **Version, Status, Headers y Body**:
> ```http
> HTTP/1.1 200 OK                              ← versión y status
> Date: Mon, 27 Jul 2009 12:28:53 GMT
> Server: Apache/2.2.14 (Win32)
> Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
> Content-Length: 88
> Content-Type: text/html
> Connection: Closed
>
> <html>…</html>                               ← body
> ```

> [!tip] Complemento — métodos y códigos de estado más usados
> | Método | Uso típico (CRUD) |
> |---|---|
> | `GET` | Leer (*Read*) |
> | `POST` | Crear (*Create*) |
> | `PUT` / `PATCH` | Actualizar (*Update*): reemplazar todo o una parte |
> | `DELETE` | Borrar (*Delete*) |
>
> | Código | Significado |
> |---|---|
> | 200 OK · 201 Created · 204 No Content | Éxito |
> | 301 / 302 | Redirección (lo que hace `redirect_to` en Rails) |
> | 400 Bad Request · 404 Not Found · 422 Unprocessable Entity | Error del cliente (422 lo usa Rails cuando falla una validación) |
> | 500 Internal Server Error | Error del servidor |
>
> **Postman** es una herramienta para armar y enviar requests HTTP a mano y ver la respuesta. En clase se usó para probar la PokeAPI y las primeras APIs en Rails.

## Preguntas de repaso

1. ¿Qué partes tiene un HTTP request y cuáles una response?
> [!question]- Respuesta
> Request: método, target (ruta), versión, headers y body. Response: versión, status (código), headers y body.

2. ¿Qué método HTTP corresponde a cada operación CRUD?
> [!question]- Respuesta
> Create → POST, Read → GET, Update → PUT/PATCH, Delete → DELETE.

3. ¿Qué indica un código 404 y qué indica uno 500?
> [!question]- Respuesta
> 404: el recurso pedido no existe (error del cliente). 500: error interno del servidor al procesar el request.

4. ¿Por qué se necesita un protocolo para comunicar dos computadores?
> [!question]- Respuesta
> Porque los bits por sí solos no tienen significado: ambas partes deben acordar cómo interpretarlos. El ejemplo de las slides: "Hi" leído como número da 18537.
