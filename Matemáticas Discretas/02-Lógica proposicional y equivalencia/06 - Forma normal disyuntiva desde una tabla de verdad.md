---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[05 - Leyes de equivalencia y cadenas de demostración]]"
---

# Forma normal disyuntiva desde una tabla de verdad

Hay fórmulas para todo significado posible: dada **cualquier** tabla de verdad se puede construir una fórmula que la tenga. Esto muestra que el lenguaje no deja afuera ninguna función booleana y da una forma estándar (normal) de escribir fórmulas.

## La construcción

Sea $\varphi$ una fórmula de la que solo se conoce su tabla (con variables $p, q, r$). La estrategia tiene dos pasos: codificar cada valuación en que $\varphi$ vale $1$ y combinar esas codificaciones con una disyunción.

![Construcción de la fórmula desde la tabla](adjuntos/Forma%20normal%20disyuntiva%20desde%20una%20tabla%20de%20verdad.png)

> [!example]- Transcripción de la imagen
> Dos mitades de una tabla con columnas $p, q, r, \varphi$ y filas $\sigma_1, \dots, \sigma_8$ en orden binario. $\varphi$ vale $1$ en $\sigma_1 = (0,0,0)$, $\sigma_4 = (0,1,1)$, $\sigma_5 = (1,0,0)$ y $\sigma_8 = (1,1,1)$, y $0$ en las otras. Debajo, la fórmula propuesta: $(\neg p \wedge \neg q \wedge \neg r) \vee (\neg p \wedge q \wedge r) \vee (p \wedge \neg q \wedge \neg r) \vee (p \wedge q \wedge r)$, con cada término rotulado con la valuación que codifica ($\sigma_1, \sigma_4, \sigma_5, \sigma_8$).

Cada término es una conjunción que vale $1$ en **una sola** valuación: pone la variable tal cual si $\sigma$ le asigna $1$, y su negación si le asigna $0$. Una disyunción de esos términos vale $1$ justo en las valuaciones elegidas. Aquí las filas con $1$ son las de $q = r$, así que la fórmula equivale a $q \leftrightarrow r$ (escrita de forma muy larga).

## Caso general

Para $n$ variables, si $\sigma_j(\varphi) = 1$ se define
$$\varphi_j = \Big(\bigwedge_{\sigma_j(p_i)=1} p_i\Big) \wedge \Big(\bigwedge_{\sigma_j(p_i)=0} \neg p_i\Big),$$
y $\varphi \equiv \bigvee_{j:\,\sigma_j(\varphi)=1} \varphi_j$. Para ver que son equivalentes: $\varphi_j$ vale $1$ en $\sigma$ si y solo si $\sigma = \sigma_j$, de modo que la disyunción vale $1$ en $\sigma$ si y solo si $\sigma$ es una de las valuaciones que hacen verdadera a $\varphi$.

> [!tip] Teorema
> Para toda tabla de verdad existe una fórmula equivalente que usa solo $\neg$, $\wedge$ y $\vee$.

Si la tabla no tiene ningún $1$, se toma una contradicción como $p \wedge \neg p$.

## Formas normales

Un **literal** es una variable o su negación. Una fórmula está en **forma normal disyuntiva** (DNF) si es una disyunción de conjunciones de literales, como la de arriba. Está en **forma normal conjuntiva** (CNF) si es una conjunción de disyunciones de literales (**cláusulas**).

La CNF se obtiene dualmente: por cada fila en que $\varphi$ vale $0$ se escribe la cláusula que **prohíbe** esa valuación (variable negada si $\sigma$ le da $1$, sin negar si le da $0$), y se toma la conjunción. Para $\varphi \equiv q \leftrightarrow r$, las filas con $0$ son $(0,0,1)$, $(0,1,0)$, $(1,0,1)$, $(1,1,0)$ y resulta
$$(p \vee q \vee \neg r) \wedge (p \vee \neg q \vee r) \wedge (\neg p \vee q \vee \neg r) \wedge (\neg p \vee \neg q \vee r).$$
Otra vía es pasar a DNF la **negación** de $\varphi$ y negar con De Morgan, con lo que toda fórmula tiene una CNF y una DNF equivalentes.

> [!warning] Equivalente no es la más corta
> La DNF canónica tiene un término por cada fila con $1$ y suele ser enorme. $q \leftrightarrow r$ cabe en $(\neg q \vee r) \wedge (q \vee \neg r)$. Las formas normales aseguran **existencia**, no economía.

## Preguntas de repaso

> [!question]- ¿Por qué cada término de la DNF vale $1$ en una sola valuación?
> Porque contiene, para cada variable, el literal que la fija a su valor en $\sigma_j$. Con cualquier otro valor, algún literal queda en $0$ y la conjunción entera falla.

> [!question]- ¿Cuál es la DNF canónica de $p \to q$?
> Vale $1$ en $(0,0)$, $(0,1)$ y $(1,1)$: $(\neg p \wedge \neg q) \vee (\neg p \wedge q) \vee (p \wedge q)$. Equivale a $\neg p \vee q$.

> [!question]- ¿Cuántos términos puede tener la DNF canónica de una fórmula con $n$ variables?
> Hasta $2^n$, uno por cada valuación (si la fórmula es tautología).
