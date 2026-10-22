---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/tuplas
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructuras de datos y tuplas]]"
---

# Tuplas con nombre: namedtuple

Acceder a los elementos de una tupla mediante índices numéricos como `alumno[3]` o `registro[1]` suele oscurecer el código: obliga a recordar de memoria qué significa cada posición y genera errores silenciosos si el orden de los campos cambia en el futuro.

## Qué es una namedtuple

La función fábrica **`namedtuple`** del módulo `collections` genera una subclase de tupla que permite acceder a cada posición tanto por su índice numérico como por un **nombre de atributo** descriptivo.

Combina la ligereza y eficiencia en memoria de una tupla con la legibilidad y claridad de un objeto con atributos:

```python
from collections import namedtuple

# Definición de la tupla con nombre
Curso = namedtuple("Curso", ["sigla", "secciones", "semestre", "cupos"])

# Creación de una instancia
prog_avanzada = Curso("IIC2233", 5, "2026-2", 520)

# Acceso por nombre de atributo y por índice
print(f"Curso: {prog_avanzada.sigla}")
print(f"Cupos (por atributo): {prog_avanzada.cupos}")
print(f"Cupos (por índice):    {prog_avanzada[3]}")
```

```
Curso: IIC2233
Cupos (por atributo): 520
Cupos (por índice):    520
```

## Formas de declarar campos

El segundo argumento de `namedtuple` acepta tanto una lista de cadenas como una única cadena con los nombres separados por espacios o comas:

```python
from collections import namedtuple

Punto2D = namedtuple("Punto2D", ["x", "y"])
Punto3D = namedtuple("Punto3D", "x y z")
PuntoColor = namedtuple("PuntoColor", "x, y, color")

p1 = Punto3D(10, 20, 30)
print(p1)
```

```
Punto3D(x=10, y=20, z=30)
```

## Inmutabilidad y el método _replace

Al ser tuplas, las instancias de `namedtuple` son **estrictamente inmutables**. Si se intenta modificar un atributo de manera directa, Python levanta una excepción `AttributeError`:

```python
# p1.x = 99  # AttributeError: can't set attribute
```

Para actualizar uno o más campos sin perder la inmutabilidad, `namedtuple` provee el método auxiliar **`_replace(**kwargs)`**. Este método construye y retorna una **nueva instancia** con los valores actualizados, dejando la instancia original intacta:

```python
from collections import namedtuple

Estudiante = namedtuple("Estudiante", ["nombre", "carrera", "semestre"])

alumno1 = Estudiante("Matías", "Computación", 3)
alumno2 = alumno1._replace(semestre=4)

print(f"Original:   {alumno1}")
print(f"Modificado: {alumno2}")
```

```
Original:   Estudiante(nombre='Matías', carrera='Computación', semestre=3)
Modificado: Estudiante(nombre='Matías', carrera='Computación', semestre=4)
```

> [!tip] Desempaquetado idéntico a tuplas
> Las *named tuples* son tuplas en todo sentido: admiten desempaquetado con `a, b, c = punto`, iteración con bucles `for`, particionamiento (*slicing*) y comparación de igualdad tupla a tupla.

> [!warning] El método _replace no muta el objeto original
> Invocar `alumno.replace(semestre=4)` sin guardar el retorno en una variable descarta el cambio por completo. Siempre debe asignarse el resultado a una variable: `alumno = alumno._replace(...)`.

## Cuándo usar namedtuple

| Criterio | Tupla normal | namedtuple | Clase completa |
|---|---|---|---|
| Acceso por nombre | ❌ Solo índice | ✅ Sí (`obj.campo`) | ✅ Sí (`obj.campo`) |
| Inmutabilidad | ✅ Sí | ✅ Sí | ❌ Mutable por defecto |
| Consumo de memoria | Mínimo | Mínimo (sin `__dict__`) | Mayor (posee `__dict__`) |
| Métodos personalizados | ❌ No | ❌ No | ✅ Sí |

`namedtuple` es ideal para agrupar registros de datos inmutables leídos desde archivos CSV, bases de datos o servicios web donde solo se requiere lectura clara sin lógica de negocio compleja.

## Preguntas de repaso

> [!question]- ¿Qué ventaja ofrece `namedtuple` frente a una tupla convencional en proyectos grandes?
> Permite acceder a los datos mediante nombres semánticos legibles (`alumno.nombre`) en lugar de índices mágicos (`alumno[0]`), lo que previene errores al reorganizar campos y mejora la mantenibilidad del código.

> [!question]- ¿Por qué `namedtuple` consume menos memoria que una instancia de una clase normal de Python?
> Porque no crea un diccionario de atributos dinámicos (`__dict__`) en cada instancia; almacena los datos internamente como una tupla compacta de bajo nivel.

> [!question]- ¿Cómo se modifica el valor de un campo en una `namedtuple` si las tuplas son inmutables?
> No se modifica in-situ; se utiliza el método `_replace(**kwargs)`, el cual retorna una nueva tupla con los campos actualizados mientras la instancia previa permanece inalterada.

> [!question]- Si se define `Punto = namedtuple("Punto", ["x", "y"])` y `p = Punto(3, 4)`, ¿es válida la instrucción `x, y = p`?
> Sí, es completamente válida porque `namedtuple` hereda de `tuple`, por lo que conserva todas sus capacidades secuenciales, incluyendo el desempaquetado posicional y la iteración.
