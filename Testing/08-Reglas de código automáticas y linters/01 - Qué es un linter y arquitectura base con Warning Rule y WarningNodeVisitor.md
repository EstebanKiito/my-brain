---
ramo: "Testing"
tema: "Reglas de código automáticas y linters"
tags:
  - testing/reglas-de-codigo-automaticas-y-linters
  - origen/complemento
prerrequisitos:
  - "[[Testing/07-Análisis estático y árboles de sintaxis abstracta/05 - Recorrido del AST con NodeVisitor y la importancia de generic_visit|Recorrido del AST con NodeVisitor y la importancia de generic_visit]]"
---

# Qué es un linter y arquitectura base con Warning, Rule y WarningNodeVisitor

## ¿Qué hace por dentro una herramienta como `ruff`, `flake8` o `pylint`?

Un **linter** es una herramienta de análisis estático automático que inspecciona el código fuente buscando posibles bugs, vulnerabilidades de seguridad, malas prácticas de mantenibilidad o violaciones de estilo **sin ejecutar ni una sola línea del programa**. Su nombre viene de *lint* (la pelusa que se pega a la ropa): así como un rodillo quita la pelusa de un abrigo, el linter barre el código antes de que llegue a un *Pull Request* o a producción.

Aunque herramientas industriales como `ruff`, `pylint` o `ESLint` aplican cientos de reglas en milisegundos, por dentro todas funcionan con el mismo principio que aprendimos en el Tema 07:
1. Parsean el texto del archivo a un **Árbol de Sintaxis Abstracta (AST)** una sola vez.
2. Ejecutan una colección de **reglas independientes**, donde cada regla es un `NodeVisitor` que busca una forma específica en el árbol y acumula advertencias (`Warning`).
3. Reúnen todas las advertencias detectadas, las ordenan por número de línea y se las muestran al programador.

---

## Las cuatro piezas de la arquitectura de nuestro Linter

Para que agregar una nueva regla sea tan limpio como crear una clase sin tocar el resto del sistema (principio Abierto/Cerrado), separamos la arquitectura del linter en cuatro clases que colaboran entre sí:

```
Linter.analyze_all([Regla1, Regla2], source)
   │
   ├──► 1. tree = ast.parse(source)
   ├──► 2. Para cada Rule:
   │         └──► instancia su WarningNodeVisitor
   │                   └──► recorre tree y acumula objetos Warning(name, line, desc)
   └──► 3. Ordena la lista global de Warning por línea (__lt__) y la retorna
```

### 1. `Warning`: representación de un hallazgo

Cada vez que una regla detecta un problema, crea un objeto `Warning` con el nombre de la advertencia, el número de línea (`node.lineno` en el AST) y una explicación. Observa por qué implementamos `__eq__` y `__lt__`:

```python
from ast import *

class Warning:
    def __init__(self, name, line, description):
        self.name = name
        self.lineNumber = line
        self.description = description

    def __str__(self):
        return f"[ Line {self.lineNumber} ] {self.name} - {self.description}"

    __repr__ = __str__

    def __eq__(self, other):
        # Permite comparar dos warnings en tests unitarios según su texto formateado
        return str(self) == str(other)

    def __lt__(self, other):
        # Permite que warnings.sort() ordene automáticamente de menor a mayor línea
        return self.lineNumber < other.lineNumber
```

### 2. `Rule`: la interfaz común de toda regla

Es la clase abstracta de la que hereda cualquier regla del linter. Obliga a definir un método `analyze(self, tree)` (que recibe el AST ya parseado y devuelve una lista de `Warning`) y un método de clase `name(cls)` con el identificador de la regla:

```python
class Rule:
    def analyze(self, tree):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError
```

### 3. `WarningNodeVisitor`: un `NodeVisitor` con memoria de advertencias

Como todas las reglas recorren el AST y guardan advertencias en una lista, evitamos repetir `self.warnings = []` creando una subclase intermedia de `ast.NodeVisitor`:

```python
class WarningNodeVisitor(NodeVisitor):
    def __init__(self):
        self.warnings = []

    def add_warning(self, name, line, description):
        self.warnings.append(Warning(name, line, description))

    def detected_warnings(self):
        return self.warnings
```

### 4. `Linter`: el orquestador central

Recibe una regla (`analyze`) o una lista de clases de reglas (`analyze_all`), parsea el código fuente una única vez, ejecuta cada regla sobre ese mismo árbol y devuelve todas las advertencias ordenadas cronológicamente por línea:

```python
class Linter:
    @classmethod
    def analyze(cls, rule, source):
        return cls.analyze_all([rule], source)

    @classmethod
    def analyze_all(cls, rules, source):
        tree = parse(source)
        warnings = []
        for ruleClass in rules:
            warnings.extend(ruleClass().analyze(tree))
        warnings.sort()
        return warnings
```

---

---

## Ejemplo práctico: correr cuatro reglas sobre un mismo archivo

Con las piezas de la arquitectura, analizamos un programa con varios problemas a la vez. El `Linter` parsea una sola vez, ejecuta cada regla y ordena por línea:

```python
fuente = """def procesar(a, b, c, d, e, f, g):
    if True:
        resultado = eval(a)
    print(resultado)

def sumar(x, y):
    return x + y
"""

reglas = [EvalUsedRule, AlwaysTrueIfRule, ManyArgumentsRule, MissingReturnRule]
for advertencia in Linter.analyze_all(reglas, fuente):
    print(advertencia)
```

Salida:

```
[ Line 1 ] ManyArgumentsWarning - function procesar defined with many arguments!
[ Line 1 ] MissingReturnWarning - function procesar has no return statement
[ Line 2 ] AlwaysTrueIfWarning - this if does not have any sense!
[ Line 3 ] EvalWarning - eval should not be used!!
```

Puntos para fijarse:

* `sumar` no genera advertencias: tiene $2$ parámetros y un `return`.
* Las dos advertencias de la línea $1$ conservan el orden en que se ejecutaron las reglas: `sort()` es estable y `__lt__` solo compara números de línea.
* **Agregar una regla nueva no obliga a tocar ni `Linter` ni las demás reglas**: basta una clase `Rule` más en la lista. Ese es el principio Abierto/Cerrado de la arquitectura.
* Cada regla recorre el **mismo** árbol ya parseado; parsear de nuevo por cada regla desperdiciaría tiempo.

---

## Preguntas de repaso

> [!question]- ¿Por qué `Linter.analyze_all(rules, source)` invoca `ast.parse(source)` afuera del bucle `for ruleClass in rules:` y qué ventaja tiene esto cuando un linter industrial aplica 200 reglas?
> Porque el **parsing de texto a AST es costoso**, pero ninguna regla de linter modifica el árbol (solo lo leen). Al parsear el código fuente una sola vez y pasarle la misma referencia `tree` a las 200 reglas, se evita re-tokenizar y re-construir el árbol 200 veces.

> [!question]- ¿Para qué sirve definir el método mágico `__lt__(self, other)` dentro de la clase `Warning`?
> Sirve para definir el criterio de ordenamiento natural («menor que») entre dos advertencias comparando `self.lineNumber < other.lineNumber`. Gracias a eso, cuando `Linter.analyze_all` reúne advertencias de distintas reglas y llama a `warnings.sort()`, la salida queda ordenada desde la primera hasta la última línea del archivo sin importar en qué orden se ejecutaron las reglas.

> [!question]- ¿Qué responsabilidades separa el diseño entre `Rule` y `WarningNodeVisitor`?
> `WarningNodeVisitor` se encarga específicamente del **recorrido del AST** (sobrescribiendo los métodos `visit_*` y llamando a `add_warning`), mientras que `Rule` actúa como la **fachada pública de la regla** ante el `Linter` (exponiendo `name()` y `analyze(tree)`), lo que permite incluso que una regla combine más de un visitante si lo necesita.

> [!question]- ¿Por qué `Warning` implementa `__lt__` y `__eq__`? ¿Para qué se usa cada uno?
> `__lt__` permite que `warnings.sort()` ordene los hallazgos por número de línea para mostrárselos al usuario en orden de lectura. `__eq__` compara dos advertencias por su texto formateado, lo que simplifica los tests unitarios del linter (`assertEqual` entre advertencias esperadas y obtenidas).

> [!question]- Quieres agregar la regla «prohibir `print`». ¿Qué clases debes crear y cuál nodo del AST buscas?
> Un `PrintVisitor(WarningNodeVisitor)` con `visit_Call` que compare `node.func.id == "print"` (previa verificación `isinstance(node.func, Name)`) y llame a `generic_visit`, más una `PrintUsedRule(Rule)` con `analyze` y `name`. No hace falta modificar `Linter` ni las demás reglas.
