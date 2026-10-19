---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Node.js"
tags:
  - web
  - nodejs
  - backend
  - origen/complemento
prerrequisitos:
  - "[[01 - APIs y APIs web]]"
  - "[[01 - Código asíncrono y callbacks]]"
---

# Node.js como runtime de JavaScript

Del lado del cliente ya está todo: HTML, CSS, JavaScript y React. Falta el **servidor**, que recibe requests de muchos clientes a la vez, consulta la base de datos y responde. Ese servidor necesita un lenguaje que responda a eventos, que ejecute callbacks cuando terminan operaciones lentas y que soporte *closures*. JavaScript cumple todo eso, pero vive en el navegador. ¿Cómo se ejecuta fuera de él?

## Motores de JavaScript

Cada navegador trae un **motor** (*engine*) que interpreta y ejecuta JavaScript:

| Motor | Navegadores |
|---|---|
| **V8** (Google) | Chrome, Edge, Opera, Brave |
| **SpiderMonkey** (Mozilla) | Firefox |
| **JavaScriptCore** (Apple, WebKit) | Safari |

Pero el motor solo no basta. Para ser útil, el JavaScript necesita además conexión con el sistema operativo (archivos, red), manejo de eventos y librerías internas. Motor más esas piezas forman un **JavaScript runtime**. En el navegador, el runtime agrega las *Web APIs* (DOM, temporizadores, `fetch`):

![Componentes de un runtime de JavaScript](adjuntos/Componentes%20de%20un%20runtime%20de%20JavaScript.png)

> [!example]- Transcripción de la imagen
> Dentro de "JavaScript runtime": el **JS engine**, con su *heap* (memoria de los objetos) y su *call stack*; las **Web APIs** (DOM, *timers*, *fetch API*, …); una **microtasks queue** (con los resultados de `fetch`); y una **callback queue** (*timer*, *data*, …). Una flecha circular, el event loop, conecta las colas con el call stack.

## Qué es Node.js

**Node.js** es un **entorno de ejecución** (*runtime environment*) para JavaScript, de código abierto y multiplataforma, construido sobre **V8**, el motor de Chrome. V8 interpreta el código JavaScript; Node combina distintas APIs alrededor de él para que funcione como **backend**: leer archivos, abrir puertos, hablar con bases de datos.

| Año | Hito |
|---|---|
| 1995 | Nace JavaScript como lenguaje para el navegador |
| 2007 | La librería `libev` ofrece un event loop de alto rendimiento |
| 2008 | Nace V8, el motor de código abierto de Chrome |
| 2009 | Ryan Dahl crea Node.js combinando V8 con APIs de I/O de bajo nivel (libuv y C++) |

Node.js no es el único runtime: **Deno**, también de Ryan Dahl, se diseñó para superar limitaciones y problemas de seguridad de Node; **Bun**, basado en el motor de WebKit, se enfoca en la velocidad de ejecución y de arranque.

## Arquitectura en capas

![Capas de la arquitectura de Node.js](adjuntos/Capas%20de%20la%20arquitectura%20de%20Node.js.png)

> [!example]- Transcripción de la imagen
> De arriba hacia abajo: **Application / script**; **Node.js API** (`http`, `fs`, `crypto`, …, escrita en JavaScript); **Bindings** y **C++ Add-ons**; **V8** y **Libuv**, apoyados en **C-Ares**, **HTTP-parser**, **OpenSSL** y **zlib**; y abajo de todo, el **Operating system**.

Cada capa usa la API de la capa de abajo, y el código del programador está arriba:

- **Node.js API**: los módulos que se usan desde el código (`http`, `fs`, `crypto`, `net`…), escritos en JavaScript.
- **Bindings y C++ add-ons**: V8 está escrito en C++ y libuv en C, así que hacen falta *bindings* para que el JavaScript de la API llegue a esas capas. También se pueden escribir módulos propios en C++.
- **V8**: ejecuta el JavaScript. Es un compilador **JIT** (*just-in-time*), escrito en C++, que alterna continuamente entre compilar y ejecutar bloques de código.
- **libuv**: una librería en C, multiplataforma, creada para Node, que **abstrae las operaciones de I/O** para que no bloqueen en ningún sistema operativo.
- **Dependencias**: C-Ares (consultas DNS asíncronas), HTTP-parser (parseo de requests y respuestas), OpenSSL (criptografía, SSL y TLS) y zlib (compresión).

> [!tip] En resumen
> V8 es el **intérprete** que ejecuta JavaScript. Node.js es el **runtime**, escrito en C++, que envuelve a V8 y agrega la API de Node (y, mediante libuv, el I/O no bloqueante).

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un motor de JavaScript y un runtime?
> El motor (como V8) solo interpreta y ejecuta el lenguaje. El runtime agrega lo que hace falta para hacer algo útil: acceso al sistema operativo, manejo de eventos y librerías. En el navegador son las Web APIs; en Node, la API de Node y libuv.

> [!question]- ¿Qué aporta libuv a Node.js?
> El event loop y la ejecución no bloqueante de operaciones de I/O (archivos, red, DNS) en distintos sistemas operativos. Gracias a libuv, el hilo de JavaScript no se queda esperando esas operaciones.

> [!question]- ¿Por qué JavaScript resultó adecuado para escribir servidores?
> Porque ya estaba diseñado alrededor de eventos y callbacks: un servidor pasa la mayor parte del tiempo esperando I/O (red, disco, base de datos), y el modelo de JavaScript permite atender otras requests mientras tanto.
