---
ramo: "Arquitectura de Sistemas de Software"
tema: "Caché y protocolos web"
tags:
  - arquisis/cache
  - indice
---

# Índice — Caché y protocolos web

La **caché** como táctica de performance (requerimientos, desafíos de consistencia, desalojo, cuándo no usarla), sus formas en la web (**navegador, proxy, CDN y proxy inverso**, con las reglas HTTP de frescura) y la evolución de **HTTP/1 a HTTP/3** como parte del stack.

## Contenido

1. [[01 - Caché conceptos desafíos y buenas prácticas]] — Proximidad, latencia y tamaño, jerarquía de la CPU, consistencia, coherencia, warm-up, LRU, LFU y FIFO, buenas prácticas y cuándo no cachear.
2. [[02 - Caché web navegador proxy CDN y proxy inverso]] — Caché del navegador, de red y de distribución, proxy inverso y CDN, Expires, Cache-Control, ETag y 304, buenas prácticas y caché por zona.
3. [[03 - Evolución de HTTP 1 a HTTP 3]] — Una conexión por petición, keep-alive, pipelining y HOL blocking, HTTP/2 multiplexado y HTTP/3 sobre QUIC.
