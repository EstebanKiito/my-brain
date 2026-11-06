---
ramo: "Arquitectura de Sistemas de Software"
tema: "Caché y protocolos web"
tags:
  - arquisis/performance
  - arquisis/cache
  - origen/complemento
prerrequisitos:
  - "[[01 - Caché conceptos desafíos y buenas prácticas]]"
  - "[[02 - Componentes conectores y el flujo de una petición web]]"
---

# Caché web navegador proxy CDN y proxy inverso

En la web, en vez de descargar contenido desde un servidor remoto, el cliente lo obtiene de una copia **geográficamente cercana** o conectada por un enlace rápido. Hay tres lugares donde vive esa copia, y cada uno sirve a quien lo paga: el usuario, su red o el dueño del sitio.

## Los tres tipos de caché web

| | Caché del navegador | Caché de red (proxy) | Caché de distribución de contenido |
|---|---|---|---|
| Dónde | En el equipo del usuario | En el ISP o la red de una empresa | Cerca de los usuarios, operada por el dueño del sitio |
| Para quién | Un solo usuario | Todos los usuarios de esa red | Todos los usuarios del sitio, en todas partes |
| Ventaja | Copias cercanas y rápidas | Ahorra ancho de banda: una copia por cada contenido que alguien descargó | El contenido es accesible rápido en todas partes |
| Ejemplos | Caché de Chrome | Proxy cache, proxy de intercepción | **CDN**, **proxy inverso**, gateway cache, caché sustituta |

