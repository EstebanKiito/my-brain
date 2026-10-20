---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Gestión del curso"
tags:
  - web
  - gestion-del-curso
  - recursos
  - origen/complemento
prerrequisitos:
  - "[[01 - Evaluación y organización de IIC2513]]"
---

# Material de Tecnologías y Aplicaciones Web

El curso se apoya en documentación pública más que en un libro. Esta nota reúne las referencias recomendadas a lo largo del semestre, ordenadas por para qué sirven, junto con las clases y su correspondencia con los temas del vault.

## Clases y temas del vault

| Clases | Tema del vault |
|---|---|
| 0 | Gestión del curso |
| 1 | Fundamentos de la web |
| 2 | HTML y CSS |
| 3 | JavaScript como lenguaje |
| 4 | Asincronía en JavaScript; DOM y eventos |
| 5 | React |
| 6 | APIs web y REST |
| 7 | Node.js |
| 8 | Servidores y aplicaciones web |
| 9 | Construir una API con Express |
| 10 | Calidad, CI y CD |
| 12 y 13 | Diseño web; CSS moderno |
| 14 | Cookies y sesiones |
| 15 | Autenticación y autorización |
| 16 | Almacenamiento en el cliente |
| 17 | Tecnologías web adicionales |
| 18 | Testing en la web |
| 19 | Escala e ingeniería inversa |
| 20 | IA para desarrolladores |
| 21 y 22 | Privacidad y ética |

## Documentación de referencia

| Recurso | Para qué |
|---|---|
| **MDN Web Docs** | La referencia principal: HTML, CSS, JavaScript, HTTP y las Web APIs |
| **JavaScript.info** | Tutorial completo de JavaScript moderno, desde lo básico hasta el DOM y la asincronía |
| **W3Schools** | Ejemplos rápidos de HTML, CSS y JS |
| **react.dev** | Documentación oficial de React y sus hooks |
| **Documentación de Express, Sequelize y Jest** | Referencia de cada librería del stack |
| **CSS-Tricks** y las guías interactivas de **Josh W. Comeau** | Flexbox y Grid explicados con ejemplos |
| **Can I Use** | Qué navegadores soportan cada funcionalidad |
| **Guía de estilo de Airbnb** | Convenciones de JavaScript |

## Herramientas

- **DevTools** del navegador: inspeccionar el DOM y los estilos, la pestaña *Network* y el almacenamiento.
- **Postman** o `curl`: probar endpoints sin escribir código.
- **CodePen** y **JSFiddle**: probar HTML, CSS y JS en línea; **CSSBattle** para practicar CSS.
- **Figma**: prototipar interfaces.
- **WebAIM Contrast Checker** y **WAVE**: evaluar la accesibilidad.
- **Have I Been Pwned** y **Mozilla Monitor**: revisar si un correo apareció en una brecha de datos.

## Repositorios de ejemplo del curso

La organización IIC2513 en GitHub publica implementaciones de referencia para seguir las clases paso a paso (conviene seguir los commits):

- **TodoApp**: una aplicación React creada con Vite, incluido un ejemplo de `fetch`.
- **primera-API-express**: la API de películas con Express, Sequelize y PostgreSQL.
- **Mi-primera-GA**: GitHub Actions con un workflow de ESLint.

> [!tip] Cómo usar este material
> Los temas del vault resumen y ordenan los conceptos. Para los detalles de una API o de una propiedad (todos los parámetros de `fetch`, cada valor de `grid-template`), la fuente es la documentación oficial, que se mantiene actualizada.

## Preguntas de repaso

> [!question]- ¿Dónde se revisa si una propiedad de CSS nueva se puede usar en producción?
> En Can I Use, que muestra qué versiones de cada navegador la soportan.

> [!question]- ¿Qué herramienta permite probar un endpoint sin escribir código?
> Postman (o `curl` desde la terminal): se arma la request con su método, headers y body, y se ve la respuesta completa.

> [!question]- ¿Por qué conviene seguir los commits de los repositorios de ejemplo y no solo mirar el resultado final?
> Porque cada commit corresponde a un paso de la clase (crear el proyecto, agregar el router, configurar Sequelize…), y así se entiende el orden en que se construye la aplicación y por qué existe cada archivo.
