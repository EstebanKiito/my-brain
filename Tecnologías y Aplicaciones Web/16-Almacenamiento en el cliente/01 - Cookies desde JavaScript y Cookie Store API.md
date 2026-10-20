---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Almacenamiento en el cliente"
tags:
  - web
  - almacenamiento
  - cookies
  - javascript
  - origen/complemento
prerrequisitos:
  - "[[01 - Cookies y el header Set-Cookie]]"
---

# Cookies desde JavaScript y Cookie Store API

Cada vez hay más formas de guardar datos **en el navegador**, con distinta duración y complejidad: cookies, Web Storage, IndexedDB y la Cache API. Esta nota abre el tema: por qué conviene guardar datos del lado del cliente y cómo se manejan las cookies directamente desde JavaScript, sin pasar por el servidor.

## ¿Por qué almacenar del lado del cliente?

- **Personalizar** el sitio: orden de elementos, colores, tamaño de fuente preferido.
- **Persistir la actividad** entre páginas: el contenido de un carro de compras, si el usuario ya inició sesión.
- **Cargar más rápido** y consumir menos recursos, al reutilizar datos y archivos ya descargados, e incluso funcionar **sin conexión**.
- **Guardar lo que genera la aplicación** para usarlo offline.

| Mecanismo | En pocas palabras |
|---|---|
| **Cookies** | Lo más tradicional; pocos datos, que viajan en cada request |
| **Web Storage** | `localStorage` y `sessionStorage`: pares de strings, solo desde JavaScript |
| **IndexedDB** | Una base de datos transaccional de objetos en el navegador |
| **Cache API** | Pares request-respuesta, para cargar rápido y funcionar offline |

## Cookies con `document.cookie`

Además de los headers HTTP, las cookies se manejan desde JavaScript con `document.cookie`. Su interfaz es extraña: **asignar** agrega o modifica **una** cookie, mientras que **leer** devuelve **todas** en un solo string.

```javascript
// Crear o modificar una cookie (no borra las demás)
document.cookie = 'theme=dark; path=/; max-age=' + 24 * 60 * 60;   // expira en 24 horas

// Leer: document.cookie es un string 'theme=dark; lang=es'
const cookies = Object.fromEntries(
  document.cookie.split('; ').map((c) => c.split('='))
);
console.log(cookies.theme);   // 'dark'

// Eliminar: max-age=0
document.cookie = 'theme=; path=/; max-age=0';
```

Usos típicos: recordar la sesión, guardar preferencias y hacer seguimiento de la actividad.

> [!warning] `HttpOnly` no se ve desde JavaScript
> Las cookies marcadas `HttpOnly` no aparecen en `document.cookie`. Es lo esperado: por eso son las adecuadas para las sesiones, ya que un script malicioso no puede leerlas.

## Cookie Store API

`document.cookie` obliga a parsear strings a mano. **CookieStore** (con **CookieStoreManager**) es una API moderna, basada en **promesas**, para leer, escribir y **observar cambios** en las cookies de forma estructurada:

```javascript
// Crear
await cookieStore.set('theme', 'dark', {
  path: '/',
  expires: Date.now() + 24 * 60 * 60 * 1000,   // en 24 horas (ms)
});

// Leer una cookie específica
const cookie = await cookieStore.get('theme');
console.log(cookie ? cookie.value : '¡La cookie "theme" no existe!');

// Eliminar
await cookieStore.delete('theme');

// Reaccionar a cambios (por ejemplo, desde otra pestaña)
cookieStore.addEventListener('change', (event) => console.log(event.changed));
```

Sus aplicaciones son una gestión estructurada de las cookies y la sincronización en tiempo real.

> [!tip] Cookies solo para lo que el servidor necesita
> Las cookies viajan en **cada** request al dominio y tienen un límite de unos 4 KB. Si el dato solo lo usa el frontend (el tema visual, un borrador), conviene Web Storage, que no se envía al servidor.

## Preguntas de repaso

> [!question]- ¿Por qué `document.cookie = 'a=1'` no borra las demás cookies?
> Porque asignar a `document.cookie` no reemplaza el string completo: crea o actualiza solo la cookie indicada. Leerlo, en cambio, devuelve todas las cookies visibles concatenadas.

> [!question]- ¿Cómo se elimina una cookie desde JavaScript?
> Asignándola con `max-age=0` (o con una fecha de expiración pasada) y el mismo `path`, o con `cookieStore.delete(nombre)`.

> [!question]- ¿Qué mejora la Cookie Store API respecto de `document.cookie`?
> Trabaja con objetos y promesas en vez de un string que hay que parsear, permite leer una cookie por nombre y avisa con un evento cuando las cookies cambian.
