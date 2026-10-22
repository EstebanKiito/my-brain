# Progreso de la migración — Introducción a la Programación (IIC1103)

Rama: `migrar/introduccion-programacion`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Introducción a la Programación" --tema "<Tema>"` revisando el código de salida, y se ejecutan con `python3` los bloques de código de las notas. Pausas de revisión: después del tema 2 (piloto), del 7 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Introducción a la Programación/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Algoritmos y pensamiento computacional | `01-Algoritmos y pensamiento computacional/` | ✅ hecho | 2 + índice | 2 |
| 2 | Primeros pasos en Python | `02-Primeros pasos en Python/` | ✅ hecho | 4 + índice | 0 |
| 3 | Condicionales | `03-Condicionales/` | ✅ hecho | 3 + índice | 0 |
| 4 | Ciclos | `04-Ciclos/` | ✅ hecho | 4 + índice | 0 |
| 5 | Funciones y módulos | `05-Funciones y módulos/` | ⏳ pendiente | – | – |
| 6 | Recursión | `06-Recursión/` | ⏳ pendiente | – | – |
| 7 | Strings | `07-Strings/` | ⏳ pendiente | – | – |
| 8 | Listas | `08-Listas/` | ⏳ pendiente | – | – |
| 9 | Listas de listas | `09-Listas de listas/` | ⏳ pendiente | – | – |
| 10 | Archivos | `10-Archivos/` | ⏳ pendiente | – | – |
| 11 | Programación orientada a objetos | `11-Programación orientada a objetos/` | ⏳ pendiente | – | – |
| 12 | Ordenamiento | `12-Ordenamiento/` | ⏳ pendiente | – | – |
| 13 | Gestión del curso | `13-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md), con detalle medio-alto y lenguaje para primer año: cada concepto parte de un problema cotidiano, el código es corto, corre con `python3` y va con su salida esperada.
- No hay export de Notion ni apuntes propios. Fuentes: PDF de clase (`CLASES/I1`, `I2`, `Examen`), códigos de la profesora (`Codigos/claseNN/`, con una numeración de clases distinta a la de los PDF: se asignan por contenido) y `pythonbook.pdf` como apoyo.
- Los códigos se reescriben dentro de las notas; los `.py` y PDF no se suben al repo. Solo las figuras útiles de las slides van como PNG en `adjuntos/`, registradas con `tipo: "clase"`.
- Otros ramos: se enlaza en vez de duplicar (recursión y ordenamiento avanzado en Estructuras de Datos; POO en Ingeniería de Software; C en Programación en C).

## Registro
- **2026-10-22 · Algoritmos y pensamiento computacional.** Fuentes: slides de la bienvenida (objetivos y etapas de resolución de problemas) y de Blockly (receta de pizza, definición de algoritmo, formas de comunicarlo, Turtle y Maze). Se omitieron presentaciones del equipo, encuestas y la actividad de participación; las reglas y la evaluación quedan para Gestión del curso. 2 notas; 2 figuras de clase. Sin dudas.
- **2026-10-22 · Primeros pasos en Python.** Fuentes: slides de introducción a Python y de variables/operadores/bool, más los códigos `holamundo`, `dimetunombre`, `jalisco`, `millas a kms`, `chocolates repartir` y `dados`. Se agregaron la tabla de errores frecuentes y el ejemplo de prioridad con Fahrenheit (ejercicio propuesto). 4 notas; sin imágenes (las slides son texto). Sin dudas.
- **2026-10-22 · Condicionales.** Fuentes: slides de if/else y elif, y los códigos `lanzar dado`, `cachipun`, `chocolates` y las seis versiones de `monitoreo`. Se corrigió sin comentar una errata en la condición de alerta (un umbral 300 donde iba 200). El `main.py` de plantilla de PyCharm se omite (el patrón `__name__` se ve con módulos). 3 notas; 0 imágenes.
- **2026-10-22 · Ciclos.** Fuentes: slides de while/for y de while 2 (mejor nota, RUT), y los códigos de cuadrados, notas (cuatro versiones), `que pasa`, `pig`, `rut` y `carrera1`-`carrera2`. El `pig` se resume en prosa; `dccamaradas` depende de un módulo externo y se deja para Funciones. 4 notas; 0 imágenes.
