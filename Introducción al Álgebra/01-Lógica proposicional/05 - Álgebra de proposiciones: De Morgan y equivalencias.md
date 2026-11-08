---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos:
  - "[[04 - Tautologías, contradicciones y leyes lógicas]]"
---

# Álgebra de proposiciones: De Morgan y equivalencias

Las leyes lógicas funcionan como reglas de reescritura: permiten transformar una fórmula en otra equivalente sin pasar por la tabla de verdad. Las más importantes son las **leyes de De Morgan**, que explican cómo se distribuye la negación sobre conjunciones y disyunciones.

## Leyes de De Morgan

Negar un "y" o un "o" invierte el conectivo y niega cada parte:

$$
\neg(p \wedge q) \Leftrightarrow \neg p \vee \neg q, \qquad
\neg(p \vee q) \Leftrightarrow \neg p \wedge \neg q .
$$

Así, "no es cierto que llueve y hace frío" equivale a "no llueve o no hace frío", y "no es cierto que es lunes o martes" equivale a "no es lunes y no es martes".

> [!tip] De Morgan
> La negación **no** se "reparte" dejando el conectivo igual: al negar, $\wedge$ se cambia por $\vee$ (y viceversa) y cada proposición se niega. $\neg(p \wedge q) \equiv \neg p \vee \neg q$ y $\neg(p \vee q) \equiv \neg p \wedge \neg q$.

## Conmutatividad, asociatividad y distributividad

Como en el álgebra numérica, los conectivos cumplen propiedades de reordenamiento:

| Propiedad | Equivalencias |
|---|---|
| Conmutatividad | $p \vee q \Leftrightarrow q \vee p$, $p \wedge q \Leftrightarrow q \wedge p$ |
| Asociatividad | $p \vee (q \vee r) \Leftrightarrow (p \vee q) \vee r$, $p \wedge (q \wedge r) \Leftrightarrow (p \wedge q) \wedge r$ |
| Distributividad | $p \wedge (q \vee r) \Leftrightarrow (p \wedge q) \vee (p \wedge r)$, $p \vee (q \wedge r) \Leftrightarrow (p \vee q) \wedge (p \vee r)$ |

Nota que, a diferencia de la aritmética, aquí **ambas** distributividades valen: el "y" distribuye sobre el "o" y el "o" distribuye sobre el "y".

## Equivalencia dividida

La equivalencia se puede partir en dos implicaciones:

$$
(p \Leftrightarrow q) \Leftrightarrow \big[(p \Rightarrow q) \wedge (q \Rightarrow p)\big].
$$

Es la justificación formal de demostrar "si y solo si" probando ida y vuelta.

## Simplificar usando propiedades

**Ejemplo.** Demuestre que $(p \wedge q) \vee (p \wedge \neg q) \vee (\neg p \wedge q) \vee (\neg p \wedge \neg q) \Leftrightarrow V$.

Las cuatro conjunciones recorren todas las combinaciones de $p$ y $q$. Agrupando por la distributividad:

$$
(p \wedge q) \vee (p \wedge \neg q) \Leftrightarrow p \wedge (q \vee \neg q) \Leftrightarrow p \wedge V \Leftrightarrow p,
$$

y de manera análoga $(\neg p \wedge q) \vee (\neg p \wedge \neg q) \Leftrightarrow \neg p$. Luego la expresión original equivale a $p \vee \neg p \Leftrightarrow V$.

**Ejemplo.** Pruebe que $(p \Leftrightarrow q) \Leftrightarrow (p \wedge q) \vee (\neg p \wedge \neg q)$.

Por equivalencia dividida, $p \Leftrightarrow q$ equivale a $(p \Rightarrow q) \wedge (q \Rightarrow p)$. Aplicando la caracterización de la implicación a cada uno, $(\neg p \vee q) \wedge (\neg q \vee p)$, y distribuyendo se llega a $(p \wedge q) \vee (\neg p \wedge \neg q)$.

> [!warning] Negar correctamente
> Al negar una fórmula compuesta, la negación "entra" hasta las proposiciones y va cambiando cada conectivo. Negar $p \wedge q$ como $\neg p \wedge \neg q$ es un error: lo correcto es $\neg p \vee \neg q$.

## Preguntas de repaso

> [!question]- Simplifique $\neg(p \vee q)$ con De Morgan y verifique con un ejemplo.
> $\neg(p \vee q) \equiv \neg p \wedge \neg q$. Ejemplo: "no es cierto que hoy es lunes o martes" equivale a "hoy no es lunes y hoy no es martes".

> [!question]- ¿Por qué la equivalencia dividida permite demostrar $p \Leftrightarrow q$ en dos partes?
> Porque $p \Leftrightarrow q$ es lo mismo que $(p \Rightarrow q) \wedge (q \Rightarrow p)$: probar la ida y la vuelta es, juntas, exactamente probar la equivalencia.

> [!question]- Demuestre $p \wedge (q \vee r) \Leftrightarrow (p \wedge q) \vee (p \wedge r)$ usando tablas de verdad.
> Se construye la tabla de $2^3=8$ filas y se comprueba que la columna de $p \wedge (q \vee r)$ coincide fila a fila con la de $(p \wedge q) \vee (p \wedge r)$. Es la distributividad del "y" sobre el "o".

> [!question]- Simplifique $p \wedge (\neg p \vee q)$ usando propiedades.
> Por distributividad, $(p \wedge \neg p) \vee (p \wedge q)$, y por consistencia $p \wedge \neg p \Leftrightarrow F$, así que queda $F \vee (p \wedge q) \equiv p \wedge q$. (También se puede ver con absorción.)
