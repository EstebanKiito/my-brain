---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[01 - Qué es el testing de software|Qué es el testing de software]]", "[[03 - Patrón MVC en Rails|Patrón MVC en Rails]]"]
---
# Niveles de testing en Rails

En Rails se prueba en tres niveles: **unit** (modelos aislados), **integration** (controladores) y **system** (la app completa, como un usuario).

## Testing con Rails
- **Unit testing:** en Rails, trata de verificar si las **clases del modelo** que creamos funcionan correctamente **en isolación** (por sí solas, sin interacción de otras).
- **Integration testing:** en Rails, trata de verificar si los **controladores** creados en el proyecto están funcionando de manera correcta.
- **System testing:** en Rails, evalúa la funcionalidad del **sistema como un todo**. Es como abrir la página web e interactuar con ella para ver que todo funcione. Se puede hacer **manual o automática**.

| Nivel | Qué prueba | Clase base | Carpeta |
|---|---|---|---|
| Unit | modelo | `ActiveSupport::TestCase` | `test/models/` |
| Integration | controlador | `ActionDispatch::IntegrationTest` | `test/controllers/` |
| System | sistema completo | `ApplicationSystemTestCase` | `test/system/` |

> [!tip] Complemento (slides "Testing")
> - El system testing automático se hace con un **bot** que maneja el navegador (en Rails, Capybara con Selenium).
> - Se profundiza en [[04 - Unit tests en Rails|Unit tests]] e [[07 - Integration tests en Rails|Integration tests]].
> - Todos se ejecutan con `rails test`. Los de sistema, con `rails test:system`.

## Preguntas de repaso

1. ¿Qué prueba cada nivel en Rails?
> [!question]- Respuesta
> Unit: las clases del modelo, aisladas. Integration: los controladores (requests y responses). System: la aplicación completa, interactuando con la página como un usuario.

2. ¿El system testing es manual o automático?
> [!question]- Respuesta
> Puede ser ambos: manual (una persona usa la app) o automático (un bot controla el navegador).

3. ¿Qué significa probar un modelo "en isolación"?
> [!question]- Respuesta
> Probar la clase por sí sola, sin depender del controlador, de las vistas ni de otras clases.
