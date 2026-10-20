---
ramo: "Tecnologías y Aplicaciones Web"
tema: "React"
tags:
  - web
  - react
  - jsx
  - frontend
  - origen/complemento
prerrequisitos:
  - "[[02 - Crear y modificar elementos del DOM]]"
  - "[[03 - Eventos y event listeners]]"
---

# React, JSX y Virtual DOM

Con el DOM y los eventos ya se puede construir cualquier interfaz, pero a mano todo se complica: cada cambio en los datos obliga a encontrar los nodos afectados y actualizarlos uno por uno, y es fácil que la pantalla quede desincronizada. **React** resuelve eso: se describe **cómo debe verse** la interfaz para ciertos datos y React se encarga de actualizar el DOM.

## Qué es React

React es una **librería** de JavaScript, de código abierto, para construir interfaces de usuario en **aplicaciones dinámicas**, donde los datos van cambiando. La inició Facebook (primera versión en 2013) y hoy la mantienen la empresa y la comunidad; la versión 19 salió en diciembre de 2024.

- En el patrón **MVC**, React es la **vista**.
- Es una librería y no un framework, porque solo especifica el proceso de *rendering*. Todo lo demás (rutas, manejo de datos, llamadas al servidor) queda a elección del proyecto.
- Se basa en **componentes**, que se usan como si fueran tags:

```jsx
function Video({ video }) {
  return (
    <div>
      <Thumbnail video={video} />
      <a href={video.url}>
        <h3>{video.title}</h3>
        <p>{video.description}</p>
      </a>
      <LikeButton video={video} />
    </div>
  );
}
```

Conviene usarlo cuando hay muchos cambios de estado que se relacionan o dependen entre sí y el contenido se genera dinámicamente: dashboards y herramientas de visualización, interfaces basadas en componentes, casos donde el DOM debe actualizarse rápido, y para reutilizar componentes entre web y móvil.

## Arquitectura basada en componentes

Un **componente** es un trozo de código que describe una porción de la interfaz. Es reutilizable, fácil de mantener, y los componentes se pueden **componer** entre sí.

![App de tareas dividida en componentes](adjuntos/App%20de%20tareas%20dividida%20en%20componentes.png)

> [!example]- Transcripción de la imagen
> Una lista de tareas con recuadros de colores que marcan sus componentes: el contenedor completo (amarillo); el formulario para agregar con su botón "Add" (rojo); la lista (morado), que contiene tres tareas, cada una un componente (azul): "Preparar diapositivas", "Hacer la clase" y "Subir diapositivas"; y el botón "Delete all done" (verde).

## Rendering y elementos

Una aplicación React se dibuja **sobre un elemento que ya existe** en el DOM, normalmente un `<div id="root">`. A partir de ese nodo, React dibuja todo hacia abajo:

```jsx
import ReactDOM from 'react-dom/client';
import { App } from './App.jsx';

const rootNode = document.getElementById('root');
ReactDOM.createRoot(rootNode).render(<App />);
```

La unidad mínima de una aplicación React es el **elemento**, que se traduce directamente en elementos del DOM. Se crea con `createElement(type, props, ...children)`:

- `type`: el nombre del tag o un componente de React.
- `props`: las propiedades con que se crea (atributos en HTML, *properties* en JS).
- `children` (opcional): cero o más hijos, que pueden ser elementos, strings o números.

```jsx
const element = React.createElement('h1', null, 'Un título');   // equivale a <h1>Un título</h1>
```

## JSX

**JSX** (*JavaScript + XML*) es una extensión de la sintaxis de JavaScript, también creada por Facebook. Se parece a un lenguaje de plantillas, pero tiene todo el poder de JavaScript: entre llaves se puede poner cualquier **expresión**. React no lo exige, pero es mucho más legible que llamar a `createElement` directamente. Una herramienta de compilación (como Vite) lo traduce a esas llamadas.

![createElement frente a JSX y su HTML resultante](adjuntos/createElement%20frente%20a%20JSX%20y%20su%20HTML%20resultante.png)

> [!example]- Transcripción de la imagen
> - Izquierda: `Greeting({ name })` retorna `createElement('h1', { className: 'greeting' }, 'Hello ', createElement('i', null, name), '. Welcome!')`.
> - Derecha, lo mismo en JSX: `<h1 className='greeting'>Hello <i>{name}</i>. Welcome!</h1>`.
> - Abajo, el HTML resultante dentro de `<div id="root">`: `<h1 class="greeting">Hello <i>Taylor</i>. Welcome!</h1>`.

![Sintaxis regular frente a JSX](adjuntos/Sintaxis%20regular%20frente%20a%20JSX.png)

> [!example]- Transcripción de la imagen
> Con sintaxis "regular", `App` retorna `createElement(Greeting, { name: 'Taylor' })`. Con JSX retorna `<Greeting name='Taylor' />`.

```jsx
const user = { name: 'Antonio', avatarUrl: '/a.png' };
const movies = ['Alien', 'Up', 'Coco'];
const profile = (
  <div>
    <h1>Hello, {user.name}!</h1>
    <img src={user.avatarUrl} alt="avatar" />
    <ul>
      {movies.map((m) => <li key={m}>{m}</li>)}
    </ul>
  </div>
);
```

> [!warning] JSX no es HTML
> Los atributos usan nombres de JavaScript (`className` en vez de `class`, `onClick` en vez de `onclick`), todo tag debe cerrarse (`<img />`) y las listas generadas con `map` necesitan una `key` única por elemento, para que React sepa cuál cambió.

## Virtual DOM

Modificar el DOM real es caro, porque cada cambio puede obligar al navegador a recalcular el layout y repintar. React mantiene en memoria un **Virtual DOM**: una representación "ideal" de la interfaz, sincronizada con el DOM real por la librería `ReactDOM`. Cuando cambia algo, React genera el nuevo Virtual DOM, lo **compara** (*diff*) con el anterior y aplica al DOM real **solo las diferencias**.

![Diff del Virtual DOM aplicado al DOM real](adjuntos/Diff%20del%20Virtual%20DOM%20aplicado%20al%20DOM%20real.png)

> [!example]- Transcripción de la imagen
> Dos árboles de componentes (*Previous* y *Current*) generan dos versiones del Virtual DOM; la actual tiene un nodo extra. Un *Diff* entre ambas produce un *PATCH*, que se aplica (*Apply*) al Real DOM: solo se agrega el nodo nuevo, marcado con un círculo rojo.

## Preguntas de repaso

> [!question]- ¿Por qué React se considera una librería y no un framework?
> Porque solo resuelve el rendering de la interfaz. Rutas, estado global y comunicación con el servidor quedan a elección del proyecto, que combina React con otras herramientas.

> [!question]- ¿Qué gana React al comparar Virtual DOMs en vez de redibujar todo?
> Toca el DOM real solo donde hubo cambios. Así evita recalcular el layout y repintar partes que no cambiaron, que es la operación más cara del navegador.

> [!question]- ¿Qué es JSX y qué pasa con él antes de llegar al navegador?
> Es una sintaxis que mezcla marcado con expresiones de JavaScript. El navegador no la entiende: una herramienta de compilación la traduce a llamadas a `createElement`.
