---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, bd/data-science, origen/complemento]
prerrequisitos: ["[[01 - SQL desde Python con cursores|SQL desde Python con cursores]]", "[[03 - GROUP BY|GROUP BY]]"]
---
# Data Science con Pandas

Una vez que los datos están guardados y sabemos consultarlos, la **ciencia de datos** busca extraer información útil de ellos. En Python la herramienta base es **Pandas**, cuyos DataFrames se parecen a tablas y permiten hacer joins, filtros y GROUP BY en memoria.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Pandas y ciencia de datos")
> **Data Science** (según IBM): un enfoque multidisciplinario para extraer *insights* accionables de los grandes y crecientes volúmenes de datos de las organizaciones. Incluye preparar los datos, analizarlos y presentar los resultados para revelar patrones y apoyar decisiones informadas.
>
> Engloba Data Analysis, Machine Learning, Deep Learning, AI, Computer Vision, Natural Language Processing, etc. En el curso se ve **Data Analysis**: el proceso de inspección, limpieza, transformación y modelamiento de datos para extraer información relevante para un fin.
>
> ```mermaid
> flowchart LR
>   BD[(Datos en una BD)] --> ENV["Se cargan en un entorno<br/>(Jupyter, R, Tableau…)"] --> INFO["Información importante:<br/>reportes, modelos…"]
> ```
>
> **Pandas:** *"a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language"*. Lee `.xlsx`, `.xls`, `.csv`, `.tsv`, `.json` y más (https://pandas.pydata.org/docs/user_guide/io.html).
>
> **DataFrame:** tabla con **índice**, **columnas** con nombre y filas (tuplas). Tiene las operaciones de SQL:
> | SQL | Pandas |
> |---|---|
> | `SELECT * FROM t WHERE edad > 20` | `df.query("edad > 20")` o `df[df.edad > 20]` |
> | `JOIN … ON a.id = b.id` | `a.merge(b, on="id")` |
> | `GROUP BY producto` + `SUM` | `df.groupby("producto")["venta"].sum()` |
>
> ```python
> import pandas as pd, sqlite3
> conn = sqlite3.connect("cine.db")
> df = pd.read_sql("SELECT * FROM Peliculas", conn)   # de la BD a un DataFrame
> df.groupby("director")["calificacion"].mean()
> ```
>
> Cursos UC para seguir: IIC2613 Inteligencia Artificial, IIC3633 Sistemas recomendadores, IIC2433 Minería de datos, IIC3697 Aprendizaje profundo, IIC2026 Visualización de información, IIC3733 Visión por computador, IMT3120 Fundamentos matemáticos para ciencia de datos.

## Preguntas de repaso

1. ¿Qué es el análisis de datos?
> [!question]- Respuesta
> El proceso de inspeccionar, limpiar, transformar y modelar datos para extraer información relevante para un fin.

2. ¿Qué es un DataFrame de Pandas?
> [!question]- Respuesta
> Una estructura tabular en memoria, con índice, columnas con nombre y filas, sobre la que se pueden hacer filtros, joins y agrupaciones.

3. ¿Cuál es el equivalente Pandas de un `JOIN` y de un `GROUP BY`?
> [!question]- Respuesta
> `merge` para el join y `groupby(...)` seguido de una agregación (`sum`, `mean`…) para el GROUP BY.
