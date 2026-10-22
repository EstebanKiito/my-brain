---
ramo: "Introducción a la Programación"
tema: "Strings"
tags:
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[01 - Índices, len y recorrer un string]]"
  - "[[01 - Caso base y caso recursivo]]"
---

# Slicing: rebanar strings

Con `s[i]` se obtiene **un** carácter. Muchas veces se necesita un **pedazo**: las tres primeras letras, todo menos la primera, el texto al revés. Para eso Python tiene el **slicing** (rebanar): `s[i:j]` corta el string como si fuera un pan.

## `s[i:j]`: desde `i` hasta antes de `j`

```python
s = "abracadabra"
print(s[2:6])     # raca  (índices 2, 3, 4 y 5)
print(s[1:3])     # br
print(s[0:11])    # abracadabra (todo)
```

| a | b | **r** | **a** | **c** | **a** | d | a | b | r | a |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | **2** | **3** | **4** | **5** | 6 | 7 | 8 | 9 | 10 |

`s[2:6]` toma los índices 2, 3, 4 y 5: **incluye el inicio y excluye el final**, igual que `range(2, 6)`. Así, el largo del pedazo es `j - i`.

Si se omite un extremo, se toma "desde el comienzo" o "hasta el final":

| Slice | Significa | Con `"abracadabra"` |
|---|---|---|
| `s[:3]` | los 3 primeros | `"abr"` |
| `s[5:]` | desde el índice 5 hasta el final | `"adabra"` |
| `s[1:]` | todo menos el primero | `"bracadabra"` |
| `s[:-1]` | todo menos el último | `"abracadabr"` |
| `s[:]` | una copia completa | `"abracadabra"` |

A diferencia de `s[i]`, un slice **nunca da error** por salirse del rango: `s[5:100]` simplemente entrega hasta el final.

## `s[i:j:k]`: con paso

El tercer número es el **paso**: cada cuántos caracteres tomar uno.

```python
s = "abracadabra"
print(s[1:9:2])   # baaa  (índices 1, 3, 5, 7)
print(s[::5])     # aaa   (índices 0, 5, 10)
print(s[::-1])    # arbadacarba (al revés)
```

Con paso `-1` el string se recorre de atrás hacia adelante: `s[::-1]` es el truco clásico para **invertir** un texto.

## Palíndromo, versión corta

Con slicing, la función de palíndromo queda en una línea:

```python
def es_palindromo(s):
    return s == s[::-1]

print(es_palindromo("oso"), es_palindromo("osa"))
```

```
True False
```

`s == s[::-1]` ya es un `bool`, así que se puede retornar directamente; no hace falta escribir `if … : return True else: return False`. Las tres versiones (comparar extremos, invertir con `if`, retornar la comparación) son correctas; la última es la más clara.

## Palíndromo, versión recursiva

Una palabra es palíndromo si su primera y última letra coinciden **y** lo de en medio también es palíndromo. Caso base: una palabra de 0 o 1 letras siempre lo es.

```python
def es_palindromo_rec(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo_rec(s[1:-1])   # quita la primera y la última

print(es_palindromo_rec("reconocer"))
```

Del mismo modo, el largo de un string sin usar `len`: el vacío mide 0, y cualquier otro mide 1 más que el resto.

```python
def largo(s):
    if s == "":
        return 0
    return 1 + largo(s[1:])

print(largo("abracadabra"))   # 11
```

## Buscar un pedazo dentro de un texto

Para saber en qué posición aparece `"rac"` en `"abracadabra"`, se compara cada pedazo del mismo largo:

```python
def buscar(texto, buscado):
    for i in range(len(texto) - len(buscado) + 1):
        if texto[i:i + len(buscado)] == buscado:
            return i
    return -1      # convención: -1 significa "no está"

print(buscar("abracadabra", "rac"), buscar("abracadabra", "rb"))
```

```
2 -1
```

## "Modificar" un string: armar uno nuevo

Como los strings son inmutables, para cambiar la letra en la posición `pos` se pega lo de antes, la letra nueva y lo de después:

```python
palabra = "gito"
pos = 1
nueva = palabra[:pos] + "a" + palabra[pos + 1:]
print(nueva)    # gato
```

> [!tip] Idea clave
> `s[i:j]` va desde `i` hasta **antes** de `j`. `s[:j]` es el comienzo, `s[i:]` el final, y `s[::-1]` el string al revés. Un slice siempre crea un string **nuevo**; el original no cambia.

## Preguntas de repaso

> [!question]- Con `s = "programar"`, ¿qué entregan `s[3:7]`, `s[:3]` y `s[-3:]`?
> `"gram"`, `"pro"` y `"mar"`.

> [!question]- ¿Por qué `s[100]` da error pero `s[2:100]` no?
> Indexar pide un carácter que debe existir; rebanar pide "lo que haya" en ese rango, así que si el final se pasa, entrega hasta donde llegue el string.

> [!question]- ¿Cómo se cambia la primera letra de `"hola"` por `"c"`?
> Armando un string nuevo: `"c" + "hola"[1:]` da `"cola"`. No se puede hacer `s[0] = "c"` porque los strings son inmutables.
