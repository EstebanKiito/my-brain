---
ramo: "Testing"
tema: "Fuzzing aleatorio y fuzzing basado en mutación"
tags:
  - testing/fuzzing-aleatorio-y-fuzzing-basado-en-mutacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Fuzzing aleatorio y sus límites ante entradas estructuradas]]"
---

# Fuzzing por mutación, operadores de strings y apilamiento de mutaciones

## La idea central: mutar una semilla válida en vez de inventar desde cero

*«La forma más rápida de encontrar entradas interesantes no es inventarlas desde cero, sino modificar levemente una que ya funciona»*. Si generar una URL válida al azar es casi imposible, el **fuzzing basado en mutación** (*mutation-based fuzzing*) invierte el enfoque: partimos de una o más entradas válidas conocidas —llamadas **semillas** (*seed inputs*), como `"https://example.com/api/users?id=10"`— y les aplicamos pequeñas alteraciones aleatorias (**mutaciones**).

Como la semilla ya tiene `"https://"`, dominio, `"/api/"` e `"?id=10"`, una pequeña mutación mantiene casi toda la estructura intacta mientras empuja un componente hacia un **caso borde** (por ejemplo, mutar `"?id=10"` a `"?id=0"` o borrar el dominio), que es justamente donde se esconden los defectos. En el experimento del curso con `http_program(url)`, de $1000$ mutaciones simples sobre `"http://www.google.com/search?q=fuzzing"`, **$824$ ($82.4\%$) siguen siendo URLs válidas**, frente a un $0\%$ del fuzzing aleatorio puro.

---

## Los tres operadores clásicos de mutación de strings

Un **mutador** es una función que recibe una cadena `s` y devuelve una copia levemente modificada:

```python
import random

def delete_random_character(s: str) -> str:
    """1. Borra un carácter en una posición elegida al azar (reduce el largo en 1)."""
    if s == "":
        return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]

def insert_random_character(s: str) -> str:
    """2. Inserta un carácter ASCII imprimible (32..126) en una posición al azar (aumenta el largo en 1)."""
    pos = random.randint(0, len(s))
    random_char = chr(random.randrange(32, 127))
    return s[:pos] + random_char + s[pos:]

def flip_random_character(s: str) -> str:
    """3. Cambia un carácter volteando (XOR) uno de sus 7 bits bajos (mantiene el largo intacto)."""
    if s == "":
        return s
    pos = random.randint(0, len(s) - 1)
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(s[pos]) ^ bit)
    return s[:pos] + new_c + s[pos + 1:]

def mutate(s: str) -> str:
    """Elige uno de los tres operadores al azar y lo aplica sobre s."""
    return random.choice([
        delete_random_character,
        insert_random_character,
        flip_random_character,
    ])(s)
```

### Efecto de cada mutador sobre invariantes de entrada (`validar_pin`)

En evaluaciones es fundamental analizar cómo afecta cada operador a las guardas de una función. Considera `validar_pin(pin)` con semilla `seed = ["1234"]`, que exige: (1) `len(pin) != 4`, (2) `not pin.isdigit()` y (3) `pin == "0000"`:

| Operador aplicado a `"1234"` | ¿Qué pasa con `len == 4`? | ¿Qué pasa con `isdigit()`? |
| :--- | :--- | :--- |
| **`borrar_caracter`** | **Siempre rompe** la longitud ($4 \to 3$). | Mantiene solo dígitos, pero ya falla en el primer `if` por longitud. |
| **`insertar_caracter`** | **Siempre rompe** la longitud ($4 \to 5$). | Suele romper `isdigit()` (solo $10$ de $\sim 100$ imprimibles son dígitos), y ya falla en el primer `if`. |
| **`cambiar_caracter` / `flip`** | **Mantiene siempre** la longitud ($4 \to 4$). | Puede mantener o romper `isdigit()`: es el **único** mutador de los tres que permite pasar del primer `if` en una sola mutación. |

---

## Apilamiento de mutaciones: `min_mutations` y `max_mutations` en `MutationFuzzer`

Una sola mutación explora solo la vecindad inmediata de la semilla. Para diversificar las entradas, la clase `MutationFuzzer` encadena múltiples mutaciones sucesivas:

