---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/terminal
  - origen/complemento
prerrequisitos:
  - "[[07 - La terminal: comandos y navegación]]"
---

# Ejecutar Python en terminal y directorio de trabajo

Al programar en un entorno de desarrollo integrado (IDE), muchas veces se ejecuta el código presionando un botón verde. Sin embargo, esto oculta desde qué carpeta exacta se está llamando al intérprete, lo que causa constantes errores de lectura de archivos. Esta nota explica cómo ejecutar Python desde la consola y cómo funciona el **directorio de trabajo actual**.

## La consola interactiva de Python

Al escribir `python3` (o `python`) sin argumentos en la terminal, se inicia la sesión interactiva (*REPL*):

![Consola de Python abierta en la terminal](adjuntos/Consola%20de%20Python%20abierta%20en%20la%20terminal.png)

> [!example]- Transcripción de la imagen
> - Ventana de terminal con el comando `python`.
> - Información de bienvenida: versión de Python (3.10.6), compilador y comandos de ayuda (`help`, `copyright`, `license`).
> - Línea final con el prompt interactivo de tres signos mayor que (`>>> `) esperando instrucciones.

En esta consola se pueden evaluar expresiones al vuelo, probar métodos de objetos y hacer pruebas rápidas. Para salir se usa `exit()` o la combinación `Ctrl + D` (en Linux/macOS) o `Ctrl + Z` luego `Enter` (en Windows).

## Ejecución de un archivo de Python

Para ejecutar un script guardado, se pasa la ruta del archivo como argumento:

```bash
python3 programa.py
```

También es posible ejecutar un script ubicado en otra carpeta:

```bash
python3 modulos/analisis.py
```

Pero aquí surge la principal fuente de confusiones: el **directorio de trabajo**.

## El conflicto clásico: CWD frente a la ubicación del script

Cuando un programa en Python abre un archivo mediante una ruta relativa como `open("datos.txt")`, el intérprete **no busca el archivo donde está guardado el código `.py`**, sino en el **directorio de trabajo actual** (*Current Working Directory* o **CWD**), que es la carpeta donde estaba parada la terminal al escribir el comando.

Imagina la siguiente estructura:

```
proyecto/
├── principal.py
└── auxiliar/
    ├── proceso.py
    └── mensaje.txt
```

Si el archivo `auxiliar/proceso.py` contiene:

```python
with open("mensaje.txt", "r") as f:
    print(f.read())
```

Y lo ejecutas desde la carpeta raíz `proyecto/`:

```bash
pwd
# /home/estudiante/proyecto

python3 auxiliar/proceso.py
# FileNotFoundError: [Errno 2] No such file or directory: 'mensaje.txt'
```

El error ocurre porque Python busca `mensaje.txt` en `/home/estudiante/proyecto/`, donde el archivo no existe.

> [!warning] Dónde estás parado importa
> Una ruta relativa como `"mensaje.txt"` o `"data/archivo.csv"` siempre se evalúa con respecto a la carpeta que devuelve `os.getcwd()`, no con respecto al archivo `.py` que la contiene.

## Soluciones al problema de rutas relativas

Existen dos estrategias habituales:

**1. Moverse antes de ejecutar:**
Hacer `cd` a la carpeta que contiene el archivo antes de correrlo:

```bash
cd auxiliar
python3 proceso.py
```

**2. Construir la ruta a partir de `__file__`:**
La variable especial `__file__` contiene la ubicación real del script en ejecución. Con ella se pueden armar rutas independientes del directorio de la terminal:

```python
import os
from pathlib import Path

# Con os.path
base = os.path.dirname(__file__)
ruta_archivo = os.path.join(base, "mensaje.txt")

# Con pathlib (más conciso)
ruta_pathlib = Path(__file__).parent / "mensaje.txt"
```

## Preguntas de repaso

> [!question]- ¿Qué determina desde dónde se resuelven las rutas relativas al hacer `open("archivo.txt")`?
> El directorio de trabajo actual (*CWD*) desde donde se ejecutó el comando en la terminal, que coincide con el valor de `os.getcwd()`.

> [!question]- ¿Por qué falla un script al ejecutarlo desde una carpeta distinta si usa `open("datos.txt")`?
> Porque Python intenta buscar `datos.txt` en la carpeta donde está situada la terminal, y no en la carpeta donde reside el script.

> [!question]- ¿Cómo garantiza `Path(__file__).parent / "archivo.txt"` que el archivo se encuentre siempre?
> Porque `__file__` indica la ubicación física del propio archivo de código, por lo que su carpeta contenedora (`.parent`) es constante sin importar desde qué directorio se llame al programa.
