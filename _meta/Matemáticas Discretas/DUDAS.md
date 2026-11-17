# Dudas y posibles errores en el material original — Matemáticas Discretas (IIC1253)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido, las discrepancias entre fuentes y las pautas que no calzan con el cálculo verificado.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

<!-- Satisfacibilidad, consecuencia y resolución -->
- ℹ️ **Capacidad de jaulas (I1 2015-2).** La pauta usa "si hay tres animales en la jaula, ningún otro lo está"; en la nota se escribió la forma equivalente "no hay cuatro animales distintos en una jaula" (verificada con fuerza bruta).
- ℹ️ **Prueba de Σ⊨□ ⇔ inconsistente.** Se mantuvo el orden de la clase (los dos teoremas se enuncian en notas distintas por claridad); sin discrepancias con los apuntes.

<!-- Teoría de conjuntos -->
- ℹ️ **Figura 6.1.4 del libro.** En el cuarto diagrama (complemento) el dibujo deja sin sombrear el círculo $B$ completo, lo que corresponde a $(A\cup B)^c$ y no a $A^c$; la transcripción lo aclara. La clase no trae diagramas de Venn propios (solo texto), por eso se usó el libro.
- ℹ️ **Pares ordenados y producto cartesiano.** Esa parte aparece en la clase de relaciones (inicio) y no en la de conjuntos; se incluyó en este tema por el alcance pedido. El tema de relaciones puede enlazarla.
- ℹ️ **Ayudantía 5, solución de T(A).** La solución de la ayudante separa casos (A finito/infinito) innecesariamente y razona la unión con una enumeración $\{X_1, X_2, \dots\}$; en la nota se reescribió con el argumento directo $A\setminus\bigcup T(A) \subseteq A\setminus X$ para un $X \in T(A)$ no vacío. La intersección exige familia finita y no vacía (con $n>0$, como en la ayudantía).
- ℹ️ **Intersección generalizada de la familia vacía.** Los apuntes de Dissett la definen como el universo $U$; la clase no lo trata. Se explica como convención por vacuidad.
