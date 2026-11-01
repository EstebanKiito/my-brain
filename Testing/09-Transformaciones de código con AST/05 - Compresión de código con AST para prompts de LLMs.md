---
ramo: "Testing"
tema: "Transformaciones de código con AST"
tags:
  - testing/transformaciones-de-codigo-con-ast
  - origen/complemento
prerrequisitos:
  - "[[Testing/09-Transformaciones de código con AST/04 - Transformadores de sentencias y funciones inyección de código y limpieza en dos pasadas|Transformadores de sentencias y funciones inyección de código y limpieza en dos pasadas]]"
---

# Compresión de código con AST para prompts de LLMs

## El problema del presupuesto de tokens al generar tests con IA

Cuando usamos un Modelo de Lenguaje (LLM) para generar pruebas unitarias sobre un sistema grande, enviar archivos enteros llenos de documentación extensa, comentarios, anotaciones de tipo y métodos accesorios consume miles de **tokens de contexto** (aumentando el costo y la latencia).

Esto plantea una pregunta de ingeniería fascinante: **¿cuánto código podemos podar programáticamente usando `ast.NodeTransformer` antes de que el LLM pierda contexto semántico y empiece a generar peores tests?**

> [!IMPORTANT] Lo que `ast.parse` + `ast.unparse` ya hace gratis
> Antes de medir cualquier transformación, recuerda que el simple hecho de pasar un archivo Python por `ast.unparse(ast.parse(source))` **elimina gratis todos los comentarios `# ...`, las líneas en blanco y el formato original**, porque el AST no almacena comentarios ni espacios decorativos. Por lo tanto, un compresor basado en AST debe atacar nodos reales del árbol.

---

## Tres transformadores de compresión sobre el AST

En el estudio práctico sobre `BillingService` ($251$ líneas, $2\,196$ tokens en su versión base `c0`), implementamos tres podas estructurales con `ast.NodeTransformer` cuidando una regla sintáctica vital de Python: **si al vaciar el `body` de una clase o función la lista `node.body` queda vacía (`[]`), es obligatorio insertar `[ast.Pass()]`** para que el código regenerado siga siendo sintácticamente válido.

### 1. `DocstringRemover` (`c1`): eliminar *docstrings* de módulos, clases y funciones

En el AST de Python, un *docstring* no es un comentario `#`, sino **el primer elemento de `node.body` (`node.body[0]`) cuando dicho elemento es un `ast.Expr` cuyo valor es un `ast.Constant` de tipo `str`** (detectable también con `ast.get_docstring(node) is not None`):

```python
class DocstringRemover(ast.NodeTransformer):
    def _quitar_docstring(self, node):
        self.generic_visit(node)
        if ast.get_docstring(node) is not None:
            node.body = node.body[1:] or [ast.Pass()]
        return node

    visit_Module = _quitar_docstring
    visit_ClassDef = _quitar_docstring
    visit_FunctionDef = _quitar_docstring
    visit_AsyncFunctionDef = _quitar_docstring
```

### 2. `TypeRemover` (`c2`): eliminar anotaciones de tipo en firmas y atributos

En Python, las anotaciones de tipo viven en tres lugares distintos del AST:
1. El tipo de retorno de una función (`def f() -> Invoice:`): atributo **`node.returns`** en `FunctionDef`.
2. El tipo de cada parámetro (`factura: Invoice`): atributo **`node.annotation`** en cada nodo `ast.arg`.
3. Las asignaciones anotadas (`MONTO: float = 1000.0` o `clock: Any`): son nodos **`ast.AnnAssign`**. Si tienen valor (`node.value is not None`), las convertimos en un `ast.Assign` normal (`MONTO = 1000.0`); si son solo declaraciones de tipo sin valor (`clock: Any`), retornamos `None` para borrarlas:

