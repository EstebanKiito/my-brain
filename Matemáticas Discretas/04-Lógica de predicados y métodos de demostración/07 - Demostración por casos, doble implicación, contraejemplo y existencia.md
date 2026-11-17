---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - discretas/demostraciones
  - origen/complemento
prerrequisitos:
  - "[[06 - Demostración directa, por contrapositivo y por contradicción]]"
---

# Demostración por casos, doble implicación, contraejemplo y existencia

Los métodos de la nota anterior prueban implicaciones $\forall x\,(P(x) \to Q(x))$. Otros enunciados tienen otra forma lógica ($\leftrightarrow$, $\neg\forall$, $\exists$) y piden una estrategia que calce con ella.

## Análisis de casos

Se divide el dominio en un número finito de casos $C_1, \dots, C_k$ cuya unión es todo el dominio y se prueba la afirmación en cada uno. Es válido porque cada elemento cae en algún caso. Los casos deben ser **exhaustivos**; no necesitan ser disjuntos.

*Para todo $n \in \mathbb{Z}$, $n^2 \ge n$.*
- $n = 0$: $0 \ge 0$.
- $n > 0$: como $n$ es entero, $n \ge 1$; multiplicando por $n > 0$ se tiene $n^2 \ge n$.
- $n < 0$: $n^2 > 0 > n$, luego $n^2 \ge n$.

Como $0$, positivos y negativos agotan $\mathbb{Z}$, vale para todo entero.

## Doble implicación

Para $\forall x\,(P(x) \leftrightarrow Q(x))$ se prueban **ambas direcciones**: $\forall x\,(P(x) \to Q(x))$ y $\forall x\,(Q(x) \to P(x))$, cada una con el método que convenga.

*$n$ es impar si y sólo si $n^2$ es impar.* ($\Rightarrow$) Si $n = 2k + 1$, entonces $n^2 = 2(2k^2 + 2k) + 1$ es impar (directa). ($\Leftarrow$) Por contrapositivo: si $n$ es par, $n = 2k$, entonces $n^2 = 2(2k^2)$ es par.

> [!warning] No sirve probar sólo una dirección
> Probar $P \to Q$ no dice nada sobre $Q \to P$. Por ejemplo, «si $n$ es múltiplo de $4$, $n$ es par» es verdadero, pero su recíproco es falso.

## Contraejemplo

Para refutar $\forall x\,P(x)$ basta probar $\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)$: se exhibe **un** elemento que no cumple $P$. Un solo contraejemplo derriba una generalización; en cambio, muchos ejemplos a favor no demuestran nada.

*No todo entero es suma de dos cuadrados perfectos.* Los únicos cuadrados que no superan $3$ son $0$ y $1$, y sus sumas posibles son $0, 1, 2$: nunca $3$. Otros enteros como $2 = 1 + 1$ o $5 = 4 + 1$ sí lo son, pero con $n = 3$ la generalización ya queda refutada.

## Demostración existencial

Para $\exists x\,P(x)$ hay que probar que **existe** un $n$ con $P(n)$. Una prueba **constructiva** lo exhibe; una **no constructiva** garantiza que existe sin decir cuál (no es estrictamente necesario nombrarlo).

*Existen irracionales $a, b$ con $a^b$ racional.* Se sabe que $\sqrt 2$ es irracional; se considera $\sqrt 2^{\sqrt 2}$ y se razona por casos:
1. Si $\sqrt 2^{\sqrt 2}$ es racional, sirven $a = b = \sqrt 2$.
2. Si es irracional, sirven $a = \sqrt 2^{\sqrt 2}$ y $b = \sqrt 2$, porque $a^b = \sqrt 2^{\sqrt 2 \cdot \sqrt 2} = \sqrt 2^{\,2} = 2$.

En ambos casos hay un par que sirve, aunque no se sepa en cuál de los dos casos se está. (Es una prueba no constructiva que combina casos y existencia.)

## Qué método para qué forma lógica

| Afirmación | Método natural |
|---|---|
| $\forall x\,(P \to Q)$ | directa, contrapositivo o contradicción |
| $\forall x\,(P \leftrightarrow Q)$ | doble implicación |
| el dominio se parte naturalmente | análisis de casos |
| $\neg\forall x\,P(x)$ | contraejemplo |
| $\exists x\,P(x)$ | exhibir un testigo, o existencia no constructiva |

## Preguntas de repaso

> [!question]- ¿Por qué un contraejemplo basta para refutar «para todo» pero un ejemplo no basta para probarlo?
> Porque $\neg\forall x\,P \equiv \exists x\,\neg P$: un elemento que falla ya hace falso el universal. En cambio, que $P$ valga en algunos elementos no excluye que falle en otro.

> [!question]- ¿Qué se necesita para que una demostración por casos sea válida?
> Que los casos cubran todo el dominio (sean exhaustivos) y que la afirmación se pruebe en cada uno. Si se olvida un caso, la prueba queda incompleta.

> [!question]- ¿La prueba de $\sqrt 2^{\sqrt 2}$ exhibe el par $(a, b)$?
> No: demuestra que alguno de dos pares sirve, sin decidir cuál. Es una demostración existencial no constructiva.
