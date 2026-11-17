---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[03 - Interpretaciones y satisfacción de fórmulas]]"
---

# Equivalencias y negación con cuantificadores

Saber cuándo dos fórmulas con cuantificadores dicen lo mismo sirve para negar enunciados («no todos…» equivale a «alguno no…»), para simplificar demostraciones y para detectar errores de razonamiento. La definición es la misma que en lógica proposicional, pero cuantificada sobre interpretaciones.

## Definición

> [!tip] Equivalencia lógica
> Dos fórmulas $\varphi, \psi$ son **lógicamente equivalentes**, $\varphi \equiv \psi$, si para toda interpretación $I$ y todos los valores $a_1, \dots, a_n$ se tiene $I \models \varphi(\bar a) \iff I \models \psi(\bar a)$. Para oraciones: para toda $I$, $I \models \varphi \iff I \models \psi$.

Toda equivalencia proposicional (conmutatividad, asociatividad, De Morgan, doble negación, distributividad, $\varphi \to \psi \equiv \neg\varphi \vee \psi$...) sigue valiendo para fórmulas de predicados. Por ejemplo $\forall x\,(P(x) \to R(x)) \equiv \forall x\,(\neg P(x) \vee R(x))$. Además hay cuatro equivalencias propias de los cuantificadores.

## Las cuatro equivalencias básicas

Para fórmulas $\varphi(x), \psi(x)$ con $x$ libre:

$$\neg\forall x\,\varphi(x) \equiv \exists x\,\neg\varphi(x) \qquad \neg\exists x\,\varphi(x) \equiv \forall x\,\neg\varphi(x)$$
$$\forall x\,(\varphi(x) \wedge \psi(x)) \equiv \forall x\,\varphi(x) \wedge \forall x\,\psi(x) \qquad \exists x\,(\varphi(x) \vee \psi(x)) \equiv \exists x\,\varphi(x) \vee \exists x\,\psi(x)$$

Las dos primeras son el **De Morgan de los cuantificadores**: negar «para todo» da «existe un contraejemplo», y negar «existe» da «para todo no». Las otras dos dicen que $\forall$ se reparte sobre $\wedge$ y $\exists$ se reparte sobre $\vee$.

**Demostración de $\exists x\,(\varphi \vee \psi) \equiv \exists x\,\varphi \vee \exists x\,\psi$.** Sea $I$ una interpretación.
- ($\Rightarrow$) Si $I \models \exists x\,(\varphi \vee \psi)$, hay un $a$ con $I \models \varphi(a)$ o $I \models \psi(a)$. En el primer caso $I \models \exists x\,\varphi$ y en el segundo $I \models \exists x\,\psi$; en ambos se cumple la disyunción.
- ($\Leftarrow$) Si $I \models \exists x\,\varphi$, hay un $a$ con $I \models \varphi(a)$, luego $I \models (\varphi \vee \psi)(a)$ y $I \models \exists x\,(\varphi \vee \psi)$. El caso $\exists x\,\psi$ es simétrico.

Las dos direcciones usan «sin pérdida de generalidad» por separado: no se puede condensar en una cadena de equivalencias sin cuidado.

## Lo que **no** se reparte

> [!warning] Tres falsas equivalencias frecuentes
> - $\forall x\,\exists y\,\varphi(x, y) \not\equiv \exists x\,\forall y\,\varphi(x, y)$.
> - $\forall x\,(\varphi \vee \psi) \not\equiv \forall x\,\varphi \vee \forall x\,\psi$.
> - $\exists x\,(\varphi \wedge \psi) \not\equiv \exists x\,\varphi \wedge \exists x\,\psi$.

Para refutar cada una basta una interpretación:

| Falsa equivalencia | Interpretación que la refuta |
|---|---|
| $\forall\exists$ contra $\exists\forall$ | $\mathbb{Z}$ con $x < y$: $\forall x\,\exists y\,x < y$ es verdadera; $\exists x\,\forall y\,x < y$ es falsa |
| $\forall x\,(\varphi \vee \psi)$ contra $\forall\varphi \vee \forall\psi$ | $\mathbb{N}$, $\varphi$ = «par», $\psi$ = «impar»: todo natural es par o impar, pero no todos son pares ni todos impares |
| $\exists x\,(\varphi \wedge \psi)$ contra $\exists\varphi \wedge \exists\psi$ | $\mathbb{N}$ con la misma $\varphi$ y $\psi$: hay un par y hay un impar, pero ninguno es ambos |

También falla $\forall x\,(P(x) \to Q(x)) \equiv (\forall x\,P(x)) \to (\forall x\,Q(x))$: con dominio $\{a, b\}$, $P$ sólo en $a$ y $Q$ sólo en $b$, el lado derecho es verdadero (su antecedente es falso) y el izquierdo es falso ($P(a)$ verdadero con $Q(a)$ falso). La implicación sí vale en una dirección ($\forall(P \to Q) \models (\forall P) \to (\forall Q)$).

## Negar fórmulas paso a paso

Para negar una fórmula, se empuja la negación hacia dentro cambiando $\forall \leftrightarrow \exists$ y aplicando De Morgan. Ejemplo:

$$\neg\forall x\,\exists y\,(x < y \wedge P(y)) \equiv \exists x\,\forall y\,(x \ge y \vee \neg P(y)).$$

Este mecanismo se usa al buscar contraejemplos y al hacer demostraciones por contradicción, donde hay que negar la tesis.

## Preguntas de repaso

> [!question]- ¿Por qué $\neg\forall x\,\varphi(x) \equiv \exists x\,\neg\varphi(x)$?
> $\forall x\,\varphi$ falla exactamente cuando algún $a$ del dominio no cumple $\varphi$, es decir cuando $\exists x\,\neg\varphi$ es verdadera. Se razona sobre una interpretación arbitraria y se usa que $I \not\models \forall x\,\varphi$ significa «hay un $a$ con $I \not\models \varphi(a)$».

> [!question]- ¿Por qué $\exists x\,(\varphi \wedge \psi)$ no equivale a $\exists x\,\varphi \wedge \exists x\,\psi$?
> En el lado izquierdo el **mismo** objeto debe cumplir ambas. En el derecho pueden ser objetos distintos. La izquierda implica la derecha, pero no al revés (por ejemplo, un natural par y otro impar, ninguno ambos).

> [!question]- ¿Cómo se prueba que dos fórmulas no son equivalentes?
> Se da una interpretación (dominio y significado de los predicados) que satisface una y no la otra. Un dominio finito de dos elementos suele bastar.
