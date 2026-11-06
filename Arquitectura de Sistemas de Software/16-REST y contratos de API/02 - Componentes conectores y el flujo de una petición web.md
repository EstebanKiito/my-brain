---
ramo: "Arquitectura de Sistemas de Software"
tema: "REST y contratos de API"
tags:
  - arquisis/integracion
  - arquisis/rest
  - origen/complemento
prerrequisitos:
  - "[[01 - REST como estilo derivado de restricciones]]"
  - "[[04 - Protocolos de aplicación DNS y HTTP]]"
---

# Componentes conectores y el flujo de una petición web

Como REST es un estilo arquitectónico, se describe igual que cualquier estilo: con **componentes**, **conectores** y **elementos de datos**. Conviene conocerlos con los nombres actuales (nginx, API Gateway, CDN), porque son las piezas que se dibujan en un diagrama de componentes cuando la solución usa la web.

## Componentes, conectores y datos

| Tipo | Elemento | Ejemplo actual |
|---|---|---|
| Componente | **Servidor de origen** | nginx, el backend que tiene los recursos |
| Componente | **Gateway y proxy** | Envoy, API Gateway |
| Componente | **User agent** | El navegador, o un agente de IA que llama herramientas |
| Conector | **Cliente y servidor HTTP** | La librería HTTP del cliente y el servidor web |
| Conector | **Caché** | Caché del navegador, CDN |
| Conector | **Resolver** | DNS, que traduce nombres a direcciones IP |
| Conector | **Túnel** | TLS, que cifra la comunicación |

Los roles son los mismos de la tesis de Fielding (2000), solo que hoy tienen otros nombres.

**Elementos de datos:**
- **Recurso:** el objetivo conceptual.
- **Identificador del recurso:** una URL o URN.
- **Representación:** un documento HTML, una imagen JPEG, un JSON.
- **Metadata de la representación:** *media type*, fecha de última modificación.
- **Metadata del recurso:** enlace a la fuente, representaciones alternativas.
- **Datos de control:** `If-Modified-Since`, `Cache-Control`.

