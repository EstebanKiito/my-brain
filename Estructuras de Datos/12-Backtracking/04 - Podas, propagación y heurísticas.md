---
ramo: "Estructuras de Datos"
tema: "Backtracking"
tags:
  - edd
  - backtracking
  - poda
  - heuristicas
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmo de backtracking]]"
---

# Podas, propagación y heurísticas

El [[02 - Algoritmo de backtracking|backtracking básico]] tiene tres ineficiencias. Detecta que una asignación es inviable solo cuando una restricción explícita falla, y quizás después de muchos llamados. Revisa valores del dominio que otras asignaciones ya volvieron imposibles. Y prueba variables y valores en un orden arbitrario. Cada una se ataca con una mejora distinta, sin cambiar la estructura de la plantilla.

## Las tres mejoras

- **Podas:** se agregan **nuevas restricciones deducidas** de las originales, que se revisan junto con ellas y descartan ramas inviables antes. Por ejemplo, en una mochila, si lo que queda por cargar ya no cabe, se corta sin seguir asignando.
- **Propagación:** después de asignar una variable, se **modifican los dominios** de las demás, quitando los valores que esa asignación invalida. En las 8 reinas, al poner una reina se eliminan esa columna y esas diagonales de los dominios de las filas siguientes. Si un dominio queda vacío, la rama es inviable de inmediato.
- **Heurísticas:** son criterios (falibles) para elegir **qué variable** asignar primero y **en qué orden** probar sus valores. Si existiera un oráculo con el orden perfecto, el problema se volvería lineal. Las heurísticas intentan aproximarse a ese oráculo.

> [!tip] Heurísticas típicas
> - Partir por la **variable con el dominio más pequeño**: es la más restringida, y si va a fallar, mejor que falle pronto.
> - Probar primero el **valor con menos apariciones** (el que menos restringe a las demás variables).

## La plantilla mejorada

![isSolvable con heurísticas, poda y propagación](adjuntos/isSolvable%20con%20heur%C3%ADsticas%2C%20poda%20y%20propagaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Podemos incorporar estas mejoras según convenga en un problema particular". `isSolvable(X, D, R)`: 1. `if X = ∅: return true`; 2. `x ← la mejor variable de X`; 3. `for v ∈ D_x de mejor a peor:`; 4. `if x = v no rompe R:` (con R ampliado por las podas); 5. `x ← v, propagar`; 6. `if isSolvable(X − {x}, D, R):`; 7. `return true`; 8. `x ← ∅, propagar` (deshacer la propagación); 9. `return false`. Las partes nuevas aparecen en rojo.

> [!warning] Deshacer la propagación
> Al retroceder (línea 8), hay que **restaurar** los dominios que se habían reducido; si no, las otras ramas verían dominios incorrectos. Es el error más común al implementar propagación.

## De backtracking a algoritmo codicioso

Si la heurística elige siempre la mejor variable con su mejor valor **y nunca se retrocede**, backtracking se convierte en un **algoritmo codicioso**: más rápido, pero sin garantía de encontrar la solución o la mejor. La diferencia está en el arrepentimiento: backtracking puede deshacer una decisión y el algoritmo codicioso no. Si la estrategia codiciosa falla, backtracking con esa misma heurística igual encuentra la solución.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre una poda y la propagación?
> La poda agrega restricciones deducidas que descartan asignaciones parciales inviables. La propagación modifica los dominios de las variables pendientes después de cada asignación, eliminando valores que ya no pueden funcionar.

> [!question]- ¿Por qué conviene asignar primero la variable con el dominio más pequeño?
> Porque es la que tiene más probabilidades de fallar, y es mejor detectar ese fallo cerca de la raíz del árbol de búsqueda, donde corta más ramas, que en lo profundo.

> [!question]- ¿Qué hay que hacer con los dominios al retroceder si se usa propagación?
> Restaurarlos al estado anterior a la asignación. Si no, las ramas siguientes trabajarían con dominios reducidos por una decisión que ya se deshizo.

> [!question]- ¿Qué se obtiene si backtracking usa una heurística y nunca retrocede?
> Un algoritmo codicioso: toma la mejor decisión aparente en cada paso sin arrepentirse. Es más rápido, pero puede no encontrar solución aunque exista.
