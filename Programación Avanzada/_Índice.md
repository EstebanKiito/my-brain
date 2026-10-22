# Programación Avanzada (IIC2233) — mapa del curso

Vault de estudio del ramo. Las notas están escritas para alguien que ya sabe programar lo básico en Python y quiere avanzar: cada concepto empieza por el problema que resuelve, sigue con ejemplos cortos que se pueden copiar y ejecutar, y termina con las trampas más comunes. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` y `prerrequisitos` (notas que conviene leer antes).
- **Cuerpo:** explicación paso a paso, tablas para comparar y código Python 3 con su salida esperada.
- **Imágenes:** figuras del material del curso en PNG, con su transcripción en un callout plegable.
- **Cierre:** cada nota termina con preguntas de repaso con la respuesta oculta.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Programación Avanzada/01-Repaso y POO básica/_Índice\|Repaso y POO básica]] | Tipos, funciones, listas, strings, clases y objetos, encapsulamiento, archivos y anotaciones de tipo |
| [[Programación Avanzada/02-Entorno de trabajo/_Índice\|Entorno de trabajo]] | Guías de estilo, PEP8, modularización, manejo de rutas con os y pathlib, terminal y control de versiones con Git |
| [[Programación Avanzada/03-Estructuras de datos de Python/_Índice\|Estructuras de datos de Python]] | Colecciones secuenciales y no secuenciales, tuplas y namedtuple, stacks y colas con deque, diccionarios y defaultdict, sets y álgebra de conjuntos, y args y kwargs |
| [[Programación Avanzada/04-POO avanzada/_Índice\|POO avanzada]] | Herencia, overriding, super(), polimorfismo, duck typing, sobrecarga de operadores, multiherencia, clases abstractas, decoradores, properties, UML, MRO y metaclases |
| [[Programación Avanzada/05-Excepciones e iterables/_Índice\|Excepciones e iterables]] | Errores en tiempo de ejecución, try/except/else/finally, raise y excepciones personalizadas, protocolo de iteración (__iter__, __next__, StopIteration), generadores con yield, y listas ligadas |
| [[Programación Avanzada/06-Programación funcional/_Índice\|Programación funcional]] | Paradigma declarativo, funciones puras, generadores con send, map/filter/reduce, lambda, zip, enumerate, itertools y pipelines de datos O(1) |
| [[Programación Avanzada/07-Threading/_Índice\|Threading]] | Concurrencia con hilos, procesos vs threads, sincronización con join, hilos daemon, exclusión mutua con Lock, deadlocks, coordinación con Event, colas sincronizadas y el GIL |
| [[Programación Avanzada/08-Interfaces gráficas con PyQt/_Índice\|Interfaces gráficas con PyQt]] | GUI con PyQt, QApplication y event loop, widgets básicos (QLabel, QLineEdit, QPushButton), layouts, signals y slots, eventos de mouse y teclado, arquitectura Front-Back y múltiples ventanas |
| [[Programación Avanzada/09-Serialización y networking I/_Índice\|Serialización y networking I]] | Serialización con JSON, modelo cliente-servidor, IP y puertos, TCP vs UDP, protocolo HTTP, seguridad TLS/HTTPS, cliente con requests, servidor con Flask y concurrencia web |
| [[Programación Avanzada/10-Serialización y networking II/_Índice\|Serialización y networking II]] | Serialización con pickle, manejo de bytes y endianness, sockets TCP de bajo nivel, protocolos de longitud prefijada con chunks, servidores multihilo concurrentes y sockets UDP |
| [[Programación Avanzada/11-PyQt avanzado/_Índice\|PyQt avanzado]] | Concurrencia con QThread, integración de networking con GUI, temporizadores QTimer y singleShot, ventanas QMainWindow (menús, toolbars, status bar) y multimedia con audio |
