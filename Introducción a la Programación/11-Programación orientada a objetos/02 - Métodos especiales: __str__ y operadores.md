---
ramo: "Introducción a la Programación"
tema: "Programación orientada a objetos"
tags:
  - programacion/poo
  - origen/complemento
prerrequisitos:
  - "[[01 - Clases, objetos, atributos y métodos]]"
---

# Métodos especiales: __str__ y operadores

Al crear un tipo propio, Python todavía no sabe cómo **mostrarlo** con `print` ni cómo **sumarlo** con `+`. Los **métodos especiales** (los que tienen doble guion bajo, como `__init__`) permiten enseñárselo, para que los objetos propios se usen igual de cómodo que los tipos de Python.

## El problema de `print`

```python
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Punto2D(4, 4)
print(p)
```

```
<__main__.Punto2D object at 0x10a3f2d90>
```

Python solo sabe decir "es un objeto `Punto2D` guardado en tal lugar de la memoria". Para mostrar algo útil se define **`__str__`**, que debe **retornar** un string:

```python
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Punto2D(4, 4)
print(p)                   # (4, 4)
print("El punto es " + str(p))
```

`print(p)` y `str(p)` llaman a `__str__` automáticamente.

> [!warning] `__str__` retorna, no imprime
> Dentro de `__str__` va `return`, no `print`. Si se escribe `print(...)` dentro y no se retorna nada, `print(p)` da error porque espera recibir un string.

### `__repr__`: cuando el objeto está dentro de una lista

Al imprimir una **lista** de objetos, Python no usa `__str__` sino otro método, **`__repr__`**. Si no está definido, la lista se ve como `[<__main__.Punto2D object at …>, …]`. Lo más simple es definirlo para que devuelva lo mismo:

```python
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

print([Punto2D(0, 0), Punto2D(1, 2)])     # [(0, 0), (1, 2)]
```

## Ejemplo: un tipo `Fraccion`

Una fracción tiene numerador y denominador. Sumar a/b + c/d = (a·d + b·c) / (b·d):

```python
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def suma(self, otra):
        return Fraccion(self.num * otra.den + self.den * otra.num,
                        self.den * otra.den)

    def mult(self, k):                   # multiplicar por un entero
        return Fraccion(self.num * k, self.den)

f = Fraccion(1, 4)
g = Fraccion(1, 2)
h = f.suma(g)
print(h)              # 6/8
print(h.mult(3))      # 18/8
```

Fíjate que `suma` **retorna un objeto nuevo** (`Fraccion(...)`): no modifica `f` ni `g`, igual que `3 + 4` no cambia al 3 ni al 4.

## Usar `+` con objetos propios: `__add__`

Escribir `f.suma(g)` funciona, pero sería más natural escribir `f + g`. Python traduce cada operador a un método especial: `a + b` se convierte en `a.__add__(b)`. Basta con definirlo:

```python
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, otra):
        return Fraccion(self.num * otra.den + self.den * otra.num,
                        self.den * otra.den)

print(Fraccion(1, 4) + Fraccion(1, 2))     # 6/8
```

| Operador | Método especial |
|---|---|
| `a + b` | `__add__` |
| `a - b` | `__sub__` |
| `a * b` | `__mul__` |
| `a == b` | `__eq__` |
| `a < b` | `__lt__` |
| `str(a)`, `print(a)` | `__str__` |

> [!tip] Idea clave
> Los métodos con doble guion bajo no se llaman directamente: Python los usa por detrás cuando se escribe `print(obj)`, `obj + otro`, etc. Definirlos hace que los tipos propios se comporten como los de Python.

## Preguntas de repaso

> [!question]- ¿Por qué `print(p)` muestra algo como `<__main__.Punto2D object at ...>` si la clase no define `__str__`?
> Porque Python no sabe qué texto representa a ese objeto, así que muestra su tipo y su dirección de memoria. Con `__str__` se le dice qué mostrar.

> [!question]- ¿Por qué el método `suma` retorna una `Fraccion` nueva en vez de cambiar `self`?
> Para que sumar no altere los operandos, igual que con los números. Así `f` y `g` siguen valiendo lo mismo después de calcular `f.suma(g)`.

> [!question]- ¿Qué método hay que definir para poder escribir `a + b` con objetos de una clase propia?
> `__add__(self, otro)`, que debe retornar el resultado de la suma.
