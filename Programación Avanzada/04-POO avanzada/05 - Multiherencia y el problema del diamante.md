---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/herencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Herencia y especialización de clases]]"
  - "[[02 - Sobrescritura de métodos y la función super]]"
---

# Multiherencia y el problema del diamante

En problemas complejos de modelado, ciertas entidades combinan naturalmente características de más de una categoría: un ornitorrinco reúne rasgos de mamífero y de ovíparo, o un asistente de docencia cumple roles simultáneos de estudiante y de trabajador universitario.

## Qué es la multiherencia

La **multiherencia** (*multiple inheritance*) es la capacidad de una subclase de heredar atributos y métodos de **dos o más superclases** simultáneamente.

A diferencia de lenguajes como Java o C# que restringen las clases a herencia simple, Python admite multiherencia directa declarando múltiples clases base separadas por coma en la cabecera:

```python
class Base1:
    pass

class Base2:
    pass

class Subclase(Base1, Base2):
    pass
```

![Jerarquía de multiherencia](adjuntos/Jerarqu%C3%ADa%20de%20multiherencia.jpeg)

> [!example]- Transcripción de la imagen
> - Diagrama de multiherencia.
> - Dos superclases independientes situadas en la parte superior.
> - Una única subclase derivada en la parte inferior conectada mediante flechas de herencia hacia ambas superclases.

## Resolución básica de conflictos por orden de declaración

Si dos superclases definen un método con el mismo nombre, ¿cuál de ellos se ejecuta al invocarlo desde la subclase?

En su forma más simple, Python resuelve la ambigüedad buscando **de izquierda a derecha** según el orden en que las clases base fueron listadas en la definición de la clase:

```python
class MaestroAgua:
    def entrenar(self):
        print("Entrenando técnicas de agua.")


class MaestroFuego:
    def entrenar(self):
        print("Entrenando técnicas de fuego.")


class PersonajeHibrido(MaestroAgua, MaestroFuego):
    pass


avatar = PersonajeHibrido()
avatar.entrenar()  # Se ejecuta MaestroAgua por estar primero a la izquierda
```

```
Entrenando técnicas de agua.
```

## El problema del diamante

El desafío más clásico de la multiherencia ocurre cuando dos superclases intermedias comparten a su vez un ancestro común, formando una estructura con forma de rombo o diamante:

![Problema del diamante en multiherencia](adjuntos/Problema%20del%20diamante%20en%20multiherencia.jpeg)

> [!example]- Transcripción de la imagen
> - Estructura de clases en diamante:
>   - La clase `A` se ubica en la cúspide superior.
>   - Las clases intermedias `B` y `C` heredan directamente de `A`.
>   - La clase `D` en la base hereda conjuntamente de `B` y `C`.

### El peligro de las llamadas manuales a la clase padre

Si las clases intermedias inicializan la superclase llamándola por su nombre explícito (`A.__init__(self)`), la clase raíz termina ejecutándose **dos veces**:

```python
class Dispositivo:
    def __init__(self):
        print("Inicializando Dispositivo (raíz)")


class Telefono(Dispositivo):
    def __init__(self):
        Dispositivo.__init__(self)  # Llamada directa
        print("Inicializando Teléfono")


class Camara(Dispositivo):
    def __init__(self):
        Dispositivo.__init__(self)  # Llamada directa
        print("Inicializando Cámara")


class Smartphone(Telefono, Camara):
    def __init__(self):
        Telefono.__init__(self)
        Camara.__init__(self)
        print("Inicializando Smartphone")


telefono_inteligente = Smartphone()
```

```
Inicializando Dispositivo (raíz)
Inicializando Teléfono
Inicializando Dispositivo (raíz)
Inicializando Cámara
Inicializando Smartphone
```

La inicialización de `Dispositivo` ocurrió dos veces. Si esa clase abriera una conexión a base de datos, descontara un contador o asignara un identificador único, provocaría errores graves de inconsistencia.

> [!warning] La causa del problema del diamante
> El problema del diamante no es un defecto de la herencia múltiple en sí, sino el resultado de utilizar llamadas rígidas y manuales (`ClasePadre.__init__(self)`) que ignoran la jerarquía global del árbol.

> [!tip] La solución definitiva: super() y MRO
> Para evitar ejecuciones duplicadas, Python utiliza la función cooperativa **`super()`** y el algoritmo **MRO** (*Method Resolution Order*), que garantiza que cada clase del diamante se inicialice exactamente una sola vez.

## Preguntas de repaso

> [!question]- ¿Qué regla básica aplica Python cuando dos superclases contienen un método con el mismo nombre y no hay diamante?
> Aplica el orden de búsqueda de izquierda a derecha según el orden en que las superclases fueron listadas entre los paréntesis de la definición de la subclase.

> [!question]- ¿Por qué se le llama "problema del diamante" a esta situación de herencia múltiple?
> Porque el grafo de dependencias forma visualmente un rombo o diamante: una clase raíz en la cúspide se bifurca en dos clases hijas intermedias que luego convergen en una única subclase final.

> [!question]- ¿Qué consecuencia negativa tiene inicializar clases base con `ClaseBase.__init__(self)` en un diamante?
> Provoca que el constructor de la clase raíz común se ejecute múltiples veces sobre la misma instancia, duplicando recursos o reinicializando atributos con valores incorrectos.

> [!question]- ¿Qué ventaja ofrece Python frente a lenguajes como Java en cuanto al soporte de clases base?
> Python permite multiherencia completa de clases concretas, mientras que Java solo admite herencia simple de una clase y exige el uso de interfaces separadas para capacidades múltiples.
