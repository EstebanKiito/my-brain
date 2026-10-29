---
ramo: "Testing"
tema: "Ejecución simbólica y fuzzing concólico"
tags:
  - testing/ejecucion-simbolica-y-fuzzing-concolico
  - origen/complemento
prerrequisitos:
  - "[[Testing/11-Ejecución simbólica y fuzzing concólico/02 - Fuzzing simbólico manual construcción de caminos y ramas inalcanzables|Fuzzing simbólico manual construcción de caminos y ramas inalcanzables]]"
  - "[[Testing/11-Ejecución simbólica y fuzzing concólico/04 - Ejecución concólica ConcolicTracer y exploración negando restricciones|Ejecución concólica ConcolicTracer y exploración negando restricciones]]"
---

# Symbolic Fuzzing frente a Concolic Fuzzing, explosión de caminos y uso de LLMs

## Comparación directa: *Symbolic Fuzzing* frente a *Concolic Fuzzing* (Pregunta de Interrogación 2)

En la Clase 17 de preparación para la Interrogación 2 y en la Sección 13.5 del libro se exige comparar directamente ambas técnicas explicando sus diferencias, ventajas y limitaciones:

| Dimensión | *Concolic Fuzzing* (Concreto + Simbólico) | *Symbolic Fuzzing* (Ejecución Simbólica Pura) |
| :--- | :--- | :--- |
| **Punto de partida** | Requiere una **entrada concreta semilla (*seed*)** para ejecutar el programa de verdad. | Parte **directamente del código fuente** (sin ejecutarlo ni necesitar semillas previas). |
| **Cómo recolecta las restricciones** | **Dinámicamente** durante la ejecución concreta, usando objetos *proxy* (`zint`, `zstr`) y `ConcolicTracer`. | **Estáticamente** recorriendo el AST / CFG (`get_all_paths` + `extract_constraints`) antes de correr nada. |
| **Alcance de exploración** | Explora el camino ejecutado por la semilla y va descubriendo **caminos vecinos** al negar condiciones una a una. | Intenta enumerar y resolver **todos los caminos posibles** del programa hasta una profundidad fija (`max_depth`). |
| **Ventaja principal** | Siempre avanza y produce ejecuciones reales desde el segundo uno; si una función interna no es simbolizable, usa el valor concreto y sigue adelante. | Es **exhaustivo** hasta la profundidad dada y puede **demostrar formalmente que una rama es inalcanzable (`unsat`)** sin depender de la calidad de una semilla. |
| **Riesgo / Limitación principal** | Si la semilla inicial queda atrapada lejos de una región del programa o la instrumentación pierde el rastro, puede no alcanzar ramas lejanas. | Sufre de **explosión combinatoria de caminos (*path explosion*)** ante bucles o condicionales en cascada, y se rompe ante código que su traductor estático no soporta. |

---

## Los tres grandes límites: explosión de caminos, funciones opacas y `hash(x)`

Tanto el enfoque simbólico como el concólico enfrentan tres barreras fundamentales que debes saber argumentar:

1. **Explosión de caminos (*Path Explosion*):**
   Cada `if/else` secuencial duplica el número de caminos ($k$ condicionales producen $2^k$ caminos). Y si el programa contiene un bucle `while` o `for` cuya condición depende de la entrada simbólica, el número de caminos posibles se vuelve **astronómico o infinito** (un bucle de $100$ iteraciones con un `if` adentro genera $2^{100}$ caminos). Para no colgarse, las herramientas acotan la profundidad (`max_depth`), sacrificando completitud.
2. **Restricciones no lineales o funciones criptográficas (`if hash(x) == 0xCAFE:`):**
   Considera la pregunta crítica del Capítulo 13: ¿qué pasa frente a la condición `if sha256(x) == 0xCAFE...`?
   * Un *fuzzer* aleatorio tiene probabilidad prácticamente nula de acertar.
   * La ejecución simbólica y concólica intentarán plantear la ecuación $\text{sha256}(x) == \text{0xCAFE}$, pero las funciones de *hash* criptográfico están diseñadas matemáticamente para ser **no invertibles (funciones de un solo sentido)**. El *SMT Solver* (Z3) se estanca o agota su *timeout* porque la restricción es computacionalmente intratable.
3. **Llamadas opacas y entorno externo:**
   Si el código llama a una librería compilada en C, consulta una base de datos por red o lee la hora del sistema, el analizador simbólico no tiene su AST para extraer ecuaciones (aunque el enfoque concólico al menos puede reemplazar esa llamada por el valor concreto retornado durante la corrida).

---

## Disección experimental: *Fuzzer* Simbólico + Z3 frente a un LLM

Un generador simbólico realiza dos tareas distintas: **(1) Extraer** las restricciones de cada camino leyendo el código, y **(2) Resolver** cada conjunción de restricciones para hallar entradas concretas. Para saber en qué etapa conviene usar un LLM y en cuál un solver formal como Z3, diseñamos una **matriz experimental $2 \times 2$** sobre tres funciones (`apply_coupon` con $2$ caminos, `tarifa_noche` con $4$ y `puntaje_riesgo` con $8$, sumando $14$ caminos):

