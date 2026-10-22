---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/funciones
  - programacion/argumentos
  - origen/complemento
prerrequisitos:
  - "[[09 - Parámetros y argumentos: posicionales, keywords y desempaquetado]]"
---

# Parámetros variables: args y kwargs en funciones

Existen funciones que deben ser capaces de procesar una cantidad indeterminada de datos sin saber de antemano cuántos valores entregará el usuario: la función `print()`, por ejemplo, acepta desde cero hasta cientos de argumentos separados por coma.

## Recibir argumentos posicionales arbitrarios: *args

Al anteponer un asterisco a un parámetro en la **definición** de una función (por convención llamado `*args`, de *arguments*), Python empaqueta todos los argumentos posicionales adicionales en una **tupla**:

```python
def calcular_promedio(*notas: float) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

print(f"Promedio de 2 notas: {calcular_promedio(6.5, 5.5)}")
print(f"Promedio de 4 notas: {calcular_promedio(7.0, 6.0, 5.0, 6.5)}")
print(f"Sin notas:          {calcular_promedio()}")
```

```
Promedio de 2 notas: 6.0
Promedio de 4 notas: 6.125
Sin notas:          0.0
```

Dentro de la función, `notas` es una tupla común y corriente, lo que garantiza inmutabilidad y permite iterar con un bucle `for` o usar funciones como `len()` y `sum()`.

## Recibir argumentos por palabra clave arbitrarios: **kwargs

Al anteponer dos asteriscos a un parámetro (por convención llamado `**kwargs`, de *keyword arguments*), Python empaqueta todos los argumentos por palabra clave adicionales en un **diccionario**:

```python
def registrar_evento(tipo: str, **detalles):
    print(f"Evento: {tipo}")
    for clave, valor in detalles.items():
        print(f"  - {clave}: {valor}")

registrar_evento(
    "error_conexion",
    codigo=404,
    servidor="api.uc.cl",
    reintentos=3
)
```

```
Evento: error_conexion
  - codigo: 404
  - servidor: api.uc.cl
  - reintentos: 3
```

Dentro de la función, `detalles` es un diccionario mutable (`dict`) donde las llaves son cadenas con los nombres de los parámetros y los valores son los argumentos enviados.

## Orden de declaración en la cabecera de la función

Cuando combinamos distintos tipos de parámetros en una misma función, Python exige respetar una jerarquía estricta:

```
def funcion(posicionales, defaults, *args, keyword_only, **kwargs):
```

1. **Parámetros obligatorios posicionales o por palabra clave.**
2. **Parámetros con valor por defecto.**
3. **`*args`** (recolector de posicionales sobrantes en tupla).
4. **Parámetros solo por palabra clave** (*keyword-only*): van después del asterisco y **solo** pueden suministrarse con su nombre explícito (`clave=valor`).
5. **`**kwargs`** (recolector de palabras clave sobrantes en diccionario).

```python
def configurar_servidor(host: str, puerto: int = 8080, *ips_bloqueadas, ssl: bool = False, **opciones):
    print(f"Servidor en {host}:{puerto} (SSL={ssl})")
    print(f"IPs bloqueadas ({type(ips_bloqueadas).__name__}): {ips_bloqueadas}")
    print(f"Otras opciones ({type(opciones).__name__}): {opciones}")

configurar_servidor(
    "127.0.0.1", 443,
    "192.168.1.5", "10.0.0.1",
    ssl=True,
    timeout=30, modo="producción"
)
```

```
Servidor en 127.0.0.1:443 (SSL=True)
IPs bloqueadas (tuple): ('192.168.1.5', '10.0.0.1')
Otras opciones (dict): {'timeout': 30, 'modo': 'producción'}
```

> [!warning] Reglas de unicidad sintáctica
> - No se puede utilizar más de un `*args` ni más de un `**kwargs` en la misma firma de función.
> - `**kwargs` debe situarse **estrictamente al final** de la lista de parámetros. Escribir `def f(**kwargs, extra):` genera un error de sintaxis inmediato.

> [!tip] Delegación y reenvío con super()
> Un uso indispensable de `*args` y `**kwargs` aparece en la herencia de clases: permite que una subclase acepte cualquier combinación de argumentos y los reenvíe intactos al constructor de la clase base con `super().__init__(*args, **kwargs)`.

## Preguntas de repaso

> [!question]- ¿De qué tipo de datos son internamente `args` y `kwargs` dentro del cuerpo de la función?
> `args` es una **tupla** (`tuple`) inmutable con los argumentos posicionales adicionales, y `kwargs` es un **diccionario** (`dict`) mutable con los pares clave-valor adicionales.

> [!question]- ¿Qué ocurre si se llama a una función que define `def f(*args):` pasando un argumento nombrado como `f(x=10)`?
> Python levanta un error `TypeError: f() got an unexpected keyword argument 'x'`, porque `*args` captura únicamente argumentos posicionales sin nombre.

> [!question]- ¿Qué es un parámetro solo por palabra clave (*keyword-only*) y cómo se define?
> Es un parámetro que solo puede recibir valor nombrándolo explícitamente (`nombre=valor`). Se define ubicándolo en la cabecera de la función después de `*args` o después de un asterisco solitario `*`.

> [!question]- ¿Por qué no está permitido escribir ningún parámetro después de `**kwargs` en la firma de una función?
> Porque `**kwargs` captura absolutamente todos los argumentos nombrados restantes en un diccionario; cualquier parámetro situado después jamás podría recibir un valor, por lo que Python lo rechaza con un `SyntaxError`.
