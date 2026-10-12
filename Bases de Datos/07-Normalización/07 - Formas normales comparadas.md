---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[03 - Primera forma normal|Primera forma normal]]", "[[04 - Segunda forma normal|Segunda forma normal]]", "[[05 - Tercera forma normal|Tercera forma normal]]", "[[06 - Forma normal de Boyce-Codd|Forma normal de Boyce-Codd]]"]
---
# Formas normales comparadas

Tabla para repasar qué exige cada forma normal, de la más débil (1NF) a la más fuerte (BCNF).

## Resumen de dependencias y formas normales (mis apuntes)

| Forma Normal | Condiciones |
|---|---|
| 1NF | Atributos atómicos y registros únicos |
| 2NF | En 1NF y sin dependencias parciales |
| 3NF | En 2NF y sin dependencias transitivas |
| BCNF | En 3NF y cada determinante es una superllave |

> [!tip] Complemento — qué elimina cada una y con qué ejemplo
> | Forma | Prohíbe | Ejemplo de violación (mis apuntes) | Arreglo |
> |---|---|---|---|
> | 1NF | listas o grupos en una celda | Transacciones de Isaac en una celda | una fila por transacción |
> | 2NF | atributo no clave que depende de **parte** de la llave | Fabricante → País con llave (Fabricante, Modelo) | separar (Fabricante, País) |
> | 3NF | atributo no clave que depende de **otro no clave** | País → Continente | separar (País, Continente) |
> | BCNF | **cualquier** X → Y con X no superllave | Profesor → Aula | separar (Profesor, Aula) |
>
> **En la práctica (slides "Clase 7"):** se parte de tablas posiblemente mal diseñadas, se identifican las dependencias funcionales y se intenta descomponer en **BCNF**. Si con eso se pierden dependencias, se usa **3NF**. El algoritmo está en [[08 - Descomposición en BCNF y 3NF|Descomposición en BCNF y 3NF]].
>
> Regla mnemotécnica clásica: cada atributo no clave debe depender "de la llave (1NF), de toda la llave (2NF) y de nada más que la llave (3NF)". BCNF extiende la última regla a **todos** los atributos.

## Preguntas de repaso

1. Ordena 1NF, 2NF, 3NF y BCNF de menos a más restrictiva.
> [!question]- Respuesta
> 1NF ⊃ 2NF ⊃ 3NF ⊃ BCNF: cada una exige lo de la anterior y algo más.

2. ¿Qué tipo de dependencia elimina 2NF y cuál 3NF?
> [!question]- Respuesta
> 2NF elimina las dependencias parciales (de parte de la llave). 3NF elimina las transitivas (de un atributo no clave hacia otro).

3. Si una tabla está en BCNF, ¿está en 3NF?
> [!question]- Respuesta
> Sí. Toda tabla en BCNF está en 3NF, pero no toda tabla en 3NF está en BCNF.
