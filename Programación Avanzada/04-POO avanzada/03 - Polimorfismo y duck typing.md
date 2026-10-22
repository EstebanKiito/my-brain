---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/polimorfismo
  - origen/complemento
prerrequisitos:
  - "[[02 - Sobrescritura de métodos y la función super]]"
---

# Polimorfismo y duck typing

Cuando escribimos código que procesa colecciones de elementos heterogéneos —como una lista de figuras que deben dibujarse o un conjunto de servicios de notificación—, no queremos comprobar el tipo exacto de cada objeto con infinitos `if isinstance(...)`. Queremos tratar a todos con la misma interfaz unificada.

## Qué es el polimorfismo

El **polimorfismo** (del griego "muchas formas") es la capacidad de invocar el mismo método o mensaje sobre objetos de clases distintas, obteniendo en cada caso un comportamiento adaptado a la naturaleza particular de ese objeto.

Permite que una función receptora opere sobre cualquier objeto que respete un contrato común, sin importar su clase concreta:

```python
class MaestroAgua:
    def entrenar(self):
        print("Entrenando junto a una cascada congelada.")


class MaestroFuego:
    def entrenar(self):
        print("Entrenando frente a las llamas de un volcán.")


class MaestroAire:
    def entrenar(self):
        print("Meditando en la cima de una montaña ventosa.")


def realizar_entrenamiento(maestros: list):
    for m in maestros:
        m.entrenar()  # Misma llamada, comportamientos distintos


equipo = [MaestroAgua(), MaestroFuego(), MaestroAire()]
realizar_entrenamiento(equipo)
```

```
Entrenando junto a una cascada congelada.
Entrenando frente a las llamas de un volcán.
Meditando en la cima de una montaña ventosa.
```

## Por qué Python no tiene sobrecarga de métodos (overloading)

En lenguajes compilados estáticos como C++ o Java existe la **sobrecarga de métodos** (*method overloading*): definir varios métodos con el mismo nombre pero diferente número o tipo de parámetros.

En Python esto **no existe**. Las funciones y métodos son objetos de primera clase asignados a un identificador en el espacio de nombres. Si defines un método dos veces dentro de una misma clase, la segunda definición **sobrescribe** por completo a la primera:

```python
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def sumar(self, a, b, c):  # Sobrescribe la versión anterior
        return a + b + c


calc = Calculadora()
# calc.sumar(2, 3)  # TypeError: Calculadora.sumar() missing 1 required positional argument: 'c'
print(calc.sumar(1, 2, 3))
```

```
6
```

> [!tip] Cómo emular sobrecarga en Python
> En lugar de duplicar métodos, la flexibilidad en la firma se logra mediante **parámetros con valores por defecto** (`def sumar(self, a, b, c=0):`) o capturando argumentos variables con **`*args`**.

## Duck typing: el estilo dinámico de Python

El tipado dinámico de Python da lugar a una forma de polimorfismo pragmática conocida como **duck typing** (*tipado de pato*), basada en el adagio popular:

> *"Si camina como pato y grazna como pato, entonces es un pato."*

Bajo esta filosofía, no importa si dos clases comparten una superclase común o si declaran explícitamente una interfaz. Lo único relevante es si el objeto **provee el método o atributo que se intenta utilizar** al momento de ejecutar la instrucción:

```python
class Pato:
    def graznar(self):
        print("¡Cuac, cuac!")


class PersonaDisfrazada:
    def graznar(self):
        print("Hago como que grazno: ¡Cuac!")


def hacer_sonar(criatura):
    # No verifica si hereda de Pato; solo invoca el método graznar
    criatura.graznar()


hacer_sonar(Pato())
hacer_sonar(PersonaDisfrazada())
```

```
¡Cuac, cuac!
Hago como que grazno: ¡Cuac!
```

> [!warning] El riesgo del duck typing
> Si se envía un objeto que carece del método requerido (`hacer_sonar(42)`), el error no se detecta al inicio ni al compilar: el programa fallará en plena ejecución con un `AttributeError: 'int' object has no attribute 'graznar'`.

## Preguntas de repaso

> [!question]- ¿Qué ventaja aporta el polimorfismo a la extensibilidad del software?
> Permite agregar nuevas clases con sus propias implementaciones sin tener que modificar ni una sola línea de las funciones existentes que consumen esa interfaz común.

> [!question]- ¿Por qué no es posible definir dos métodos con el mismo nombre y distinta cantidad de argumentos en una clase de Python?
> Porque en Python los nombres de los métodos son entradas en el diccionario de la clase; definir un segundo método con el mismo nombre simplemente reasigna esa clave al nuevo objeto función, perdiendo la definición anterior.

> [!question]- ¿Cuál es la diferencia entre el polimorfismo basado en herencia y el duck typing?
> El polimorfismo por herencia exige que las clases pertenezcan a un mismo árbol jerárquico o compartan una superclase, mientras que el duck typing solo exige que el objeto posea el método solicitado en tiempo de ejecución, sin importar su genealogía.

> [!question]- ¿Cómo se recomienda diseñar un método en Python que deba aceptar tanto 2 como 3 argumentos?
> Asignando un valor por defecto al tercer parámetro (por ejemplo `def calcular(self, a, b, c=None):`) y evaluando dentro del cuerpo si `c` fue provisto por el usuario.
