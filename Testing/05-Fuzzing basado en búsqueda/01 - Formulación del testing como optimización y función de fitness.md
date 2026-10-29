---
ramo: "Testing"
tema: "Fuzzing basado en búsqueda"
tags:
  - testing/fuzzing-basado-en-busqueda
  - origen/complemento
prerrequisitos:
  - "[[Testing/04-Fuzzing aleatorio y fuzzing basado en mutación/03 - Fuzzing por mutación guiado por cobertura|Fuzzing por mutación guiado por cobertura]]"
---

# Formulación del testing como optimización y función de fitness

## De mutar a ciegas a buscar con brújula

En el tema anterior vimos que el *fuzzing* por mutación explora mediante una caminata aleatoria: si queremos cubrir una rama protegida por una condición específica como `if x == 2 * (y + 1):`, mutar al azar y mirar solo si la línea se cubrió o no es como buscar una moneda en un estadio con los ojos vendados diciendo únicamente «frío, frío... ¡bingo!».

El **fuzzing basado en búsqueda** (*search-based fuzzing*, o *Search-Based Software Testing*, SBST) cambia las reglas del juego: reemplaza el «frío / bingo» binario por un **juego de frío, tibio y caliente**. Convierte la generación de casos de prueba en un **problema de optimización matemática** compuesto por tres ingredientes:

1. **Representación de las soluciones candidatas:** cómo codificamos una entrada de prueba (por ejemplo, una tupla de enteros `(x, y)` o un string `s` dentro de ciertos límites `bounds`).
2. **Noción de vecindad u operadores de variación:** cómo generamos nuevas candidatas cercanas a la actual (por ejemplo, sumar o restar un paso `step` a cada coordenada).
3. **Función de aptitud (*fitness function*):** una heurística numérica $f(s) \ge 0$ que mide **qué tan lejos está la candidata $s$ de cumplir la condición objetivo**.

> [!important] Convención del curso: minimizar el fitness hasta $0$
> Aunque el nombre histórico *hill climbing* habla de «subir la colina», en generación de pruebas medimos **distancia al objetivo**, por lo que **menor es mejor**: buscamos **minimizar** $f(s)$ descendiendo por la ladera hasta alcanzar $f(s) = 0$, instante exacto en que la condición de la rama se cumple.

---

## El paisaje de fitness y la importancia del gradiente

Consideremos la función `test_me(x, y)` que solo entra al `if` cuando $x = 2(y + 1)$ en el dominio $[-1000, 1000]^2$. Su función de fitness natural es la distancia absoluta entre ambos lados de la igualdad:

```python
def get_fitness(x: int, y: int) -> int:
    """Distancia al objetivo x == 2 * (y + 1). Vale 0 exactamente en la solución."""
    return abs(x - 2 * (y + 1))

print(get_fitness(100, 3))  # |100 - 8| = 92 (lejos)
print(get_fitness(10, 3))   # |10 - 8|  = 2  (muy cerca)
print(get_fitness(8, 3))    # |8 - 8|   = 0  (¡solución encontrada!)
```

¿Por qué funciona esta función? Porque tiene un **gradiente suave**: aunque ni `(100, 3)` ni `(10, 3)` satisfacen el `if`, la función de fitness nos informa que `(10, 3)` es muchísimo mejor ($2 < 92$), creando una **pendiente** que guía al algoritmo paso a paso hacia `(8, 3)`. Si en cambio hubiésemos definido un fitness binario (`0` si $x = 2(y+1)$ y `1` en caso contrario), todo el paisaje sería una llanura plana de altura `1` con un único agujero oculto, degradando la búsqueda al mismo azar ciego del *random fuzzing*.

---

## Generación del vecindario ($N$-dimensiones)

Para movernos desde una solución actual `values` hacia puntos adyacentes, en dos dimensiones enteras usamos el **vecindario de Moore** (los $8$ vecinos inmediatos que suman $dx, dy \in \{-1, 0, +1\}$ descartando el $(0, 0)$ y respetando `[MIN, MAX]`). Para generalizarlo a una función con $N$ parámetros cualesquiera, con límites `bounds = [(min_1, max_1), ...]` y tamaños de paso `steps = [step_1, ...]`, construimos el producto cartesiano de las opciones `[v - step, v, v + step]` de cada argumento:

```python
def neighbors_of_one_value(value, minimum, maximum, step=1):
    candidates = [value - step, value, value + step]
    return [c for c in candidates if minimum <= c <= maximum]

def build_combinations(options_per_argument):
    if not options_per_argument:
        return [()]
    first_options, *rest_options = options_per_argument
    rest_combinations = build_combinations(rest_options)
    return [(opt,) + comb for opt in first_options for comb in rest_combinations]

def generate_neighbors(values, bounds, steps):
    options = [
        neighbors_of_one_value(v, lo, hi, st)
        for v, (lo, hi), st in zip(values, bounds, steps)
    ]
    return [c for c in build_combinations(options) if c != values]
```

Por ejemplo, para `values = (5, 100)`, `bounds = [(-10, 20), (0, 200)]` y `steps = [1, 10]`, `generate_neighbors` produce los $3^2 - 1 = 8$ vecinos: `(4, 90)`, `(4, 100)`, `(4, 110)`, `(5, 90)`, `(5, 110)`, `(6, 90)`, `(6, 100)` y `(6, 110)`.

---

## Preguntas de repaso

> [!question]- Explica por qué una función de fitness gradual hace posible el *search-based fuzzing*, mientras que una función de fitness binaria (`0` si entra al `if`, `1` si no entra) lo vuelve inútil. Ilustra con la condición `if x == 42:`.
> Un algoritmo de búsqueda decide hacia qué vecino moverse comparando sus valores de fitness. Para `if x == 42:`, el fitness gradual $f(x) = |x - 42|$ vale $8$ en $x = 50$, $7$ en $x = 49$ y $9$ en $x = 51$: el algoritmo ve inmediatamente que moverse hacia $49$ disminuye el fitness y desciende directo hasta $42$. Con un fitness binario, tanto $x = 50$ como sus vecinos $49$ y $51$ tienen exactamente fitness $1$; no existe pendiente que indique hacia qué lado está el $42$.

> [!question]- Si una función recibe $3$ argumentos enteros y ningún argumento está en el borde de sus `bounds`, ¿cuántos vecinos genera `generate_neighbors` en cada iteración?
> Para cada uno de los $3$ argumentos se prueban $3$ valores (`v - step`, `v` y `v + step`). El producto cartesiano tiene $3^3 = 27$ combinaciones, y al excluir la tupla original (`c != values`) quedan exactamente **$26$ vecinos**. En general, en el interior del dominio con $N$ variables se generan $3^N - 1$ vecinos.

> [!question]- ¿Qué tres componentes son indispensables para formular la generación de pruebas como un problema de búsqueda metaheurística?
> 1. Una **representación** de las soluciones candidatas dentro del espacio de búsqueda.
> 2. Un operador de **vecindad** (o de variación genética) que genere nuevas candidatas a partir de las actuales.
> 3. Una **función de fitness** que asigne un puntaje numérico a cada candidata estimando su cercanía al objetivo.

