---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/herencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Herencia y especialización de clases]]"
---

# Sobrescritura de métodos y la función super

Cuando una subclase hereda un comportamiento general de su superclase, es frecuente que deba adaptarlo para cumplir con las reglas particulares de su tipo, ya sea reemplazando la lógica por completo o complementándola con pasos adicionales.

## Qué es la sobrescritura de métodos (overriding)

La **sobrescritura de métodos** (*method overriding*) consiste en redefinir en una subclase un método que ya fue declarado en su superclase, conservando el mismo nombre.

Cuando el programa invoca el método sobre una instancia de la subclase, Python ejecuta la versión especializada de la subclase en lugar de la versión de la clase base:

```python
class Vehiculo:
    def acelerar(self):
        print("El vehículo acelera suavemente a 40 km/h.")


class Deportivo(Vehiculo):
    # Sobrescritura total del método acelerar
    def acelerar(self):
        print("¡El deportivo ruge y acelera a 200 km/h en 3 segundos!")


v = Vehiculo()
d = Deportivo()

v.acelerar()
d.acelerar()
```

```
El vehículo acelera suavemente a 40 km/h.
¡El deportivo ruge y acelera a 200 km/h en 3 segundos!
```

## La función integrada super()

A menudo no queremos reemplazar el método original por completo, sino **extenderlo**: queremos que la superclase realice su trabajo fundamental y luego añadir lógica extra.

La función **`super()`** retorna un objeto proxy que delega las llamadas de métodos a la clase superior en la jerarquía de herencia.

### Ventajas de usar super() frente al nombre directo

- **Desacoplamiento:** no fija el nombre de la superclase en el cuerpo del código; si la clase base cambia de nombre, no hay que modificar los métodos hijos.
- **Sintaxis limpia:** no requiere pasar el argumento `self` manualmente (`super().metodo()` en lugar de `ClaseBase.metodo(self)`).
- **Herencia múltiple segura:** en jerarquías con varias clases base, `super()` garantiza que cada método en la cadena se ejecute una sola vez respetando el orden MRO.

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float):
        self.saldo += monto
        print(f"Depósito de ${monto:.2f}. Saldo: ${self.saldo:.2f}")


class CuentaConComision(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, comision: float):
        # 1. Delega la inicialización base a la superclase
        super().__init__(titular, saldo_inicial)
        self.comision = comision

    def depositar(self, monto: float):
        # 2. Extiende el comportamiento descontando comisión
        monto_neto = monto - self.comision
        print(f"Comisión por servicio descontada: ${self.comision:.2f}")
        super().depositar(monto_neto)


cuenta = CuentaConComision("Camila", 1000.0, 50.0)
cuenta.depositar(200.0)
```

```
Comisión por servicio descontada: $50.00
Depósito de $150.00. Saldo: $1150.00
```

> [!warning] Olvidar super().__init__() deja objetos rotos
> Si una subclase define su propio `__init__` pero no invoca `super().__init__(...)`, los atributos de la superclase nunca se crearán. Intentar acceder a ellos posteriormente provocará una excepción `AttributeError`.

> [!tip] super() funciona con cualquier método
> Aunque el caso más común es `__init__`, `super()` puede utilizarse dentro de cualquier método para reutilizar la lógica previa de la clase superior antes o después de la acción propia.

## Preguntas de repaso

> [!question]- ¿Qué ocurre internamente cuando un objeto invoca un método que ha sido sobrescrito en su subclase?
> El despachador dinámico de métodos de Python encuentra primero la definición ubicada en la clase más específica del objeto y la ejecuta, ocultando la implementación de la superclase.

> [!question]- ¿Por qué es una mala práctica invocar `ClasePadre.__init__(self)` de forma directa en lugar de `super().__init__()`?
> Porque acopla el código al nombre rígido del padre inmediato y rompe la cadena cooperativa de resolución de métodos en situaciones de herencia múltiple o reorganización de clases.

> [!question]- ¿En qué se diferencia el overriding (sobrescritura) del enriquecimiento o extensión de un método?
> El overriding puro descarta por completo la lógica del padre e implementa una nueva, mientras que la extensión ejecuta primero o después el método original mediante `super().metodo()` y añade comportamiento complementario.

> [!question]- ¿Por qué no es necesario pasar `self` como argumento al llamar a `super().metodo()`?
> Porque `super()` retorna automáticamente un objeto proxy vinculado a la instancia actual (`self`), inyectándola implícitamente en la llamada al método de la superclase.

