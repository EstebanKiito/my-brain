---
ramo: "Sistemas Distribuidos"
tema: "Comunicación directa y sockets"
tags:
  - sd/comunicacion
  - redes
  - origen/complemento
prerrequisitos:
  - "[[03 - Protocolos de transporte TCP y UDP]]"
---

# Protocolos de aplicación DNS y HTTP

TCP y UDP mueven bytes, pero no dicen qué significan. Los **protocolos de aplicación** definen los pasos y el formato de los mensajes para cada servicio. Abrir una página web es el ejemplo completo: primero DNS traduce el nombre a una IP (y DNS es, en sí mismo, un sistema distribuido) y luego HTTP pide la página sobre TCP.

## Un protocolo para cada pregunta

| ¿Qué pasos sigo para… | Protocolo |
|---|---|
| …transferir un archivo? | FTP |
| …saber la IP de destino a partir de la URL? | DNS |
| …acceder a una página web? | HTTP |
| …acceder a una página web de forma segura? | HTTPS |
| …enviar un correo? | SMTP |
| …acceder a un servidor remoto por un canal seguro? | SSH |

## DNS: un servidor distribuido de nombres

DNS mantiene la tabla que traduce nombres de dominio a direcciones IP. No es un servidor, sino un **sistema distribuido y jerárquico**. Tanto el sistema operativo como los servidores guardan las consultas en **caché**; solo si la caché no tiene el resultado comienza la búsqueda:

![Resolución DNS en ocho pasos](adjuntos/Resoluci%C3%B3n%20DNS%20en%20ocho%20pasos.png)

> [!example]- Transcripción de la imagen
> 1. El computador pregunta `www3.animeflv.net?` al **DNS resolver**.
> 2. El resolver pregunta al **root server** (1.1.1.1).
> 3. El root responde `.net = 2.2.2.2`.
> 4. El resolver pregunta al **Top-Level Domain server** (2.2.2.2).
> 5. El TLD responde `animeflv.net = 3.3.3.3`.
> 6. El resolver pregunta al **authoritative server** (3.3.3.3).
> 7. Este responde `185.178.208.140`.
> 8. El resolver entrega `185.178.208.140` al computador.
>
> Las IP de los servidores DNS son ilustrativas.

Cada nivel solo sabe a quién preguntar después: la raíz conoce los TLD, el TLD conoce los servidores autoritativos de cada dominio, y el autoritativo tiene la IP final. Ningún servidor guarda todo, y por eso escala. Ver [[05 - Sistema de nombres de dominio (DNS) y resolución de consultas|DNS y resolución de consultas]].

## HTTP: pedir la página

1. Conseguir la IP del servidor (con DNS).
2. Construir la **petición** con el formato que exige HTTP.
3. Enviarla por **TCP** al servidor.
4. Esperar la **respuesta**.

```http
GET /anime/detective-conan HTTP/1.1
Host: www3.animeflv.net
Accept: text/html
```

La conexión TCP va a `185.178.208.140:443` (la IP que entregó DNS y el puerto de HTTPS). La respuesta trae una línea de estado, cabeceras y el cuerpo:

```http
HTTP/1.1 200 OK
Server: www3.animeflv.net
Content-Type: text/html
Content-Length: 4444

<html>
...
</html>
```

> [!tip] HTTP es texto con reglas
> Una petición HTTP no es más que un mensaje con un formato acordado que viaja por un socket TCP. Por eso, con un socket y respetando el formato, cualquier programa puede hablar HTTP.

> [!warning] `Remote Address` no es una cabecera
> Las herramientas de desarrollo del navegador muestran "Remote Address" junto a la petición, pero esa es la dirección a la que se abrió la conexión TCP, no una línea del mensaje HTTP.

El formato completo de los mensajes, los métodos y los códigos de estado están en [[04 - Mensajes HTTP y versiones del protocolo|Mensajes HTTP]] y [[04 - Protocolo HTTP, formato de mensajes y estado con cookies|Protocolo HTTP]].

## Preguntas de repaso

> [!question]- ¿Por qué DNS se considera un sistema distribuido?
> Porque la información está repartida entre muchos servidores organizados en jerarquía (raíz, TLD y autoritativos) y replicada en cachés. Ningún nodo tiene la tabla completa, y el sistema sigue funcionando aunque algunos fallen.

> [!question]- ¿Qué ganan el sistema operativo y los resolvers al guardar consultas en caché?
> Evitan repetir todo el recorrido por la jerarquía en cada visita: responden al instante y reducen la carga de los servidores raíz y TLD.

> [!question]- ¿Qué protocolo de transporte usa HTTP y por qué?
> TCP, porque una página debe llegar completa y en orden. Perder o desordenar un trozo del HTML la dejaría corrupta.
