---
ramo: "Tecnologías y Aplicaciones Web"
tema: "JavaScript como lenguaje"
tags:
  - web
  - javascript
  - typescript
  - origen/complemento
prerrequisitos:
  - "[[05 - DOM, CSSOM y critical rendering path]]"
---

# Origen de JavaScript, ECMAScript y TypeScript

HTML estructura y CSS presenta, pero ninguno de los dos puede **reaccionar**: validar un formulario, cargar datos sin recargar la página o cambiar el contenido cuando el usuario hace click. Para eso los navegadores ejecutan un lenguaje de programación, **JavaScript** (JS). Conocer su historia explica varias de sus rarezas y por qué el estándar se llama ECMAScript.

## Historia temprana

- En **1995**, Brendan Eich escribe en Netscape la primera versión, llamada *Mocha*.
- Se renombra *LiveScript* y aparece en las betas de Netscape 2 (septiembre de 1995).
- Pasa a llamarse **JavaScript** cuando Netscape se alía con Sun (hoy Oracle, dueña de la marca Java), con la idea de que fuera un complemento ligero de Java en el navegador.
- Como "JavaScript" es una marca registrada de Oracle, el estándar se publicó en ECMA con el nombre **ECMAScript**.

> [!warning] JavaScript no es Java
> Solo comparten el nombre por una decisión de marketing. Se parecen tanto como "casilla" a "silla".

## La evolución del estándar

| Versión | Qué trajo |
|---|---|
| ES1 (1997), ES2 (1998), ES3 (1999) | Las primeras ediciones del estándar |
| ES4 (2003-2008) | Abandonada: el comité se dividió entre un cambio incremental (Microsoft, Yahoo) y una gran actualización (Adobe, Mozilla, Opera, Google) |
| ES5 (2009) | El cambio incremental sobre ES3; las ideas de ES4 se dejaron para después |
| **ES6 = ES2015** | La gran actualización ("Harmony"): clases, módulos, iteradores, generadores, funciones flecha, `let`, `const` y promesas |
| ES2017 | `async` y `await` |
| ES2020 | `BigInt` y el operador `??` |
| Desde entonces | Una versión por año, publicada en junio; **ES.Next** es siempre la siguiente |

Los cambios los decide el **TC39**, un comité de desarrolladores, implementadores y académicos. Las propuestas avanzan por etapas (*stages*) en un proceso abierto y público. Un ejemplo es *Temporal*, la nueva API de fechas y horas.

## Cómo es JavaScript como lenguaje

- Es un lenguaje de **scripting interpretado**, como Python: se escribe y se ejecuta, sin un paso de compilación explícito.
- Su sintaxis se parece más a la de C que a la de cualquier otro lenguaje (llaves, punto y coma, `for (;;)`).
- Tiene **tipado dinámico**: una variable tiene el tipo del último valor que se le asignó.
- Está en extensión constante. Como todo lenguaje, tiene partes buenas y otras con "mañas".

La maña más conocida es la **conversión implícita de tipos**. Para no lanzar errores, JavaScript intenta convertir los valores hasta llegar a un resultado:

```javascript
console.log("a" + 10);       // "a10"
console.log("1" + 10);       // "110"
console.log([] + 10);        // "10"
console.log([2, 2, 7] + 10); // "2,2,710"
console.log(+"2" + 10);      // 12
console.log(-"1" + 10);      // 9
console.log(-"a" + 10);      // NaN
```

Con `+`, si alguno de los operandos es string (o se convierte en uno, como un arreglo), se concatena. Los operadores unarios `+` y `-` fuerzan una conversión a número. Que no haya error no significa que el resultado tenga sentido.

## TypeScript

**TypeScript** (TS) es un **superconjunto** de JavaScript, desarrollado y mantenido por Microsoft, que agrega **tipos estáticos** y objetos basados en clases. Formaliza los tipos que JavaScript ya maneja implícitamente y permite declarar variables y funciones tipadas. Todo programa JS válido es TS válido, y el compilador de TS genera JavaScript.

```typescript
const user = { firstName: 'Antonio', lastName: 'Ossa', role: 'Teacher' };
console.log(user.name);
// Error: Property 'name' does not exist on type
// '{ firstName: string; lastName: string; role: string; }'
```

En JavaScript esa línea imprimiría `undefined` sin avisar. TypeScript detecta el error **antes de ejecutar**.

> [!tip] Lo que gana TypeScript
> Mueve errores desde el momento de ejecución (cuando le ocurren al usuario) al momento de escribir el código (cuando le ocurren al desarrollador), y permite que el editor autocomplete con información de tipos.

## Preguntas de repaso

> [!question]- ¿Por qué el estándar se llama ECMAScript y no JavaScript?
> Porque "JavaScript" es una marca registrada, hoy de Oracle. Al estandarizar el lenguaje en ECMA se usó otro nombre para no depender de esa marca.

> [!question]- ¿Por qué `"1" + 10` da `"110"` pero `-"1" + 10` da `9`?
> Con `+` binario, si un operando es string, JavaScript concatena: convierte 10 a texto. En cambio, el `-` unario convierte `"1"` al número $-1$, y luego la suma es numérica.

> [!question]- ¿Qué problema resuelve TypeScript que JavaScript no?
> Detectar errores de tipos antes de ejecutar, como acceder a una propiedad que no existe. JavaScript, por su tipado dinámico, solo los manifiesta en ejecución, muchas veces como un `undefined` silencioso.
