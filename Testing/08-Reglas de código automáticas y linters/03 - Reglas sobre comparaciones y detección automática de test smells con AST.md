---
ramo: "Testing"
tema: "Reglas de código automáticas y linters"
tags:
  - testing/reglas-de-codigo-automaticas-y-linters
  - origen/complemento
prerrequisitos:
  - "[[Testing/02-Pruebas unitarias dobles de prueba y test smells/05 - Test smells y generación de pruebas unitarias con LLMs|Test smells y generación de pruebas unitarias con LLMs]]"
  - "[[Testing/08-Reglas de código automáticas y linters/02 - Implementación de reglas AST eval condiciones constantes y exceso de argumentos|Implementación de reglas AST eval condiciones constantes y exceso de argumentos]]"
---

# Reglas sobre comparaciones y detección automática de test smells con AST

## Reglas sobre comparaciones (`== None` y comparaciones booleanas redundantes)

Uno de los usos más frecuentes de los linters en Python (regla `E711` y `E712` en `flake8` / `ruff`) es detectar comparaciones mal escritas en nodos `ast.Compare`. Recuerda que un nodo `Compare` tiene tres atributos clave:
* `node.left`: la expresión a la izquierda (ej. `Name(id='x')`).
* `node.ops`: lista de operadores de comparación (ej. `[Eq()]`, `[NotEq()]`, `[Is()]`).
* `node.comparators`: lista de expresiones a la derecha (ej. `[Constant(value=None)]`).

### 1. Comparación con `None` usando `==` en vez de `is` (`CompareNoneRule`)

En Python, `None` es un objeto único (*singleton*) y cualquier clase puede sobrescribir `__eq__` haciendo que `x == None` sea lento o devuelva un resultado inesperado; por eso el estándar PEP 8 exige usar `x is None` o `x is not None`. ¿Cómo detectamos `x == None` o `None == x` en el AST?

```python
class CompareNoneVisitor(WarningNodeVisitor):
    def visit_Compare(self, node):
        # Chequeamos si hay un operador == (Eq) o != (NotEq)
        has_eq = any(isinstance(op, (Eq, NotEq)) for op in node.ops)
        # Chequeamos si alguno de los operandos (left o comparators) es Constant(None)
        operands = [node.left] + node.comparators
        has_none = any(isinstance(arg, Constant) and arg.value is None for arg in operands)
        if has_eq and has_none:
            self.add_warning("CompareNoneWarning", node.lineno,
                             "comparison to None should be 'is None', not '== None'")
        self.generic_visit(node)
```

Si la comparación es `x is None`, `node.ops[0]` es `ast.Is()`, por lo que `has_eq` es `False` y la regla no emite ninguna advertencia. Si es `x == 5`, `has_eq` es `True` pero `has_none` es `False`.

---

## Aplicando el Linter a las pruebas: detección automática de *Test Smells*

El código de nuestras pruebas unitarias (`test_*.py`) también es código fuente y sufre de problemas estructurales llamados **test smells** (Van Deursen et al., 2001). Como vimos en el Tema 02, los tests generados automáticamente (por ejemplo, por EvoSuite o por un LLM sin contexto) suelen estar plagados de *test smells* (Galindo-Gutiérrez et al., 2023). Con el módulo `ast`, podemos detectarlos automáticamente examinando cada método `FunctionDef` cuyo nombre empiece con `"test"`:

### 1. Detector de *Conditional Test Logic* (`if`, `for`, `while` dentro de un test)

Un test unitario debe ser una secuencia lineal y predecible (*Arrange, Act, Assert*). Si contiene un `if`, `for` o `while`, el camino que toma la prueba depende de la lógica interna del propio test:

```python
class ConditionalLogicDetector(NodeVisitor):
    def __init__(self):
        self.smelly_tests = []

    def visit_FunctionDef(self, node):
        if node.name.startswith("test"):
            for child in walk(node):
                if isinstance(child, (If, For, While)):
                    self.smelly_tests.append(node.name)
                    break
        self.generic_visit(node)
```

### 2. Detector de *Assertion Roulette* (múltiples aserciones sin mensaje)

Un método de test sufre de *Assertion Roulette* cuando tiene **más de una aserción sin mensaje explicativo**, dificultando saber cuál falló al mirar un reporte de integración continua. En `unittest`, métodos de un argumento como `self.assertTrue(x)` llevan mensaje si reciben $\ge 2$ argumentos (`len(node.args) >= 2` o `msg=` en `node.keywords`), y métodos de dos argumentos como `self.assertEqual(a, b)` llevan mensaje si reciben $\ge 3$ argumentos (`len(node.args) >= 3` o `msg=` en `node.keywords`). En un `assert x` nativo de Python (`ast.Assert`), el mensaje opcional vive en `node.msg`:

```python
class AssertionRouletteDetector(NodeVisitor):
    def __init__(self):
        self.smelly_tests = []

    def visit_FunctionDef(self, node):
        if node.name.startswith("test"):
            unexplained = 0
            for child in walk(node):
                # Caso 1: sentencia nativa 'assert cond, msg'
                if isinstance(child, Assert) and child.msg is None:
                    unexplained += 1
                # Caso 2: llamada self.assert*(...) en unittest
                elif (isinstance(child, Call) and isinstance(child.func, Attribute)
                      and child.func.attr.startswith("assert")):
                    has_kw_msg = any(kw.arg == "msg" for kw in child.keywords)
                    max_no_msg = 1 if child.func.attr in ("assertTrue", "assertFalse", "assertIsNone") else 2
                    if not has_kw_msg and len(child.args) <= max_no_msg:
                        unexplained += 1
            if unexplained > 1:
                self.smelly_tests.append(node.name)
        self.generic_visit(node)
```

Con la misma lógica se detecta un **test sin aserciones** (cuando el conteo total de nodos `Assert` o llamadas `self.assert*` dentro de `def test_...` es igual a `0`) o una **Redundant Assertion** (cuando un `assert` compara dos literales idénticos como `assert 1 == 1` o `self.assertTrue(True)`).

---

## Preguntas de repaso

> [!question]- En el AST de Python, ¿qué diferencia exacta hay entre los nodos generados por `x == None` y por `x is None`, y cómo los distingue `CompareNoneVisitor`?
> Ambos generan un nodo `ast.Compare` con `left=Name(id='x')` y `comparators=[Constant(value=None)]`. La única diferencia está en la lista `node.ops`: en `x == None` contiene una instancia de **`ast.Eq()`**, mientras que en `x is None` contiene una instancia de **`ast.Is()`**.

> [!question]- ¿Por qué `ConditionalLogicDetector` incluye un `break` apenas encuentra el primer nodo `(If, For, While)` dentro de `for child in walk(node):`?
> Porque una función de prueba como `def test_algo(self):` puede contener varios bucles o condicionales anidados; sin el `break`, el nombre del mismo método `test_algo` se agregaría repetidas veces a la lista `self.smelly_tests`.

> [!question]- En un nodo `ast.Assert` (correspondiente a la instrucción nativa `assert x > 0, "x debe ser positivo"`), ¿en qué atributos del nodo se almacenan la condición evaluada y el mensaje de error?
> La condición (`x > 0`) se almacena en **`node.test`** y el mensaje opcional (`"x debe ser positivo"`) se almacena en **`node.msg`** (que vale `None` cuando el programador escribió solo `assert x > 0` sin mensaje).
