---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/herencia
  - programacion/mro
  - origen/complemento
prerrequisitos:
  - "[[05 - Multiherencia y el problema del diamante]]"
  - "[[10 - Parámetros variables: args y kwargs en funciones]]"
---

# MRO y multiherencia cooperativa en Python

En jerarquías complejas con multiherencia y múltiples clases base que comparten ancestros, determinar qué método debe ejecutarse y cómo coordinar los constructores sin duplicar llamadas es un reto que Python resuelve con un algoritmo formal riguroso.

## Qué es el MRO (Method Resolution Order)

El **MRO** (*Method Resolution Order* u Orden de Resolución de Métodos) es la lista lineal ordenada que Python calcula para cada clase, especificando la secuencia exacta en la que se buscarán los atributos y métodos.

Python utiliza el algoritmo de **Linearización C3** (introducido en Python 2.3), el cual garantiza tres propiedades esenciales:

1. **Prioridad de la subclase:** una subclase siempre se consulta antes que cualquiera de sus superclases.
2. **Preservación del orden local:** si se declara `class D(B, C):`, `B` siempre se consultará antes que `C`.
3. **Monotonicidad:** si una clase precede a otra en el MRO de una superclase, ese orden relativo se mantiene en todas las subclases derivadas. Si la jerarquía produce una contradicción lógica, Python detiene la definición de la clase arrojando un error: `TypeError: Cannot create a consistent method resolution order (MRO)`.

## Cómo inspeccionar el MRO

Toda clase posee el atributo especial **`__mro__`** (que devuelve una tupla) y el método **`mro()`** (que devuelve una lista):

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print([cls.__name__ for cls in D.__mro__])
```

```
['D', 'B', 'C', 'A', 'object']
```

![Resolución del diamante con orden MRO](adjuntos/Resoluci%C3%B3n%20del%20diamante%20con%20orden%20MRO.png)

> [!example]- Transcripción de la imagen
> - Grafo en diamante con clases `A`, `B`, `C` y `D`.
> - Flechas numeradas que indican el recorrido de resolución lineal: primero `D`, luego `B`, después `C`, luego `A`, y finalmente `object`.

## La verdadera naturaleza de super(): herencia cooperativa

Un error muy común es pensar que `super()` invoca "a la clase padre en el diagrama".

En realidad, **`super()` invoca a la siguiente clase en el MRO de la instancia concreta (`self`)**.

En la jerarquía anterior, al llamar a `super()` dentro de `B`, ¡no se ejecuta `A`! Se ejecuta **`C`**, porque en el MRO de `D` el elemento que sigue a `B` es `C`. Esto se denomina **herencia cooperativa**:

```python
class A:
    def __init__(self):
        print(" -> A")
        super().__init__()

class B(A):
    def __init__(self):
        print(" -> B")
        super().__init__()

class C(A):
    def __init__(self):
        print(" -> C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("Iniciando D:")
        super().__init__()

instancia = D()
```

```
Iniciando D:
 -> B
 -> C
 -> A
```

Gracias al MRO, la clase raíz `A` se ejecutó **una sola vez**, resolviendo por completo el problema del diamante.

## Manejo de argumentos con *args y **kwargs

Dado que en una cadena cooperativa cada clase intermedia no sabe con certeza cuál será su clase sucesora en tiempo de ejecución, los inicializadores deben aceptar y propagar parámetros arbitrarios:

```python
class Persona:
    def __init__(self, nombre: str, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre

class Deportista(Persona):
    def __init__(self, disciplina: str, **kwargs):
        super().__init__(**kwargs)
        self.disciplina = disciplina

class Estudiante(Persona):
    def __init__(self, carrera: str, **kwargs):
        super().__init__(**kwargs)
        self.carrera = carrera

class BecadoDeportivo(Deportista, Estudiante):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

alumno = BecadoDeportivo(nombre="Diego", disciplina="Natación", carrera="Informática")
print(f"{alumno.nombre}: {alumno.disciplina} | {alumno.carrera}")
```

```
Diego: Natación | Informática
```

> [!tip] object es la última parada
> Todas las clases en Python heredan implícitamente de `object`. `object.__init__()` no acepta ningún argumento por palabra clave, por lo que cada clase debe extraer sus propios parámetros antes de propagar el resto con `super().__init__(**kwargs)`.

## Preguntas de repaso

> [!question]- ¿Qué significa que `super()` actúe según el MRO y no según el padre biológico directo de la clase?
> Significa que el método ejecutado por `super()` se determina dinámicamente según el orden de linearización de la clase de la instancia que originó la llamada, saltando entre ramas hermanas del árbol si el MRO así lo estipula.

> [!question]- ¿Por qué `A` se ejecuta solo una vez al instanciar `D(B, C)` si tanto `B` como `C` heredan de `A`?
> Porque el algoritmo de linearización C3 coloca a la superclase común `A` después de todas sus clases hijas intermedias (`B` y `C`), garantizando que cada nodo del grafo aparezca una sola vez en la lista de resolución.

> [!question]- ¿Qué sucede si dos superclases tienen un ordenamiento contradictorio que hace imposible una linearización válida?
> El intérprete de Python falla al compilar la definición de la clase lanzando una excepción `TypeError: Cannot create a consistent method resolution order (MRO)`.

> [!question]- ¿Por qué es fundamental utilizar `**kwargs` en los constructores de clases diseñadas para multiherencia cooperativa?
> Porque una clase no sabe qué clase aparecerá después de ella en el MRO; al recibir y reenviar `**kwargs`, permite que las clases posteriores reciban los argumentos que les corresponden.
