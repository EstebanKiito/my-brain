---
ramo: "Introducción a la Programación"
tema: "Archivos"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[01 - Leer archivos de texto]]"
---

# Escribir archivos

Leer sirve para usar datos que ya existen. Para **guardar** los resultados de un programa (las traducciones que ingresó el usuario, un reporte, un ranking) hay que **escribir** en un archivo. La diferencia está en el **modo** con que se abre.

## Modos de apertura

| Modo | Nombre | Qué hace | Si el archivo no existe |
|---|---|---|---|
| `"r"` | *read* (leer) | Solo lectura. Es el modo por defecto | Error |
| `"w"` | *write* (escribir) | **Borra todo** el contenido y empieza de cero | Lo crea |
| `"a"` | *append* (agregar) | Escribe **al final**, conservando lo que había | Lo crea |

> [!warning] `"w"` borra el archivo
> Abrir un archivo existente con `"w"` elimina su contenido en ese mismo instante, aunque no se escriba nada. Si la idea es ir sumando datos a lo que ya había, el modo correcto es `"a"`.

## `write` y `print(..., file=)`

```python
salida = open("chao.txt", "w")
salida.write("567\n")
salida.write("890\n")
print("919", file=salida)      # print también puede escribir en un archivo
salida.close()

print(open("chao.txt").read())
```

```
567
890
919
```

- `write(texto)` escribe **exactamente** el texto, **sin** agregar salto de línea: hay que poner `\n` a mano. Además, solo acepta strings (`write(5)` da error; hay que escribir `write(str(5))`).
- `print(..., file=archivo)` funciona como el `print` de siempre (agrega el salto de línea y acepta números), pero escribe en el archivo en vez de la pantalla.

> [!warning] No olvidar `close()`
> Al escribir, Python junta los datos y los manda al disco de a poco. Si el programa termina sin `close()`, parte de lo escrito puede no quedar guardado. Usar `with open(...) as f:` evita el problema porque cierra solo.

## Ejemplo: un traductor que recuerda

El usuario ingresa palabras y su traducción hasta escribir "fin". Cada par se guarda en una línea, separado por un carácter que no aparezca en las palabras (aquí `&`):

```python
pares = [("gato", "cat"), ("pez", "fish"), ("fin", "")]   # simula lo que escribe el usuario

archivo = open("traducciones.txt", "a")
for palabra, traduccion in pares:
    if palabra == "fin":
        break
    print(palabra + "&" + traduccion, file=archivo)
archivo.close()
```

Como se abre con `"a"`, cada vez que se ejecuta el programa las nuevas traducciones se **agregan** a las anteriores. El archivo queda así:

```text
gato&cat
pez&fish
```

Elegir un **separador** es lo que permite después volver a leer el archivo y separar cada línea con `split("&")` (ver la nota siguiente).

## Leer y escribir a la vez: traducir un archivo

Un programa puede abrir varios archivos: dos para leer y uno para escribir. Ejemplo: traducir una lista de palabras usando un diccionario donde cada línea es `palabra-traduccion`.

```python
with open("catalan.txt", "w") as f:
    f.write("cel\ngat\n")
with open("dic.txt", "w") as f:
    f.write("gat-gato\ncel-cielo\n")

palabras = open("catalan.txt").readlines()
diccionario = open("dic.txt").readlines()
salida = open("castellano.txt", "w")
for palabra in palabras:
    for linea in diccionario:
        original, traduccion = linea.strip().split("-")
        if original == palabra.strip():
            print(traduccion, file=salida)
salida.close()
print(open("castellano.txt").read())
```

```
cielo
gato
```

`original, traduccion = …` guarda los dos elementos de la lista que entrega `split` en dos variables a la vez (funciona porque la lista tiene exactamente dos elementos).

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre abrir un archivo con `"w"` y con `"a"`?
> `"w"` borra el contenido y escribe desde cero; `"a"` conserva lo que había y agrega al final. Ambos crean el archivo si no existe.

> [!question]- ¿Por qué después de `f.write("hola")` y `f.write("chao")` el archivo dice `holachao`?
> Porque `write` no agrega saltos de línea. Hay que escribirlos explícitamente: `f.write("hola\n")`.

> [!question]- ¿Para qué sirve elegir un separador como `&` al guardar pares de datos?
> Para poder separarlos de nuevo al leer el archivo, con `split("&")`. El separador no debe aparecer dentro de los datos.
