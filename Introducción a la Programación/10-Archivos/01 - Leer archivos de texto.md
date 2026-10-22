---
ramo: "Introducción a la Programación"
tema: "Archivos"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[02 - Métodos de listas y conversión con strings]]"
---

# Leer archivos de texto

Imagina un programa que funciona como diccionario: el usuario agrega palabras con su significado y después las consulta. Funciona perfecto… hasta que se cierra el programa y **todo se pierde**. Las variables viven en la memoria del computador solo mientras el programa corre. Para que la información sobreviva hay que guardarla en un **archivo**.

## Memoria RAM versus disco

| | Memoria RAM | Disco (duro o de estado sólido) |
|---|---|---|
| ¿Qué guarda? | Las variables del programa en ejecución | Archivos |
| ¿Dura? | No: se borra al terminar el programa (es **volátil**) | Sí: es **permanente** |
| Velocidad | Muy rápida | Más lenta |
| Precio por GB | Caro | Barato |

Un programa lee datos del disco para trabajar con ellos en la RAM, y escribe en el disco lo que quiere conservar.

En este curso se usan **archivos de texto plano** (`.txt`, `.csv`, incluso `.py`): solo contienen texto y se pueden abrir con cualquier editor. Otros archivos (imágenes, Word, Excel) guardan información en formatos especiales.

## Abrir y leer un archivo

Supongamos un archivo `numeros.txt` con este contenido:

```text
123
642
923
```

```python
# (esto solo crea el archivo de ejemplo)
with open("numeros.txt", "w") as f:
    f.write("123\n642\n923\n")

archivo = open("numeros.txt")
lineas = archivo.readlines()
archivo.close()
print(lineas)
print("Cantidad de lineas:", len(lineas))
```

```
['123\n', '642\n', '923\n']
Cantidad de lineas: 3
```

- `open(nombre)` **abre** el archivo y entrega un objeto para trabajar con él.
- `readlines()` lee **todas las líneas** y las entrega como una **lista de strings**.
- `close()` cierra el archivo cuando ya no se necesita.

Desde aquí, todo es trabajar con listas y strings, que ya se conocen.

## El `\n` al final de cada línea

Cada línea termina con el carácter **salto de línea** `\n` (excepto, a veces, la última). Si no se quita, aparece al imprimir o hace fallar comparaciones: `"gato\n" == "gato"` es `False`. Por eso casi siempre se usa `strip()`:

```python
lineas = ["123\n", "642\n", "923\n"]
total = 0
for linea in lineas:
    total += int(linea.strip())
print(total)       # 1688
```

> [!warning] Todo lo que se lee es texto
> Igual que con `input`, lo que viene de un archivo es `str`. Para operar con números hay que convertir con `int` o `float`.

## Ejemplo: una palabra al azar de un diccionario

```python
import random

with open("diccionario.txt", "w") as f:      # archivo de ejemplo
    f.write("gato\nperro\npez\nleon\n")

def palabra_azar():
    archivo = open("diccionario.txt")
    lineas = archivo.readlines()
    archivo.close()
    pos = random.randint(0, len(lineas) - 1)
    return lineas[pos].strip()

print(palabra_azar())
```

## Errores comunes

| Error | Causa |
|---|---|
| `FileNotFoundError: No such file or directory` | El nombre está mal escrito o el archivo **no está en la misma carpeta** que el programa |
| `IsADirectoryError` | Se pasó el nombre de una carpeta, no de un archivo |
| `UnicodeDecodeError` | El archivo usa otra codificación de caracteres (tildes, ñ). Se arregla con `open(nombre, encoding="latin-1")` o `encoding="utf-8"` |

## Leer con `with`

La forma recomendada en Python cierra el archivo automáticamente al salir del bloque, incluso si hay un error:

```text
with open("numeros.txt") as archivo:
    lineas = archivo.readlines()
# aquí el archivo ya está cerrado
```

También se puede recorrer el archivo directamente, línea por línea, sin `readlines`: `for linea in archivo:`.

> [!tip] Idea clave
> Leer un archivo es convertirlo en una **lista de líneas**. Desde ahí se aplica todo lo de listas y strings: `strip` para limpiar, `split` para separar, `int` para convertir.

## Preguntas de repaso

> [!question]- ¿Por qué se pierden los datos de un programa al cerrarlo, y cómo se evita?
> Porque las variables viven en la RAM, que es volátil y se libera al terminar. Se evita guardando la información en un archivo en el disco.

> [!question]- ¿Por qué `"gato\n" == "gato"` es `False` y cómo se arregla?
> Porque la línea leída incluye el salto de línea `\n`. Se arregla con `strip()`, que quita espacios y saltos de línea de los extremos.

> [!question]- ¿Qué significa `FileNotFoundError` si el archivo sí existe en el computador?
> Probablemente no está en la misma carpeta que el programa (o el nombre tiene un error), así que Python no lo encuentra donde lo busca.
