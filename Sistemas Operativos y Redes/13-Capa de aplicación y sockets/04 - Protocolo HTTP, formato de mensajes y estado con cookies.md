---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - http
  - cookies
  - ftp
  - correo
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/03 - Sockets UDP y TCP: modelos y llamadas al sistema|03 - Sockets UDP y TCP: modelos y llamadas al sistema]]"
---

# Protocolo HTTP, formato de mensajes y estado con cookies

**HTTP** (*HyperText Transfer Protocol*) es el protocolo de la web: con él se envía información de texto enriquecido, como páginas HTML. Es un protocolo de la **capa de aplicación**, no de transporte (puerto 80 por defecto, 443 para HTTPS): por debajo usa [[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|TCP]]. Esta nota cubre HTTP y, al final, otros dos protocolos de aplicación: FTP y los de correo.

## Cómo funciona HTTP

Usa una arquitectura **cliente-servidor**:

- el **cliente** (el navegador) **solicita** y recibe archivos;
- el **servidor** **recibe** solicitudes y envía archivos.

Cuando se pide una **URL** (*Uniform Resource Locator*) desde el navegador, este la convierte en un mensaje de solicitud (*request*) y lo envía al servidor HTTP.

![Estructura y formato de un mensaje de solicitud HTTP request](adjuntos/Estructura%20y%20formato%20de%20un%20mensaje%20de%20solicitud%20HTTP%20request.png)

> [!example]- Transcripción de la imagen
> (1) *User issues URL from a browser* `http://host:port/path/file`. (2) *Browser sends a request message*: `GET URL HTTP/1.1`, `Host: host:port`, … (3) *Server maps the URL to a file or program under the document directory*. (4) *Server returns a response message*: `HTTP/1.1 200 OK`, … (5) *Browser formats the response and displays*. Abajo: *Client (Browser)*, *HTTP (Over TCP/IP)*, *Server (@ host:port)*.

Un request es texto plano. Por ejemplo:

```text
GET /slides/disk.html HTTP/1.1
Host: iic2333.ing.puc.cl
Connection: close
```

El método de la primera línea dice qué se quiere hacer: `GET` (obtener), `POST` (enviar datos, por ejemplo de un formulario), `PUT`, `DELETE`, `HEAD`… Se puede probar a mano desde la terminal (servidor del curso: [iic2333.ing.puc.cl](http://iic2333.ing.puc.cl)) con `telnet iic2333.ing.puc.cl 80` y escribiendo esas líneas: el servidor devuelve la página. La respuesta empieza con una **línea de estado** y sigue con headers y el contenido:

```text
HTTP/1.1 200 OK
Connection: close
Date: ...
Server: ...
(línea en blanco y luego los datos)
```

## Códigos de respuesta

![Estructura y formato de un mensaje de respuesta HTTP response](adjuntos/Estructura%20y%20formato%20de%20un%20mensaje%20de%20respuesta%20HTTP%20response.png)

> [!example]- Transcripción de la imagen
> "Códigos": **1xx** mensaje de información. **2xx** mensaje de éxito: 200 OK, 206 Partial Content. **3xx** mensaje de redirección: 301 Moved Permanently, 307 Temporary Redirect. **4xx** mensaje de error del cliente: 400 Bad Request, 403 Forbidden, 404 Not Found, 405 Method Not Allowed. **5xx** mensaje de error del servidor: 500 Internal Server Error, 501 Not Implemented, 502 Bad Gateway, 503 Server Not Available.

## Sin estado: cookies

HTTP es **stateless** (sin estado): el servidor **no recuerda** las solicitudes anteriores. Para "recordar" a un usuario se usan **cookies**: el servidor le asigna al cliente un identificador, y el cliente **se compromete a enviarlo cada vez que se conecte**, para que el servidor lo reconozca. El navegador guarda las cookies, y el servidor asocia cada identificador con información del usuario en su base de datos.

![Mecanismo de estado mediante cookies HTTP entre cliente y servidor](adjuntos/Mecanismo%20de%20estado%20mediante%20cookies%20HTTP%20entre%20cliente%20y%20servidor.png)

> [!example]- Transcripción de la imagen
> *Client host* con un archivo de cookies (*ebay: 8734*) envía un *usual http request msg*. El *Server host* crea el *ID 1678 for user* (*entry in backend database*) y responde con *Set-cookie: 1678*; el archivo de cookies del cliente pasa a tener *amazon: 1678, ebay: 8734*. El siguiente request lleva *cookie: 1678* y el servidor hace una *Cookie-specific action* consultando su base de datos. *One week later*, un nuevo request vuelve a llevar *cookie: 1678*.

```python
import http.server, socket, threading

class Hola(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        cuerpo = b"<h1>hola</h1>"
        self.send_response(200)                                   # 200 OK
        self.send_header("Content-Type", "text/html")
        self.send_header("Set-Cookie", "id=1678")                 # el servidor le asigna un id
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)
    def log_message(self, *args): pass

srv = http.server.HTTPServer(("127.0.0.1", 0), Hola)
threading.Thread(target=srv.serve_forever, daemon=True).start()

with socket.create_connection(srv.server_address) as s:          # lo mismo que hacer telnet
    s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")
    print(s.recv(4096).decode())   # línea de estado, headers (con Set-Cookie) y el HTML
srv.shutdown()
```

**Conexiones persistentes.** En HTTP/1.0 se abría una conexión TCP por cada objeto de la página, con un costo de unos $2 \times RTT$ (*round-trip time*) más la transmisión por objeto. HTTP/1.1 mantiene la conexión abierta y la reutiliza para varios objetos.

**Caché web.** Cuando el contenido no cambia (es estático), se puede guardar en servidores intermedios: un **web proxy**, o redes de caché como las **CDN** (*Content Delivery Network*, por ejemplo Cloudflare). Así la información llega más rápido y se descarga al servidor original.

## Otros protocolos de aplicación

- **FTP** (*File Transfer Protocol*): transfiere archivos entre un sistema local y uno remoto (FileZilla, por ejemplo). Usa TCP y requiere iniciar sesión con usuario y contraseña. Usa **dos conexiones** (dos sockets por cliente): una de **control**, para comandos y respuestas, y otra de **datos**, para las transferencias.
- **Correo electrónico**:
  - **SMTP**: el servidor de **salida**, que envía los correos y los deposita en el servidor del destinatario.
  - **IMAP**: para **recibir**; mantiene los correos y su estado **en el servidor**, así que cualquier dispositivo donde se inicie sesión ve todos los mensajes.
  - **POP3**: para recibir; **descarga** los correos a un **único dispositivo**, donde quedan almacenados localmente.

## Preguntas de repaso

> [!question]- ¿Qué significa que HTTP sea stateless y cómo se compensa?
> Que el servidor no recuerda las solicitudes anteriores. Se compensa con cookies: el servidor entrega un identificador y el cliente lo reenvía en cada solicitud para que lo reconozcan.

> [!question]- ¿Qué indican los códigos 2xx, 3xx, 4xx y 5xx?
> Éxito (200 OK), redirección (301), error del cliente (404 Not Found) y error del servidor (500), respectivamente.

> [!question]- ¿Por qué FTP usa dos conexiones?
> Para separar el control (comandos y respuestas, como el inicio de sesión) de la transferencia de los datos de los archivos.

> [!question]- ¿Qué diferencia hay entre IMAP y POP3?
> IMAP deja los correos y su estado en el servidor, sincronizados en todos los dispositivos. POP3 los descarga a un único dispositivo.
