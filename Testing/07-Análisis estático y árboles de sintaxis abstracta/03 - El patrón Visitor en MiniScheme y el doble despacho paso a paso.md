---
ramo: "Testing"
tema: "Análisis estático y árboles de sintaxis abstracta"
tags:
  - testing/analisis-estatico-y-arboles-de-sintaxis-abstracta
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/02 - Construcción de MiniScheme modelo de nodos parser e intérprete eval|Construcción de MiniScheme modelo de nodos parser e intérprete eval]]"
---

# El patrón Visitor en MiniScheme y el doble despacho paso a paso

## ¿Por qué no seguir metiendo métodos dentro de las clases de los nodos?

En la nota anterior pusimos `pretty_print()` y `eval()` directamente dentro de `NumberNode`, `AdditionNode`, etc. Pero ahora imagina que queremos escribir **diez análisis estáticos distintos**: uno que cuente cuántas sumas hay, otro que cuente cuántos números pares existen, otro que calcule la profundidad del árbol, otro que busque el patrón redundante `(if0 0 <e1> <e2>)`...

Si metiéramos un método nuevo dentro de cada clase del AST por cada análisis que se nos ocurra, terminaríamos contaminando `NumberNode`, `AdditionNode` e `If0Node` con decenas de métodos inconexos y tendríamos que editar todas las clases cada vez que inventemos una regla nueva (y cuando usemos el módulo `ast` de Python, ni siquiera somos dueños de sus clases para editarlas).

El **patrón de diseño Visitor** resuelve este problema: **separa la estructura de datos (los nodos del AST) de los algoritmos que operan sobre ella (los analizadores)**.

---

## La analogía del vendedor y el mecanismo de doble despacho (*double dispatch*)

Imagina a un inspector o vendedor (`visitor`) que va tocando las puertas de un edificio sin saber de antemano qué tipo de oficina hay detrás de cada puerta:

1. **Primera llamada (`node.accept(visitor)`):** nosotros le decimos al nodo raíz del árbol: *«recibe a este visitante»*.
2. **Segunda llamada (`visitor.visit_<tipo>(self)`):** el nodo abre la puerta y, como él sí sabe qué clase de nodo es, le dice al visitante exactamente qué método ejecutar pasándose a sí mismo como argumento (`self`). Por ejemplo, `NumberNode.accept(visitor)` ejecuta `visitor.visit_number(self)`, mientras que `AdditionNode.accept(visitor)` ejecuta `visitor.visit_addition(self)`.

A esta coreografía de dos llamadas encadenadas (`tree.accept(visitor)` $\to$ `visitor.visit_addition(tree)`) se le llama **doble despacho (*double dispatch*)**.

![Esquema en cuaderno del recorrido recursivo de accept(visitor) en un árbol de MiniScheme para contar nodos de suma](adjuntos/Recorrido%20de%20accept%20y%20visitor%20en%20MiniScheme.png)

### La clase base `CodeVisitor` (quién propaga la visita a los hijos)

Para no repetir el código que baja por las ramas en cada análisis nuevo, definimos una clase base `CodeVisitor` cuyos métodos recorren recursivamente los hijos de cada nodo compuesto:

```python
class CodeVisitor:
    def visit_number(self, node):
        pass  # hoja: no tiene hijos

    def visit_boolean(self, node):
        pass  # hoja: no tiene hijos

    def visit_addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_subtraction(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_equal(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_if0(self, node):
        node.condNode.accept(self)
        node.thenNode.accept(self)
        node.elseNode.accept(self)
```

---

## Cuatro visitantes concretos de examen en MiniScheme

Cualquier análisis estático ahora solo hereda de `CodeVisitor` y sobrescribe el método del nodo que le interesa, **recordando llamar a `super().visit_<tipo>(node)`** (o a `.accept(self)` en sus hijos) para no cortar el recorrido hacia abajo.

![Implementación de AdditionCounterVisitor en el notebook de clases propagando accept a leftNode y rightNode](adjuntos/Implementacion%20de%20AdditionCounterVisitor%20en%20MiniScheme.png)

