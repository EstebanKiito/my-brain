---
ramo: "Introducción a la Programación"
tema: "Primeros pasos en Python"
tags:
  - programacion/python
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un algoritmo]]"
  - "[[02 - Conceptos de programación con Blockly]]"
---

# Python, IDLE y el primer programa

Un algoritmo escrito en español no lo puede ejecutar un computador; hay que traducirlo a un lenguaje de programación. El curso usa **Python**, un lenguaje pensado para que el código se lea casi como texto normal. Esta nota muestra cómo se escribe y ejecuta un programa, y la primera instrucción: `print`.

## Por qué Python

Python es un lenguaje de **uso general** (sirve para ciencia de datos, web, juegos, automatizar tareas…) y de **alto nivel**: se escribe con palabras parecidas al inglés y no obliga a pensar en detalles de la máquina, como la memoria. Su filosofía privilegia la **legibilidad**: expresar una idea en pocas líneas claras. Hay que instalar la versión 3 o superior desde python.org.

Un programa en Python es una **lista de instrucciones ordenadas** que el computador sigue de arriba hacia abajo, igual que los bloques apilados de Blockly. El trabajo de quien programa es que esas instrucciones existan y sean correctas.

## Dónde se escribe: IDLE y otros editores

Para programar se usa un **entorno de desarrollo** (IDE). Python trae uno simple, **IDLE**, con dos modos:

| Modo | Para qué sirve |
|---|---|
| **Shell** (ventana interactiva, con `>>>`) | Probar una instrucción y ver el resultado al tiro |
| **Archivo** (`.py`) | Escribir un programa completo, guardarlo y ejecutarlo (F5) |

Python es un lenguaje **interpretado**: lee y ejecuta las instrucciones una por una, sin un paso previo de traducción de todo el programa. Por eso existe el modo interactivo, útil para experimentar. Otros editores populares son PyCharm, Spyder, Jupyter o editores en línea como Replit; todos ejecutan el mismo Python.

## El primer programa: `print`

```python
# Mi primer programa
print("hola mundo")
print("este es mi primer programa")
print("fin")  # escribe fin
```

Salida:
```
hola mundo
este es mi primer programa
fin
```

- `print(...)` **muestra en pantalla** lo que va entre paréntesis. Lo que va dentro se llama **argumento** o parámetro.
- El texto va entre comillas (`"…"` o `'…'`, ambas sirven). Al texto entre comillas se le llama **string**.
- Todo lo que viene después de `#` hasta el final de la línea es un **comentario**: Python lo ignora. Sirve para dejar notas a quien lea el código (incluido tu yo del futuro).

> [!tip] Sintaxis y semántica
> La **sintaxis** es *cómo se escribe* una instrucción (`print("…")`, con paréntesis y comillas). La **semántica** es *qué hace* (escribe su argumento en la pantalla). Un error de sintaxis impide que el programa corra; un error de semántica hace que corra pero haga otra cosa.

> [!warning] Comillas rectas
> Python solo acepta comillas rectas (`"` y `'`). Si se copia código desde un PowerPoint o Word, a veces aparecen comillas curvas (`“ ”`) y el programa falla con un error de sintaxis. Lo mismo pasa con `Print` en mayúscula: Python distingue mayúsculas de minúsculas.

## Errores frecuentes al empezar

| Código | Problema |
|---|---|
| `print("hola)` | Falta cerrar las comillas |
| `print "hola"` | Faltan los paréntesis (era la forma de Python 2) |
| `Print("hola")` | `Print` no existe; es `print` |
| `print(hola)` | Sin comillas, Python busca una *variable* llamada `hola` |

Cuando algo falla, Python muestra un mensaje de error indicando la línea. Leerlo con calma (en vez de borrarlo) es la forma más rápida de encontrar el problema.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre usar la shell de IDLE y escribir un archivo `.py`?
> En la shell cada instrucción se ejecuta apenas se presiona Enter y no queda guardada; sirve para probar. En un archivo se escribe el programa completo, se guarda y se ejecuta entero las veces que se quiera.

> [!question]- ¿Por qué `print(hola)` da error pero `print("hola")` no?
> Con comillas, `"hola"` es un texto literal. Sin comillas, Python interpreta `hola` como el nombre de una variable, y como no existe ninguna con ese nombre, avisa un error.

> [!question]- ¿Para qué sirve un comentario si Python lo ignora?
> Para las personas: explica qué hace o por qué se escribió así una parte del código, y facilita entenderlo o corregirlo después.
