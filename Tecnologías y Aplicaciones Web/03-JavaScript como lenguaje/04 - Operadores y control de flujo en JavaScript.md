---
ramo: "Tecnologías y Aplicaciones Web"
tema: "JavaScript como lenguaje"
tags:
  - web
  - javascript
  - origen/complemento
prerrequisitos:
  - "[[03 - Tipos de datos en JavaScript]]"
---

# Operadores y control de flujo en JavaScript

La sintaxis de control de JavaScript viene de C: `if`, `for`, `while` y `switch` funcionan casi igual. Lo distinto está en los operadores: dos tipos de igualdad, y `||`, `&&` y `??`, que no devuelven booleanos sino **uno de sus operandos**. Ese detalle es la base de muchos patrones idiomáticos, como los valores de respaldo.

## Comparaciones: `===` frente a `==`

| Expresión | Resultado |
|---|---|
| `x === y` | `true` si son **iguales**: mismo tipo y mismo valor (`1 !== true`) |
| `x !== y` | Negación de lo anterior |
| `x == y` | `true` si son **similares**: valores equivalentes tras convertir tipos (`1 == true`) |
| `x != y` | Negación de lo anterior |

> [!tip] Usar siempre `===`
> `==` convierte tipos antes de comparar y produce resultados difíciles de predecir (`"" == 0` es verdadero). Con `===` lo que se compara es exactamente lo que se ve.

## Operadores lógicos y de respaldo

| Expresión | Devuelve |
|---|---|
| `x && y` | Si `x` es falsy, `x`; si no, `y` |
| `x \|\| y` | Si `x` es truthy, `x`; si no, `y` |
| `!x` | `false` si `x` es truthy; si no, `true` |
| `x ?? y` | Si `x` es `null` o `undefined`, `y`; si no, `x` |
| `c ? a : b` | Operador ternario: un `if/else` en una línea |
| `+x`, `-x` | Conversión a número |

```javascript
const podriaSerNumero = '42';
console.log(typeof +podriaSerNumero);   // 'number'

const cantidad = 0;
console.log(cantidad || 10);  // 10: 0 es falsy, se usa el respaldo
console.log(cantidad ?? 10);  // 0: 0 no es nulo, se conserva
```

> [!warning] `||` frente a `??`
> `||` reemplaza **cualquier** valor falsy, incluidos `0` y `""`, que muchas veces son valores válidos. `??` solo reemplaza `null` y `undefined`. Para valores por defecto, `??` es casi siempre lo correcto.

## Bloques y condicionales

Las llaves delimitan los bloques; la indentación no tiene significado (a diferencia de Python). Si el bloque tiene una sola línea se pueden omitir, pero conviene mantenerlas por legibilidad.

```javascript
let variable = 8;
const constante = 1;
if (variable > 5 && constante === 1) {
  variable = variable / 2;          // ambas se cumplen (AND)
} else if (variable < 5 || constante === 1) {
  variable -= 2;                    // alguna se cumple (OR)
} else {
  variable = 0;
}
if (!(variable > 5)) {              // NOT: la condición siempre va entre paréntesis
  variable = -1;
}
console.log(variable);              // -1
```

## Ciclos

- `for (inicio; condición; paso)`: usar `let` en el inicio hace que la variable solo exista dentro del ciclo.
- `while (condición)`: revisa la condición **al comenzar** cada vuelta.
- `do { … } while (condición)`: la revisa **al terminar**, así que el cuerpo se ejecuta al menos una vez.
- `break` termina el ciclo; `continue` salta a la siguiente vuelta.

```javascript
let suma = 0;
for (const element of [1, 2, 3]) {        // for...of: recorre los VALORES de un iterable
  suma += element;
}
const objeto = { a: 1, b: 2, c: 3 };
for (const propiedad in objeto) {         // for...in: recorre las LLAVES de un objeto
  suma += objeto[propiedad];
}
console.log(suma);                        // 12
```

## `switch`

Evalúa una expresión, la compara con cada `case` y ejecuta **desde el que coincide hacia abajo**, hasta encontrar un `break`:

```javascript
const grade = 'B+';
switch (grade) {
  case 'A':
  case 'B+':
    console.log('Muy bien!');           // 'A' y 'B+' comparten esta rama
    break;
  case 'B':
  case 'C':
    console.log('Bien');
    break;
  default:
    console.log('¿Me repites la nota?');
}
```

> [!warning] El `break` olvidado
> Sin `break`, la ejecución "cae" al siguiente `case` y ejecuta también su código. A veces se usa a propósito (agrupar casos), pero casi siempre es un error.

## Preguntas de repaso

> [!question]- ¿Qué imprime `console.log(0 || 'respaldo')` y qué imprime `console.log(0 ?? 'respaldo')`?
> El primero imprime `'respaldo'`, porque `0` es falsy y `||` lo reemplaza. El segundo imprime `0`, porque `??` solo reemplaza `null` y `undefined`.

> [!question]- ¿Cuál es la diferencia entre `for...of` y `for...in`?
> `for...of` recorre los valores de un iterable (arreglos, strings, Maps). `for...in` recorre los nombres de las propiedades de un objeto. Usar `for...in` sobre un arreglo entrega los índices como strings, no los elementos.

> [!question]- ¿Cuándo se ejecuta al menos una vez el cuerpo de un ciclo aunque la condición sea falsa?
> En un `do...while`, porque la condición se evalúa al final de cada vuelta y no al principio.
