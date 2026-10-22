# Estructuras de datos de Python — índice

Estructuras de datos fundamentales de la biblioteca estándar de Python: clasificación entre colecciones secuenciales y no secuenciales, tuplas inmutables y `namedtuple`, pilas LIFO y colas FIFO con `deque`, diccionarios y funciones de dispersión (*hashing*), diccionarios por defecto con `defaultdict`, conjuntos (*sets*) y álgebra booleana de conjuntos, y gestión avanzada de argumentos con `*args` y `**kwargs`.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cinco notebooks de la tercera semana del curso (introducción y tuplas, stacks y colas, diccionarios, sets, y args y kwargs), complementado con las diapositivas de estructuras integradas y el libro del ramo.

## Orden de estudio
1. [[01 - Estructuras de datos y tuplas|Estructuras de datos y tuplas]]: estructuras secuenciales vs no secuenciales, tuplas inmutables, indexación, slicing y desempaquetado con `*`.
2. [[02 - Tuplas con nombre: namedtuple|Tuplas con nombre: namedtuple]]: acceso por atributos, inmutabilidad, método `_replace()` y comparación con tuplas y clases.
3. [[03 - Stacks: pilas LIFO e implementación|Stacks: pilas LIFO e implementación]]: principio LIFO, operaciones push, pop y peek con listas, historial del navegador y reversión de secuencias.
4. [[04 - Colas FIFO y deques de doble extremo|Colas FIFO y deques de doble extremo]]: principio FIFO, limitaciones de listas como colas, operaciones $O(1)$ en extremos con `collections.deque` y verificación de palíndromos.
5. [[05 - Diccionarios: llave-valor, hashing y métodos|Diccionarios: llave-valor, hashing y métodos]]: tablas hash, acceso con corchetes y `.get()`, objetos hasheables vs mutables, vistas `.items()` y comprensión.
6. [[06 - Diccionarios por defecto: defaultdict y conteos|Diccionarios por defecto: defaultdict y conteos]]: el problema de inicialización de llaves, funciones fábrica (`int`, `list`, `set`), y aplicaciones para contar y agrupar.
7. [[07 - Sets: conjuntos únicos y pertenencia|Sets: conjuntos únicos y pertenencia]]: colecciones sin duplicados, elementos hasheables, mutabilidad de sets, métodos `add`, `remove` y `discard`, y deduplicación.
8. [[08 - Operaciones de conjuntos: unión, intersección y álgebra de sets|Operaciones de conjuntos: unión, intersección y álgebra de sets]]: unión, intersección, diferencia y diferencia simétrica con operadores y métodos, y relaciones de inclusión.
9. [[09 - Parámetros y argumentos: posicionales, keywords y desempaquetado|Parámetros y argumentos: posicionales, keywords y desempaquetado]]: parámetros vs argumentos, llamadas por posición y por palabra clave, desempaquetado con `*` y `**`, y valores por defecto.
10. [[10 - Parámetros variables: args y kwargs en funciones|Parámetros variables: args y kwargs en funciones]]: captura de posicionales arbitrarios en tupla con `*args`, palabras clave en diccionario con `**kwargs`, y orden en la cabecera.
