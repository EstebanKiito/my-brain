---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos:
  - "[[02 - Negación, conjunción y disyunción]]"
---

# Implicación y equivalencia

La mayoría de las afirmaciones matemáticas tienen la forma "si se cumple $p$, entonces se cumple $q$". Para expresarlas se usa la **implicación**, y para decir que dos condiciones son intercambiables se usa la **equivalencia**. Son los dos conectivos que sostienen los teoremas y sus demostraciones.

## Implicación ($p \Rightarrow q$)

La **implicación** $p \Rightarrow q$, que se lee "si $p$ entonces $q$" o "$p$ implica $q$", es falsa solo cuando $p$ es verdadera y $q$ es falsa.

| $p$ | $q$ | $p \Rightarrow q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

En $p \Rightarrow q$, la proposición $p$ es la **hipótesis** (o antecedente) y $q$ la **tesis** (o conclusión). La implicación captura la idea de "una proposición verdadera no puede implicar una falsa": el único caso prohibido es $V \Rightarrow F$.

> [!warning] La implicación no exige relación causal
> Las filas donde la hipótesis es falsa son verdaderas sin importar la conclusión: $F \Rightarrow q$ es siempre V. Por eso "si $2+2=5$, entonces la Luna es de queso" es una implicación verdadera (tiene hipótesis falsa). La lógica solo mira los valores de verdad, no si $p$ "causa" $q$.

Esta propiedad —que de una hipótesis falsa se sigue cualquier cosa— es lo que vuelve delicado razonar a partir de suposiciones falsas, y es exactamente lo que explota la demostración por reducción al absurdo.

## Equivalencia ($p \Leftrightarrow q$)

La **equivalencia** (o doble implicación) $p \Leftrightarrow q$ se lee "$p$ si y solo si $q$" y es verdadera solo cuando $p$ y $q$ tienen el mismo valor de verdad.

| $p$ | $q$ | $p \Leftrightarrow q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

La equivalencia es el concepto central en la clasificación y el despeje: decir $p \Leftrightarrow q$ es decir que $p$ y $q$ valen exactamente en los mismos casos, así que se pueden reemplazar una por otra.

> [!tip] Equivalencia como doble implicación
> $p \Leftrightarrow q$ equivale a $(p \Rightarrow q) \wedge (q \Rightarrow p)$: valen a la vez la implicación y su recíproca. Por eso "si y solo si" se demuestra probando las dos direcciones por separado.

## Evaluar una proposición compuesta

Con estos conectivos se arman fórmulas más complejas, evaluadas con su tabla de verdad. Por ejemplo, para $((p \Rightarrow q) \vee s) \Leftrightarrow (p \wedge q)$ se construye una tabla de $2^3 = 8$ filas y se van calculando las subexpresiones de adentro hacia afuera, primero $p \Rightarrow q$, luego su disyunción con $s$, luego $p \wedge q$, y finalmente la equivalencia.

## Razonar hacia atrás desde un valor conocido

Muchas preguntas de prueba no piden la tabla completa, sino deducir valores a partir de un dato como "la implicación $A \Rightarrow B$ es falsa". Como la implicación tiene **una sola fila falsa**, ese dato fija dos cosas a la vez: $A = V$ y $B = F$. Del mismo modo, una conjunción verdadera obliga a que **todas** sus partes sean V, y una disyunción falsa obliga a que **todas** sus partes sean F.

> [!tip] Lo que fija cada dato
> | Dato | Consecuencia |
> |---|---|
> | $A \Rightarrow B$ es F | $A = V$ y $B = F$ |
> | $A \wedge B$ es V | $A = V$ y $B = V$ |
> | $A \vee B$ es F | $A = F$ y $B = F$ |
> | $A \Leftrightarrow B$ es V y se conoce $A$ | $B$ tiene el mismo valor que $A$ |

**Ejemplo.** Si $[(p \wedge q) \Rightarrow r] \Rightarrow (r \vee s)$ es falsa, entonces $r \vee s$ es F, así que $r = F$ y $s = F$; y $(p \wedge q) \Rightarrow r$ es V con $r = F$, así que $p \wedge q$ es F. Se sabe que $p$ y $q$ no son ambas verdaderas, pero no se puede decir más: la información fija algunas variables y deja otras libres.

Al revés, si el antecedente de una implicación resulta F, la implicación es V **sin importar** el consecuente, y no hace falta evaluarlo.

## Preguntas de repaso

> [!question]- ¿Cuál es la única fila en que $p \Rightarrow q$ es falsa? ¿Por qué es la que hay que vigilar?
> La fila $p=V$, $q=F$. Es la única combinación que "rompe" la promesa de la implicación; todas las demás (incluidas las de hipótesis falsa) son V.

> [!question]- ¿Cuál es la negación de $p \Rightarrow q$?
> $\neg(p \Rightarrow q)$ es verdadera exactamente cuando $p \Rightarrow q$ es falsa, es decir, cuando $p = V$ y $q = F$. En símbolos, $\neg(p \Rightarrow q) \equiv p \wedge \neg q$.

> [!question]- Dadas $p$: "llueve" y $q$: "la calle se moja", escriba $p \Rightarrow q$ y su recíproca en palabras. ¿Son equivalentes?
> $p \Rightarrow q$: "si llueve, la calle se moja". Recíproca $q \Rightarrow p$: "si la calle se moja, llueve". No son equivalentes: la calle puede mojarse por otra razón (un camión de riego).

> [!question]- ¿Cuándo es verdadera $p \Leftrightarrow q$?
> Cuando $p$ y $q$ tienen el mismo valor de verdad (ambas V o ambas F). Es el conectivo que afirma la coincidencia de valores, no la mera implicación.
