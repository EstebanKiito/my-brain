---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/clases-abstractas
  - origen/complemento
prerrequisitos:
  - "[[01 - Herencia y especialización de clases]]"
  - "[[03 - Polimorfismo y duck typing]]"
---

# Clases abstractas y el módulo abc

Cuando diseñamos arquitecturas de software medianas o grandes, a menudo requerimos definir contratos estrictos: garantizar que toda clase que represente una base de datos tenga un método `conectar()`, o que toda figura geométrica calcule obligatoriamente su `area()`, evitando que un programador olvide implementarlos.

## Qué es una clase abstracta

Una **clase abstracta** es una clase diseñada exclusivamente para servir como plantilla o modelo base para otras clases:

1. **No se puede instanciar directamente:** representa un concepto genérico (como "Figura Geométrica" o "Animal") del cual no tiene sentido crear objetos aislados.
2. **Define contratos de interfaz:** establece qué métodos deben existir obligatoriamente en todas sus subclases concretas.
3. **Subclases concretas:** son aquellas que implementan la totalidad de los métodos abstractos exigidos, permitiendo finalmente crear instancias reales.

## El módulo abc en Python

En Python, las clases abstractas se implementan utilizando el módulo estándar **`abc`** (*Abstract Base Classes*), empleando dos componentes esenciales:

- **`ABC`:** clase base de la cual debe heredar nuestra clase abstracta.
- **`@abstractmethod`:** decorador que marca aquellos métodos que toda subclase debe implementar de manera obligatoria.

```python
from abc import ABC, abstractmethod


class Figura(ABC):
    """Clase abstracta que define el contrato de las figuras geométricas."""

    @abstractmethod
    def area(self) -> float:
        """Calcula y retorna el área de la figura."""
        pass

    @abstractmethod
    def perimetro(self) -> float:
        """Calcula y retorna el perímetro de la figura."""
        pass


# Intentar instanciar la clase abstracta directamente falla:
# f = Figura()  # TypeError: Can't instantiate abstract class Figura with abstract methods area, perimetro
```

## Implementación en subclases concretas

Para que una subclase pueda instanciarse, debe proveer una implementación real para **todos** los métodos marcados con `@abstractmethod`:

```python
import math
from abc import ABC, abstractmethod


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


c = Circulo(5.0)
r = Rectangulo(4.0, 6.0)

print(f"Área del círculo:     {c.area():.2f}")
print(f"Perímetro rectángulo: {r.perimetro():.2f}")
```

```
Área del círculo:     78.54
Perímetro rectángulo: 20.00
```

> [!warning] La herencia incompleta mantiene la clase abstracta
> Si una subclase solo implementa una parte de los métodos abstractos (por ejemplo, implementa `area` pero olvida `perimetro`), Python considerará que la subclase sigue siendo abstracta y prohibirá su instanciación con el mismo `TypeError`.

> [!tip] Los métodos abstractos pueden tener código base
> Un método abstracto puede contener lógica compartida en su cuerpo (en lugar de solo `pass`). Las subclases que lo sobrescriban pueden invocar esa lógica común mediante `super().metodo_abstracto()`.

## Cuándo usar clases abstractas

- **Para definir APIs y bibliotecas:** cuando construyes un marco de trabajo (*framework*) y necesitas que los desarrolladores completen piezas respetando firmas exactas.
- **Validación temprana:** evita errores silenciosos donde un método faltante solo se descubre cuando el programa ya está en producción al ejecutar una línea específica.

## Preguntas de repaso

> [!question]- ¿Por qué Python lanza un error si intentamos instanciar directamente una clase que hereda de `ABC` y tiene `@abstractmethod`?
> Porque las clases abstractas representan conceptos incompletos cuya finalidad es definir una estructura común; permitir su instanciación causaría fallas cuando se intentaran ejecutar métodos sin implementación.

> [!question]- ¿Qué ocurre si una subclase hereda de una clase abstracta pero no implementa uno de sus métodos abstractos?
> La subclase hereda ese método abstracto sin resolver, por lo que Python la clasifica también como clase abstracta y prohíbe crear instancias de ella.

> [!question]- ¿Cuál es la diferencia entre una clase convencional con métodos que lanzan `NotImplementedError` y una clase abstracta con `ABC`?
> Con `NotImplementedError` el error solo se detecta en tiempo de ejecución al invocar el método faltante; con `ABC` y `@abstractmethod` el error se detecta inmediatamente al intentar crear la instancia del objeto.

> [!question]- ¿Puede una clase abstracta contener métodos normales y atributos concretos no abstractos?
> Sí. Una clase abstracta puede mezclar métodos abstractos con métodos completamente implementados y atributos regulares que son heredados de forma estándar por sus subclases.
