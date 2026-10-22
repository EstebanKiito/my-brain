---
ramo: "Introducción a la Programación"
tema: "Strings"
tags:
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[02 - El ciclo for y range]]"
  - "[[03 - Return versus print y funciones booleanas]]"
---

# Índices, len y recorrer un string

Hasta ahora los textos (`str`) se usaban "enteros": se leían con `input`, se unían con `+` y se mostraban con `print`. Pero muchos problemas necesitan mirar **dentro** del texto: contar cuántas veces aparece una letra, revisar si una palabra es palíndromo, encontrar la palabra más larga. Para eso hay que entender un string como una **secuencia de caracteres numerados**.

## Un string es una fila de caracteres

Cada carácter ocupa una posición, llamada **índice**, que **parte en 0**:

| Carácter | a | b | r | a | c | a | d | a | b | r | a |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Índice negativo | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
s = "abracadabra"
print(s[0])        # a   (primer carácter)
print(s[4])        # c
print(s[-1])       # a   (último carácter)
print(len(s))      # 11  (cantidad de caracteres)
print(s[len(s) - 1])   # a, otra forma de pedir el último
```

- `s[i]` entrega el carácter en la posición `i` (también es un `str`, de largo 1).
- `len(s)` entrega el **largo**: la cantidad de caracteres, contando espacios y signos.
- Los índices negativos cuentan desde el final: `-1` es el último, `-2` el penúltimo.

> [!warning] Fuera de rango
> Como se parte en 0, el último índice válido es `len(s) - 1`. Pedir `s[11]` en `"abracadabra"` produce `IndexError: string index out of range`.

> [!warning] Los strings no se pueden modificar
> `s[1] = "x"` da error: los strings son **inmutables**. Para "cambiar" un carácter hay que construir un string nuevo (ver [[02 - Slicing: rebanar strings|Slicing]]).

## Comillas y operadores

Un string se escribe entre comillas simples, dobles o triples. Tener varias opciones sirve para incluir comillas dentro del texto: `"McDonald's"` o `'Dijo "hola"'`. Las triples (`'''…'''`) permiten texto de varias líneas.

| Operación | Ejemplo | Resultado |
|---|---|---|
| Concatenar `+` | `"ab" + "cd"` | `"abcd"` |
| Repetir `*` | `"ja" * 3` | `"jajaja"` |
| Agregar `+=` | `s = "ho"; s += "la"` | `s` queda `"hola"` |

## Recorrer un string

Hay dos formas de visitar cada carácter:

```python
palabra = "hola"

for letra in palabra:          # 1. por elemento: letra toma "h", "o", "l", "a"
    print(letra, end=" ")
print()

for i in range(len(palabra)):  # 2. por índice: i toma 0, 1, 2, 3
    print(i, palabra[i])
```

```
h o l a
0 h
1 o
2 l
3 a
```

La primera es más simple; la segunda sirve cuando importa **la posición** (por ejemplo, para comparar un carácter con el siguiente o con el del otro extremo).

## Ejemplo: contar apariciones de un carácter

```python
def contar(texto, c):
    contador = 0
    for letra in texto:
        if letra == c:
            contador += 1
    return contador

print(contar("abracadabra", "a"))   # 5
print(contar("abracadabra", "x"))   # 0
```

Es el mismo patrón de contador visto con ciclos, aplicado a las letras.

## Ejemplo: la palabra más larga

Se leen palabras hasta escribir "fin" y se muestra la más larga. Es el patrón del máximo, comparando **largos**:

```python
mayor = ""
palabra = input("palabra? ")
while palabra != "fin":
    if len(palabra) > len(mayor):
        mayor = palabra
    palabra = input("palabra? ")
print("La palabra mas larga es:", mayor)
```

`mayor` parte como el **string vacío** `""` (largo 0), así cualquier palabra real lo supera.

## Ejemplo: ¿es palíndromo?

Un **palíndromo** se lee igual al derecho y al revés ("reconocer", "oso"). Se compara el primer carácter con el último, el segundo con el penúltimo, y así hasta la mitad:

```python
def es_palindromo(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

print(es_palindromo("reconocer"), es_palindromo("casa"))
```

```
True False
```

## Preguntas de repaso

> [!question]- En `s = "python"`, ¿qué entregan `s[0]`, `s[5]`, `s[-2]` y `len(s)`?
> `"p"`, `"n"`, `"o"` y `6`. El último índice válido es 5 porque se parte contando desde 0.

> [!question]- ¿Por qué en el palíndromo basta recorrer hasta `len(s) // 2`?
> Porque cada comparación revisa dos caracteres a la vez (uno de cada extremo). Al llegar a la mitad ya se compararon todos los pares.

> [!question]- ¿Cuándo conviene recorrer con `for i in range(len(s))` en vez de `for letra in s`?
> Cuando se necesita la posición del carácter, por ejemplo para compararlo con el de otra posición o para saber dónde apareció.
