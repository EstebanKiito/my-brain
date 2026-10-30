---
ramo: "Testing"
tema: "Análisis dinámico y perfilado de ejecución"
tags:
  - testing/analisis-dinamico-y-perfilado-de-ejecucion
  - origen/complemento
prerrequisitos:
  - "[[02 - Implementación de FunctionInstrumentor manejo de return y recursión]]"
  - "[[03 - Perfilado por muestreo Execution Sampling y Calling Context Tree]]"
---

# Instrumentación frente a muestreo efecto del observador y sesgo de período constante

## Comparación directa: Instrumentación vs. Muestreo

Elegir entre perfilado por instrumentación y perfilado por muestreo (*sampling*) es una decisión clásica de ingeniería guiada por el compromiso entre **exactitud** y **sobrecarga (*overhead*)**:

| Dimensión | Instrumentación (*Instrumentation*) | Muestreo (*Execution Sampling*) |
| :--- | :--- | :--- |
| **Cómo observa** | Modifica el código o bytecode inyectando sondas al inicio y fin de cada función | Interrumpe periódicamente la ejecución desde otro hilo y fotografía la pila (`_current_frames`) |
| **Precisión de conteo** | **Exacta**: registra el 100% de las llamadas y sus argumentos reales | **Estadística**: estima la proporción de tiempo, pero no sabe cuántas veces se llamó una función |
| **Cobertura de eventos** | **Total**: captura incluso funciones que duran nanosegundos | **Parcial (ceguera a lo breve)**: funciones más cortas que el intervalo $\Delta t$ pueden no salir en ninguna foto |
| **Overhead en tiempo** | **Alto**: ejecuta código del profiler en cada llamada a función | **Bajo y controlable**: depende solo de la frecuencia de muestreo $1/\Delta t$ |
| **Riesgo de alterar el sistema** | **Alto**: puede introducir bugs si la transformación AST falla y distorsiona tiempos relativos | **Mínimo**: no modifica el código fuente del programa analizado |
| **Herramientas en Python** | `cProfile`, `profile`, `coverage.py` | `py-spy`, `pyinstrument`, `Austin` |

### Regla de decisión práctica
- **Usa instrumentación** cuando necesites **conteos exactos o cobertura completa** (por ejemplo, verificar en un test que un endpoint o caché se llamó exactamente $N$ veces, o medir cobertura de líneas/ramas) en un entorno de pruebas donde el overhead sea aceptable.
- **Usa muestreo (*sampling*)** cuando necesites encontrar cuellos de botella de tiempo (**hotspots**) en un sistema en producción o en un pipeline que corre durante horas, donde no puedes permitirte ralentizar el programa 10x.

---

## El Efecto del Observador (*Observer Effect*) y la distorsión de tiempos

Una pregunta fundamental de examen (Clase 17, Pregunta 28) es: **¿Cuál es la principal desventaja de usar instrumentación para medir tiempos de ejecución y qué es el Efecto del Observador?**

El **Efecto del Observador** ocurre cuando el acto de medir un sistema modifica el comportamiento del propio sistema que se está midiendo. En el perfilado por instrumentación, esto se manifiesta de dos formas graves:

1. **Distorsión desproporcionada de funciones pequeñas y frecuentes**:
   Supongamos que cada sonda (`record_start` + `record_end`) tarda $2\,\mu\text{s}$ en ejecutarse.
   - La función `pesada()` se llama $1$ vez y tarda $100\,000\,\mu\text{s}$ ($100\text{ ms}$). Con instrumentación tarda $100\,002\,\mu\text{s}$ (error del $0.002\%$).
   - La función `trivial(x)` hace `return x + 1` (tarda $0.1\,\mu\text{s}$), pero se llama dentro de un bucle $100\,000$ veces (tiempo real total: $10\,000\,\mu\text{s} = 10\text{ ms}$).
   - Al instrumentarla, las $100\,000$ llamadas pagan $100\,000 \times 2\,\mu\text{s} = 200\,000\,\mu\text{s}$ ($200\text{ ms}$) de puro overhead del profiler.
   - **Resultado**: el profiler reporta que `trivial(x)` tardó $210\text{ ms}$ (más del doble que `pesada()`), engañando al desarrollador con un **falso hotspot** creado por el propio peso de los sensores.
