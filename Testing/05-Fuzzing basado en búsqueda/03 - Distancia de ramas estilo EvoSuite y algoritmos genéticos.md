---
ramo: "Testing"
tema: "Fuzzing basado en búsqueda"
tags:
  - testing/fuzzing-basado-en-busqueda
  - origen/complemento
prerrequisitos:
  - "[[01 - Formulación del testing como optimización y función de fitness]]"
  - "[[02 - Algoritmo Hill Climbing óptimos locales mesetas y reinicios aleatorios]]"
---

# Distancia de ramas estilo EvoSuite y algoritmos genéticos

## Cómo derivar mecánicamente la función de fitness (*Branch Distance*)

Para no tener que «adivinar» a ojo la función de fitness de cada `if`, herramientas industriales como **EvoSuite** utilizan un algoritmo mecánico llamado **distancia de rama** (*branch distance*). Dada una constante positiva $K = 1$ (que penaliza las desigualdades estrictas para que la distancia solo valga $0$ cuando la condición ya se cumplió), aplicamos tres reglas paso a paso:

### 1. Tabla de distancia para predicados atómicos

Si el predicado ya se cumple, su distancia es **`0`**. Si **no** se cumple, se aplica la columna derecha:

| Predicado atómico | Distancia si NO se cumple | Equivalente directo en Python (con $K = 1$) |
| :---: | :---: | :--- |
| `a == b` | `abs(a - b)` | `abs(a - b)` |
| `a != b` | `K` | `0 if a != b else 1` |
| `a < b` | `(a - b) + K` | `max(0, (a - b) + 1)` |
| `a <= b` | `(a - b) + K` *(o `a - b` en enteros)* | `max(0, (a - b) + 1)` *(o `max(0, a - b)`)* |
| `a > b` | `(b - a) + K` | `max(0, (b - a) + 1)` |
| `a >= b` | `(b - a) + K` *(o `b - a` en enteros)* | `max(0, (b - a) + 1)` *(o `max(0, b - a)`)* |

### 2. Predicados compuestos (`and`, `or`, `not`) y Leyes de De Morgan

* **Conjunción (`A and B`):** como **ambas** condiciones deben cumplirse simultáneamente, sus distancias se **suman**:
  $$\text{dist}(A \land B) = \text{dist}(A) + \text{dist}(B)$$
* **Disyunción (`A or B`):** como basta con que **una** de las dos se cumpla, tomamos el **mínimo**:
  $$\text{dist}(A \lor B) = \min\bigl(\text{dist}(A),\, \text{dist}(B)\bigr)$$
* **Negación (`not`, para cubrir la rama `False` de un `if`):** jamás se le «resta» nada a la distancia del `True`. Primero se empuja el `not` hacia adentro aplicando las **Leyes de De Morgan** (cambiando `and` $\leftrightarrow$ `or` e invirtiendo cada comparador por su opuesto exacto: `>` $\leftrightarrow$ `<=`, `<` $\leftrightarrow$ `>=`, `==` $\leftrightarrow$ `!=`), y recién sobre la expresión transformada se aplican las reglas 1 y 2.

### 3. Ramas anidadas (dentro de otros `if`)

Para alcanzar un `if` anidado (o una sentencia que vive después de varios `if` con `return` temprano, como en `classify_order` o `evaluar_prestamo`), la función de fitness debe **sumar la distancia de todos los `if` padres** que deben atravesarse primero más la distancia local de la rama objetivo:

$$\text{fitness}(\text{rama}) = \text{dist}(\text{padre}_1) + \text{dist}(\text{padre}_2) + \dots + \text{dist}(\text{local})$$

```python
def ejemplo(a, b, c):
    if a > 10 and b < 5:   # B1
        if c == 0:         # B2 (anidado dentro de B1 True)
            return "x"
        return "y"
    return "z"

# Para cubrir B1 False: negamos not(a > 10 and b < 5) -> (a <= 10) or (b >= 5)
def fitness_b1_false(a, b, c):
    return min(max(0, a - 10), max(0, 5 - b))

# Para cubrir B2 True: necesitamos B1 True (a > 10 and b < 5) + local (c == 0)
def fitness_b2_true(a, b, c):
    dist_b1_true = max(0, 11 - a) + max(0, b - 4)
    dist_local = abs(c - 0)
    return dist_b1_true + dist_local
```

Corriendo un bucle de `hillclimb` por cada una de las $2M$ funciones de fitness de un programa con $M$ decisiones (*Hill Climbing 2.0*), generamos automáticamente la batería completa que alcanza el $100\%$ de *Branch Coverage*.

---

