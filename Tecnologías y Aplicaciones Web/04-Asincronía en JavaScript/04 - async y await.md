---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Asincronía en JavaScript"
tags:
  - web
  - javascript
  - async-await
  - origen/complemento
prerrequisitos:
  - "[[03 - Encadenamiento y errores en promesas]]"
---

# async y await

Las cadenas de promesas son planas, pero siguen siendo una sucesión de callbacks. Introducidos en ES2017, **`async`** y **`await`** son *syntactic sugar* sobre promesas: permiten escribir código asíncrono que **se lee como si fuera síncrono**, de arriba hacia abajo, con variables normales y `try/catch`.

## `async`: funciones que retornan promesas

La palabra `async` antes de una función hace que **siempre retorne una promesa**, sin usar el constructor. No se llama a `resolve` ni a `reject`: lo que la función retorna es el valor de la promesa, y si lanza una excepción, la promesa queda rechazada. Desde afuera se maneja con `then` y `catch`, como cualquier promesa.

```javascript
async function functionQuePromete() {
  return 'Han pasado 84 años';
}
const valor = functionQuePromete();
console.log(valor);    // Promise { 'Han pasado 84 años' }
```

## `await`: esperar el resultado

`await` se antepone a una promesa y **pausa la función** hasta que la promesa se resuelva; entonces entrega su valor. Así JavaScript "espera" el resultado, emulando un comportamiento síncrono:

```javascript
async function functionQuePromete() {
  return 'Han pasado 84 años';
}
async function functionQueEspera() {
  const value = await functionQuePromete();   // functionQuePromete retorna una promesa
  console.log(`Esperaba por ${value}`);
  return 'Ahora yo retorno';
}
functionQueEspera();   // Esperaba por Han pasado 84 años
```

> [!warning] `await` solo vale dentro de una función `async`
> En una función normal, `await` es un error de sintaxis. La única excepción es el nivel superior de un módulo (*top-level await*). Además, la función que usa `await` es `async`, así que también retorna una promesa: la asincronía no desaparece, solo se escribe más cómodo.

> [!tip] Pausar la función no bloquea el programa
> Mientras una función `async` espera en un `await`, el resto del programa sigue corriendo (otros eventos, otros callbacks). Solo esa función queda suspendida hasta que llegue el valor.

## Promesas frente a `await`

![Fetch con promesas frente a async await](adjuntos/Fetch%20con%20promesas%20frente%20a%20async%20await.png)

> [!example]- Transcripción de la imagen
> - **Izquierda, con promesas:** `fetch('coffee.jpg').then(response => response.blob()).then(myBlob => { … })`. Dentro se crea un `img` con `document.createElement('img')`, se le asigna `URL.createObjectURL(myBlob)` y se agrega con `document.body.appendChild(img)`. Termina con `.catch(e => console.log(`Error ${e.message}`))`.
> - **Derecha, con `async`/`await`:** `async function myFetch()` hace `let response = await fetch('coffee.jpg')` y `let myBlob = await response.blob()`, y crea y agrega la imagen igual. Después se llama `myFetch().catch(e => …)`.

Las dos versiones hacen exactamente lo mismo. Con `await`, cada resultado intermedio tiene nombre (`response`, `myBlob`) y queda disponible para todo el resto de la función, sin pasarlo de un `then` al siguiente.

## Manejo de errores

Dentro de una función `async`, una promesa rechazada hace que `await` **lance una excepción**, que se atrapa con un `try/catch` normal:

```javascript
async function cargarUsuarios(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error(`Hubo un error: ${err}`);
  }
}
```

Es la versión con `await` de `fetchData`, la función con `then` y `catch` del ejemplo de `fetch` en [[03 - Encadenamiento y errores en promesas|Encadenamiento y errores en promesas]].

> [!warning] `await` en serie es lento si las tareas son independientes
> `await a(); await b();` espera a que termine `a` antes de empezar `b`. Si no dependen entre sí, conviene lanzarlas juntas: `await Promise.all([a(), b()])`.

## Preguntas de repaso

> [!question]- ¿Qué retorna una función `async` que hace `return 5`?
> Una promesa cumplida con el valor 5. Toda función `async` retorna una promesa, aunque el código retorne un valor normal.

> [!question]- ¿Por qué se dice que `async`/`await` es *syntactic sugar*?
> Porque no agrega capacidades nuevas: todo lo que hace se puede escribir con promesas, `then` y `catch`. Solo cambia la forma de escribirlo, para que se lea como código secuencial.

> [!question]- ¿Cómo se maneja un error de una promesa esperada con `await`?
> Con `try/catch`: si la promesa se rechaza, `await` lanza la excepción en esa línea. También se puede dejar que la promesa de la función `async` se rechace y manejarla afuera con `.catch`.
