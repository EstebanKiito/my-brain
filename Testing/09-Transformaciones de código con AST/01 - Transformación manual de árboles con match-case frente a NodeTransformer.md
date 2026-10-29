---
ramo: "Testing"
tema: "Transformaciones de código con AST"
tags:
  - testing/transformaciones-de-codigo-con-ast
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/04 - El módulo ast de Python anatomía de nodos y visualización con dump|El módulo ast de Python anatomía de nodos y visualización con dump]]"
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/05 - Recorrido del AST con NodeVisitor y la importancia de generic_visit|Recorrido del AST con NodeVisitor y la importancia de generic_visit]]"
---

# Transformación manual de árboles con match-case frente a NodeTransformer

## De diagnosticar el código a reescribirlo automáticamente

En los Temas 07 y 08 usamos el AST de manera pasiva: recorríamos el árbol con `ast.NodeVisitor` para contar estructuras o emitir advertencias (`Warning`). Pero el AST es una estructura de datos mutable en memoria: **podemos reemplazar un nodo por otro, borrarlo o inyectar sentencias nuevas**, y luego convertir el árbol modificado de vuelta a texto con `ast.unparse(tree)` o compilarlo con `compile(tree, ...)`.

Esa es la diferencia entre un linter que te avisa de un problema y el botón *Quick Fix* de tu IDE (o `ruff --fix`) que lo corrige automáticamente por ti.

---

## El patrón `match-case` de Python (Structural Pattern Matching)

Antes de usar `NodeTransformer`, es muy útil conocer la sentencia **`match-case`** (introducida en Python 3.10), porque permite inspeccionar qué clase tiene un objeto y extraer sus atributos internos en una sola línea, como si fuera una mezcla entre una expresión regular estructural y un `if/elif`:

```python
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

def clasificar(f):
    match f:
        case Fraccion(num=0, den=_):
            return "es cero"
        case Fraccion(num=n, den=1):
            return f"es el entero {n}"
        case Fraccion(num=n, den=d) if n == d:
            return "es igual a 1"
        case Fraccion(num=n, den=d):
            return f"es {n}/{d}"
```

Observa cómo `case Fraccion(num=n, den=d) if n == d:` verifica simultáneamente tres cosas: que `f` sea instancia de `Fraccion`, captura sus atributos `num` y `den` en las variables locales `n` y `d`, y evalúa la guarda condicional `if n == d`.

---

## Transformar un AST manualmente con `match-case` y su limitación

Supongamos que queremos cambiar todas las sumas (`+`) por restas (`-`) en una expresión aritmética como `"(1 + 2) + (3 + 4)"`. Podemos escribir una función recursiva con `match-case`:

```python
import ast

def cambiar_suma_por_resta(nodo):
    match nodo:
        case ast.BinOp(left=izq, op=ast.Add(), right=der):
            return ast.BinOp(
                left=cambiar_suma_por_resta(izq),
                op=ast.Sub(),
                right=cambiar_suma_por_resta(der)
            )
        case ast.BinOp(left=izq, op=op, right=der):
            return ast.BinOp(
                left=cambiar_suma_por_resta(izq),
                op=op,
                right=cambiar_suma_por_resta(der)
            )
        case ast.Constant():
            return nodo

arbol = ast.parse("(1 + 2) + (3 + 4)", mode="eval")
nuevo = cambiar_suma_por_resta(arbol.body)
ast.fix_missing_locations(nuevo)
print(ast.unparse(nuevo))  # Imprime: (1 - 2) - (3 - 4)
```

### ¿Por qué este enfoque manual no escala a programas reales?

¿Qué pasa si ahora le pasamos la expresión `"(1 + eval(2 + 3)) + (3 + 4)"` a `cambiar_suma_por_resta`?
* El subárbol izquierdo tiene un nodo `ast.Call` (`eval(2 + 3)`), y adentro de sus argumentos (`args[0]`) hay una suma `2 + 3`.
* Como nuestra función `match-case` solo definió casos para `ast.BinOp` y `ast.Constant`, cuando se topa con `ast.Call` no entra en ningún `case` y devuelve `None`, rompiendo el árbol (o ignorando la suma que vive adentro de `eval(...)`).
* Para que una función manual recorra cualquier programa Python real, tendríamos que escribir más de cien bloques `case` para bajar por `Module`, `FunctionDef`, `If`, `Call`, `Assign`, `For`, `While`, etc.

### La solución: `ast.NodeTransformer`

La clase `ast.NodeTransformer` hereda de `ast.NodeVisitor` y nos regala el recorrido automático de los cien tipos de nodos de Python a través de `self.generic_visit(node)`:

```python
class CambiarSumaPorResta(ast.NodeTransformer):
    def visit_BinOp(self, nodo):
        nodo = self.generic_visit(nodo)  # 1. Transforma recursivamente cualquier hijo
        if isinstance(nodo.op, ast.Add):
            nodo.op = ast.Sub()          # 2. Cambia + por -
        return nodo                      # 3. ¡Obligatorio devolver el nodo!
```

Si ejecutamos `CambiarSumaPorResta().visit(ast.parse("(1 + eval(2 + 3)) + (3 + 4)", mode="eval"))`, como `generic_visit` sabe atravesar nodos `Call` aunque nosotros no hayamos escrito `visit_Call`, entra automáticamente a los argumentos de `eval` y devuelve `1 - eval(2 - 3) - (3 - 4)`. Incluso podemos combinar lo mejor de ambos mundos: **usar `NodeTransformer` para recorrer el árbol y usar `match-case` adentro de un método `visit_*` para reconocer patrones complejos**.

---

## Preguntas de repaso

> [!question]- ¿Qué ventaja fundamental ofrece heredar de `ast.NodeTransformer` frente a escribir una función recursiva propia con `match-case` para transformar un programa Python?
> Que `NodeTransformer` incluye `generic_visit(node)`, el cual sabe recorrer y reconstruir automáticamente todos los tipos de nodos de la gramática de Python (`Module`, `FunctionDef`, `Call`, `If`, `Assign`, etc.). Así solo necesitamos sobrescribir el método `visit_<Tipo>` del nodo específico que queremos alterar, incluso si aparece anidado dentro de llamadas o condicionales.

> [!question]-En el ejemplo `CambiarSumaPorResta`, ¿por qué también es posible implementarlo en dos líneas sobrescribiendo directamente `def visit_Add(self, nodo): return ast.Sub()`?
> Porque en el AST de Python el operador de un `BinOp` (`nodo.op`) es a su vez un nodo hijo del árbol (`ast.Add()`). Cuando `NodeTransformer` recorre por defecto el `BinOp` mediante `generic_visit`, visita `nodo.left`, `nodo.op` y `nodo.right`, reemplazando el nodo `ast.Add()` por el `ast.Sub()` retornado por `visit_Add`.

> [!question]- Al usar `match nodo:` en Python 3.10+, ¿qué diferencia hay entre escribir `case ast.BinOp(left=izq, op=ast.Add(), right=der):` y usar `isinstance` tradicional?
> El patrón `case` no solo comprueba que `nodo` sea un `ast.BinOp` y que su atributo `op` sea una instancia de `ast.Add`, sino que además **desestructura** el objeto en el mismo paso, asignando automáticamente `nodo.left` a la variable `izq` y `nodo.right` a la variable `der`.

