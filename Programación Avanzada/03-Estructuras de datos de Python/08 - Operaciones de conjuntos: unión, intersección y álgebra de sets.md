---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/sets
  - origen/complemento
prerrequisitos:
  - "[[07 - Sets: conjuntos únicos y pertenencia]]"
---

# Operaciones de conjuntos: unión, intersección y álgebra de sets

En muchas aplicaciones prácticas necesitamos comparar grupos de datos: identificar qué usuarios tienen gustos en común, encontrar los alumnos inscritos en dos cursos simultáneamente o filtrar los permisos que un usuario todavía no posee.

## Álgebra de conjuntos en Python

Python implementa de forma nativa las operaciones matemáticas del álgebra de conjuntos. Todas estas operaciones retornan un **nuevo conjunto** sin modificar los conjuntos originales:

```python
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
```

### 1. Unión ($A \cup B$)
Contiene todos los elementos presentes en el primer conjunto, en el segundo o en ambos. Se expresa con el operador tubería **`|`** o el método **`union()`**:

```python
union = grupo_a | grupo_b
print(f"Unión: {union}")
```

```
Unión: {1, 2, 3, 4, 5, 6}
```

### 2. Intersección ($A \cap B$)
Contiene únicamente los elementos que están presentes simultáneamente en ambos conjuntos. Se expresa con el operador ampersand **`&`** o el método **`intersection()`**:

```python
interseccion = grupo_a & grupo_b
print(f"Intersección: {interseccion}")
```

```
Intersección: {3, 4}
```

### 3. Diferencia ($A \setminus B$)
Contiene los elementos que pertenecen al primer conjunto pero que **no están** en el segundo. Se expresa con el operador menos **`-`** o el método **`difference()`**. En esta operación el orden de los operandos altera el resultado:

```python
solo_a = grupo_a - grupo_b
solo_b = grupo_b - grupo_a
print(f"Solo en A: {solo_a}")
print(f"Solo en B: {solo_b}")
```

```
Solo en A: {1, 2}
Solo en B: {5, 6}
```

### 4. Diferencia simétrica ($A \triangle B$)
Contiene los elementos que están en uno de los conjuntos o en el otro, pero **no en ambos**. Se expresa con el operador intercalación **`^`** o el método **`symmetric_difference()`**:

```python
dif_simetrica = grupo_a ^ grupo_b
print(f"Diferencia simétrica: {dif_simetrica}")
```

```
Diferencia simétrica: {1, 2, 5, 6}
```

## Operadores vs Métodos de conjunto

Existe una diferencia práctica clave entre usar operadores simbólicos y métodos con nombre:

- **Operadores (`|`, `&`, `-`, `^`):** exigen estrictamente que ambos operandos sean instancias de `set`.
- **Métodos (`.union()`, `.intersection()`, etc.):** aceptan **cualquier iterable** como argumento (listas, tuplas, cadenas o diccionarios), transformándolo internamente:

```python
s = {1, 2, 3}
# s | [3, 4, 5]  # TypeError: unsupported operand type(s) for |: 'set' and 'list'
resultado = s.union([3, 4, 5])  # Válido
print(resultado)
```

```
{1, 2, 3, 4, 5}
```

## Comparación y relaciones de inclusión

Podemos verificar la relación de contención entre dos conjuntos mediante operadores relacionales o métodos semánticos:

| Relación matemática | Operador | Método Python | Significado |
|---|---|---|---|
| **Subconjunto** | `A <= B` | `A.issubset(B)` | Todo elemento de `A` pertenece a `B` |
| **Subconjunto propio** | `A < B` | – | `A <= B` y además `A != B` |
| **Superconjunto** | `A >= B` | `A.issuperset(B)` | `A` contiene a todos los elementos de `B` |
| **Disjuntos** | – | `A.isdisjoint(B)` | `A` y `B` no tienen ningún elemento en común |

```python
docentes = {"Valeria", "Rodrigo", "Hernán", "Daniela"}
coordinadores = {"Hernán", "Daniela"}

print(f"¿Son subconjunto?: {coordinadores <= docentes}")
print(f"¿Son disjuntos?:   {coordinadores.isdisjoint({'Claudio', 'Beatriz'})}")
```

```
¿Son subconjunto?: True
¿Son disjuntos?:   True
```

> [!tip] Comprobar elementos en común en una sola línea
> Para saber si dos colecciones comparten al menos un elemento de forma eficiente, basta con comprobar `if not a.isdisjoint(b):` o evaluar si la intersección es no vacía: `bool(a & b)`.

## Preguntas de repaso

> [!question]- ¿Por qué `A - B` y `B - A` entregan resultados diferentes en la diferencia de conjuntos?
> Porque la diferencia no es conmutativa: `A - B` retiene los elementos exclusivos de `A` eliminando los que coinciden con `B`, mientras que `B - A` retiene exclusivamente los elementos de `B` que no están en `A`.

> [!question]- ¿Qué ventaja práctica ofrecen los métodos como `s.union(iterable)` frente al operador `s | otro_set`?
> Los métodos permiten pasar como argumento cualquier iterable (como listas, tuplas o generadores) sin necesidad de convertirlos previamente a conjunto de forma explícita.

> [!question]- ¿Qué expresa la diferencia simétrica `A ^ B` en términos de unión e intersección?
> Es equivalente a la unión de ambos conjuntos menos su intersección: $(A \cup B) - (A \cap B)$.

> [!question]- ¿Qué condición debe cumplirse para que el método `A.isdisjoint(B)` retorne `True`?
> Que la intersección entre `A` y `B` sea vacía ($A \cap B = \emptyset$), es decir, que no compartan ningún elemento en común.
