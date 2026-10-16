---
ramo: "Estructuras de Datos"
tema: "Backtracking"
tags:
  - edd
  - backtracking
  - csp
  - recursion
  - origen/complemento
prerrequisitos:
  - "[[01 - Problemas de satisfacción de restricciones]]"
---

# Algoritmo de backtracking

La **fuerza bruta** asigna valores a **todas** las variables y recién al final pregunta si se cumplen las restricciones. **Backtracking** revisa las restricciones **a medida que asigna**: apenas una asignación parcial rompe una regla, deja de explorarla y **retrocede** a la variable anterior para probar su siguiente valor. Además entrega una garantía completa: si el problema tiene solución la encuentra, y si no la tiene, también lo dice.

![Idea de backtracking](adjuntos/Idea%20de%20backtracking.png)

> [!example]- Transcripción de la imagen
> "Queremos garantías sobre la existencia de soluciones": si el problema tiene solución, queremos saberlo; si no, también. Se puede responder recursivamente la pregunta "dado un problema, ¿es posible resolverlo?", aprovechando que extender una asignación parcial $(x_1, \dots, x_{k-1}) \to (x_1, \dots, x_{k-1}, x_k)$ genera una nueva instancia del problema. "Hacemos *backtracking* para la nueva instancia".

## La plantilla

![Pseudocódigo de isSolvable](adjuntos/Pseudoc%C3%B3digo%20de%20isSolvable.png)

> [!example]- Transcripción de la imagen
> input: conjunto de variables sin asignar $X$, dominios $D$, restricciones $R$. `isSolvable(X, D, R)`: 1. `if X = ∅: return true`; 2. `x ← alguna variable de X`; 3. `for v ∈ D_x:`; 4. `if x = v no rompe R:`; 5. `x ← v`; 6. `if isSolvable(X − {x}, D, R):`; 7. `return true`; 8. `x ← ∅`; 9. `return false`.

- **Caso base:** si no quedan variables sin asignar, todas cumplen las restricciones y hay solución.
- Se elige una variable y se prueban los valores de su dominio.
- Si un valor **no rompe** las restricciones, se asigna y se resuelve **recursivamente** el resto.
- Si la recursión tiene éxito, se propaga el `true`. Si no, se **deshace** la asignación (`x ← ∅`): ese es el **backtrack**, y el `for` sigue con el siguiente valor.
- Si ningún valor funciona, se retorna `false`, y es la variable **anterior** la que debe cambiar de valor.

```python
def valida(x, i, col):
    """¿Puede la reina de la fila i ir en la columna col, dado x[0..i-1]?"""
    return all(x[j] != col and abs(x[j] - col) != i - j for j in range(i))

def reinas(n, x=None, i=0):
    x = x or [0] * n
    if i == n:                       # todas las variables asignadas
        return x[:]
    for col in range(1, n + 1):      # dominio de x_i
        if valida(x, i, col):        # no rompe las restricciones
            x[i] = col
            sol = reinas(n, x, i + 1)
            if sol: return sol
            x[i] = 0                 # backtrack
    return None

print(reinas(8))                     # [1, 5, 8, 6, 3, 7, 2, 4]
```

> [!tip] Descomponer en funciones
> La plantilla es siempre la misma; lo que cambia en cada problema es **cómo validar** las restricciones. Conviene escribir esa validación como una función aparte (aquí, `valida`) y dejar la plantilla intacta.

## Complejidad

![Complejidad de backtracking](adjuntos/Complejidad%20de%20backtracking.png)

> [!example]- Transcripción de la imagen
> La complejidad de las posibles soluciones para un CSP cumple que la estrategia de fuerza bruta revisa **todas las tuplas**, $\mathcal{O}(K^n)$, y que backtracking puede revisar menos tuplas, pero sigue siendo proporcional, $\mathcal{O}(K^n)$. Es decir, asintóticamente ambas estrategias tienen la misma complejidad. "¿Cuál es más rápido en la práctica?". "No olvidar: *backtracking* es igual o más rápido que la fuerza bruta".

Con $n$ variables y dominios $D_1, \dots, D_n$ hay $|D_1| \times \dots \times |D_n|$ asignaciones posibles. Si todos los dominios tienen tamaño $K$, son $K^n$. Backtracking sigue siendo **exponencial en el peor caso**, pero en la práctica descarta ramas enteras temprano. En las 8 reinas hay $8^8 \approx 16{,}7$ millones de tuplas y solo 92 son soluciones; backtracking encuentra la primera recorriendo una fracción mínima.

Además de **decidir** si hay solución, la plantilla se adapta a otros tipos de problema. Para **contar** soluciones, en vez de retornar al encontrar una, se suman. Para **buscar**, se retorna la asignación. Para **optimizar** hay que recorrer todas las soluciones y comparar, y ahí backtracking suele dejar de ser buena opción.

## Preguntas de repaso

> [!question]- ¿En qué se diferencia backtracking de la fuerza bruta?
> La fuerza bruta completa cada asignación y recién entonces verifica las restricciones. Backtracking verifica en cada paso y abandona una asignación parcial apenas rompe una restricción, sin explorar sus extensiones.

> [!question]- ¿Qué línea de la plantilla es el "retroceso" y qué pasa después?
> `x ← ∅`, cuando la llamada recursiva falló. Se deshace la asignación y el `for` prueba el siguiente valor del dominio. Si no quedan valores, se retorna `false` y retrocede la variable anterior.

> [!question]- ¿Por qué backtracking tiene la misma complejidad asintótica que la fuerza bruta?
> Porque en el peor caso las restricciones fallan tarde y hay que explorar casi todas las $K^n$ tuplas. Lo que mejora es el caso práctico, gracias a las ramas que se cortan.

> [!question]- ¿Cómo se modifica la plantilla para contar todas las soluciones?
> En el caso base se retorna 1, y en el `for` se suman los resultados de todas las llamadas recursivas en vez de retornar la primera que tiene éxito.
