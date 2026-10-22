---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/diccionarios
  - origen/complemento
prerrequisitos:
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
---

# Diccionarios por defecto: defaultdict y conteos

Al realizar conteos de frecuencia o agrupar registros por categoría, escribir repetidamente comprobaciones del tipo `if llave not in diccionario:` entorpece la lectura del código y añade sobrecarga innecesaria.

## El problema de las llaves no inicializadas

Imaginemos que deseamos contar la frecuencia de cada letra en un texto con un diccionario estándar:

```python
texto = "programacion"
conteo = {}

for letra in texto:
    if letra not in conteo:
        conteo[letra] = 0
    conteo[letra] += 1
```

O al agrupar alumnos por curso:

```python
alumnos_por_curso = {}
# Para cada alumno:
# if curso not in alumnos_por_curso:
#     alumnos_por_curso[curso] = []
# alumnos_por_curso[curso].append(nombre)
```

En ambos casos, acceder a una llave inexistente sin inicializarla previamente provocaría un error fatal `KeyError`.

## Qué es un defaultdict

La clase **`defaultdict`** del módulo `collections` es una subclase de `dict` que soluciona este problema: recibe como argumento una **función fábrica** (*callable*) que genera automáticamente el valor inicial de cualquier llave consultada que no exista aún en el diccionario.

Cuando se consulta `diccionario[clave_nueva]`, `defaultdict` ejecuta el *callable* sin argumentos, guarda el resultado en esa clave y lo retorna inmediatamente.

### Conteo con defaultdict(int)

Al pasar `int` como fábrica, cada clave nueva se inicializa con el valor por defecto que retorna `int()`, que es `0`:

```python
from collections import defaultdict

mensaje = "supercalifragilisticoespialidoso"
vocales = defaultdict(int)

for letra in mensaje:
    if letra in "aeiou":
        vocales[letra] += 1  # Si no existe, se crea en 0 y se suma 1

print(dict(vocales))
```

```
{'u': 1, 'e': 2, 'a': 3, 'i': 6, 'o': 3}
```

### Agrupación con defaultdict(list) y defaultdict(set)

Al pasar `list`, cada clave ausente crea automáticamente una lista vacía `[]`, permitiendo llamar a `.append()` directamente:

```python
from collections import defaultdict

estudiantes = [
    ("Computación", "Ana"),
    ("Industrial", "Pedro"),
    ("Computación", "Sofía"),
    ("Biomédica", "Carlos"),
    ("Industrial", "Elena"),
]

carreras = defaultdict(list)

for carrera, nombre in estudiantes:
    carreras[carrera].append(nombre)

for carrera, alumnos in carreras.items():
    print(f"{carrera}: {alumnos}")
```

```
Computación: ['Ana', 'Sofía']
Industrial: ['Pedro', 'Elena']
Biomédica: ['Carlos']
```

> [!tip] Funciones fábrica personalizadas
> Se puede utilizar cualquier función o expresión `lambda` sin argumentos como fábrica. Por ejemplo, `defaultdict(lambda: "Sin asignar")` inicializará cada nueva consulta con el texto `"Sin asignar"`.

> [!warning] La consulta con corchetes modifica el diccionario
> Consultar una llave inexistente con corchetes `valor = mi_defaultdict["clave_nueva"]` **crea la llave** e incrementa el tamaño del diccionario. Si solo deseas consultar si existe sin alterar el diccionario, utiliza `clave in mi_defaultdict` o el método `.get()`.

## Preguntas de repaso

> [!question]- ¿Qué ocurre internamente cuando se accede a una llave inexistente en un `defaultdict(int)`?
> El diccionario invoca la función fábrica `int()` sin argumentos (que retorna el valor `0`), asigna ese valor a la llave consultada, la almacena en el diccionario y devuelve `0` para que continúe la operación.

> [!question]- ¿Cuál es la principal diferencia entre `dict.get(llave, default)` y `defaultdict`?
> `.get()` devuelve el valor por defecto solo para esa consulta puntual sin modificar el diccionario, mientras que `defaultdict` inserta permanentemente la nueva llave con el valor por defecto en la estructura interna.

> [!question]- ¿Por qué al definir `defaultdict(list)` se pasa `list` sin paréntesis en lugar de `list()`?
> Porque se debe entregar la referencia a la **función o clase** que se invocará en el futuro cada vez que aparezca una llave nueva. Si se pasara `list()`, se estaría entregando una lista vacía ya instanciada en vez del generador de listas.

> [!question]- ¿Cómo se modelaría una estructura de datos para asociar usuarios con un conjunto de etiquetas únicas sin duplicados?
> Mediante `defaultdict(set)`, de modo que cada usuario nuevo tenga un conjunto vacío asociado y se pueda ejecutar directamente `etiquetas[usuario].add(etiqueta)`.
