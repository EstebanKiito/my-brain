---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de límite de una sucesión]]"
---

# Demostrar límites con la definición

"Demuestre, usando la definición de límite, que $\lim a_n = L$" es una pregunta fija de las interrogaciones. El método es siempre el mismo: calcular y simplificar $|a_n - L|$, **acotarlo** por algo simple que dependa solo de $n$ (como $\tfrac{c}{n}$), despejar $n$ y usar el principio de Arquímedes para elegir $N$. Lo difícil es la acotación; por eso conviene tener claras las técnicas.

## El método en cuatro pasos

> [!tip] Receta
> 1. Sea $\varepsilon > 0$ arbitrario (siempre se declara).
> 2. Simplificar $|a_n - L|$ hasta una expresión sencilla.
> 3. **Acotarla** por una cantidad $b_n$ más simple (por ejemplo $\tfrac{c}{n}$ o $\tfrac{c}{n + 1}$), válida para $n \ge$ algún $n_1$.
> 4. Elegir $N \ge n_1$ (con Arquímedes) tal que $b_N < \varepsilon$. Entonces para $n > N$: $|a_n - L| \le b_n \le b_N < \varepsilon$.

Se puede **despejar** $n$ cuando $|a_n - L|$ es exacto (ejemplos 1 y 2); si no, hay que acotar (ejemplos 3 a 5). Cualquier $N$ que cumpla es válido: no hace falta el mínimo.

## Ejemplos con despeje exacto

**Ejemplo 1: $a_n = 1 + \tfrac{5}{n + 1}$, $L = 1$ (clase 21).** $|a_n - 1| = \tfrac{5}{n + 1}$. Se quiere $\tfrac{5}{n + 1} < \varepsilon \iff \tfrac{5}{\varepsilon} - 1 < n$. Por Arquímedes existe $N \in \mathbb{N}$ con $N > \tfrac{5}{\varepsilon} - 1$; si $n > N$, entonces $\tfrac{5}{\varepsilon} - 1 < n$, o sea $\tfrac{5}{\varepsilon} < n + 1$ y $\tfrac{5}{n + 1} < \varepsilon$.

**Ejemplo 2: $a_n = \tfrac{n}{n + 1}$, $L = 1$ (clase 21).** $|a_n - 1| = \tfrac{1}{n + 1}$; $\tfrac{1}{n + 1} < \varepsilon \iff \tfrac{1}{\varepsilon} - 1 < n$. Se elige $N > \tfrac{1}{\varepsilon} - 1$.

**Ejemplo 3: $a_n = \tfrac{n + 1}{n - 1}$, $L = 1$ (I6, 2026-1).** Para $n \ge 2$, $|a_n - 1| = \tfrac{2}{n - 1}$. Se pide $\tfrac{2}{n - 1} < \varepsilon \iff \tfrac{2}{\varepsilon} + 1 < n$. Por Arquímedes existe un entero $n_0 \ge 2$ con $n_0 > \tfrac{2}{\varepsilon} + 1$; vale para todo $n \ge n_0$.

## Ejemplos con acotación

**Ejemplo 4: $a_n = \dfrac{3n^2 + 1}{n^2 + n + 1}$, $L = 3$ (I7, 2022-1).** $|a_n - 3| = \dfrac{3n + 2}{n^2 + n + 1}$. Se acota el numerador y el denominador: $3n + 2 \le 5n$ y $n^2 + n + 1 > n^2 + n$, de modo que
$$|a_n - 3| \le \frac{5n}{n^2 + n} = \frac{5}{n + 1}.$$
Ahora basta $\tfrac{5}{n + 1} < \varepsilon$, como en el ejemplo 1: se escoge $N > \tfrac{5}{\varepsilon} - 1$ y, para $n > N$, $|a_n - 3| \le \tfrac{5}{n + 1} < \varepsilon$.

**Ejemplo 5: $a_n = \dfrac{n^2}{2n^2 + n + 1}$, $L = \tfrac{1}{2}$ (I9, 2020-1).** $\left|a_n - \tfrac{1}{2}\right| = \dfrac{n + 1}{2(2n^2 + n + 1)} = \dfrac{1}{n}\cdot\dfrac{1 + 1/n}{2(2 + 1/n + 1/n^2)}$. Para $n \ge 1$ el segundo factor es $\le 1$ (el numerador es $\le 2$ y el denominador $\ge 4$), luego $\left|a_n - \tfrac{1}{2}\right| \le \tfrac{1}{n}$. Se toma $n_0$ con $\tfrac{1}{n_0} < \varepsilon$ y para $n \ge n_0$ queda $< \varepsilon$.

**Ejemplo 6: $a_n = \sqrt{\tfrac{2n + 1}{n}}$, $L = \sqrt{2}$ (I6, 2026-1).** Se escribe $a_n = \sqrt{2 + \tfrac{1}{n}}$ y se racionaliza:
$$|a_n - \sqrt{2}| = \frac{\tfrac{1}{n}}{\sqrt{2 + \tfrac{1}{n}} + \sqrt{2}} \le \frac{1}{n\cdot 2\sqrt{2}} \le \frac{1}{n},$$
pues el denominador es $\ge 2\sqrt{2} > 1$. Entonces basta $\tfrac{1}{n} < \varepsilon$.

## Técnicas de acotación

- **Numerador hacia arriba, denominador hacia abajo:** $\tfrac{3n + 2}{n^2 + n + 1} \le \tfrac{5n}{n^2 + n}$ (se agranda el numerador y se achica el denominador).
- **Racionalizar** cuando hay una raíz: $|\sqrt{u} - \sqrt{v}| = \dfrac{|u - v|}{\sqrt{u} + \sqrt{v}}$.
- **Factorizar $\tfrac{1}{n}$** y acotar el resto por una constante.
- **Cota de la forma $\tfrac{c}{n + k}$ o $\tfrac{c}{n - k}$:** al despejar $n$ aparece $N > \tfrac{c}{\varepsilon} \mp k$.

> [!warning] Errores frecuentes
> - Elegir un $N$ sin demostrar que funciona: hay que verificar que $n > N$ implica $|a_n - L| < \varepsilon$.
> - Acotar en sentido contrario (achicar el numerador): la cota debe ser una **cota superior** de $|a_n - L|$.
> - Olvidar el umbral inferior ($n \ge 2$ para que $n - 1 > 0$, por ejemplo) al dividir por expresiones que podrían ser $0$ o negativas.
> - Usar $\varepsilon$ específico (como $\varepsilon = 0{,}1$): la definición exige **todo** $\varepsilon > 0$.

## Preguntas de repaso

> [!question]- Demuestre con la definición que $\lim \frac{2n + 1}{n} = 2$.
> $\left|\frac{2n + 1}{n} - 2\right| = \frac{1}{n}$. Dado $\varepsilon > 0$, por Arquímedes existe $N$ con $\frac{1}{N} < \varepsilon$; si $n > N$, $\frac{1}{n} < \frac{1}{N} < \varepsilon$.

> [!question]- ¿Por qué se puede acotar $\frac{3n + 2}{n^2 + n + 1}$ por $\frac{5}{n + 1}$?
> Porque $3n + 2 \le 5n$ (para $n \ge 1$) y $n^2 + n + 1 > n^2 + n = n(n + 1)$; al achicar el denominador y agrandar el numerador, la fracción crece.

> [!question]- ¿Qué se obtiene de $\frac{5}{n + 1} < \varepsilon$ al despejar $n$?
> $n > \frac{5}{\varepsilon} - 1$. Se elige un natural $N$ mayor que ese número (existe por Arquímedes).
