---
ramo: "Testing"
tema: "Fuzzing aleatorio y fuzzing basado en mutación"
tags:
  - testing/fuzzing-aleatorio-y-fuzzing-basado-en-mutacion
  - origen/complemento
prerrequisitos:
  - "[[Testing/03-Cobertura de código e instrumentación con settrace/04 - La clase Coverage diferencias de conjuntos y límites de la cobertura|La clase Coverage diferencias de conjuntos y límites de la cobertura]]"
---

# Fuzzing aleatorio y sus límites ante entradas estructuradas

## ¿Qué es el *Fuzzing*?

Hasta ahora hemos diseñado cada entrada de prueba a mano. El **fuzzing** (término acuñado por Barton Miller en 1988 al probar utilidades de UNIX con ruido telefónico) consiste en **alimentar un programa automáticamente con miles de entradas generadas al azar —muchas veces malformadas— y observar cómo reacciona**.

Como al generar entradas al azar no conocemos de antemano cuál debería ser el valor de retorno exacto para cada una, el fuzzing se apoya en **oráculos implícitos (genéricos)**: verificar que el programa no sufra una caída abrupta (*crash*), no lance excepciones inesperadas no documentadas, no viole un `assert` interno ni se quede colgado en un bucle infinito.

---

## Implementación de `RandomFuzzer`

La forma más simple de fuzzing es el **fuzzing aleatorio puro**: elegir una longitud al azar entre `min_length` y `max_length` y concatenar caracteres extraídos uniformemente de un alfabeto (como `string.printable`):

```python
import random
import string

class RandomFuzzer:
    def __init__(self, min_length=2, max_length=10, chars=string.printable):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def create_candidate(self):
        length = random.randint(self.min_length, self.max_length)
        return "".join(random.choice(self.chars) for _ in range(length))
```

Si combinamos `RandomFuzzer` con nuestra clase `Coverage` (del Tema 03) para probar una función de validaciones independientes como `validate_password(pw)` —que chequea secuencialmente largo mínimo ($8$), largo máximo ($16$), presencia de mayúscula, minúscula, dígito, símbolo y ausencia de espacios—, en $100$ intentos aleatorios logra cubrir casi todas las guardas iniciales conservando apenas $7$ entradas en su *corpus*.

---

## El muro del fuzzing aleatorio: entradas estructuradas (`validate_url`)

¿Qué ocurre cuando aplicamos exactamente el mismo `RandomFuzzer` contra una función que espera un **formato estructurado**, como el analizador de URLs `validate_url(url)`?

```python
from urllib.parse import urlparse, parse_qs

def validate_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme not in {"http", "https"}:
        return "invalid scheme"
    if not parsed_url.netloc:
        return "missing domain"
    if parsed_url.hostname is None or "." not in parsed_url.hostname:
        return "invalid domain"
    if not parsed_url.path.startswith("/api/"):
        return "invalid API path"
    parameters = parse_qs(parsed_url.query)
    if "id" not in parameters:
        return "missing id"
    identifier = parameters["id"][0]
    if not identifier.isdigit():
        return "invalid id"
    if int(identifier) <= 0:
        return "id must be positive"
    return "valid URL"
```

Al correr $100$ iteraciones de `RandomFuzzer` generando cadenas como `'tYgjmUh#Be'` o `'R5Kjp$1vRt!1fjO'`, **el $100\%$ de los intentos es rechazado en la primera condición (`return "invalid scheme"`)**, sin avanzar ni una sola línea hacia el interior de la función.

### ¿Por qué fracasa matemáticamente la aleatoriedad pura?

Si `string.printable` tiene $100$ caracteres posibles, la probabilidad de que los primeros $7$ caracteres elegidos al azar formen exactamente el prefijo `"http://"` es:

$$P(\text{"http://"}) = \left(\frac{1}{100}\right)^7 = 10^{-14}$$

Y si además exigimos que tenga un punto en el dominio, la subcadena `"/api/"` en la ruta y `"?id="` seguido de dígitos positivos, la probabilidad conjunta cae por debajo de $10^{-30}$. El fuzzing aleatorio puro choca contra el muro de los *parsers*: **casi ninguna cadena aleatoria supera los chequeos sintácticos iniciales**, dejando toda la lógica profunda del programa con $0\%$ de cobertura.

---

## Preguntas de repaso

> [!question]- ¿Qué tipo de oráculo de prueba utiliza el fuzzing cuando genera miles de entradas automáticas sin saber qué valor exacto debería retornar la función para cada una?
> Utiliza un **oráculo implícito (o genérico)**: en lugar de verificar que la salida coincida con un valor de negocio específico, verifica que la ejecución no provoque un fallo catastrófico (como un *crash* del intérprete, una excepción no controlada, una violación de memoria o un tiempo de espera infinito).

> [!question]- ¿Por qué `RandomFuzzer` logra cubrir varias ramas en `validate_password` pero se queda estancado en la primera línea de `validate_url`?
> Porque las primeras condiciones de `validate_password` son propiedades densas en el espacio de cadenas aleatorias (tener largo $< 8$, largo $> 16$, o contener al menos una letra mayúscula o dígito entre $10$ caracteres al azar ocurre con alta probabilidad). En cambio, `validate_url` exige prefijos y delimitadores exactos (`"http://"`, `"/api/"`, `"?id="`) cuya probabilidad de aparecer por azar independiente carácter a carácter es astronómicamente cercana a cero.

> [!question]- Si una función comienza con la guarda `if codigo == "SECRETO_2026":`, ¿cuál es la probabilidad de que un `RandomFuzzer` que genera cadenas de largo $12$ sobre un alfabeto de $95$ caracteres imprimibles entre al `if` en un intento?
> Como cada uno de los $12$ caracteres debe coincidir exactamente de forma independiente, la probabilidad es $(1/95)^{12} \approx 1.85 \times 10^{-24}$, lo que hace imposible cubrir esa rama mediante fuerza bruta aleatoria.
