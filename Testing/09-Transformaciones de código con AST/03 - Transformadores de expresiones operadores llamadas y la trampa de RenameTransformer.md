---
ramo: "Testing"
tema: "Transformaciones de código con AST"
tags:
  - testing/transformaciones-de-codigo-con-ast
  - origen/complemento
prerrequisitos:
  - "[[Testing/09-Transformaciones de código con AST/02 - Mecánica de NodeTransformer orden de recursión y fix_missing_locations|Mecánica de NodeTransformer orden de recursión y fix_missing_locations]]"
---

# Transformadores de expresiones: operadores, llamadas y la trampa de RenameTransformer

## 1. Simplificación algebraica: `SimplificarSumaCero` (Pregunta de Interrogación 2)

Un ejercicio clásico de la pauta de preparación para la Interrogación 2 pide implementar una clase `SimplificarSumaCero(ast.NodeTransformer)` que simplifique cualquier suma donde uno de los operandos sea el literal entero `0`:
* `x + 0` $\to$ `x`
* `0 + x` $\to$ `x`
* `(x + 0) + 0` $\to$ `x` (sumas anidadas)

¿Por qué el caso anidado `(x + 0) + 0` funciona sin esfuerzo adicional si llamamos a `node = self.generic_visit(node)` **al principio** de `visit_BinOp`?
1. En la raíz `(x + 0) + 0`, antes de mirar si el operando izquierdo es `0`, `self.generic_visit(node)` baja al hijo izquierdo `x + 0` y lo simplifica, devolviendo el nodo `Name(id='x')`.
2. De vuelta en la raíz, el árbol ahora es `x + 0`. Nuestro `if` detecta que `node.right` es `Constant(0)` y devuelve `node.left` (`x`).

```python
import ast

class SimplificarSumaCero(ast.NodeTransformer):
    def visit_BinOp(self, node):
        # 1. Transformamos primero los subárboles izquierdo y derecho (bottom-up)
        node = self.generic_visit(node)

        # 2. Si es una suma (+), revisamos si alguno de los lados es el entero 0
        if isinstance(node.op, ast.Add):
            if (isinstance(node.right, ast.Constant)
                    and type(node.right.value) is int and node.right.value == 0):
                return node.left
            if (isinstance(node.left, ast.Constant)
                    and type(node.left.value) is int and node.left.value == 0):
                return node.right
        return node
```

*(Nota: usamos `type(val) is int` o `isinstance(val, int) and not isinstance(val, bool)` porque en Python `False == 0` es `True` y `isinstance(False, int)` también es `True`, por lo que sin ese cuidado simplificaríamos erróneamente `x + False`!).*

---

## 2. Simplificación de comparaciones (`== True`, `== False`, `== None`) y `eval`

Veamos tres transformadores directos que corrigen automáticamente las advertencias que nuestro Linter detectaba en el Tema 08:

### A. `SimplificarBooleanos`: `var == True` $\to$ `var` y `var == False` $\to$ `not var`

```python
class SimplificarBooleanos(ast.NodeTransformer):
    def visit_Compare(self, nodo):
        nodo = self.generic_visit(nodo)
        match nodo:
            case ast.Compare(left=izq, ops=[ast.Eq()], comparators=[ast.Constant(value=True)]):
                return izq
            case ast.Compare(left=izq, ops=[ast.Eq()], comparators=[ast.Constant(value=False)]):
                return ast.UnaryOp(op=ast.Not(), operand=izq)
        return nodo
```

### B. `CompareNoneToIsTransformer`: `x == None` $\to$ `x is None`

```python
class CompareNoneToIsTransformer(ast.NodeTransformer):
    def visit_Compare(self, node):
        node = self.generic_visit(node)
        if (len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq)
                and isinstance(node.comparators[0], ast.Constant)
                and node.comparators[0].value is None):
            node.ops[0] = ast.Is()
        return node
```

### C. `LiteralEvalTransformer`: `eval('1 + 2')` $\to$ `ast.literal_eval('1 + 2')`

