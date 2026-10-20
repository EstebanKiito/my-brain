---
ramo: "Tecnologías y Aplicaciones Web"
tema: "DOM y eventos"
tags:
  - web
  - javascript
  - eventos
  - origen/complemento
prerrequisitos:
  - "[[02 - Crear y modificar elementos del DOM]]"
  - "[[01 - Código asíncrono y callbacks]]"
---

# Eventos y event listeners

Una página interactiva reacciona a lo que pasa: un click, una tecla, una ventana que cambia de tamaño. Cada una de esas cosas es un **evento**. La forma de reaccionar es **suscribirse** al evento: se registra un callback y el navegador lo ejecuta cuando el evento ocurre. Es la asincronía aplicada a la interfaz.

## Tipos de eventos

- **Mouse**: selección, clicks, movimiento, *hover*.
- **Teclado**: presionar teclas.
- **Ventana**: cambio de tamaño (*resize*) o cierre del navegador.
- **Foco**: se gana (`focusin`) o se pierde (`blur`).
- **Tiempo**: temporizadores.
- **Formularios**: cambio de valor en un input, envío de un form.
- **Otros**: cambia el contenido de un elemento, termina de cargar la página o una imagen, ocurre una excepción.

## Event listener

Para definir un manejador de eventos se especifican tres cosas: **qué pasó** (el evento, por ejemplo `"click"`), **dónde pasó** (el elemento, por ejemplo un botón) y **qué hacer** (el callback).

![Event listener que cambia el color de fondo](adjuntos/Event%20listener%20que%20cambia%20el%20color%20de%20fondo.png)

> [!example]- Transcripción de la imagen
> - `const btn = document.querySelector("button");` obtiene el botón.
> - Una función `random(number)` retorna `Math.floor(Math.random() * (number + 1))`.
> - `btn.addEventListener("click", () => { … })` arma `` const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})` `` y lo asigna a `document.body.style.backgroundColor`.
> - Recuadros numerados: **1** marca `"click"` (qué pasó), **2** marca `btn` (dónde pasó) y **3** marca el cuerpo del callback (qué hacer).

Hay dos formas de registrar el listener:

![Dos formas de definir un event listener](adjuntos/Dos%20formas%20de%20definir%20un%20event%20listener.png)

> [!example]- Transcripción de la imagen
> 1. En el código HTML, atado a un elemento particular: `<button onclick="algunaFuncion();"></button>`.
> 2. Con JS usando el DOM, más mantenible y flexible: `btn.addEventListener("click", () => {`.

> [!tip] Preferir `addEventListener`
> Mantiene el comportamiento en JavaScript y la estructura en HTML. Además permite registrar varios listeners para el mismo evento y quitarlos con `removeEventListener`.

## El objeto `Event`

Cada listener recibe un objeto `Event` con información de lo ocurrido:

- `type`: el nombre del evento (`"click"`).
- `timeStamp`: el momento en que se creó.
- `target`: el elemento que **despachó** el evento (donde realmente se hizo click).
- `currentTarget`: el elemento que **tiene** el listener.

```javascript
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();               // evita que el navegador recargue la página
  console.log(event.type, event.target === event.currentTarget);
});
```

## Propagación: por qué `target` y `currentTarget` difieren

![target y currentTarget en capturing y bubbling](adjuntos/target%20y%20currentTarget%20en%20capturing%20y%20bubbling.png)

> [!example]- Transcripción de la imagen
> Un *Child div* dentro de un *Parent div*. Al hacer click en el hijo, el evento primero baja desde afuera hacia el hijo (**Capturing**, flecha azul), donde un listener del padre ve `{ currentTarget: parent, target: child }`. En el hijo se ve `{ currentTarget: child, target: child }`. Luego sube hacia afuera (**Bubbling**, flecha amarilla), y el listener del padre vuelve a ver `{ currentTarget: parent, target: child }`.

Un evento no ocurre solo en el elemento clickeado: recorre el árbol. Primero baja desde la raíz hasta el elemento (**capturing**) y luego sube de vuelta hasta la raíz (**bubbling**). Por defecto los listeners se ejecutan en la fase de bubbling. Por eso un listener puesto en un contenedor recibe los clicks de todos sus hijos: `target` es el hijo clickeado y `currentTarget` es el contenedor.

> [!warning] Delegación de eventos
> Gracias al bubbling basta **un** listener en la lista para manejar los clicks de todos sus `li`, incluso de los que se agreguen después; se identifica cuál fue con `event.target`. Es más eficiente que poner un listener en cada elemento.

## Preguntas de repaso

> [!question]- ¿Cuáles son las tres piezas de un event listener?
> El evento que interesa (qué pasó), el elemento sobre el que se registra (dónde pasó) y el callback que se ejecuta cuando ocurre (qué hacer).

> [!question]- Un listener está en un `ul` y se hace click en un `li`. ¿Qué valen `target` y `currentTarget`?
> `target` es el `li` (quien despachó el evento) y `currentTarget` es el `ul` (quien tiene el listener). El listener se ejecuta porque el evento sube por bubbling desde el `li`.

> [!question]- ¿Para qué sirve `event.preventDefault()` en un `submit`?
> Para cancelar la acción por defecto del navegador, que es enviar el formulario y recargar la página. Así JavaScript puede validar o enviar los datos con `fetch` sin perder el estado de la página.
