---
ramo: "Testing"
tema: "Análisis estático y árboles de sintaxis abstracta"
tags:
  - testing/analisis-estatico-y-arboles-de-sintaxis-abstracta
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/03 - El patrón Visitor en MiniScheme y el doble despacho paso a paso|El patrón Visitor en MiniScheme y el doble despacho paso a paso]]"
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/04 - El módulo ast de Python anatomía de nodos y visualización con dump|El módulo ast de Python anatomía de nodos y visualización con dump]]"
---

# Recorrido del AST con NodeVisitor y la importancia de generic_visit

## ¿Cómo implementa Python el patrón Visitor en `ast.NodeVisitor`?

En el módulo `ast`, la clase base `ast.NodeVisitor` hace automáticamente el trabajo que en MiniScheme hacía `CodeVisitor`. Cuando llamas a `visitor.visit(node)`, internamente `NodeVisitor` ejecuta estas tres líneas:

```python
class NodeVisitor:
    def visit(self, node):
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)
```

Leámoslo con calma porque aquí está el secreto de todas las preguntas de prueba sobre `NodeVisitor`:
1. Toma el nombre exacto de la clase del nodo (por ejemplo, `'If'`, `'Call'`, `'Assign'` o `'Name'`) y busca en tu visitante si definiste un método llamado `visit_If`, `visit_Call`, etc.
2. **Si NO definiste ese método:** ejecuta por defecto **`self.generic_visit(node)`**, que recorre en orden todos los hijos del nodo llamando a `self.visit(hijo)` sobre cada uno.
3. **Si SÍ sobrescribiste `visit_<Tipo>(self, node)`:** Python ejecuta **únicamente tu método** y **NO llama automáticamente a `generic_visit(node)`**. Si dentro de tu método no llamas tú mismo a `self.generic_visit(node)` (o a `self.visit(...)` sobre los hijos que quieras explorar), **el recorrido se detiene en ese nodo y jamás baja a sus hijos**.

---

## El efecto de olvidar `self.generic_visit(node)` en nodos anidados

Observa qué ocurre cuando queremos contar cuántas llamadas a funciones (`ast.Call`) existen en la expresión anidada `code = "foo(bar(zoo(2)))"`. En el AST, `foo(...)` es un nodo `Call` cuyo argumento (`node.args[0]`) es otro nodo `Call` (`bar(...)`), cuyo argumento es a su vez el tercer `Call` (`zoo(2)`).

* Si en `visit_Call` incrementamos `self.counter += 1` pero **comentamos `self.generic_visit(node)`**, el visitante entra al nodo exterior `foo(...)`, suma `1`, y como no desciende a visitar sus argumentos (`node.args`), **nunca descubre `bar` ni `zoo`**: retorna `1`.
* Si **incluimos `self.generic_visit(node)`**, después de contar `foo` el visitante baja a sus hijos, encuentra `bar(zoo(2))`, suma el segundo, baja a sus hijos, encuentra `zoo(2)` y retorna el conteo real: **`3`**.

![Comparación en Colab donde DemoVisitor sin generic_visit cuenta solo 1 llamada en foo(bar(zoo(2)))](adjuntos/DemoVisitor%20sin%20generic_visit%20en%20llamadas%20anidadas.png)

![Comparación en Colab donde DemoVisitor con self.generic_visit(node) propaga el recorrido y cuenta las 3 llamadas](adjuntos/DemoVisitor%20con%20generic_visit%20contando%20tres%20llamadas.png)

---

## Análisis de preguntas clásicas de interrogación (`NodeVisitor`)

### Caso 1: Traza de `PrintNames` en asignaciones (`x = 1; y = x + 2`)

Considera el siguiente código y visitante:

```python
import ast

code = """
x = 1
y = x + 2
"""

class PrintNames(ast.NodeVisitor):
    def visit_Name(self, node):
        print(node.id)

PrintNames().visit(ast.parse(code))
```

