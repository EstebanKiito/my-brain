---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/funcional
  - programacion/generadores
  - programacion/eficiencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Paradigma funcional y funciones puras]]"
  - "[[03 - Funciones de orden superior: map, filter y reduce]]"
  - "[[05 - Generadores y la palabra clave yield]]"
---

# Pipelines de datos y evaluación perezosa en la práctica

En proyectos de ciencia de datos, análisis de registros web (*logs*) o servicios financieros, procesar conjuntos de datos que superan la memoria RAM del computador es una necesidad habitual. Si cargamos el archivo completo en memoria, el sistema operativo colapsa por agotamiento de recursos.

## La arquitectura de tuberías de datos (Data Pipelines)

Un **pipeline de datos** (*tubería de datos*) es una cadena de procesamiento donde los datos fluyen a través de etapas modulares independientes:

1. **Emisión (*Source*):** genera o lee registros de forma perezosa mediante un generador.
2. **Transformación (*Map*):** normaliza o extrae campos relevantes.
3. **Filtrado (*Filter*):** descarta registros que no cumplen los criterios de análisis.
4. **Agregación (*Sink / Reduce*):** condensa la información final en un reporte o base de datos.

Dado que cada etapa retorna un iterador perezoso, los elementos se procesan **uno a uno**, manteniendo el consumo de memoria en un orden constante **$O(1)$**.

```python
# Simulación de registros de compras: (id_cliente, monto, categoria)
registro_compras = [
    ("usr_1", 12000, "tecnologia"),
    ("usr_2", 4500, "alimentos"),
    ("usr_3", 85000, "tecnologia"),
    ("usr_4", 1500, "alimentos"),
    ("usr_5", 35000, "hogar"),
    ("usr_6", 62000, "tecnologia"),
]

# Etapa 1: Emisor perezoso
def leer_registros(datos):
    for fila in datos:
        yield fila

# Etapa 2: Filtrado (solo compras de tecnología)
solo_tecnologia = filter(lambda c: c[2] == "tecnologia", leer_registros(registro_compras))

# Etapa 3: Transformación (extraer solo los montos)
montos_tecnologia = map(lambda c: c[1], solo_tecnologia)

# Etapa 4: Agregación con sum()
gasto_total_tec = sum(montos_tecnologia)
print(f"Gasto total en tecnología: ${gasto_total_tec}")
```

```
Gasto total en tecnología: $159000
```

## Agrupación de datos con diccionarios

Cuando la etapa de agregación requiere clasificar métricas por categoría en una sola pasada, los generadores se combinan de forma óptima con estructuras como `defaultdict`:

```python
from collections import defaultdict

resumen_por_categoria = defaultdict(int)

# Tubería que lee y acumula en una sola pasada lineal O(N)
for _, monto, categoria in leer_registros(registro_compras):
    resumen_por_categoria[categoria] += monto

for cat, total in resumen_por_categoria.items():
    print(f"Categoría {cat.capitalize()}: ${total}")
```

```
Categoría Tecnologia: $159000
Categoría Alimentos: $6000
Categoría Hogar: $35000
```

## Comparación de eficiencia: listas vs generadores

| Métrica | Enfoque imperativo con listas | Pipeline con generadores |
|---|---|---|
| **Consumo de memoria RAM** | Crece linealmente con los datos: $O(N)$ | Estrictamente constante: $O(1)$ |
| **Tiempo al primer resultado** | Lento (debe esperar que termine la lista completa) | Inmediato (apenas se procesa el primer elemento) |
| **Capacidad de procesamiento** | Limitado al tamaño de la memoria física | Ilimitado (capaz de procesar archivos de terabytes) |

> [!tip] Componer tuberías sin ejecutar cómputo
> Definir `paso1 = map(...)` y `paso2 = filter(...)` no realiza ningún cómputo en el procesador. La máquina solo comienza a evaluar las operaciones cuando un consumidor final (como un bucle `for`, `sum()` o `list()`) solicita el primer elemento.

> [!warning] Los generadores no pueden rebobinarse
> Recuerda que una vez que el pipeline se ejecuta y se calcula el total, el generador queda agotado. Si necesitas realizar otro cálculo sobre los mismos datos, debes reiniciar el generador desde la fuente.

## Preguntas de repaso

> [!question]- ¿Por qué un pipeline de procesamiento basado en generadores puede procesar archivos de 100 GB en una máquina con solo 8 GB de RAM?
> Porque los generadores leen y procesan los datos línea por línea de forma perezosa, ocupando únicamente en memoria el registro que se está transformando en ese instante.

> [!question]- ¿En qué momento exacto comienzan a ejecutarse las transformaciones declaradas con `map` y `filter` en un pipeline?
> Comienzan a ejecutarse únicamente cuando un consumidor final (como `sum()`, `next()` o un bucle `for`) solicita explícitamente el primer dato de la secuencia.

> [!question]- ¿Qué riesgo existe si se utiliza `list(mi_pipeline_de_datos)` al procesar un conjunto masivo de información?
> La función `list()` fuerza la evaluación completa y materializa todos los elementos en la memoria RAM simultáneamente, perdiendo por completo la ventaja del ahorro de memoria del generador y pudiendo agotar la memoria disponible.

> [!question]- ¿Cómo se estructuran modularmente las distintas etapas de un pipeline funcional en Python?
> Se diseñan como funciones generadoras puras o llamadas a `map`/`filter`, donde cada etapa recibe un iterable de entrada y retorna un nuevo iterador de salida, permitiendo encadenarlas mediante composición.

