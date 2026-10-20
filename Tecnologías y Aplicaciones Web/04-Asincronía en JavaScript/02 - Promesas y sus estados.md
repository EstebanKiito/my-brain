---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Asincronía en JavaScript"
tags:
  - web
  - javascript
  - promesas
  - origen/complemento
prerrequisitos:
  - "[[01 - Código asíncrono y callbacks]]"
---

# Promesas y sus estados

Una **promesa** (*Promise*) es un objeto que representa el **estado intermedio** de una operación cuyo valor se resolverá en el futuro. Es la promesa de un valor: "no puedo retornarte el valor ahora, pero prometo que lo haré en algún momento". Por ejemplo, al esperar el click de un usuario no se sabe cuándo ocurrirá, pero eventualmente se tendrán sus coordenadas. Al leer un archivo, los datos no están todavía, pero llegarán. Las promesas simplifican el trabajo con callbacks, sobre todo cuando están anidados.

## Crear una promesa

El constructor recibe una función con dos callbacks: **`resolve`**, para entregar el resultado exitoso, y **`reject`**, para avisar de un error.

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success'), 1000);
});
promise.then(result => console.log(result));   // 'Success', un segundo después
```

En la práctica pocas veces se crean promesas a mano: casi siempre se **reciben** como resultado de una librería o de funciones como `fetch`.

## Estados

![Promesa recién creada en estado pending](adjuntos/Promesa%20reci%C3%A9n%20creada%20en%20estado%20pending.png)

> [!example]- Transcripción de la imagen
> En la consola del navegador, `new Promise(() => {});` devuelve `Promise { <state>: "pending" }`: una promesa que nunca llama a `resolve` ni a `reject` se queda pendiente.

![Estados de una promesa y sus métodos](adjuntos/Estados%20de%20una%20promesa%20y%20sus%20m%C3%A9todos.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, los tres estados: **Pending** (estado inicial, aún no ocurre nada), **Resolved** (la promesa retornó un valor sin errores) y **Rejected** (la promesa no se pudo completar).
> - A la derecha, un diagrama: "A Promise is made" → Pending, que se bifurca en Resolve (sigue `.then` → `.then`) y Reject (sigue `.catch`). Ambas ramas terminan en `.finally`.

| Estado | Significado | Qué se ejecuta |
|---|---|---|
| **pending** | La operación aún no termina | Nada todavía |
| **fulfilled** (*resolved*) | Terminó con un valor | Los `.then` |
| **rejected** | Falló | El `.catch` |

Una promesa que dejó de estar pendiente está **settled** (resuelta o rechazada), y ese estado ya no cambia.

## Obtener el valor prometido

Una función que retorna una promesa no entrega el valor, sino la promesa:

```javascript
function miFuncionAsincrona() {
  return new Promise((resolve, reject) => {
    resolve('Prometí este valor');
  });
}
console.log(miFuncionAsincrona());              // Promise { 'Prometí este valor' }
miFuncionAsincrona().then(valorPrometido => {
  console.log(valorPrometido);                  // 'Prometí este valor'
});
```

El valor se obtiene con **`then`**, que recibe como callback la función que se ejecutará cuando la promesa se cumpla.

## `then`, `catch` y `finally`

Un ejemplo completo con las tres ramas:

```javascript
const momsPromise = new Promise(function (resolve, reject) {
  const momsSavings = 1000000;
  const priceOfPhone = 800000;
  if (momsSavings > priceOfPhone) {
    resolve({ brand: 'iphone', model: '14' });
  } else {
    reject('We dont have enough savings. Let us save some more money.');
  }
});
momsPromise
  .then(value => console.log('Hurray I got this phone as a gift', JSON.stringify(value)))
  .catch(reason => console.log("Mom couldn't buy me the phone because", reason))
  .finally(() => console.log('Irrespective of whether my mom can buy me a phone or not, I still love her'));
```

- `then` se ejecuta si la promesa se **cumple** y recibe el valor.
- `catch` se ejecuta si la promesa se **rechaza** y recibe el motivo.
- `finally` se ejecuta **siempre**, se cumpla o se rechace; sirve para tareas de cierre, como ocultar un indicador de carga.

> [!tip] Una promesa es un valor futuro con dos salidas
> El código que la crea decide la salida (`resolve` o `reject`). El código que la usa reacciona a ella (`then` o `catch`), sin anidar callbacks.

> [!warning] El valor no "sale" de la promesa
> `const v = miFuncionAsincrona()` guarda una promesa, no el string. El valor solo está disponible dentro del `then`, o con `await`.

## Preguntas de repaso

> [!question]- ¿Qué imprime `console.log(miFuncionAsincrona())` y por qué?
> Imprime un objeto `Promise`, no el valor. La función retorna la promesa de inmediato; el valor solo se obtiene registrando un callback con `then` (o esperándolo con `await`).

> [!question]- ¿Puede una promesa pasar de rejected a fulfilled?
> No. Una vez que una promesa queda settled (cumplida o rechazada), su estado es definitivo. Lo que sí puede pasar es que un `catch` retorne un valor y genere una **nueva** promesa cumplida.

> [!question]- ¿Para qué sirve `finally` si ya existen `then` y `catch`?
> Para ejecutar código que debe correr en ambos casos, como liberar un recurso u ocultar un spinner, sin duplicarlo en el `then` y en el `catch`.