## Algoritmos Genéticos (*Genetic Algorithms*, GA)

En lugar de mover un único individuo como hace *Hill Climbing*, un **algoritmo genético** mantiene una **población** completa de soluciones candidatas («cromosomas») y las hace evolucionar en paralelo generación tras generación:

1. **Población inicial:** creamos $N$ individuos aleatorios (por ejemplo, $100$ cadenas aleatorias para descubrir `TARGET = "PASSWORD"`, evaluadas con la distancia de caracteres $\text{str\_fitness}(s) = \bigl||s| - |T|\bigr| + \sum | \text{ord}(a) - \text{ord}(b)|$).
2. **Selección por torneo (`selection`):** sorteamos $k$ individuos al azar de la población (ej. $k = 10$) y elegimos como padre al que tenga el mejor (menor) fitness.
3. **Cruce de un punto (*Crossover*):** dados dos padres `p1` y `p2`, elegimos un índice de corte `pos` al azar e intercambiamos sus mitades para crear dos hijos (`p1[:pos] + p2[pos:]` y `p2[:pos] + p1[pos:]`), combinando subsoluciones útiles descubiertas por separado.
4. **Mutación gaussiana (`mutate`):** alteramos cada «gen» (carácter) con probabilidad $P = 1/\text{len}(s)$ sumando ruido gaussiano `random.gauss(ord(c), 20)` para mantener diversidad y evitar converger prematuramente.

### ¿Cuándo elegir Hill Climbing y cuándo un Algoritmo Genético?

* **Ventaja del Algoritmo Genético:** en paisajes muy accidentados llenos de óptimos locales, el GA explora múltiples regiones en paralelo y el operador de **cruce (*crossover*)** permite dar grandes saltos combinando la mitad buena del padre A con la mitad buena del padre B, convergencia que en el ejemplo de `"PASSWORD"` logra fitness $0$ en apenas $34$ generaciones.
* **Ventaja de Hill Climbing:** en paisajes suaves o unimodales (como ecuaciones lineales o ramas numéricas simples), *Hill Climbing* es mucho más simple de programar, no requiere calibrar hiperparámetros delicados (tamaño de población, tasa de cruce, tamaño de torneo) y realiza muchas menos ejecuciones del programa bajo prueba.

---

---

## Ejemplo práctico: distancia de rama calculada a mano

Para el `ejemplo(a, b, c)` de la nota, calculamos cuánto falta para llegar a `return "x"` (rama `B2` verdadera) desde tres entradas distintas, usando las fórmulas de la tabla con $K = 1$:

* **Camino a cubrir:** `a > 10` ∧ `b < 5` ∧ `c == 0`.
* $\text{dist}(a > 10) = \max(0, 10 - a + 1)$, $\text{dist}(b < 5) = \max(0, b - 5 + 1)$, $\text{dist}(c == 0) = |c|$.

| Entrada $(a, b, c)$ | $\text{dist}(a>10)$ | $\text{dist}(b<5)$ | $\text{dist}(c==0)$ | Fitness total |
| :---: | :---: | :---: | :---: | :---: |
| $(0, 10, 7)$ | $11$ | $6$ | $7$ | $\mathbf{24}$ |
| $(5, 4, 0)$ | $6$ | $0$ | $0$ | $\mathbf{6}$ |
| $(11, 4, 0)$ | $0$ | $0$ | $0$ | $\mathbf{0}$ ✓ |

Se confirma que `ejemplo(11, 4, 0)` devuelve `"x"`. Fíjate en el borde: con $a = 10$ la distancia sería $1$, porque `10 > 10` es falso. La constante $K = 1$ existe justamente para que el fitness sea $0$ solo cuando la desigualdad estricta se cumple.

```python
def dist_gt(a, b):            # a > b
    return max(0, (b - a) + 1)

def dist_lt(a, b):            # a < b
    return max(0, (a - b) + 1)

def fitness_x(a, b, c):
    return dist_gt(a, 10) + dist_lt(b, 5) + abs(c)

print(fitness_x(0, 10, 7), fitness_x(5, 4, 0), fitness_x(11, 4, 0))    # 24 6 0
```

### Un algoritmo genético para adivinar `"PASSWORD"`

Aplicamos las cuatro piezas (población, torneo, cruce de un punto y mutación gaussiana) con fitness $\sum_i |\text{ord}(s_i) - \text{ord}(\text{TARGET}_i)|$:

