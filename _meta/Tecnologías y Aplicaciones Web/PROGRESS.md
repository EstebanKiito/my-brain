# Progreso de la migración — Tecnologías y Aplicaciones Web (IIC2513)

Rama: `migrar/tecnologias-web`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Tecnologías y Aplicaciones Web" --tema "<Tema>"` revisando el código de salida; en cada pausa de revisión (después de los temas 01, 06, 11, 16 y al cierre), la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Tecnologías y Aplicaciones Web/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de la web | `01-Fundamentos de la web/` | ✅ hecho | 8 + índice | 7 + 3 |
| 2 | HTML y CSS | `02-HTML y CSS/` | ✅ hecho | 5 + índice | 3 + 2 |
| 3 | JavaScript como lenguaje | `03-JavaScript como lenguaje/` | ✅ hecho | 5 + índice | 0 + 0 |
| 4 | Asincronía en JavaScript | `04-Asincronía en JavaScript/` | ✅ hecho | 4 + índice | 8 + 0 |
| 5 | DOM y eventos | `05-DOM y eventos/` | ✅ hecho | 3 + índice | 9 + 2 |
| 6 | React | `06-React/` | ✅ hecho | 5 + índice | 13 + 0 |
| 7 | APIs web y REST | `07-APIs web y REST/` | ✅ hecho | 4 + índice | 0 + 0 |
| 8 | Node.js | `08-Node.js/` | ⏳ pendiente | – | – |
| 9 | Servidores y aplicaciones web | `09-Servidores y aplicaciones web/` | ⏳ pendiente | – | – |
| 10 | Construir una API con Express | `10-Construir una API con Express/` | ⏳ pendiente | – | – |
| 11 | Calidad, CI y CD | `11-Calidad, CI y CD/` | ⏳ pendiente | – | – |
| 12 | Diseño web | `12-Diseño web/` | ⏳ pendiente | – | – |
| 13 | CSS moderno | `13-CSS moderno/` | ⏳ pendiente | – | – |
| 14 | Cookies y sesiones | `14-Cookies y sesiones/` | ⏳ pendiente | – | – |
| 15 | Autenticación y autorización | `15-Autenticación y autorización/` | ⏳ pendiente | – | – |
| 16 | Almacenamiento en el cliente | `16-Almacenamiento en el cliente/` | ⏳ pendiente | – | – |
| 17 | Tecnologías web adicionales | `17-Tecnologías web adicionales/` | ⏳ pendiente | – | – |
| 18 | Testing en la web | `18-Testing en la web/` | ⏳ pendiente | – | – |
| 19 | Escala e ingeniería inversa | `19-Escala e ingeniería inversa/` | ⏳ pendiente | – | – |
| 20 | IA para desarrolladores | `20-IA para desarrolladores/` | ⏳ pendiente | – | – |
| 21 | Privacidad y ética | `21-Privacidad y ética/` | ⏳ pendiente | – | – |
| 22 | Gestión del curso | `22-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): prosa reescrita que mezcla los apuntes con el material de clase, sin marcas de procedencia ni citas literales, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables.
- Prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador da advertencias y no errores.
- **Apuntes:** cubren las clases 0-6 y son buenos; se conservan sus conceptos, ejemplos y código, corrigiendo erratas y ordenando. Desde la clase 7 la fuente es el material de clase.
- **Slides:** ningún PDF entra al repo (no tienen licencia). Las útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` y se registran con `tipo: "slide"` y `original: …pdf#page=N`.
- **Código:** JavaScript corto, ejecutado con `node` (v20) antes del commit; lo que depende del navegador o de React se revisa con `node --check` o se marca como ilustrativo.
- **Tareas y proyecto:** solo lo genérico (flujo de `sequelize-cli`, setup de Postgres, router de Express) con modelos de ejemplo neutros; nombres, rutas, usuarios, contraseñas y modelos del proyecto quedan en `aceptados`.
- **Otros ramos:** se enlazan en vez de duplicar (HTTP y DNS en Sistemas Operativos y Redes; HTML, CSS, MVC y testing en Ingeniería de Software; ORMs, NoSQL y privacidad en Bases de Datos).

## Registro

