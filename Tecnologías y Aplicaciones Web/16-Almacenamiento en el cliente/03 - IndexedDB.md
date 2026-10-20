---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Almacenamiento en el cliente"
tags:
  - web
  - almacenamiento
  - indexeddb
  - origen/complemento
prerrequisitos:
  - "[[02 - localStorage y sessionStorage]]"
  - "[[01 - Código asíncrono y callbacks]]"
---

# IndexedDB

Web Storage alcanza para unos pocos strings, pero una aplicación que funciona offline (un cliente de correo, un editor de notas) necesita guardar miles de objetos, buscarlos por distintos campos y modificarlos de forma segura. Para eso el navegador incluye una base de datos completa: **IndexedDB**.

## Qué es

**IndexedDB** es un sistema de bases de datos **transaccional**, pero orientado a **objetos de JavaScript** en vez de tablas. Guarda y recupera objetos indexados por una **llave**. Su capacidad depende del navegador y del espacio en disco disponible, y puede llegar a varios gigabytes.

Trabajar con ella implica tres pasos:

1. **Definir el esquema**: crear los *object stores*, el equivalente de las tablas.
2. **Abrir una conexión** con la base de datos.
3. **Leer y escribir dentro de transacciones**.

La API es **asíncrona** y está basada en eventos (`onsuccess`, `onerror`), para no bloquear la página.

## Crear la base de datos

```javascript
let db;
const request = indexedDB.open('LibraryDB', 1);   // nombre y versión del esquema

request.onupgradeneeded = function (event) {
  db = event.target.result;
  if (!db.objectStoreNames.contains('books')) {
    // "id" es la llave; autoIncrement la genera si el objeto no la trae
    db.createObjectStore('books', { keyPath: 'id', autoIncrement: true });
  }
};

request.onsuccess = function (event) {
  db = event.target.result;
  console.log('IndexedDB initialized');
};

request.onerror = function (event) {
  console.error('IndexedDB error:', event.target.error);
};
```

`onupgradeneeded` solo se ejecuta cuando la base no existe o cuando se abre con un **número de versión mayor**. Es el único lugar donde se puede cambiar el esquema, algo parecido a una migración.

## Escribir en una transacción

```javascript
function addBooks() {
  const books = [
    { title: '1984', author: 'George Orwell' },
    { title: 'The Hobbit', author: 'J.R.R. Tolkien' },
  ];

  const transaction = db.transaction(['books'], 'readwrite');
  const store = transaction.objectStore('books');
  books.forEach((book) => store.add(book));

  transaction.oncomplete = () => console.log('Books added successfully');
  transaction.onerror = (event) => console.error('Transaction error:', event.target.error);
}
```

Después de la transacción, los libros quedan con `id: 1` e `id: 2`. Para leerlos, se abre otra transacción y se usa, por ejemplo, `store.getAll()` o `store.get(1)`.

> [!warning] Sin `autoIncrement`, cada objeto debe traer su llave
> Si el store se crea solo con `keyPath: 'id'` y se agrega un objeto sin campo `id`, `add` lanza un `DataError`. O se usa `autoIncrement: true`, o cada objeto incluye su propio `id`.

> [!tip] La transacción es todo o nada
> Si una de las escrituras de la transacción falla, se deshacen todas. Es la misma garantía de atomicidad de las bases de datos relacionales: no quedan datos a medio escribir.

## IndexedDB frente a Web Storage

| | **Web Storage** | **IndexedDB** |
|---|---|---|
| Datos | Solo strings | Objetos de JS, archivos, blobs |
| Capacidad | Unos 5 MB | Depende del disco (GBs) |
| API | Síncrona y simple | Asíncrona, con transacciones |
| Búsquedas | Solo por llave | Por llave y por índices |

En la práctica se suele usar una librería envoltorio (como `idb`) que expone la API con promesas en vez de eventos.

## Preguntas de repaso

> [!question]- ¿Cuándo se ejecuta `onupgradeneeded` y para qué sirve?
> Cuando la base se abre por primera vez o con un número de versión mayor que el guardado. Es el único momento en que se pueden crear o modificar los object stores, es decir, el esquema.

> [!question]- ¿Por qué falla `store.add({ title: '1984' })` en un store con `keyPath: 'id'` y sin `autoIncrement`?
> Porque el objeto no trae la llave que el store exige y nadie la genera. IndexedDB lanza un `DataError`.

> [!question]- ¿Qué ventaja tiene IndexedDB sobre `localStorage` para una aplicación offline?
> Guarda objetos completos (y archivos) sin convertirlos a texto, con mucha más capacidad, búsquedas por índices y transacciones atómicas, sin bloquear la página.