2. **Alteración de concurrencia (*Heisenbugs*)**:
   Al inyectar instrucciones adicionales y adquirir locks o escribir en estructuras compartidas del profiler, cambian los tiempos relativos entre hilos, la localidad de caché y el *scheduling* del sistema operativo. Esto puede ocultar condiciones de carrera (*race conditions*) que ocurrían en producción, o provocar bloqueos que no existían sin el profiler.

---

## El peligro de un período de muestreo constante $K$ (Sesgo de sincronización)

Si el muestreo es tan liviano, ¿basta con despertar exactamente cada $K$ milisegundos constantes (`sleep(K)`)? Otra pregunta clásica de evaluación es: **¿Por qué elegir un período constante $K$ puede ser problemático en Execution Sampling?**

El problema es el **sesgo de sincronización (*synchronization bias* o *aliasing*)**:
- Muchos programas tienen comportamientos cíclicos o periódicos (por ejemplo, un bucle de juego a 60 Hz, un *worker* que procesa un lote y limpia memoria cada $10\text{ ms}$, o un temporizador interno de período $T$).
- Si el período constante del sampler $K$ coincide con el período $T$ del programa (o es un múltiplo/armónico exacto, como $K = 10\text{ ms}$ y el bucle dura $10\text{ ms}$ donde los primeros $9\text{ ms}$ ejecuta `procesar()` y el último $1\text{ ms}$ ejecuta `limpiar()`), el sampler tomará todas sus fotografías **exactamente en la misma fase del ciclo**.
- En consecuencia, podría muestrear el 100% de las veces a `limpiar()` (haciendo creer que consume el 100% de la CPU cuando solo usa el 10%) o no verla jamás (0%).

**Solución**: añadir **aleatoriedad (*jitter*)** al intervalo de muestreo, despertando en cada iteración tras un tiempo uniforme o exponencial alrededor de $K$ (por ejemplo, $K \pm \epsilon$ aleatorio). Al romper la periodicidad estricta, las muestras se distribuyen uniformemente sobre todas las fases de cualquier ciclo del programa.

---

---

## Ejemplo práctico: medir el efecto del observador y ver el aliasing

### 1. Cuánto pesa una sonda sobre una función diminuta

Envolvemos `trivial(x)` con una sonda que mide y registra cada llamada, igual que haría un profiler por instrumentación:

```python
import time

registro = []

def con_sonda(f):
    def envuelta(*args):
        t0 = time.perf_counter()
        resultado = f(*args)
        registro.append((f.__name__, time.perf_counter() - t0))
        return resultado
    return envuelta

def trivial(x):
    return x + 1

trivial_instrumentada = con_sonda(trivial)

N = 200_000
t0 = time.perf_counter()
for i in range(N):
    trivial(i)
sin_sonda = time.perf_counter() - t0

t0 = time.perf_counter()
for i in range(N):
    trivial_instrumentada(i)
con_sonda_t = time.perf_counter() - t0

print(f"sin sonda: {sin_sonda:.3f} s | con sonda: {con_sonda_t:.3f} s | factor: {con_sonda_t / sin_sonda:.1f}x")
```

En una máquina de prueba el factor fue de alrededor de $3\times$ (los números exactos dependen del equipo). La función no cambió: lo que creció es el costo de observarla, y el profiler la mostraría mucho más lenta de lo que es en producción.

### 2. Simular el sesgo de sincronización con período constante

Un programa repite un ciclo de $T = 10\text{ ms}$: $9\text{ ms}$ en `procesar()` y $1\text{ ms}$ en `limpiar()`. Simulamos un sampler que mira qué función está activa en cada instante:

