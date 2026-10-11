---
ramo: Bases de Datos
tema: Evaluación de consultas
tags: [bd/evaluacion, origen/complemento]
prerrequisitos: ["[[04 - Block nested loop join|Block nested loop join]]"]
---
# External merge sort

Algoritmo para **ordenar tablas mucho más grandes que la RAM**: crea *runs* ordenados que caben en memoria y luego los mezcla por fases, escribiendo resultados intermedios a disco. Lo usa el DBMS para `ORDER BY`, `DISTINCT`, `GROUP BY` y sort-merge join.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 10: Evaluación de consultas")
> Los algoritmos de sorting ya son conocidos. ¿Por qué estudiarlos otra vez? Porque en una base de datos hay que ordenar tuplas que **exceden por mucho el tamaño de la RAM**.
>
> Un **run** es una secuencia de páginas que contiene un conjunto ordenado de tuplas. El algoritmo funciona por fases:
> - **Fase 0:** crear los runs iniciales (traer páginas a memoria, ordenarlas y escribirlas).
> - **Fase i:** traer runs a memoria, hacer el **merge** de cada par de runs y almacenar el nuevo run en disco (se materializan los resultados intermedios).
>
> ```mermaid
> flowchart TB
>   subgraph F0["Fase 0: runs de 1 página (cada página ordenada)"]
>     a[3,4] --- b[2,6] --- c[4,9] --- d[7,8]
>   end
>   subgraph F1[Fase 1: merge de pares]
>     e[2,3,4,6] --- f[4,7,8,9]
>   end
>   subgraph F2[Fase 2]
>     g[2,3,4,4,6,7,8,9]
>   end
>   F0 --> F1 --> F2
> ```

> [!tip] Complemento — costo (Ramakrishnan y Gehrke, cap. 13)
> Para N páginas, con merge de a 2 (2-way):
> - Número de fases: $\lceil \log_2 N \rceil + 1$.
> - En cada fase se lee y se escribe cada página: $2N$ I/O.
> - **Costo total:** $2N \cdot (\lceil \log_2 N \rceil + 1)$.
>
> Con $B$ páginas de buffer se mezclan $B-1$ runs a la vez (merge de $B-1$ vías) y la fase 0 crea runs de $B$ páginas. El número de fases baja a $1 + \lceil \log_{B-1} \lceil N/B \rceil \rceil$: con buffers razonables, casi cualquier tabla se ordena en **2 o 3 fases**.
>
> Ejemplo: N = 8 páginas, 2-way → 4 fases → $2 \cdot 8 \cdot 4 = 64$ I/O.

## Preguntas de repaso

1. ¿Por qué un DBMS no usa un sort normal en memoria?
> [!question]- Respuesta
> Porque las tablas pueden ser mucho más grandes que la RAM. Hay que ordenar por partes y mezclar usando el disco.

2. ¿Qué es un run y qué se hace en la fase 0?
> [!question]- Respuesta
> Un run es una secuencia de páginas con tuplas ordenadas. En la fase 0 se crean los runs iniciales: cada grupo de páginas que cabe en memoria se ordena y se escribe.

3. ¿Cuál es el costo del external merge sort 2-way sobre N páginas?
> [!question]- Respuesta
> $2N \cdot (\lceil \log_2 N \rceil + 1)$ I/O: en cada fase se lee y escribe cada página.

4. Nombra tres operaciones SQL que pueden requerir ordenar.
> [!question]- Respuesta
> `ORDER BY`, `DISTINCT` y `GROUP BY` (y también el sort-merge join).