```python
import random

TARGET = "PASSWORD"

def fitness(s):
    return sum(abs(ord(a) - ord(b)) for a, b in zip(s, TARGET))

def aleatorio():
    return "".join(chr(random.randint(32, 126)) for _ in TARGET)

def torneo(poblacion, k=10):
    return min(random.sample(poblacion, k), key=fitness)

def cruce(p1, p2):
    corte = random.randint(1, len(p1) - 1)
    return p1[:corte] + p2[corte:], p2[:corte] + p1[corte:]

def mutar(s):
    resultado = []
    for c in s:
        if random.random() < 1 / len(s):
            c = chr(max(32, min(126, round(random.gauss(ord(c), 20)))))
        resultado.append(c)
    return "".join(resultado)

poblacion = [aleatorio() for _ in range(100)]
for generacion in range(1, 500):
    mejor = min(poblacion, key=fitness)
    if fitness(mejor) == 0:
        break
    nueva = [mejor]                        # elitismo: conservamos al mejor
    while len(nueva) < 100:
        h1, h2 = cruce(torneo(poblacion), torneo(poblacion))
        nueva += [mutar(h1), mutar(h2)]
    poblacion = nueva[:100]
print(generacion, mejor)                   # típicamente en menos de ~100 generaciones: "PASSWORD"
```

En una corrida de prueba con semilla fija encontró `"PASSWORD"` a la generación $40$. El número cambia con la semilla, pero converge de forma sistemática, mientras que un fuzzer aleatorio tendría que acertar $8$ caracteres entre $95$ posibles cada uno ($95^8 \approx 6.6 \times 10^{15}$ intentos).

---

## Preguntas de repaso

> [!question]- Dada la condición `if plazo_meses > 60 and monto > 5000000:`, deriva paso a paso la función de distancia de rama (con $K=1$ para desigualdad estricta en enteros) tanto para la rama `True` como para la rama `False`.
> * **Rama `True` (`plazo_meses > 60 and monto > 5000000`):** es un `and`, por lo que sumamos las distancias de ambas desigualdades estrictas:
>   $$\text{dist}_{\text{True}} = \max(0,\, 61 - \text{plazo\_meses}) + \max(0,\, 5\,000\,001 - \text{monto})$$
> * **Rama `False`:** primero aplicamos De Morgan a `not (plazo_meses > 60 and monto > 5000000)`, obteniendo `plazo_meses <= 60 or monto <= 5000000`. Como ahora es un `or`, tomamos el mínimo:
>   $$\text{dist}_{\text{False}} = \min\bigl(\max(0,\, \text{plazo\_meses} - 60),\, \max(0,\, \text{monto} - 5\,000\,000)\bigr)$$

> [!question]- ¿Por qué la función de fitness de un `if` que está después de un `if historial_atrasos > 3: return "rechazado"` debe incluir en su suma la distancia de `historial_atrasos <= 3`?
> Porque si `historial_atrasos > 3` se cumple, la función retorna inmediatamente en la primera línea y el flujo de ejecución jamás llega al segundo `if`. Sumar la distancia del padre (`max(0, historial_atrasos - 3)`) garantiza que el fitness total solo pueda llegar a $0$ cuando la entrada evita el retorno temprano **y además** satisface la condición del segundo `if`.

> [!question]- ¿Qué papel cumple el operador de cruce (*crossover*) en un algoritmo genético y por qué le da ventaja frente a un *hill climber* con reinicios cuando buscamos una cadena como `"PASSWORD"`?
> Un *hill climber* con reinicios desecha todo lo aprendido cada vez que se atasca y empieza desde cero con un solo individuo. En cambio, en un algoritmo genético un individuo de la población puede haber descubierto los primeros caracteres `"PASSxxxx"` y otro individuo los últimos `"xxxxWORD"`; el **cruce de un punto** combina ambos segmentos en una sola generación produciendo directamente `"PASSWORD"`.

> [!question]- Calcula el fitness de rama para entrar al bloque de `if x >= 20 or y == 3:` con `(x, y) = (15, 10)`.
> Es una disyunción, así que se toma el mínimo: $\text{dist}(x \ge 20) = \max(0, 20 - 15) = 5$ (o $6$ con $K = 1$ estricto) y $\text{dist}(y == 3) = |10 - 3| = 7$. El fitness es $\min(5, 7) = 5$: basta acercarse a una de las dos condiciones.

> [!question]- ¿Por qué un algoritmo genético conserva al mejor individuo de cada generación (elitismo) y qué pasa si no lo hace?
> Sin elitismo, el cruce y la mutación pueden destruir al mejor individuo y la población empeora temporalmente (o para siempre, con mala suerte). Conservarlo garantiza que el mejor fitness nunca aumente de una generación a otra, aunque las demás mutaciones exploren.
