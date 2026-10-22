---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[01 - Repaso de Python: tipos, funciones y módulos]]"
---

# Listas: creación y comprensión

Una **lista** guarda varios datos en un orden y se puede modificar después de creada. Aquí se repasa cómo crearla, cómo agregarle elementos y cómo construirla de forma compacta con una comprensión.

## Qué es una lista

Una lista es **ordenada** (cada elemento tiene una posición, el **índice**, que parte en 0) y **mutable** (se puede cambiar su contenido y su orden). Puede mezclar tipos, incluso otras listas, aunque en la práctica casi siempre se guardan datos del mismo tipo, igual que un arreglo en otros lenguajes.

```python
lista = list()            # también sirve lista = []
lista.append(2015)        # agrega UN elemento al final
lista.append(2016)
print(lista, len(lista))

lista = [1, 'string', 20.5, [False, True]]
lista.append('último elemento')
print(lista)
print(lista[1])
```

```
[2015, 2016] 2
[1, 'string', 20.5, [False, True], 'último elemento']
string
```

Para agregar muchos elementos hay dos métodos más:

| Método | Qué hace | Ejemplo |
|---|---|---|
| `append(x)` | Agrega `x` al final como **un** elemento | `l.append([1, 2])` agrega una lista adentro |
| `extend(otra)` | Agrega **cada elemento** de `otra` al final | `l.extend([1, 2])` agrega dos elementos |
| `insert(pos, x)` | Inserta `x` en la posición `pos` | `l.insert(2, 'a')` |

```python
bandas = ['Radiohead', 'City and Colour', 'toe']
bandas.extend(['Young the Giant', 'Portugal. The Man'])
bandas.insert(2, 'Of Monsters and Men')
print(bandas)
```

```
['Radiohead', 'City and Colour', 'Of Monsters and Men', 'toe', 'Young the Giant', 'Portugal. The Man']
```

## Listas por comprensión

Es una forma corta de construir una lista nueva a partir de otra. En vez de crear una lista vacía y llenarla en un ciclo, se describe **qué elementos la forman**.

```python
# Con ciclo
largos = []
for nombre in bandas:
    largos.append(len(nombre))

# Por comprensión: lo mismo en una línea
largos = [len(nombre) for nombre in bandas]
print(largos)
```

```
[9, 15, 19, 3, 15, 17]
```

La forma general es `[expresión for elemento in lista]`. Con un `if` al final se filtra: solo entran los elementos que cumplen la condición.

```python
cortas = [nombre for nombre in bandas if len(nombre) < 10]
print(cortas)
```

```
['Radiohead', 'toe']
```

Es equivalente a un `for` con un `if` adentro y un `append`.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `append` y `extend` al agregar `[1, 2]` a una lista?
> `append([1, 2])` agrega **una** sublista como último elemento; `extend([1, 2])` agrega los elementos `1` y `2` por separado.

> [!question]- ¿Cuándo conviene una lista por comprensión en vez de un ciclo?
> Cuando se construye una lista nueva a partir de otra aplicando una expresión o un filtro simple: queda más corta y más clara. Si la lógica es larga, un ciclo normal se entiende mejor.

> [!question]- ¿Qué lista produce `[x * 2 for x in [1, 2, 3, 4] if x % 2 == 0]` y por qué?
> Produce `[4, 8]`: el `if` deja pasar solo los pares (2 y 4) y la expresión los multiplica por 2.
