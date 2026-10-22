---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[04 - Strings: inmutabilidad, escapes y métodos]]"
---

# Formato de strings: f-strings y columnas

Armar mensajes con variables y alinear datos en columnas es algo que se hace todo el tiempo. Esta nota muestra los *f-strings*, `str.format()` y la especificación de formato.

## Variables dentro de un string

Un ***f-string*** lleva una `f` antes de las comillas y deja escribir variables entre llaves:

```python
nombre = "Ana"
edad = 20
print(f"Hola, soy {nombre} y tengo {edad} años")
```

```
Hola, soy Ana y tengo 20 años
```

Con `str.format()` se arma una **plantilla** que se reutiliza con distintos valores, por posición (`{}`) o por nombre (`{saludado}`):

```python
saludar = "Hola {}, te damos la bienvenida!"
print(saludar.format("a@ejemplo.com"))

entre = "Hola {saludado}, te saluda el usuario {saludador}"
print(entre.format(saludado="b@ejemplo.com", saludador="a@ejemplo.com"))
```

```
Hola a@ejemplo.com, te damos la bienvenida!
Hola b@ejemplo.com, te saluda el usuario a@ejemplo.com
```

## Alinear columnas

Para imprimir tablas, después de los dos puntos se escribe una **especificación de formato**. El orden es siempre: **relleno, alineación, tamaño, tipo**.

```python
compra = [('leche', 2, 120), ('pan', 3.5, 800), ('arroz', 1.75, 960)]
print("PRODUCTO | CANTIDAD | PRECIO | SUBTOTAL")
for producto, cantidad, precio in compra:
    subtotal = cantidad * precio
    print(f"{producto:8s} | {cantidad: ^8} | ${precio: <5} | ${subtotal: >7.2f}")
```

```
PRODUCTO | CANTIDAD | PRECIO | SUBTOTAL
leche    |    2     | $120   | $ 240.00
pan      |   3.5    | $800   | $2800.00
arroz    |   1.75   | $960   | $1680.00
```

| Pieza | Significado |
|---|---|
| `8s` | String de al menos 8 caracteres (rellena con espacios a la derecha) |
| `^` | Centrado |
| `<` | Alineado a la izquierda |
| `>` | Alineado a la derecha |
| `7.2f` | Número decimal (*float*) de 7 caracteres con 2 decimales |
| `d` | Número entero |
| `8.8s` | Como `8s`, pero **corta** el texto a 8 caracteres |

> [!warning] El tamaño no corta el texto
> Si el string es más largo que el tamaño indicado (`{producto:8s}` con `'lecheeeeeeeeeeeeeee'`), se imprime completo y la tabla se desalinea. Para truncarlo hay que agregar la precisión: `{producto:8.8s}`.

La lista completa de opciones está en la documentación oficial de Python: <https://docs.python.org/3/library/string.html#format-specification-mini-language>.

## Preguntas de repaso

> [!question]- ¿Qué hace `{x:>7.2f}` dentro de un f-string?
> Muestra `x` como decimal con 2 decimales, en un espacio de 7 caracteres y alineado a la derecha.

> [!question]- ¿Qué pasa con `{producto:8s}` si `producto` tiene 15 letras?
> El texto se imprime completo (el tamaño es un mínimo) y las columnas siguientes se desalinean. Para cortarlo a 8 caracteres hay que usar `{producto:8.8s}`.

> [!question]- ¿En qué orden se escriben las partes de una especificación de formato como `{x:*^10.2f}`?
> Primero el relleno (`*`), luego la alineación (`^`), el tamaño (`10`) y al final el tipo con sus decimales (`.2f`).