Reemplaza la llamada insegura `eval(...)` cambiando el `node.func` de un `Name(id='eval')` a un nodo `Attribute` que representa `ast.literal_eval`:

```python
class LiteralEvalTransformer(ast.NodeTransformer):
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == "eval":
            node.func = ast.Attribute(
                value=ast.Name(id="ast", ctx=ast.Load()),
                attr="literal_eval",
                ctx=ast.Load()
            )
        return node
```

---

## 3. La trampa mortal de `RenameTransformer` (Pregunta de Interrogación 2)

En la Clase 17 de preparación para la Interrogación 2 se presenta el siguiente código y se pregunta: **¿Cómo queda el código transformado y qué ocurre al intentar ejecutar `f(3)`?**

```python
import ast

code = """
def f(x):
    return x + 1
"""

class RenameTransformer(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id == "x":
            return ast.copy_location(ast.Name(id="y", ctx=node.ctx), node)
        return node

tree = ast.parse(code)
new_tree = RenameTransformer().visit(tree)
```

* **¿Cómo queda el código regenerado (`ast.unparse(new_tree)`)?** `def f(x): return y + 1`.
* **¿Por qué cambió el cuerpo `return y + 1` pero NO cambió el parámetro `def f(x):`, y qué pasa al ejecutar `f(3)`?**
  1. En el AST de Python, dentro del cuerpo `return x + 1`, la variable `x` es efectivamente un nodo **`ast.Name(id='x', ctx=Load())`**, por lo que `visit_Name` se activa y la reemplaza por `Name(id='y')`.
  2. Sin embargo, en el encabezado de la función `def f(x):`, el parámetro `x` dentro de `node.args.args` **NO es un nodo `ast.Name`, sino un nodo `ast.arg(arg='x')`**.
  3. Como `RenameTransformer` solo sobrescribió `visit_Name` y no sobrescribió **`visit_arg`**, la firma de la función sigue recibiendo el parámetro `x`, pero el cuerpo ahora intenta leer una variable inexistente `y`. Al ejecutar `f(3)`, el programa lanza un **`NameError: name 'y' is not defined`**.
* **¿Cómo se corrige `RenameTransformer`?** Agregando el método `visit_arg`:
  ```python
  def visit_arg(self, node):
      if node.arg == "x":
          node.arg = "y"
      return node
  ```

---

## Preguntas de repaso

> [!question]- En `SimplificarSumaCero`, ¿qué devolvería el transformador para la expresión anidada `(x + 0) + 0` si olvidáramos escribir `node = self.generic_visit(node)` al inicio de `visit_BinOp`?
> Devolvería **`x + 0`** (simplificando solo el nivel exterior). Al no llamar primero a `self.generic_visit(node)`, el nodo raíz ve que su hijo derecho es `0` y retorna directamente su hijo izquierdo sin haberlo visitado ni transformado (`x + 0`).

> [!question]- ¿Por qué al transformar `var == False` en `SimplificarBooleanos` no podemos escribir simplemente `return not izq` dentro de `visit_Compare`, sino que debemos retornar `ast.UnaryOp(op=ast.Not(), operand=izq)`?
> Porque en Python `izq` es un objeto nodo del AST (por ejemplo, una instancia de `ast.Name`), y para cualquier objeto existe el valor de verdad `bool(izq) == True`, de modo que evaluar `not izq` en Python devuelve el booleano `False` en vez de un nodo del AST. Para construir la expresión `not var` dentro del árbol debemos instanciar un nodo `ast.UnaryOp` con operador `ast.Not()`.

> [!question]- Explica por qué un `NodeTransformer` que solo implementa `visit_Name` para renombrar `x` a `y` rompe la función `def f(x): return x + 1` produciendo un `NameError` en tiempo de ejecución.
> Porque en el AST de Python los parámetros declarados en la firma de una función (`def f(x):`) se representan mediante nodos **`ast.arg`** (con atributo `.arg`), no mediante `ast.Name`. En consecuencia, `visit_Name` renombra el uso de `x` a `y` en el `return`, pero deja el parámetro como `x` en la firma, haciendo que `y` no esté definida al llamar a `f`.
