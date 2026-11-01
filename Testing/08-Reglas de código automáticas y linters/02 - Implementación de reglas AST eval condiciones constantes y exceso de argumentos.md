---
ramo: "Testing"
tema: "Reglas de código automáticas y linters"
tags:
  - testing/reglas-de-codigo-automaticas-y-linters
  - origen/complemento
prerrequisitos:
  - "[[Testing/08-Reglas de código automáticas y linters/01 - Qué es un linter y arquitectura base con Warning Rule y WarningNodeVisitor|Qué es un linter y arquitectura base con Warning Rule y WarningNodeVisitor]]"
---

# Implementación de reglas AST: eval, condiciones constantes y exceso de argumentos

## El molde universal para programar cualquier regla

Con la arquitectura base lista, escribir una regla nueva consiste siempre en responder dos preguntas sobre el AST:
1. **¿Qué tipo de nodo representa la construcción que busco?** (Eso define qué método `visit_<Nodo>` sobrescribir en el `WarningNodeVisitor`).
2. **¿Qué condición sobre los atributos de ese nodo distingue el caso defectuoso del caso normal?** (Eso define el `if` antes de llamar a `self.add_warning(...)`, sin olvidar nunca `self.generic_visit(node)` al final).

Veamos cómo se aplica este molde en cuatro reglas fundamentales del curso.

---

## Regla 1: Prohibir el uso de `eval` (`EvalUsedRule`)

* **Problema que resuelve:** la función `eval("...")` ejecuta cualquier string como código Python. Si ese string viene de un usuario externo, permite inyección y ejecución remota de código.
* **Patrón en el AST:** una llamada a función es un nodo `ast.Call`. El objeto llamado está en `node.func`. Si se llamó directamente a `eval(...)`, `node.func` es un nodo `ast.Name` cuyo `id` es `'eval'`.

```python
class EvalVisitor(WarningNodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, Name) and node.func.id == "eval":
            self.add_warning("EvalWarning", node.lineno, "eval should not be used!!")
        self.generic_visit(node)  # ¡indispensable por si hay eval() dentro de foo(eval('2'))!

class EvalUsedRule(Rule):
    def analyze(self, tree):
        visitor = EvalVisitor()
        visitor.visit(tree)
        return visitor.detected_warnings()

    @classmethod
    def name(cls):
        return "eval-used"
```

> [!WARNING] ¿Por qué es obligatorio chequear `isinstance(node.func, Name)` antes de leer `node.func.id`?
> Porque no toda llamada en Python tiene un nombre simple a la izquierda del paréntesis. En una llamada a un método como `modelo.eval()` (muy común en PyTorch), `node.func` **no** es un `ast.Name`, sino un **`ast.Attribute(value=Name(id='modelo'), attr='eval')`**, que no posee el atributo `.id`. Si intentas evaluar `node.func.id == 'eval'` directamente sin `isinstance(node.func, Name)`, tu linter se caerá con un `AttributeError: 'Attribute' object has no attribute 'id'`.

---

## Regla 2: Condiciones constantes `if True:` (`AlwaysTrueIfRule`)

* **Problema que resuelve:** escribir `if True:` (o `if False:`) hace que la condición sea inútil o deje código muerto, casi siempre como resto olvidado de una sesión de depuración.
* **Patrón en el AST:** un condicional es un nodo `ast.If` y su expresión booleana vive en `node.test`. Buscamos cuándo `node.test` es un `ast.Constant` con `value is True` (o `value == True` cuidando que en Python `1 == True` es verdadero, por lo que `node.test.value is True` es aún más preciso).

```python
class AlwaysTrueIfVisitor(WarningNodeVisitor):
    def visit_If(self, node):
        if isinstance(node.test, Constant) and node.test.value is True:
            self.add_warning("AlwaysTrueIfWarning", node.lineno,
                             "this if does not have any sense!")
        self.generic_visit(node)
```

---

## Regla 3: Funciones con demasiados parámetros (`ManyArgumentsRule`)

* **Problema que resuelve:** una función que recibe más de un umbral razonable de parámetros (por ejemplo, `threshold = 6`) es difícil de leer, probar y mantener (*Long Parameter List*).
* **Patrón en el AST:** una función es un nodo `ast.FunctionDef`; sus parámetros posicionales están en la lista `node.args.args`.

```python
class ManyArgumentsVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.threshold = 6

    def visit_FunctionDef(self, node):
        if len(node.args.args) > self.threshold:
            self.add_warning("ManyArgumentsWarning", node.lineno,
                             f"function {node.name} defined with many arguments!")
        self.generic_visit(node)
```

---

## Regla 4: Funciones sin sentencia `return` (`MissingReturnRule`)

¿Cómo detectamos si una función `def f(...):` no contiene **ninguna** sentencia `return` en todo su cuerpo (incluyendo dentro de bloques `if` o bucles)? En vez de escribir métodos para cada estructura interna, podemos combinar `visit_FunctionDef` con **`ast.walk(node)`**, que recorre todos los nodos descendientes del subárbol de esa función:

