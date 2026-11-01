---
ramo: "Testing"
tema: "Análisis dinámico y perfilado de ejecución"
tags:
  - testing/analisis-dinamico-y-perfilado-de-ejecucion
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es el profiling y perfilado por instrumentación con AST]]"
---

# Implementación de FunctionInstrumentor manejo de return y recursión

## El desafío de medir tiempos de ejecución

Contar cuántas veces entra una función basta con inyectar una línea al inicio de `node.body`. Pero si queremos medir **cuánto tiempo tarda cada llamada** (`record_start` al entrar y `record_end` al salir) y construir un grafo de llamadas preciso, aparecen tres problemas técnicos que suelen evaluarse en pruebas:
1. **Múltiples puntos de salida**: una función puede tener varios `return` dentro de `if/else` o ciclos, o no tener ningún `return` explícito al final.
2. **Evaluación de la expresión de retorno**: en `return calculo_costoso(x)`, si llamamos a `record_end` *antes* del `return`, no habremos medido cuánto tardó `calculo_costoso(x)`; y si lo ponemos *después* del `return`, será código muerto inalcanzable.
3. **Funciones recursivas**: si `factorial(5)` llama a `factorial(4)`, ambas comparten el mismo nombre `"factorial"`. Si guardamos un único `start_time` por nombre de función, la llamada hija sobrescribirá el tiempo de inicio de la llamada padre.

---

## Arquitectura del proyecto `instrumentor`

En la implementación de referencia del curso (`function_instrumentor.py`, `profiler.py` y `function_record.py`), estos tres problemas se resuelven combinando una transformación AST cuidadosa con variables locales por invocación:

### 1. Envolver el valor de `return` dentro de `Profiler.record_end`

El método `Profiler.record_end(start_data, return_value)` recibe dos argumentos: los datos de inicio de esa llamada y el **valor de retorno ya evaluado**, registra la duración transcurrida y **devuelve `return_value` intacto**. Así, `FunctionInstrumentor` transforma cada nodo `Return(value=expr)` en:

```python
return Profiler.record_end(_profiler_start_data, expr)
```

Como Python evalúa los argumentos de una llamada antes de invocar la función, primero ejecuta `expr` (incluyendo cualquier llamada recursiva o cálculo costoso dentro del `return`), luego ejecuta `Profiler.record_end(...)` cerrando el cronómetro en el instante exacto de salida, y finalmente retorna el valor original sin alterar la semántica del programa.

```python
from ast import NodeTransformer, Return, parse, unparse, fix_missing_locations

class FunctionInstrumentor(NodeTransformer):
    def visit_Module(self, node):
        self.generic_visit(node)
        node.body.insert(0, parse("from profiler import Profiler").body[0])
        return fix_missing_locations(node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        arg_list = "[" + ", ".join(a.arg for a in node.args.args) + "]"
        start_stmt = parse(
            f"_profiler_start_data = Profiler.record_start('{node.name}', {arg_list})"
        ).body[0]
        node.body.insert(0, start_stmt)

        # Si la función no termina en un Return explícito, cerramos al final del cuerpo
        if not isinstance(node.body[-1], Return):
            end_stmt = parse("Profiler.record_end(_profiler_start_data, None)").body[0]
            node.body.append(end_stmt)
        return fix_missing_locations(node)

    def visit_Return(self, node):
        val_code = unparse(node.value) if node.value is not None else "None"
        return parse(f"return Profiler.record_end(_profiler_start_data, {val_code})").body[0]
```

---

## Cómo soportar recursión sin corromper los tiempos

Observa cómo `visit_FunctionDef` guarda el resultado de `Profiler.record_start` en la variable local `_profiler_start_data`:

```python
class Profiler:
    # ...
    def fun_call_start(self, functionName, args):
        if self.callStack:
            caller = self.callStack[-1]
            self.get_record(caller).add_function_callee(functionName)
        self.callStack.append(functionName)
        record = self.get_record(functionName)
        record.UpdateCallers(args, self.callStack)
        return (functionName, time.perf_counter())

    def fun_call_end(self, start_data, return_value):
        functionName, start_time = start_data
        end_time = time.perf_counter()
        self.get_record(functionName).UpdateTime(end_time - start_time)
        self.callStack.pop()
        return return_value
```

¿Por qué funciona esto con funciones recursivas como `factorial(5)`?
- Cada invocación a `factorial(n)` crea su **propio frame de ejecución independiente** en la pila de Python, con su propia variable local `_profiler_start_data = ('factorial', t_inicio_n)`.
- Cuando `factorial(5)` invoca `return Profiler.record_end(_profiler_start_data, n * factorial(n - 1))`, primero se evalúa `factorial(4)` (y sus descendientes `3, 2, 1, 0`).
- Cada llamada interna mide su propio `end_time - start_time` usando su `_profiler_start_data` local (o equivalentemente, desapilando su `start_time` desde una pila LIFO de tiempos de inicio). Ninguna llamada hija sobrescribe el `start_time` de su padre.
- Con las duraciones registradas en `executionTimes`, `FunctionRecord.computeMetrics()` calcula el número de llamadas (`freq`), tiempo máximo (`max`), mínimo (`min`), promedio (`avg`) y la lista de funciones llamadas (`callees`) y llamadoras (`callers`).

