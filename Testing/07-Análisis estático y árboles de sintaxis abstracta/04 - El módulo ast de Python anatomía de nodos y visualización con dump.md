---
ramo: "Testing"
tema: "Análisis estático y árboles de sintaxis abstracta"
tags:
  - testing/analisis-estatico-y-arboles-de-sintaxis-abstracta
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/02 - Construcción de MiniScheme modelo de nodos parser e intérprete eval|Construcción de MiniScheme modelo de nodos parser e intérprete eval]]"
---

# El módulo ast de Python: anatomía de nodos y visualización con dump

## De MiniScheme a Python real: `ast.parse`, `ast.dump` y `ast.unparse`

Todo lo que programamos a mano en MiniScheme ya viene incluido de fábrica en la librería estándar de Python dentro del módulo `ast` (*Abstract Syntax Trees*). Sus tres funciones esenciales (además de `inspect.getsource(fn)` cuando queremos extraer el código fuente de una función ya cargada en memoria) son:

1. **`ast.parse(source)`:** recibe un `str` con código Python válido, ejecuta el análisis léxico y sintáctico y retorna el nodo raíz del árbol (un objeto `ast.Module`).
2. **`ast.dump(tree, indent=2)`:** devuelve un `str` legible que muestra todos los nodos y atributos internos del árbol (el equivalente a nuestro `pretty_print()`).
3. **`ast.unparse(tree)`:** hace el camino inverso: recibe un nodo AST y reconstruye el código fuente Python equivalente como texto (disponible desde Python 3.9).

Veamos qué árbol genera `ast.parse("2 + 3")`:

```python
import ast
tree = ast.parse("2 + 3")
print(ast.dump(tree, indent=2))
```

```python
Module(
  body=[
    Expr(
      value=BinOp(
        left=Constant(value=2),
        op=Add(),
        right=Constant(value=3)))])
```

Léelo de adentro hacia afuera: igual que nuestro `AdditionNode`, hay un `BinOp` con `left=Constant(value=2)`, `op=Add()` y `right=Constant(value=3)`. La única diferencia es que Python envuelve las expresiones sueltas dentro de una sentencia `Expr`, y todas las sentencias del archivo viven en la lista `body` del nodo raíz `Module`.

---

## Mapa de supervivencia de los nodos del AST de Python

En las pruebas escritas y de programación de reglas o transformaciones, casi todos los problemas giran en torno a diez clases de nodos del módulo `ast`. Conocer los nombres exactos de sus atributos es indispensable:

| Construcción en Python | Clase en `ast` | Atributos principales del nodo |
| :--- | :--- | :--- |
| Archivo o bloque raíz | `ast.Module` | `body` (lista de sentencias del programa) |
| Literal (`5`, `'hola'`, `True`, `None`) | `ast.Constant` | `value` (el dato literal en sí: `5`, `'hola'`, `True`, `None`) |
| Variable (`x`, `contador`) | `ast.Name` | `id` (string con el nombre, ej. `'x'`), `ctx` (`ast.Load()` si se lee o `ast.Store()` si se asigna) |
| Atributo (`self.x`, `obj.val`) | `ast.Attribute` | `value` (el objeto a la izquierda del punto, ej. `Name(id='self')`), `attr` (string con el nombre del atributo, ej. `'x'`), `ctx` |
| Operación binaria (`a + b`) | `ast.BinOp` | `left`, `op` (`ast.Add`, `ast.Sub`, `ast.Mult`, `ast.Div`), `right` |
| Operación booleana (`a and b`) | `ast.BoolOp` | `op` (`ast.And`, `ast.Or`), `values` (lista de operandos: `[a, b, ...]`) |
| Comparación (`x == 10`) | `ast.Compare` | `left` (primer operando `x`), `ops` (lista de operadores: `[ast.Eq()]`, `NotEq`, `Lt`, `Gt`, `Is`), `comparators` (lista de operandos derechos: `[Constant(10)]`) |
| Asignación (`x = expr`) | `ast.Assign` | `targets` (lista de destinos a la izquierda del `=`, ej. `[Name(id='x', ctx=Store())]`), `value` (expresión a la derecha) |
| Llamada (`foo(a, b)`) | `ast.Call` | `func` (`Name(id='foo')` o `Attribute(value=..., attr=...)`), `args` (lista de expresiones pasadas como argumentos posicionales), `keywords` |
| Condicional (`if c: ... else: ...`) | `ast.If` | `test` (la condición `c`), `body` (lista de sentencias del bloque `if`), `orelse` (lista de sentencias del bloque `else` o `elif`) |
| Definición de función (`def f(a, b):`) | `ast.FunctionDef` | `name` (string `'f'`), `args` (`ast.arguments`, cuya lista `args.args` contiene nodos `ast.arg` con atributo `.arg`), `body` (lista de sentencias) |
| Definición de clase (`class C:`) | `ast.ClassDef` | `name` (string `'C'`), `bases`, `body` (lista de métodos y atributos de la clase) |

---

## Dos detalles críticos que suelen ser trampa de prueba

1. **El contexto `ctx` en `ast.Name` (`Store` frente a `Load`):**
   Cuando escribes `contador = contador + 1`, el identificador `'contador'` aparece dos veces en el árbol como un nodo `ast.Name(id='contador')`. ¿Cómo sabemos cuál se está sobrescribiendo y cuál se está leyendo? Por su atributo `node.ctx`:
   * A la izquierda del `=` (en `Assign.targets`), tiene `ctx=ast.Store()`.
   * A la derecha del `=` (dentro del `BinOp`), tiene `ctx=ast.Load()`.
