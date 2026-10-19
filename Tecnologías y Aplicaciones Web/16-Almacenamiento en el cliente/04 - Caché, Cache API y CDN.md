---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Almacenamiento en el cliente"
tags:
  - web
  - cache
  - cdn
  - origen/complemento
prerrequisitos:
  - "[[03 - IndexedDB]]"
  - "[[03 - Encadenamiento y errores en promesas]]"
---

# Caché, Cache API y CDN

La request más rápida es la que no se hace. Guardar copias de respuestas, en el navegador o en servidores cercanos al usuario, permite cargar más rápido, consumir menos datos y aliviar al servidor de origen. Esa copia es una **caché**, y existe en varios niveles.

## Tipos de caché

- **Caché privada**: vinculada a un cliente específico, en general el navegador. Solo la usa ese usuario.
- **Caché compartida**: guarda respuestas que se comparten entre varios usuarios.
  - **Caché proxy**: un servidor actúa como intermediario de contenido general para muchos usuarios y aplicaciones (por ejemplo, el proxy de una empresa).
  - **Caché administrada** (*managed cache*): se implementa para evitar la sobrecarga del servidor de origen, optimizada para una aplicación específica. Ejemplos: proxies reversos, **CDNs** y **service workers**.

> [!warning] Lo privado no va en una caché compartida
> Una respuesta con datos personales (un perfil, un carro de compras) no puede guardarse en una caché compartida, o se le mostraría a otro usuario. El header `Cache-Control: private` lo indica.

## Cache API

La **Cache API** permite al código guardar y gestionar **pares request-respuesta**. Con ella una aplicación puede funcionar sin conexión, cargar más rápido y reducir el consumo de datos reutilizando respuestas. Sus usos:

- guardar recursos para usarlos offline;
- optimizar los tiempos de carga;
- evitar solicitudes redundantes.

```javascript
// Abrir (o crear) una caché y guardar un recurso
caches.open('my-cache').then((cache) => {
  cache.add('/example-resource');   // hace la request y guarda la respuesta
});

// Recuperar el recurso guardado
caches.match('/example-resource').then((response) => {
  if (response) {
    response.text().then((content) => console.log('Cached content:', content));
  } else {
    console.log('Resource not found in cache!');
  }
});
```

| Método | Qué hace |
|---|---|
| `add(request)`, `addAll(requests)` | Hace la request y guarda la respuesta |
| `put(request, response)` | Guarda una respuesta ya obtenida |
| `match(request)`, `matchAll(request)` | Busca respuestas guardadas |
| `delete(request)` | Elimina una entrada |
| `keys()` | Lista las requests guardadas |

Se accede desde la página (`window.caches`) o desde un **service worker** (`self.caches`). Es la pieza central de las aplicaciones que funcionan offline.

> [!tip] La Cache API no expira sola
> A diferencia de la caché HTTP del navegador, que sigue los headers `Cache-Control`, lo que se guarda con la Cache API se queda hasta que el código lo borra. La aplicación decide cuándo renovar cada recurso.

## CDN: caché cerca del usuario

Una **CDN** (*Content Delivery Network*) es una red de servidores repartidos por el mundo que guardan copias del contenido (imágenes, CSS, JS y páginas) del **servidor de origen**. Cada usuario es atendido por el servidor de la CDN más cercano.

![Servidores CDN frente al servidor de origen](adjuntos/Servidores%20CDN%20frente%20al%20servidor%20de%20origen.png)

> [!example]- Transcripción de la imagen
> Un mapa mundial con un **servidor de origen** (naranja) en Norteamérica y **servidores CDN** (azules) en Canadá, Sudamérica, África, Asia y el sur de África. Cada usuario se conecta al servidor CDN más cercano, y solo los servidores CDN se comunican con el de origen (flechas naranjas).

- **Menos latencia**: la respuesta recorre menos distancia.
- **Menos carga en el origen**: la mayoría de las requests las responde la CDN.
- **Más disponibilidad**: si un nodo falla o hay un pico de tráfico, otros responden.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre una caché privada y una compartida?
> La privada pertenece a un solo cliente (el navegador) y puede guardar datos personales. La compartida sirve las mismas respuestas a muchos usuarios, así que solo debe guardar contenido público.

> [!question]- ¿Para qué sirve `caches.match` y qué devuelve si no hay nada guardado?
> Busca en la Cache API una respuesta guardada para una request. Si no la encuentra, la promesa se resuelve con `undefined`, y la aplicación puede ir a la red.

> [!question]- ¿Por qué una CDN mejora la velocidad aunque el servidor de origen sea rápido?
> Porque buena parte del tiempo de respuesta es la distancia física: la luz y los routers tardan. Un servidor de la CDN cercano al usuario evita cruzar continentes en cada request.
