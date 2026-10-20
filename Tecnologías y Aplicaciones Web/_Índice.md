# Tecnologías y Aplicaciones Web (IIC2513) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto atómico**: basta con buscar el concepto, sin saber en qué clase se vio. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` y `prerrequisitos` (conceptos que conviene leer antes).
- **Cuerpo:** prosa explicativa que parte por el problema que resuelve cada tecnología, con ejemplos de código en JavaScript, JSX, TypeScript, CSS y SQL. Todo el código se ejecutó o compiló (Node.js, jsdom, React, esbuild, tsc, Jest, Sass, PostgreSQL).
- **Otros ramos:** lo que ya está en otro ramo se enlaza en vez de repetirse: HTTP, DNS, TCP y UDP en [[Sistemas Operativos y Redes/_Índice|Sistemas Operativos y Redes]]; HTML, CSS, MVC y testing con Rails en [[Ingeniería de Software/_Índice|Ingeniería de Software]]; ORMs, migraciones, NoSQL y privacidad en [[Bases de Datos/_Índice|Bases de Datos]].
- **Imágenes:** capturas de los apuntes y figuras de las slides en PNG, con su transcripción en un callout plegable.
- **Cierre:** cada nota termina con preguntas de repaso con la respuesta oculta en un callout plegable.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Tecnologías y Aplicaciones Web/01-Fundamentos de la web/_Índice\|Fundamentos de la web]] | Internet e ISPs, URLs, IP y DNS, HTTP (mensajes, métodos y códigos), TCP, UDP y TLS |
| [[Tecnologías y Aplicaciones Web/02-HTML y CSS/_Índice\|HTML y CSS]] | Documento HTML, HTML5 semántico, reglas y cascada de CSS, modelo de caja, DOM, CSSOM y rendering |
| [[Tecnologías y Aplicaciones Web/03-JavaScript como lenguaje/_Índice\|JavaScript como lenguaje]] | Historia y ECMAScript, TypeScript, variables y scope, tipos, operadores, control de flujo, funciones, clases y módulos |
| [[Tecnologías y Aplicaciones Web/04-Asincronía en JavaScript/_Índice\|Asincronía en JavaScript]] | Callbacks, callback hell, promesas y sus estados, encadenamiento, manejo de errores y async/await |
| [[Tecnologías y Aplicaciones Web/05-DOM y eventos/_Índice\|DOM y eventos]] | Búsqueda y recorrido de nodos, creación de elementos, eventos y propagación |
| [[Tecnologías y Aplicaciones Web/06-React/_Índice\|React]] | JSX y Virtual DOM, componentes, props y state, eventos, ciclo de vida, hooks y proyecto con Vite |
| [[Tecnologías y Aplicaciones Web/07-APIs web y REST/_Índice\|APIs web y REST]] | APIs web, CRUD, principios REST, autenticación con tokens, documentación y consumo con fetch y Axios |
| [[Tecnologías y Aplicaciones Web/08-Node.js/_Índice\|Node.js]] | Runtime y arquitectura de Node, call stack y event loop, scripts, módulos y servidor HTTP |
| [[Tecnologías y Aplicaciones Web/09-Servidores y aplicaciones web/_Índice\|Servidores y aplicaciones web]] | Servidor web y aplicación web, frontend y backend, MVC, CSR/SSR/SSG/ISR, middleware y ORM |
| [[Tecnologías y Aplicaciones Web/10-Construir una API con Express/_Índice\|Construir una API con Express]] | Proyecto Node, routers, Sequelize con PostgreSQL, modelos, migraciones, seeds y CRUD |
| [[Tecnologías y Aplicaciones Web/11-Calidad, CI y CD/_Índice\|Calidad, CI y CD]] | Calidad y QA, análisis estático con ESLint, code review, GitHub flow, commits, CI con GitHub Actions y CD |
| [[Tecnologías y Aplicaciones Web/12-Diseño web/_Índice\|Diseño web]] | UI y UX, prototipado, jerarquía visual, patrones, identidad visual, responsivo, accesibilidad e impacto ambiental |
| [[Tecnologías y Aplicaciones Web/13-CSS moderno/_Índice\|CSS moderno]] | Rendering entre navegadores, unidades, variables, nesting, selectores, Flexbox, Grid, animaciones, frameworks y design systems |
| [[Tecnologías y Aplicaciones Web/14-Cookies y sesiones/_Índice\|Cookies y sesiones]] | Cookies y Set-Cookie, sesiones con session id, Express y abusos (tracking, CSRF, robo de sesión) |
| [[Tecnologías y Aplicaciones Web/15-Autenticación y autorización/_Índice\|Autenticación y autorización]] | Autenticación frente a autorización, contraseñas, hashing con bcrypt, JWT, OAuth y SSO |
| [[Tecnologías y Aplicaciones Web/16-Almacenamiento en el cliente/_Índice\|Almacenamiento en el cliente]] | Cookies desde JS, localStorage y sessionStorage, IndexedDB, Cache API, CDN y bases SQL y NoSQL |
| [[Tecnologías y Aplicaciones Web/17-Tecnologías web adicionales/_Índice\|Tecnologías web adicionales]] | TypeScript, WebAssembly, WebSockets y Progressive Web Apps |
| [[Tecnologías y Aplicaciones Web/18-Testing en la web/_Índice\|Testing en la web]] | Niveles de testing, TDD, mocks y stubs, Jest, CI y tests de front-end |
| [[Tecnologías y Aplicaciones Web/19-Escala e ingeniería inversa/_Índice\|Escala e ingeniería inversa]] | Colas, balanceadores y bases en tiempo real; ingeniería inversa y tipos de hackers |
| [[Tecnologías y Aplicaciones Web/20-IA para desarrolladores/_Índice\|IA para desarrolladores]] | IA, ML y DL, modelos de lenguaje, RAG y herramientas de IA para programar |
| [[Tecnologías y Aplicaciones Web/21-Privacidad y ética/_Índice\|Privacidad y ética]] | Privacidad, GDPR, CCPA, ley chilena, código de ética de la ACM, IA generativa y código abierto |
| [[Tecnologías y Aplicaciones Web/22-Gestión del curso/_Índice\|Gestión del curso]] | Evaluación, fórmulas, integridad académica, tareas, proyecto y material del curso |

## Ruta de estudio sugerida
1. **Fundamentos de la web → HTML y CSS:** qué pasa entre la URL y la página, y cómo se describe el contenido y su presentación.
2. **JavaScript → Asincronía → DOM y eventos → React:** el lenguaje del navegador, cómo espera sin bloquear, cómo modifica la página y cómo construir interfaces con componentes.
3. **APIs y REST → Node.js → Servidores → API con Express:** el otro lado, desde consumir una API hasta construir la propia con Sequelize y PostgreSQL.
4. **Calidad, CI y CD → Testing:** desarrollar bien y automatizar la verificación.
5. **Diseño web → CSS moderno:** que la aplicación, además de funcionar, se entienda y se vea bien en cualquier pantalla.
6. **Cookies y sesiones → Autenticación y autorización → Almacenamiento en el cliente:** identificar usuarios, proteger sus credenciales y decidir dónde vive cada dato.
7. **Tecnologías adicionales → Escala e ingeniería inversa → IA para desarrolladores → Privacidad y ética:** el mundo real, desde TypeScript y PWAs hasta la responsabilidad de quien desarrolla.
8. **Gestión del curso:** evaluaciones, tareas, proyecto y material de referencia.
