---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/metaclases
  - origen/complemento
prerrequisitos:
  - "[[01 - Herencia y especialización de clases]]"
  - "[[06 - Clases abstractas y el módulo abc]]"
---

# Metaclases: la clase de una clase y el comando type

En Python existe un principio rector: **todo es un objeto**. Un número es una instancia de `int`, una cadena es una instancia de `str`, e incluso una función es una instancia de `function`. Si todo es un objeto, surge una pregunta natural: ¿de qué clase son instancia las propias clases?

## Las clases como objetos y el constructor type

Cuando definimos una clase con la palabra clave `class`, Python no solo genera una plantilla estática: crea un **objeto de tipo clase** en memoria.

La clase que da origen a todas las clases convencionales en Python es **`type`**:

```python
class Usuario:
    pass

u = Usuario()

print(type(u))        # u es una instancia de Usuario
print(type(Usuario))  # Usuario es una instancia de type
print(type(type))     # type es instancia de sí misma
```

```
<class '__main__.Usuario'>
<class 'type'>
<class 'type'>
```

### Creación dinámica de clases con type()

La función `type()` tiene un doble propósito: cuando recibe un solo argumento retorna su tipo; pero cuando recibe **tres argumentos**, crea una nueva clase de forma dinámica en tiempo de ejecución:

`type(nombre_clase, tupla_de_bases, diccionario_de_atributos)`

```python
# Creación dinámica sin usar la palabra clave 'class'
def saludar(self):
    return f"Hola, soy {self.nombre}"

Atributos = {"especie": "Humano", "saludar": saludar}
PersonaDinamica = type("PersonaDinamica", (object,), Atributos)

p = PersonaDinamica()
p.nombre = "Elena"
print(f"Tipo: {type(p).__name__} | Especie: {p.especie}")
print(p.saludar())
```

```
Tipo: PersonaDinamica | Especie: Humano
Hola, soy Elena
```

La sentencia `class MiClase:` no es más que azúcar sintáctico que el intérprete traduce internamente a una llamada a `type()`.

## Qué es una metaclase

Una **metaclase** es la clase de una clase. Así como una clase define cómo se comportan sus instancias (objetos), una metaclase define cómo se construyen y comportan las propias clases.

Para crear una metaclase personalizada, debemos heredar de `type` y sobrescribir su método **`__new__`**:

```python
class MetaValidadora(type):
    def __new__(mcs, name, bases, dct):
        # Valida que toda subclase defina un atributo 'codigo_version'
        if "codigo_version" not in dct and name != "ClaseBase":
            raise TypeError(f"La clase '{name}' debe definir obligatoriamente 'codigo_version'.")
        print(f"[METACLASE] Creando y registrando clase: {name}")
        return super().__new__(mcs, name, bases, dct)


class Servicio(metaclass=MetaValidadora):
    codigo_version = "1.0.0"


# La siguiente definición fallaría al cargarse:
# class ServicioInvalido(metaclass=MetaValidadora):
#     pass  # TypeError: La clase 'ServicioInvalido' debe definir obligatoriamente 'codigo_version'.
```

```
[METACLASE] Creando y registrando clase: Servicio
```

> [!tip] Validación en tiempo de definición
> A diferencia de los métodos abstractos que fallan al instanciar (`c = Circulo()`), las metaclases ejecutan sus validaciones al momento en que Python **lee y define la clase**, detectando inconsistencias arquitectónicas antes de que el programa procese su primera petición.

## Aplicación práctica: el patrón Singleton

Una metaclase puede controlar la instanciación de sus clases asociadas sobrescribiendo el método `__call__`, garantizando que solo exista una única instancia de la clase en todo el programa:

```python
class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]


class ConfiguracionGlobal(metaclass=SingletonMeta):
    def __init__(self):
        self.servidor = "api.produccion.cl"


c1 = ConfiguracionGlobal()
c2 = ConfiguracionGlobal()

print(f"¿Son exactamente el mismo objeto?: {c1 is c2}")
```

```
¿Son exactamente el mismo objeto?: True
```

> [!warning] La regla de Tim Peters sobre metaclases
> *"Las metaclases son magia más profunda de lo que el 99% de los usuarios necesitará jamás. Si te preguntas si necesitas una, probablemente no la necesitas."* Úsalas solo para marcos de trabajo (*frameworks*), librerías de validación o herramientas de serialización avanzada.

## Preguntas de repaso

> [!question]- ¿Qué relación existe entre una instancia, una clase y una metaclase en Python?
> Un objeto común es una instancia de su clase, y esa clase es a su vez una instancia de una metaclase (que por defecto es `type`).

> [!question]- ¿Qué representan los tres parámetros de la función constructora `type(nombre, bases, dict)`?
> `nombre` es la cadena con el nombre de la clase; `bases` es una tupla con las superclases de las que hereda; y `dict` es el diccionario con los atributos y métodos asociados a esa clase.

> [!question]- ¿En qué momento exacto se ejecuta el método `__new__` de una metaclase?
> Se ejecuta en el momento en que el intérprete de Python procesa y crea la definición de la clase, no cuando se crean instancias de la misma.

> [!question]- ¿Cómo logra una metaclase implementar el patrón Singleton?
> Sobrescribiendo el método `__call__` de la metaclase, el cual intercepta el acto de instanciar la clase (`MiClase()`), almacenando la primera instancia creada en un diccionario y retornando esa misma referencia en llamadas posteriores.
