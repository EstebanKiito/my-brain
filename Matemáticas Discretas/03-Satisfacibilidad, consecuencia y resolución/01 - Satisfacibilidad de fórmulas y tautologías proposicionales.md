---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos: []
---

# Satisfacibilidad de fórmulas y tautologías proposicionales

Una fórmula proposicional puede ser verdadera en algunos "mundos" y falsa en otros. Clasificarlas según en cuántos mundos son verdaderas permite formular preguntas como "¿tiene solución este problema?", que es la base de casi todo lo que sigue en el tema.

## Satisfacibilidad

Una **valuación** $\sigma$ asigna $0$ o $1$ a cada variable proposicional y, por extensión, un valor a cada fórmula. Cada valuación representa un "mundo" posible.

> [!tip] Satisfacible
> Una fórmula $\varphi$ es **satisfacible** si existe una valuación $\sigma$ con $\sigma(\varphi) = 1$. Es decir, si hay al menos un mundo donde es verdadera.

Ejemplos de fórmulas satisfacibles: $(p \lor q) \to r$ (basta $p = q = 0$) y $p \to \neg p$ (basta $p = 0$). Ejemplos de insatisfacibles: $p \land \neg p$ y $(p \lor q) \leftrightarrow \neg(p \lor q)$, porque una fórmula nunca coincide con su propia negación.

## Contradicciones y tautologías

Los dos extremos tienen nombre propio:

| Tipo | Condición | Ejemplo |
|---|---|---|
| **Contradicción** | $\sigma(\varphi) = 0$ para toda $\sigma$ (no es satisfacible) | $p \land \neg p$ |
| **Tautología** | $\sigma(\varphi) = 1$ para toda $\sigma$ | $p \lor \neg p$, $p \leftrightarrow p$ |
| **Contingencia** | verdadera en algunas valuaciones y falsa en otras | $p \to q$ |

Una fórmula satisfacible es una tautología o una contingencia. Además, $\varphi$ es tautología si y solo si $\neg\varphi$ es contradicción: negar intercambia los $1$ y los $0$ de la columna de resultados.

## Equivalencia como tautología

La equivalencia lógica se puede reformular con estos conceptos.

> [!tip] Equivalencia y tautología
> $\varphi \equiv \psi$ si y solo si $\varphi \leftrightarrow \psi$ es una tautología.

Demostración: $\varphi \leftrightarrow \psi$ vale $1$ en $\sigma$ exactamente cuando $\sigma(\varphi) = \sigma(\psi)$. Así, que valga $1$ para toda $\sigma$ es lo mismo que decir que $\varphi$ y $\psi$ coinciden en toda valuación.

## El problema SAT

El **problema de satisfacibilidad** (*SAT*) pide decidir si una fórmula dada es satisfacible. Con $n$ variables hay $2^n$ valuaciones, de modo que la tabla de verdad completa crece exponencialmente. SAT es central en computación porque muchos problemas de otras áreas (horarios, coloreo, verificación de circuitos) se pueden traducir a una fórmula que es satisfacible exactamente cuando el problema tiene solución (ver [[02 - Modelar problemas con lógica proposicional y el 3-coloreo de mapas]]).

> [!warning] Satisfacible no es tautología
> Basta **un** mundo para ser satisfacible; ser tautología exige **todos**. Por eso $p$ es satisfacible pero no es tautología, y $p \land \neg p$ es la única forma en que "ningún mundo" aparece.

## Preguntas de repaso

> [!question]- ¿Por qué $p \to \neg p$ es satisfacible aunque "parezca" absurda?
> Porque con $p = 0$ el antecedente es falso y la implicación vale $1$. Satisfacible solo pide un mundo que la haga verdadera; en este caso resulta equivalente a $\neg p$.

> [!question]- Si $\varphi$ es tautología, ¿qué se puede decir de $\neg\varphi$ y de $\varphi \land \psi$?
> $\neg\varphi$ es una contradicción. Y $\varphi \land \psi$ es equivalente a $\psi$, porque $\varphi$ vale $1$ en toda valuación y no aporta restricción.

> [!question]- ¿Por qué comprobar $\varphi \equiv \psi$ equivale a comprobar una tautología?
> Porque $\varphi \leftrightarrow \psi$ solo vale $1$ cuando ambos valores coinciden; que valga $1$ siempre significa que coinciden siempre.

> [!question]- ¿Por qué SAT no se resuelve cómodamente con tablas de verdad?
> Una fórmula con $n$ variables tiene $2^n$ filas; con $30$ variables ya son más de mil millones.
