---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/funcional
  - programacion/itertools
  - origen/complemento
prerrequisitos:
  - "[[04 - Protocolo de iteración: iterables, iteradores y StopIteration]]"
  - "[[05 - Generadores y la palabra clave yield]]"
---

# Herramientas de iteración: itertools y combinatoria

Al trabajar con colecciones complejas, generar permutaciones, cortar flujos infinitos de datos o combinar múltiples secuencias de manera eficiente, implementar la lógica con bucles anidados manuales es lento y proclive a errores.

## El módulo itertools

El módulo estándar **`itertools`** contiene una colección de funciones optimizadas implementadas en lenguaje C para construir y manipular iteradores de alto rendimiento y bajo consumo de memoria.

Se dividen principalmente en tres familias: iteradores infinitos, procesadores de secuencias y combinatoria.

## 1. Iteradores infinitos y controlados

- **`count(start, step)`:** genera una progresión aritmética infinita:
- **`cycle(iterable)`:** recorre una colección y, al llegar al final, vuelve a comenzar desde el primer elemento indefinidamente:
- **`islice(iterable, start, stop[, step])`:** permite aplicar particionamiento (*slicing*) sobre cualquier iterador o generador sin cargarlo en memoria:

```python
import itertools

# Generador infinito de turnos: A, B, C, A, B, C...
turnos = itertools.cycle(["Equipo Rojo", "Equipo Azul"])

# islice corta los primeros 4 elementos de la secuencia infinita
primeros_turnos = list(itertools.islice(turnos, 4))
print(f"Primeros 4 turnos: {primeros_turnos}")

# count con paso de 5
multiplos_cinco = itertools.islice(itertools.count(start=0, step=5), 5)
print(f"Primeros múltiplos de 5: {list(multiplos_cinco)}")
```

```
Primeros 4 turnos: ['Equipo Rojo', 'Equipo Azul', 'Equipo Rojo', 'Equipo Azul']
Primeros múltiplos de 5: [0, 5, 10, 15, 20]
```

## 2. Combinación y concatenación: chain y compress

- **`chain(*iterables)`:** une múltiples colecciones en una sola secuencia lineal continua, pasando a la siguiente colección solo cuando la anterior se agota:
- **`compress(datos, mascara)`:** filtra elementos reteniendo solo aquellos cuya posición correspondiente en la máscara booleana sea verdadera:

```python
import itertools

grupo1 = [1, 2, 3]
grupo2 = [4, 5, 6]

# Concatena sin crear una lista nueva intermedia
unidos = list(itertools.chain(grupo1, grupo2))
print(f"Secuencia unida con chain: {unidos}")

# Filtrado selectivo con máscara
letras = ["A", "B", "C", "D"]
mascara = [True, False, True, False]
seleccionados = list(itertools.compress(letras, mascara))
print(f"Filtrados con compress: {seleccionados}")
```

```
Secuencia unida con chain: [1, 2, 3, 4, 5, 6]
Filtrados con compress: ['A', 'C']
```

## 3. Combinatoria: product, permutations y combinations

| Función | Operación matemática | ¿Importa el orden? | ¿Admite repetición? |
|---|---|---|---|
| **`product(A, B)`** | Producto cartesiano ($A \times B$) | Sí | Sí |
| **`permutations(A, r)`** | Permutaciones de $r$ elementos | Sí | No |
| **`combinations(A, r)`** | Combinaciones de $r$ elementos | No | No |

```python
import itertools

opciones = ["A", "B", "C"]

permutaciones = list(itertools.permutations(opciones, 2))
combinaciones = list(itertools.combinations(opciones, 2))

print(f"Permutaciones (orden importa): {permutaciones}")
print(f"Combinaciones (orden ignora):  {combinaciones}")
```

```
Permutaciones (orden importa): [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
Combinaciones (orden ignora):  [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

## Predicados globales con cortocircuito: all() y any()

- **`all(iterable)`:** retorna `True` si **todos** los elementos evalúan a verdadero; si encuentra un `False`, se detiene de inmediato (cortocircuito).
- **`any(iterable)`:** retorna `True` si **al menos uno** de los elementos evalúa a verdadero; se detiene inmediatamente al encontrar el primer `True`:

```python
notas = [5.5, 6.0, 4.2, 3.8]

todos_aprobados = all(n >= 4.0 for n in notas)
algun_distinguido = any(n >= 6.5 for n in notas)

print(f"¿Aprobaron todos?: {todos_aprobados}")
print(f"¿Hay alguien sobre 6.5?: {algun_distinguido}")
```

```
¿Aprobaron todos?: False
¿Hay alguien sobre 6.5?: False
```

> [!tip] Cortocircuito para ahorrar cómputo
> Combinar `any()` o `all()` con expresiones generadoras evita evaluar elementos innecesarios: `any(es_primo(x) for x in lista)` dejará de ejecutar la costosa función `es_primo` tan pronto encuentre el primer número primo.

## Preguntas de repaso

> [!question]- ¿Qué ventaja ofrece `itertools.chain(lista1, lista2)` frente al operador suma `lista1 + lista2`?
> `lista1 + lista2` crea y reserva memoria para una tercera lista intermedia que duplica los datos; `itertools.chain` produce un iterador que lee secuencialmente de una y luego de otra sin consumir memoria adicional.

> [!question]- ¿Por qué no se puede aplicar la sintaxis convencional de slicing `gen[0:5]` sobre un generador y se debe usar `itertools.islice`?
> Porque los generadores no almacenan elementos ni soportan indexación arbitraria; `islice` consume el generador invocando `next()` paso a paso hasta alcanzar el rango solicitado.

> [!question]- ¿Cuál es la diferencia entre `permutations(['A', 'B'], 2)` y `combinations(['A', 'B'], 2)`?
> `permutations` considera el orden relevante y genera tanto `('A', 'B')` como `('B', 'A')`; `combinations` considera que ambos pares representan el mismo subconjunto y produce únicamente `('A', 'B')`.

> [!question]- ¿Cómo opera el mecanismo de cortocircuito en la función `all()`?
> Evalúa los elementos secuencialmente y, en el instante en que un solo elemento resulta ser falso (`False`), retorna `False` de inmediato sin evaluar los elementos restantes del iterable.

