---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Tecnologías web adicionales"
tags:
  - web
  - typescript
  - origen/complemento
prerrequisitos:
  - "[[01 - Origen de JavaScript, ECMAScript y TypeScript]]"
  - "[[05 - Funciones, clases y módulos en JavaScript]]"
---

# TypeScript en la práctica

El tipado dinámico de JavaScript permite escribir rápido, pero en un proyecto grande los errores de tipo aparecen recién al ejecutar, a veces en producción. **TypeScript** agrega tipos estáticos que el compilador revisa antes de ejecutar. Esta nota recorre las herramientas del lenguaje que más se usan en la práctica.

## Qué es y por qué se usa

- Lo desarrolla Microsoft desde 2012 (la versión 1.0 es de 2014), y es de código abierto.
- Es un **superconjunto** de JavaScript: todo JS válido es TS válido.
- Lo que agrega se elimina al **transpilar** a JavaScript, que es lo que finalmente se ejecuta.
- Ganó tracción cuando Angular lo adoptó como lenguaje principal, y su popularidad sigue creciendo.

Sus beneficios principales:

- **Type safety**: los tipos estáticos detectan errores al compilar, antes de ejecutar.
- **Escalabilidad**: facilita mucho mantener proyectos grandes.
- **Soporte de herramientas**: autocompletado, refactorización y navegación del código; al pasar sobre una variable o función, el editor muestra su tipo.

## Anotaciones e inferencia

```typescript
let favNumber: number = 42;
const COURSES: string[] = ['IIC2513', 'IIC3585'];
let someValue: boolean = false;

favNumber = someValue;
// error TS2322: Type 'boolean' is not assignable to type 'number'.
```

No hace falta anotar todo: TypeScript **infiere** el tipo desde el valor inicial. `let nombre = "Antonio"` es equivalente a `let nombre: string = "Antonio"`. Pero `let cantidad: string = 7` es un error, porque la anotación (`string`) contradice el valor (`number`).

| Herramienta | Ejemplo | Para qué |
|---|---|---|
| `any` | `let item: any = { id: 1 }` | Desactiva la verificación (último recurso) |
| Unión | `obj: string \| number` | Acepta uno de varios tipos |
| `enum` | `enum DoorState { Open, Closed }` | Conjunto cerrado de valores con nombre |
| `interface` | `interface Point { x: number; y: number }` | Forma que debe tener un objeto |
| `type` | `type Car = { year: number; model: string }` | Alias de un tipo (también para uniones) |
| `readonly` | `const names: readonly string[]` | Impide modificar el arreglo |
| `as` | `(x as string).length` | Casting explícito: "confía en mí, es un string" |

## Interfaces y funciones

```typescript
interface Point {
  x: number;
  y: number;
}
let start: Point = { x: 1, y: 2 };
let idk: Point = { x: 2 };
// error TS2741: Property 'y' is missing in type '{ x: number; }' but required in type 'Point'.

function calculate(a: number, b: number): number {
  return a + b + a * b + a ** b;
}
calculate('3', '2');
// error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'.
```

TypeScript usa **tipado estructural** (*duck typing*): dos objetos son del mismo tipo si tienen las mismas propiedades, sin importar cómo se crearon. Si a un objeto le falta una propiedad que el tipo exige (por ejemplo, un método `print`), el compilador lo rechaza.

## Clases, interfaces y herencia

```typescript
interface Shape {
  getArea: () => number;
}

class Rectangle implements Shape {
  public constructor(protected readonly width: number, protected readonly height: number) {}
  public getArea(): number { return this.width * this.height; }
}

class Square extends Rectangle {
  public constructor(width: number) { super(width, width); }
  public override toString(): string { return `Square[width=${this.width}]`; }
}
```

- `private`, `protected` y `public` controlan la visibilidad. Acceder desde afuera a un atributo `private` es un error de compilación (TS2341).
- Escribir `private name: string` como parámetro del constructor declara e inicializa el atributo en una sola línea.
- `readonly` impide cambiar un atributo después del constructor.
- Una clase puede **extender una sola** clase, pero **implementar varias** interfaces.

## Genéricos

Los **genéricos** permiten escribir código que funciona con cualquier tipo sin perder la información de tipos:

```typescript
class NamedValue<T> {
  private _value: T | undefined;
  constructor(private name: string) {}
  public setValue(value: T) { this._value = value; }
  public toString(): string { return `${this.name}: ${this._value}`; }
}

const value = new NamedValue<number>('myNumber');
value.setValue(10);
console.log(value.toString());   // myNumber: 10
// value.setValue('diez');        // error: 'string' no es asignable a 'number'
```

> [!tip] Preferir `unknown` antes que `any`
> `any` apaga el chequeo de tipos por completo. `unknown` también acepta cualquier valor, pero obliga a verificar o castear el tipo antes de usarlo.

> [!warning] Los tipos desaparecen al ejecutar
> TypeScript verifica en tiempo de compilación y luego se transpila a JavaScript sin tipos. Si llega un JSON inesperado desde una API, TypeScript no lo detecta en ejecución: los datos externos hay que validarlos.

## Preguntas de repaso

> [!question]- ¿Por qué `let cantidad: string = 7` es un error pero `let cantidad = 7` no?
> En el primero la anotación exige un `string` y se asigna un `number`. En el segundo no hay anotación: TypeScript infiere `number` a partir del valor.

> [!question]- ¿Qué significa que TypeScript use tipado estructural?
> Que dos tipos son compatibles si tienen la misma forma (las mismas propiedades con los mismos tipos), sin importar su nombre ni cómo se crearon.

> [!question]- ¿Para qué sirven los genéricos?
> Para escribir funciones y clases reutilizables con cualquier tipo, conservando la verificación: un `NamedValue<number>` solo acepta números, aunque la clase se escribió una sola vez.
