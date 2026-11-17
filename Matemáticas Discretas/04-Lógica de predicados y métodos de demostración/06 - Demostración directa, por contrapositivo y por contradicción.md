---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - discretas/demostraciones
  - origen/complemento
prerrequisitos:
  - "[[05 - Consecuencia lógica en predicados y reglas de inferencia]]"
---

# Demostración directa, por contrapositivo y por contradicción

Una **demostración** es un argumento válido que establece la verdad de una afirmación matemática: una secuencia de pasos, cada uno justificado por axiomas, hipótesis o resultados ya demostrados, y conectado con el anterior por una regla de inferencia. Es lo mismo que una derivación en un sistema deductivo, pero escrita en lenguaje matemático. Esta nota presenta tres métodos para afirmaciones de la forma $\forall x\,(P(x) \to Q(x))$.

## Vocabulario de afirmaciones

Una **afirmación matemática** es una sentencia sobre objetos matemáticos que es verdadera o falsa; todo predicado o fórmula lo es. Según su estatus:

| Tipo | Qué es |
|---|---|
| **Axioma** | afirmación que se acepta sin demostración (por ejemplo, los axiomas de Peano: $0 \in \mathbb{N}$, $\forall x\,(x \in \mathbb{N} \to S(x) \in \mathbb{N})$, $\neg\exists x\,S(x) = 0$) |
| **Teorema** | afirmación verdadera y demostrable (Pitágoras, los cuatro colores) |
| **Lema** | resultado menor que sirve para demostrar un teorema |
| **Proposición** | resultado interesante, de menor importancia que un teorema |
| **Corolario** | consecuencia casi directa de un teorema |
| **Conjetura** | se cree verdadera, pero no se ha demostrado (Goldbach: todo par mayor que $2$ es suma de dos primos) |
| **Problema abierto** | no se sabe si es verdadera o falsa |

> [!warning] Qué no es una demostración
> No lo es una colección de símbolos sueltos ni argumentos desconectados. Debe ser clara, precisa y completa, de modo que el lector quede convencido sin dudas. Encontrarla exige experiencia, intuición y perseverancia; los métodos son guías para elegir por dónde partir.

## Demostración directa

Para $\forall x\,(P(x) \to Q(x))$: se toma un $n$ arbitrario, se **supone $P(n)$** y se deduce **$Q(n)$**. Es la aplicación de modus ponens.

*Si $n$ es impar, $n^2$ es impar.* Sea $n = 2k + 1$. Entonces $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, que es impar.

*Si $n, m$ son cuadrados perfectos, $n \cdot m$ también.* Con $n = a^2$ y $m = b^2$, $n \cdot m = (ab)^2$ y $ab \in \mathbb{Z}$.

## Contrapositivo

La implicación $P \to Q$ es equivalente a $\neg Q \to \neg P$. Así que se puede **suponer $\neg Q(n)$** y deducir **$\neg P(n)$**. Conviene cuando negar la conclusión da más información que suponer la hipótesis.

*Si $3n + 2$ es impar, entonces $n$ es impar.* Contrapositivo: si $n$ es par ($n = 2k$), entonces $3n + 2 = 6k + 2 = 2(3k + 1)$ es par. Directamente costaría: de «$3n + 2$ es impar» no se ve cómo despejar $n$.

*Si $n = a \cdot b$ con $a, b \in \mathbb{Z}^+$, entonces $a \le \sqrt n$ o $b \le \sqrt n$.* Contrapositivo: si $a > \sqrt n$ y $b > \sqrt n$, entonces $a \cdot b > n$, y por tanto $a \cdot b \ne n$.

## Contradicción

Para $\forall x\,(P(x) \to Q(x))$ se **supone que existe $n$ con $P(n)$ verdadero y $Q(n)$ falso** (la negación de la afirmación) y se infiere una contradicción. Es más flexible que el contrapositivo, porque se dispone de $P$ y $\neg Q$ a la vez.

**$\sqrt 2$ es irracional.** Si fuera racional, $\sqrt 2 = a/b$ con $a, b$ enteros sin factores comunes y $b \ne 0$ (en particular no ambos pares). Elevando al cuadrado, $a^2 = 2b^2$, así que $a^2$ es par, y por tanto $a$ es par (si fuera impar, $a^2$ lo sería, como se mostró arriba): $a = 2k$. Entonces $4k^2 = 2b^2$, o sea $b^2 = 2k^2$, luego $b^2$ es par y $b$ también. Ambos pares contradice que no tienen factores comunes.

**Hay infinitos primos.** Si fueran finitos, $p_1, \dots, p_k$, el número $N = p_1 \cdots p_k + 1$ tendría un factor primo $q$ (todo número mayor que $1$ lo tiene). Ese $q$ es alguno de los $p_i$, así que divide a $p_1 \cdots p_k$ y a $N$, por lo que divide a su diferencia, $1$: imposible.

> [!tip] Tres métodos, una misma implicación
> **Directa:** suponer $P$, llegar a $Q$. **Contrapositivo:** suponer $\neg Q$, llegar a $\neg P$. **Contradicción:** suponer $P \wedge \neg Q$, llegar a algo absurdo. Si no se sabe cuál usar, se prueba primero la directa.

## Preguntas de repaso

> [!question]- ¿Por qué probar el contrapositivo demuestra la implicación original?
> Porque $P \to Q$ y $\neg Q \to \neg P$ son lógicamente equivalentes: son falsas exactamente cuando $P$ es verdadera y $Q$ falsa.

> [!question]- ¿Qué diferencia hay entre el contrapositivo y la contradicción?
> El contrapositivo parte sólo de $\neg Q$ y llega a $\neg P$, que es la meta. La contradicción parte de $P \wedge \neg Q$ y puede llegar a cualquier absurdo (no necesariamente $\neg P$ ni $Q$).

> [!question]- ¿Por qué en la prueba de que $\sqrt 2$ es irracional se exige que $a$ y $b$ no tengan factores comunes?
> Porque toda fracción se puede reducir a esa forma, y es lo que permite concluir que $a$ y $b$ no pueden ser ambos pares; la contradicción nace de que el desarrollo los obliga a serlo.
