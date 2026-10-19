---
ramo: "Tecnologías y Aplicaciones Web"
tema: "APIs web y REST"
tags:
  - web
  - api
  - fetch
  - origen/complemento
prerrequisitos:
  - "[[03 - Autenticación con tokens en APIs]]"
  - "[[04 - async y await]]"
---

# Documentar y consumir APIs

Para usar una API hay que saber qué endpoints tiene, qué esperan y qué responden. Eso lo dice la **documentación**. Después, desde el código, hace falta una herramienta para enviar las requests: en el navegador y en Node la opción moderna es `fetch`, y existen librerías como Axios y aplicaciones como Postman para explorar a mano.

## Documentación de una API

La mayoría de las APIs REST tienen documentación: un **manual de uso** con ejemplos. Su calidad define en gran parte la experiencia de quien consume la API. Ejemplos de buena documentación son las de GitHub, Stripe y Canvas. Normalmente incluye:

- el método HTTP y el endpoint (path);
- los parámetros de la request;
- la response;
- los errores posibles;
- ejemplos.

Por ejemplo, para listar los commits de un repositorio en la API de GitHub:

```http
GET https://api.github.com/repos/IIC2513/Syllabus-S1/commits
Accept: application/vnd.github+json
Authorization: Bearer <YOUR-TOKEN>
X-GitHub-Api-Version: 2022-11-28
```

Y para crear una issue, con los datos en el body:

```http
POST https://api.github.com/repos/IIC2513/Syllabus-S1/issues
Accept: application/vnd.github+json
Authorization: Bearer <YOUR-TOKEN>
X-GitHub-Api-Version: 2022-11-28

{ "title": "Found a bug", "body": "I'm having a problem with this.", "labels": ["bug"] }
```

## OpenAPI

**OpenAPI** es un estándar para describir una API REST en un archivo JSON o YAML con estructura definida, que entienden tanto las personas como las máquinas. Herramientas como **Swagger** generan a partir de él la documentación navegable, e incluso clientes y servidores de ejemplo. La propia API de GitHub publica su descripción en este formato.

```yaml
openapi: 3.0.4
info:
  title: Sample API
  version: 0.1.9
servers:
  - url: http://api.example.com/v1
paths:
  /users:
    get:
      summary: Returns a list of users.
      responses:
        "200":
          description: A JSON array of user names
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
```

## APIs no documentadas

Toda aplicación web moderna obtiene su contenido desde su backend con requests HTTP. Con la pestaña *Network* de DevTools se pueden ver esas requests y descubrir qué endpoints y métodos usa la página. Eso es **ingeniería inversa**, y permite escribir scripts útiles contra APIs que nadie documentó (lo explica bien el artículo de Julia Evans *How to use undocumented web APIs*).

## Consumir una API desde código

| Entorno | Opciones |
|---|---|
| Navegador | `fetch` (nativo, recomendado), `XMLHttpRequest` (nativo, legado), `axios` |
| Node | `fetch` (incluido desde Node 18), `axios`, `superagent`, el módulo `http` |

**AJAX** (*Asynchronous JavaScript and XML*) es la técnica de hacer requests **asíncronas** desde la página: la aplicación no se bloquea ni se queda en blanco, y el DOM se actualiza cuando llega la respuesta, así que se siente más responsiva. El primer mecanismo fue `XMLHttpRequest`, creado por Microsoft a fines de los 90 y hoy estandarizado:

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1', true);
xhr.send();
xhr.onload = function () {
  if (xhr.status != 200) alert(`Error ${xhr.status}: ${xhr.statusText}`);
  else alert(`Listo, se recibieron ${xhr.response.length} bytes`);
};
```

`fetch` es la API moderna, basada en **promesas**:

```javascript
fetch('https://api.github.com/repos/IIC2513/Syllabus-S1/commits', {
  headers: { Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
})
  .then((response) => {
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    return response.json();
  })
  .then((commits) => console.log(commits[0].author.login))
  .catch((error) => console.error('Error fetching commits:', error));
```

> [!warning] `fetch` no rechaza ante un 404 o un 500
> La promesa de `fetch` solo se rechaza si falla la red. Un `404` o un `500` llegan como respuesta normal, con `response.ok === false`. Por eso hay que revisar `response.ok` (o `response.status`) y lanzar el error a mano, como en el ejemplo.

**Axios** es una librería externa que simplifica lo anterior: convierte el JSON automáticamente y rechaza la promesa ante códigos de error.

```javascript
async function postIssue(owner, repo, token) {
  const url = `https://api.github.com/repos/${owner}/${repo}/issues`;
  const data = { title: 'Found a bug', body: "I'm having a problem with this.", labels: ['bug'] };
  const res = await axios.post(url, data, { headers: { Authorization: `Bearer ${token}` } });
  return res.data;
}
```

Para probar endpoints a mano, sin escribir código, se usa **Postman** (o `curl` desde la terminal).

## Preguntas de repaso

> [!question]- ¿Qué gana un equipo al describir su API con OpenAPI?
> Una especificación única y legible por máquinas, de la que se generan la documentación navegable (Swagger), validaciones y clientes. Así la documentación no se desactualiza respecto de lo que la API realmente acepta.

> [!question]- ¿Por qué un `catch` después de `fetch` no atrapa un error 404 por sí solo?
> Porque `fetch` considera exitosa cualquier respuesta HTTP, incluidas las de error. Solo rechaza ante fallas de red; para tratar un 404 como error hay que revisar `response.ok` y lanzar una excepción.

> [!question]- ¿Qué mejora AJAX en la experiencia del usuario?
> Permite pedir datos al servidor sin recargar la página: la interfaz sigue respondiendo mientras espera, y solo se actualiza la parte del DOM que cambia cuando llega la respuesta.
