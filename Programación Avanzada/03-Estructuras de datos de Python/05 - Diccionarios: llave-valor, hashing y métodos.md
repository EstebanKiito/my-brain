---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/diccionarios
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructuras de datos y tuplas]]"
---

# Diccionarios: llave-valor, hashing y métodos

Buscar datos mediante comparaciones secuenciales o cadenas interminables de `if-elif-else` es ineficiente y difícil de mantener. Cuando necesitamos asociar un identificador único con su información correspondiente, la estructura adecuada es una tabla de correspondencia directa.

## Qué es un diccionario

Un **diccionario** (`dict`) es una estructura de datos no secuencial y mutable que almacena pares formados por una **llave** (*key*) y un **valor** (*value*).

Internamente está implementado mediante una **tabla hash** (*hash table*), lo que permite consultar, insertar o eliminar elementos en **tiempo constante promedio $O(1)$**, sin importar cuántos datos contenga.

![Estructura de tabla hash en diccionarios](adjuntos/Estructura%20de%20tabla%20hash%20en%20diccionarios.png)

> [!example]- Transcripción de la imagen
> - Diagrama conceptual de una tabla hash.
> - A la izquierda, una función hash recibe una llave de entrada (un texto) y calcula un índice entero.
> - A la derecha, un arreglo de ranuras (*buckets*) donde cada índice apunta al valor correspondiente almacenado en memoria.

## Operaciones básicas y acceso

En Python los diccionarios se declaran mediante llaves `{}` con la sintaxis `llave: valor`:

```python
monedas = {
    "Chile": "Peso",
    "Perú": "Sol",
    "España": "Euro",
    "Japón": "Yen",
}

# Acceso directo por llave e inserción/actualización
print(monedas["Chile"])
monedas["Brasil"] = "Real"
monedas["Chile"] = "CLP"

# Acceso seguro con .get() y comprobación in en O(1)
print(monedas.get("Argentina", "Sin registro"))
print("España" in monedas)
```

```
Peso
Sin registro
True
```

> [!warning] Acceso con corchetes vs get
> Intentar leer una llave inexistente con `monedas["Argentina"]` produce un error fatal `KeyError`. Para evitarlo, usa siempre `monedas.get(llave, default)` cuando no exista certeza de que la llave esté en el diccionario.

> [!tip] Eliminar elementos con del
> La instrucción `del diccionario[llave]` remueve el par llave-valor en tiempo $O(1)$. Si la llave no existe levantará `KeyError`, por lo que es prudente verificar con `in` o usar el método `diccionario.pop(llave, default)` que no arroja error si se le pasa un valor de respaldo.

## Qué objetos pueden ser llaves: hashing

Para que un objeto pueda ser utilizado como llave de un diccionario en Python, debe ser **hasheable** (*hashable*):

1. Debe poseer un método `__hash__()` que retorne un número entero invariable durante toda su vida útil.
2. Debe poder compararse con otros objetos mediante igualdad `__eq__()`.
3. Objetos iguales deben tener obligatoriamente el mismo valor hash: si `a == b`, entonces `hash(a) == hash(b)`.

```python
# Tipos inmutables son hasheables (retornan un entero)
print(isinstance(hash("Chile"), int))
print(isinstance(hash((1, 2, 3)), int))

# Tipos mutables no son hasheables
try:
    hash([1, 2, 3])
except TypeError as error:
    print(f"Error: {error}")
```

```
True
True
Error: unhashable type: 'list'
```

- **Llaves válidas:** enteros, flotantes, strings, booleanos y tuplas cuyos elementos sean a su vez inmutables.
- **Llaves inválidas:** listas, diccionarios y conjuntos (*sets*), pues su contenido puede mutar y cambiaría la posición que les corresponde en la tabla hash.
- **Valores:** cualquier objeto de Python, mutable o inmutable, incluyendo otras listas o diccionarios anidados.

## Métodos de iteración y comprensión

Los diccionarios ofrecen tres vistas dinámicas para recorrer su contenido:

```python
precios = {"manzana": 500, "plátano": 300, "naranja": 400}

# Iterar sobre pares (llave, valor) con .items()
for fruta, precio in precios.items():
    print(f"{fruta.capitalize()}: ${precio}")

# Diccionarios por comprensión (dict comprehension)
descuentos = {fruta: precio * 0.9 for fruta, precio in precios.items() if precio > 350}
print(f"Con descuento: {descuentos}")
```

```
Manzana: $500
Plátano: $300
Naranja: $400
Con descuento: {'manzana': 450.0, 'naranja': 360.0}
```

## Preguntas de repaso

> [!question]- ¿Por qué una lista de Python no puede utilizarse como llave de un diccionario?
> Porque las listas son mutables. Si una lista cambiara su contenido tras ser insertada como llave, su valor hash cambiaría o invalidaría su ubicación en la tabla hash interna, haciendo imposible volver a encontrar el valor asociado.

> [!question]- ¿Qué ventaja presenta el método `.get()` frente al acceso directo con corchetes `[]`?
> Evita que el programa se caiga con una excepción `KeyError` cuando la llave no existe, permitiendo devolver `None` o un valor por defecto seguro de manera concisa.

> [!question]- ¿Por qué el operador `elemento in diccionario` es mucho más rápido que `elemento in lista`?
> Porque en un diccionario la búsqueda se realiza mediante la función hash de la llave en tiempo constante promedio $O(1)$, mientras que en una lista se debe realizar una búsqueda lineal que recorre los elementos uno por uno en tiempo $O(N)$.

> [!question]- ¿Qué recorre por defecto un bucle `for x in mi_diccionario:` si no se especifica ningún método?
> Recorre únicamente las **llaves** del diccionario. Para recorrer los valores se debe usar `.values()`, y para ambos en tuplas se debe usar `.items()`.
