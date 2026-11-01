---
ramo: "Testing"
tema: "Análisis estático y árboles de sintaxis abstracta"
tags:
  - testing/analisis-estatico-y-arboles-de-sintaxis-abstracta
  - origen/complemento
prerrequisitos:
  - "[[Testing/01-Fundamentos del testing de software/01 - Qué es el testing error defecto falla y el oráculo de prueba|Qué es el testing error defecto falla y el oráculo de prueba]]"
---

# Análisis estático frente a dinámico y qué es un árbol de sintaxis abstracta

## ¿Podemos encontrar defectos sin correr el programa ni una sola vez?

En las primeras seis unidades del curso, todas las técnicas tenían un requisito en común: **ejecutar el programa** con ciertas entradas y observar qué pasaba (sus retornos, excepciones o líneas visitadas). A ese enfoque se le llama **testing o análisis dinámico**.

Sin embargo, piensa en lo que hace tu editor de código (como VS Code o PyCharm) apenas terminas de escribir una línea: subraya una variable que nunca usaste, te advierte que escribiste `if x == True:` o te avisa de que una función recibe demasiados argumentos **antes siquiera de que presiones el botón Run**. A esa familia de técnicas que examinan el código fuente o intermedio sin ejecutarlo se le denomina **testing estático**, y se divide en dos ramas:

1. **Revisión manual:** inspecciones humanas sobre el código (*code reviews* en Pull Requests, *walkthroughs* o auditorías en equipo).
2. **Análisis estático automático:** herramientas (linters, *type checkers*, analizadores de seguridad SAST) que inspeccionan automáticamente el programa buscando patrones defectuosos o vulnerables.

| Dimensión | Análisis estático | Análisis dinámico |
| :--- | :--- | :--- |
| **¿Requiere ejecutar el código?** | No: examina la estructura del código fuente o *bytecode*. | Sí: corre el programa con entradas concretas. |
| **Momento de detección** | Muy temprano (mientras se programa o en cada *commit*). | Más tardío (requiere código ejecutable y casos de prueba). |
| **Alcance del análisis** | Cubre **todas las ramas sintácticas** del archivo a la vez, incluso las que rara vez se ejecutan. | Solo observa el **camino específico** que tomaron las entradas de prueba. |
| **Punto ciego principal** | No conoce los valores reales en tiempo de ejecución; sufre de **falsos positivos** y depende de la forma sintáctica. | No ve defectos en ramas no ejecutadas ni patrones de mala mantenibilidad si el resultado numérico coincide. |

---

## De texto plano a estructura: el *parsing* y el AST

¿Por qué un analizador estático no busca errores simplemente con expresiones regulares o ` string.find()` sobre el archivo `.py`? Imagina que quieres prohibir el uso de la función peligrosa `eval(...)`. Si buscas la subcadena `"eval("` en el texto plano, marcarás por error comentarios como `# nunca uses eval(x)` o textos dentro de un mensaje como `print("No llamar a eval(datos)")`.

Para razonar sobre un programa sin confundir comentarios, textos y código real, necesitamos pasar de la **sintaxis concreta** (el texto plano lleno de espacios, paréntesis, comas y saltos de línea) a la **sintaxis abstracta** (una estructura de datos jerárquica que captura el significado gramatical de cada construcción). Ese proceso se llama **parsing** y ocurre en dos etapas:

```
Texto fuente: "(+ 2 (+ 3 1))"
      │
      ▼  1. Análisis léxico (Tokenizer / Lexer)
Lista de tokens: ['(', '+', '2', '(', '+', '3', '1', ')', ')']
      │
      ▼  2. Análisis sintáctico (Parser)
Árbol de Sintaxis Abstracta (AST):
        AdditionNode(+)
         ├── leftNode: NumberNode(2)
         └── rightNode: AdditionNode(+)
                         ├── leftNode: NumberNode(3)
                         └── rightNode: NumberNode(1)
```

Un **Árbol de Sintaxis Abstracta (AST)** es un árbol donde cada **nodo interno** representa un operador, sentencia o declaración del lenguaje (una suma, un `if`, una definición de función) y cada **nodo hoja** representa un valor atómico o identificador (un número constante, un booleano o el nombre de una variable). Se llama «abstracto» porque descarta detalles puramente decorativos del texto (como los paréntesis o cuántos espacios dejaste alrededor del `+`), puesto que la jerarquía padre-hijo del árbol ya codifica sin ambigüedad qué operación se agrupa primero.

---

## Estructura frente a significado y los límites teóricos (Teorema de Rice)

Analizar el AST en lugar de ejecutar el programa tiene tres consecuencias fundamentales que siempre se evalúan en las interrogaciones:

