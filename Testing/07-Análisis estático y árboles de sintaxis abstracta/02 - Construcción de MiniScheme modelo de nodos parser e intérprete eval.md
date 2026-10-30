---
ramo: "Testing"
tema: "Análisis estático y árboles de sintaxis abstracta"
tags:
  - testing/analisis-estatico-y-arboles-de-sintaxis-abstracta
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/01 - Análisis estático frente a dinámico y qué es un árbol de sintaxis abstracta|Análisis estático frente a dinámico y qué es un árbol de sintaxis abstracta]]"
  - "[[Programación Avanzada/01-Repaso y POO básica/06 - Clases, objetos y variables de clase|Clases, objetos y variables de clase]]"
---

# Construcción de MiniScheme: modelo de nodos, parser e intérprete eval

## Construir un mini-lenguaje antes de atacar Python

El módulo `ast` de Python tiene más de cien clases de nodos distintas. Para entender sin magia cómo nace un árbol de sintaxis abstracta, cómo se parsea desde un `str` y cómo se evalúa, construimos primero un lenguaje funcional en miniatura llamado **MiniScheme** (inspirado en *Programming Languages: Application and Interpretation* de Shriram Krishnamurthi).

MiniScheme utiliza **notación prefija** (como Lisp o Scheme): el operador se escribe justo después del paréntesis de apertura y antes de sus operandos, por ejemplo `(+ 2 3)` o `(+ 2 (+ 3 1))`. Su gramática completa (incluyendo las extensiones de booleanos, resta, igualdad y condicional `if0`) es:

```
<expr> ::= <number> | <boolean> (#t o #f)
         | (+ <expr> <expr>) | (- <expr> <expr>) | (= <expr> <expr>)
         | (if0 <expr> <expr> <expr>) -- si la 1ª expr da 0, evalúa la 2ª; si no, la 3ª
```

---

## Jerarquía orientada a objetos de los nodos del AST

En lugar de usar diccionarios o largos bloques de `if isinstance(...)`, aplicamos polimorfismo: **cada construcción de la gramática es una clase que hereda de `Node`** y sabe imprimirse (`print_tree`), evaluarse (`eval`) y aceptar un visitante (`accept`).

```python
class Node:
    def pretty_print(self): self.print_tree(0)
    def print_tree(self, level): pass
    def eval(self): pass
    def accept(self, visitor): pass

class LiteralNode(Node):
    def __init__(self, val): self.value = val
    def eval(self): return self.value
    def print_tree(self, level): print(" " * level + str(self.value))

class NumberNode(LiteralNode):
    def accept(self, visitor): return visitor.visit_number(self)

class BooleanNode(LiteralNode):
    def accept(self, visitor): return visitor.visit_boolean(self)
```

Para las operaciones compuestas definimos `BinaryOperatorNode` (con `leftNode` y `rightNode`) y el nodo ternario `If0Node` (`condNode`, `thenNode`, `elseNode`):

```python
class OperatorNode(Node):
    def __init__(self, sym): self.symbol = sym

class BinaryOperatorNode(OperatorNode):
    def __init__(self, leftNode, rightNode, sym):
        super().__init__(sym)
        self.leftNode = leftNode
        self.rightNode = rightNode
    def print_tree(self, level):
        print(" " * level + self.symbol)
        self.leftNode.print_tree(level + 1)
        self.rightNode.print_tree(level + 1)

class AdditionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode): super().__init__(leftNode, rightNode, "+")
    def eval(self): return self.leftNode.eval() + self.rightNode.eval()
    def accept(self, visitor): return visitor.visit_addition(self)

class SubtractionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode): super().__init__(leftNode, rightNode, "-")
    def eval(self): return self.leftNode.eval() - self.rightNode.eval()
    def accept(self, visitor): return visitor.visit_subtraction(self)

class EqualNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode): super().__init__(leftNode, rightNode, "=")
    def eval(self): return self.leftNode.eval() == self.rightNode.eval()
    def accept(self, visitor): return visitor.visit_equal(self)

class If0Node(OperatorNode):
    def __init__(self, condNode, thenNode, elseNode):
        super().__init__("if0")
        self.condNode, self.thenNode, self.elseNode = condNode, thenNode, elseNode
    def eval(self):
        return self.thenNode.eval() if self.condNode.eval() == 0 else self.elseNode.eval()
    def accept(self, visitor): return visitor.visit_if0(self)
```

---

## Cómo funciona el *parser* recursivo y `splitArgs`

¿Cómo convertimos el texto `"(+ 2 (+ 3 1))"` en objetos conectados en memoria? Si simplemente hiciéramos `.split(" ")` sobre el interior `"+ 2 (+ 3 1)"`, romperíamos la subexpresión anidada `(+ 3 1)` en pedazos sueltos. La clave de MiniScheme es la función `splitArgs(string)`, que lleva un contador de paréntesis abiertos (`open_counter`): **solo corta por un espacio `' '` cuando `open_counter == 0`** (es decir, en el nivel superior de la expresión actual).

![Esquema en cuaderno del parseo de una expresión prefija en su árbol con nodos izquierdo y derecho y llamadas recursivas](adjuntos/Esquema%20de%20parser%20y%20arbol%20recursivo%20en%20MiniScheme.png)

