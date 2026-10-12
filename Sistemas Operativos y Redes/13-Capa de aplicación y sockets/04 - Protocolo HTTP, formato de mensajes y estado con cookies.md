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
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/03 - Sockets UDP y TCP: modelos y llamadas al sistema|03 - Sockets UDP y TCP: modelos y llamadas al sistema]]"
---

# Protocolo HTTP, formato de mensajes y estado con cookies

El protocolo de transferencia de hipertexto (HTTP, *Hypertext Transfer Protocol*) es el protocolo base de la World Wide Web. Opera sobre una arquitectura cliente-servidor utilizando el protocolo [[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|TCP]] en la capa de transporte (típicamente puerto 80 para HTTP y 443 para HTTPS). Es un protocolo sin estado (*stateless*), por lo que mecanismos como las cookies y cachés intermedias son necesarios para mantener sesiones y optimizar el rendimiento.

---

## HTTP, FTP y correo electrónico (mis apuntes)

PROTOCOLOS

1. HTTP
Envio de informacion de texto enriquecido
- Usa arquitectura CLIENTE/SERVIDOR
- Cliente: Solicita y revibe archivos
- Servidor: Recibe solicitudes y envia archivos
- (no de capa de transporte), si no de capa de APLICACION
- Es TCP:
Si usamos HTTP: Por debajo estamos usando protocolo TCP

REQUESTS:
HTTP Funciona a base de requests:
- GET /slides/disk.html HTTP/1.1
- Host: [iic2333.ing.puc.cl](http://iic2333.ing.puc.cl)
- Connection: close

Prueba eso en la terminal →
telnet iic2333.ing.puc.cl 80
GET / HTTP/1.1
Host: iic2333.ing.puc.cl
Connection: close
deberia devolver la landing page del servidor del curso (la pagina)

- Formato
- Siempre que pidas una URL (Uniform Resource Locator) desde el navegador para obtener un recurso web mediante HTTP. El navegador convierte la URL en un mensaje de solicitud y lo envía al servidor HTTP.

![Estructura y formato de un mensaje de solicitud HTTP request](adjuntos/Estructura%20y%20formato%20de%20un%20mensaje%20de%20solicitud%20HTTP%20request.png)

> [!example]- Transcripción de la imagen
> Formato de una petición HTTP (Request):
> - Línea de solicitud (*request line*): Método (`GET`, `POST`, `HEAD`, `PUT`, `DELETE`), URL del recurso y versión de HTTP (`HTTP/1.1`), terminada en `\r\n`.
> - Líneas de encabezado (*header lines*): `Host: ...`, `User-Agent: ...`, `Accept-Language: ...`, `Connection: close`, etc.
> - Línea vacía en blanco (`\r\n`) que delimita el fin de los encabezados.
> - Cuerpo de la entidad (*entity body*), utilizado en métodos como `POST` para enviar datos de formularios.

CODIGOS DE RESPUESTA

![Estructura y formato de un mensaje de respuesta HTTP response](adjuntos/Estructura%20y%20formato%20de%20un%20mensaje%20de%20respuesta%20HTTP%20response.png)

> [!example]- Transcripción de la imagen
> Formato de una respuesta HTTP (Response):
> - Línea de estado (*status line*): Versión del protocolo, código de estado y frase explicativa (ej. `HTTP/1.1 200 OK`).
> - Líneas de encabezado (*header lines*): `Connection: close`, `Date: ...`, `Server: ...`, `Last-Modified: ...`, `Content-Length: ...`, `Content-Type: text/html`.
> - Línea vacía en blanco (`\r\n`).
> - Cuerpo de la entidad (*data*): El archivo o página HTML solicitada.

HTTP/1.1 200 OK
Connection: close
Date: wed Jun 15 01:20:33 CLT
Server: …..data

Es Stateless → Sin Estado
No tiene capacidad de recordar solicitudes anteriores, para ellos se usan:
- COOKIES (informacion de la accion, se almacena en tu navegador, me compromento con el servidor, cada vez que me conecte, le mando informacion mia al servidor)
- Un ejemplo es por ejemplo: Me da un Id, me comprometo a cuando me conecte, lo haré con esa Id, para que sea mas facil acordarse de mi

![Mecanismo de estado mediante cookies HTTP entre cliente y servidor](adjuntos/Mecanismo%20de%20estado%20mediante%20cookies%20HTTP%20entre%20cliente%20y%20servidor.png)

> [!example]- Transcripción de la imagen
> Los cuatro componentes de la tecnología de cookies:
> 1. Línea de encabezado en la respuesta HTTP: `Set-cookie: 1678`.
> 2. Línea de encabezado en la siguiente solicitud HTTP: `Cookie: 1678`.
> 3. Archivo de cookies administrado por el navegador en el host cliente.
> 4. Base de datos back-end en el servidor que asocia el ID de cookie con el perfil y estado del usuario.

- Cuando el contenido no cambia (estatico) → Puede ser almacenado en Servidores Intermedios → WEB PROXY
- Redes de Cache → CDN: content delivery network): ej: CLOUDFORM: Cachear informacion sobre un servidor web
Web Caching: Cachear tu informacion, para que llegue mas rapido

