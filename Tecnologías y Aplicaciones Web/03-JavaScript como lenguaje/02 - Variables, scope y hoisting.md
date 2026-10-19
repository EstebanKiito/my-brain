---
ramo: "Tecnologías y Aplicaciones Web"
tema: "JavaScript como lenguaje"
tags:
  - web
  - javascript
  - scope
  - origen/complemento
prerrequisitos:
  - "[[01 - Origen de JavaScript, ECMAScript y TypeScript]]"
---

# Variables, scope y hoisting

En JavaScript hay tres formas de declarar una variable (`var`, `let` y `const`), y se comportan distinto en dos aspectos: **dónde** es visible la variable (*scope*) y **desde cuándo** existe (*hoisting*). La regla práctica es corta, `const` por defecto, `let` si cambia y nunca `var`, pero entender por qué evita muchos errores.

## Declaración frente a inicialización

JavaScript distingue dos pasos:

- **Declarar** hace que la variable exista: se puede usar sin lanzar un `ReferenceError`.
- **Inicializar** le asigna un valor.

```javascript
let variable;      // declaración: vale undefined
variable = 17;     // inicialización
let otra = 17;     // ambas juntas: equivalente
```

Una variable declarada pero no inicializada vale `undefined`.

## `let`, `const` y `var`

| | Scope | ¿Se puede reasignar? | ¿Exige inicializar al declarar? |
|---|---|---|---|
| `const` | Bloque | No | Sí |
| `let` | Bloque | Sí | No |
| `var` | Función (ignora los bloques) | Sí | No |

```javascript
let valorQueCambia = 1;
valorQueCambia = 4;      // bien

const valorFijo = 1;
// valorFijo = 4;        // TypeError: Assignment to constant variable.
```

> [!tip] Regla práctica
> `const` para valores que no se van a reasignar, `let` para los que sí y que solo deben existir en el bloque actual, y **nunca `var`**. `let` y `const` son menos flexibles y, justamente por eso, se comportan de forma menos inesperada.

> [!warning] `const` no congela el objeto
> `const` impide **reasignar** el nombre, no modificar el valor. Con `const persona = {}` igual se puede hacer `persona.edad = 20`; lo que falla es `persona = otroObjeto`.

## Scope

Una variable declarada fuera de toda función es **global**: está disponible en todo el documento. Una declarada dentro de una función es **local** a ella. Además, cada par de llaves crea un **bloque** (funciones, `if`, `else`, `for`, `while`), y `let` y `const` quedan limitados a él:

```javascript
if (true) {
  let unValor = 42;
  var otroValor = 17;
}
console.log(typeof unValor); // "undefined": unValor no existe fuera del bloque
console.log(otroValor);      // 17: var no respeta el bloque
```

Lo que sí sale del bloque es la **asignación** a una variable externa:

```javascript
let variable = 1;
if (true) {
  variable = 2;          // no declara: modifica la de afuera
}
console.log(variable);   // 2
```

¿Por qué importa tanto? Los scopes explícitos llegaron recién con ES6. Antes, todo `var` declarado fuera de una función era global, y en el navegador distintos scripts chocaban al declarar las mismas variables globales.

## Hoisting

El **hoisting** es el proceso por el cual las **declaraciones** de variables y funciones se registran en memoria antes de ejecutar el código, como si el intérprete las "subiera" al comienzo de su scope. Lo que se mueve es la declaración, **no la inicialización**:

```javascript
function demo() {
  console.log(value); // undefined: la declaración de var subió, el valor no
  var value = 5;
}
demo();

console.log(f());     // "Hola IIC2513": las funciones declaradas suben completas
function f() {
  return 'Hola IIC2513';
}
```

Con `let` y `const` la declaración también se registra, pero la variable no se puede usar hasta la línea donde se declara (la llamada *temporal dead zone*):

```javascript
const x = 1;
{
  try {
    console.log(x);   // ReferenceError: la x interna ya existe, pero aún no se inicializa
  } catch (e) { console.log(e.name); }
  const x = 2;
}
```

> [!warning] Por qué confunde el hoisting
> En el último ejemplo podría esperarse que se imprima el `x = 1` de afuera. Pero la `x` del bloque ya "existe" desde el inicio del bloque y tapa a la externa, así que el acceso falla. Por eso las guías de estilo recomiendan declarar todo antes de usarlo.

## Preguntas de repaso

> [!question]- ¿Por qué se desaconseja `var`?
> Porque no respeta los bloques (una variable declarada en un `if` sigue existiendo afuera) y porque su hoisting la deja con `undefined` antes de su declaración. Eso esconde errores que con `let` o `const` serían un `ReferenceError` inmediato.

> [!question]- Si `const lista = [1, 2]`, ¿se puede hacer `lista.push(3)`?
> Sí. `const` impide reasignar el nombre `lista` a otro valor, pero el arreglo al que apunta se puede modificar.

> [!question]- ¿Qué se mueve en el hoisting: la declaración o la inicialización?
> Solo la declaración. Por eso un `var` usado antes de su línea vale `undefined`, mientras que una función declarada con `function` se puede llamar antes, porque su declaración incluye el cuerpo completo.
