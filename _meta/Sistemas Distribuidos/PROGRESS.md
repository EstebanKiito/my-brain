# Progreso de la migración — Sistemas Distribuidos (IIC2523)

Rama: `migrar/sistemas-distribuidos`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Sistemas Distribuidos" --tema "<Tema>"` revisando el código de salida; en cada pausa de revisión (después de los temas 01, 06, 11, 16, 21 y al cierre), la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Sistemas Distribuidos/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de sistemas distribuidos | `01-Fundamentos de sistemas distribuidos/` | ✅ hecho | 5 + índice | 6 + 2 |
| 2 | Procesos e hilos en Python | `02-Procesos e hilos en Python/` | ✅ hecho | 6 + índice | 13 + 0 |
| 3 | Comunicación directa y sockets | `03-Comunicación directa y sockets/` | ✅ hecho | 6 + índice | 3 + 2 |
| 4 | Comunicación indirecta | `04-Comunicación indirecta/` | ✅ hecho | 3 + índice | 3 + 0 |
| 5 | Invocación remota | `05-Invocación remota/` | ⬜ pendiente | – | – |
| 6 | Sincronización de relojes físicos | `06-Sincronización de relojes físicos/` | ⬜ pendiente | – | – |
| 7 | Relojes lógicos y estados globales | `07-Relojes lógicos y estados globales/` | ⬜ pendiente | – | – |
| 8 | Consenso | `08-Consenso/` | ⬜ pendiente | – | – |
| 9 | Elección de líder | `09-Elección de líder/` | ⬜ pendiente | – | – |
| 10 | Exclusión mutua distribuida | `10-Exclusión mutua distribuida/` | ⬜ pendiente | – | – |
| 11 | Tolerancia a fallos | `11-Tolerancia a fallos/` | ⬜ pendiente | – | – |
| 12 | Replicación y modelos de consistencia | `12-Replicación y modelos de consistencia/` | ⬜ pendiente | – | – |
| 13 | Protocolos de replicación | `13-Protocolos de replicación/` | ⬜ pendiente | – | – |
| 14 | Transacciones distribuidas | `14-Transacciones distribuidas/` | ⬜ pendiente | – | – |
| 15 | Control de concurrencia distribuido | `15-Control de concurrencia distribuido/` | ⬜ pendiente | – | – |
| 16 | Teoremas CAP y PACELC | `16-Teoremas CAP y PACELC/` | ⬜ pendiente | – | – |
| 17 | Consistencia centrada en el cliente | `17-Consistencia centrada en el cliente/` | ⬜ pendiente | – | – |
| 18 | Ataques a sistemas distribuidos | `18-Ataques a sistemas distribuidos/` | ⬜ pendiente | – | – |
| 19 | Criptografía | `19-Criptografía/` | ⬜ pendiente | – | – |
| 20 | Autenticación y control de acceso | `20-Autenticación y control de acceso/` | ⬜ pendiente | – | – |
| 21 | Monitoreo de seguridad | `21-Monitoreo de seguridad/` | ⬜ pendiente | – | – |
| 22 | Arquitecturas peer-to-peer | `22-Arquitecturas peer-to-peer/` | ⬜ pendiente | – | – |
| 23 | Casos aplicados | `23-Casos aplicados/` | ⬜ pendiente | – | – |
| 24 | Gestión del curso | `24-Gestión del curso/` | ⬜ pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): prosa reescrita que mezcla los apuntes con el material de clase, sin marcas de procedencia ni citas literales, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables.
- Prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador da advertencias y no errores.
- **Apuntes:** `apuntes_i1` cubre las clases 0-9 y un resumen de la unidad 2; `apuntes_i2`, las clases 11, 12, 14, 15 y 18 y un resumen de la I2. Se conservan sus conceptos, ejemplos y código, corrigiendo erratas y ordenando. Las clases 10 (repaso), 13, 16, 17 y 19-23 no tienen apuntes: la fuente es el material de clase.
- **Slides:** ningún PDF entra al repo (no tienen licencia). Las útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` y se registran con `tipo: "slide"` y `original: …pdf#page=N`. El PDF de la clase 8 adjunto a los apuntes duplica `Clases-I1.pdf` y no se usa.
- **Código:** Python corto (procesos, hilos, sockets, RPC), ejecutado con `python3` antes del commit; lo que necesita dependencias externas (MPI, gRPC) se marca como ilustrativo.
- **Otros ramos:** se enlazan en vez de duplicar (hilos, semáforos, sockets, TCP/UDP, P2P y seguridad en Sistemas Operativos y Redes; ACID, 2PL, deadlocks y NoSQL en Bases de Datos; teorema CAP en Ingeniería de Software; REST, autenticación, OAuth y TLS en Tecnologías y Aplicaciones Web).

