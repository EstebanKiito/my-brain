---
ramo: "Tecnologías y Aplicaciones Web"
tema: "JavaScript como lenguaje"
tags:
  - web
  - javascript
  - tipos
  - origen/complemento
prerrequisitos:
  - "[[02 - Variables, scope y hoisting]]"
---

# Tipos de datos en JavaScript

JavaScript tiene **tipado dinámico**: el tipo de una variable se determina en tiempo de ejecución, a partir del valor asignado, y puede cambiar al reasignarla. No hace falta declarar tipos, pero sí conviene conocerlos, porque las conversiones automáticas y la diferencia entre valores y referencias explican la mayoría de los errores del lenguaje.

```javascript
let variable = 10;      console.log(typeof variable); // 'number'
variable = 'Hello';     console.log(typeof variable); // 'string'
variable = [1, 2, 3];   console.log(typeof variable); // 'object'
variable = true;        console.log(typeof variable); // 'boolean'
```

## Los siete primitivos

| Tipo | Valores | Ejemplo |
|---|---|---|
| `boolean` | `true`, `false` | `let b = true;` |
| `null` | Ausencia intencional de valor | `let n = null;` |
| `undefined` | Valor aún no asignado | `let u;` |
| `number` | Enteros y decimales (un solo tipo) | `42`, `3.14159` |
| `bigint` | Enteros de precisión arbitraria | `9007199254740992n` |
| `string` | Texto | `'Hola'` |
| `symbol` | Identificador único, distinto de cualquier otro | `Symbol('dog')` |

**Números.** Se pueden escribir en binario (`0b1101`), octal (`0o237`), decimal o hexadecimal (`0x6f`). La división por cero da `Infinity` y las operaciones inválidas dan `NaN` (*not a number*), que curiosamente es de tipo `number` y no es igual ni a sí mismo:

```javascript
console.log(0o237, 0x6f);            // 159 111
console.log(1 / 0 === Infinity);     // true
console.log(Math.sqrt(-1) == NaN);   // false
console.log(isNaN(Math.sqrt(-1)));   // true
console.log(0.1 + 0.2);              // 0.30000000000000004 (punto flotante)
```

**Strings.** Se delimitan con comillas simples, dobles o *backticks*. Solo los backticks permiten **interpolación**:

```javascript
let mensaje = "Este mensaje es para";
mensaje = mensaje + " IIC2513";
console.log(mensaje.length);                    // 28
console.log(`Con interpolación: ${mensaje}`);
```

## Truthy, falsy, null y undefined

En una condición, cualquier valor se interpreta como booleano. Son **falsy** `false`, `0`, `NaN`, `""`, `undefined` y `null`; todo lo demás es **truthy** (incluso `"0"`, `[]` y `{}`).

`undefined` significa "todavía no tiene valor asignado"; `null` significa "ningún valor", puesto a propósito. Ambos son falsy, y `null == undefined` es verdadero pero `null === undefined` es falso: son equivalentes, pero de distinto tipo.

## Objetos y referencias

Todo lo que no es primitivo es un **objeto**: una colección de pares nombre-valor llamados propiedades. Se accede con punto o con corchetes, y se pueden agregar y quitar propiedades en cualquier momento:

```javascript
let persona = { name: 'Alice', age: 23, country: 'Chile' };
console.log(persona.name, persona['country']); // Alice Chile
console.log(persona.estoNoExiste);             // undefined
persona.course = 'IIC2513';
delete persona.country;
console.log(Object.keys(persona));             // [ 'name', 'age', 'course' ]
```

Las variables guardan **referencias** a objetos, no los objetos en sí. Por eso, al comparar dos objetos no se miran sus propiedades, sino si apuntan al mismo lugar en memoria:

```javascript
const p = { x: 3, y: 5 };
const q = { x: 3, y: 5 };
const r = q;                 // copia la referencia
console.log(p === q);        // false: mismo contenido, objetos distintos
console.log(q === r);        // true: el mismo objeto
```

> [!warning] Copiar una variable no copia el objeto
> Tras `const r = q`, modificar `r.x` también cambia `q.x`, porque ambos nombres apuntan al mismo objeto.

## Colecciones y otros objetos

- **Array**: lista ordenada; puede mezclar tipos y tener huecos.
- **Map** (y `WeakMap`): pares llave-valor donde la llave puede ser de cualquier tipo, incluso un objeto.
- **Set** (y `WeakSet`): colección de valores sin duplicados.
- **Date**: un instante en el tiempo (`new Date()`, `getFullYear()`; ojo, `getMonth()` va de 0 a 11).
- **Function**: las funciones también son objetos, aunque `typeof` responde `'function'`.

```javascript
const lenguajesFav = ['JS', 'Python'];
lenguajesFav.push('C');
lenguajesFav[10] = 'PHP';
console.log(lenguajesFav.length);   // 11, con 7 posiciones vacías

const map = new Map([['name', 'SomeName'], ['age', 30]]);
map.set('age', 31);
console.log(map.get('age'), map.has('city')); // 31 false

const set = new Set(['Apple', 'Banana']);
set.add('Banana');                  // no se duplica
console.log(set.size);              // 2
```

## Preguntas de repaso

> [!question]- ¿Por qué `p === q` es falso si ambos objetos tienen las mismas propiedades?
> Porque `===` sobre objetos compara referencias: son dos objetos distintos en memoria, aunque tengan el mismo contenido. Solo es verdadero si ambas variables apuntan al mismo objeto.

> [!question]- ¿Cómo se comprueba si un valor es `NaN`?
> Con `isNaN(x)` o `Number.isNaN(x)`. Comparar con `== NaN` siempre da falso, porque `NaN` no es igual a ningún valor, ni siquiera a sí mismo.

> [!question]- ¿Qué diferencia hay entre `null` y `undefined`?
> `undefined` indica que una variable o propiedad no tiene un valor asignado; `null` es un valor que el programador asigna para decir explícitamente "ninguno". Son equivalentes con `==` pero distintos con `===`.

> [!question]- ¿Cuándo conviene un `Map` en vez de un objeto?
> Cuando las llaves no son strings (por ejemplo, objetos), cuando se agregan y quitan pares constantemente o cuando importa el orden de inserción y el tamaño (`map.size`).