2. FTP
- TRANSFERENCIA DE ARCHIVOS entre sistema Local y Remoto (Filezile funciona con FTP)
- Utiliza TCP
- Funciona con Inicio sesion → Contraseña y usuario
- Usa 2 Conexiones (2 Sockets por 1 Cliente)
- una conexión para los comandos y respuestas llamada conexión de control
- una segunda conexión para transferencias de datos llamada conexión de datos.
- FTP crea 2 conexiones entre las computadoras,

SMTP, POP, IMAP → CORREO ELECTRONICO
ENVIO → SMTP: Servidor de salida, encargado de enviar los correos y se depositen en el servidor
RECIBO →
- IMAP: Protocolo Nuevo , Almacena emails en el servidor (msj y estado) (cualquier dispositivo que pueda iniciar sesión, tenga acceso a todos los mensajes)
- Emails NO SE ALMACENAN en el servidor (si no de manera local)
- POP3: Descarga los mails en un UNICO DISPOSITIVO!

> [!tip] Complemento de clase: HTTP no persistente vs persistente
> - **HTTP/1.0 (No persistente)**: Se abre una conexión TCP independiente por cada objeto referenciado. Cada transferencia cuesta $2 \times \text{RTT} + \text{tiempo de transmisión}$.
> - **HTTP/1.1 (Persistente)**: Mantiene la conexión TCP abierta tras la primera solicitud, permitiendo enviar múltiples peticiones y respuestas consecutivas sobre el mismo socket (*pipelining*), ahorrando aperturas repetidas de conexión.

---

## Preguntas de repaso

> [!question]- ¿Qué significa que HTTP sea un protocolo sin estado (*stateless*) y por qué se diseñó así?
> Significa que el servidor no conserva información sobre peticiones previas del cliente; simplifica enormemente el diseño del servidor, haciéndolo robusto ante fallos y escalable a millones de conexiones simultáneas sin almacenar estados en memoria.

> [!question]- ¿Cuál es la diferencia fundamental en la arquitectura de FTP respecto a HTTP?
> FTP utiliza dos conexiones paralelas separadas: una conexión de control fuera de banda (*out-of-band*) en el puerto 21 para autenticación y comandos, y una conexión de datos en el puerto 20 que se abre y cierra por cada archivo transmitido.

> [!question]- ¿Por qué IMAP es preferido frente a POP3 en entornos multidispositivo modernos?
> Porque POP3 descarga y borra (o desincroniza) los correos localmente en un solo dispositivo, mientras que IMAP mantiene la jerarquía de carpetas, estados de lectura y mensajes sincronizados centralmente en el servidor de correo.

