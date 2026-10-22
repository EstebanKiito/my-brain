---
ramo: "Introducción a la Programación"
tema: "Listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[01 - Índices, len y recorrer un string]]"
  - "[[03 - Centinela, banderas y break]]"
---

# Qué es una lista

Hasta ahora cada variable guardaba **un** valor. Pero muchos problemas manejan **muchos** valores del mismo tipo: los votos de cada candidato, las notas de un curso, los nombres de los días. Crear una variable por cada uno (`voto1`, `voto2`, …, `voto9`) no escala. La **lista** guarda una secuencia de valores bajo un solo nombre.

## El problema: una votación

Con dos candidatos basta con dos contadores:

```python
voto1 = 0
voto2 = 0
for voto in [1, 2, 1, 1]:      # votos de ejemplo
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
print(voto1, voto2)
```

¿Y con 9 candidatos? Habría que escribir nueve variables, nueve `elif` y nueve `print`. ¿Y si la cantidad de candidatos la decide el usuario? Imposible con variables sueltas.

## La solución: una lista de contadores

```python
votos = [0, 0, 0, 0, 0, 0, 0, 0, 0]   # un contador por candidato
for voto in [3, 9, 3, 1]:
    votos[voto - 1] += 1              # el candidato 1 está en la posición 0
print(votos)
print("Votos emitidos:", sum(votos))
```

```
[1, 0, 2, 0, 0, 0, 0, 0, 1]
Votos emitidos: 4
```

El truco está en `votos[voto - 1] += 1`: el número del voto se usa como **índice** para elegir qué contador aumentar. Una sola línea reemplaza a los nueve `elif`.

## Crear listas y acceder a sus elementos

Una lista se escribe entre corchetes, con elementos separados por comas. Los índices funcionan igual que en los strings: parten en 0 y los negativos cuentan desde el final.

```python
dias_habiles = ["lunes", "martes", "miercoles", "jueves", "viernes"]
fin_semana = ["sabado", "domingo"]
dias = dias_habiles + fin_semana      # + une listas
print(dias[2])        # miercoles
print(dias[-1])       # domingo
print(len(dias))      # 7
```

Formas útiles de crear listas:

| Código | Resultado |
|---|---|
| `[]` | Lista vacía |
| `[0] * 5` | `[0, 0, 0, 0, 0]` |
| `list(range(1, 6))` | `[1, 2, 3, 4, 5]` |
| `[3, "hola", True, 2.5]` | Una lista puede mezclar tipos |

## Las listas sí se pueden modificar

A diferencia de los strings, las listas son **mutables**: se puede cambiar un elemento asignándolo.

```python
dias = ["lunes", "martes", "miercoles"]
dias[0] = "feriado"
print(dias)       # ['feriado', 'martes', 'miercoles']
```

> [!warning] Fuera de rango
> Con 7 elementos los índices válidos van de 0 a 6: `dias[7]` da `IndexError`. Esto vale tanto para leer como para asignar.

## Recorrer una lista

Igual que con strings, por elemento o por índice:

```python
animales = ["buho", "gato", "delfin"]
for animal in animales:              # cuando solo importa el valor
    print(animal)
for i in range(len(animales)):       # cuando importa la posición
    print(f"{i} => {animales[i]}")
```

## Funciones útiles con listas

| Función | Entrega | Ejemplo con `[4, 9, 1]` |
|---|---|---|
| `len(l)` | Cantidad de elementos | `3` |
| `sum(l)` | Suma (solo números) | `14` |
| `min(l)`, `max(l)` | Menor y mayor | `1`, `9` |
| `x in l` | ¿Está `x`? | `9 in l` → `True` |

> [!tip] Idea clave
> Una lista agrupa muchos valores bajo un nombre y los numera desde 0. Cuando un enunciado tiene "un contador por cada…" o "guardar todos los…", casi siempre la respuesta es una lista.

## Preguntas de repaso

> [!question]- ¿Por qué en la votación se escribe `votos[voto - 1]` y no `votos[voto]`?
> Porque los candidatos se numeran desde 1, pero los índices de la lista parten en 0. El candidato 1 se guarda en la posición 0.

> [!question]- ¿Qué diferencia hay entre `dias[0] = "x"` en una lista y `s[0] = "x"` en un string?
> En la lista funciona porque las listas son mutables. En el string da error porque los strings no se pueden modificar.

> [!question]- ¿Cómo se crea una lista con 20 ceros sin escribirlos uno por uno?
> Con `[0] * 20`.
