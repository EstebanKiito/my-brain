---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - origen/complemento
prerrequisitos:
  - "[[03 - Orquestación con Docker Compose]]"
  - "[[04 - Protocolos de aplicación DNS y HTTP]]"
---

# Redes DNS NGINX y despliegue básico

Para que un usuario llegue desde un dominio como `api.misitio.me` hasta la API dentro de un contenedor en una EC2, intervienen varias piezas: el modelo **TCP/IP**, el **DNS** que traduce el nombre a una IP, y un **servidor web** (nginx) como **reverse proxy** delante de la API. Esta nota sigue ese camino y termina en el despliegue básico del proyecto.

## Internet por capas: TCP/IP

![Modelo TCP/IP con sus capas](adjuntos/Modelo%20TCP%20IP%20por%20capas.png)

> [!example]- Transcripción de la imagen
> - Un nodo de red con cuatro capas: **Application layer** (protocolos de aplicación), **Transport layer** (TCP y UDP), **Internet layer** (IP e ICMP, el módulo de internet) y **Data link layer** (Ethernet), que conecta al cable de red.

| Capa | Rol | Protocolos |
|---|---|---|
| **Aplicación** | Comunicación entre aplicaciones, funciones para el usuario | HTTP, HTTPS, SSH, SMTP |
| **Transporte** | Que el mensaje llegue al otro computador | **TCP** (confirma la recepción, mensaje íntegro) · **UDP** (solo envía, más rápido) |
| **Internet** | Cómo se identifican las máquinas y **enrutamiento** | IP |
| **Enlace de datos** | Hardware: cables, señales wifi | Ethernet |

![Enrutamiento de un mensaje por varias redes](adjuntos/Enrutamiento%20entre%20redes.png)

> [!example]- Transcripción de la imagen
> - **Computer A** envía a un **Router**, que puede llevar el mensaje por *Network 1 → 3 → 5* o por *Network 2 → 4* hasta **Computer B**.

Los routers se comunican entre sí para llevar el mensaje por el mejor camino disponible.

## DNS

Las personas usan URLs, no IPs. Una URL tiene **protocolo** (`https`), **subdominio** (`www`), **dominio** (`google`) y **dominio de nivel superior** (TLD, `.com`). El **DNS** traduce el nombre a una IP.

![Resolución DNS paso a paso hasta el servidor web](adjuntos/Resolución%20DNS%20paso%20a%20paso.png)

> [!example]- Transcripción de la imagen
> 1. El usuario pide `www.example.com`.
> 2. La consulta llega al **DNS resolver**.
> 3. El resolver pregunta al **DNS root name server**, que responde "ve al name server del TLD .com".
> 4. Pregunta al **name server del TLD .com**, que responde "ve al name server de Route 53".
> 5. Pregunta a **Amazon Route 53**, que responde `192.0.2.44`.
> 6-7. El resolver devuelve la IP al usuario.
> 8. El navegador pide `http://www.example.com` a esa IP.
> 9. El **web server** responde con la página.

| Registro | Para qué sirve |
|---|---|
| **A** (*address*) | Traduce el dominio a una IP |
| **CNAME** | Da otro nombre al mismo dominio (por ejemplo, `www`) |
| **TXT** | Información arbitraria (por ejemplo, verificaciones) |
| **NS** | Indica qué servidor tiene los registros del dominio |

**Pasos para el proyecto:**
1. Levantar el servidor.
2. Asociarle una **IP elástica**, que no cambia en el tiempo (se pide a AWS).
3. Contratar un dominio (por ejemplo, un `.me` gratuito con el GitHub Student Pack en Namecheap).
4. Crear un **registro A** que apunte a la IP elástica y un **CNAME** para `www`.
5. Esperar a que se **propague** y probar desde distintos servidores DNS.

## Servidor web: nginx

Un **servidor web** es un programa que corre en una máquina, atiende a los clientes y se comunica con los servidores de aplicación. Hay varios (Apache, Traefik, IIS), y el curso usa **nginx**: muy rápido, basado en un loop de eventos para atender muchas conexiones, y flexible y extensible.

![Servidor web entre el cliente, los datos estáticos y el servidor de aplicación](adjuntos/Servidor%20web%20entre%20cliente%20y%20servidor%20de%20aplicación.png)

> [!example]- Transcripción de la imagen
> - El **Web Client** envía una petición HTTP al **Web Server**.
> - El web server pide datos estáticos al **Static Data Store**, y reenvía las peticiones dinámicas (*Servlet Request*) al **Application Server** (*Web Container* y *Web Services*), que usa el **Application Data Store**.

