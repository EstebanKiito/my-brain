---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[06 - Regla de resolución y factorización]]"
---

# Demostraciones por resolución y completitud

Con la regla de resolución y la factorización se arma un procedimiento completo para decidir si un conjunto de cláusulas es inconsistente, y por lo tanto para decidir consecuencia lógica. Esta nota define qué es una demostración por resolución, muestra dos trazas y explica por qué el método es confiable.

## Qué es una demostración por resolución

Una **demostración por resolución** de que $\Sigma$ es inconsistente es una secuencia de cláusulas $C_1, \dots, C_n$ tal que:

- cada $C_i$ está en $\Sigma$, o se obtiene por resolución de dos cláusulas anteriores $C_j, C_k$ ($j, k < i$), o se obtiene por factorización de una anterior $C_j$;
- la última es $C_n = \square$.

Se escribe $\Sigma \vdash \square$. Cada línea lleva su justificación ("$\in \Sigma$", "resolución de (a), (b)" o "factorización de (a)").

## Primera traza: razonamiento por casos

Sea $\Sigma = \{p \lor q \lor r,\; \neg p \lor s,\; \neg q \lor s,\; \neg r \lor s,\; \neg s\}$. Es la demostración por partes: si alguno de $p, q, r$ ocurre y cada uno lleva a $s$, entonces $s$; pero se agrega $\neg s$.

![Resolución de un conjunto con cuatro variables](adjuntos/Resolución%20de%20un%20conjunto%20con%20cuatro%20variables.png)

> [!example]- Transcripción de la imagen
> Lista numerada de 11 pasos. (1) $p \lor q \lor r$ y (2) $\neg p \lor s$ pertenecen a $\Sigma$; (3) $s \lor q \lor r$ es resolución de (1) y (2). (4) $\neg q \lor s \in \Sigma$; (5) $s \lor s \lor r$ es resolución de (3) y (4); (6) $s \lor r$ es factorización de (5). (7) $\neg r \lor s \in \Sigma$; (8) $s \lor s$ es resolución de (6) y (7); (9) $s$ es factorización de (8). (10) $\neg s \in \Sigma$; (11) $\square$ es resolución de (9) y (10).

La idea es ir "eliminando" $p$, luego $q$ y luego $r$, hasta quedar con $s$, que choca con $\neg s$. Las factorizaciones (pasos 6 y 9) fusionan las copias de $s$.

## Segunda traza: consecuencia con implicaciones anidadas

Para probar $\{p,\; q \to (p \to r)\} \models q \to r$ se siguen tres pasos:

1. Agregar la negación de la conclusión: $\neg(q \to r)$.
2. Llevar todo a CNF y separar en cláusulas: $\{p,\; \neg q \lor \neg p \lor r,\; q,\; \neg r\}$.
3. Buscar una secuencia que llegue a $\square$.

![Resolución de la consecuencia con implicaciones anidadas](adjuntos/Resolución%20de%20la%20consecuencia%20con%20implicaciones%20anidadas.png)

> [!example]- Transcripción de la imagen
> Se tiene $\Sigma = \{p, \neg q \lor \neg p \lor r, q, \neg r\}$ y la demostración: (1) $p$; (2) $\neg q \lor \neg p \lor r$; (3) $\neg q \lor r$ por resolución de (1) y (2); (4) $q$; (5) $r$ por resolución de (3) y (4); (6) $\neg r$; (7) $\square$ por resolución de (5) y (6). Las líneas (1), (2), (4) y (6) pertenecen a $\Sigma$.

## Por qué se puede confiar en el método

> [!tip] Correctitud y completitud
> Para un conjunto de cláusulas $\Sigma$: **correctitud**, si $\Sigma \vdash \square$ entonces $\Sigma \models \square$; **completitud**, si $\Sigma \models \square$ entonces $\Sigma \vdash \square$.

La correctitud sale de que cada regla es correcta: si $\Sigma$ fuera satisfacible, toda cláusula derivada también sería verdadera en esa valuación, y $\square$ no lo es. La completitud asegura que **siempre** existe una demostración cuando el conjunto es inconsistente. Juntas:

- $\Sigma$ (de cláusulas) es inconsistente si y solo si existe una demostración por resolución de ello.
- Para $\Sigma$ y $\varphi$ cualesquiera, $\Sigma \models \varphi$ si y solo si $\Sigma' \vdash \square$, donde $\Sigma'$ es un conjunto de cláusulas equivalente a $\Sigma \cup \{\neg\varphi\}$.

> [!warning] Resolución demuestra inconsistencia, no satisfacibilidad
> Si no se llega a $\square$ tras agotar las cláusulas derivables, el conjunto es satisfacible, pero el método no entrega de antemano un plan: encontrar la secuencia correcta puede requerir tanteo, y que una demostración exista no dice cuán larga es.

## Preguntas de repaso

> [!question]- ¿Por qué se parte negando la conclusión?
> Porque $\Sigma \models \varphi$ equivale a que $\Sigma \cup \{\neg\varphi\}$ sea inconsistente, y resolución solo sabe detectar inconsistencias.

> [!question]- ¿Qué garantiza la completitud que no garantiza la correctitud?
> La correctitud asegura que no se "demuestra" algo falso; la completitud, que ninguna inconsistencia queda sin demostración.

> [!question]- Si tras resolver todas las combinaciones posibles no aparece $\square$, ¿qué se concluye?
> Que el conjunto de cláusulas es satisfacible (por completitud) y, si se había agregado $\neg\varphi$, que $\varphi$ no es consecuencia de las premisas.

> [!question]- ¿Por qué en la primera traza hay pasos de factorización?
> Porque resolver (3) con (4) produce $s \lor s \lor r$, con $s$ repetido; sin fusionar los duplicados no se podría llegar a la cláusula $s$ sola.
