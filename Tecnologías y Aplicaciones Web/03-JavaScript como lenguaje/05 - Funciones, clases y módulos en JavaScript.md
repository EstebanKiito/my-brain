---
ramo: "Tecnologías y Aplicaciones Web"
tema: "JavaScript como lenguaje"
tags:
  - web
  - javascript
  - funciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Variables, scope y hoisting]]"
  - "[[04 - Operadores y control de flujo en JavaScript]]"
---

# Funciones, clases y módulos en JavaScript

En JavaScript las funciones son **valores**: se guardan en variables, se pasan como argumento y se retornan. Todo el JavaScript asíncrono (callbacks, promesas, eventos) depende de eso. Hay cuatro tipos de función (regulares, generadoras, asíncronas y generadoras asíncronas). Esta nota cubre las regulares, que se ejecutan completas al invocarlas y pueden retornar cualquier cosa, además de clases y módulos.

## Tres formas de definir una función

**Declaración.** Se comporta como en otros lenguajes: variables locales, acceso a variables externas, valores por defecto y retorno. Gracias al hoisting se puede llamar **antes** de definirla, por lo que suele usarse en el scope global.

```javascript
console.log(factorial(5));            // 120: funciona por hoisting
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
console.log(typeof factorial);        // 'function'
```

**Expresión.** La función es un valor asignado a una variable. Se crea cuando la ejecución llega a esa línea (no hay hoisting). Sirve para limitar dónde está disponible y mantener limpio el scope global.

```javascript
const multiply = function (x, y) {
  return x * y;
};
```

**Función flecha** (*arrow function*). Es anónima, tiene una sintaxis corta y **no tiene `this` propio**: usa el del contexto donde se escribió. Por eso es ideal para callbacks y funciones anidadas.

```javascript
const materials = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium'];
console.log(materials.map(material => material.length)); // [ 8, 6, 7, 9 ]
const sumar = (x, y) => x + y;   // con una sola expresión, el return es implícito
```

> [!tip] Cuál usar
> Declaración para funciones con nombre de uso general; expresión para funciones que solo deben existir en un ámbito; flecha para callbacks y funciones anónimas cortas.

## Parámetros por defecto

Una función siempre pudo recibir más o menos argumentos de los declarados (accesibles con `arguments`). Antes de ES6, los valores por defecto se simulaban con `||`. Ahora se declaran directamente, incluso desestructurando un objeto de opciones:

```javascript
function showMessage(from, text = '<vacio>') {
  console.log(`${from}: ${text}`);
}
showMessage('Antonio', '¡Hola!');  // Antonio: ¡Hola!
showMessage('Antonio');            // Antonio: <vacio>

function selectEnt({ start = 0, end = -1, step = 1 } = {}) {
  return [start, end, step];
}
console.log(selectEnt({ end: 5 })); // [ 0, 5, 1 ]
```

## Clases

ES6 incorporó la sintaxis `class`, con constructor, métodos, métodos estáticos y herencia con `extends` y `super`. Por debajo siguen funcionando los prototipos de JavaScript; la clase es una sintaxis más cómoda para lo mismo.

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  area() { return this.width * this.height; }
  static describe() { return 'A Rectangle'; }
}
class Square extends Rectangle {
  constructor(size) { super(size, size); }
  static describe() { return 'A Square'; }
}
console.log(new Square(15).area(), Square.describe()); // 225 'A Square'
```

## Utilidades modernas de arreglos

`Array.from` convierte algo iterable o parecido a una lista (por ejemplo, el resultado de una búsqueda en el DOM) en un arreglo, y opcionalmente lo transforma. `Array.of` arma un arreglo con sus argumentos.

```javascript
console.log(Array.from('foo'));                 // [ 'f', 'o', 'o' ]
console.log(Array.from([1, 2, 3], x => x + x)); // [ 2, 4, 6 ]
console.log(Array.of('foo', 2, 'bar', true));   // [ 'foo', 2, 'bar', true ]
```

## Módulos

Un archivo puede **exportar** funciones, objetos o valores, y otro los **importa**. Así cada archivo tiene su propio scope y no contamina el global.

```javascript
// lib.js
export const sqrt = Math.sqrt;
export function square(x) { return x * x; }
export function diag(x, y) { return sqrt(square(x) + square(y)); }

// main.js
import { square, diag } from './lib.js';
console.log(square(11), diag(3, 4)); // 121 5
// o bien: import * as lib from './lib.js'; lib.square(11);
```

> [!warning] Los módulos resolvieron el problema de las globales
> Antes de los módulos, cada `<script>` compartía el mismo scope global y dos librerías podían pisarse las variables. Con `import` y `export`, cada archivo declara explícitamente qué expone y qué usa.

## Preguntas de repaso

> [!question]- ¿Por qué una función declarada se puede llamar antes de su definición y una expresión no?
> Porque el hoisting registra completa la declaración de una función (nombre y cuerpo). Una expresión es una asignación a una variable, y la asignación solo ocurre cuando la ejecución llega a esa línea.

> [!question]- ¿Qué tiene de especial `this` en una función flecha?
> Que no tiene uno propio: toma el `this` del contexto donde fue escrita. Por eso dentro de un callback mantiene el `this` del método que lo contiene, en vez de perderlo.

> [!question]- ¿Qué problema de los scripts en el navegador resuelven los módulos?
> El de las variables globales compartidas: sin módulos, todos los scripts escriben en el mismo scope global y pueden pisarse. Con módulos, cada archivo tiene su scope y solo comparte lo que exporta.
