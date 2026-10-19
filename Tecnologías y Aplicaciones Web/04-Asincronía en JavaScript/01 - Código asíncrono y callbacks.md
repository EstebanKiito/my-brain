---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Asincronía en JavaScript"
tags:
  - web
  - javascript
  - asincronia
  - callbacks
  - origen/complemento
prerrequisitos:
  - "[[05 - Funciones, clases y módulos en JavaScript]]"
---

# Código asíncrono y callbacks

En la web casi todo implica **esperar**: que el servidor responda una request, que el usuario presione una tecla o haga click. Si el programa se detuviera en cada espera, la página quedaría congelada. JavaScript evita eso con código **asíncrono**, y la forma más simple de expresarlo es el **callback**: una función que se entrega ahora para que se ejecute después.

## Síncrono frente a asíncrono

- **Síncrono**: cada instrucción espera a que termine la anterior; se ejecuta línea por línea, en el orden escrito.
- **Asíncrono**: las operaciones diferidas no detienen la ejecución; el programa sigue y la operación se completa más tarde.

```javascript
console.log('Inicio');
setTimeout(() => {
  console.log('Procesamiento...');
}, 2000);
console.log('Final');
// Inicio
// Final
// (2 segundos después) Procesamiento...
```

`setTimeout` no bloquea: agenda la función para dentro de 2 segundos y la ejecución continúa de inmediato con `'Final'`.

> [!warning] Asíncrono no es paralelo
> El código de JavaScript corre en un solo hilo: no se ejecutan dos funciones a la vez. Lo que ocurre "en paralelo" es la espera (el temporizador, la red, el disco), que la gestiona el entorno. Cuando la espera termina, el callback se ejecuta en ese mismo hilo, en cuanto queda libre.

## Callbacks

Un **callback** es una función que se pasa como argumento a otra, para que esta la invoque cuando corresponda. Así se encapsula el comportamiento y se ejecuta en el momento oportuno:

```javascript
function primeraFuncion() {
  console.log('hago algo');
}
function otraFuncion(callback) {
  callback();                 // llamada al callback
}
otraFuncion(primeraFuncion);
```

El ejemplo clásico es leer un archivo en Node.js:

```javascript
const { readFile } = require('fs');
readFile(__filename, 'utf8', function (err, contents) {
  if (err) throw err;
  console.log(contents.length > 0);    // se imprime al final
});
console.log('Hi!');                    // se imprime primero
```

1. `readFile` empieza la lectura y retorna de inmediato.
2. `"Hi!"` aparece al tiro.
3. Cuando la lectura termina, se ejecuta el callback.
4. Recién ahí se usa el contenido.

Los callbacks pueden ser de dos tipos:

- **Síncronos**: se ejecutan de inmediato, dentro de la llamada. Por ejemplo, `array.map(elem => console.log(elem))`.
- **Asíncronos**: su ejecución se pospone. Por ejemplo, la función entregada a `setTimeout(..., 3000)`.

![Estructura general de un callback](adjuntos/Estructura%20general%20de%20un%20callback.png)

> [!example]- Transcripción de la imagen
> - `funcionAsincrona(unCallback)` hace una operación de duración desconocida (leer un archivo) que no debe detener la ejecución; obtiene `data` y llama a `unCallback(data)`. La flecha señala esa línea: "Aquí se usa el callback".
> - Tres formas de entregar el callback, cada una marcada con una flecha ("Esta función es un callback", "Esta también", "Y esta"):
>   - una función ya definida, `funcionAsincrona(esteEsUnCallback)`;
>   - una expresión de función, `funcionAsincrona(function (param) { console.log(param); })`;
>   - una función flecha, `funcionAsincrona(param => console.log(param))`.

## Callback hell

Un callback puede a su vez llamar a otra función asíncrona con su propio callback. Si cada paso depende del anterior, el código se anida cada vez más:

```javascript
const cocinar = function () {
  setTimeout(function () {
    console.log('Empiezo a cocinar');
    setTimeout(function () {
      console.log('Seleccionar ingredientes');
      setTimeout(function () {
        console.log('Paso 1...');
        setTimeout(function () {
          console.log('Paso 2...');
          setTimeout(function () {
            console.log('Paso 3...');
          }, 1000);
        }, 1000);
      }, 3000);
    }, 2000);
  }, 1000);
};
cocinar();
```

Este problema se conoce como **callback hell** (o "pirámide de la perdición"). En código real se suma el manejo de errores en cada nivel (`if (err) … else …`), y seguir el flujo se vuelve muy difícil. Las **promesas** se introdujeron justamente para resolverlo.

> [!tip] Idea central
> Un callback invierte el control: en vez de esperar el resultado, se le dice a la operación "cuando termines, llama a esta función". Funciona bien con un nivel; con muchos niveles anidados aparece el callback hell.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejemplo de `setTimeout` se imprime `'Final'` antes que `'Procesamiento...'`?
> Porque `setTimeout` no detiene la ejecución: solo agenda el callback. El programa sigue con la línea siguiente y el callback se ejecuta cuando vence el plazo.

> [!question]- ¿En qué se diferencia el callback de `map` del de `setTimeout`?
> El de `map` es síncrono: se ejecuta para cada elemento antes de que `map` retorne. El de `setTimeout` es asíncrono: se ejecuta después, cuando el temporizador vence y el hilo está libre.

> [!question]- ¿Qué hace difícil de mantener el callback hell?
> Cada paso queda anidado dentro del anterior, así que el flujo se lee en diagonal. Además, el manejo de errores se repite en cada nivel, y reordenar o agregar un paso obliga a reestructurar toda la pirámide.
