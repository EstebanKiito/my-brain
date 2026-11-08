---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[01 - Método directo]]"
  - "[[06 - Técnicas de demostración como tautologías]]"
---

# Contrarrecíproca y contradicción en la práctica

El método directo no siempre sirve: a veces la hipótesis da poco con qué trabajar ("$x$ es irracional" no entrega ninguna fórmula para $x$) o la tesis es una disyunción difícil de atacar. En esos casos se usan las dos técnicas indirectas que la lógica proposicional justifica como tautologías: la **contrarrecíproca** y la **reducción al absurdo** (contradicción).

## Contrarrecíproca

> [!tip] Contrarrecíproca
> Para probar $p \Rightarrow q$ basta probar $\neg q \Rightarrow \neg p$: se supone que la tesis **falla** y se deduce que la hipótesis **falla**.

Conviene cuando $\neg q$ es más concreta que $p$. Un caso típico es una tesis con "o": la negación de "$a \le 0$ o $a \ge 3$" es "$0 < a < 3$", que es una sola condición fácil de usar.

**Ejemplo.** Si $a \in \mathbb{R}$ cumple $a^2 \ge 3a$, entonces $a \le 0$ o $a \ge 3$.

*Demostración (contrarrecíproca).* Supongamos $0 < a < 3$. Como $a > 0$, multiplicar $a < 3$ por $a$ conserva el sentido: $a^2 < 3a$. Es decir, falla la hipótesis. $\blacksquare$

> [!warning] Multiplicar una desigualdad exige conocer el signo
> El paso clave fue "$a > 0$, así que $a \cdot a < 3 \cdot a$". Si $a$ pudiera ser negativo, la desigualdad se daría vuelta. En las pautas, decir explícitamente que $a > 0$ vale puntaje.

## Reducción al absurdo

> [!tip] Reducción al absurdo
> Para probar $p \Rightarrow q$ se supone $p$ **y** $\neg q$, y se deduce una contradicción (algo de la forma $r \wedge \neg r$). Como de premisas verdaderas no puede salir algo falso, la suposición $\neg q$ era imposible.

Conviene cuando la tesis es una negación ("no es racional", "no es par", "no existe"), porque al negarla queda una afirmación positiva con la que sí se puede calcular.

**Ejemplo 1: racional más irracional.** Si $a \in \mathbb{Q}$ y $b \notin \mathbb{Q}$, entonces $a + b \notin \mathbb{Q}$.

*Demostración.* Supongamos que $a + b \in \mathbb{Q}$: $a + b = \frac{m}{n}$ y $a = \frac{p}{q}$ con enteros y $n, q \neq 0$. Entonces
$$b = \frac{m}{n} - \frac{p}{q} = \frac{mq - np}{nq},$$
cociente de enteros con denominador no nulo, así que $b \in \mathbb{Q}$. Eso contradice $b \notin \mathbb{Q}$. $\blacksquare$

**Ejemplo 2: paridad.** Si los naturales $m, n$ cumplen $n + 2n^2 = m + m^2$, entonces $n$ es par.

*Demostración.* Supongamos que $n$ es impar. Como $2n^2$ es par, $n + 2n^2$ es impar. Pero $m + m^2 = m(m+1)$ es producto de dos consecutivos, uno de los cuales es par, así que es par. Un impar no puede ser igual a un par: contradicción. $\blacksquare$

## ¿Cuál elegir?

| Si la tesis es… | Conviene |
|---|---|
| una igualdad o fórmula concreta | método directo |
| una disyunción "$q_1$ o $q_2$" | contrarrecíproca (su negación es una conjunción) |
| una negación: "no es racional", "no existe" | reducción al absurdo |
| para todo $n \in \mathbb{N}$ | inducción |

Las dos técnicas indirectas suelen ser intercambiables: el ejemplo de paridad también sale por contrarrecíproca ("si $n$ es impar, entonces $n + 2n^2 \neq m + m^2$"). Lo importante es **declarar** qué técnica se usa y qué se supone.

## Preguntas de repaso

> [!question]- Al probar $p \Rightarrow q$ por contrarrecíproca, ¿qué se supone y qué se debe llegar a mostrar?
> Se supone $\neg q$ y se debe llegar a $\neg p$. No se supone $p$ en ningún momento.

> [!question]- ¿En qué se diferencia la reducción al absurdo de la contrarrecíproca?
> En la contradicción se suponen a la vez $p$ y $\neg q$ y se busca **cualquier** contradicción; en la contrarrecíproca solo se supone $\neg q$ y el objetivo es exactamente $\neg p$.

> [!question]- Si $a + b \notin \mathbb{Q}$, ¿por qué al menos uno de $a$, $b$ es irracional?
> Por contrarrecíproca: si ambos fueran racionales, $a = \frac{p}{q}$ y $b = \frac{r}{s}$, y su suma $\frac{ps + rq}{qs}$ sería racional.

> [!question]- ¿Por qué $m(m+1)$ es siempre par?
> Entre dos enteros consecutivos uno es par, y un producto con un factor par es par.

> [!question]- ¿Es cierto que la suma de dos irracionales es irracional?
> No: $\sqrt{2}$ y $-\sqrt{2}$ son irracionales y su suma es $0$. Basta ese contraejemplo.
