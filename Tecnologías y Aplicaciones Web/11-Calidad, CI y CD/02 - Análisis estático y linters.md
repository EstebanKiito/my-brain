---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Calidad, CI y CD"
tags:
  - web
  - calidad
  - eslint
  - linter
  - origen/complemento
prerrequisitos:
  - "[[01 - Calidad de software y QA]]"
---

# Análisis estático y linters

Muchos errores se pueden detectar **sin ejecutar** el programa: una variable que nunca se usa, un punto y coma olvidado, una comparación con `==` que debería ser `===`. Revisarlos a mano es tedioso y poco confiable. Para eso existen los **linters**, herramientas que automatizan esa revisión.

## Análisis estático

El **análisis estático** examina el código fuente **sin ejecutarlo** (de ahí "estático"), normalmente con herramientas automáticas, según criterios predefinidos: un conjunto de reglas o una guía de estilo. Permite:

- identificar código duplicado;
- mejorar el manejo de errores;
- encontrar problemas de sintaxis;
- detectar *code smells* (señales de diseño problemático);
- cumplir con buenas prácticas.

## Linters

Un **linter** automatiza el análisis estático para un lenguaje: ESLint para JavaScript, RuboCop para Ruby, Pylint o Flake8 para Python.

**ESLint** define una base de reglas para evaluar código JavaScript. Es:

- **configurable**: se elige qué reglas aplicar y con qué severidad;
- **extensible**: se agregan capacidades con plugins (por ejemplo, reglas para React).

Muchos equipos adoptan una guía de estilo existente en vez de definir todas las reglas; una de las más conocidas es la **guía de estilo de JavaScript de Airbnb**.

## Un ejemplo con ESLint

```bash
yarn init -y
yarn add eslint --dev
```

```javascript
// eslint.config.js
module.exports = [
  {
    rules: {
      semi: 'error',            // exigir punto y coma
      'prefer-const': 'error',  // usar const si la variable no se reasigna
    },
  },
];
```

```javascript
// src/index.js
let a = 3
console.log(a);
```

```text
$ yarn run eslint .
src/index.js
  1:5   error  'a' is never reassigned. Use 'const' instead  prefer-const
  1:10  error  Missing semicolon                             semi
✖ 2 problems (2 errors, 0 warnings)
  2 errors and 0 warnings potentially fixable with the `--fix` option.
```

Con `yarn run eslint . --fix`, ESLint corrige solo lo que puede arreglar de forma segura, y el archivo queda como `const a = 3;`.

> [!tip] El linter como acuerdo de equipo
> Las reglas del linter son decisiones que el equipo toma una vez (comillas, punto y coma, `const`) y que la herramienta hace cumplir siempre. Así el code review se dedica a la lógica y no a discutir estilo.

> [!warning] El linter no reemplaza a los tests
> Un código sin advertencias del linter puede estar perfectamente equivocado. El análisis estático encuentra problemas de forma y algunos errores típicos, pero no verifica que el programa haga lo que debe.

El linter rinde más cuando se ejecuta solo en cada push, como parte de la integración continua: [[04 - Integración y despliegue continuos|Integración y despliegue continuos]].

## Preguntas de repaso

> [!question]- ¿Qué significa que el análisis sea "estático"?
> Que se hace sobre el código fuente sin ejecutarlo. Por eso es rápido y puede correr en cada cambio, pero solo detecta problemas visibles en el texto del programa, no fallas de comportamiento.

> [!question]- ¿Qué hace `eslint --fix` y qué no puede hacer?
> Corrige automáticamente las infracciones que tienen un arreglo seguro y mecánico, como agregar un punto y coma o cambiar `let` por `const`. No puede corregir errores de lógica ni reglas cuyo arreglo requiere decidir qué quiso hacer el programador.

> [!question]- ¿Por qué conviene adoptar una guía como la de Airbnb?
> Porque entrega un conjunto de reglas ya pensado y conocido, que el equipo no tiene que discutir desde cero, y deja el código con un estilo uniforme y familiar para otros desarrolladores.
