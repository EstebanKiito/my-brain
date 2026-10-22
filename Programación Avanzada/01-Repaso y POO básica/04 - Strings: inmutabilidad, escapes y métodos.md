---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[03 - Listas: slicing y orden]]"
---

# Strings: inmutabilidad, escapes y métodos

Un **string** es texto. Esta nota repasa por qué no se puede modificar "por dentro", cómo escribir comillas y saltos de línea y qué métodos trae para hacerle preguntas al texto.

## Un string no se puede modificar

Un string es una **secuencia inmutable** de caracteres (en Python 3, caracteres Unicode, es decir, de cualquier idioma). Se puede leer una posición, pero no cambiarla.

```python
cadena = "mi cadena de texto"
print(cadena[0], cadena[-1])   # m o

cadena[0] = "M"                # TypeError: 'str' object does not support item assignment
```

Para "modificarlo" hay que **crear uno nuevo** (por ejemplo, concatenando letra por letra o volviendo a asignar la variable):

```python
cadena = "Mi cadena de texto"
otra = ""
for caracter in cadena:
    otra += caracter
print(otra)
```

```
Mi cadena de texto
```

> [!tip] Regla
> Inmutable significa que el objeto no cambia: lo que cambia es a qué objeto apunta la variable.

## Distintas formas de escribir un string

```python
a = "programando"
b = 'mucho'
c = '''un string
con múltiples
lineas'''
d = """También con
comillas dobles"""
e = ("Tres" " strings" " juntos")        # se pegan solos
f = "un string " + "concatenado"
g = ("Otra forma de string que permite "
     "usar más de una línea de código")  # sigue siendo un solo string
```

Las comillas triples permiten varias líneas. Los paréntesis con varios trozos sirven para no pasarse del largo de línea recomendado.

## Secuencias de escape

El `\` (**carácter de escape**) se combina con otro carácter para darle un significado especial.

| Secuencia | Significado |
|---|---|
| `\"` | Comilla doble |
| `\'` | Comilla simple |
| `\n` | Salto de línea |
| `\t` | Tabulador |
| `\\` | Barra inversa (*backslash*) |

```python
print("hola quiero escribir comillas dobles \" y seguir escribiendo")
```

```
hola quiero escribir comillas dobles " y seguir escribiendo
```

## Métodos útiles

`dir(str)` muestra la lista completa de métodos. Algunos responden preguntas sobre el string:

| Método | Pregunta que responde |
|---|---|
| `isalpha()` | ¿Solo tiene letras de algún idioma? |
| `isdigit()` | ¿Solo tiene dígitos? |
| `startswith(s)` / `endswith(s)` | ¿Empieza / termina con `s`? |
| `find(s)` | ¿En qué posición aparece `s`? (`-1` si no está) |
| `index(s)` | Igual que `find`, pero falla si no está |

```python
print("abñ".isalpha())          # True
print("t/".isalpha())           # False
print("34".isdigit())           # True
s = "estoy programando"
print(s.startswith("est"))      # True
print(s.endswith("do"))         # True
print(s.find("y p"))            # 4
```

```
True
False
True
True
True
4
```

## Preguntas de repaso

> [!question]- ¿Por qué `cadena[0] = "M"` da error pero `cadena = "M" + cadena[1:]` funciona?
> Los strings son inmutables, así que no se puede cambiar una posición. La segunda forma crea un string **nuevo** y hace que la variable apunte a él.

> [!question]- ¿Qué diferencia hay entre `find` e `index` cuando el texto no está?
> `find` devuelve `-1`; `index` lanza un `ValueError`.

> [!question]- ¿Cómo se escribe un string que contenga una comilla doble y un salto de línea?
> Con secuencias de escape: `"dijo \"hola\"\nchao"`. El `\"` es la comilla y el `\n` el salto de línea.