![Proxy cache del lado de los clientes y proxy inverso del lado del servidor](adjuntos/Caché%20de%20proxy%20y%20caché%20de%20proxy%20inverso.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, tres **Client**, cada uno con su **Browser cache**.
> - Los clientes se conectan a un servidor **proxy** con su **Proxy cache**, que sale a **Internet**.
> - Del otro lado de Internet, un **proxy inverso** con su **Reverse proxy cache** está delante del **Web server**.

![Herramientas del navegador con recursos servidos desde la caché en memoria](adjuntos/Caché%20del%20navegador%20entre%20el%20cliente%20y%20el%20servidor.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, la pestaña *Network* de las herramientas de desarrollo: varias imágenes con estado 200 y la columna *Size* marcada "(memory cache)".
> - A la derecha, un esquema: **Browser** envía un *request* al **Server** y recibe un *response* solo si el contenido no está cacheado o está stale. La **Cache** está conectada al navegador y guarda contenido "cached and not stale".

**Proxy inverso:** se ubica delante de los servidores del sitio (nginx, Varnish) y responde desde su caché las peticiones repetidas, para que no lleguen al servidor de aplicación. Además puede balancear carga y terminar TLS.

**CDN** (*Content Delivery Network*): una red de servidores repartidos por el mundo que guarda copias de los **archivos estáticos** (fotos, video, audio, streaming). Aprovecha la **cercanía** para bajar la latencia. Ejemplo: **CloudFront** delante de un bucket S3. **Ojo con la consistencia:** una mala política de caché o no usar **ETags** puede servir contenido viejo (*stale*).

## Reglas de caché en HTTP

- Si la respuesta dice `no-cache`, no se usa sin validar. Las peticiones **autenticadas o seguras** normalmente no se cachean en cachés compartidas.
- Una representación cacheada es **fresca** (se sirve desde la caché) si:
  - su fecha de expiración (`Expires`) o su edad máxima (`Cache-Control: max-age`) aún no se cumple; o
  - la caché la vio hace poco y fue modificada hace mucho (`Last-Modified`).
- Si está **añeja** (*stale*), se pide al servidor de origen que la **valide**. Con `If-None-Match` + `ETag` o `If-Modified-Since`, el servidor responde `304 Not Modified` sin reenviar el cuerpo.
- En ciertas circunstancias, como estar offline, se sirve la respuesta añeja sin consultar al origen.

```http
HTTP/1.1 200 OK
Cache-Control: public, max-age=31536000, immutable
ETag: "v3-a1b2c3"
Last-Modified: Tue, 01 Sep 2026 10:00:00 GMT
```

**Cómo implementarlo:**
- No usar headers en el HTML (`<meta>`), porque solo afectan a algunos navegadores. Hay que usar **headers HTTP**.
- `Expires` (en la respuesta) afecta a todas las cachés, pero **`Cache-Control` tiene precedencia**. Es una fecha absoluta, así que depende de que los relojes estén sincronizados.
- **Problema:** si `Expires` no se actualiza, todo vence a la vez y hay un aumento brusco de visitas al origen.

## Buenas prácticas web

- Usar **URLs de manera consistente**: la misma imagen siempre con la misma URL.
- Usar **librerías de imágenes comunes**.
- Marcar lo que cambia poco con `Cache-Control: max-age` grande, y versionar el nombre del archivo cuando cambia (`app.3f9a.js`).
- Ajustar `max-age` o `Expires` según cada recurso.
- **No actualizar archivos innecesariamente**: un `Last-Modified` falso invalida cachés sin motivo.
- Usar **cookies solo cuando sea necesario**: son difíciles de cachear, así que deben limitarse a las páginas dinámicas.

> [!example]- Respuesta modelo: lectores que deben ver noticias de su zona rápidamente
> **Herramienta:** caché por zona geográfica: una **CDN** o un **proxy** que detecte la región y sirva las noticias aprobadas de esa zona.
> **Justificación:** las mismas noticias las leen muchos lectores de la misma zona, y cambian relativamente poco una vez aprobadas.
> **Ubicación:** en la sección de lectores, entre los usuarios y el servidor.
> **Puntaje:** 1 punto por la solución, 2 por la justificación y 1 por la ubicación.

## Preguntas de repaso

> [!question]- Diferencie caché de proxy y caché de proxy inverso según quién la opera y a quién beneficia.
> El proxy lo opera la red del cliente (un ISP o una empresa), está cerca de los usuarios y ahorra ancho de banda a todos los de esa red. El proxy inverso lo opera el dueño del sitio, está delante de sus servidores y les quita carga respondiendo las peticiones repetidas.

> [!question]- ¿Qué tipo de contenido conviene poner en una CDN y qué riesgo hay?
> Archivos estáticos (imágenes, video, audio, CSS, JS) que muchos usuarios piden desde distintas regiones. El riesgo es servir contenido viejo si la política de caché o la invalidación (ETags, versionado) están mal configuradas.

> [!question]- ¿Qué precedencia hay entre `Expires` y `Cache-Control`, y qué problema tiene `Expires`?
> `Cache-Control` tiene precedencia. `Expires` es una fecha absoluta: depende de que los relojes estén sincronizados, y si no se actualiza, todo el contenido vence a la vez y produce un pico de visitas al origen.

> [!question]- ¿Qué ocurre cuando una representación está stale y el cliente tiene su ETag?
> La caché pide validarla al origen con `If-None-Match: <etag>`. Si no cambió, el origen responde `304 Not Modified` sin cuerpo, y la caché vuelve a servir su copia. Así se ahorra la transferencia.

> [!question]- ¿Por qué se recomienda usar cookies solo cuando es necesario?
> Porque una respuesta que depende de cookies varía por usuario y las cachés compartidas no pueden reutilizarla. Si se usan en páginas que podrían ser estáticas, se pierde la caché.

> [!question]- Mini caso: un supermercado sin cajeros tendrá mucha carga de consultas de productos al crecer en tiendas. ¿Es buena idea una caché por ubicación? ¿Dónde?
> Sí: hay productos populares que se consultan mucho en cada tienda y cambian poco. Se implementa una caché por tienda en el backend (por ejemplo, Redis con llaves por tienda) o una CDN para los datos de catálogo, delante de la base de productos, para no saturarla.

> [!question]- V o F: "Los navegadores tienen implementada internamente una caché tipo CDN".
> Falso. El navegador tiene su propia caché local, para un solo usuario. Una CDN es una red de servidores del proveedor del sitio, compartida por todos los usuarios.
