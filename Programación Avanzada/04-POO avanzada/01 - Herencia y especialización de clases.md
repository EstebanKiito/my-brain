---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/herencia
  - origen/complemento
prerrequisitos:
  - "[[06 - Clases, objetos y variables de clase]]"
  - "[[07 - Encapsulamiento y atributos privados]]"
---

# Herencia y especialización de clases

Al modelar sistemas con múltiples entidades relacionadas —como vehículos de transporte, usuarios de un sistema o figuras en una interfaz gráfica—, definir cada clase desde cero provoca duplicación de código innecesaria y dificulta el mantenimiento.

## Relación de especialización y generalización

La **herencia** (*inheritance*) es uno de los pilares de la programación orientada a objetos. Modela una relación de tipo **"es un"** (*is-a*) entre dos clases:

- **Superclase** (o clase base / madre): define el comportamiento y los atributos más generales compartidos por una familia de objetos.
- **Subclase** (o clase derivada / hija): hereda automáticamente todos los atributos y métodos de la superclase y los **especializa**, agregando nuevos datos o funcionalidades exclusivas.

![Jerarquía de herencia simple](adjuntos/Jerarqu%C3%ADa%20de%20herencia%20simple.jpeg)

> [!example]- Transcripción de la imagen
> - Diagrama conceptual de herencia simple.
> - La clase base superior `Persona` posee atributos y métodos comunes.
> - Dos subclases derivadas, `Estudiante` y `Docente`, heredan directamente de `Persona` y añaden comportamientos especializados.

## Sintaxis de herencia en Python

Para indicar que una clase hereda de otra, se coloca el nombre de la superclase entre paréntesis en la definición: `class Subclase(Superclase):`.

```python
class Auto:
    def __init__(self, marca: str, modelo: str, kilometraje: int):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

    def conducir(self, kms: int):
        self.kilometraje += kms
        print(f"Avanzando {kms} km. Kilometraje actual: {self.kilometraje} km")


class FurgonEscolar(Auto):
    def __init__(self, marca: str, modelo: str, kilometraje: int, capacidad: int):
        # Inicializa los atributos compartidos en la clase base
        Auto.__init__(self, marca, modelo, kilometraje)
        self.capacidad = capacidad
        self.estudiantes = []

    def inscribir_estudiante(self, nombre: str):
        if len(self.estudiantes) < self.capacidad:
            self.estudiantes.append(nombre)
            print(f"{nombre} inscrito exitosamente.")
        else:
            print("Capacidad máxima alcanzada.")


furgon = FurgonEscolar("Mercedes", "Sprinter", 50000, 2)
furgon.conducir(15)  # Método heredado de Auto
furgon.inscribir_estudiante("Tomás")
furgon.inscribir_estudiante("Sofía")
```

```
Avanzando 15 km. Kilometraje actual: 50015 km
Tomás inscrito exitosamente.
Sofía inscrito exitosamente.
```

> [!tip] La regla del "es un" frente al "tiene un"
> Aplica herencia solo si la relación lógica es **"es un"** (un Furgón Escolar *es un* Auto). Si la relación es **"tiene un"** (un Auto *tiene un* Motor), la técnica correcta es la **composición**, donde el objeto Auto guarda una instancia de Motor como atributo.

## Especialización de tipos incorporados (built-ins)

En Python las clases estándar integradas en el lenguaje (`list`, `dict`, `set`) son clases convencionales y pueden ser heredadas para crear estructuras especializadas:

```python
class ListaOrdenada(list):
    """Lista que se mantiene ordenada de menor a mayor tras cada inserción."""
    def agregar_ordenado(self, valor):
        self.append(valor)
        self.sort()


mi_lista = ListaOrdenada([10, 5, 20])
mi_lista.agregar_ordenado(7)
print(f"Lista ordenada: {mi_lista}")
print(f"Tamaño (heredado de list): {len(mi_lista)}")
```

```
Lista ordenada: [5, 7, 10, 20]
Tamaño (heredado de list): 4
```

Al heredar de `list`, `ListaOrdenada` conserva automáticamente toda la interfaz nativa de Python: acceso por corchetes, rebanado (*slicing*), iteración con bucles `for` y métodos como `append()` o `pop()`.

## Preguntas de repaso

> [!question]- ¿Qué significa que una subclase especialice a una superclase?
> Significa que la subclase adquiere todas las características generales de la superclase y añade atributos o comportamientos particulares que solo aplican a su dominio específico.

> [!question]- ¿Cuál es la diferencia de diseño entre herencia y composición?
> La herencia modela una relación "es un" y comparte estructura y comportamiento jerárquicamente; la composición modela una relación "tiene un" e incluye referencias a otros objetos independientes dentro de los atributos.

> [!question]- ¿Qué ventaja ofrece heredar de una clase built-in como `list` en lugar de crear una clase contenedora con un atributo interno `self.elementos = []`?
> Permite que los objetos de la nueva clase utilicen de inmediato todos los métodos nativos de listas (`len()`, slicing, `for x in obj:`) sin necesidad de reimplementar manualmente cada uno de esos métodos dunder.

> [!question]- ¿Qué ocurre si una instancia de `FurgonEscolar` invoca un método que no está definido en `FurgonEscolar` pero sí en `Auto`?
> Python busca el método primero en la clase del objeto (`FurgonEscolar`); al no encontrarlo, sube por la jerarquía de herencia y lo ejecuta desde `Auto`.