2. **Los parámetros de una función NO son nodos `ast.Name`, sino `ast.arg`:**
   En el encabezado `def sumar(x, y):`, los parámetros `x` e `y` dentro de `node.args.args` son instancias de **`ast.arg`** (cuyo nombre se guarda en `param.arg`, por ejemplo `param.arg == 'x'`). En cambio, cuando `x` e `y` se usan **adentro del cuerpo** (`return x + y`), ahí sí son nodos **`ast.Name`** (cuyo nombre se guarda en `nodo.id`). Confundir `ast.arg` con `ast.Name` es uno de los errores más preguntados en la Interrogación 2.

---

---

## Ejemplo práctico: leer el AST de una función completa

Veamos el árbol de una función con asignación, condicional y retornos:

```python
import ast

codigo = """
def sumar(x, y):
    total = x + y
    if total > 10:
        return total
    return 0
"""
print(ast.dump(ast.parse(codigo), indent=2))
```

(En versiones recientes de Python `ast.dump` omite campos vacíos como `decorator_list=[]`; en versiones anteriores verás algunos más.)

```
Module(
  body=[
    FunctionDef(
      name='sumar',
      args=arguments(
        args=[
          arg(arg='x'),
          arg(arg='y')]),
      body=[
        Assign(
          targets=[
            Name(id='total', ctx=Store())],
          value=BinOp(
            left=Name(id='x', ctx=Load()),
            op=Add(),
            right=Name(id='y', ctx=Load()))),
        If(
          test=Compare(
            left=Name(id='total', ctx=Load()),
            ops=[
              Gt()],
            comparators=[
              Constant(value=10)]),
          body=[
            Return(
              value=Name(id='total', ctx=Load()))]),
        Return(
          value=Constant(value=0))])])
```

### Cómo leerlo

* `FunctionDef` tiene `name='sumar'` y sus parámetros son `arg(arg='x')` y `arg(arg='y')`, **no** `Name`.
* `total = x + y`: el destino `total` es `Name(..., ctx=Store())`, y `x`, `y` dentro del `BinOp` son `Load()`.
* `total > 10` es un `Compare` con `left=Name(total)`, `ops=[Gt()]` y `comparators=[Constant(10)]`: por eso la comparación guarda *listas*, para soportar `a < b < c`.
* El `if` no tiene `else`, así que `orelse` está vacío (y no aparece en el dump abreviado). El segundo `Return` es una sentencia del cuerpo de la función, **no** del `If`.

### Distinguir `Store` de `Load` en la práctica

```python
class Nombres(ast.NodeVisitor):
    def __init__(self):
        self.escritos, self.leidos = [], []

    def visit_Name(self, node):
        destino = self.escritos if isinstance(node.ctx, ast.Store) else self.leidos
        destino.append(node.id)

n = Nombres()
n.visit(ast.parse("total = 0\nfor i in range(3):\n    total = total + helper(i)\nprint(total)"))
print(n.escritos)     # ['total', 'i', 'total']
print(n.leidos)       # ['range', 'total', 'helper', 'i', 'print', 'total']
```

Fíjate en dos cosas: `range`, `helper` y `print` aparecen como `Name` leídos (en una llamada, `func` es un `Name` con `Load`), y la variable del `for` (`i`) cuenta como `Store`.

---

## Preguntas de repaso

> [!question]- En el AST de Python, ¿por qué en un nodo `ast.Compare` (como `a < b < c` o `x == 5`) los atributos `ops` y `comparators` son listas en lugar de un único operador y un único operando derecho?
> Porque Python permite **comparaciones encadenadas** en una sola expresión, como `0 <= x < 10`. En ese caso, `left` es `Constant(0)`, `ops` es la lista `[LtE(), Lt()]` y `comparators` es la lista `[Name(id='x'), Constant(10)]`. Incluso en una comparación simple `x == 5`, `node.ops[0]` es `Eq()` y `node.comparators[0]` es `Constant(5)`.

> [!question]- Si parseas la instrucción `total = precio + total`, ¿cuántos nodos `ast.Name` existen en el árbol y qué valor tienen sus atributos `id` y `ctx` en orden de aparición?
> Existen **tres** nodos `ast.Name`:
> 1. `Name(id='total', ctx=Store())` (dentro de `Assign.targets`, porque recibe el valor asignado).
> 2. `Name(id='precio', ctx=Load())` (hijo izquierdo de `BinOp`, porque se lee su valor).
> 3. `Name(id='total', ctx=Load())` (hijo derecho de `BinOp`, porque también se lee su valor actual antes de sumar).

> [!question]- ¿Qué diferencia hay en el AST de Python entre cómo se representa el parámetro `x` en la firma `def f(x):` y cómo se representa `x` en la línea `return x + 1` dentro de esa función?
> En la firma `def f(x):`, `x` se representa como un nodo **`ast.arg(arg='x')`** dentro de la lista `node.args.args` del `FunctionDef`. En cambio, dentro del cuerpo (`return x + 1`), `x` se representa como un nodo **`ast.Name(id='x', ctx=Load())`**.

> [!question]- ¿Cómo se representa `a < b < c` en el AST y por qué `Compare` usa listas?
> Es un único nodo `Compare(left=a, ops=[Lt(), Lt()], comparators=[b, c])`. Las listas existen porque Python permite encadenar comparaciones y cada operador se aplica entre el operando anterior y el siguiente; con una sola comparación (`x == 10`) las listas tienen un elemento.

> [!question]- Dado `self.balance += 5`, ¿qué nodo `ast` lo representa y con qué `ctx` aparece `balance`?
> Es un `AugAssign` cuyo `target` es `Attribute(value=Name(id='self'), attr='balance', ctx=Store())`, con `op=Add()` y `value=Constant(5)`. El `ctx` de `balance` es `Store` porque se está escribiendo (aunque, semánticamente, también se lee antes de sumar).