```python
class MutationFuzzer:
    def __init__(self, seed: list[str], min_mutations: int = 2, max_mutations: int = 10):
        self.seed = seed
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.reset()

    def reset(self):
        self.population = list(self.seed)
        self.seed_index = 0

    def create_candidate(self) -> str:
        candidate = random.choice(self.population)
        trials = random.randint(self.min_mutations, self.max_mutations)
        for _ in range(trials):
            candidate = mutate(candidate)  # Apila la mutación sobre el resultado anterior
        return candidate

    def fuzz(self) -> str:
        if self.seed_index < len(self.seed):
            self.inp = self.seed[self.seed_index]
            self.seed_index += 1
        else:
            self.inp = self.create_candidate()
        return self.inp
```

> [!warning] Pregunta clásica de Interrogación 2: ¿para qué sirven `min_mutations` y `max_mutations`?
> **Trampa frecuente:** muchos estudiantes responden erróneamente que `min_mutations` y `max_mutations` definen «la cantidad mínima y máxima de inputs o casos de prueba que genera el fuzzer». **¡Eso es falso!**
>
> **Respuesta correcta de pauta:** definen el número mínimo y máximo de **mutaciones apiladas (*stacked mutations*) que se aplican de forma iterativa para construir un único candidato**. Cuando `create_candidate()` elige una semilla de `self.population`, sortea un entero aleatorio $K$ tal que $\text{min\_mutations} \le K \le \text{max\_mutations}$ (`trials`) y ejecuta un ciclo de $K$ pasos donde **cada mutación se aplica sobre el resultado de la mutación inmediatamente anterior** ($s_0 \to s_1 \to s_2 \to \dots \to s_K$).
>
> Esto controla el *trade-off* de exploración: un $K$ pequeño mantiene al candidato muy cerca de la semilla válida pero explora poco; un $K$ muy grande (por ejemplo, $50$ mutaciones seguidas) deforma tanto la cadena que vuelve a ser «basura» irreconocible rechazada en la primera línea del parser.

---

## Preguntas de repaso

> [!question]- En la clase `MutationFuzzer(seed, min_mutations=2, max_mutations=10)`, explica con precisión cómo utiliza el algoritmo los atributos `min_mutations` y `max_mutations` al generar un nuevo input.
> Para generar **un** candidato en `create_candidate()`, el fuzzer toma un elemento base de `self.population`, elige al azar un número entero $K$ en el rango $[\text{min\_mutations}, \text{max\_mutations}]$ (entre $2$ y $10$) y aplica iterativamente $K$ mutaciones encadenadas, donde cada llamada a `mutate(candidate)` transforma el string resultante de la mutación anterior. No representa la cantidad de inputs generados por el fuzzer, sino cuántas mutaciones sucesivas acumula un mismo candidato.

> [!question]- En la función `validar_pin(pin)` (que verifica primero `len(pin) != 4`, luego `not pin.isdigit()` y finalmente `pin == "0000"`) partiendo de la semilla `"1234"`, ¿cuál de las tres ramas es la más improbable de alcanzar mediante `MutationFuzzer` y por qué?
> La rama `pin == "0000"`. Mientras que `len(pin) != 4` se alcanza inmediatamente con cualquier `borrar_caracter` o `insertar_caracter`, y `not pin.isdigit()` se alcanza fácilmente al cambiar un carácter por una letra o símbolo ($\sim 90\%$ de los caracteres imprimibles), llegar a `"0000"` exige conservar longitud $4$ y acertar por puro azar el carácter exacto `'0'` en las posiciones mutadas ($\approx 10^{-4}$), una aguja en un pajar que motiva el *search-based fuzzing* y la ejecución simbólica.

> [!question]- ¿Por qué el método `fuzz()` de `MutationFuzzer` devuelve primero los elementos de `self.seed` sin mutar antes de empezar a llamar a `create_candidate()`?
> Porque las semillas originales son entradas válidas conocidas que ya atraviesan el camino feliz del programa. Devolverlas intactas en las primeras llamadas garantiza que la suite cubra primero el comportamiento base válido antes de explorar variaciones deformadas alrededor de él.

