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