```python
class TypeRemover(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.returns = None
        return node

    def visit_arg(self, node):
        self.generic_visit(node)
        node.annotation = None
        return node

    def visit_AnnAssign(self, node):
        self.generic_visit(node)
        if node.value is not None:
            return ast.copy_location(ast.Assign(targets=[node.target], value=node.value), node)
        return None
```

### 3. `TrivialRemover` (`c3`): eliminar *getters* y *setters* de una sola línea

Identifica métodos `FunctionDef` que (descontando su *docstring*) tienen exactamente $1$ sentencia en su cuerpo: si empiezan con `get_` o `is_` y esa sentencia es un `ast.Return`, o empiezan con `set_` y es un `ast.Assign`, retorna `None` para eliminarlos.

---

## El *trade-off* empírico: ahorro de tokens frente a cobertura y *Mutation Score*

| Variante enviada al LLM | Tokens | Ahorro | Cobertura Stmt / Branch | Mutation Score | Tests válidos |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`c0` (código completo)** | $2\,196$ | $0.0\%$ | $100.0\% \;/\; 100.0\%$ | $85.0\%$ | $35 / 37$ ($2$ descartados) |
| **`c1` (sin *docstrings*)** | $1\,306$ | **$40.5\%$** | $100.0\% \;/\; 100.0\%$ | $87.6\%$ | $41 / 41$ ($0$ descartados) |
| **`c2` (sin tipos)** | $1\,911$ | $13.0\%$ | $100.0\% \;/\; 100.0\%$ | $87.6\%$ | $50 / 50$ ($0$ descartados) |
| **`c3` (sin *getters/setters*)** | $1\,873$ | $14.7\%$ | **$95.7\%$** $\;/\; 100.0\%$ | $88.5\%$ | $58 / 58$ ($0$ descartados) |
| **`c4` (`c1 + c2 + c3` en cadena)** | $1\,097$ | **$50.0\%$** | $95.7\% \;/\; 100.0\%$ | $87.6\%$ | $38 / 39$ ($1$ descartado) |

De este experimento se extraen cuatro lecciones clave:
1. **Compresión «gratis» (`c1` y `c2`):** quitar *docstrings* ahorró un **$40.5\%$ de los tokens** y quitar tipos ahorró un **$13.0\%$** sin perder absolutamente nada de cobertura ($100\%$) ni de *Mutation Score* ($\sim 87.6\%$), porque el LLM lee directamente las condiciones y operaciones del cuerpo de los métodos.
2. **El ahorro combinado (`c4`) no es aditivo:** sumar los ahorros individuales daría $40.5\% + 13.0\% + 14.7\% = 68.2\%$, pero `c4` ahorra un **$50.0\%$**, porque los *getters/setters* eliminados por `c3` ya contenían *docstrings* y anotaciones de tipo que se solapaban con `c1` y `c2`.
3. **Qué información es cara de quitar:** eliminar métodos de la interfaz (`c3`) redujo inmediatamente la cobertura de sentencias al $95.7\%$, porque el LLM desconoce que esos métodos existen y jamás genera pruebas que los invoquen.
4. **Tests descartados por falta de contexto:** cuando el *prompt* está muy comprimido (o cuando un *docstring* complejo no acompaña a reglas de negocio intrincadas como en `c4`), el LLM **inventa semántica** y genera tests cuyas aserciones fallan contra el código real. Esos tests deben descartarse antes de medir el *Mutation Score*, pues un test que ya falla sobre el código original mataría artificialmente a todos los mutantes.

---

---

## Ejemplo práctico: comprimir una clase pequeña y medir

Tomamos una clase con docstrings y tipos, y aplicamos `DocstringRemover` y `TypeRemover` en cadena:

```python
codigo = '''class Factura:
    """Representa una factura."""
    def total(self, impuesto: float) -> float:
        """Calcula el total con impuesto."""
        return self.monto * (1 + impuesto)
'''

arbol = ast.parse(codigo)
arbol = DocstringRemover().visit(arbol)
arbol = TypeRemover().visit(arbol)
print(ast.unparse(arbol))
```

