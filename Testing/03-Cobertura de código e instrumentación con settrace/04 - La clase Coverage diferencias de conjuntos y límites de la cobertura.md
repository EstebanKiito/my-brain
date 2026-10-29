---
ramo: "Testing"
tema: "Cobertura de código e instrumentación con settrace"
tags:
  - testing/cobertura-de-codigo-e-instrumentacion-con-settrace
  - origen/complemento
prerrequisitos:
  - "[[02 - Cobertura de sentencias frente a cobertura de ramas]]"
  - "[[03 - Rastreo de ejecución en Python con sys settrace y frames de pila]]"
  - "[[Programación Avanzada/01-Repaso y POO básica/09 - Context manager y archivos en memoria|Context manager y archivos en memoria]]"
---

# La clase Coverage, diferencias de conjuntos y límites de la cobertura

## Encapsulando el rastreo en un *Context Manager*: la clase `Coverage`

Tener que llamar manualmente a `sys.settrace(traceit)` y recordar apagarlo con `sys.settrace(None)` usando variables globales es propenso a errores (especialmente si la función bajo prueba lanza una excepción y el código salta antes de llegar al `sys.settrace(None)`). La solución elegante en Python es encapsular el rastreo en una clase **`Coverage`** que implemente el protocolo de **administrador de contexto** (`__enter__` y `__exit__`, visto en [[Programación Avanzada/01-Repaso y POO básica/09 - Context manager y archivos en memoria|Context manager y archivos en memoria]]):

```python
import sys

class Coverage:
    """Registra las líneas ejecutadas durante un bloque `with`."""
    def __init__(self, func_name=None):
        self._trace = []
        self.func_name = func_name

    def traceit(self, frame, event, arg):
        if event == 'line':
            if self.func_name is None or frame.f_code.co_name == self.func_name:
                # Si filtramos por func_name guardamos lineno; si es general, (co_name, lineno)
                item = frame.f_lineno if self.func_name else (frame.f_code.co_name, frame.f_lineno)
                self._trace.append(item)
        return self.traceit

    def __enter__(self):
        self.original_trace = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        sys.settrace(self.original_trace)

    def coverage(self):
        return set(self._trace)
```

Observa las dos variantes vistas en el curso:
* **En los apuntes del libro (`Coverage("cgi_decode")`):** recibe el nombre de la función objetivo para filtrar `frame.f_code.co_name == self.func_name` y devuelve un conjunto de enteros `{3, 4, 5, ..., 11, ...}`.
* **En las láminas y *The Fuzzing Book* (`Coverage()`):** no filtra por nombre y guarda tuplas `(function_name, lineno)` como `{('cgi_decode', 20), ...}`, lo que permite rastrear programas que llaman a múltiples funciones auxiliares.

---

## Álgebra de conjuntos sobre la cobertura

Al representar `cov.coverage()` como un `set` de Python, podemos usar las operaciones matemáticas de conjuntos para diagnosticar y mejorar nuestras suites de pruebas:

### 1. Diferencia entre dos pruebas ($A - B$)

![Comparación de cobertura restando el conjunto de líneas de dos casos de prueba distintos](adjuntos/Diferencia%20de%20cobertura%20entre%20dos%20casos%20de%20prueba.png)

Si ejecutamos `cgi_decode("a+b")` bajo `cov_plus` y `cgi_decode("abc")` bajo `cov_abc`, la resta de conjuntos `cov_plus.coverage() - cov_abc.coverage()` devuelve `{11}` (o `{('cgi_decode', 20)}` según la numeración del archivo). Esto significa exactamente que **esa línea (`t += ' '`) fue ejecutada por la entrada `"a+b"`, pero NO fue ejecutada por `"abc"`**.

### 2. Diferencia contra la cobertura máxima ($\text{Total} - \text{Actual}$)

![Cálculo de las líneas que faltan por probar restando contra el coverage máximo](adjuntos/Diferencia%20contra%20la%20cobertura%20máxima%20en%20cgi_decode.png)

Si conocemos el conjunto total de líneas ejecutables `cov_max.coverage()` (por ejemplo, uniendo las $4$ pruebas que ejercitan todas las ramas de `cgi_decode`), la resta `cov_max.coverage() - cov_plus.coverage()` nos entrega la **lista exacta de tareas pendientes**: todas las líneas de código que nuestra prueba actual aún no ha tocado. Asimismo, la cobertura acumulada de una suite de $k$ pruebas es la **unión** $C_{\text{suite}} = C_1 \cup C_2 \cup \dots \cup C_k$.

---

## Los cuatro límites fundamentales de la cobertura y predicción con IA

Como enfatiza el epígrafe del capítulo: *«La cobertura te dice qué código no probaste. No te dice que el código que probaste esté bien»*. Todos sus límites nacen de que **la cobertura mide ejecución, no verificación**:

