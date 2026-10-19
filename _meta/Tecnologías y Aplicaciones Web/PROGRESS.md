# Progreso de la migración — Tecnologías y Aplicaciones Web (IIC2513)

Rama: `migrar/tecnologias-web`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Tecnologías y Aplicaciones Web" --tema "<Tema>"` revisando el código de salida; en cada pausa de revisión (después de los temas 01, 06, 11, 16 y al cierre), la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Tecnologías y Aplicaciones Web/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de la web | `01-Fundamentos de la web/` | ⏳ pendiente | – | – |
| 2 | HTML y CSS | `02-HTML y CSS/` | ⏳ pendiente | – | – |
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
