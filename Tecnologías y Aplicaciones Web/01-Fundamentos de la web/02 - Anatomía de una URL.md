---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - url
  - origen/complemento
prerrequisitos:
  - "[[01 - Internet, routers e ISPs]]"
---

# Anatomía de una URL

Todo empieza cuando el usuario escribe una **URL** (*Uniform Resource Locator*) en el navegador. La URL no es un texto arbitrario: cada parte le dice a alguien distinto qué hacer. El esquema le habla al navegador, el host a la red, el path y la query al servidor, y el fragmento de nuevo solo al navegador.

## Las partes

![Sintaxis de una URL](adjuntos/Sintaxis%20de%20una%20URL.png)

> [!example]- Transcripción de la imagen
> Diagrama de sintaxis: `scheme` `:` y luego, opcionalmente, `//` seguido de `[userinfo @] host [: port]`; después `path`, luego opcionalmente `? query` y opcionalmente `# fragment`.

| Parte | Para qué sirve | Ejemplo |
|---|---|---|
| **Scheme** | Cómo interpretar el resto de la URL | `https` |
| **Host** | Nombre de la máquina a la que se conecta | `buscacursos.uc.cl` |
| **Port** | Puerto de esa máquina (si se omite, el del scheme) | `:443` |
| **Path** | Lo usa el servidor para encontrar el contenido | `/wiki/URL` |
| **Query** | Parámetros adicionales en pares llave-valor | `?search=URI+generic+syntax` |
| **Fragment** | Sección a la que hacer *scroll*; solo la usa el navegador | `#Syntax` |

Dos ejemplos para identificar cada parte: `https://en.wikipedia.org/wiki/URL#Syntax` y `https://en.wikipedia.org/w/index.php?search=URI+generic+syntax&ns0=1`.

## Scheme

El esquema indica cómo interpretar lo que viene después de los dos puntos, para que la aplicación use el protocolo adecuado:

- `http`: protocolo de transferencia de hipertexto, puerto 80.
- `https`: lo mismo, pero sobre el protocolo seguro **TLS**, puerto 443.
- `file`: el resto se interpreta como una ruta del sistema de archivos local.
- `mailto`: abre un programa para redactar un email.

Así, una URL también puede indicarle al sistema operativo **qué aplicación** abrir. Los schemes válidos los define la **IANA** (*Internet Assigned Numbers Authority*), una organización sin fines de lucro que supervisa identificadores únicos a nivel mundial: direcciones IP, identificadores de protocolos, la base de zonas horarias, la base de TLDs y otras asignaciones.

## Host: subdominio, dominio y TLD

El host se lee de derecha a izquierda. En `https://buscacursos.uc.cl/`:

- **TLD** (*top-level domain*), `.cl`: la parte final del nombre. Hay TLD genéricos (`.com`), por país (`.cl`), patrocinados (`.gov`, `.app`), de infraestructura y reservados (`.localhost`).
- **Dominio**, `uc`: identifica de manera única un sitio web con un nombre fácil de recordar, sin necesidad de memorizar identificadores numéricos.
- **Subdominio**, `buscacursos`: una parte o dependencia del dominio con un propósito propio, como `portal.uc.cl`, `blog.example.com` o `support.example.com`.

> [!tip] `www` es solo una convención
> `www` es un subdominio como cualquier otro. Por eso existen variantes como `ww2` o `ww3`: réplicas del mismo contenido en otras máquinas, usadas para repartir la carga cuando `www` recibe demasiadas conexiones.

## Path

El path es una serie de segmentos separados por `/`. Se parece a una ruta de archivos, pero no tiene por qué existir una carpeta con ese archivo: muchas veces indica un **recurso lógico** que el servidor (y más adelante, las aplicaciones web propias) genera o selecciona dinámicamente según lo pedido.

## Query string

La query extiende la URL con pares `?llave1=valor1&llave2=valor2`. Se usa en búsquedas (`https://www.google.com/search?q=chile`) o para cambiar la vista de un recurso, por ejemplo un filtro o un orden.

¿Por qué en la URL y no en el cuerpo de la request? Al ser parte de la URL, la búsqueda queda en el **historial** (se puede volver a ella) y la respuesta se puede **cachear**, lo que acelera solicitudes repetidas.

> [!warning] Datos sensibles nunca en la query
> Justamente porque la query queda en el historial y en cachés, una contraseña no puede viajar ahí. El inicio de sesión usa `POST` y envía las credenciales en el **body** de la request.

## Preguntas de repaso

> [!question]- ¿Qué partes de una URL nunca llegan al servidor y por qué?
> El fragmento (`#…`): solo le indica al navegador a qué sección hacer scroll dentro del documento ya descargado, así que el navegador no lo envía en la request.

> [!question]- ¿Por qué el path no necesariamente corresponde a un archivo en el servidor?
> Porque muchas veces es un recurso lógico: el servidor interpreta la ruta y genera la respuesta dinámicamente (por ejemplo, consultando una base de datos), sin que exista una carpeta con ese nombre.

> [!question]- En `https://portal.uc.cl/`, ¿qué es cada parte del host?
> `.cl` es el TLD (por país), `uc` es el dominio que identifica el sitio y `portal` es un subdominio, una parte del sitio con un propósito propio.

> [!question]- ¿Cuándo conviene usar query string y cuándo el body?
> La query conviene para datos que se quieren recordar y cachear, como búsquedas y filtros. El body se usa para datos que no deben quedar en el historial ni en cachés, como credenciales o formularios con información sensible.
