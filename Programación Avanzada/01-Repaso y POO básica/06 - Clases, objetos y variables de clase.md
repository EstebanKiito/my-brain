---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/poo
  - origen/complemento
prerrequisitos:
  - "[[05 - Formato de strings: f-strings y columnas]]"
---

# Clases, objetos y variables de clase

La **programación orientada a objetos** (POO u *OOP*) organiza un programa como un conjunto de **objetos** que se hablan entre sí. Esta nota repasa cómo se define una clase, cómo interactúan los objetos y cómo compartir un dato entre todos los objetos de una clase.

## Objetos, clases e instancias

Un **objeto** es una colección de **datos** que además tiene **comportamientos**. Los datos lo describen y los comportamientos son las acciones que puede hacer. Un objeto se describe de manera general con una **clase**:

- Los datos de la clase se llaman **atributos**.
- Los comportamientos se llaman **métodos**.
- Crear un objeto a partir de una clase se llama **instanciar**, y por eso decimos que un objeto es una **instancia** de su clase.

Una analogía: la clase es el molde de galletas y los objetos son las galletas que salen de él.

## Definir una clase

```python
class Persona:
    def __init__(self, nombre, apellido, edad=25):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Mi nombre es {self.nombre} {self.apellido}'

    def saludar(self, otra_persona):
        print(f'Hola {otra_persona.nombre}, soy {self.nombre} y te saludo.')

persona1 = Persona("Francesca", "Aguirre")
persona2 = Persona("Renato", "Leal")
print(persona2)
persona1.saludar(persona2)
```

```
Mi nombre es Renato Leal
Hola Renato, soy Francesca y te saludo.
```

- `class` define la clase.
- `__init__` es el método que se ejecuta **al crear** cada objeto: ahí se inicializan los atributos. Por eso toda `Persona` nace con nombre, apellido y edad.
- `self` es el primer parámetro de todo método de instancia y es una referencia **al objeto que está ejecutando el método**. En `persona1.saludar(persona2)`, `self` es `persona1`. No es una palabra reservada, pero usar `self` es la convención.
- `__str__` define el texto que se ve al hacer `print` del objeto.

> [!warning] Olvidar `self`
> Si se escribe `nombre = nombre` en vez de `self.nombre = nombre`, el dato queda en una variable local y se pierde al terminar `__init__`.

## Objetos que interactúan

Un objeto puede usar los métodos y atributos de otro. Un huerto guarda plantas y las riega al plantarlas:

```python
class Planta:
    def __init__(self, nombre, resistencia):
        self.nombre = nombre
        self.agua = 0
        self.resistencia = resistencia

    def __str__(self):
        return f'{self.nombre} - {self.agua}/{self.resistencia}'

    def regar(self, cantidad):
        self.agua += cantidad
        if self.agua >= self.resistencia:
            self.agua = self.resistencia

class Huerto:
    def __init__(self):
        self.plantas = []

    def plantar(self, planta):
        if planta not in self.plantas:
            planta.regar(5)
            self.plantas.append(planta)

huerto = Huerto()
zapallo = Planta('Zapallo', 50)
huerto.plantar(zapallo)
print(zapallo)
```

```
Zapallo - 5/50
```

`Huerto` no sabe cómo se riega una planta: solo le pide a `Planta` que se riegue. Cada objeto se ocupa de lo suyo.

## Variables de clase y de instancia

A veces hace falta un valor **compartido por todas las instancias**. Eso es una **variable de clase**: se declara dentro de la clase, fuera de los métodos, y se usa con el nombre de la clase. Una **variable de instancia** (`self.algo`) es propia de cada objeto.

El caso típico es un número único para cada persona (como el RUN), que se asigna desde un contador compartido:

```python
class Persona:
    run = 1                       # variable de clase: la comparten todas

    def __init__(self, nombre):
        self.nombre = nombre
        self.run = Persona.run    # copia el valor actual al objeto
        Persona.run += 1          # avanza el contador compartido

    def presentarse(self):
        print(f'Hola, soy {self.nombre} y mi run es {self.run}')

for n in ['Jaime', 'Pablo', 'Toño']:
    Persona(n).presentarse()
```

```
Hola, soy Jaime y mi run es 1
Hola, soy Pablo y mi run es 2
Hola, soy Toño y mi run es 3
```

El `run` de cada objeto queda propio de ese objeto, y el siguiente número disponible vive en la clase.

## Preguntas de repaso

> [!question]- ¿Qué es `self` y por qué es necesario en los métodos?
> Es una referencia al objeto que ejecuta el método. Sin ella, el método no sabría de cuál objeto leer o modificar los atributos.

> [!question]- ¿Qué diferencia hay entre una clase y una instancia?
> La clase describe cómo son los objetos (atributos y métodos); una instancia es un objeto concreto creado a partir de esa descripción.

> [!question]- En el ejemplo del RUN, ¿por qué `Persona.run += 1` y no `self.run += 1`?
> Porque se quiere avanzar el contador compartido de la clase. `self.run += 1` cambiaría solo el `run` de ese objeto y todas las personas siguientes recibirían el mismo número.
