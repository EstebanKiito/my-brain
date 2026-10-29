---
ramo: "Testing"
tema: "Transformaciones de código con AST"
tags:
  - testing/transformaciones-de-codigo-con-ast
  - origen/complemento
prerrequisitos:
  - "[[Testing/09-Transformaciones de código con AST/03 - Transformadores de expresiones operadores llamadas y la trampa de RenameTransformer|Transformadores de expresiones operadores llamadas y la trampa de RenameTransformer]]"
---

# Transformadores de sentencias y funciones: inyección de código y limpieza en dos pasadas

## 1. Inyección de sentencias al inicio de una función (`XTransformer` y `PrintArguments`)

Un patrón fundamental de instrumentación con AST (que volveremos a usar en el Tema 12 para construir perfiladores de ejecución) consiste en **inyectar una nueva sentencia en la posición `0` de la lista `node.body` de cada función (`ast.FunctionDef`)**.

### Caso A: Pregunta de Interrogación 2 (`XTransformer`)

En la Clase 17 se presenta el siguiente transformador y se pide mostrar cómo queda el código de `def foo(x): return x + 1` tras ejecutarlo:

```python
import ast

code = """
def foo(x):
    return x + 1
"""

class XTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        new_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[ast.Constant(value=node.name)],
                keywords=[]
            )
        )
        node.body.insert(0, new_stmt)
        return node
```

* **¿Qué nodo construye `new_stmt`?** Es una sentencia de expresión (`ast.Expr`) que envuelve una llamada (`ast.Call`) a la función `print` pasando como único argumento una constante string con el nombre de la función (`node.name`, que para `foo` vale `'foo'`).
* **¿Dónde lo coloca?** `node.body.insert(0, new_stmt)` lo inserta como **primera línea del cuerpo de la función**, desplazando el `return x + 1` hacia abajo.
* **Resultado final (`ast.unparse`):**
  ```python
  def foo(x):
      print('foo')
      return x + 1
  ```

### Caso B: Imprimir la lista de argumentos al entrar (`PrintArgumentsTransformer`)

Si en lugar del nombre de la función queremos que imprima los valores de sus argumentos `print([a, b])` en `def add(a, b):`, extraemos los nombres desde `node.args.args` (recordando convertir cada `ast.arg` en un `ast.Name` con contexto `Load()`):

```python
class PrintArgumentsTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        args_as_names = [ast.Name(id=arg.arg, ctx=ast.Load()) for arg in node.args.args]
        print_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[ast.List(elts=args_as_names, ctx=ast.Load())],
                keywords=[]
            )
        )
        node.body.insert(0, print_stmt)
        return node
```

---

## 2. Simplificación de bloques: `IfTrueTransformer`

Para eliminar un condicional redundante `if True:` conservando las instrucciones que estaban adentro de su bloque, retornamos directamente la lista `node.body`:

```python
class IfTrueTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        self.generic_visit(node)  # primero simplifica cualquier if True interno
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            return node.body      # reemplaza el nodo If por la lista de sentencias de su cuerpo
        return node
```

---

## 3. Refactorización en dos pasadas (`Visitor` + `Transformer`) y sus riesgos

Muchas transformaciones no pueden decidir qué borrar en una sola mirada, porque primero necesitan **recolectar información de todo el subárbol**. Por ejemplo, para eliminar parámetros que nunca se usan en `def combine(a, b, c): return a + b`, combinamos dos pasadas:
1. **Pasada 1 (`UsedNamesVisitor`):** recorre el `FunctionDef` y guarda en un conjunto `self.used_names` todos los `node.id` de los nodos `ast.Name` que aparecen en el cuerpo.
2. **Pasada 2 (`RemoveUnusedArgumentsTransformer`):** filtra `node.args.args` conservando solo los `arg` cuyo `arg.arg` esté en `visitor.used_names`:

```python
class UsedNamesVisitor(ast.NodeVisitor):
    def __init__(self):
        self.used_names = set()
    def visit_Name(self, node):
        self.used_names.add(node.id)

class RemoveUnusedArgumentsTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        visitor = UsedNamesVisitor()
        visitor.visit(node)
        node.args.args = [arg for arg in node.args.args if arg.arg in visitor.used_names]
        return node
```

### ¿Por qué este transformador (o borrar `assert 1 == 1`) puede romper un programa real?

Esta es una pregunta crítica de diseño del Capítulo 11:
* **Por qué `RemoveUnusedArgumentsTransformer` rompe programas reales:** si `def combine(a, b, c):` pasa a ser `def combine(a, b):`, cualquier otro archivo del sistema que llame a `combine(1, 2, 3)` pasándole tres argumentos posicionales fallará inmediatamente en ejecución con **`TypeError: combine() takes 2 positional arguments but 3 were given`** (o romperá el polimorfismo si era un método que sobrescribía una interfaz base o un *callback*). Una transformación que solo mira el AST local de una función no conoce los puntos de llamada (*call sites*) del resto del programa.
* **Por qué eliminar *Redundant Assertions* (`assert 1 == 1`) a ciegas es peligroso:** si un test tiene `assert True` o `assert 1 == 1`, suele ser un *placeholder* incompleto que dejó el programador para recordar qué debía verificar. Si un transformador lo borra silenciosamente, deja el test sin aserciones (en verde falso) y **destruye la señal de alerta** sin que el humano escriba la aserción real que faltaba.

---

## Preguntas de repaso

> [!question]- En `XTransformer` y `PrintArgumentsTransformer`, ¿por qué la llamada `ast.Call(func=Name(id='print', ...), ...)` debe envolverse dentro de un nodo `ast.Expr(value=...)` antes de insertarse en `node.body`?
> Porque en la gramática del AST de Python `node.body` es una lista de **sentencias (*statements*)**, mientras que `ast.Call` es una **expresión (*expression*)**. Cuando una expresión como `print(...)` se escribe sola en una línea como instrucción independiente, Python la envuelve obligatoriamente en un nodo sentencia `ast.Expr`.

> [!question]- ¿Por qué `RemoveUnusedArgumentsTransformer` funciona en una sola pasada de `UsedNamesVisitor` precisamente gracias a que los parámetros en `def combine(a, b, c):` son nodos `ast.arg` y no `ast.Name`?
> Porque `UsedNamesVisitor` solo implementa `visit_Name`. Al recorrer el `FunctionDef`, ignora automáticamente los parámetros declarados en la firma (`node.args.args`, que son `ast.arg`) y solo registra los identificadores que efectivamente aparecen dentro del cuerpo (`node.body`, que sí son `ast.Name`).

> [!question]- Da dos ejemplos concretos en los que `RemoveUnusedArgumentsTransformer` rompa el comportamiento de un programa aunque el argumento eliminado realmente no se lea dentro del cuerpo de la función.
> 1. **Llamadas existentes:** cualquier llamada existente `combine(1, 2, 3)` lanzará un `TypeError` por exceso de argumentos.
> 2. **Polimorfismo / firmas de interfaz:** si el método implementa una firma requerida por una superclase, un *framework* o `sys.settrace(frame, event, arg)` (donde `arg` debe recibirse por contrato aunque no se use), quitarlo rompe la interfaz.
