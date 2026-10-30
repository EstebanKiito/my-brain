---
ramo: "Testing"
tema: "Transformaciones de código con AST"
tags:
  - testing/transformaciones-de-codigo-con-ast
  - origen/complemento
prerrequisitos:
  - "[[Testing/09-Transformaciones de código con AST/01 - Transformación manual de árboles con match-case frente a NodeTransformer|Transformación manual de árboles con match-case frente a NodeTransformer]]"
---

# Mecánica de NodeTransformer, orden de recursión y fix_missing_locations

## Las cuatro cosas que puede retornar un método `visit_*` en `NodeTransformer`

A diferencia de `ast.NodeVisitor` (donde el valor de retorno de `visit_*` se ignora al recorrer los hijos), en **`ast.NodeTransformer`** el padre reemplaza a su hijo por **exactamente lo que retorne `visit_<Tipo>(self, node)`**. Existen cuatro retornos posibles y debes dominarlos todos:

| Qué retorna `visit_<Tipo>(self, node)` | Efecto en el árbol padre | Ejemplo de uso |
| :--- | :--- | :--- |
| **El mismo `node`** (intacto o mutado en sus atributos) | Conserva el nodo en su posición actual. | Cambiar `node.op = ast.Sub()` y hacer `return node`. |
| **Un nuevo nodo `ast.AST`** | Reemplaza por completo al nodo original por el nuevo nodo. | En `x + 0`, retornar `node.left` (`Name(id='x')`) en lugar del `BinOp`. |
| **`None`** | **Elimina el nodo** del árbol (si estaba en una lista como `body` o `args`, desaparece de la lista). | Eliminar llamadas a `print(...)` o métodos triviales retornando `None`. |
| **Una lista de nodos `[n1, n2, ...]`** | Cuando el nodo vive dentro de una lista de sentencias (como `body`), **desempaqueta (*splices*) la lista** en ese lugar, reemplazando $1$ nodo por $N$ nodos. | En `IfTrueTransformer`, retornar `return node.body` para quitar el `if True:` y subir sus sentencias al bloque exterior. |

> [!CAUTION] El error número uno en `NodeTransformer`: olvidar el `return node`
> En Python, toda función que termina sin sentencia `return` devuelve implícitamente **`None`**. En un `NodeTransformer`, devolver `None` significa **«borra este nodo del árbol»**. Si sobrescribes `visit_FunctionDef` o `visit_BinOp` y olvidas poner `return node` al final, ¡borrarás todas las funciones o expresiones del programa!

---

## Orden de recursión: por qué transformar de abajo hacia arriba (*bottom-up*)

Observa la pizarra y los diagramas de clase para transformar `2 + 3 + 4` (que el parser agrupa como `(2 + 3) + 4`):

![Pizarra de clases explicando que al visitar un operador binario en un transformer se parte desde abajo transformando primero los subárboles hijos](adjuntos/Pizarra%20de%20transformacion%20de%20suma%20a%20resta%20en%20AST.png)

![Árbol de sintaxis de la expresión 2 + 3 + 4 antes de aplicar el transformador](adjuntos/Ejemplo%20de%20CambiarSumaPorResta%20con%20NodeTransformer.png)

![Transformación paso a paso de abajo hacia arriba convirtiendo primero el subárbol 2 + 3 en 2 - 3 y luego la raíz en 2 - 3 - 4](adjuntos/Ejemplo%20de%20SimplificarSumaCero%20con%20NodeTransformer.png)

En casi todo `NodeTransformer`, la primera línea de tu método debe ser **`node = self.generic_visit(node)`**:
1. Primero desciende hasta las hojas y transforma los subárboles hijos (por ejemplo, convierte el hijo izquierdo `2 + 3` en `2 - 3`, o simplifica un `if True:` interno antes de evaluar el `if True:` externo).
2. Luego, cuando los hijos ya están limpios y transformados, evalúa e interviene el nodo padre actual.

---

## Pregunta clásica de interrogación: ¿para qué sirve `ast.fix_missing_locations(tree)`?

Cuando `ast.parse(source)` crea nodos a partir de un texto, anota automáticamente en cada nodo los atributos de posición en el archivo original: **`lineno`** (número de línea) y **`col_offset`** (columna).

Sin embargo, cuando nosotros **creamos nodos nuevos a mano** dentro de un `NodeTransformer` (por ejemplo, instanciando `ast.BinOp(...)`, `ast.Call(...)` o `ast.Constant(...)`), esos nodos recién fabricados **no tienen `lineno` ni `col_offset`**.

```python
arbol = ast.Expression(
    body=ast.BinOp(left=ast.Constant(value=1), op=ast.Add(), right=ast.Constant(value=2))
)
ast.fix_missing_locations(arbol)
codigo = compile(arbol, "<string>", "eval")
```

