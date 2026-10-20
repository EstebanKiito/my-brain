---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Testing en la web"
tags:
  - web
  - testing
  - frontend
  - origen/complemento
prerrequisitos:
  - "[[03 - Testing con Jest]]"
  - "[[02 - Componentes, props y state]]"
---

# Tests de front-end

Que la API responda bien no garantiza que el usuario pueda usar la aplicación. Los **tests de front-end** validan que la interfaz gráfica funcione: que un formulario acepte los caracteres correctos, que aparezcan los mensajes de error, que la página cargue a tiempo y que se vea bien en distintos navegadores y dispositivos.

Sirven para identificar problemas de rendimiento, verificar el funcionamiento en distintos navegadores y dispositivos, y comprobar la integración con servicios externos.

## Tipos de tests de front-end

| Tipo | Qué verifica | Herramientas |
|---|---|---|
| **Regresión visual** | Que un cambio de código no altere la interfaz más allá de lo esperado | Comparación de capturas de pantalla |
| **Performance** | El tiempo de respuesta bajo cierta carga de usuarios e interacciones, para encontrar cuellos de botella | JMeter, BlazeMeter |
| **Accesibilidad** | Que la mayor cantidad de personas, incluidas las que tienen dificultades visuales u otras necesidades, pueda usar la aplicación | WAVE |
| **End-to-end** (E2E) | El funcionamiento de principio a fin en un escenario real, emulando a un usuario a través de la interfaz | Selenium, Playwright |

Un test de **regresión**, en general, verifica que los cambios no rompan funcionalidades que ya existían. La **regresión visual** aplica la misma idea al aspecto: compara capturas de antes y después y marca las diferencias.

## E2E: emular a un usuario

Un test end-to-end controla un navegador real: escribe en los campos, hace click y espera respuestas, como lo haría una persona.

```javascript
test('Successful login', async () => {
  // Ingresar las credenciales
  await driver.findElement(webdriver.By.id('username')).sendKeys(TEST_USER);
  await driver.findElement(webdriver.By.xpath('//*[@type="password"]')).sendKeys(TEST_PWD);

  // Hacer click y esperar la respuesta
  await driver.findElement(webdriver.By.css('button[type=submit]')).click();
  const output = await driver.wait(
    webdriver.until.elementLocated(webdriver.By.id('logged-in')),
    1000
  );

  // Verificar el resultado
  const outputVal = await output.getAttribute('innerHTML');
  expect(outputVal).toEqual('You are now logged in!');
});
```

> [!warning] Los E2E son lentos y frágiles
> Levantan un navegador, dependen de tiempos de espera y se rompen con cambios menores de la interfaz (un id que cambia). Por eso se escriben pocos, solo para los flujos críticos, como el login o el pago.

## Testing Library y React

**Testing Library** prueba los componentes **como los usa una persona**: busca elementos por su texto, su rol o su etiqueta, no por detalles de implementación como clases CSS o el estado interno. Su versión para React es **React Testing Library** (RTL).

Los tests siguen el patrón **Arrange-Act-Assert**:

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import Fetch from './fetch';

test('loads and displays greeting', async () => {
  // ARRANGE: dibujar el componente
  render(<Fetch url="/greeting" />);

  // ACT: interactuar como un usuario
  await userEvent.click(screen.getByText('Load Greeting'));
  await screen.findByRole('heading');

  // ASSERT: verificar lo que el usuario ve
  expect(screen.getByRole('heading')).toHaveTextContent('hello there');
  expect(screen.getByRole('button')).toBeDisabled();
});
```

```jsx
it('CheckboxWithLabel changes the text after click', () => {
  const { queryByLabelText, getByLabelText } = render(
    <CheckboxWithLabel labelOn="On" labelOff="Off" />
  );
  expect(queryByLabelText(/off/i)).toBeTruthy();
  fireEvent.click(getByLabelText(/off/i));
  expect(queryByLabelText(/on/i)).toBeTruthy();
});
```

> [!tip] Buscar como busca un usuario
> `getByRole('button')` o `getByText('Load Greeting')` siguen funcionando aunque se cambien las clases o la estructura interna del componente. Además, si un elemento no se encuentra por su rol, probablemente tampoco sea accesible para un lector de pantalla.

## Preguntas de repaso

> [!question]- ¿Qué detecta un test de regresión visual que un test unitario no?
> Cambios no intencionados en el aspecto de la interfaz (un botón desplazado, un color distinto) producidos por modificaciones de código. Un test unitario solo revisa lógica y valores.

> [!question]- ¿Por qué no se escribe todo como test E2E, si es el más realista?
> Porque los E2E son lentos, costosos de mantener y frágiles ante cambios menores de la interfaz. Se reservan para los flujos críticos, y la mayor parte se cubre con tests unitarios y de integración.

> [!question]- ¿Por qué Testing Library busca elementos por rol o texto y no por clase CSS?
> Porque así el test verifica lo que percibe el usuario y no depende de detalles de implementación. Un cambio de estilo no rompe el test, y se refuerza la accesibilidad.
