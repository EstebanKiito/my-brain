# Progreso de la migración — Tecnologías y Aplicaciones Web (IIC2513)

Rama: `migrar/tecnologias-web`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Tecnologías y Aplicaciones Web" --tema "<Tema>"` revisando el código de salida; en cada pausa de revisión (después de los temas 01, 06, 11, 16 y al cierre), la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Tecnologías y Aplicaciones Web/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de la web | `01-Fundamentos de la web/` | ✅ hecho | 8 + índice | 7 + 3 |
| 2 | HTML y CSS | `02-HTML y CSS/` | ✅ hecho | 5 + índice | 3 + 2 |
| 3 | JavaScript como lenguaje | `03-JavaScript como lenguaje/` | ⏳ pendiente | – | – |
| 4 | Asincronía en JavaScript | `04-Asincronía en JavaScript/` | ⏳ pendiente | – | – |
| 5 | DOM y eventos | `05-DOM y eventos/` | ⏳ pendiente | – | – |
| 6 | React | `06-React/` | ⏳ pendiente | – | – |
| 7 | APIs web y REST | `07-APIs web y REST/` | ⏳ pendiente | – | – |
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
