---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Testing en la web"
tags:
  - web
  - testing
  - jest
  - origen/complemento
prerrequisitos:
  - "[[02 - Tests unitarios, mocks y stubs]]"
  - "[[04 - Integración y despliegue continuos]]"
---

# Testing con Jest

**Jest** es el framework de testing más usado en JavaScript: trae el ejecutor de tests, las aserciones y los mocks en una sola herramienta. Esta nota cubre cómo se estructura un test, cómo se compara el resultado con lo esperado, cómo se prueban funciones asíncronas y cómo correr los tests automáticamente en cada push.

## La estructura de un test

Todo test sigue el mismo esquema: **dado** un conjunto de condiciones iniciales (*dado que hoy hace frío*), **cuando** se ejecutan ciertas acciones (*cuando salgo con poco abrigo*), **entonces** se cumplen las expectativas (*entonces me da frío*). En Jest, `describe` agrupa y `test` (o `it`) define cada caso:

```javascript
describe('Dado que hoy hace frío', () => {
  describe('Cuando salgo con poco abrigo', () => {
    test('Entonces me da frío', () => {
      expect(body).toBe('cold');
    });
  });
});
```

## Configuración

```bash
yarn add jest --dev
```

```json
{
  "scripts": {
    "test": "jest --verbose"
  }
}
```

Jest considera archivos de tests a todos los que terminan en `.test.js`. Se ejecutan con `yarn test`.

## `expect` y matchers

Se compara el resultado de una acción (*received*) con el valor esperado (*expected*) mediante un **matcher**:

```javascript
expect(received).toBe(expected);
//  ↑ función de Jest    ↑ matcher

test('adds 2 + 3 to equal 5', () => {
  expect(add(2, 3)).toBe(5);
});
```

| Categoría | Matchers |
|---|---|
| Igualdad | `toBe` (identidad, `===`), `toEqual` (igualdad de contenido, para objetos y arreglos) |
| Truthiness | `toBeNull`, `toBeUndefined`, `toBeTruthy`, `toBeFalsy` |
| Números | `toBeGreaterThan`, `toBeGreaterThanOrEqual`, `toBeLessThan`, `toBeLessThanOrEqual` |
| Strings | `toMatch` (con una regex) |
| Arreglos | `toContain`, `toHaveLength` |
| Objetos | `toHaveProperty` |

Cualquier matcher se niega con `.not`: `expect(x).not.toBeNull()`.

> [!warning] `toBe` no sirve para objetos
> `expect({ a: 1 }).toBe({ a: 1 })` **falla**, porque son dos objetos distintos en memoria. Para comparar contenido se usa `toEqual`.

## Funciones asíncronas

Jest tiene que saber que debe esperar el resultado. Hay tres formas equivalentes:

```javascript
async function asyncAdd(a, b) {
  return a + b;
}

test('(Promise) adds 2 + 3 to equal 5', () => {
  return asyncAdd(2, 3).then((result) => expect(result).toBe(5));    // retornar la promesa
});

test('(resolves) adds 2 + 3 to equal 5', () => {
  return expect(asyncAdd(2, 3)).resolves.toBe(5);
});

test('(async/await) adds 2 + 3 to equal 5', async () => {
  const result = await asyncAdd(2, 3);
  expect(result).toBe(5);
});
```

> [!warning] Olvidar el `return` o el `await`
> Si el test no retorna la promesa ni usa `await`, Jest da el test por terminado antes de que la promesa se resuelva. El `expect` se ejecuta fuera del test: según el caso, el test queda en verde aunque esté mal, o el fallo aparece como un error suelto que no se asocia a ningún test (en Jest 30 incluso puede botar la ejecución completa).

## Funciones mock

`jest.fn()` crea una función falsa que registra cómo fue llamada:

```javascript
const myFn = jest.fn();
const myImplementedFn = jest.fn(() => 'return value');
myFn();
myFn();
myImplementedFn();

console.log(myFn.mock.calls);              // [ [], [] ]: dos llamadas sin argumentos
console.log(myImplementedFn.mock.results); // [ { type: 'return', value: 'return value' } ]
```

## Tests en cada push con GitHub Actions

```yaml
# .github/workflows/jest.yml
name: Tests
run-name: Ejecutando Jest
on: [push]
jobs:
  Ejecutando-Jest:
    runs-on: ubuntu-latest
    timeout-minutes: 5        # siempre poner un límite
    steps:
      - uses: actions/checkout@v4
      - name: Install modules
        run: yarn
      - name: Run Jest
        run: yarn test
```

Si un test falla, Jest termina con un código distinto de 0 y el workflow queda en rojo en el commit y en el PR.

> [!tip] `timeout-minutes` siempre
> Un test que se queda esperando (una promesa que nunca se resuelve, un servidor sin cerrar) dejaría el job corriendo hasta el límite por defecto de GitHub, que es de horas.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `toBe` y `toEqual`?
> `toBe` compara identidad (`===`), así que dos objetos con el mismo contenido no son iguales. `toEqual` compara el contenido recursivamente.

> [!question]- ¿Qué pasa si un test asíncrono no retorna la promesa ni usa `await`?
> Jest da el test por terminado antes de que la promesa se resuelva, así que el `expect` se ejecuta fuera del test: este puede quedar en verde aunque el código esté mal, o el fallo aparece desligado del test que lo causó.

> [!question]- ¿Qué información guarda una función creada con `jest.fn()`?
> Sus llamadas (`mock.calls`, con los argumentos de cada una) y sus resultados (`mock.results`), lo que permite verificar cómo la usó el código bajo prueba.