1. **$100\%$ de cobertura sin oráculo tiene poder de detección nulo:** si llamamos a `dias_en_mes(mes, anio)` con entradas para febrero bisiesto secular ($2000$), secular no bisiesto ($1900$), bisiesto normal ($2020$), febrero normal ($2021$), mes de $30$ días ($4$), mes de $31$ días ($1$) y mes inválido ($0$), alcanzamos **$100\%$ de *statement coverage***. Pero si no escribimos ningún `assert` que compare el retorno contra el oráculo (o si la función devolviera `99` en lugar de `29` para el año $2000$), la cobertura sigue siendo $100\%$ mientras el bug pasa intacto.
2. **Ocultamiento de ramas:** un *statement coverage* alto puede esconder ramas `False` nunca tomadas en condicionales sin `else`.
3. **Ceguera ante errores de omisión:** no detecta requerimientos que nunca fueron codificados.
4. **Ley de Goodhart en CI:** cuando un equipo impone un porcentaje de cobertura como meta burocrática, los programadores (o los LLMs) tienden a escribir tests sin `assert` significativos solo para inflar el número.

### Investigación reciente: ¿pueden los LLMs y el Machine Learning predecir la cobertura?

En el cierre de la unidad analizamos tres estudios recientes sobre predicción estática sin ejecutar el código:
* **CodePilot (Dhulipala et al., FORGE 2024):** al pedirle a un LLM que prediga qué líneas cubrirá un test sin ejecutarlo, usar *prompting* guiado por planificación paso a paso (*PA-based planning* sobre `if-else` y ciclos) eleva el *statement-match* de GPT-3.5 hasta un $89\%$ (y $55\%$ de *exact-match*), aunque sigue lejos de reemplazar a `sys.settrace`.
* **Predicción de veredicto (Hora, FSE 2024):** GPT-4 logra un $81\%$ de *accuracy* ($88.8\%$ precisión, $71\%$ *recall*) adivinando si un test de la librería estándar de Python pasará o fallará sin ejecutarlo, pero su eficacia cae drásticamente a medida que aumenta la complejidad del test.
* **Refined Code Coverage (Brandt & Ramírez, ICST 2025):** clasificadores clásicos de Machine Learning (como *Random Forest* sobre métricas del método y del AST) predicen con hasta $90\%$ de *accuracy* qué líneas merecen ser cubiertas, descubriendo que el contexto del método pesa más que la línea aislada.

---

## Preguntas de repaso

> [!question]- Se ejecuta `with Coverage("cgi_decode") as cov_1: cgi_decode("a+b")` y luego `with Coverage("cgi_decode") as cov_2: cgi_decode("abc")`. Si `cov_1.coverage() - cov_2.coverage()` entrega `{11}`, ¿qué significa exactamente ese resultado?
> Significa que la línea $11$ de `cgi_decode` (la asignación `t += ' '` dentro del `if c == '+':`) fue **ejecutada durante la llamada con `"a+b"`, pero no fue ejecutada durante la llamada con `"abc"`**. Es la definición matemática de la diferencia de conjuntos $A \setminus B = \{x \in A \mid x \notin B\}$.

> [!question]- ¿Por qué el método `__exit__` de la clase `Coverage` restaura `sys.settrace(self.original_trace)` en lugar de poner simplemente `sys.settrace(None)`?
> Porque permite anidar bloques `with Coverage()` o convivir con depuradores externos sin romperlos: al entrar en `__enter__` guardamos cualquier rastreador previo que estuviera activo (`sys.gettrace()`), y al salir en `__exit__` dejamos el entorno exactamente como estaba antes (que será `None` si no había otro rastreador, o el rastreador externo si existía). Además, `__exit__` se ejecuta siempre, incluso si la función bajo prueba lanza un `ValueError`.

> [!question]- En la función `dias_en_mes(mes, anio)`, ¿qué conjunto mínimo de llamadas necesitas para cubrir el $100\%$ de las líneas ejecutables, y por qué cubrirlas todas sin `assert` no detectaría si la línea del año divisible por $400$ devolviera `28` en vez de `29`?
> Se necesitan $7$ llamadas que ejerciten cada `return` y el `raise`: por ejemplo `(0, 2020)` para el `ValueError`, `(2, 2000)` para `anio % 400 == 0`, `(2, 1900)` para `anio % 100 == 0`, `(2, 2020)` para `anio % 4 == 0`, `(2, 2021)` para febrero no bisiesto, `(4, 2021)` para meses de $30$ días y `(1, 2021)` para meses de $31$ días. Si solo ejecutamos esas llamadas sin comparar su retorno contra un oráculo (`assertEqual`), `sys.settrace` registrará que la línea del `return` se ejecutó ($100\%$ de cobertura), pero nadie verificará que el número retornado era incorrecto.