```
class Factura:

    def total(self, impuesto):
        return self.monto * (1 + impuesto)
```

Medimos el largo en caracteres como aproximación al número de tokens:

| Variante | Caracteres | Ahorro |
| :--- | :---: | :---: |
| Original (tras `unparse`) | $184$ | $0\%$ |
| Sin docstrings (`c1`) | $105$ | $43\%$ |
| Sin tipos (`c2`) | $168$ | $9\%$ |
| `c1` + `c2` | $89$ | $52\%$ |

En esta clase minúscula, quitar docstrings ahorra más que quitar tipos, igual que en el estudio sobre `BillingService`. Los números exactos dependen del código, pero la jerarquía se repite: los docstrings son texto largo, mientras que los tipos son pocas palabras por firma.

### ¿Qué estamos perdiendo?

Con el docstring `"Calcula el total con impuesto."` el LLM sabe que `impuesto` es una fracción (por ejemplo, `0.19`) y no un porcentaje (`19`). Sin él debe inferirlo del código: `(1 + impuesto)` sugiere una fracción, pero en casos ambiguos podría inventar la regla de negocio. Es el mismo riesgo de «semántica inventada» que vimos con $S_2$ en el Tema 02.

---

## Preguntas de repaso

> [!question]- ¿Cómo se representa un *docstring* dentro del AST de Python y por qué es distinto de un comentario con `#`?
> Un comentario con `#` es descartado por el analizador léxico y no existe en el AST. En cambio, un *docstring* es una cadena literal que ocupa la primera posición (`node.body[0]`) de un `Module`, `ClassDef` o `FunctionDef` bajo la forma `ast.Expr(value=ast.Constant(value="..."))`.

> [!question]- Al implementar `DocstringRemover` o `TypeRemover`, ¿por qué es obligatorio verificar `if not node.body: node.body = [ast.Pass()]` después de eliminar nodos del cuerpo de una clase o función?
> Porque en la sintaxis de Python un bloque indentado (`class C:` o `def f():`) no puede tener cero sentencias. Si una clase solo contenía un *docstring* o declaraciones de atributos sin valor (`AnnAssign` con `value=None`), al eliminarlos `node.body` queda vacío (`[]`) y `ast.unparse` produciría código inválido si no se rellena con `ast.Pass()`.

> [!question]- ¿Por qué el porcentaje de tokens ahorrados al aplicar tres transformaciones en cadena (`c4`) es menor que la suma de los porcentajes ahorrados por cada transformación por separado (`c1 + c2 + c3`)?
> Porque las transformaciones tienen **intersección en los nodos que eliminan**: por ejemplo, cuando `TrivialRemover` (`c3`) borra un método *getter* completo, borra también su *docstring* (que contaba en `c1`) y las anotaciones de tipo de su firma (que contaban en `c2`).

> [!question]- Un equipo quiere reducir tokens antes de pedirle tests a un LLM, pero necesita que los tests respeten reglas de negocio documentadas en docstrings. ¿Qué compresión elegirías primero y cuál evitarías?
> Empezaría por quitar anotaciones de tipo y `getters`/`setters` triviales, que casi no contienen reglas de negocio, y evitaría `DocstringRemover` justamente porque los docstrings documentan esas reglas. Después mediría cobertura y *mutation score* del resultado para confirmar que no se perdió calidad.

> [!question]- ¿Por qué el ahorro de `c4` (todas las podas) es menor que la suma de los ahorros individuales?
> Porque las podas se solapan: al quitar docstrings ya se eliminó parte del texto de los métodos triviales que luego `TrivialRemover` elimina, así que ese mismo texto no puede ahorrarse dos veces. Los porcentajes se calculan sobre el código original de cada variante, no sobre el resultado de aplicar la anterior.
