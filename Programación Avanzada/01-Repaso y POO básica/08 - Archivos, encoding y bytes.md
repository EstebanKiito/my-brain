---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[04 - Strings: inmutabilidad, escapes y métodos]]"
---

# Archivos, encoding y bytes

Guardar datos en archivos permite que sobrevivan al cierre del programa. Esta nota repasa cómo abrirlos, qué es el *encoding* (por qué a veces aparecen símbolos raros) y cómo trabajar con bytes.

## Abrir, leer y escribir

`open(path, modo)` entrega un objeto que representa al archivo. El **modo** dice qué se puede hacer:

| Modo | Qué hace |
|---|---|
| `'r'` | Lectura (por defecto) |
| `'w'` | Escritura: **crea** el archivo y, si existía, **borra** su contenido |
| `'a'` | *Append*: escribe al final, sin borrar lo anterior |

Para leer: `readline()` entrega una línea, `readlines()` entrega una lista con todas las líneas y `read()` entrega todo el texto. Para escribir: `write(s)` (**no** agrega `\n`) y `print(s, file=archivo)` (**sí** agrega `\n`). Siempre hay que cerrar con `close()`.

```python
archivo = open("ejemplo.txt", "w", encoding="utf-8")
archivo.write("sorry pero ahora yo soy lo que habrá dentro del archivo")
archivo.close()

archivo = open("ejemplo.txt", "a", encoding="utf-8")
archivo.write("\nyo me agregaré al final")
archivo.close()

archivo = open("ejemplo.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()
```

```
sorry pero ahora yo soy lo que habrá dentro del archivo
yo me agregaré al final
```

> [!warning] `'w'` borra lo que había
> Abrir un archivo existente con `'w'` lo deja vacío. Para agregar texto al final hay que usar `'a'`.

## Encoding: de bytes a texto

El sistema operativo no guarda texto: guarda **bytes** (secuencias de números). El **encoding** es la regla que traduce entre bytes y caracteres. Si se escribe con una regla y se lee con otra, el texto sale mal.

```python
contenido = "¿Qué pasa con las tildes?"
with open("enc.txt", "w", encoding="utf-8") as f:
    f.write(contenido)

with open("enc.txt", "r", encoding="ascii", errors="replace") as f:
    print(f.read())        # ascii no entiende las tildes

with open("enc.txt", "r", encoding="utf-8") as f:
    print(f.read())        # mismo encoding con el que se escribió
```

```
��Qu�� pasa con las tildes?
¿Qué pasa con las tildes?
```

El argumento `errors="replace"` indica qué hacer con un byte que no se entiende: en vez de caerse, el programa lo reemplaza por `�`. Por defecto habría un error.

> [!tip] Regla
> Se lee con el **mismo encoding** con el que se escribió. En la práctica, usar `utf-8` en ambos lados evita casi todos los problemas.

## Archivos binarios

Agregando una `b` al modo (`'wb'`, `'rb'`) el archivo trabaja directamente con **bytes**, sin traducción a texto. Los bytes se escriben con una `b` antes de las comillas y se pueden concatenar con `+`. `read(n)` lee exactamente `n` bytes.

```python
with open("bin.dat", "wb") as f:
    f.write(b"abcde12")

with open("bin.dat", "rb") as f:
    print(f.read())
    f.seek(0)
    print(f.read(3))
```

```
b'abcde12'
b'abc'
```

Este modo se usará más adelante, por ejemplo, en la nota de bytes y en las comunicaciones por red.

## Preguntas de repaso

> [!question]- Un archivo escrito con `utf-8` se lee con `ascii` y salen símbolos `�`. ¿Por qué?
> `ascii` no tiene los caracteres con tilde o `¿`, que `utf-8` guarda con más de un byte. Al leer con otra regla, esos bytes no se entienden y se reemplazan.

> [!question]- ¿Qué diferencia hay entre `'w'` y `'a'`?
> `'w'` borra el contenido existente y escribe desde cero; `'a'` conserva el contenido y agrega al final.

> [!question]- ¿Qué muestra `print(f.read())` si el archivo se abrió en modo `'rb'`?
> Muestra un objeto `bytes` (por ejemplo `b'abc'`) en vez de texto, porque en modo binario no hay traducción automática de bytes a caracteres.
