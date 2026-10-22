---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/funciones
  - programacion/decoradores
  - origen/complemento
prerrequisitos:
  - "[[10 - Parámetros variables: args y kwargs en funciones]]"
---

# Decoradores: funciones de primera clase y sintaxis arroba

Cuando necesitamos añadir una misma funcionalidad transversal a muchas funciones —como medir el tiempo de ejecución, registrar accesos en un log o comprobar si un usuario tiene permisos—, copiar y pegar código dentro de cada función resulta sucio y propenso a errores.

## Funciones como objetos de primera clase

En Python las funciones son **ciudadanos de primera clase** (*first-class citizens*). Esto significa que una función se comporta como cualquier otro objeto (como un número o una cadena):

- Puede asignarse a una variable.
- Puede pasarse como argumento a otra función.
- Puede definirse dentro del cuerpo de otra función (funciones anidadas).
- Puede ser retornada como resultado de otra función.

```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

# Asignar una función a otra variable
mi_funcion = saludar
print(mi_funcion("Daniela"))
```

```
Hola, Daniela
```

## Qué es un decorador

Un **decorador** es un patrón de diseño implementado mediante una función que **recibe una función como argumento**, le añade un comportamiento adicional envolviéndola en una función interna (*wrapper*), y **retorna la función resultante modificada**.

```python
def registrar_llamada(funcion_original):
    def envoltura(*args, **kwargs):
        print(f"[LOG] Ejecutando: {funcion_original.__name__}")
        resultado = funcion_original(*args, **kwargs)
        print(f"[LOG] Finalizó: {funcion_original.__name__}")
        return resultado
    return envoltura
```

## La sintaxis con arroba (@)

Python ofrece una sintaxis simplificada utilizando el símbolo **`@`** colocado inmediatamente antes de la definición de la función:

```python
# Aplicación del decorador con sintaxis @
@registrar_llamada
def multiplicar(a: int, b: int) -> int:
    return a * b

# La línea anterior equivale exactamente a:
# multiplicar = registrar_llamada(multiplicar)

resultado = multiplicar(4, 5)
print(f"Resultado: {resultado}")
```

```
[LOG] Ejecutando: multiplicar
[LOG] Finalizó: multiplicar
Resultado: 20
```

### El rol de *args y **kwargs en la envoltura

Para que un decorador pueda aplicarse a cualquier función sin importar cuántos argumentos reciba (desde cero hasta múltiples posicionales o por palabra clave), la función interna de envoltura debe declararse siempre con `(*args, **kwargs)` y reenviarlos intactos a la función original con `funcion_original(*args, **kwargs)`.

> [!tip] Preservar los metadatos con functools.wraps
> Al envolver una función, sus metadatos (`__name__` y docstring `__doc__`) quedan reemplazados por los de la función `envoltura`. Para conservar los datos originales de la función decorada, se utiliza el decorador `@wraps(funcion_original)` del módulo estándar `functools`.

> [!warning] El orden de ejecución de la envoltura
> Recuerda que el código del decorador exterior se ejecuta **una sola vez** al momento de definir o cargar la función. En cambio, el código dentro de la función `envoltura` se ejecuta **cada vez** que la función decorada es llamada.

## Preguntas de repaso

> [!question]- ¿Qué significa que las funciones sean "ciudadanos de primera clase" en Python?
> Significa que las funciones son tratadas como cualquier otro objeto o valor: pueden ser asignadas a variables, almacenadas en listas o diccionarios, entregadas como argumentos y retornadas desde otras funciones.

> [!question]- ¿A qué equivale sintácticamente escribir `@mi_decorador` sobre `def mi_funcion():`?
> Equivale exactamente a definir la función de forma habitual y luego reasignar su identificador al resultado de invocar el decorador: `mi_funcion = mi_decorador(mi_funcion)`.

> [!question]- ¿Por qué es fundamental que la función envoltura interior reciba `*args` y `**kwargs`?
> Porque permite que el decorador sea genérico y reutilizable sobre funciones con cualquier cantidad y tipo de argumentos posicionales o por palabra clave.

> [!question]- ¿Por qué una función decorada debe retornar el valor devuelto por `funcion_original(*args, **kwargs)`?
> Porque si la envoltura no retorna explícitamente ese resultado, la llamada a la función decorada devolverá siempre `None`, perdiendo el valor calculado por la función original.