![Vista de procesos de REST con clientes, cachés, capas y servidores](adjuntos/Vista%20de%20procesos%20del%20estilo%20REST.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, user agents con conector de cliente; algunos tienen caché (\$) y otros código bajo demanda (cuadro amarillo).
> - Al centro, intermediarios encadenados (proxies y gateways) con conectores de cliente y servidor, algunos con caché.
> - A la derecha, servidores de origen: uno con recursos, otro con código bajo demanda y uno conectado a una base de datos.
> - Leyenda: *Client Connector*, *Client + Cache*, *Server Connector*, *Server + Cache*, *Uniform Interface* (punto gris), *Code on demand* (amarillo) y *Layered System* (barra).

![Elementos de una arquitectura REST desde el agente hasta el servidor de origen](adjuntos/Elementos%20de%20una%20arquitectura%20REST%20del%20agente%20al%20servidor%20de%20origen.png)

> [!example]- Transcripción de la imagen
> - **User agent (1)** contiene *Application State (4)*, *Message processor (8)*, *Cache (3)* y *COD engine (5)*.
> - Envía un **Request** con una *Representation (7)* y recibe un **Response** con una *Representation (7)* que incluye `{Link1, Link2, …}`.
> - Pasa por un **Intermediary component (2)** con *Cache (3)* y *Message processor (8)*.
> - Llega al **Origin server (1)** con *Cache (3)*, *Message processor (8)* y los *Resource (6)*.
> - Flechas rojas punteadas (9) van de los links de la respuesta al estado de la aplicación del agente: la hipermedia guía el estado.
> - Los números corresponden a los principios REST: 1 cliente-servidor, 2 capas, 3 caché, 4 stateless, 5 código bajo demanda, 6 recursos identificables, 7 representaciones, 8 mensajes autodescriptivos y 9 HATEOAS.

![Croquis de un servidor con dos GET, un middleware y un cliente](adjuntos/Croquis%20de%20servidor%20middleware%20y%20cliente%20REST.png)

> [!example]- Transcripción de la imagen
> - Croquis en un cuaderno titulado "Rest".
> - Un componente **Server** con dos operaciones, *Get1* y *Get2*, expone una interfaz.
> - Esa interfaz la consume un **Middleware**, anotado "puede ser NGINX, API Gateway", que a su vez expone una interfaz al **Client**.

## El flujo de una petición por internet

![Flujo de una petición: DNS, navegador y servidor web](adjuntos/Flujo%20de%20una%20petición%20web%20con%20DNS.png)

> [!example]- Transcripción de la imagen
> - Arriba, la URL `http://ejemplo.com:80/index.html` descompuesta en **protocolo** (http, https, ftp, ftps, smtp…), **servidor** (dirección o dominio), **puerto** y **recurso** (estático o dinámico).
> - (1) El navegador (cliente HTTP) pregunta la dirección al **DNS**. (2) El DNS responde con la **IP pública**.
> - (3) El navegador envía `GET /index.html HTTP/1.1` con `Accept: text/plain` y `Host: ejemplo.com:80` al **Web server**.
> - (4) El servidor responde `HTTP/1.1 200 OK` con `Content-type: text/plain`, una cookie (`Set-cookie`) y el contenido.

Paso a paso:
1. **Encontrar la IP.** El cliente consulta al DNS, que entrega la dirección y el puerto del servidor. La IP puede quedar en caché para no volver a preguntar.
2. **Hacer la petición.** Por defecto se usa `GET` para pedir el recurso, con headers que indican el host y los formatos aceptados.
3. **Recibir la respuesta.** Trae el código de estado, el `Content-Type`, posibles cookies y el contenido.

![Flujo de una petición con caché del cliente, proxy del ISP y CDN](adjuntos/Flujo%20de%20una%20petición%20web%20con%20proxy%20y%20CDN.png)

> [!example]- Transcripción de la imagen
> - (1) El cliente HTTP revisa primero su **client cache**. (2) Consulta el DNS y obtiene la IP pública.
> - (3) La petición pasa por un **Proxy** con **proxy cache** dentro del **ISP**, ahora con el header `Cache-control: no-cache`.
> - (4) Llega a un **Gateway** con **gateway cache**, parte de una **CDN**. (5) Si no hay copia en caché, se consulta al **Origin Server**.
> - La respuesta agrega `Expires: Thu, 01 Dec 1994 16:00:00 GMT`, que indica hasta cuándo puede cachearse.

Esta segunda figura muestra la restricción de **capas** en acción. Entre el navegador y el servidor de origen hay varias cachés, y cualquiera puede responder si tiene una copia válida. El cliente no sabe si le respondió el origen o una caché, y no necesita saberlo. Una **VPN** agrega otra capa de este tipo: la petición sale hacia el ISP desde el servidor de la VPN, así que el destino no ve quién la originó.

> [!warning] El middleware en el diagrama
> Un reverse proxy o una API Gateway entre el cliente y los servidores es un **componente** del estilo REST (gateway o proxy), no un detalle de infraestructura. En un diagrama de componentes debe aparecer con sus interfaces, como en el croquis: servidor → middleware → cliente.

## Preguntas de repaso

> [!question]- Nombre los cuatro conectores del estilo REST y un ejemplo actual de cada uno.
> Cliente y servidor HTTP (la librería del navegador y el servidor web), caché (la caché del navegador o una CDN), resolver (DNS) y túnel (TLS).

> [!question]- ¿Cuál es la diferencia entre un componente "gateway/proxy" y un "servidor de origen"?
> El servidor de origen tiene los recursos y es la fuente de verdad de sus representaciones. El gateway o proxy es un intermediario que reenvía peticiones y puede cachear, balancear, autenticar o transformar, sin ser dueño de los recursos.

> [!question]- Describa los pasos de una petición a `http://ejemplo.com:80/index.html` sin cachés.
> El navegador consulta al DNS por la IP de ejemplo.com, recibe la IP pública, abre una conexión al puerto 80 y envía `GET /index.html` con headers como `Host` y `Accept`. El servidor responde con un código de estado (200 OK), el `Content-Type`, posibles cookies y el contenido.

> [!question]- En la figura con proxy y CDN, ¿qué restricción de REST permite que el cliente no sepa quién le respondió?
> La de capas (sistema en capas). Cada componente solo ve a su vecino inmediato, así que un proxy o una CDN pueden responder desde su caché sin que el cliente lo note. Junto con la restricción de caché, esto reduce la latencia y la carga en el servidor de origen.

> [!question]- V o F: "En REST, el user agent siempre es un navegador web".
> Falso. El user agent es cualquier cliente que inicia peticiones: un navegador, una app móvil, otro servicio o un agente de IA que llama herramientas.

> [!question]- ¿Para qué sirven headers como `Cache-Control` o `Expires`, y a qué tipo de elemento de datos de REST corresponden?
> Son datos de control: le dicen a las cachés intermedias y al cliente si pueden guardar la respuesta y hasta cuándo. Permiten que la restricción de caché funcione sin que cada caché conozca la aplicación.