1. **Dos programas con el mismo resultado pueden tener ASTs distintos:** en notación prefija, las expresiones `(+ 2 (+ 3 1))` y `(+ (+ 2 3) 1)` evalúan ambas a `6`. Sin embargo, la primera produce un árbol inclinado a la derecha (el hijo derecho de la raíz es otro `AdditionNode`), mientras que la segunda produce un árbol inclinado a la izquierda (el hijo izquierdo de la raíz es el `AdditionNode`). Un análisis estático mira la **estructura**, no el valor final.
2. **Ceguera ante valores de ejecución:** ante una división `x / y`, el AST solo ve un nodo de división entre dos variables `x` e `y`; en general no puede saber si en tiempo de ejecución el usuario ingresará `y = 0`.
3. **Indecidibilidad teórica (Teorema de Rice):** en ciencia de la computación, el Teorema de Rice demuestra que cualquier propiedad semántica no trivial sobre el comportamiento de un programa arbitrario (por ejemplo, «¿este programa terminará alguna vez o dividirá por cero?») es **indecidible** de forma exacta. Por eso todo analizador estático real trabaja con **aproximaciones conservadoras**, aceptando algunos falsos positivos (alarmas sobre código inofensivo) o falsos negativos a cambio de terminar en pocos segundos.

---

---

## Ejemplo práctico: por qué una expresión regular no basta para encontrar `eval`

Queremos contar las llamadas reales a `eval(...)` en este archivo:

```python
fuente = """# nunca uses eval(x)
print("no llames eval(x)")
resultado = eval(entrada)
evaluador = 5
"""
```

**Con una expresión regular:**

```python
import re
print(len(re.findall(r"eval\(", fuente)))      # 3
```

Encuentra $3$ coincidencias: el comentario, el texto dentro del `print` y la llamada real. Dos son **falsos positivos**.

**Con el AST:**

```python
import ast

class ContarEval(ast.NodeVisitor):
    def __init__(self):
        self.n = 0

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "eval":
            self.n += 1
        self.generic_visit(node)

v = ContarEval()
v.visit(ast.parse(fuente))
print(v.n)                                      # 1
```

El parser ya descartó comentarios y entiende que lo que va entre comillas es un `Constant`, no una llamada. Solo queda una `Call` cuyo `func` es `Name(id='eval')`. Ese es el valor de pasar de la sintaxis concreta a la estructura.

### Mismo resultado, distinto árbol

```python
ast.dump(ast.parse("2 + 3 + 4"))
ast.dump(ast.parse("2 + (3 + 4)"))
```

Ambos evalúan a $9$, pero el primero es `BinOp(BinOp(2, +, 3), +, 4)` (asociativo a la izquierda) y el segundo `BinOp(2, +, BinOp(3, +, 4))`. Un analizador que cuenta la forma del árbol los ve distintos aunque su significado sea el mismo.

---

## Preguntas de repaso

> [!question]- Da un ejemplo concreto de un defecto que el análisis estático detecta trivialmente pero el análisis dinámico no puede detectar, y otro ejemplo del caso inverso.
> * **Fácil para estático, invisible para dinámico:** código muerto o mantenibilidad, como una variable declarada y nunca leída (`temp = 5`), una comparación redundante (`if x == True:`) o un método de test sin aserciones (`assert`). Como no alteran el resultado ni lanzan excepciones, los tests dinámicos pasan en verde sin notarlo.
> * **Fácil para dinámico, invisible para estático puro de AST:** una división por cero o un desbordamiento cuyo denominador proviene de una petición externa o de un cálculo complejo en tiempo de ejecución (`return total / obtener_cantidad_usuarios_activos()`), donde la estructura sintáctica es perfectamente válida.

> [!question]- ¿Por qué las expresiones `(+ 2 (+ 3 1))` y `(+ (+ 2 3) 1)` son tratadas como programas diferentes por un analizador basado en AST a pesar de que ambas evalúan a `6`?
> Porque el AST representa la **estructura sintáctica** y el agrupamiento de las operaciones, no su resultado numérico: en `(+ 2 (+ 3 1))` el nodo raíz tiene como hijo izquierdo la hoja `2` y como hijo derecho una sub-suma `(+ 3 1)`, mientras que en `(+ (+ 2 3) 1)` el hijo izquierdo es la sub-suma `(+ 2 3)` y el hijo derecho es la hoja `1`.

> [!question]- ¿Qué establece el Teorema de Rice y qué compromiso práctico obliga a tomar al diseñar herramientas de análisis estático?
> Establece que toda propiedad semántica no trivial sobre lo que calcula un programa es indecidible en el caso general. En la práctica, esto obliga a los analizadores estáticos a verificar aproximaciones sintácticas sobre el AST, asumiendo un compromiso (*trade-off*) entre **falsos positivos** (advertir de un posible error que en ejecución nunca ocurre) y **falsos negativos** (dejar pasar un bug camuflado con otra forma sintáctica).

> [!question]- Un analizador estático avisa de una posible división por cero en `x / (a - b)`, pero en tu programa `a` y `b` nunca son iguales. ¿Qué tipo de resultado es y por qué ocurre?
> Es un **falso positivo**. El análisis estático ve solo la estructura (una división cuyo divisor es una resta) y no conoce los valores reales en ejecución, así que debe asumir que `a == b` es posible. Para evitar perder defectos reales, estas herramientas aceptan emitir avisos que a veces son infundados.

> [!question]- Menciona una ventaja y una limitación del análisis estático frente al dinámico, con un ejemplo de cada una.
> Ventaja: revisa **todas** las ramas del archivo sin ejecutarlas (por ejemplo, un `eval` dentro de un `else` que nunca se ejecuta en las pruebas). Limitación: no conoce los valores en tiempo de ejecución, por lo que no puede decidir con certeza si, por ejemplo, un índice quedará fuera de rango cuando depende de la entrada del usuario.
