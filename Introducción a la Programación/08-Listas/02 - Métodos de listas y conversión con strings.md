---
ramo: "Introducción a la Programación"
tema: "Listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es una lista]]"
  - "[[03 - Métodos de strings]]"
---

# Métodos de listas y conversión con strings

Una lista no tiene por qué tener un tamaño fijo: puede **crecer** a medida que llegan datos y **achicarse** al quitar elementos. Esta nota reúne los métodos para hacerlo, los slices de listas y cómo pasar de un string a una lista y de vuelta, algo que se usa todo el tiempo para procesar frases y archivos.

## Agregar y quitar elementos

| Método | Qué hace | Ejemplo con `l = [10, 20, 30]` | `l` queda |
|---|---|---|---|
| `l.append(x)` | Agrega `x` al final | `l.append(40)` | `[10, 20, 30, 40]` |
| `l.insert(i, x)` | Agrega `x` en la posición `i` | `l.insert(1, 15)` | `[10, 15, 20, 30]` |
| `l.remove(x)` | Quita la **primera** aparición del valor `x` | `l.remove(20)` | `[10, 30]` |
| `l.pop(i)` | Quita el elemento de la **posición** `i` y lo entrega | `l.pop(0)` → `10` | `[20, 30]` |
| `l.pop()` | Quita y entrega el último | `l.pop()` → `30` | `[10, 20]` |
| `l.count(x)` | Cuántas veces está `x` (no modifica) | `l.count(20)` → `1` | igual |
| `l.index(x)` | Posición de la primera aparición de `x` | `l.index(30)` → `2` | igual |

> [!warning] `remove` quita por valor, `pop` por posición
> `l.remove(0)` busca el **valor** 0 (y da error si no está); `l.pop(0)` quita lo que haya en la **posición** 0. Confundirlos es un error frecuente.

A diferencia de los métodos de strings, estos **modifican la lista** directamente; no hace falta escribir `l = l.append(x)` (de hecho, eso dejaría `l` en `None`).

## Votación sin saber cuántos candidatos hay

En vez de un contador por candidato, se guardan **todos** los votos y al final se cuentan con `count`:

```python
votos = []
for voto in [1, 3, 1, 2, 1]:      # en el programa real vendrían de input
    votos.append(voto)
print("Votos emitidos:", len(votos))
for candidato in range(1, 4):
    print(f"#{candidato}: {votos.count(candidato)}")
```

```
Votos emitidos: 5
#1: 3
#2: 1
#3: 1
```

## Slices de listas

Los slices funcionan igual que en los strings y entregan una lista nueva:

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[1:3])     # [1, 2]
print(l[:5])      # [0, 1, 2, 3, 4]
print(l[::-1])    # la lista al revés
l[3:5] = ["a", "b"]   # en listas, un slice también se puede reemplazar
print(l)          # [0, 1, 2, 'a', 'b', 5, 6, 7, 8, 9]
```

## Del string a la lista y de vuelta

| Herramienta | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `s.split()` | Corta el string en los espacios | `"pata de cabra".split()` | `["pata", "de", "cabra"]` |
| `s.split(d)` | Corta donde aparece el separador `d` | `"10/06/2023".split("/")` | `["10", "06", "2023"]` |
| `list(s)` | Una lista con cada carácter | `list("hola")` | `["h", "o", "l", "a"]` |
| `d.join(l)` | Une una lista de strings poniendo `d` entre ellos | `"-".join(["a", "b", "c"])` | `"a-b-c"` |

```python
frase = "Como estas hoy"
for palabra in frase.split():
    print(palabra)
print(" ".join(["Como", "estas", "hoy"]).upper())
```

```
Como
estas
hoy
COMO ESTAS HOY
```

> [!warning] `split` entrega strings
> `"4 5 6".split()` da `["4", "5", "6"]`: textos, no números. Para sumarlos hay que convertir cada uno con `int`.

## Una función puede retornar una lista

Una función que filtra: entrega las palabras que empiezan con cierta letra.

```python
def empiezan_con(lista, letra):
    resultado = []
    for palabra in lista:
        if palabra[0] == letra:
            resultado.append(palabra)
    return resultado

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print(empiezan_con(dias, "m"))
```

```
['martes', 'miercoles']
```

Este es el patrón **filtrar**: partir con una lista vacía y hacer `append` solo de los elementos que cumplen la condición.

Para ver todos los métodos de listas, `help(list)` en la consola de Python.

## Preguntas de repaso

> [!question]- ¿Qué queda en `l` después de `l = [5, 7, 5]` y `l.remove(5)`?
> `[7, 5]`. `remove` quita solo la primera aparición del valor.

> [!question]- ¿Por qué `l = l.append(3)` es un error?
> Porque `append` modifica la lista y no retorna nada (retorna `None`). Al asignarlo, `l` pasa a ser `None` y se pierde la lista.

> [!question]- ¿Cómo se suman los números del string `"3 4 5"`?
> Separándolo con `split()` y convirtiendo cada parte: `sum` de los `int(x)` de cada `x` en `"3 4 5".split()`, que da 12.
