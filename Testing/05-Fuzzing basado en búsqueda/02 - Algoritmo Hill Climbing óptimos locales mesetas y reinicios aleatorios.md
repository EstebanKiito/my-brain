---
ramo: "Testing"
tema: "Fuzzing basado en búsqueda"
tags:
  - testing/fuzzing-basado-en-busqueda
  - origen/complemento
prerrequisitos:
  - "[[01 - Formulación del testing como optimización y función de fitness]]"
---

# Algoritmo Hill Climbing, óptimos locales, mesetas y reinicios aleatorios

## El algoritmo del escalador (*Hill Climbing*)

El algoritmo metaheurístico más directo para recorrer un paisaje de fitness es **Hill Climbing** (ascenso de colina, o descenso en nuestra convención de minimizar distancia): partimos de un punto inicial aleatorio, evaluamos a sus vecinos y nos movemos siempre hacia un vecino que mejore estrictamente el fitness actual (`best_fitness < current_fitness`), repitiendo hasta llegar a $0$ o quedar atascados.

Existen dos variantes clásicas según cómo se elige el vecino en cada paso:
1. **Simple Hill Climbing (primer mejor vecino):** recorre la lista de vecinos y salta (`break`) apenas encuentra el **primero** que tiene `new_fitness < fitness`. Hace menos trabajo por iteración, pero puede requerir más pasos totales.
2. **Steepest Ascent / Descent (máxima pendiente):** evalúa **todos** los vecinos (`min(neighbors, key=...)`) y se mueve al mejor de todos. Cuesta más evaluaciones por iteración, pero desciende por la dirección más empinada en menos pasos.

```python
def hillclimb(fitness_function, bounds, steps, seed=0, restarts=True, max_iterations=10_000):
    random.seed(seed)
    def random_input():
        return tuple(random.randint(lo, hi) for lo, hi in bounds)

    current = random_input()
    current_fitness = fitness_function(*current)
    iterations = 0

    while current_fitness > 0 and iterations < max_iterations:
        iterations += 1
        neighbors = generate_neighbors(current, bounds, steps)
        best_neighbor = min(neighbors, key=lambda c: fitness_function(*c))
        best_fitness = fitness_function(*best_neighbor)

        if best_fitness < current_fitness:
            current, current_fitness = best_neighbor, best_fitness
        else:
            if not restarts:
                return None  # Quedó atrapado en un óptimo local o meseta
            current = random_input()
            current_fitness = fitness_function(*current)

    return current if current_fitness == 0 else None
```

---

## El talón de Aquiles: óptimos locales y mesetas (*plateaus*)

El movimiento codicioso (`best_fitness < current_fitness`) sufre de dos trampas topográficas fundamentales:

