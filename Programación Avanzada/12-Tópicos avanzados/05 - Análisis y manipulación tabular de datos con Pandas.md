---
ramo: "Programación Avanzada"
tema: "Tópicos avanzados"
tags:
  - programacion/pandas
  - programacion/ciencia-de-datos
  - origen/complemento
prerrequisitos:
  - "[[04 - Computación numérica con NumPy ndarrays vectorización y broadcasting]]"
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
---

# Análisis y manipulación tabular de datos con Pandas

Gran parte de la información en el desarrollo de software y la ciencia de datos reside en formato tabular: tablas de bases de datos relacionales, hojas de cálculo de Excel o archivos CSV. Si bien NumPy provee arreglos numéricos ultrarrápidos, carece de etiquetas de texto para columnas, manejo nativo de datos heterogéneos y operaciones de agrupamiento tipo SQL. **Pandas** proporciona la estructura definitiva para este trabajo: el **DataFrame**.

## Estructuras fundamentales: Series y DataFrame

- **`Series`:** arreglo unidimensional etiquetado capaz de almacenar cualquier tipo de dato, indexado por etiquetas. Equivale a una columna individual.
- **`DataFrame`:** estructura bidimensional tabular (filas y columnas) donde cada columna es una `Series` que comparte un índice común de filas.

```python
import pandas as pd

# Creación de un DataFrame a partir de un diccionario de listas
datos = {
    "nombre": ["Camila", "Mateo", "Valentina", "Lucas"],
    "carrera": ["Computación", "Civil", "Computación", "Industrial"],
    "nota": [6.5, 5.2, 6.8, 4.8],
    "edad": [21, 22, 20, 23]
}

df = pd.DataFrame(datos)
```

## Exploración, Selección e Indexación

### 1. Métodos rápidos de exploración
- `df.head(n)` / `df.tail(n)`: previsualiza las primeras o últimas $n$ filas.
- `df.info()`: resume tipos de datos y cantidad de valores no nulos por columna.
- `df.describe()`: genera estadísticas descriptivas básicas (media, desviación, cuartiles).
- `df.shape`: retorna una tupla con `(filas, columnas)`.

### 2. Acceso a datos: loc e iloc
- **`.loc[filas, columnas]`:** selección basada en **etiquetas o nombres** (por ejemplo `df.loc[0, "nombre"]` retorna `"Camila"`).
- **`.iloc[filas, columnas]`:** selección basada en **posiciones enteras numéricas** (por ejemplo `df.iloc[0:2, 0:3]` selecciona las primeras 2 filas y 3 columnas).

## Filtrado booleano y creación de columnas

Para filtrar filas se aplican condiciones lógicas vectorizadas. En Pandas, los operadores lógicos estándar son `&` (AND), `|` (OR) y `~` (NOT), y **cada condición debe ir obligatoriamente entre paréntesis**:

```python
import pandas as pd

# Filtrar estudiantes de Computación con nota mayor o igual a 6.0
seleccion = df[(df["carrera"] == "Computación") & (df["nota"] >= 6.0)]

# Añadir una nueva columna calculada de forma vectorizada
df["aprobado"] = df["nota"] >= 5.0
```

## Agrupación de datos con groupby()

El método **`groupby()`** implementa el patrón clásico *Dividir-Aplicar-Combinar* (*Split-Apply-Combine*):

```python
import pandas as pd

# Calcular el promedio de notas y la cantidad de alumnos por carrera
resumen_carreras = df.groupby("carrera")["nota"].agg(["mean", "count"])
```

## Persistencia de datos en disco

```python
import pandas as pd

# Guardar en archivo CSV sin incluir la columna de índices numéricos
df.to_csv("alumnos.csv", index=False)

# Cargar datos desde un archivo CSV
df_leido = pd.read_csv("alumnos.csv")
```

> [!warning] Paréntesis obligatorios en filtros compuestos
> Escribir `df[df["edad"] > 18 & df["nota"] > 5]` arroja un error `ValueError` debido a la precedencia del operador bitwise `&`. Encapsula siempre cada subcondición entre paréntesis: `df[(df["edad"] > 18) & (df["nota"] > 5)]`.

> [!tip] Limpieza de valores nulos (NaN)
> Para manejar datos incompletos en un dataset, utiliza **`df.isna().sum()`** para contar nulos por columna, **`df.dropna()`** para descartar filas con celdas vacías, o **`df.fillna(valor)`** para imputar datos faltantes.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia fundamental entre una `Series` y un `DataFrame` en Pandas?
> Una `Series` es una estructura unidimensional que representa una sola columna etiquetada, mientras que un `DataFrame` es una tabla bidimensional compuesta por múltiples `Series` que comparten un mismo índice de filas.

> [!question]- ¿En qué se diferencian los métodos de selección `.loc` e `.iloc`?
> `.loc` selecciona filas y columnas utilizando sus nombres o etiquetas declaradas, mientras que `.iloc` selecciona estrictamente por la posición entera numérica de índice base cero.

> [!question]- ¿Por qué es obligatorio usar paréntesis en filtros booleanos con múltiples condiciones como `(df['A'] > 2) & (df['B'] < 5)`?
> Porque en Python el operador `&` tiene mayor precedencia matemática que los operadores de comparación (`>`, `<`), por lo que sin paréntesis la expresión intentaría evaluar `2 & df['B']` primero y fallará.

> [!question]- ¿Qué operación realiza el método `df.groupby('categoria')['precio'].mean()`?
> Divide el DataFrame en grupos según los valores únicos de la columna `'categoria'`, calcula el promedio aritmético de la columna `'precio'` para cada grupo por separado y combina el resultado en una nueva `Series`.