---

---

## Ejemplo práctico: ver el código instrumentado y los registros

Instrumentamos un programa con una función recursiva (`factorial`) y otra sin `return` (`saludar`):

```python
fuente = """def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def saludar(nombre):
    print("hola", nombre)

factorial(4)
saludar("ana")
"""

arbol = FunctionInstrumentor().visit(ast.parse(fuente))
print(ast.unparse(arbol))
```

El código transformado es:

```python
def factorial(n):
    _profiler_start_data = Profiler.record_start('factorial', [n])
    if n <= 1:
        return Profiler.record_end(_profiler_start_data, 1)
    return Profiler.record_end(_profiler_start_data, n * factorial(n - 1))

def saludar(nombre):
    _profiler_start_data = Profiler.record_start('saludar', [nombre])
    print('hola', nombre)
    Profiler.record_end(_profiler_start_data, None)
factorial(4)
saludar('ana')
```

Tres detalles que resuelven los desafíos de la nota:

1. **Múltiples salidas:** cada `return` fue reemplazado individualmente por `return Profiler.record_end(...)`.
2. **Evaluación antes de cerrar:** en `n * factorial(n - 1)` Python evalúa los argumentos primero, así que la llamada recursiva completa su ciclo `record_start`/`record_end` **antes** de que se cierre la llamada exterior.
3. **Sin `return`:** `saludar` no tiene ninguno, así que el instrumentador agrega `record_end(..., None)` al final.

### Resultado de ejecutar el programa instrumentado

| Función | Llamadas (`freq`) | Tiempos registrados | Llama a |
| :--- | :---: | :---: | :--- |
| `factorial` | $4$ | $4$ (uno por llamada) | `factorial` |
| `saludar` | $1$ | $1$ | — |

`factorial(4)` genera cuatro llamadas anidadas (`n = 4, 3, 2, 1`), y cada una guarda su propio `_profiler_start_data` en su variable local, por lo que los tiempos no se mezclan. El hecho de que `factorial` aparezca como llamador de sí misma en el grafo es lo esperado en una función recursiva.

> [!caution] Qué mide el tiempo de `factorial(4)`
> El tiempo de la llamada exterior **incluye** el de todas las llamadas internas (tiempo inclusivo). Si se sumaran los $4$ tiempos se contaría varias veces el mismo trabajo, por lo que en una función recursiva hay que decidir si se reporta el tiempo inclusivo o el exclusivo.

---

## Preguntas de repaso

> [!question]- ¿Por qué no basta con insertar `Profiler.record_end(...)` justo antes de cada sentencia `return expr`?
> Porque si `expr` contiene trabajo pesado o una llamada recursiva (como `return n * factorial(n - 1)`), ejecutar `record_end` *antes* del `return` detendría el cronómetro antes de evaluar `expr`, subestimando drásticamente el tiempo real de la función y cerrando el registro del padre antes de que se ejecuten sus hijos.

> [!question]- ¿Qué ocurre con una función que no tiene ninguna sentencia `return` (por ejemplo, un procedimiento que solo imprime en pantalla)?
> `visit_FunctionDef` inspecciona la última sentencia de `node.body` (`if not isinstance(node.body[-1], Return):`) e inyecta al final del cuerpo `Profiler.record_end(_profiler_start_data, None)` para garantizar que toda entrada tenga su correspondiente salida.

> [!question]- Si no guardáramos `start_time` en una variable local del frame (`_profiler_start_data`) sino dentro del objeto `FunctionRecord` de la función, ¿qué estructura de datos deberíamos usar dentro de `FunctionRecord` para que la recursión funcione?
> Una **pila (LIFO)** de tiempos de inicio (`start_times.append(perf_counter())` al entrar y `start_times.pop()` al salir), de modo que cada `record_end` empareje exactamente con el `record_start` de la invocación recursiva más reciente.

> [!question]- ¿Qué pasaría si `visit_Return` llamara a `record_end` en una sentencia separada antes del `return` en lugar de envolver el valor?
> Se cerraría la medición antes de evaluar la expresión de retorno. Por ejemplo, con `return calculo_costoso(x)` el profiler registraría un tiempo casi nulo y atribuiría el costo real a quien llame, porque `calculo_costoso` se ejecutaría después de `record_end`.

> [!question]- Una función tiene un `if/else` donde ambas ramas terminan en `return`, y su última sentencia es ese `if`. ¿Agrega el instrumentador un `record_end` extra al final?
> Sí, porque la regla mira solo si la **última sentencia** del cuerpo es un `Return`, y aquí es un `If`. Ese `record_end` final queda inalcanzable (ambas ramas ya retornaron), así que no se ejecuta ni causa problemas. Los `return` de cada rama siguen cerrando la medición gracias a `visit_Return`.
