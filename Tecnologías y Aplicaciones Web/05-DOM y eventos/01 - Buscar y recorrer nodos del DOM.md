---
ramo: "Tecnologías y Aplicaciones Web"
tema: "DOM y eventos"
tags:
  - web
  - javascript
  - dom
  - origen/complemento
prerrequisitos:
  - "[[05 - DOM, CSSOM y critical rendering path]]"
  - "[[05 - Funciones, clases y módulos en JavaScript]]"
---

# Buscar y recorrer nodos del DOM

El DOM es el árbol que el navegador arma a partir del HTML para poder interpretarlo y dibujarlo. Lo importante para JavaScript es que ese árbol **se puede consultar y modificar**, y que el usuario ve los cambios de inmediato. Antes de cambiar un elemento hay que encontrarlo: esta nota cubre cómo llegar a un nodo y cómo moverse entre nodos vecinos.

## El HTML DOM como interfaz

El HTML DOM es un modelo de objetos estandarizado y una interfaz de programación para HTML. Define:

- los elementos HTML como **objetos**;
- las **propiedades** de todos los elementos;
- los **métodos** para acceder a ellos;
- los **eventos** de todos los elementos.

Es decir, es el estándar de cómo obtener, cambiar, agregar o eliminar elementos HTML. En el navegador está disponible como variable global: `window.document`, o simplemente `document`.

## Jerarquía de nodos

El nodo raíz (el tag `<html>`) está en `document.documentElement`, y desde ahí el árbol sigue la estructura del HTML: `document.head` y `document.body`.

![Árbol DOM con nodos de texto y comentario](adjuntos/%C3%81rbol%20DOM%20con%20nodos%20de%20texto%20y%20comentario.png)

> [!example]- Transcripción de la imagen
> - `html` tiene tres hijos: `head`, un `#text` y `body`.
> - `head` contiene `#text`, `meta`, `#text`, `title` (con su propio `#text`) y `#text`.
> - `body` contiene, alternados con nodos `#text`, un `h1` (con texto), un `p` (con texto), un `img` y un comentario `<!-- -->`.
> - Los elementos están en azul, los textos en amarillo o verde y el comentario en morado.

> [!warning] También los espacios son nodos
> Los saltos de línea e indentación entre tags generan nodos `#text`. Por eso `firstChild` puede devolver un texto vacío en vez del primer elemento; para saltarlos existen las variantes `…ElementChild` y `…ElementSibling`.

## Búsqueda de nodos

**Por id.** `document.getElementById(id)` encuentra el elemento con ese `id`, esté donde esté:

![Buscar un elemento con getElementById](adjuntos/Buscar%20un%20elemento%20con%20getElementById.png)

> [!example]- Transcripción de la imagen
> Un `div` con `id="elem"` contiene otro `div` con `id="elem-content"` y el texto "Element". El script hace `let elem = document.getElementById('elem');` y luego `elem.style.background = 'red';` para pintar el fondo de rojo.

**Por selector CSS.** `elem.querySelectorAll(css)` retorna todos los elementos dentro de `elem` que calzan con el selector, y `querySelector(css)` retorna solo el primero. Es la forma **más común y versátil**, porque acepta cualquier selector CSS:

![Buscar elementos con querySelectorAll](adjuntos/Buscar%20elementos%20con%20querySelectorAll.png)

> [!example]- Transcripción de la imagen
> Dos `ul`: el primero con los `li` "The" y "test", el segundo con "has" y "passed". El script busca `document.querySelectorAll('ul > li:last-child')`, es decir, los `li` que son el último hijo de su `ul`, y en un `for...of` muestra con `alert(elem.innerHTML)` los textos "test" y "passed".

**Con `getElementsBy*`.** Son métodos más antiguos:

- `elem.getElementsByTagName(tag)` busca por nombre de tag (o `'*'` para todos);
- `elem.getElementsByClassName(className)` busca por clase CSS;
- `document.getElementsByName(name)` busca por el atributo `name`.

![Comparación de métodos de búsqueda en el DOM](adjuntos/Comparaci%C3%B3n%20de%20m%C3%A9todos%20de%20b%C3%BAsqueda%20en%20el%20DOM.png)

> [!example]- Transcripción de la imagen
> Tabla con las columnas Método, Busca por…, ¿Puede llamar a un elemento? y ¿Vivo?:
> - `querySelector` y `querySelectorAll`: selector CSS; sí se pueden llamar sobre un elemento; no son vivos.
> - `getElementById`: `id`; solo sobre `document`; no es vivo.
> - `getElementsByName`: `name`; solo sobre `document`; vivo.
> - `getElementsByTagName`: etiqueta o `'*'`; sobre un elemento; vivo.
> - `getElementsByClassName`: clase; sobre un elemento; vivo.
> - Nota: una colección **viva** "siempre refleja el estado actual del documento y se actualiza cuando el documento cambia".

> [!tip] Viva frente a estática
> `getElementsBy*` devuelve una colección viva: si después se agrega un elemento que calza, aparece solo en la colección. `querySelectorAll` devuelve una "foto" del momento de la búsqueda.

## Propiedades de un nodo

- **Identidad**: `nodeName` (`P`, `DIV` o `#text`), `nodeType` (1 para elementos, 3 para texto) y `nodeValue` (el contenido de un nodo de texto).
- **Jerarquía**: `parentNode`; `nextSibling` y `previousSibling`; `firstChild` y `lastChild`; y sus variantes que solo consideran elementos (`nextElementSibling`, `firstElementChild`, etc.).
- **Atributos**: `getAttribute` y `setAttribute`.
- **Contenido**: `textContent` (todo el texto), `innerText` (el texto "legible", según el CSS), `innerHTML` (el HTML interior) y `outerHTML` (incluye al propio elemento).
- **Estilo**: `element.classList.add('mi-clase')` y `element.style.color`.

![Hijos de un nodo p con texto y negrita](adjuntos/Hijos%20de%20un%20nodo%20p%20con%20texto%20y%20negrita.png)

> [!example]- Transcripción de la imagen
> Para `<p>Curso <b>IIC2513</b> 2025-1</p>`, el nodo `P` (nodeType 1) tiene como `firstChild` un `#text` con "Curso ", como `firstElementChild` el nodo `B` y como `lastChild` un `#text` con el año. El nodo `B` tiene un único hijo (`firstChild` y `lastChild` a la vez), un `#text` con "IIC2513".

## Preguntas de repaso

> [!question]- ¿Por qué `firstChild` de un `<ul>` indentado no es el primer `<li>`?
> Porque el salto de línea y los espacios entre `<ul>` y `<li>` forman un nodo de texto, que es el verdadero primer hijo. Para obtener el primer elemento se usa `firstElementChild`.

> [!question]- ¿Qué ventaja tiene `querySelectorAll` sobre `getElementsByClassName`?
> Acepta cualquier selector CSS (combinadores, pseudoclases, atributos), así que una sola llamada expresa búsquedas complejas como `ul > li:last-child`.

> [!question]- ¿Qué significa que una colección sea "viva"?
> Que se actualiza sola cuando el documento cambia: si se agrega o elimina un elemento que calza con la búsqueda, la colección lo refleja sin volver a buscar.
