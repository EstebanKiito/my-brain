---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Literales, cláusulas y formas normales DNF y CNF]]"
  - "[[07 - Demostraciones por resolución y completitud]]"
---

# Ejercicios de ayudantías de satisfacibilidad y resolución

Cinco ejercicios de ayudantía sobre formas normales, redundancia de conjuntos, resolución y consecuencia entre fórmulas. Todas las tablas de verdad, equivalencias y consecuencias de las soluciones se comprobaron revisando todas las valuaciones. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. DNF y CNF de una implicación
Encuentre fórmulas en DNF y en CNF equivalentes a $(p \land q) \to (r \land \neg q)$.

> [!example]- Solución
> La fórmula vale $0$ solo cuando $p = q = 1$ (el antecedente es verdadero y $r \land \neg q$ es falso porque $q = 1$), es decir en $(1,1,0)$ y $(1,1,1)$.
>
> **DNF:** una conjunción por cada fila verdadera, seis en total:
> $(\neg p \land \neg q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land \neg r) \lor (p \land \neg q \land r)$.
>
> **CNF:** se niega la DNF de las filas falsas, $\neg\big((p \land q \land \neg r) \lor (p \land q \land r)\big)$, y De Morgan da $(\neg p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor \neg r)$. Ambas formas se pueden simplificar mucho: la fórmula es equivalente a $\neg p \lor \neg q$.

### 2. Conjuntos redundantes
Un conjunto $\Sigma$ es **redundante** si existe $\alpha \in \Sigma$ con $\Sigma \setminus \{\alpha\} \models \alpha$, y **redundante de a pares** si existen $\alpha \neq \beta$ en $\Sigma$ con $\{\alpha\} \models \beta$. Demuestre: (a) si $\Sigma$ tiene dos fórmulas distintas equivalentes, es redundante; (b) redundante de a pares implica redundante; (c) redundante no implica redundante de a pares.

> [!example]- Solución
> (a) Sean $\alpha \neq \beta$ en $\Sigma$ con $\alpha \equiv \beta$. Si $\sigma$ satisface $\Sigma \setminus \{\alpha\}$, satisface $\beta$ (que está ahí), y por la equivalencia también $\alpha$. Luego $\Sigma \setminus \{\alpha\} \models \alpha$.
>
> (b) Sean $\alpha \neq \beta$ con $\alpha \models \beta$. Si $\sigma$ satisface $\Sigma \setminus \{\beta\}$, satisface $\alpha$, y de $\alpha \models \beta$ también $\beta$. Luego $\Sigma \setminus \{\beta\} \models \beta$.
>
> (c) Contraejemplo: $\Sigma = \{p, q, p \leftrightarrow q\}$. Es redundante: la única valuación que satisface $\{p, q\}$ es $p = q = 1$, que satisface $p \leftrightarrow q$. Pero ninguna fórmula implica a otra por sí sola: $p \not\models q$ (con $p=1, q=0$), $p \not\models p \leftrightarrow q$ (misma valuación), $q \not\models p$ y $q \not\models p \leftrightarrow q$ ($p=0, q=1$), $p \leftrightarrow q \not\models p$ y $p \leftrightarrow q \not\models q$ ($p = q = 0$).

### 3. Resolución con el o exclusivo
Demuestre por resolución que $\Sigma = \{p \leftrightarrow q,\; p \oplus q\}$ es inconsistente, con $\oplus$ la disyunción exclusiva (verdadera si exactamente uno de los dos lo es).

> [!example]- Solución
> A cláusulas: $p \leftrightarrow q \equiv (\neg p \lor q) \land (\neg q \lor p)$ y $p \oplus q \equiv (p \lor q) \land (\neg p \lor \neg q)$. El conjunto de cláusulas es $\{\neg p \lor q,\; p \lor \neg q,\; p \lor q,\; \neg p \lor \neg q\}$.
>
> | Paso | Cláusula | Justificación |
> |---|---|---|
> | (1) | $\neg p \lor q$ | $\in \Sigma$ |
> | (2) | $p \lor q$ | $\in \Sigma$ |
> | (3) | $q$ | resolución de (1), (2) |
> | (4) | $p \lor \neg q$ | $\in \Sigma$ |
> | (5) | $p$ | resolución de (3), (4) |
> | (6) | $\neg p \lor \neg q$ | $\in \Sigma$ |
> | (7) | $\neg q$ | resolución de (5), (6) |
> | (8) | $\square$ | resolución de (3), (7) |

### 4. Modus tollens y razonamiento por casos mediante resolución
Pruebe por resolución (a) $\{\neg q,\; p \to q\} \models \neg p$ y (b) $\{p \lor q,\; p \to r,\; q \to r\} \models r$.

> [!example]- Solución
> (a) Se agrega $\neg\neg p \equiv p$. Cláusulas: $\{\neg q,\; \neg p \lor q,\; p\}$. Resolviendo $p$ con $\neg p \lor q$ se obtiene $q$; con $\neg q$ se llega a $\square$.
>
> (b) Se agrega $\neg r$. Cláusulas: $\{p \lor q,\; \neg p \lor r,\; \neg q \lor r,\; \neg r\}$. De $p \lor q$ y $\neg p \lor r$ sale $q \lor r$; con $\neg q \lor r$ sale $r \lor r$; factorizando, $r$; con $\neg r$ sale $\square$. Es la versión chica de la demostración por partes.

### 5. Cadenas de consecuencias y cantidad de modelos
Sea $\alpha_1 \models \alpha_2 \models \dots \models \alpha_n$ una cadena de fórmulas sobre las mismas variables. Demuestre que si $\alpha_1$ y $\alpha_n$ son satisfechas por la **misma cantidad** de valuaciones, todas las $\alpha_i$ son equivalentes.

> [!example]- Solución
> Sea $N(\alpha)$ la cantidad de valuaciones que satisfacen $\alpha$. Como $\alpha_i \models \alpha_{i+1}$, toda valuación que satisface $\alpha_i$ satisface $\alpha_{i+1}$, así que $N(\alpha_i) \le N(\alpha_{i+1})$ y el conjunto de modelos de $\alpha_i$ está contenido en el de $\alpha_{i+1}$. Entonces $N(\alpha_1) \le \dots \le N(\alpha_n)$ y, como los extremos coinciden, todos los $N(\alpha_i)$ son iguales. Un conjunto finito contenido en otro del mismo tamaño es igual a él: los modelos de $\alpha_i$ y $\alpha_{i+1}$ coinciden, luego son equivalentes, y por encadenamiento todas lo son.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 2c hace falta más de una premisa para producir la fórmula redundante?
> Porque $p \leftrightarrow q$ se deduce del conjunto $\{p, q\}$ completo, pero de cada una por separado no: la consecuencia depende de usar las dos premisas juntas.

> [!question]- ¿Por qué en el ejercicio 3 el paso (8) usa (3) y (7)?
> Porque son $q$ y $\neg q$: dos cláusulas de un solo literal complementario, cuya resolución da la cláusula vacía.

> [!question]- ¿Qué tienen en común los ejercicios 4 y 5 con el teorema de consecuencia e inconsistencia?
> El 4 lo usa de forma explícita (se agrega la negación de la conclusión). El 5 usa la definición de consecuencia: modelos de una fórmula incluidos en los de la siguiente.
