---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/archivos
  - origen/complemento
prerrequisitos:
  - "[[08 - Archivos, encoding y bytes]]"
---

# Context manager y archivos en memoria

Un archivo siempre debe cerrarse, incluso si ocurre un error. La sentencia `with` lo hace sola gracias a los *context managers*. También se muestra cómo fingir un archivo en memoria.

## `with`: el *context manager*

Un archivo siempre debe cerrarse, incluso si ocurre un error mientras está abierto. Una forma es un `try/finally`:

```python
archivo = open("ejemplo.txt", "r")
try:
    contenido = archivo.read()
finally:
    archivo.close()      # se ejecuta aunque haya un error
```

Pero es mucho código. La sentencia `with` hace lo mismo por debajo:

```python
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
# aquí el archivo ya está cerrado
```

Esto funciona porque el archivo es un ***context manager***: tiene los métodos `__enter__` (prepara el contexto y entrega lo que va en el `as`) y `__exit__` (limpia al salir, aunque haya excepción).

También se puede crear un *context manager* propio con cualquier clase que tenga esos dos métodos:

```python
class Cronometro:
    def __enter__(self):
        print("1. entro")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("3. salgo (aunque haya error)")

with Cronometro() as c:
    print("2. dentro del with")
```

```
1. entro
2. dentro del with
3. salgo (aunque haya error)
```

## Bonus: emular un archivo en memoria

A veces un módulo solo sabe leer o escribir *archivos*, pero los datos están en un string. `StringIO` (texto) y `BytesIO` (bytes) fingen ser un archivo sin tocar el disco.

```python
from io import StringIO, BytesIO

entrada = StringIO("información como texto y más")
salida = BytesIO()

caracter = entrada.read(1)
while caracter:
    salida.write(caracter.encode("ascii", "ignore"))   # ignora lo que ascii no entiende
    caracter = entrada.read(1)

print(salida.getvalue())
```

```
b'informacin como texto y ms'
```

## Preguntas de repaso

> [!question]- ¿Por qué conviene usar `with open(...)` en vez de `open` y `close`?
> Porque cierra el archivo automáticamente aunque ocurra una excepción. Con `close()` manual, un error a mitad de camino deja el archivo abierto.

> [!question]- ¿Qué dos métodos convierten a una clase en *context manager*?
> `__enter__`, que se ejecuta al entrar al `with`, y `__exit__`, que se ejecuta al salir, incluso si hubo una excepción.

> [!question]- ¿Para qué sirve `StringIO` si ya existen los archivos de verdad?
> Para pasarle a código que solo sabe leer o escribir archivos un texto que está en memoria, sin crear un archivo en disco.
