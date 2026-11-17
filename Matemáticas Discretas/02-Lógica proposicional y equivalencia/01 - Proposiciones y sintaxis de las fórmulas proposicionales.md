---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[05 - Definiciones inductivas y listas enlazadas]]"
---

# Proposiciones y sintaxis de las fórmulas proposicionales

Una **lógica** es un lenguaje formal para modelar cierto tipo de problema y decidir qué conclusiones son válidas. La más simple es la **lógica proposicional**, que parte de afirmaciones que solo pueden ser verdaderas o falsas y estudia cómo se combinan. Antes de hablar de verdad hay que decir qué es una fórmula bien escrita: eso es la **sintaxis**.

## Proposiciones

Una **proposición** es una afirmación que admite exactamente uno de dos valores de verdad: verdadera ($1$) o falsa ($0$).

| Afirmación | ¿Proposición? | Valor |
|---|---|---|
| Sócrates es mortal | sí | $1$ |
| La luna es una estrella | sí | $0$ |
| $4 + 9 = 11$ | sí | $0$ |
| Hemos sido visitados por extraterrestres | sí (aunque se ignore cuál) | $0$ o $1$ |
| $34 + 59$ | no, es una expresión, no afirma nada | |
| ¿Es el cielo azul? | no, es una pregunta | |

Lo que importa es que **exista** un valor de verdad, no que se conozca.

## Fórmulas: una definición inductiva

Sea $P$ un conjunto de **variables proposicionales** (los nombres $p, q, r, \dots$ de proposiciones atómicas). El conjunto de **fórmulas** $L(P)$ es el menor conjunto tal que:

1. si $p \in P$, entonces $p \in L(P)$;
2. si $\varphi \in L(P)$, entonces $(\neg\varphi) \in L(P)$;
3. si $\varphi, \psi \in L(P)$ y $\star \in \{\wedge, \vee, \to, \leftrightarrow\}$, entonces $(\varphi \star \psi) \in L(P)$.

Es una definición inductiva como las de [[05 - Definiciones inductivas y listas enlazadas]]: un caso base (las variables) y dos reglas constructoras (negación y conectivos binarios). "Menor conjunto" significa que no hay más fórmulas que las que se obtienen aplicando las reglas un número finito de veces.

> [!tip] Por qué importa la sintaxis inductiva
> Como toda fórmula se construye por pasos, se pueden **definir funciones** sobre fórmulas por recursión y **demostrar propiedades** por [[06 - Inducción estructural]]: se prueba la propiedad para las variables y se muestra que las reglas la conservan.

## Paréntesis y abreviaciones

La definición formal exige un paréntesis en cada paso, lo que hace único el modo de construir cada fórmula. Para leer con comodidad se acuerda:

- omitir los paréntesis externos y los que no producen ambigüedad (los de la asociatividad);
- dar a $\neg$ precedencia sobre los conectivos binarios: $((\neg p) \vee q) \wedge (\neg r)$ se escribe $(\neg p \vee q) \wedge \neg r$;
- usar operadores generalizados: $\bigvee_{i=1}^n \varphi_i = \varphi_1 \vee \dots \vee \varphi_n$ y $\bigwedge_{i=1}^n \varphi_i$ análogo.

> [!warning] Los operadores generalizados solo valen para $n$ finito
> Una fórmula es una cadena finita de símbolos, de modo que $\bigvee_{i=1}^{\infty}\varphi_i$ no es una fórmula de $L(P)$.

## Ejemplo: ¿es fórmula?

Con $P = \{p, q\}$: $((\neg(\neg p)) \leftrightarrow ((\neg p) \wedge q))$ es una fórmula (se arma con la regla 2 dos veces, la regla 2 una vez más, la regla 3 con $\wedge$ y luego con $\leftrightarrow$). En cambio $p \wedge$ no lo es, porque a la regla 3 le falta un operando.

## Preguntas de repaso

> [!question]- ¿Por qué $\neg p \wedge q$ se lee como $(\neg p) \wedge q$ y no como $\neg(p \wedge q)$?
> Por la convención de precedencia: la negación se aplica primero, a la variable más cercana. Si se quisiera negar la conjunción habría que escribir los paréntesis, y las dos fórmulas son semánticamente distintas.

> [!question]- ¿Qué se gana con que $L(P)$ sea "el menor conjunto" cerrado bajo las reglas?
> Garantiza que toda fórmula es una variable o se obtiene de fórmulas más chicas por una regla. Eso es lo que justifica definir funciones por recursión y demostrar por inducción estructural.

> [!question]- ¿"Hoy lloverá" es una proposición aunque nadie sepa si es cierto?
> Sí. Basta que la afirmación sea verdadera o falsa en el mundo; el valor puede ignorarse. Una pregunta o una expresión sin afirmación no cumple ese requisito.