* **¿Qué hace `ast.fix_missing_locations(tree)`?** Recorre el AST y, cada vez que encuentra un nodo al que le faltan `lineno` o `col_offset`, **los rellena copiando las coordenadas de su nodo padre** (o poniéndolos en `1` y `0` si ya está en la raíz).
* **¿Por qué es indispensable?** Porque la función nativa **`compile(tree, ...)` exige que todos los nodos del AST tengan `lineno` y `col_offset`** (para poder generar *tracebacks* y reportar errores de ejecución en la línea correcta); si llamas a `compile()` sobre un árbol con nodos nuevos sin haber corrido `ast.fix_missing_locations(tree)` (o `ast.copy_location`), Python lanza un **`ValueError` o `TypeError: required field "lineno" missing from expr`**.

---

---

## Ejemplo práctico: los cuatro retornos en acción

Probamos cada posibilidad sobre un mismo programa:

```python
fuente = """def f(x):
    print('entrando')
    y = x + 1
    print('saliendo')
    return y
"""
```

**Retornar `None` elimina el nodo.** Quitamos las sentencias `print`:

```python
class QuitarPrints(ast.NodeTransformer):
    def visit_Expr(self, node):
        if (isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "print"):
            return None            # se borra de la lista 'body'
        return node

print(ast.unparse(QuitarPrints().visit(ast.parse(fuente))))
```

```
def f(x):
    y = x + 1
    return y
```

**Retornar una lista inserta varias sentencias en el lugar de una.** Después de cada asignación agregamos un `log(...)`:

```python
class LogDespuesDeAsignar(ast.NodeTransformer):
    def visit_Assign(self, node):
        aviso = ast.Expr(value=ast.Call(
            func=ast.Name(id="log", ctx=ast.Load()),
            args=[ast.Constant(value="asignado")], keywords=[]))
        return [node, aviso]

arbol = LogDespuesDeAsignar().visit(ast.parse("x = 1\ny = 2"))
ast.fix_missing_locations(arbol)
print(ast.unparse(arbol))
```

```
x = 1
log('asignado')
y = 2
log('asignado')
```

**Olvidar el `return` rompe el árbol.** Un transformador con `self.generic_visit(node)` pero sin `return node`:

```python
class Olvido(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)       # falta: return node

print(ast.unparse(Olvido().visit(ast.parse("def f(x):\n    y = x + 1\n    return y"))))
```

```
AttributeError: 'Assign' object has no attribute 'value'
```

Como `visit_BinOp` devuelve `None`, el `BinOp` (`x + 1`) se **elimina** del atributo `value` del `Assign`, que queda sin valor y hace fallar a `ast.unparse`. El error aparece lejos de su causa, por eso hay que revisar el `return` primero.

---

## Preguntas de repaso

> [!question]- ¿Qué ocurre si en un método `visit_If(self, node)` de un `ast.NodeTransformer` modificas `node.test`, pero olvidas escribir `return node` al final del método?
> Como en Python una función sin `return` devuelve `None`, `NodeTransformer` interpreta ese retorno como una orden de **eliminación** y borra el bloque `if` completo del árbol padre.

> [!question]- ¿Por qué es necesario llamar a `ast.fix_missing_locations(tree)` después de aplicar un `NodeTransformer` que inserta nodos creados manualmente y antes de invocar `compile(tree, filename, mode)`?
> Porque los nodos instanciados manualmente en memoria (como `ast.Call(...)` o `ast.Constant(...)`) carecen de los atributos de ubicación `lineno` y `col_offset` que `ast.parse` asigna normalmente. `ast.fix_missing_locations` recorre el árbol heredando esos atributos desde el nodo padre, evitando que `compile()` falle por falta de metadatos de línea.

> [!question]- ¿Cómo permite `ast.NodeTransformer` reemplazar una única sentencia (como `if True:`) por múltiples sentencias (todas las instrucciones que estaban dentro de su bloque `body`)?
> Retornando directamente una **lista de nodos** (`return node.body`). Cuando `NodeTransformer.generic_visit` recorre una lista de sentencias del padre (como `Module.body` o `FunctionDef.body`) y un método `visit_*` devuelve una `list`, extiende la lista nueva con todos sus elementos en vez de insertar una lista anidada.

> [!question]- Un transformador define `visit_Return(self, node)` y termina con `return None` explícito. ¿Qué le pasa a la función `def f(): return 5`?
> El nodo `Return` se elimina del cuerpo de la función, por lo que queda `def f():` sin sentencias, que `ast.unparse` imprime como un cuerpo vacío (código inválido que no se puede compilar). Si se quería quitar el `return` conviene reemplazarlo por `ast.Pass()`.

> [!question]- ¿En qué casos se necesita `fix_missing_locations` y en cuáles no?
> Se necesita cuando el transformador **crea nodos nuevos** (`ast.Call`, `ast.Expr`...), porque no tienen `lineno` ni `col_offset` y `compile` los exige. No hace falta si solo se **mutan atributos** de nodos existentes (como `node.op = ast.Sub()`) o se reutilizan nodos que ya traían posiciones.
