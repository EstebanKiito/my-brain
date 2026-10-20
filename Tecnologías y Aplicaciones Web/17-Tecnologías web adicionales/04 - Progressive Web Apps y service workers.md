---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Tecnologías web adicionales"
tags:
  - web
  - pwa
  - service-workers
  - origen/complemento
prerrequisitos:
  - "[[04 - Caché, Cache API y CDN]]"
  - "[[06 - Capas de la web, TCP, UDP y TLS]]"
---

# Progressive Web Apps y service workers

¿Puede una aplicación web comportarse como una app móvil, con ícono en la pantalla de inicio, funcionando sin conexión y recibiendo notificaciones? Eso buscan las **Progressive Web Apps** (PWAs). La pieza que lo hace posible es el **service worker**, un script que se interpone entre la aplicación y la red.

## Qué es una PWA

Una **PWA** es un conjunto de técnicas para crear aplicaciones web que ofrecen una experiencia **similar a la de una app móvil**:

- funcionar **offline**;
- recibir **notificaciones push**;
- guardar recursos en una **caché local**;
- ser **segura**;
- verse y responder con rapidez **casi nativa**.

| Enfoque | Tecnologías |
|---|---|
| **Nativo** | iOS: Swift u Objective-C. Android: Kotlin o Java |
| **Multiplataforma o híbrido** | React Native (JS), Flutter (Dart), Xamarin (C#), Ionic (JS), Unity (C#) |
| **Basado en web** | Progressive Web Apps, Apache Cordova |

Las PWAs buscan apps de calidad usando **solo tecnologías web**, lo que es más barato y más simple: un solo código para todas las plataformas. Además reducen la **fricción de instalación**: estar en una tienda de apps ayuda poco a que la encuentren, mientras que una PWA se descubre desde un buscador y se instala desde el navegador.

## Componentes clave

1. **HTTPS**: HTTP sobre TLS; las PWAs y los service workers lo exigen.
2. **Web App Manifest**: la información para instalar la app.
3. **Service workers**: el intermediario que permite funcionar offline.
4. **Cache API**: dónde el service worker guarda los recursos.
5. **Notificaciones push**.

## Web App Manifest

Es un archivo JSON (extensión oficial `.webmanifest`, aunque también se usa `.json`) con la información de la aplicación que el navegador necesita para **instalarla**: nombre, íconos, URL de inicio, orientación y pantalla de presentación (*splash screen*).

```json
{
  "short_name": "MDN",
  "name": "MDN Web Docs",
  "icons": [
    { "src": "/favicon-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/favicon-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```

Se enlaza desde el `head` de **todas** las páginas, como una hoja de estilos: `<link rel="manifest" href="manifest.json" />`. `"display": "standalone"` hace que la app instalada se abra sin la barra del navegador.

## Service workers

Un **web worker** ejecuta JavaScript fuera del hilo principal. Un **service worker** es un tipo especial que actúa como **proxy** entre la aplicación, el navegador y la red:

![Service worker entre la PWA y la red](adjuntos/Service%20worker%20entre%20la%20PWA%20y%20la%20red.png)

> [!example]- Transcripción de la imagen
> En el dispositivo del usuario (navegador), *Your PWA* (el cliente) se comunica con el **Service Worker** (*proxy middleware*), y este con la nube: *Your Server* y *Cross-Domain Servers / CDNs*.

- **Intercepta** las requests de la aplicación y decide: responder desde la caché, ir a la red o combinar ambas cosas.
- Permite experiencias **offline**, notificaciones **push** y sincronización en segundo plano.
- Funciona de forma **independiente** de la página: puede recibir mensajes con el navegador cerrado, queda inactivo cuando no se usa y se reactiva cuando hace falta.
- Una vez instalado, controla todas las páginas de su **scope** (por defecto, la carpeta donde está el archivo y sus subcarpetas).

```javascript
// app.js: registrar el service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/service-worker.js')
      .then((registration) => console.log('Service Worker registered with scope:', registration.scope))
      .catch((error) => console.error('Registration failed:', error));
  });
}
```

## Ciclo de vida

![Ciclo de vida de un service worker](adjuntos/Ciclo%20de%20vida%20de%20un%20service%20worker.png)

> [!example]- Transcripción de la imagen
> 1. El usuario navega a una URL. 2. Durante el registro (*Register*), el navegador descarga, parsea y ejecuta el service worker. 3. Apenas se ejecuta, se dispara el evento *install*. 4. Si tiene éxito, queda **Activated** y puede controlar clientes y manejar eventos.

1. **Registro**: le dice al navegador dónde está el service worker y su scope; solo ocurre la primera vez o cuando el archivo cambia.
2. **Instalación**: se prepara para usarse; típicamente se llena la caché con los recursos estáticos.
3. **Activación**: queda habilitado para responder en las próximas cargas de página.

```javascript
// service-worker.js
const CACHE_NAME = 'my-cache';
const urlsCache = ['css/style.css', 'images/myIcon.png', 'scripts/index.js'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsCache)));
});

self.addEventListener('activate', () => console.log('Service Worker: Activado'));

self.addEventListener('fetch', (event) => {
  // "cache first": responder desde la caché y, si no está, ir a la red
  event.respondWith(caches.match(event.request).then((cached) => cached || fetch(event.request)));
});
```

> [!warning] Un service worker nuevo no toma el control de inmediato
> Si cambia el archivo, la versión nueva se instala pero queda esperando hasta que se cierren todas las pestañas controladas por la anterior. Por eso un cambio a veces "no se ve" al recargar.

## Preguntas de repaso

> [!question]- ¿Qué permite a una PWA funcionar sin conexión?
> El service worker, que intercepta las requests y responde con recursos guardados en la Cache API cuando no hay red.

> [!question]- ¿Para qué sirve el Web App Manifest?
> Le entrega al navegador la información para instalar la aplicación: nombre, íconos, URL de inicio y modo de visualización, como `standalone` para abrirse sin la interfaz del navegador.

> [!question]- ¿Qué ocurre en la fase de instalación de un service worker?
> El navegador lo prepara para usarse; normalmente se abre una caché y se guardan los recursos estáticos que la aplicación necesitará offline.