* **Óptimo local (*local optimum*):** un punto que no es la solución global ($f(s) > 0$), pero donde **todos sus vecinos inmediatos tienen un fitness peor**. Esto ocurre, por ejemplo, en `evaluar_credito(ingreso, monto, plazo)` cuando buscamos entrar en la franja estrecha $0.349 \le \frac{\text{monto}/\text{plazo}}{\text{ingreso}} \le 0.351$: para mantener el cociente mientras cambia una variable habría que mover dos variables coordinadamente, pero mover una sola empeora temporalmente el fitness.
* **Meseta (*plateau*):** una región plana del espacio de búsqueda donde **todos los vecinos tienen exactamente el mismo fitness que el punto actual** ($f(s') = f(s)$). Sin pendiente hacia ningún lado, la desigualdad estricta `<` se detiene de inmediato.

### Dos estrategias para escapar

1. **Reinicios aleatorios (*Random Restarts*, `restarts=True`):** cuando ningún vecino mejora el fitness actual, nos rendimos en esa colina y saltamos a un nuevo `random_input()` en otra zona del espacio de búsqueda.
2. **Caminata en meseta y algoritmo evolutivo $(1+1)\text{EA}$:** reemplazar la condición estricta `<` por `<=` (`new_fitness <= fitness`). Esto permite al individuo «deambular» horizontalmente por una meseta de fitness constante hasta encontrar un borde con pendiente descendente.

---

## Ejercicio clásico de interrogación: comparando dos funciones de fitness

Supongamos que queremos cubrir la rama **`if x > 100 and y > 100:`** partiendo desde el punto inicial **`(50, 50)`** con movimientos de paso $1$ (vecindario de Moore). Analicemos qué ocurre con dos propuestas de fitness:

```python
def fitness_a(x, y):
    return max(0, 100 - x) + max(0, 100 - y)

def fitness_b(x, y):
    if x > 100:
        return max(0, 100 - y)
    return 1000
```

Evaluemos ambas funciones en el punto actual `(50, 50)` y en sus $8$ vecinos inmediatos:

| Punto $(x, y)$ | Cálculo de `fitness_a(x, y)` | Cálculo de `fitness_b(x, y)` |
| :---: | :---: | :---: |
| **Actual `(50, 50)`** | $50 + 50 = \mathbf{100}$ | Como $50 \not> 100 \implies \mathbf{1000}$ |
| `(49, 49)` | $51 + 51 = 102$ | $1000$ |
| `(49, 50)` / `(50, 49)` | $101$ | $1000$ |
| `(49, 51)` / `(51, 49)` | $100$ | $1000$ |
| `(50, 51)` / `(51, 50)` | $99$ | $1000$ |
| **Mejor vecino `(51, 51)`** | $49 + 49 = \mathbf{98}$ | Como $51 \not> 100 \implies \mathbf{1000}$ |

* **Con `fitness_a`:** el escalador ve un gradiente claro; salta de `(50, 50)` a **`(51, 51)`** (donde $f_a = 98 < 100$) y avanza en diagonal directo hacia $(101, 101)$.
* **Con `fitness_b`:** como en `(50, 50)` y en sus $8$ vecinos se cumple $x \le 100$, **todos valen exactamente $1000$**. El algoritmo cae en una **meseta / óptimo local inmediato** en la primera iteración y jamás puede avanzar a menos que haga **reinicios aleatorios** hasta caer por azar en un punto con $x > 100$.

---

---

## Ejemplo práctico: corriendo los dos fitness del ejercicio

Ejecutamos el escalador de máxima pendiente sobre ambas funciones desde `(50, 50)`:

```python
def vecinos(x, y):
    return [(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]

def escalar(fitness, inicio, max_iter=1000):
    actual, f, it = inicio, fitness(*inicio), 0
    while f > 0 and it < max_iter:
        mejor = min(vecinos(*actual), key=lambda p: fitness(*p))
        if fitness(*mejor) >= f:
            return actual, f, it          # atascado
        actual, f, it = mejor, fitness(*mejor), it + 1
    return actual, f, it

print(escalar(fitness_a, (50, 50)))   # ((100, 100), 0, 50)
print(escalar(fitness_b, (50, 50)))   # ((50, 50), 1000, 0)
```

* Con `fitness_a` el escalador baja $2$ unidades por paso y llega a fitness $0$ en **$50$ iteraciones**.
* Con `fitness_b` se detiene en la iteración $0$ con fitness $1000$: los $8$ vecinos tienen exactamente el mismo valor, no hay dirección que seguir.

> [!warning] Cuidado con el borde: `fitness_a` llega a $0$ en $(100, 100)$, y ahí `x > 100` es **falso**
> La condición es `x > 100 and y > 100`, o sea, se necesita $x \ge 101$ e $y \ge 101$. Con `fitness_a` tal como está escrito, el fitness vale $0$ ya en $(100, 100)$, que **no** entra al `if`. Una versión correcta usa `max(0, 101 - x) + max(0, 101 - y)`. La idea del ejercicio (gradiente claro frente a meseta) no cambia, pero es el mismo tipo de *off-by-one* que vimos en valores límite: la función de fitness también necesita probarse en el borde.

### Escapar de una meseta con reinicios

```python
import random

def escalar_con_reinicios(fitness, limites, intentos=20):
    for _ in range(intentos):
        inicio = tuple(random.randint(lo, hi) for lo, hi in limites)
        punto, f, _ = escalar(fitness, inicio)
        if f == 0:
            return punto
    return None
```

Con `fitness_b`, desde un inicio con $x \le 100$ no hay gradiente, pero un reinicio que caiga en $x > 100$ sí tiene pendiente (`max(0, 100 - y)`) y llega a la meta. Los reinicios convierten una trampa en un problema de probabilidad: $P(\text{éxito})$ crece con el número de intentos.

---

## Preguntas de repaso

> [!question]- ¿Cuál es el *trade-off* computacional entre *Simple Hill Climbing* (moverse al primer vecino que mejore) y *Steepest Ascent Hill Climbing* (moverse al mejor de todos los vecinos)?
> *Simple Hill Climbing* ahorra evaluaciones de la función de fitness dentro de cada iteración porque se detiene (`break`) en cuanto halla un vecino mejor, pero suele tomar caminos más largos en número de iteraciones. *Steepest Ascent* garantiza elegir el mejor paso local en cada iteración (menos iteraciones totales), pero paga el costo fijo de evaluar los $3^N - 1$ vecinos completos en cada paso.

> [!question]- ¿Por qué la función `fitness_b(x, y)` del ejemplo anterior es un mal diseño de función de fitness para la condición compuesta `x > 100 and y > 100`?
> Porque oculta la información de la primera cláusula (`x > 100`) detrás de una constante plana `return 1000`. Mientras $x \le 100$, la función no ofrece ningún gradiente que indique que $x = 99$ está más cerca de superar el umbral que $x = 50$, creando una meseta gigantesca en todo el semiplano $x \le 100$.

> [!question]- En la función `fitness_a(x, y) = max(0, 100 - x) + max(0, 100 - y)`, ¿qué pequeño defecto de borde tiene respecto a la condición estricta `x > 100 and y > 100` (con enteros) y cómo se corrige con la constante $K = 1$?
> En `(100, 100)`, `fitness_a(100, 100)` ya devuelve $0 + 0 = 0$, deteniendo el *hill climber*, pero `100 > 100` es `False` (se necesitaba al menos `(101, 101)`). Para una desigualdad estricta `x > 100` sobre enteros, debemos sumar la constante de penalización $K = 1$: `max(0, (100 - x) + 1) = max(0, 101 - x)`, que recién se hace $0$ cuando $x \ge 101$.

> [!question]- Una función de fitness devuelve $0$ si `x > 100` se cumple y $1$ si no. ¿Por qué es mala para guiar la búsqueda?
> Porque no tiene gradiente: todos los puntos que no cumplen la condición valen igual ($1$), así que ningún vecino parece mejor y el algoritmo queda atrapado en una meseta. Es el mismo caso que `fitness_b`: indica *si* se cumple, pero no *qué tan cerca* está.

> [!question]- Diferencia práctica entre Simple Hill Climbing y Steepest Descent: ¿cuál hace menos evaluaciones por iteración y cuál suele necesitar menos iteraciones?
> Simple Hill Climbing hace menos evaluaciones por iteración (se detiene en el primer vecino que mejora); Steepest Descent evalúa todos los vecinos en cada iteración, pero elige el mejor y normalmente necesita menos iteraciones totales. El balance depende del costo de evaluar el fitness.