* **¿Qué imprime exactamente al ejecutarse?** Imprime tres líneas: `x`, luego `y`, y luego `x`.
* **¿Por qué funciona aunque `visit_Name` no llame a `generic_visit`?**
  1. Como `PrintNames` no sobrescribe `visit_Module`, `visit_Assign` ni `visit_BinOp`, todos esos nodos superiores usan `generic_visit` por defecto y bajan por todo el árbol.
  2. En la primera sentencia `x = 1`, visita `targets[0]` (`Name(id='x')` $\to$ imprime `x`) y `value` (`Constant(1)` $\to$ no hace nada).
  3. En la segunda sentencia `y = x + 2`, visita `targets[0]` (`Name(id='y')` $\to$ imprime `y`) y luego `value`, que es `BinOp(left=Name(id='x'), op=Add(), right=Constant(2))`, visitando `Name(id='x')` ($\to$ imprime `x`). Como un nodo `ast.Name` es una hoja (no tiene expresiones hijas), no necesita `generic_visit`.

### Caso 2: La trampa de sobrescribir `visit_If` sin `generic_visit`

¿Qué imprime por consola el siguiente programa?

```python
import ast

code = """
if x > 0:
    print(x)
"""

class Visitor(ast.NodeVisitor):
    def visit_If(self, node):
        print("Found If")

    def visit_Call(self, node):
        print("Found Call")

Visitor().visit(ast.parse(code))
```

* **Respuesta exacta:** Imprime **únicamente `"Found If"`** (nunca imprime `"Found Call"`).
* **Explicación paso a paso:**
  1. `Visitor().visit(...)` comienza en la raíz `Module` y por defecto (`generic_visit`) visita su primer hijo en `body`, que es el nodo `ast.If`.
  2. Al visitar `ast.If`, despacha al método `visit_If`, el cual imprime `"Found If"`.
  3. Como `visit_If` **no llama a `self.generic_visit(node)`**, el visitante jamás recorre `node.test` (`x > 0`) ni las sentencias dentro de `node.body` (`print(x)`). Por lo tanto, el nodo `ast.Call` (`print(x)`) que vive dentro del cuerpo del `if` nunca es alcanzado.

### Caso 3: Cuándo NO usar `generic_visit` a propósito (funciones anidadas)

A veces queremos controlar manualmente qué hijos visitar. Por ejemplo, en `AuditorFunciones` queremos contar cuántos `return` pertenecen a una función `exterior(x)` **sin sumar por error los `return` de una función anidada `interior(y)`** declarada adentro de `exterior`. Para lograrlo, al contar retornos recorremos el cuerpo de la función pero, si encontramos otro nodo `FunctionDef` anidado, **no** descendemos dentro de él con el mismo contador, sino que le creamos su propio registro independiente.

---

## Preguntas de repaso

> [!question]- ¿Qué método ejecuta internamente `ast.NodeVisitor.visit(node)` cuando la subclase NO define un método `visit_<ClaseDelNodo>`, y qué ocurre cuando SÍ lo define?
> Cuando no existe `visit_<ClaseDelNodo>`, `getattr(self, method, self.generic_visit)` retorna y ejecuta **`self.generic_visit(node)`**, que visita recursivamente todos los nodos hijos. Cuando la subclase sí define `visit_<ClaseDelNodo>`, se ejecuta **únicamente ese método** y `generic_visit` deja de llamarse automáticamente para ese nodo.

> [!question]- En `ClassCounter(ast.NodeVisitor)`, si definimos `visit_ClassDef(self, node)` únicamente como `self.counter += 1` (sin `self.generic_visit(node)`), ¿para qué programas dará el resultado correcto y para qué programas fallará?
> Dará el resultado correcto cuando todas las clases estén declaradas en el nivel superior del módulo (o dentro de funciones si no se sobrescribe `visit_FunctionDef`). Sin embargo, **fallará cuando exista una clase anidada dentro de otra clase** (por ejemplo, `class Config:` dentro de `class Wallet:`), porque al entrar en `Wallet` sumará `1` y no bajará a su `body` para descubrir `Config`.

> [!question]- Si quieres escribir un visitante `NombresLeidos(ast.NodeVisitor)` que guarde en `self.nombres` únicamente las variables cuyo valor se lee en `resultado = precio * cantidad` (ignorando la variable asignada `resultado`), ¿qué condición debes verificar dentro de `visit_Name(self, node)`?
> Debes verificar que el contexto del nodo sea de carga: `if isinstance(node.ctx, ast.Load): self.nombres.append(node.id)`. Así ignoras `resultado` (que tiene `ctx=ast.Store()`) y guardas `['precio', 'cantidad']`.