```python
class MissingReturnVisitor(WarningNodeVisitor):
    def visit_FunctionDef(self, node):
        has_return = any(isinstance(child, Return) for child in walk(node))
        if not has_return:
            self.add_warning("MissingReturnWarning", node.lineno,
                             f"function {node.name} has no return statement")
        self.generic_visit(node)
```

---

---

## Ejemplo práctico: casos positivos y negativos de cada regla

Antes de confiar en una regla conviene probarla con entradas que la deben disparar y con entradas parecidas que **no**. Resultados reales de ejecutar las reglas sobre estos fragmentos:

| Regla | Fragmento | Resultado | Por qué |
| :--- | :--- | :---: | :--- |
| `EvalUsedRule` | `eval('2')` | 1 advertencia | `Call` con `func=Name('eval')` |
| `EvalUsedRule` | `foo(eval('2'))` | 1 advertencia | gracias a `generic_visit`, entra al argumento |
| `EvalUsedRule` | `modelo.eval()` | ninguna | `func` es `Attribute`, no `Name` |
| `AlwaysTrueIfRule` | `if True: pass` | 1 advertencia | `test` es `Constant(True)` |
| `AlwaysTrueIfRule` | `if 1: pass` | ninguna | `1 is True` es falso (`1` no es `True`) |
| `AlwaysTrueIfRule` | `if x: pass` | ninguna | `test` es `Name`, no `Constant` |
| `ManyArgumentsRule` | `def f(a, b, c, d, e, f): pass` ($6$ parámetros) | ninguna | `6 > 6` es falso |
| `ManyArgumentsRule` | `def f(a, b, c, d, e, f, g): pass` ($7$) | 1 advertencia | `7 > 6` |

La fila de `ManyArgumentsRule` con $6$ vs. $7$ parámetros es un **caso de valor límite**: la misma técnica de BVA del Tema 06 sirve para probar reglas de linter.

### Un falso negativo sutil en `MissingReturnRule`

`walk(node)` recorre **todos** los descendientes del `FunctionDef`, incluyendo funciones anidadas:

```python
def externa():
    def interna():
        return 1
    pass            # 'externa' nunca retorna
```

La regla no avisa para `externa`, porque encuentra el `return` de `interna` dentro del mismo `walk`. Es un falso negativo producido por no distinguir a quién pertenece cada `Return`. Para corregirlo habría que recorrer solo las sentencias propias de la función y detenerse en los `FunctionDef` anidados (la misma idea del Caso 3 de `NodeVisitor`).

---

## Preguntas de repaso

> [!question]- ¿Qué error en tiempo de ejecución ocurriría en `EvalVisitor.visit_Call` si escribiéramos `if node.func.id == 'eval':` sin verificar primero `isinstance(node.func, ast.Name)` al analizar el código `texto.strip()`?
> Lanzaría un **`AttributeError: 'Attribute' object has no attribute 'id'`**. En la llamada a método `texto.strip()`, el atributo `node.func` es un nodo `ast.Attribute(value=Name(id='texto'), attr='strip')`, donde el nombre del método se almacena en `.attr` y no en `.id`.

> [!question]- En `AlwaysTrueIfVisitor`, ¿por qué es más seguro escribir `isinstance(node.test, Constant) and node.test.value is True` que `node.test.value == True`?
> Porque en Python la clase `bool` es subclase de `int` y se cumple que `1 == True` y `1.0 == True`. Si el código analizado tiene `if 1:` (un entero constante), `node.test.value == True` daría `True`, mientras que el operador de identidad `node.test.value is True` verifica que el literal escrito en el código sea específicamente el booleano `True`.

> [!question]- Si combinas `[EvalUsedRule, AlwaysTrueIfRule, ManyArgumentsRule]` con `Linter.analyze_all` sobre una función `def foo(a, b, c, d, e, f, g):` (línea 1) que adentro tiene `if True:` (línea 2) y adentro `eval('x')` (línea 3), ¿por qué se detectan las tres advertencias si una está anidada dentro de la otra?
> Porque cada visitante es independiente y, además, en cada uno de sus métodos (`visit_FunctionDef`, `visit_If`, `visit_Call`) se invoca `self.generic_visit(node)`, permitiendo que el recorrido siga descendiendo hacia el interior de la función y del condicional.

> [!question]- Escribe tres fragmentos de código para probar `AlwaysTrueIfRule`: uno positivo, uno negativo cercano y uno que muestre su limitación.
> Positivo: `if True: pass`. Negativo cercano: `if x: pass` (o `if 1: pass`, que la regla no detecta porque `1 is True` es falso). Limitación: `if not False: pass` o `if 1 == 1: pass`, que son siempre verdaderos pero no son un `Constant(True)`, por lo que la regla no los ve (falsos negativos).

> [!question]- ¿Por qué `ManyArgumentsVisitor` usa `node.args.args` y qué parámetros se le escapan?
> `node.args.args` contiene solo los parámetros posicionales normales. No incluye `*args`, `**kwargs` (`vararg` y `kwarg`), los parámetros de solo palabra clave (`kwonlyargs`) ni los de solo posición (`posonlyargs`), por lo que una función con muchos de esos tipos no dispararía la regla.