## Registro

- **2026-10-20 · Fundamentos de sistemas distribuidos** (tema piloto, queda para revisión manual del usuario). Fuentes: `apuntes_i1` clase 0 (definición, objetivo de orden interno, desafíos, ejemplos de Google, IA, Cloudflare y AWS, casos de Instagram, el banco y Buscacursos) y clase 2 completa (definición, centralizado, descentralizado y distribuido, criterio de la necesidad, seis objetivos con los tipos de transparencia y de escalabilidad, HPC con clúster y grid, sistemas de información y pervasivos). Complementos: slides de las clases 0 y 2 (ejemplo de las fotos de viaje, data centers frente a edge nodes, enfoques de autoridad y robustez, ejemplos de cada objetivo, ubicua, móvil y redes de sensores, y la pregunta del *streaming* de conciertos). Se agregó como conocimiento general la lista completa de las falacias de la computación distribuida. 5 notas de 69 a 84 líneas; 6 imágenes de apuntes y 2 recortes de slides. Los "[copiar materia]" y el temario quedan en `aceptados`. Cobertura [3]: 112 bloques sin coincidencia textual, revisados a mano: todos los conceptos están reescritos. Sin dudas nuevas.
- **2026-10-20 · Procesos e hilos en Python.** Fuentes: `apuntes_i1` clase 1 completa (nodo, paralelismo y concurrencia, costo de un proceso, IPC, paso de mensajes, coordinación, multiprocessing, subprocess, threads y sus riesgos, locks, panadería, semáforos, eventos, join, deadlock, threads en Python y árbol de threads). Complementos: slides de la clase 1 (ejemplos de cada combinación de procesos y threads, definición de proceso, mecanismos de IPC del sistema operativo, reglas de la panadería, pregunta de procesos frente a threads y el dato de Lamport). Se agregaron como conocimiento general el GIL, la guarda `__main__`, `communicate()`, `start()` frente a `run()`, la inanición y el orden fijo de locks. Todo el código se ejecutó con Python 3.13, incluidos ejemplos nuevos de condición de carrera (1048 en vez de 4000 sin lock), semáforo, evento, join con timeout, deadlock con dos locks y la panadería con tres threads (6000 exacto). 6 notas; 13 imágenes de apuntes. La de join traía las etiquetas equivocadas (`T1.join()` y `T2.join(timeout=N)`), como ya anotaban los apuntes: se reemplazó por el recorte de la slide corregida y se registró como `editada`. 1 duda informativa.
- **2026-10-20 · Comunicación directa y sockets.** Fuentes: `apuntes_i1` clase 3 completa (temario, persistencia y sincronía, acoplamiento temporal y espacial, paradigmas, protocolos de transporte y de aplicación, TCP, UDP, ejemplo del juego de disparos, DNS, HTTP, comunicación directa, socket, servidor y cliente en Python, MPI). Complementos: slides de la clase 3 (ejemplos de cada tipo de comunicación, tabla de paradigmas, diagramas de TCP y UDP, recorrido DNS, las cuatro clases de llamadas MPI, ejemplo con mpi4py y la pregunta de la conferencia por Zoom). Se agregaron como conocimiento general `recv` parcial con `recibir_exacto`, un servidor con un thread por cliente (anticipa la Tarea 1), el ejemplo UDP, `MPI_Barrier` y `MPI_Bcast` explicados y por qué DNS usa UDP. Probado con Python 3.13: servidor y cliente de las slides con dos clientes, servidor con threads (un cliente lento no bloquea a uno rápido), UDP, y mpi4py con `mpiexec -n 2` en un entorno virtual del scratchpad. 6 notas; 3 imágenes de apuntes y 2 recortes de slides (TCP y UDP). 2 dudas informativas.
- **2026-10-20 · Comunicación indirecta.** Fuentes: `apuntes_i1` clase 4 hasta "Invocacion Remota" (temario, frase de la indirección, características, grupos, memoria compartida, colas, publish-subscribe, operaciones, ejemplo de IBM, heterogeneidad, modelos de suscripción y ejemplo de GitHub Discussions). Complementos: slides de la clase 4 (autores de la frase, diagramas de colas y publish-subscribe, WebSphere MQ). Se agregaron como conocimiento general los costos de un intermediario, la diferencia entre repartir trabajo (cola) y difundir (publish-subscribe) y cuándo usar una cola. Ejemplos nuevos probados con Python 3.13: `queue.Queue` con un consumidor que llega tarde y un broker publish-subscribe en memoria con filtros por canal, tópico y contenido. 3 notas; 3 imágenes de apuntes. Sin dudas nuevas.
