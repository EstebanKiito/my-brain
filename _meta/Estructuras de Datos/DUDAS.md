# Dudas y posibles errores en los apuntes originales — Estructuras de Datos (IIC2133)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Ordenamiento elemental
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Ordenar para buscar y selection sort\|Ordenar para buscar y selection sort]] | Captura de la slide: $n + (n-1) + \dots + 1 = \sum_{i=1}^{n} i = \frac{n(n-1)}{2}$ | Esa suma vale $\frac{n(n+1)}{2}$. Lo que vale $\frac{n(n-1)}{2}$ es el número de comparaciones del pseudocódigo ($n-1 + \dots + 1$). La nota da el conteo correcto y la transcripción respeta la imagen. La conclusión $O(n^2)$ no cambia. |
