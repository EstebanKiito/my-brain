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

<!-- Conjunto cuociente, órdenes y elementos extremos -->
Dudas:
- ℹ️ **Cuociente de N por ≡4 con negativos.** La clase lista $-4,-3,\dots$ en las clases de $\mathbb{N}/{\equiv_4}$; en la nota se usa $\mathbb{Z}/{\equiv_4}$ para los ejemplos con negativos (la figura de la clase mantiene el rótulo $\mathbb{N}/{\equiv_4}$).
- 🟡 **Pauta 2015-2 I2 (preorden por ínfimo y supremo).** La pauta propone $S = \{\emptyset,\{1\},\{2\},\{1,2\}\}$, pero $\inf$ y $\sup$ de $\emptyset$ no están definidos en $\mathbb{N}$; la nota usa $S = \{\{1\},\{2\},\{1,2\}\}$, verificado por enumeración.
- 🟡 **Pauta examen 2016-2 (orden de subcadena).** La pauta dice que hay mínimo sólo si $|\Sigma| = 1$ (excluyendo $\varepsilon$); la nota considera $\Sigma^*$ con la palabra vacía, que es mínimo (verificado: $\varepsilon$ es subcadena de todas) y deja la otra lectura entre paréntesis.
- ℹ️ **Contenidos sin figuras en la clase.** La clase no trae diagramas de Hasse ni orden lexicográfico; los Hasse y el grafo con lazos vienen de los apuntes y el orden lexicográfico se tomó de una pregunta de interrogación (2022-2).

<!-- Lógica de predicados y métodos de demostración -->
Dudas:
- ✅ **Ayudantía I1, modelamiento de primos.** La solución de la ayudantía escribe sólo `Entre(x, z, y)` sin exigir x≠y ni considerar y<x; con eso la oración es falsa (x=7, y=5). En la nota se corrigió (x≠y y ambos órdenes) y se verificó por cálculo.
- ✅ **2019-2-i1-4, banco.** El resumen dice que ≤ satisface c) pero habla de I2 ambiguamente; en la nota se dan I1 e I2 explícitos para a), b), c), verificados.
- ℹ️ **Ayudantía 3 y 4 (predicados).** Sólo hay 4 ejercicios de predicados en ayudantías (cahuín, Σ⊨φ ⟺ Σ∪{¬φ} inconsistente, simétrica+transitiva⊨refleja, primos); las clases no traen ejercicios de métodos de demostración en ayudantía.
- ℹ️ **Clases 07-08 sin figuras.** Son diapositivas de texto; no se generaron imágenes.