```python
def splitArgs(string):
    open_counter, temp, result = 0, "", []
    for key in string:
        if key == " " and open_counter == 0:
            result.append(temp.strip())
            temp = ""
        elif key == "(": open_counter += 1
        elif key == ")": open_counter -= 1
        temp += key
    result.append(temp.strip())
    return result

def parser(stringCode):
    if stringCode.isnumeric(): return NumberNode(int(stringCode))
    if stringCode in ("#t", "#f"): return BooleanNode(stringCode == "#t")
    if stringCode.startswith("(") and stringCode.endswith(")"):
        tokens = splitArgs(stringCode[1:-1])
        op = tokens.pop(0)
        if op == "+" and len(tokens) == 2: return AdditionNode(parser(tokens[0]), parser(tokens[1]))
        if op == "-" and len(tokens) == 2: return SubtractionNode(parser(tokens[0]), parser(tokens[1]))
        if op == "=" and len(tokens) == 2: return EqualNode(parser(tokens[0]), parser(tokens[1]))
        if op == "if0" and len(tokens) == 3: return If0Node(parser(tokens[0]), parser(tokens[1]), parser(tokens[2]))
    raise SyntaxError(f"Expresión no soportada: {stringCode}")
```

Observa cómo `If0Node.eval()` se comporta con pereza (*lazy evaluation*): evalúa primero `self.condNode.eval() == 0` y solo invoca `.eval()` sobre la rama elegida (`thenNode` o `elseNode`).

---

---

## Ejemplo práctico: construir, imprimir y evaluar un árbol a mano

Armamos con nuestras clases la expresión `(if0 (- 2 2) (+ 1 1) 9)` sin pasar por el parser:

```python
arbol = If0Node(
    SubtractionNode(NumberNode(2), NumberNode(2)),    # condición: (- 2 2)
    AdditionNode(NumberNode(1), NumberNode(1)),       # rama 'then': (+ 1 1)
    NumberNode(9),                                    # rama 'else': 9
)
arbol.pretty_print()
print(arbol.eval())
```

Salida:

```
if0
 -
  2
  2
 +
  1
  1
 9
2
```

### Cómo se evalúa (de abajo hacia arriba)

1. `SubtractionNode.eval()` calcula `2 - 2 = 0`.
2. `If0Node.eval()` compara la condición con `0`: es cierto, así que evalúa la rama `then`.
3. `AdditionNode.eval()` calcula `1 + 1 = 2`.
4. La rama `else` (`9`) **no se evalúa**: es un `if` de verdad, no una función que evalúe sus tres argumentos.

El `pretty_print` usa un espacio por nivel de profundidad, así que la sangría de cada línea es el nivel del nodo en el árbol: `if0` en el nivel $0$, `-` y `+` en el nivel $1$, y sus números en el nivel $2$.

### Ejercicios para hacer a mano

* `(+ (+ 1 2) (- 5 3))` → árbol con raíz `+`, hijos `+(1,2)` y `-(5,3)`; evalúa a $3 + 2 = 5$.
* `(if0 1 100 (+ 2 2))` → la condición vale $1 \ne 0$, así que se evalúa la rama `else` y resulta $4$.
* ¿Cuántos nodos tiene `(+ 2 (+ 3 1))`? $5$: dos `+` y tres números.

---

## Preguntas de repaso

> [!question]- ¿Por qué la función `splitArgs` en el parser de MiniScheme mantiene una variable `open_counter` en lugar de usar `string.split(' ')`?
> Porque los operandos de una expresión pueden ser a su vez subexpresiones compuestas con espacios internos, como `(+ 3 1)` dentro de `(+ 2 (+ 3 1))`. Al incrementar `open_counter` con `'('` y decrementarlo con `')'`, `splitArgs` garantiza que solo separa argumentos cuando encuentra un espacio en el nivel exterior (`open_counter == 0`), entregando `['+', '2', '(+ 3 1)']`.

> [!question]- Traza paso a paso qué árbol construye `parser("(if0 (- 4 4) (+ 10 5) 99)")` y qué devuelve su método `.eval()`.
> El nodo raíz es `If0Node` con tres hijos: `condNode = SubtractionNode(NumberNode(4), NumberNode(4))`, `thenNode = AdditionNode(NumberNode(10), NumberNode(5))` y `elseNode = NumberNode(99)`. Al llamar a `.eval()`, `condNode.eval()` calcula $4 - 4 = 0$; como es igual a `0`, evalúa `thenNode.eval()` y retorna `15` (sin llegar a evaluar `elseNode`).

> [!question]- ¿Qué ventaja de diseño ofrece que cada subclase (`NumberNode`, `AdditionNode`, `EqualNode`) implemente su propio método `eval()` frente a tener una única función global con múltiples `if isinstance(node, ...)`?
> Cumple el principio Abierto/Cerrado (polimorfismo): para agregar un nuevo operador al lenguaje (como `SubtractionNode` o `If0Node`) basta con crear una nueva subclase con su propio `eval()` y registrarla en el parser, sin modificar ni arriesgar romper la lógica de evaluación de los nodos existentes.

> [!question]- Dibuja el árbol de `(- (+ 4 1) (if0 0 3 7))` y evalúalo.
> Raíz `-` con hijos `+(4, 1)` e `if0(0, 3, 7)`. El primero vale $5$; el `if0` tiene condición $0$, así que evalúa la rama `then` y vale $3$. Resultado: $5 - 3 = 2$.

> [!question]- ¿Por qué `splitArgs` cuenta paréntesis abiertos en lugar de usar `split(" ")`?
> Porque un espacio solo separa argumentos cuando está **fuera** de cualquier paréntesis. En `+ 2 (+ 3 1)` hay un espacio dentro del segundo argumento, y un `split(" ")` ingenuo lo partiría en `"(+"`, `"3"` y `"1)"`. El contador `open_counter` lleva la cuenta de la profundidad para separar solo en el nivel $0$.