### 1. Contador de sumas (`AdditionCounterVisitor`) y de números (`NumberCounterVisitor`)

```python
class AdditionCounterVisitor(CodeVisitor):
    def __init__(self):
        self.counter = 0

    def visit_addition(self, node):
        super().visit_addition(node)  # primero visita leftNode y rightNode
        self.counter += 1             # luego cuenta esta suma

class NumberCounterVisitor(CodeVisitor):
    def __init__(self):
        self.counter = 0

    def visit_number(self, node):
        self.counter += 1  # si solo pidieran números pares: if node.value % 2 == 0:
```

### 2. Detector de patrón estático (`If0ZeroVisitor`: contar `(if0 0 <e1> <e2>)`)

Supongamos que queremos detectar cuántas veces el programador escribió un condicional `if0` cuya condición es literalmente el número `0` (como en `(if0 0 2 3)`), pero **no** cuando la condición es una operación que da cero en ejecución como `(if0 (- 1 1) 2 3)`. Esto ilustra a la perfección qué ve un análisis estático:

```python
class If0ZeroVisitor(CodeVisitor):
    def __init__(self):
        self.counter = 0

    def visit_if0(self, node):
        if isinstance(node.condNode, NumberNode) and node.condNode.value == 0:
            self.counter += 1
        super().visit_if0(node)  # ¡crucial para encontrar otros if0 anidados adentro!
```

Si evaluamos `If0ZeroVisitor` sobre `(if0 (+ 1 1) (if0 0 2 3) (if0 1 4 (if0 (- 1 1) 2 3)))`, el visitante reporta exactamente **`1`**: solo el segundo `if0` tiene como `condNode` un `NumberNode(0)` literal; el cuarto tiene un `SubtractionNode` (`(- 1 1)`), que estáticamente no es un literal `0`.

### 3. Profundidad del árbol (`DepthVisitor`)

```python
class DepthVisitor(CodeVisitor):
    def visit_number(self, node):
        return 1
    def visit_addition(self, node):
        return 1 + max(node.leftNode.accept(self), node.rightNode.accept(self))
```

---

## Preguntas de repaso

> [!question]- En `AdditionCounterVisitor`, ¿qué ocurriría al analizar `"(+ 2 (+ 3 (+ 1 2)))"` si dentro de `visit_addition(self, node)` escribimos únicamente `self.counter += 1` y olvidamos llamar a `super().visit_addition(node)`?
> El contador devolvería **`1`** en lugar de **`3`**. Al sobrescribir `visit_addition` sin invocar a `super().visit_addition(node)` (ni a `node.leftNode.accept(self)` y `node.rightNode.accept(self)`), el visitante cuenta únicamente la raíz del árbol y jamás desciende a visitar los subárboles hijos.

> [!question]- ¿Por qué `If0ZeroVisitor` cuenta `1` y no `2` en la expresión `(if0 (+ 1 1) (if0 0 2 3) (if0 1 4 (if0 (- 1 1) 2 3)))`, si tanto `0` como `(- 1 1)` valen cero?
> Porque `If0ZeroVisitor` realiza **análisis estático estructural** sin ejecutar `eval()`: inspecciona si `node.condNode` es una instancia de `NumberNode` con `value == 0`. En `(if0 (- 1 1) 2 3)`, `condNode` es un objeto `SubtractionNode`, por lo que estáticamente no coincide con el patrón literal `(if0 0 ...)`.

> [!question]- Además de contar la primera instancia en `(if0 0 2 3)`, ¿por qué `If0ZeroVisitor` logra encontrar ese nodo si se encuentra dentro de la rama `thenNode` de un `if0` exterior cuya condición `(+ 1 1)` jamás sería `0` al ejecutarse?
> Porque `CodeVisitor.visit_if0` recorre **todas las ramas sintácticas del árbol** (`condNode`, `thenNode` y `elseNode`) sin importar qué valor tomaría la condición en tiempo de ejecución. Esa es justamente una ventaja clave del análisis estático: inspecciona ramas que en una prueba dinámica podrían no ejecutarse.
