---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Almacenamiento en el cliente"
tags:
  - web
  - almacenamiento
  - web-storage
  - origen/complemento
prerrequisitos:
  - "[[01 - Cookies desde JavaScript y Cookie Store API]]"
---

# localStorage y sessionStorage

Muchos datos solo le interesan al frontend: el tema oscuro, un borrador, el carro de compras antes de pagar. No tiene sentido que viajen al servidor en cada request, como las cookies. La **Web Storage API** ofrece dos almacenes de pares llave-valor que se controlan completamente desde JavaScript: `localStorage` y `sessionStorage`.

## localStorage

- Comparte sus valores entre **todas las pestañas y ventanas** del mismo origen.
- Sus datos **no expiran**: sobreviven a reinicios del navegador e incluso del sistema operativo, hasta que se borran.

```javascript
localStorage.setItem('test', 'cookie');
// ... después de cerrar la pestaña o el navegador:
localStorage.getItem('test');      // 'cookie'
localStorage.removeItem('test');
localStorage.clear();              // borra todo el almacén del origen
```

## sessionStorage

Se usa menos, porque es más limitado:

- Sus valores existen **solo en la pestaña actual**; otra pestaña del mismo sitio tiene su propio `sessionStorage`.
- Los datos **sobreviven a una recarga**, pero **no a cerrar la pestaña**.

```javascript
sessionStorage.setItem('test', 'cookie');
// después de recargar la página:
sessionStorage.getItem('test');    // 'cookie'
// después de cerrar la pestaña y volver a abrir el sitio:
sessionStorage.getItem('test');    // null
```

## Lo común a ambos

- Guardan **pares llave-valor**, y tanto la llave como el valor son **strings**.
- La capacidad es de unos **5 MB o más**, según el navegador.
- Los datos están vinculados al **origen**: dominio, puerto y protocolo. `http://sitio.cl` y `https://sitio.cl` no comparten almacén.
- No viajan al servidor: solo los lee JavaScript.

La diferencia es cuánto sobreviven los datos: una recarga (`sessionStorage`) o un reinicio completo del navegador (`localStorage`).

> [!warning] Todo se convierte en string
> Si se guarda algo que no es string, JavaScript lo convierte sin avisar: `setItem('n', 42)` guarda `'42'`, y un objeto se guarda como el inútil `'[object Object]'`. Para guardar objetos hay que serializarlos:
> ```javascript
> localStorage.setItem('carro', JSON.stringify([{ id: 1, qty: 2 }]));
> const carro = JSON.parse(localStorage.getItem('carro'));   // carro[0].qty === 2
> ```

## Cuándo usar cada uno

![Comparación de localStorage, sessionStorage, cookies e IndexedDB](adjuntos/Comparaci%C3%B3n%20de%20localStorage,%20sessionStorage,%20cookies%20e%20IndexedDB.png)

> [!example]- Transcripción de la imagen
> Tabla con criterios para Local Storage, Session Storage y Cookies:
> - **Capacidad**: 5-10 MB, 5-10 MB y 4 KB.
> - **Expiración automática**: no, sí (al cerrar la pestaña) y sí.
> - **Accesible desde el servidor**: no, no y sí.
> - **Se envía en las requests HTTP**: no, no y sí.
> - **Persistencia**: hasta que se borra a mano, hasta que se cierra la pestaña, y según la expiración configurada.
> - Al costado, **IndexedDB**: su límite depende del navegador y del espacio en disco (pueden ser GBs).

| Caso | Mejor opción |
|---|---|
| Preferencias de la interfaz que deben persistir | `localStorage` |
| Estado temporal de un formulario o de un flujo en una pestaña | `sessionStorage` |
| Datos que el servidor debe recibir (como la sesión) | Cookie `HttpOnly` |
| Muchos datos estructurados u offline | IndexedDB |

> [!warning] Nunca guardar tokens en Web Storage
> Todo script que corre en la página puede leer `localStorage`. Un ataque XSS se llevaría cualquier token de autenticación guardado ahí. Las credenciales van en cookies `HttpOnly`.

## Preguntas de repaso

> [!question]- Un usuario abre el mismo sitio en dos pestañas. ¿Comparten `localStorage`? ¿Y `sessionStorage`?
> Comparten `localStorage`, porque es del origen completo. No comparten `sessionStorage`: cada pestaña tiene el suyo.

> [!question]- ¿Qué se guarda si se hace `localStorage.setItem('obj', {a: 1})`?
> El string `'[object Object]'`, porque Web Storage convierte todo a string. Para guardar el objeto hay que usar `JSON.stringify` y luego `JSON.parse` al leerlo.

> [!question]- ¿Por qué una preferencia visual conviene más en `localStorage` que en una cookie?
> Porque el servidor no la necesita: en una cookie viajaría inútilmente en cada request. `localStorage` la guarda en el navegador, sin expirar y con más capacidad.
