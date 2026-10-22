---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[04 - Formas de importar y la variable __name__]]"
---

# Rutas y el módulo os

Para que un programa pueda leer o guardar datos en el disco, necesita saber exactamente dónde encontrar cada archivo. Un **path** o ruta es la dirección de un archivo o directorio dentro del sistema de archivos. Esta nota explica cómo se organizan las rutas, la diferencia entre rutas absolutas y relativas, y cómo manipularlas de forma portable con `os.path`.

## Jerarquía de archivos y directorios

Los sistemas operativos organizan los archivos de forma jerárquica: carpetas dentro de otras carpetas, y archivos dentro de esas carpetas.

![Jerarquía de carpetas del ejemplo de Pedro](adjuntos/Jerarqu%C3%ADa%20de%20carpetas%20del%20ejemplo%20de%20Pedro.png)

> [!example]- Transcripción de la imagen
> - Directorio raíz `/` en la cúspide.
> - De la raíz se desprenden tres carpetas: `bin`, `Users` y `data`.
> - Dentro de `Users` está la carpeta `Pedro`.
> - Dentro de `Pedro` hay tres subcarpetas: `Fotos` (con `foto1.jpg` y `foto2.jpg`), `Libros` (`calculo.pdf` y `python.pdf`) y `Música` (`audio.mp3`).

## Rutas absolutas frente a relativas

Una ruta puede expresarse de dos maneras:

- **Ruta absoluta:** indica la ubicación desde la **raíz** del sistema de archivos. Siempre empieza con el carácter de directorio raíz (`/` en Linux y macOS, o `C:\` en Windows). No depende de la carpeta en la que estemos trabajando, pero es fija para una máquina específica.
- **Ruta relativa:** indica la dirección tomando como punto de partida un directorio de referencia, normalmente la carpeta donde se está ejecutando el programa. No empieza con `/`.

Siguiendo el esquema anterior para el archivo `python.pdf`:

| Tipo | Ejemplo de ruta | Desde dónde se interpreta |
|---|---|---|
| Absoluta | `"/home/pedro/libros/python.pdf"` | Desde la raíz `/` |
| Relativa | `"home/pedro/libros/python.pdf"` | Desde la raíz `/` |
| Relativa | `"libros/python.pdf"` | Desde `"/home/pedro"` |
| Relativa | `"python.pdf"` | Desde `"/home/pedro/libros"` |

> [!warning] Nunca usar rutas absolutas en tareas o proyectos
> Si escribes `/home/pedro/tarea/datos.txt`, el código fallará en el computador de cualquier otra persona o en el servidor de corrección porque esa ruta no existe allí. En las tareas del curso **solo se deben utilizar rutas relativas**.

## Desarmar una ruta: dirname, basename y extensiones

El módulo `os.path` permite descomponer una ruta en sus partes fundamentales:

- `dirname`: la carpeta contenedora.
- `basename`: el nombre del archivo o directorio final, incluyendo su extensión.
- `splitext`: separa el nombre base de la extensión.

```python
import os

ruta = "/home/pedro/libros/python.pdf"

directorio = os.path.dirname(ruta)
archivo = os.path.basename(ruta)
nombre, extension = os.path.splitext(archivo)

print(f"Directorio: {directorio}")
print(f"Archivo:    {archivo}")
print(f"Nombre:     {nombre}")
print(f"Extensión:  {extension}")
```

```
Directorio: /home/pedro/libros
Archivo:    python.pdf
Nombre:     python
Extensión:  .pdf
```

> [!tip] La extensión no define el tipo de archivo
> La extensión (como `.pdf` o `.txt`) es solo una convención que da una pista al usuario y al sistema operativo. Si guardas texto dentro de un archivo llamado `datos.jpg`, sigue siendo un archivo de texto ordinario, aunque el visor de imágenes intente abrirlo sin éxito.

## Portabilidad de rutas con `os.path.join`

Los sistemas tipo Unix (Linux y macOS) separan directorios usando la barra inclinada (`/`), mientras que Windows utiliza la barra invertida (`\`). Escribir rutas fijas como `"data/gato/juego.txt"` puede provocar errores al ejecutar en Windows.

Para resolver esto, `os.path.join` junta los nombres de carpetas usando el separador nativo del sistema en el que se ejecuta el código:

```python
import os

ruta_portable = os.path.join("data", "gato", "juego_1.txt")
print(ruta_portable)
```

```
data/gato/juego_1.txt
```

En macOS y Linux producirá `data/gato/juego_1.txt`, y en Windows generará `data\gato\juego_1.txt` de manera transparente.

## Preguntas de repaso

> [!question]- ¿Por qué un programa entregado con rutas absolutas como `C:\Users\Juan\tarea\datos.csv` falla al corregirse?
> Porque la ruta absoluta exige que exista exactamente esa misma estructura de carpetas y ese mismo usuario en la máquina que lo ejecuta. Con rutas relativas, el programa encuentra los archivos dentro de la propia carpeta del proyecto.

> [!question]- ¿Qué entrega `os.path.split("/a/b/c.txt")` o la combinación de `dirname` y `basename`?
> Separa la ruta en la carpeta contenedora (`/a/b`) y el nombre del archivo final (`c.txt`).

> [!question]- ¿Qué problema resuelve usar `os.path.join("carpeta", "archivo.txt")` en vez de `"carpeta/archivo.txt"`?
> Resuelve la portabilidad entre sistemas operativos, ya que inserta automáticamente `/` en Linux/macOS y `\` en Windows.
