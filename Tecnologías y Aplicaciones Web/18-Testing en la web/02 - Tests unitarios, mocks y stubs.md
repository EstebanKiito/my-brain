---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Testing en la web"
tags:
  - web
  - testing
  - mocks
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es testing y sus niveles]]"
---

# Tests unitarios, mocks y stubs

Un test unitario prueba una sola pieza. Pero casi ninguna pieza vive sola: llama a una base de datos, a un servicio de pagos o a una API externa. Para probarla aislada hay que **reemplazar** esas dependencias por imitaciones controladas, los **stubs** y los **mocks**, y para poder reemplazarlas el código tiene que estar diseñado para permitirlo.

## Elegir los casos

Una función que valida un número de teléfono:

```javascript
function validatePhoneNumber(input) {
  if (typeof input !== 'string') return false;
  const digits = input.replace(/[\s()-]/g, '');   // quitar espacios, paréntesis y guiones
  return /^(\+1)?\d{10}$/.test(digits);
}
module.exports = { validatePhoneNumber };
```

Hay que probar dos cosas: que retorne `true` con teléfonos válidos y `false` con los inválidos. Los casos se eligen para cubrir las variantes y los bordes:

```javascript
const { validatePhoneNumber } = require('./phoneValidator');

describe('validatePhoneNumber()', () => {
  test('returns true for valid phone numbers', () => {
    expect(validatePhoneNumber('1234567890')).toBe(true);           // 10 dígitos
    expect(validatePhoneNumber('+1 (123) 456-7890')).toBe(true);    // código de país y separadores
  });

  test('returns false for invalid phone numbers', () => {
    expect(validatePhoneNumber('123-45-6789')).toBe(false);         // pocos dígitos
    expect(validatePhoneNumber(1234567890)).toBe(false);            // tipo incorrecto
  });
});
```

> [!warning] El test encontró un error
> Una versión que aplica la regex directamente sobre el input, sin quitar antes los separadores, rechaza `'+1 (123) 456-7890'`, y el segundo `expect` falla. Es justamente lo que debe hacer un test: revelar que la implementación no cumple lo especificado.

## Stubs y mocks

Ambos son **imitaciones** de objetos reales, pero se usan para cosas distintas:

| | **Stub** | **Mock** |
|---|---|---|
| Qué hace | Entrega resultados predefinidos cuando se le llama | Además, **verifica** que se llamen ciertos métodos |
| Para qué | Probar un componente aislado sin la dependencia real (por ejemplo, sin la base de datos) | Comprobar que la interacción ocurrió como se esperaba |
| Si no se le llama | Al test no le importa | El test debe fallar |

En resumen: si el test solo necesita **proveer datos de entrada**, se usa un stub; si además debe **verificar la interacción**, un mock.

## Inyección de dependencias

Una clase que crea su propia dependencia no se puede probar de forma aislada:

```javascript
class AccountServices {
  constructor() {
    this.webService = new BankWebService();   // dependencia fija: siempre el banco real
  }
}
```

La solución es **invertir la dependencia**: en lugar de que la clase la cree, se la entregan desde afuera. Así, en los tests se le puede pasar un objeto falso:

```javascript
class AccountServices {
  constructor(bankWebService) {
    this.bankWebService = bankWebService;     // dependencia inyectada
  }

  registerUser(cardNumber) {
    const accepted = this.bankWebService.verifyCard(cardNumber);
    if (!accepted) return 'Tarjeta rechazada, revise sus datos';
    return 'Usuario registrado con éxito';
  }
}
module.exports = AccountServices;
```

```javascript
const AccountServices = require('./AccountServices');

test('retorna mensaje apropiado si la tarjeta es rechazada', () => {
  const mockBankService = {
    verifyCard: jest.fn().mockReturnValue(false),    // el banco falso siempre rechaza
  };
  const account = new AccountServices(mockBankService);

  expect(account.registerUser('123456789')).toBe('Tarjeta rechazada, revise sus datos');
  expect(mockBankService.verifyCard).toHaveBeenCalledWith('123456789');   // verifica la interacción
});
```

Sin tocar el banco real, el test comprueba el caso de rechazo, que sería difícil de provocar con un servicio de verdad. Con `mockReturnValue(true)` se prueba el caso de éxito.

> [!tip] Diseñar para poder probar
> Que algo sea difícil de testear suele indicar un problema de diseño: una dependencia fija o una función que hace demasiadas cosas. La inyección de dependencias mejora tanto la testeabilidad como la flexibilidad del código.

## Preguntas de repaso

> [!question]- ¿Cuándo conviene un mock en vez de un stub?
> Cuando además de entregar datos hay que verificar que la interacción ocurrió: que se llamó cierto método, con ciertos argumentos o cierta cantidad de veces.

> [!question]- ¿Por qué la primera versión de `AccountServices` no se puede probar de forma aislada?
> Porque crea internamente su `BankWebService`: el test no puede reemplazarlo por uno falso, así que cada prueba llamaría al banco real.

> [!question]- ¿Cómo se eligen buenos casos para un test unitario?
> Cubriendo los casos válidos típicos, las variantes de formato aceptadas, los bordes (largos mínimos y máximos) y los inválidos, incluidos los de tipo incorrecto.
