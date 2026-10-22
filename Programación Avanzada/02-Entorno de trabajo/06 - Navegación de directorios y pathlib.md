---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[05 - Rutas y el módulo os]]"
---

# Navegación de directorios y pathlib

Muchas aplicaciones necesitan procesar carpetas completas, comprobar si un archivo existe antes de abrirlo o recorrer árboles de subcarpetas. Python ofrece dos formas de resolverlo: las funciones del módulo `os` y la interfaz moderna y orientada a objetos que provee `pathlib`. Esta nota revisa ambas alternativas.

## Explorar carpetas con `os.listdir` y `os.walk`

La función `os.listdir(ruta)` retorna una lista con los nombres de todos los archivos y carpetas contenidos directamente en ese directorio:

```python
import os

elementos = os.listdir(".")
print([e for e in elementos if not e.startswith(".")][:4])
```

```
['01 - Guía de estilo: por qué y cómo nombrar.md', '02 - PEP8: imports, espacios y largo de línea.md', '03 - Modularización: qué es y por qué sirve.md', '04 - Formas de importar y la variable __name__.md']
```

> [!warning] `os.listdir` no busca en subcarpetas
> `os.listdir` solo entrega lo que está en el primer nivel del directorio dado. Si una carpeta contiene otra carpeta con archivos, esos archivos interiores no aparecen en la lista.

Para recorrer un directorio de forma recursiva (entrando a todas las subcarpetas), se usa `os.walk`:

```python
import os

for raiz, directorios, archivos in os.walk(".", topdown=True):
    for archivo in archivos:
        if archivo.endswith(".md"):
            ruta_completa = os.path.join(raiz, archivo)
    break  # Solo el primer nivel para este ejemplo
```

Cada iteración de `os.walk` entrega una tupla de tres elementos: la ruta actual (`raiz`), la lista de subcarpetas (`directorios`) y la lista de archivos (`archivos`). El parámetro `topdown=True` indica que primero visita la carpeta madre y luego sus hijas.

## La clase `Path` de `pathlib`

El módulo `pathlib` representa rutas como **objetos**, lo que permite consultar sus propiedades y realizar operaciones directamente sobre ellas sin tener que invocar múltiples funciones sueltas de `os` o `os.path`.

```python
from pathlib import Path

# Creamos un archivo de ejemplo para inspeccionarlo
ruta = Path("datos.txt")
ruta.write_text("primera línea\nsegunda línea", encoding="utf-8")

print("Nombre completo:", ruta.name)
print("Extensión:      ", ruta.suffix)
print("¿Es archivo?:   ", ruta.is_file())
print("¿Es directorio?:", ruta.is_dir())
print("¿Existe?:       ", ruta.exists())
```

```
Nombre completo: datos.txt
Extensión:       .txt
¿Es archivo?:    True
¿Es directorio?: False
¿Existe?:        True
```

### Leer, escribir e iterar con `Path`

Las instancias de `Path` incluyen métodos directos para manipular archivos y recorrer carpetas:

```python
from pathlib import Path

carpeta_actual = Path(".")

# iterdir() entrega objetos Path de los contenidos inmediatos
archivos_txt = [p.name for p in carpeta_actual.iterdir() if p.suffix == ".txt"]
print("¿Encontró archivos .txt?:", len(archivos_txt) > 0)

# Lectura directa de texto sin open() manual
contenido = Path("datos.txt").read_text(encoding="utf-8").splitlines()
print("Primera línea:          ", contenido[0])
```

```
¿Encontró archivos .txt?: True
Primera línea:           primera línea
```

También es posible usar `path.open(mode="r", encoding="utf-8")` dentro de un bloque `with`, integrándose perfectamente con los *context managers*.

## Comparación: `os.path` frente a `pathlib`

| Operación | Con `os` y `os.path` | Con `pathlib.Path` |
|---|---|---|
| Unir rutas | `os.path.join("a", "b.txt")` | `Path("a") / "b.txt"` |
| Nombre y extensión | `os.path.splitext(p)[1]` | `p.suffix` |
| ¿Existe en disco? | `os.path.exists(p)` | `p.exists()` |
| Listar directorio | `os.listdir(p)` | `[x for x in p.iterdir()]` |
| Leer texto completo | `open(p).read()` | `p.read_text()` |

> [!tip] El operador `/` en `pathlib`
> En `pathlib`, el operador de división `/` está sobrecargado para concatenar rutas de forma natural y portable: `Path("datos") / "experimento" / "resultado.csv"`.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia de alcance entre `os.listdir` y `os.walk`?
> `os.listdir` entrega únicamente los elementos inmediatos de una carpeta, mientras que `os.walk` recorre de forma recursiva toda la jerarquía de subdirectorios.

> [!question]- ¿Qué ventaja ofrece `pathlib.Path` frente a usar cadenas de texto comunes para manejar rutas?
> `pathlib` trata la ruta como un objeto con métodos y propiedades claras (`.name`, `.suffix`, `.exists()`, `/`), evitando manipular strings manualmente y asegurando portabilidad.

> [!question]- ¿Cómo se lee el contenido completo de un archivo de texto en una sola línea usando `pathlib`?
> Usando `Path("archivo.txt").read_text(encoding="utf-8")`, que se encarga de abrir, leer y cerrar el archivo automáticamente.
