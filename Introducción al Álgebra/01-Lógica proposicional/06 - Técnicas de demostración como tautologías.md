---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos:
  - "[[03 - Implicación y equivalencia]]"
---

# Técnicas de demostración como tautologías

La mayoría de los teoremas se escriben como una implicación $p \Rightarrow q$, donde $p$ es la hipótesis y $q$ la tesis. Detrás de cada técnica de demostración hay una tautología que la justifica: probar el teorema es, en el fondo, apoyarse en esa tautología para concluir $q$ a partir de $p$.

## Las tres tautologías de la demostración

| Técnica | Tautología que la respalda |
|---|---|
| Transitividad | $\big[(p \Rightarrow q) \wedge (q \Rightarrow r)\big] \Rightarrow (p \Rightarrow r)$ |
| Contrarrecíproca | $(p \Rightarrow q) \Leftrightarrow (\neg q \Rightarrow \neg p)$ |
| Reducción al absurdo | $\big[(p \Rightarrow q) \Leftrightarrow V\big] \Leftrightarrow \big[p \wedge \neg q \Rightarrow F\big]$ |

La **contrarrecíproca** dice que probar $p \Rightarrow q$ es lo mismo que probar $\neg q \Rightarrow \neg p$: en vez de partir de $p$, se supone la negación de la conclusión y se llega a la negación de la hipótesis.

La **reducción al absurdo** (o por contradicción) dice que, para probar $p \Rightarrow q$, basta suponer la hipótesis $p$ *y* la negación de la tesis $\neg q$, y concluir una contradicción $F$. Si suponer $\neg q$ lleva a lo imposible, la única salida es que $q$ sea verdadera.

> [!tip] Contrarrecíproca
> $(p \Rightarrow q) \Leftrightarrow (\neg q \Rightarrow \neg p)$. Es la técnica que se usa cuando la negación de la conclusión da un punto de partida más cómodo que la hipótesis original.

> [!warning] Contrarrecíproca ≠ recíproca
> La **recíproca** de $p \Rightarrow q$ es $q \Rightarrow p$ y *no* es equivalente a la implicación original. La **contrarrecíproca** es $\neg q \Rightarrow \neg p$ y sí lo es. Confundir ambas invalida la demostración.

## Reducción al absurdo aplicada

**Ejemplo.** Pruebe que si $n$ es un entero y $n^2$ es par, entonces $n$ es par.

Por contradicción, supongamos que $n$ es impar. Entonces existe $k \in \mathbb{Z}$ con $n = 2k+1$, de donde

$$
n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 = 2\ell + 1,
$$

con $\ell = 2k^2 + 2k \in \mathbb{Z}$, así que $n^2$ es impar. Esto contradice la hipótesis de que $n^2$ es par, luego $n$ es par.

**Ejemplo.** Pruebe que $\sqrt{2}$ no es racional.

Por contradicción, supongamos que $\sqrt{2} = m/n$ con $m, n \in \mathbb{Z}$, $n \neq 0$, y con $m$ y $n$ sin divisores comunes salvo el $1$. Elevando al cuadrado, $2 = m^2/n^2$, o sea $2n^2 = m^2$, de modo que $m^2$ es par, y por el ejemplo anterior $m$ es par: $m = 2k$. Sustituyendo, $2n^2 = (2k)^2 = 4k^2$, de donde $n^2 = 2k^2$, así que $n^2$ es par y por tanto $n$ es par. Se concluye que $m$ y $n$ son ambos pares, contradiciendo que no tienen divisores comunes. Por lo tanto $\sqrt{2}$ es irracional.

**Ejemplo.** Pruebe que si $3a$ no es racional, entonces $a$ no es racional.

Por contradicción, supongamos que $a$ es racional: $a = n/m$ con $n, m \in \mathbb{Z}$, $m \neq 0$. Entonces $3a = 3n/m$ es un número racional, lo que contradice la hipótesis de que $3a$ no es racional. Luego $a$ no es racional.

## Preguntas de repaso

> [!question]- ¿Qué supone usted al demostrar $p \Rightarrow q$ por reducción al absurdo?
> Se supone la hipótesis $p$ junto con la negación de la tesis, $\neg q$, y se busca llegar a una contradicción. Al obtenerla, se concluye que $\neg q$ era insostenible, así que $q$ es verdadera.

> [!question]- ¿Cuál es la contrarrecíproca de "si llueve, la calle se moja"? ¿Y su recíproca?
> Contrarrecíproca: "si la calle no se moja, no llueve" ($\neg q \Rightarrow \neg p$). Recíproca: "si la calle se moja, llueve" ($q \Rightarrow p$).

> [!question]- Escriba la tautología que justifica la transitividad y explique para qué sirve.
> $\big[(p \Rightarrow q) \wedge (q \Rightarrow r)\big] \Rightarrow (p \Rightarrow r)$. Permite encadenar implicaciones: si $p$ implica $q$ y $q$ implica $r$, entonces $p$ implica $r$.

> [!question]- ¿Por qué en el ejemplo de $\sqrt{2}$ se puede suponer que $m$ y $n$ no tienen divisores comunes?
> Porque si los tuvieran, se cancelarían del cociente $m/n$ sin cambiar su valor. Suponer la fracción "reducida" es lo que permite, al final, llegar a la contradicción de que ambos son pares.
