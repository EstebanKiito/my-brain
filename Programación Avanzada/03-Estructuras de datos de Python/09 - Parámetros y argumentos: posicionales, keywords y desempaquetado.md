---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/funciones
  - programacion/argumentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructuras de datos y tuplas]]"
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
---

# Parámetros y argumentos: posicionales, keywords y desempaquetado

En Python el paso de información a funciones ofrece gran flexibilidad: podemos entregar valores por orden, llamarlos explícitamente por su nombre, proveer valores predeterminados o desempaquetar estructuras completas en una sola línea.

## Parámetros vs Argumentos

Aunque en el lenguaje cotidiano suelen usarse como sinónimos, en Ciencia de la Computación representan conceptos distintos:

- **Parámetro:** es la variable nombrada que figura en la **definición** de la función (`def calcular(base, altura):`).
- **Argumento:** es el **valor real** que se envía al momento de invocar la función (`calcular(10, 5)`).

## Argumentos posicionales y por palabra clave

Al invocar una función existen dos formas de establecer la correspondencia entre los argumentos y los parámetros:

1. **Argumento posicional:** el valor se asocia al parámetro por el orden en que aparece de izquierda a derecha.
2. **Argumento por palabra clave** (*keyword argument*): el valor va precedido por el identificador del parámetro (`nombre=valor`), lo que permite entregarlos en cualquier orden:

```python
def describir_persona(nombre: str, edad: int, ciudad: str):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Llamada puramente posicional
describir_persona("Camila", 22, "Valparaíso")

# Llamada usando palabras clave en distinto orden
describir_persona(ciudad="Santiago", nombre="Matías", edad=25)

# Llamada mixta: posicional primero, palabras clave después
describir_persona("Ignacio", ciudad="Concepción", edad=20)
```

```
Camila tiene 22 años y vive en Valparaíso.
Matías tiene 25 años y vive en Santiago.
Ignacio tiene 20 años y vive en Concepción.
```

> [!warning] Los argumentos posicionales siempre van primero
> En una llamada de función, nunca se puede colocar un argumento posicional después de un argumento por palabra clave. La llamada `describir_persona(nombre="Ana", 20, "Arica")` produce un error de sintaxis inmediato: `SyntaxError: positional argument follows keyword argument`.

## Desempaquetado en la invocación: * y **

Cuando los datos que queremos enviar ya residen en una lista, tupla o diccionario, no es necesario extraerlos manualmente uno por uno:

- **Operador `*` (desempaquetado de iterables):** expande una lista, tupla o conjunto como una serie de argumentos posicionales independientes.
- **Operador `**` (desempaquetado de diccionarios):** expande un diccionario como argumentos por palabra clave, asociando cada llave con el parámetro homónimo:

```python
def conectar_bd(host: str, puerto: int, base_datos: str):
    print(f"Conectando a {host}:{puerto}/{base_datos}")

parametros_posicionales = ["localhost", 5432]
parametros_dict = {"base_datos": "estudiantes_db"}

# Desempaquetado simultáneo con * y **
conectar_bd(*parametros_posicionales, **parametros_dict)
```

```
Conectando a localhost:5432/estudiantes_db
```

## Parámetros con valores por defecto

Podemos asignar valores por defecto en la cabecera de la función. Si el invocador no suministra un argumento para ese parámetro, se usará el valor predeterminado:

```python
def crear_usuario(username: str, rol: str = "estudiante", activo: bool = True):
    print(f"Usuario: {username} | Rol: {rol} | Activo: {activo}")

crear_usuario("javiera")
crear_usuario("profe_hernan", rol="docente")
```

```
Usuario: javiera | Rol: estudiante | Activo: True
Usuario: profe_hernan | Rol: docente | Activo: True
```

> [!tip] Regla en la definición de funciones
> Al definir la firma de una función, los parámetros obligatorios (sin valor por defecto) deben colocarse **siempre antes** que los parámetros opcionales (con valor por defecto). Una firma como `def f(a=1, b):` es inválida y genera `SyntaxError: non-default argument follows default argument`.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre un parámetro y un argumento en Python?
> El parámetro es la variable declarada en la firma de la función durante su definición, mientras que el argumento es el valor o expresión concreto que se pasa a esa función al momento de ejecutar la llamada.

> [!question]- ¿Por qué falla la llamada `ejemplo(a=1, 2, 3)` antes de ejecutarse el cuerpo de la función?
> Porque la sintaxis de Python prohíbe colocar argumentos posicionales después de argumentos por palabra clave, produciendo un `SyntaxError` durante el análisis léxico.

> [!question]- ¿Qué ocurre si un diccionario contiene una llave que no coincide con ningún parámetro de la función al usar `**dict`?
> Python levanta un error `TypeError: got an unexpected keyword argument` indicando que la función no reconoce ese nombre de parámetro, a menos que la función declare `**kwargs` para capturar palabras clave arbitrarias.

> [!question]- ¿Por qué no está permitido definir `def f(x=0, y):` en Python?
> Porque generaría ambigüedad al llamar a la función con un solo argumento posicional (`f(5)`): el intérprete no sabría si ese argumento corresponde a `x` (dejando a `y` sin valor obligatorio) o a `y` (usando el default de `x`).
