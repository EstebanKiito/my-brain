---
ramo: "Tecnologías y Aplicaciones Web"
tema: "DOM y eventos"
tags:
  - web
  - javascript
  - dom
  - origen/complemento
prerrequisitos:
  - "[[01 - Buscar y recorrer nodos del DOM]]"
---

# Crear y modificar elementos del DOM

Encontrar nodos es la mitad del trabajo; la otra mitad es **cambiar la página**: crear elementos, darles contenido y atributos, e insertarlos en el árbol. Así se construye HTML dinámicamente, por ejemplo una lista que se arma con datos recibidos del servidor.

## Ejecutar JavaScript desde HTML

El tag `<script>` con el atributo `src` indica la ruta (URL o archivo) del código a ejecutar:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Ejemplo con JS</title>
  </head>
  <body>
    <p id="importante">Hola</p>
    <script src="programa.js"></script>
  </body>
</html>
```

> [!warning] El script necesita que el DOM ya exista
> El navegador ejecuta el script en cuanto lo encuentra. Si está en el `head`, el `body` todavía no se ha parseado y `getElementById` devuelve `null`. Por eso el `<script>` suele ir al final del `body` o lleva el atributo `defer`, que lo ejecuta cuando el documento terminó de cargarse.

## Leer el documento

![Acceder al documento desde JavaScript](adjuntos/Acceder%20al%20documento%20desde%20JavaScript.png)

> [!example]- Transcripción de la imagen
> - `console.log(document.URL);` imprime el link donde está el documento.
> - `document.children;` entrega la lista de hijos del documento: `[<html>]`.
> - `const elemento = document.getElementById("importante");` obtiene el elemento con `id="importante"`.
> - `const parrafo = document.createElement("p");` crea un elemento cuyo tag es `<p>`.

## Crear nodos e insertarlos

`document.createElement(tag)` crea un elemento y `document.createTextNode(texto)` crea un nodo de texto. Ninguno aparece en pantalla hasta que se **inserta** en el árbol con `appendChild` (o `append`, `prepend`, `insertBefore`):

![Crear un párrafo con un nodo de texto](adjuntos/Crear%20un%20p%C3%A1rrafo%20con%20un%20nodo%20de%20texto.png)

> [!example]- Transcripción de la imagen
> `const parrafo = document.createElement("p");` crea el párrafo. `const texto = document.createTextNode("¡Soy un texto >.<!");` crea un nodo de texto. `parrafo.appendChild(texto);` agrega el texto al párrafo.

## Clases, id y atributos

![Crear una imagen con clase, id y atributo](adjuntos/Crear%20una%20imagen%20con%20clase%2C%20id%20y%20atributo.png)

> [!example]- Transcripción de la imagen
> `const elemento = document.createElement("img");` crea una imagen. `elemento.className = "importante";` le define la clase. `elemento.id = "principal";` le da un id único. `elemento.setAttribute("width", 200);` le define un atributo.

Todo junto, el flujo completo para agregar contenido a la página es: crear, configurar e insertar.

```javascript
const lista = document.querySelector('#cursos');
for (const sigla of ['IIC2513', 'IIC2413', 'IIC2133']) {
  const item = document.createElement('li');
  item.textContent = sigla;           // más simple que createTextNode + appendChild
  item.classList.add('curso');
  lista.appendChild(item);
}
```

> [!tip] `textContent` frente a `innerHTML`
> `textContent` inserta texto literal, de modo que un `<b>` se ve como texto. `innerHTML` interpreta el string como HTML. Con datos que vienen del usuario o de un servidor hay que preferir `textContent`, porque `innerHTML` permite inyectar HTML y scripts (un ataque XSS).

## Preguntas de repaso

> [!question]- ¿Por qué un elemento creado con `createElement` no aparece en la página?
> Porque solo existe en memoria. Recién al insertarlo en el árbol (con `appendChild` u otro método equivalente) forma parte del DOM y el navegador lo dibuja.

> [!question]- ¿Qué pasa si un script en el `head` busca un elemento del `body` sin `defer`?
> No lo encuentra (obtiene `null`), porque el script se ejecuta antes de que el navegador haya parseado el `body`.

> [!question]- ¿Por qué es riesgoso usar `innerHTML` con texto ingresado por el usuario?
> Porque el texto se interpreta como HTML: un usuario podría insertar etiquetas o scripts que se ejecuten en la página de otros (XSS). `textContent` lo trata como texto plano.