- **2026-10-19 · Fundamentos de la web** (tema piloto, queda para revisión manual del usuario). Fuentes: `apuntes` clase 1 completa (capa física, URLs, IANA, TLD, IP, DNS, HTTP, métodos, status codes, capas y definiciones). Complementos: slides de la clase 1 (historia, routers/módem/ISP, IXP y cables submarinos, header `Host` y versiones de HTTP, TLS y las preguntas frecuentes sobre query strings, `100 Continue`, VPN, proxy, incógnito, redes públicas, LAN/MAN/WAN, port forwarding, resolvers DNS, `ww2`). 8 notas de 61 a 91 líneas; 7 imágenes de apuntes y 3 recortes de slides (sintaxis de la URL, resolución DNS, sesión TLS). Se omitieron las preguntas anecdóticas de las slides (Flash, microondas, Eduroam, dark web, PageRank, MAC) y las cookies, que van en su propio tema. El link de los apuntes a "Apuntes - Redes IIC2333" se reemplazó por wikilinks a Sistemas Operativos y Redes. Cobertura [3]: 47 bloques sin coincidencia textual, revisados a mano: todos los conceptos están reescritos en las notas. 2 dudas informativas.
- **2026-10-19 · HTML y CSS.** Fuentes: `apuntes` clase 2 (HTML, CSS, modelo de caja, DOM, CSSOM). Complementos: slides de la clase 2 (historia de HTML y CSS, anatomía de elementos y reglas, esqueleto del documento, tags, HTML5 con audio/video/SVG, selectores, tres formas de insertar CSS, cascada, DevTools, critical rendering path). 5 notas; 3 imágenes de apuntes y 2 recortes de slides (HTML4 frente a HTML5, critical rendering path). Se agregó, como conocimiento general, la especificidad dentro de un mismo nivel de la cascada y `box-sizing`. Sin dudas nuevas.
- **2026-10-19 · JavaScript como lenguaje.** Fuentes: `apuntes` clase 3 (características del lenguaje, TypeScript, declaración frente a inicialización). Complementos: slides de la clase 3 (historia, ECMAScript y TC39, conversión implícita, let/const/var, scope, hoisting, tipos, objetos y referencias, colecciones, operadores, control de flujo, switch, funciones, parámetros por defecto, clases, Array.from/of, módulos). 5 notas sin imágenes (las slides son casi solo código, que va como bloques). Todos los bloques JS se ejecutaron con `node` v20 (los módulos, como dos archivos). Se omitieron las encuestas (Octoverse, Stack Overflow, State of JS) y la disputa de la marca con Oracle. 3 dudas informativas.
- **2026-10-19 · Asincronía en JavaScript.** Fuentes: `apuntes` clase 4 hasta "Manejo del DOM" (asincronía, callbacks, callback hell, promesas, then, catch, fetch, async y await). Complementos: slides de la clase 4 (definición de síncrono y asíncrono, tipos de callbacks, constructor y estados, variantes del manejo de errores, cadena cleanRoom, Promise.all). 4 notas; 8 imágenes de apuntes (dos son código de la receta con callbacks y con promesas, transcritas). Se conservaron los ejemplos de los apuntes (cocinar, la promesa de la mamá, fetchData, "Han pasado 84 años"); el código de los apuntes que traía la salida mezclada con el código se separó en comentarios. Todo se ejecutó con `node`, incluido `fetch` contra jsonplaceholder. Sin dudas nuevas.
- **2026-10-19 · DOM y eventos.** Fuentes: `apuntes` clase 4 desde "Manejo del DOM" (HTML DOM, jerarquía, búsqueda por id, selector y getElementsBy*, propiedades de nodos, script src, ejemplos de control del DOM, eventos, event listener, objeto Event). Complementos: slides de la clase 4 (métodos de contenido y estilo, diagrama de propiedades de nodos, target y currentTarget con capturing y bubbling). 3 notas; 9 imágenes de apuntes y 2 recortes de slides (al de capturing y bubbling se le tapó un trozo de texto de la slide). Se agregaron como conocimiento general `defer`, la delegación de eventos y el riesgo de XSS con `innerHTML`. El código DOM se probó con Node y jsdom (búsquedas, colecciones vivas, submit con preventDefault y bubbling). Sin dudas nuevas.
- **2026-10-19 · React.** Fuentes: `apuntes` clase 5 completa (React, MVC, cuándo usarlo, componentes, rendering, elemento, JSX, Virtual DOM, tipos de componentes, props, state, eventos, handlers como props, ciclo de vida, hooks). Complementos: slides de la clase 5 (librería frente a framework, createElement y children, JSX con expresiones y map, cómo empezar en 4 pasos, aplicación mínima, familias de hooks, npm y Vite). 5 notas; 13 imágenes de apuntes. Las líneas de los apuntes sobre las tareas T1 y T2 y el alcance de la clase quedan en `aceptados` para Gestión del curso. Se agregaron como conocimiento general las reglas de los hooks, `key` en listas, la estructura de un proyecto Vite y `dependencies` frente a `devDependencies`. El código se compiló con esbuild y se ejecutó con React 19.3 y jsdom (createElement igual a JSX, contador, handlers como props, contexto con y sin provider, orden de efectos y limpieza). 3 dudas informativas.
- **2026-10-19 · APIs web y REST.** Fuentes: `apuntes` clase 6 (definición de API). Complementos: slides de la clase 6 (API web, endpoints, JSON y XML, CRUD e Instagram, REST y sus principios, stateless y tokens, flujo de autenticación, revocación, documentación de GitHub, OpenAPI, APIs no documentadas, quién consume APIs, AJAX, XMLHttpRequest, fetch, Axios, Postman). 4 notas sin imágenes (el flujo de autenticación va como diagrama Mermaid). Se agregaron como conocimiento general `PUT` frente a `PATCH`, el significado de Bearer y que `fetch` no rechaza ante códigos de error. Probado con Node: fetch a la API de GitHub, 404 sin rechazo, Axios con 401 y XMLHttpRequest con jsdom. 1 duda informativa.
