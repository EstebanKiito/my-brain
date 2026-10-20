# Node.js — índice

JavaScript fuera del navegador: qué es un runtime y cómo está construido Node.js sobre V8 y libuv, cómo un lenguaje de un solo hilo atiende muchas operaciones a la vez gracias al call stack, la cola y el event loop, y cómo se usa Node para ejecutar scripts, cargar módulos y levantar un servidor HTTP.

Volver al [[Tecnologías y Aplicaciones Web/_Índice|mapa del ramo]].

> [!note] Origen
> Los apuntes de clase llegan hasta la clase anterior. Este tema se construyó con las slides de la clase de Node.js (motores y runtimes, historia, arquitectura en capas, blocking y non-blocking, trazas del call stack, event loop, servidor con `http`, puertos, Express, npm y yarn). El código se ejecutó con Node.js 20.

## Orden de estudio
1. [[01 - Node.js como runtime de JavaScript|Node.js como runtime de JavaScript]]: motores, runtimes, historia, Deno y Bun, y arquitectura de Node.
2. [[02 - Call stack y event loop|Call stack y event loop]]: CPU frente a I/O, código bloqueante, cola de mensajes, event loop y libuv.
3. [[03 - Scripts, módulos y servidor HTTP en Node|Scripts, módulos y servidor HTTP en Node]]: REPL, `require`, servidor con `http`, puertos y binding, Express, npm y yarn.

Las imágenes de esta carpeta están en `adjuntos/`.