```python
import random

T = 10.0   # ms por ciclo: 9 ms procesar() + 1 ms limpiar()

def funcion_activa(t):
    return "procesar" if (t % T) < 9.0 else "limpiar"

def muestrear(proximo_intervalo, n=1000, t0=9.5):
    t, cuenta = t0, {"procesar": 0, "limpiar": 0}
    for _ in range(n):
        cuenta[funcion_activa(t)] += 1
        t += proximo_intervalo()
    return cuenta

print(muestrear(lambda: 10.0))                         # K constante
print(muestrear(lambda: random.uniform(8.0, 12.0)))    # K con jitter
```

Resultado:

```
{'procesar': 0, 'limpiar': 1000}      # K = 10 ms constante
{'procesar': 902, 'limpiar': 98}      # jitter entre 8 y 12 ms
```

Con período constante el sampler cae siempre en la misma fase y concluye que **el programa pasa el $100\%$ del tiempo en `limpiar()`** (en realidad es el $10\%$). Con *jitter* las muestras recorren todas las fases y la estimación ($\approx 9.8\%$) se acerca al valor real. Fíjate que en una máquina real el sleep tiene deriva propia y el efecto no siempre es tan limpio; la simulación aísla el fenómeno.

---

## Preguntas de repaso

> [!question]- ¿Por qué el perfilado por instrumentación puede señalar como el mayor cuello de botella a una función diminuta que en realidad consume muy poco tiempo en producción?
> Porque el costo fijo de ejecutar las sondas (`record_start` y `record_end`) se paga en **cada invocación**. Si una función muy corta (p. ej. un *getter* o cálculo aritmético simple) se invoca millones de veces dentro de un ciclo, el tiempo acumulado por las sondas del profiler multiplica artificialmente su duración aparente (*Observer Effect*).

> [!question]- Una función `validar_token()` tarda $0.05\text{ ms}$ y se ejecuta una vez por petición HTTP (10 veces por segundo). Si perfilamos el servidor con un sampler cuyo intervalo es $\Delta t = 20\text{ ms}$, ¿qué veremos en el reporte y por qué?
> Muy probablemente `validar_token()` aparecerá con $0$ muestras (o casi ninguna), porque su duración es muchísimo menor que el intervalo entre fotografías (**ceguera a lo breve**) y su tiempo acumulado total ($0.5\text{ ms}$ por segundo, es decir $0.05\%$ del tiempo) hace estadísticamente improbable que la foto caiga justo dentro de ella.

> [!question]- Explica con un ejemplo concreto cómo un período de muestreo constante $K = 100\text{ ms}$ puede producir un perfil completamente falso, y cómo se corrige en la práctica.
> Si un programa ejecuta un ciclo repetitivo que dura exactamente $100\text{ ms}$ (por ejemplo, $95\text{ ms}$ en `calcular()` y los últimos $5\text{ ms}$ en `guardar_log()`) y el sampler toma muestras exactamente en $t = 98, 198, 298\text{ ms}\dots$, el 100% de las muestras capturarán a `guardar_log()` por estar en fase con el ciclo. Se corrige introduciendo una perturbación aleatoria (*jitter*) en el tiempo de espera entre muestras (`sleep(random.uniform(0.8 * K, 1.2 * K))`).

> [!question]- Debes decidir qué usar en cada caso: (a) verificar en un test que una función de caché se llama exactamente $3$ veces; (b) encontrar por qué un servicio en producción usa mucha CPU. ¿Instrumentación o muestreo?
> (a) **Instrumentación**: necesitas conteos exactos y el overhead es aceptable en un entorno de pruebas. (b) **Muestreo**: el overhead es bajo y controlable, no modifica el código en producción y basta con una estimación estadística de dónde se va el tiempo (hotspots).

> [!question]- En el experimento de la sonda, `trivial` tardó $3\times$ más con instrumentación. Si `pesada()` tarda $100\text{ ms}$ y se llama una vez, ¿cambia el ranking de funciones más lentas? ¿Por qué?
> Sí, puede cambiar: la sonda suma un costo fijo por **llamada**, así que `pesada()` casi no se distorsiona (una llamada), mientras que `trivial` paga el costo $200\,000$ veces y podría pasar a parecer un falso hotspot. El perfil refleja entonces el costo del profiler, no el del programa.
