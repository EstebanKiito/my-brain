---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Node.js"
tags:
  - web
  - nodejs
  - servidor
  - npm
  - origen/complemento
prerrequisitos:
  - "[[02 - Call stack y event loop]]"
  - "[[05 - Un proyecto React con npm y Vite]]"
---

# Scripts, módulos y servidor HTTP en Node

Con Node instalado, JavaScript sirve para tres cosas fuera del navegador: probar código en una consola, ejecutar scripts y, sobre todo, levantar un **servidor HTTP**. Esta nota recorre esos usos hasta llegar al servidor mínimo, que muestra por qué después conviene un framework como Express.

## Consola y scripts

El comando `node` sin argumentos abre un **REPL**, una consola interactiva del lenguaje, como la del navegador o como `python` e `irb`. Con un archivo como argumento, lo ejecuta:

```javascript
// poema.js  →  se ejecuta con: node poema.js
function imprimirPoema() {
  const verso = `
  Este código por IA ha sido creado,
  Con precisión y arte bien elaborado.`;
  console.log(verso);
}
imprimirPoema();
```

## Módulos con `require`

`require()` carga un **módulo**, como `import` en Python. Puede ser un módulo incluido en Node (`http`, `fs`), uno instalado con npm (`express`) o uno propio (`./utils`). Es el sistema de módulos original de Node (*CommonJS*); Node también soporta `import`/`export` de ES6.

## Un servidor HTTP sin frameworks

```javascript
const http = require('http');

const server = http.createServer();

server.on('request', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

server.on('listening', () => {
  console.log('Server running!');
});

server.listen(3000);
```

- `require('http')` retorna el módulo HTTP de Node; su API permite crear el servidor con `http.createServer()`.
- `on()` es el equivalente en Node de `addEventListener`: suscribe un callback a un evento.
- El evento `request` se emite con **cada nueva request HTTP**. El callback recibe `req` (la información de la request entrante) y `res` (la respuesta, sobre la que se escriben el código de estado, los headers y el cuerpo).
- `listen(3000)` empieza a aceptar conexiones en el puerto 3000. Cuando el servidor queda asociado a ese puerto se emite `listening`.

## Puertos y binding

Un **puerto** es, en redes, un lugar donde ocurre una conexión lógica. Se identifica con un número de 16 bits, entre 0 y 65535. Toda conexión (por ejemplo TCP) indica a qué IP y a qué puerto se quiere conectar, y hay puertos asociados por convención a ciertos protocolos (80 para HTTP, 443 para HTTPS, 5432 para PostgreSQL). Cuando un proceso servidor se inicia, le pide al sistema operativo que asocie un puerto a ese proceso: eso es el **binding**. Desde ahí, lo que llegue a ese puerto se entrega al servidor.

El detalle de puertos y sockets está en [[02 - Concepto de socket e identificación por IP y puerto|Sockets, IP y puerto]].

> [!warning] Las limitaciones del servidor mínimo
> Este servidor responde lo mismo a **cualquier** request: `GET /`, `POST /users` o `DELETE /lo-que-sea`. Para distinguir rutas y métodos, leer el body, manejar errores o servir archivos habría que escribir todo a mano dentro del único callback. Para eso existen los frameworks.

## Express: un adelanto

**Express** es el framework web más popular para Node. Con él, el mismo servidor separa rutas y métodos de forma declarativa:

```javascript
const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  res.send('world!');
});

app.listen(3000, () => console.log('Example app listening on port 3000'));
```

## npm y yarn

Los paquetes como Express se instalan con un gestor de paquetes:

| Acción | npm | yarn |
|---|---|---|
| Agregar una dependencia | `npm install express` | `yarn add express` |
| Quitarla | `npm uninstall express` | `yarn remove express` |

**npm** (*Node Package Manager*) es una CLI escrita en JavaScript que descarga los paquetes del registro de npm en la carpeta `node_modules`. **yarn** es una alternativa que usa el mismo registro y que agregó mejoras de rendimiento: resolución determinística de dependencias e instalación en paralelo.

## Preguntas de repaso

> [!question]- ¿Qué representan `req` y `res` en el callback del evento `request`?
> `req` es la request entrante: método, URL, headers y body. `res` es la respuesta que el servidor va construyendo: código de estado, headers y cuerpo, que se envía con `res.end()`.

> [!question]- ¿Qué significa que un servidor haga binding al puerto 3000?
> Que le pide al sistema operativo asociar ese puerto a su proceso. Desde entonces, las conexiones que lleguen a la IP de la máquina en el puerto 3000 se entregan a ese servidor.

> [!question]- ¿Qué problema del servidor con `http` resuelve Express?
> El de tener un único callback para todas las requests. Express permite declarar una función por cada combinación de método y ruta, y agrega utilidades para leer el body, enviar JSON y manejar errores.
