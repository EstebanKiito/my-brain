---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/decoradores
  - programacion/encapsulamiento
  - origen/complemento
prerrequisitos:
  - "[[07 - Encapsulamiento y atributos privados]]"
  - "[[07 - Decoradores: funciones de primera clase y sintaxis arroba]]"
---

# Properties y métodos estáticos: classmethod y staticmethod

En lenguajes como Java es obligatorio escribir métodos *getter* y *setter* explícitos (`getEdad()`, `setEdad(valor)`) para proteger y validar atributos. En Python este enfoque satura el código; en su lugar, se utilizan decoradores nativos que conservan una sintaxis de atributos limpia y natural.

## Properties: getters y setters con @property

El decorador **`@property`** transforma un método en un **atributo calculado** de solo lectura. Permite consultar el método usando sintaxis de atributo directo (`objeto.temperatura`) sin escribir paréntesis:

- **Getter (`@property`):** se ejecuta al leer el atributo.
- **Setter (`@<nombre>.setter`):** se ejecuta al asignar un valor con el operador `=`. Es el lugar idóneo para validar que los datos sean coherentes.
- **Deleter (`@<nombre>.deleter`):** se ejecuta si se borra el atributo con la sentencia `del`.

```python
class Termometro:
    def __init__(self, celsius: float):
        self._celsius = celsius  # Atributo protegido

    @property
    def celsius(self) -> float:
        """Getter: consulta la temperatura."""
        return self._celsius

    @celsius.setter
    def celsius(self, nuevo_valor: float):
        """Setter: valida antes de asignar."""
        if nuevo_valor < -273.15:
            raise ValueError("La temperatura no puede ser inferior al cero absoluto (-273.15 °C).")
        self._celsius = nuevo_valor

    @property
    def fahrenheit(self) -> float:
        """Propiedad calculada en tiempo real."""
        return (self._celsius * 9 / 5) + 32


t = Termometro(25.0)
print(f"Temperatura en Celsius:    {t.celsius} °C")
print(f"Equivalente en Fahrenheit: {t.fahrenheit} °F")

t.celsius = 30.0  # Invoca automáticamente el setter
print(f"Nueva temperatura:         {t.celsius} °C")
```

```
Temperatura en Celsius:    25.0 °C
Equivalente en Fahrenheit: 77.0 °F
Nueva temperatura:         30.0 °C
```

> [!warning] La recursión infinita en setters
> Dentro del setter nunca debes asignar a `self.celsius = nuevo_valor`, pues eso volvería a invocar al setter una y otra vez de forma recursiva hasta agotar la pila con un `RecursionError`. Debes asignar siempre al atributo interno protegido: `self._celsius = nuevo_valor`.

## Métodos de clase (@classmethod) y estáticos (@staticmethod)

Dentro de una clase existen tres categorías de métodos según los datos a los que necesitan acceder:

| Tipo de método | Decorador | Primer argumento | Acceso disponible | Caso de uso principal |
|---|---|---|---|---|
| **De instancia** | *(ninguno)* | `self` | Instancia y clase | Modificar o consultar el estado de un objeto particular |
| **De clase** | `@classmethod` | `cls` | Solo a la clase | Constructores alternativos (*factories*) y atributos de clase |
| **Estático** | `@staticmethod` | *(ninguno)* | Ni objeto ni clase | Funciones utilitarias asociadas lógicamente al tema de la clase |

```python
class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    # Método de clase: constructor alternativo a partir de texto
    @classmethod
    def desde_texto(cls, fecha_str: str):
        dia, mes, anio = map(int, fecha_str.split("-"))
        return cls(dia, mes, anio)

    # Método estático: función auxiliar sin estado
    @staticmethod
    def es_bisiesto(anio: int) -> bool:
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


f1 = Fecha.desde_texto("22-10-2026")
print(f"Fecha creada: {f1.dia}/{f1.mes}/{f1.anio}")
print(f"¿2024 es bisiesto?: {Fecha.es_bisiesto(2024)}")
```

```
Fecha creada: 22/10/2026
¿2024 es bisiesto?: True
```

> [!tip] Constructores alternativos seguros ante herencia
> En `@classmethod`, instanciar con `cls(...)` en lugar del nombre rígido `Fecha(...)` asegura que si una subclase hereda el método, retornará una instancia de la subclase correspondiente y no de la clase madre.

## Preguntas de repaso

> [!question]- ¿Qué ventaja ofrece `@property` frente a métodos convencionales como `get_saldo()` y `set_saldo(monto)`?
> Permite mantener una interfaz pública limpia basada en atributos directos (`cuenta.saldo = 100`) sin perder la capacidad de validar los datos o calcular valores dinámicamente.

> [!question]- ¿Por qué ocurre un `RecursionError` si se escribe `self.edad = valor` dentro de `def edad(self, valor):`?
> Porque la asignación con el operador `=` invoca nuevamente al setter decorado de forma ininterrumpida; se debe asignar siempre a la variable privada o protegida subyacente (por ejemplo `self._edad`).

> [!question]- ¿Cuál es la diferencia entre un `@classmethod` y un `@staticmethod`?
> `@classmethod` recibe como primer parámetro la referencia a la clase misma (`cls`) y puede instanciarla o modificar atributos de clase; `@staticmethod` no recibe ni la instancia (`self`) ni la clase (`cls`), comportándose como una función ordinaria agrupada en la clase.

> [!question]- ¿Por qué se utiliza frecuentemente `@classmethod` para implementar el patrón de diseño Factory Method?
> Porque permite ofrecer métodos alternativos para construir objetos a partir de distintos formatos (cadenas, archivos JSON o diccionarios) retornando siempre una instancia del tipo dinámico `cls`.