![Forward proxy frente a reverse proxy](adjuntos/Forward%20proxy%20frente%20a%20reverse%20proxy.png)

> [!example]- Transcripción de la imagen
> - **Forward proxy:** usuarios A, B y C dentro de una LAN pasan por el *Forward Proxy* para salir a internet hacia los *Web Server A* y *B*.
> - **Reverse proxy:** usuarios en internet llegan a un *Reverse Proxy* (nginx) dentro de la LAN del servidor, que reparte hacia los *Web Server A* y *B*.

- **Forward proxy:** entre los **dispositivos de los usuarios** e internet, por ejemplo en la LAN de una empresa. Todas las salidas pasan por él.
- **Reverse proxy:** entre **internet y los servidores**. Recibe las conexiones externas y las redirige a los servidores. **El cliente cree que habla con un solo servidor.**

![Flujo de un reverse proxy hacia varios servidores de origen](adjuntos/Flujo%20de%20un%20reverse%20proxy.png)

> [!example]- Transcripción de la imagen
> - Tres dispositivos de usuario (`example.com`) llegan por **Internet** a un **reverse proxy**, que distribuye hacia dos **origin servers**.

El reverse proxy permite un **API Gateway** (varias APIs registradas detrás de una sola puerta de entrada), **balanceo de carga**, **protección ante ataques**, **caché** y **cifrado SSL**.

## Despliegue básico del proyecto

![Despliegue en una EC2 con reverse proxy, API, base de datos y suscriptor MQTT](adjuntos/Despliegue%20básico%20en%20una%20EC2.png)

> [!example]- Transcripción de la imagen
> - Una **EC2** recibe por HTTP desde una *Events API*. Dentro: **Reverse Proxy** («nginx gateway») → **Events Service** («REST»), conectado a una **Events DB**, y un **Mqtt Suscriber**.
> - El suscriptor se conecta por `mqtt` a un **Events Broker** externo («mqtt broker»).

**Pasos:** levantar el servidor y mapear el puerto 80 → conectarse por SSH → crear una llave SSH y agregarla a GitHub → clonar el repositorio → **instalar Docker** y levantar la API en contenedores → **configurar nginx** para que las llamadas externas lleguen al reverse proxy y de ahí a la API.

**RabbitMQ en el proyecto:** gestor de colas de mensajes para comunicar sistemas de forma **asíncrona**: un **producer** publica, el **broker** encola y un **consumer** se suscribe a la cola.

## Preguntas de repaso

> [!question]- Diferencie TCP y UDP.
> TCP confirma la recepción y garantiza que el mensaje llegue íntegro y en orden, a costa de más overhead. UDP solo envía, sin confirmar, lo que lo hace más rápido pero sin garantías. Lo usan, por ejemplo, el streaming y QUIC.

> [!question]- ¿Qué hace cada registro DNS: A, CNAME, TXT y NS?
> A traduce el dominio a una IP. CNAME da otro nombre a un mismo dominio (por ejemplo, `www`). TXT guarda información arbitraria. NS indica qué servidor tiene los registros del dominio.

> [!question]- ¿Por qué se usa una IP elástica en la EC2?
> Porque la IP pública normal puede cambiar al reiniciar la instancia, y el registro A del dominio quedaría apuntando a una IP equivocada. La IP elástica es fija.

> [!question]- Diferencie forward proxy y reverse proxy.
> El forward proxy está del lado de los usuarios: intermedia sus salidas a internet (por ejemplo, en una empresa). El reverse proxy está del lado de los servidores: recibe las peticiones de internet y las reparte entre los servidores, ocultándolos.

> [!question]- Nombre cuatro funciones de un reverse proxy como nginx.
> Balanceo de carga, actuar como API Gateway (una entrada para varias APIs), protección ante ataques, caché y terminación de SSL/TLS.

> [!question]- Ordene los pasos de la resolución DNS de `www.example.com`.
> El usuario consulta al resolver. El resolver pregunta al root, que lo deriva al TLD `.com`, que lo deriva al name server del dominio (Route 53), que responde la IP. El resolver la entrega al usuario, y el navegador pide la página a esa IP.

> [!question]- V o F: "Con un reverse proxy, el cliente sabe exactamente qué servidor de origen atendió su petición".
> Falso. El cliente cree que habla con un solo servidor: el reverse proxy oculta cuántos servidores hay y cuál respondió.
