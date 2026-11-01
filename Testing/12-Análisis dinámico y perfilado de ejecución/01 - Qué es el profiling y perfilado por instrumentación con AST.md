---
ramo: "Testing"
tema: "Análisis dinámico y perfilado de ejecución"
tags:
  - testing/analisis-dinamico-y-perfilado-de-ejecucion
  - origen/complemento
prerrequisitos:
  - "[[04 - Transformadores de sentencias y funciones inyección de código y limpieza en dos pasadas]]"
---

# Qué es el profiling y perfilado por instrumentación con AST

## El problema: optimizar a ciegas

En cualquier sistema de software medianamente grande se cumple una ley empírica (la regla del 90/10): un programa suele pasar el 90% de su tiempo ejecutando apenas el 10% de su código. Intentar optimizar funciones adivinando cuál es lenta casi siempre desperdicia esfuerzo en código que apenas se ejecuta.

El **profiling** (perfilado de ejecución) es una técnica de **análisis dinámico** que mide el comportamiento real de un programa mientras corre para responder preguntas concretas con datos:
- **Frecuencia de llamadas**: ¿cuántas veces se invoca cada función?
- **Tiempo de ejecución**: ¿cuántos milisegundos acumula cada función (tiempo total, promedio, mínimo y máximo)?
- **Grafo de llamadas (*Call Graph*)**: ¿qué función llamó a cuál otra y con qué argumentos?

Las regiones donde se concentra la mayor parte del tiempo o de las llamadas se denominan **hotspots** (puntos calientes). Existen dos filosofías opuestas para descubrirlos:
1. **Instrumentación (*Instrumentation Profiling*)**: modificar el programa antes de ejecutarlo (por ejemplo, reescribiendo su AST) para insertar sensores en cada entrada y salida de función.
2. **Muestreo (*Execution Sampling*)**: dejar el programa intacto y tomar "fotografías" periódicas de su pila de llamadas desde un hilo externo.

---

## Perfilado por instrumentación: `FunctionProfiler` y `FunctionInstrumentor`

Si ya sabemos reescribir árboles sintácticos con `ast.NodeTransformer`, construir un perfilador por instrumentación para contar llamadas y construir un grafo de llamadas es directo. Necesitamos dos piezas: un **recolector en tiempo de ejecución** (`FunctionProfiler`) y un **transformador de AST** (`FunctionInstrumentor`).

### 1. El recolector (`FunctionProfiler`)

Mantiene un diccionario de registros por función (`records`) y una **pila de llamadas activa** (`call_stack`) para saber quién es el llamador (*caller*) actual cuando se inicia una nueva función:

```python
import ast

class FunctionProfiler:
    records = {}     # nombre -> {"freq": int, "args": list, "callers": set}
    call_stack = []  # funciones actualmente en ejecución

    @classmethod
    def reset(cls):
        cls.records = {}
        cls.call_stack = []

    @classmethod
    def record_start(cls, func_name, args):
        if func_name not in cls.records:
            cls.records[func_name] = {"freq": 0, "args": [], "callers": set()}
        cls.records[func_name]["freq"] += 1
        cls.records[func_name]["args"].append(args)
        if cls.call_stack:
            cls.records[func_name]["callers"].add(cls.call_stack[-1])
        cls.call_stack.append(func_name)

    @classmethod
    def record_end(cls, func_name):
        if cls.call_stack and cls.call_stack[-1] == func_name:
            cls.call_stack.pop()
```

### 2. El inyector básico de entrada (`FunctionInstrumentor`)

En su versión más simple (solo para contar llamadas y argumentos al inicio de cada función), el `NodeTransformer` construye una llamada a `FunctionProfiler.record_start("nombre", [arg1, arg2, ...])` y la inserta en la posición `0` del cuerpo de cada `FunctionDef`:

```python
class BasicFunctionInstrumentor(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        arg_names = [ast.Name(id=a.arg, ctx=ast.Load()) for a in node.args.args]
        hook = ast.Expr(
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id="FunctionProfiler", ctx=ast.Load()),
                    attr="record_start",
                    ctx=ast.Load()
                ),
                args=[ast.Constant(value=node.name), ast.List(elts=arg_names, ctx=ast.Load())],
                keywords=[]
            )
        )
        node.body.insert(0, hook)
        return ast.fix_missing_locations(node)
```

Al instrumentar un programa donde `cube(x)` llama a `square(x)` y `multiply(x, y)`, el reporte revela con **precisión exacta** cuántas veces se ejecutó cada función y desde qué orígenes (`callers`).

---

---

