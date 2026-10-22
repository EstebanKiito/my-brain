# Progreso de la migración — Programación Avanzada (IIC2233)

Rama: `migrar/programacion-avanzada`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Programación Avanzada" --tema "<Tema>"` revisando el código de salida, y se ejecutan con `python3` los bloques de código de las notas. Pausas de revisión: después del tema 1 (piloto), del 7 (Threading) y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Programación Avanzada/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Repaso y POO básica | `01-Repaso y POO básica/` | ✅ hecho | 10 + índice | 2 |
| 2 | Entorno de trabajo | `02-Entorno de trabajo/` | ⏳ pendiente | – | – |
| 3 | Estructuras de datos de Python | `03-Estructuras de datos de Python/` | ⏳ pendiente | – | – |
| 4 | POO avanzada | `04-POO avanzada/` | ⏳ pendiente | – | – |
| 5 | Excepciones e iterables | `05-Excepciones e iterables/` | ⏳ pendiente | – | – |
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

## Registro
- **2026-10-22 · Repaso y POO básica.** Fuentes: los cuatro notebooks de la primera semana (contenidos mínimos, atributos y encapsulamiento, I/O y typing) y las diapositivas de OOP 1 (ejemplo Planta/Huerto). El notebook de contenidos mínimos se dividió en cinco notas (repaso, dos de listas, dos de strings), el de atributos en dos (clases y variables de clase; encapsulamiento) y el de I/O en dos (archivos y bytes; context manager) para respetar el largo máximo. Se omiten los anuncios y las reglas de issues de las slides. Las properties de las slides se tratan en POO avanzada. 10 notas; 2 imágenes de notebook. Sin dudas.
