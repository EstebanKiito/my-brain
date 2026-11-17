---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[06 - Forma normal disyuntiva desde una tabla de verdad]]"
  - "[[06 - Inducción estructural]]"
---

# Conectivos funcionalmente completos

Los cinco conectivos $\neg, \wedge, \vee, \to, \leftrightarrow$ no son todos necesarios: algunos se definen con otros. La pregunta natural es cuál es el conjunto mínimo con el que aún se puede expresar **todo**. Importa en la práctica porque los circuitos y los lenguajes pueden construirse con un solo tipo de compuerta si ese tipo basta.

## Definición

> [!tip] Conjunto funcionalmente completo
> Un conjunto de conectivos es **funcionalmente completo** si toda fórmula de $L(P)$ es lógicamente equivalente a una que usa solo esos conectivos.

Del teorema de la [[06 - Forma normal disyuntiva desde una tabla de verdad|forma normal]]: toda tabla de verdad tiene una fórmula con $\neg, \wedge, \vee$. Por lo tanto $\{\neg, \wedge, \vee\}$ es funcionalmente completo, y es el punto de partida para probar la completitud de otros.

## Cómo se demuestra que un conjunto es completo

Se parte de un conjunto $C$ ya conocido como completo y se prueba, por inducción estructural, que toda fórmula con conectivos de $C$ equivale a una con los del conjunto nuevo $C'$. Hay que **expresar los conectivos de $C$ usando los de $C'$**; la dirección es crucial y es el error típico invertirla.

**Ejemplo: $\{\neg, \to\}$.** Se prueba que toda fórmula hecha con $\neg, \wedge, \vee$ equivale a otra con $\neg, \to$.

- **Base.** Una variable $p$ ya usa solo conectivos de $C'$.
- **HI.** $\varphi \equiv \varphi'$ y $\psi \equiv \psi'$, con $\varphi', \psi'$ escritas con $\neg, \to$.
- **Paso.** $\neg\varphi \equiv \neg\varphi'$ ya está en $C'$. Para $\wedge$: $\varphi \wedge \psi \equiv \neg(\neg\varphi' \vee \neg\psi') \equiv \neg(\varphi' \to \neg\psi')$. Para $\vee$: $\varphi \vee \psi \equiv \neg\varphi' \to \psi'$.

Por inducción estructural, todo se expresa con $\neg$ y $\to$.

| Conjunto | Cómo se obtiene lo que falta |
|---|---|
| $\{\neg, \wedge\}$ | $\varphi \vee \psi \equiv \neg(\neg\varphi \wedge \neg\psi)$ |
| $\{\neg, \vee\}$ | $\varphi \wedge \psi \equiv \neg(\neg\varphi \vee \neg\psi)$ |
| $\{\neg, \to\}$ | $\varphi \wedge \psi \equiv \neg(\varphi \to \neg\psi)$ y $\varphi \vee \psi \equiv \neg\varphi \to \psi$ |
| $\{\uparrow\}$ (NAND) | $\neg\varphi \equiv \varphi \uparrow \varphi$ y $\varphi \wedge \psi \equiv (\varphi \uparrow \psi) \uparrow (\varphi \uparrow \psi)$ |

Con NAND, $\varphi \uparrow \psi \equiv \neg(\varphi \wedge \psi)$, se obtiene $\neg$ y $\wedge$, y de ahí todo lo demás: **un solo conectivo** alcanza.

## Cómo se demuestra que un conjunto NO es completo

Se encuentra una propiedad que conservan todos los conectivos del conjunto y que alguna función no cumple. Se prueba la propiedad por inducción estructural y se exhibe la fórmula que la viola.

**$\{\neg\}$ no es completo.** Con una sola variable $p$, toda fórmula con solo $\neg$ equivale a $p$ o a $\neg p$: la base es $p$ y el paso, $\neg p$ o $\neg\neg p \equiv p$. Ninguna de las dos es equivalente a $p \wedge \neg p$ (que vale siempre $0$), así que hay fórmulas inalcanzables.

**$\{\wedge, \vee, \to, \leftrightarrow\}$ no es completo.** Con la valuación que asigna $1$ a todas las variables, cada uno de esos conectivos da $1$ cuando sus entradas valen $1$, y por inducción toda fórmula sin $\neg$ vale $1$ ahí. No puede expresar $\neg p$, que en esa valuación vale $0$.

**$\{\neg, \veebar\}$ (con XOR) no es completo.** Con $n \ge 2$ variables, toda fórmula con $\neg$ y $\veebar$ tiene una cantidad **par** de valuaciones que la hacen verdadera ($2^{n-1}$ para una variable, $2^n - m$ al negar y $m_1 + m_2 - 2m_{12}$ al aplicar XOR, siempre par). Pero $p \vee q$ sobre $\{p, q\}$ tiene $3$ modelos, impar.

> [!warning] La dirección de la inducción
> Para demostrar completitud se traduce **desde** un conjunto completo **hacia** el nuevo. Traducir al revés (expresar los conectivos nuevos con los antiguos) no prueba nada, porque no muestra que se pueda llegar a todas las fórmulas.

## Preguntas de repaso

> [!question]- ¿Por qué basta probar la completitud de $\{\neg, \wedge\}$ para saber que $\{\neg, \to\}$ también lo es?
> Si $\{\neg, \to\}$ puede expresar $\wedge$ (con $\varphi \wedge \psi \equiv \neg(\varphi \to \neg\psi)$) y ya tiene $\neg$, entonces expresa todo lo que expresa $\{\neg, \wedge\}$, es decir, toda fórmula.

> [!question]- ¿Cómo se expresa $\varphi \vee \psi$ solo con NAND?
> $\varphi \vee \psi \equiv \neg(\neg\varphi \wedge \neg\psi) \equiv (\varphi \uparrow \varphi) \uparrow (\psi \uparrow \psi)$: se niega cada operando con $x \uparrow x$ y se combina con NAND.

> [!question]- ¿Qué tipo de argumento prueba que un conjunto no es funcionalmente completo?
> Una propiedad invariante: algo que todas las fórmulas del conjunto cumplen (por inducción estructural) y que alguna función booleana no cumple, como "es equivalente a $p$ o a $\neg p$" o "tiene un número par de modelos".
