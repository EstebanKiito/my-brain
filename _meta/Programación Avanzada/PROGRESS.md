# Progreso de la migración — Programación Avanzada (IIC2233)

Rama: `migrar/programacion-avanzada`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Programación Avanzada" --tema "<Tema>"` revisando el código de salida, y se ejecutan con `python3` los bloques de código de las notas. Pausas de revisión: después del tema 1 (piloto), del 7 (Threading) y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Programación Avanzada/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Repaso y POO básica | `01-Repaso y POO básica/` | ✅ hecho | 10 + índice | 2 |
| 2 | Entorno de trabajo | `02-Entorno de trabajo/` | ✅ hecho | 11 + índice | 8 |
| 3 | Estructuras de datos de Python | `03-Estructuras de datos de Python/` | ✅ hecho | 10 + índice | 5 |
| 4 | POO avanzada | `04-POO avanzada/` | ✅ hecho | 11 + índice | 10 |
| 5 | Excepciones e iterables | `05-Excepciones e iterables/` | ✅ hecho | 7 + índice | 4 |
| 6 | Programación funcional | `06-Programación funcional/` | ⏳ pendiente | – | – |
| 7 | Threading | `07-Threading/` | ⏳ pendiente | – | – |
| 8 | Interfaces gráficas con PyQt | `08-Interfaces gráficas con PyQt/` | ⏳ pendiente | – | – |
| 9 | Serialización y networking I | `09-Serialización y networking I/` | ⏳ pendiente | – | – |
| 10 | Serialización y networking II | `10-Serialización y networking II/` | ⏳ pendiente | – | – |
| 11 | PyQt avanzado | `11-PyQt avanzado/` | ⏳ pendiente | – | – |
| 12 | Tópicos avanzados | `12-Tópicos avanzados/` | ⏳ pendiente | – | – |
| 13 | Gestión del curso | `13-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md), con detalle medio-alto y lenguaje para estudiantes: cada concepto parte del problema que resuelve, el código es corto, corre con `python3` y va con su salida esperada.
- **El orden de los temas y de las notas sigue el de los notebooks** (`Clases/Contenidos/semana-NN-*/`, por número de notebook, con los `bonus-*` al final de su tema). Los PDF de `Clases/2023/` y el libro solo aportan contenido extra.
- No hay export de Notion ni apuntes propios. Los notebooks, PDF y `.py` no se suben al repo; el código se reescribe dentro de las notas. Las imágenes de los notebooks van como PNG en `adjuntos/` (`tipo: "notebook"`); las figuras de slides, con `tipo: "slide"`.
- Sin comas en los nombres de carpetas ni de notas.
- Otros ramos: se enlaza en vez de duplicar (estructuras lineales y grafos en Estructuras de Datos; hilos y sockets en Sistemas Distribuidos; POO en Ruby y UML en Ingeniería de Software; TLS en Seguridad Computacional; recursión y strings en Introducción a la Programación).

- **Nivel de detalle aprobado y flujo de trabajo:** ver [`NIVEL-DETALLE.md`](NIVEL-DETALLE.md).

## Registro
- **2026-10-22 · Repaso y POO básica.** Fuentes: los cuatro notebooks de la primera semana (contenidos mínimos, atributos y encapsulamiento, I/O y typing) y las diapositivas de OOP 1 (ejemplo Planta/Huerto). El notebook de contenidos mínimos se dividió en cinco notas (repaso, dos de listas, dos de strings), el de atributos en dos (clases y variables de clase; encapsulamiento) y el de I/O en dos (archivos y bytes; context manager) para respetar el largo máximo. Se omiten los anuncios y las reglas de issues de las slides. Las properties de las slides se tratan en POO avanzada. 10 notas; 2 imágenes de notebook. Sin dudas.
- **2026-10-22 · Entorno de trabajo.** Fuentes: los cinco notebooks de la segunda semana (guía de estilo, modularización, paths, terminal y git) y las diapositivas de GitHub y Git. Guía de estilo se dividió en dos notas (por qué y cómo nombrar; PEP8 y reglas de formato); modularización en dos notas (fundamentos y cómo se ejecuta; formas de importar y __name__); paths en dos notas (rutas absolutas/relativas y os.path; navegación y pathlib); terminal en dos notas (comandos básicos y navegación; ejecución en consola y conflicto de CWD); y git en tres notas (conceptos básicos y las cuatro áreas con add/commit/push; commits como versiones completas con la analogía de las muñecas rusas; tokens de acceso personal y problemas frecuentes). 11 notas; 8 imágenes de notebook. Sin dudas.
- **2026-10-22 · Estructuras de datos de Python.** Fuentes: los cinco notebooks de la tercera semana (introducción y tuplas, stacks y colas, diccionarios, sets, y args y kwargs) y las diapositivas de estructuras integradas (tabla comparativa de complejidad). Cada notebook se dividió en dos notas atómicas para respetar el largo máximo (tuplas e inmutabilidad / namedtuple; stacks LIFO / colas FIFO con deque; diccionarios y hashing / defaultdict y conteos; sets y pertenencia / álgebra de conjuntos y relaciones; argumentos posicionales y desempaquetado / parámetros variables con args y kwargs). 10 notas; 5 imágenes de notebook copiadas a adjuntos. Sin dudas.
- **2026-10-22 · POO avanzada.** Fuentes: los seis notebooks principales y dos bonus de la cuarta semana (herencia, polimorfismo, multiherencia, clases abstractas, decoradores, diagramas de clases, metaclases y multiherencia en Python) y las diapositivas de OOP 2 (ejemplos MaestroAgua/MaestroFuego/Todoroki y Planta/calidad). Se cubren herencia simple y extensión de built-ins; sobrescritura y super(); polimorfismo y duck typing; sobrecarga de operadores (__add__, __eq__, etc.) y __str__ vs __repr__; multiherencia y el problema del diamante; clases abstractas con abc (ABC y @abstractmethod); decoradores con wrappers y sintaxis @; properties (@property, setter) y métodos @classmethod/@staticmethod; diagramas de clases UML y relaciones (asociación, agregación, composición y herencia con el modelo de Mario); MRO y linearización C3 con herencia cooperativa; y metaclases con type y patrón Singleton. 11 notas; 10 imágenes registradas. Sin dudas.
- **2026-10-22 · Excepciones e iterables.** Fuentes: los cuatro notebooks principales y un bonus de la sexta semana (intro a excepciones, levantamiento y manejo, iterables y generadores, listas ligadas y excepciones personalizadas) y las diapositivas de excepciones (ejemplos de bytearray y raise). Se cubren excepciones comunes frente a errores de sintaxis; bloques try, except, else y finally; levantamiento con raise, jerarquía de BaseException y excepciones de negocio personalizadas; protocolo de iteración (__iter__, __next__, StopIteration y bucle for); funciones generadoras con yield, evaluación perezosa y expresiones generadoras; listas ligadas con nodos, cabeza e inserción; y dotación del protocolo de iteración a listas ligadas usando yield. 7 notas; 4 imágenes de notebook. Sin dudas.
