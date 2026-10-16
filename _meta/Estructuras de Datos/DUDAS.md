# Dudas y posibles errores en los apuntes originales — Estructuras de Datos (IIC2133)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Ordenamiento elemental
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Ordenar para buscar y selection sort\|Ordenar para buscar y selection sort]] | Captura de la slide: $n + (n-1) + \dots + 1 = \sum_{i=1}^{n} i = \frac{n(n-1)}{2}$ | Esa suma vale $\frac{n(n+1)}{2}$. Lo que vale $\frac{n(n-1)}{2}$ es el número de comparaciones del pseudocódigo ($n-1 + \dots + 1$). La nota da el conteo correcto y la transcripción respeta la imagen. La conclusión $O(n^2)$ no cambia. |

## Heaps y colas de prioridad
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Inserción y extracción en un heap\|Inserción y extracción en un heap]] | Pseudocódigo de SiftUp: `j ← ⌊i/2⌋` | Con índices desde 0 (como en el resto del material, hijos en $2k+1$ y $2k+2$), el padre es $\lfloor (i-1)/2 \rfloor$; $\lfloor i/2 \rfloor$ corresponde a índices desde 1. La nota usa $\lfloor (i-1)/2 \rfloor$ y advierte sobre las dos convenciones. |
| ℹ️ | (tema completo) | Apuntes: videos `.mov` (BuildHeap, Partition) enlazados como URL temporales de Notion (`prod-files-secure.s3…`) | Son enlaces firmados que expiran y no vienen en el export. No se migran; el contenido equivalente está en las animaciones GIF y en el pseudocódigo. |