## Ejemplo práctico: perfilar `cube` y descubrir un error del inyector básico

Programa de ejemplo:

```python
fuente = """def square(x):
    return x * x

def multiply(x, y):
    return x * y

def cube(x):
    return multiply(square(x), x)

cube(3)
cube(4)
"""
```

Lo instrumentamos con `BasicFunctionInstrumentor` y lo ejecutamos:

```python
arbol = BasicFunctionInstrumentor().visit(ast.parse(fuente))
ast.fix_missing_locations(arbol)

FunctionProfiler.reset()
exec(compile(arbol, "<instrumentado>", "exec"), {"FunctionProfiler": FunctionProfiler})

for nombre, r in FunctionProfiler.records.items():
    print(nombre, r["freq"], r["args"], sorted(r["callers"]))
```

Resultado:

```
cube     2 [[3], [4]]          ['multiply']
square   2 [[3], [4]]          ['cube']
multiply 2 [[9, 3], [16, 4]]   ['square']
```

* **Frecuencia y argumentos: correctos.** Cada función se llamó $2$ veces y vemos los argumentos exactos (por ejemplo, `multiply(9, 3)`, donde $9 = \text{square}(3)$).
* **Llamadores: incorrectos para `cube` y `multiply`.** `cube` figura como llamada por `multiply` y `multiply` por `square`, lo cual es falso: `multiply` y `square` las llama `cube`, y a `cube` nadie la llama desde otra función.

### ¿Por qué falla el grafo de llamadas?

El inyector básico solo registra la **entrada** (`record_start`) y nunca el **fin**, así que la pila de llamadas no se vacía:

```python
print(FunctionProfiler.call_stack)
# ['cube', 'square', 'multiply', 'cube', 'square', 'multiply']
```

Tras `cube(3)` la pila debería estar vacía, pero queda llena de funciones ya terminadas. En la segunda llamada, `cube` ve a `multiply` en el tope de la pila y cree que `multiply` la llamó. Es la razón por la que la siguiente nota agrega un `record_end` en **cada** punto de salida.

> [!tip] Lección general
> Un contador de entradas es fácil; mantener un **estado correcto entre entrada y salida** (pila, tiempos) requiere cubrir todas las salidas de la función, incluidos los `return` múltiples y las funciones sin `return`.

---

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre buscar bugs con un test funcional y hacer profiling de un programa?
> Un test funcional verifica la corrección de la salida frente a un oráculo (¿calcula el resultado correcto?), mientras que el profiling mide propiedades no funcionales del comportamiento dinámico durante la ejecución (dónde se gasta el tiempo de CPU, cuántas veces se invoca cada función y qué cadenas de llamadas dominan la ejecución) para localizar *hotspots*.

> [!question]- ¿Cómo logra `FunctionProfiler.record_start` descubrir qué función llamó a la función actual sin que el AST le pase explícitamente el nombre del llamador?
> Manteniendo una pila explícita `cls.call_stack` en memoria: cada vez que una función inicia (`record_start`), antes de apilar su propio nombre mira el tope actual de `call_stack` (`cls.call_stack[-1]`), que corresponde exactamente a la función padre que estaba ejecutándose cuando ocurrió la invocación, y al terminar (`record_end`) se desapila.

> [!question]- ¿Qué propiedad fundamental debe verificarse al testear un instrumentador de código antes de confiar en sus métricas?
> Además de comprobar que el AST resultante sea sintácticamente válido y que las métricas coincidan con las llamadas reales, es indispensable verificar la **preservación del comportamiento**: que el programa instrumentado produzca exactamente los mismos valores de retorno y efectos observables que el programa original.

> [!question]- Un profiler por instrumentación reporta que `helper()` se llamó $1\,000\,000$ veces y `main()` una vez. ¿Qué información da el conteo y qué no da?
> El conteo exacto de llamadas es fiable, pero no dice cuánto tiempo toma cada una. Si `helper` dura $0.1\ \mu s$, el total es $0.1$ s; si `main` dura $5$ s, el cuello de botella no es `helper` por frecuente que sea. Para decidir qué optimizar se necesitan **tiempos** (y, por la regla del 90/10, un porcentaje del total).

> [!question]- ¿Qué cambiarías en `FunctionProfiler` para que `record_end` tuviera sentido si `record_start` no devuelve nada?
> Que cada función instrumentada llame a `record_end(nombre)` justo antes de terminar (en cada `return`), y que `record_end` desapile el nombre de `call_stack`. Si hay funciones recursivas conviene devolver un identificador de la llamada desde `record_start` para emparejar cada inicio con su fin, como hace la implementación del curso.
