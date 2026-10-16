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

## Árboles balanceados
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[02 - Rotaciones simples y dobles en AVL\|Rotaciones simples y dobles en AVL]] | Apuntes, ejemplo M, D, H, B, A, C, S, K, I: al insertar A se marca "D −2 → Y" y "B −1 → X"; al insertar B se anota "H −1 … M 0" | El primer nodo desbalanceado al insertar A es D (X) y su hijo B es Y. La tabla de la nota se recalculó con una implementación de AVL; los pasos de H y C coinciden con el pizarrón. La traza de los apuntes queda incompleta después de C, y se completó con S, K e I. |
| ℹ️ | [[03 - Árboles 2-3\|Árboles 2-3]] | Captura del 3-nodo: hijo derecho con "$X < k'''$" | Debe ser $Y < k'''$ (mis apuntes ya lo anotaban). La transcripción respeta la imagen; la regla correcta está en la figura de orden de llaves y en el texto. |