| Configuración | Etapa 1: ¿Quién extrae las restricciones? | Etapa 2: ¿Quién resuelve las ecuaciones? | ¿Para qué sirve en el experimento? |
| :---: | :---: | :---: | :--- |
| **A (Referencia)** | Fuzzer simbólico | **Z3** | Línea base formal ($100\%$ exacta si el código cumple el subconjunto soportado). |
| **B (Puro LLM)** | LLM | LLM | Evalúa al modelo haciendo todo el trabajo de principio a fin. |
| **C (Híbrido 1)** | **LLM** | **Z3** | Aísla la capacidad de **extracción** del LLM (si $C \gg B$, el LLM extrajo bien pero falló al calcular números; si $C$ falla, el LLM ya se había equivocado leyendo el código). |
| **D (Híbrido 2)** | **Fuzzer simbólico** | **LLM** | Aísla la capacidad de **resolución aritmética** del LLM sobre restricciones perfectas. |

### Dos conceptos clave de medición: equivalencia lógica y *Satisface* vs. *Alcanza*

1. **Comparación de caminos por equivalencia lógica en Z3 (no por texto):**
   El LLM puede escribir una condición negada como `dias <= 7` mientras que el fuzzer simbólico escribe `not (dias > 7)`. Compararlas como strings diría que son distintas, pero ambas expresan exactamente el mismo conjunto matemático. Para verificar que dos fórmulas $F_1$ y $F_2$ son **lógicamente equivalentes**, le preguntamos a Z3 si existe algún valor que cumpla una y no la otra (`z3.Not(F1 == F2)`): si Z3 responde **`unsat`**, ¡las dos restricciones son $100\%$ equivalentes!
2. **Diferencia entre *Satisface* y *Alcanza*:**
   * **Satisface:** los números propuestos cumplen la fórmula que se intentó resolver.
   * **Alcanza:** al ejecutar la función real con esos números (usando `sys.settrace`), el programa recorre verdaderamente las líneas de ese camino.
   * ¿Cuándo una entrada **satisface** pero **no alcanza** el camino? Cuando en la Etapa 1 se **extrajo mal la restricción del camino** (por ejemplo, se olvidó negar la condición de un `else` intermedio): la solución cumple la ecuación equivocada que le dieron, pero al correr en el código real se desvía por otra rama.

### Conclusión práctica: ¿cuándo usar un LLM y cuándo usar Z3?

El `SimpleSymbolicFuzzer` del curso es rígido sintácticamente: se cae con `Z3Exception` si un `if` tiene `and`/`or`, devuelve vacío si una variable se reasigna y falla si la función tiene *docstring*. Un **LLM** es excelente en la **Etapa 1 (extracción flexible)**: comprende código con `and`/`or`, *docstrings*, llamadas auxiliares y reasignaciones sin romperse. En cambio, para la **Etapa 2 (resolución)** sobre sistemas grandes o con aritmética compleja de bordes, un **SMT Solver como Z3** es insuperable porque garantiza exactitud matemática y demuestra formalmente cuándo un camino es `unsat`.

---

## Preguntas de repaso

> [!question]- ¿Por qué la ejecución concólica necesita obligatoriamente una entrada semilla (*seed*) para empezar a trabajar, mientras que la ejecución simbólica pura no la necesita?
> Porque la ejecución concólica recolecta las restricciones **en tiempo de ejecución** observando qué ramas toma un valor concreto real a través de objetos *proxy* (`ConcolicTracer`). Sin una entrada concreta inicial la función no puede ejecutarse. La ejecución simbólica pura, en cambio, extrae las ecuaciones leyendo estáticamente el AST/CFG del código fuente.

> [!question]- En la matriz experimental $2 \times 2$ (`Configuraciones A, B, C, D`), si observas que la Configuración B (`LLM + LLM`) alcanza solo $6/14$ caminos pero la Configuración C (`LLM + Z3`) alcanza $14/14$ caminos, ¿a qué etapa debes atribuir la falla del modelo y por qué?
> La falla se atribuye exclusivamente a la **Etapa 2 (resolución aritmética de restricciones)**. El hecho de que `C` (`LLM extrae + Z3 resuelve`) alcance los $14/14$ caminos demuestra que las fórmulas extraídas por el LLM en la Etapa 1 eran lógicamente correctas, pero el propio LLM se equivocó al despejar mentalmente los números en `B`.

> [!question]- ¿Cómo se utiliza Z3 para comprobar automáticamente si una condición de camino escrita por un alumno o un LLM ($C_{\text{LLM}}$) es lógicamente equivalente a la condición de referencia ($C_{\text{ref}}$) aunque estén escritas con distinta sintaxis?
> Se construye en Z3 la negación de la bicondicional entre ambas fórmulas: **`solver.add(z3.Not(C_LLM == C_ref))`** (es decir, se busca un contraejemplo que satisfaga una fórmula y viole la otra). Si `solver.check()` devuelve **`z3.unsat`**, no existe ningún contraejemplo posible y ambas condiciones son lógicamente equivalentes.

