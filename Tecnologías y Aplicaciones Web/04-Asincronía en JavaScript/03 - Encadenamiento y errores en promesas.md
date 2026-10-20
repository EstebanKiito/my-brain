---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Asincronía en JavaScript"
tags:
  - web
  - javascript
  - promesas
  - origen/complemento
prerrequisitos:
  - "[[02 - Promesas y sus estados]]"
---

# Encadenamiento y errores en promesas

Lo que hace que las promesas resuelvan el callback hell es un detalle: **`then` y `catch` también retornan una promesa**. Por eso los pasos se escriben uno tras otro en una cadena plana, en vez de anidarse, y un solo `catch` puede atrapar el error de cualquier paso anterior.

## Encadenar `then`

![Obtener el valor prometido con then](adjuntos/Obtener%20el%20valor%20prometido%20con%20then.png)

> [!example]- Transcripción de la imagen
> - "Una promesa admite un método `then` que como parámetro recibe la función a llamar cuando la promesa se hace efectiva (un callback)": `miFuncionAsincrona().then(function (valorPrometido) { console.log(valorPrometido); });`.
> - "El método `then` devuelve una promesa, lo que hace posible encadenar una promesa tras otra": un primer `then` retorna `` `'${valorPrometido}' es el valor prometido` `` y un segundo `then` lo imprime.

Lo que retorna el callback de un `then` se convierte en el valor de la promesa siguiente. Si retorna otra promesa, la cadena espera a que esa se resuelva:

```javascript
const cleanRoom = () => Promise.resolve('cleaned the room');
const removeGarbage = message => Promise.resolve(message + ' remove garbage');
const winIcecream = message => Promise.resolve(message + ' won icecream');

cleanRoom()
  .then(result => removeGarbage(result))
  .then(result => winIcecream(result))
  .then(result => console.log('finished ' + result));
// finished cleaned the room remove garbage won icecream
```

## Promesas rechazadas y `catch`

Una promesa se **rechaza** si se llama a `reject` o si ocurre una excepción dentro de ella (o dentro de un `then`). Desde ahí, la cadena salta todos los `then` hasta el primer `catch`. Y como `catch` también retorna una promesa, lo que venga después se ejecuta igual:

```javascript
new Promise((resolve, reject) => {
  resolve('Valor resuelto');
})
  .then(valor => {
    throw new Error(`No me gusta este valor: ${valor}`);
  })
  .catch(msg => {
    console.log(`Se rechazó con: ${msg}`);
    // Se rechazó con: Error: No me gusta este valor: Valor resuelto
    return 'Estamos en una promesa, hay que resolver';
  })
  .then(otroValor => {
    console.log(`Lo que viene de la promesa previa: ${otroValor}`);
    // Lo que viene de la promesa previa: Estamos en una promesa, hay que resolver
  });
```

Variantes del mismo código:

- **Sin el `throw`**: el primer `then` retorna `'Solo pasa si no hay error'`, el `catch` se salta y el último `then` imprime ese texto.
- **Con `reject('Valor rechazado')`** en vez de `resolve`: el primer `then` se salta, el `catch` imprime `Se rechazó con: Valor rechazado` y el último `then` imprime su texto de siempre.

> [!warning] El último `then` se ejecuta igual
> Después de un `catch`, la cadena vuelve al camino feliz, porque `catch` atrapa el error y retorna una promesa cumplida. Si el resto de la cadena no debe ejecutarse, el `catch` tiene que ir al final o volver a lanzar el error (`throw`).

![Resumen de estados y métodos de promesas](adjuntos/Resumen%20de%20estados%20y%20m%C3%A9todos%20de%20promesas.png)

> [!example]- Transcripción de la imagen
> Una `Promise` *pending* se cumple (*fulfill*) o se rechaza (*reject*) y queda *settled*. Al cumplirse ejecuta `.then(onFulfillment)`, que realiza acciones asíncronas. Al rechazarse ejecuta `.then(…, onRejection)` o `.catch(onRejection)`, que manejan el error. En ambos casos se retorna (*return*) una nueva `Promise` *pending*, sobre la que se pueden encadenar más `.then()` y `.catch()`.

## Del callback hell a la cadena de promesas

La misma receta, con callbacks anidados y con promesas:

![Receta como cadena de callbacks](adjuntos/Receta%20como%20cadena%20de%20callbacks.png)

> [!example]- Transcripción de la imagen
> "Cadena de callbacks": `seleccionarReceta` recibe un callback con los ingredientes. Dentro, `seleccionarIngredientes` recibe otro; dentro, un `forEach` llama a `cortarIngrediente` con un tercer callback que cuenta cuántos faltan y avisa al llegar a 0. Luego `recetaPaso1`, `recetaPaso2` y `recetaPaso3` se anidan uno dentro de otro hasta imprimir `'Receta completada'`. El código cierra con seis niveles de `});`.

![Receta como cadena de promesas](adjuntos/Receta%20como%20cadena%20de%20promesas.png)

> [!example]- Transcripción de la imagen
> "Cadena de promesas": `seleccionarReceta().then(seleccionarIngredientes).then(ingredientes => Promise.all(ingredientes.map(cortarIngrediente))).then(ingredientesCortados => recetaPaso1(…).then(() => recetaPaso2(…)).then(() => recetaPaso3(…))).then(() => console.log('Receta completada'))`.

Dos cosas cambian. El flujo se lee de arriba hacia abajo. Y el contador manual de ingredientes desaparece: **`Promise.all`** recibe un arreglo de promesas y se cumple cuando **todas** se cumplen (o se rechaza con el primer error).

## Un ejemplo web: `fetch`

`fetch` hace una request HTTP y retorna una promesa con la respuesta. Leer el cuerpo como JSON (`response.json()`) es otra operación asíncrona, así que se encadena:

```javascript
function fetchData(url) {
  return fetch(url)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(`Hubo un error: ${err}`));
}
fetchData('https://jsonplaceholder.typicode.com/users');
```

> [!tip] Un solo `catch` para toda la cadena
> Si falla la red, la conversión a JSON o cualquier paso intermedio, el error baja por la cadena hasta el único `catch`. Con callbacks habría que revisar `err` en cada nivel.

## Preguntas de repaso

> [!question]- ¿Por qué `then` retorne una promesa elimina la anidación?
> Porque el siguiente paso se encadena sobre esa nueva promesa (`.then(...).then(...)`) en vez de escribirse dentro del callback anterior. El resultado es una secuencia plana.

> [!question]- Si un `then` lanza un error, ¿qué pasa con los `then` siguientes antes del `catch`?
> Se saltan: la promesa queda rechazada y la cadena avanza directo al primer `catch` (o al segundo argumento de un `then`).

> [!question]- ¿Qué hace `Promise.all` y cuándo conviene?
> Recibe un arreglo de promesas y retorna una que se cumple con el arreglo de todos los resultados cuando todas terminan, o se rechaza con el primer error. Conviene para lanzar operaciones independientes en paralelo y continuar cuando todas estén listas.
