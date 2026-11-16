---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[03 - Unicidad, acotación y sucesiones monótonas]]"
---

# Álgebra de límites y cocientes de polinomios

Calcular cada límite con la definición sería interminable. Las **reglas del álgebra de límites** permiten construir límites complicados a partir de pocos límites básicos ($c$, $\tfrac{1}{n^p}$, $x^n$ con $|x| < 1$), y cubren la gran mayoría de los cálculos de las interrogaciones: cocientes de polinomios, raíces con conjugado y cocientes de exponenciales.

## Las reglas

> [!tip] Álgebra de límites
> Si $\lim a_n = L$ y $\lim b_n = M$, entonces:
> 1. $\lim (a_n + b_n) = L + M$.
> 2. $\lim (a_n \cdot b_n) = L \cdot M$ (en particular, $\lim c\,a_n = cL$).
> 3. $\lim \dfrac{a_n}{b_n} = \dfrac{L}{M}$ si $M \neq 0$.

Todas las demostraciones siguen el esquema de la definición ($\tfrac{\varepsilon}{2}$ para la suma, acotación para el producto). Importa la **hipótesis**: ambos límites deben existir (ser finitos), y en el cociente $M \neq 0$. Cuando alguna falla, hay que transformar la expresión antes de aplicar las reglas.

> [!tip] El límite básico $\tfrac{1}{n^p}$
> Si $p > 0$, entonces $\displaystyle\lim_{n \to \infty}\frac{1}{n^p} = 0$.

*Demostración.* Dado $\varepsilon > 0$, $\tfrac{1}{n^p} < \varepsilon \iff n > \tfrac{1}{\varepsilon^{1/p}}$; por Arquímedes existe $N$ con $N > \tfrac{1}{\varepsilon^{1/p}}$, y para $n > N$ vale $\tfrac{1}{n^p} < \varepsilon$. $\blacksquare$

## Cociente de polinomios en $n$

> [!tip] Regla práctica
> Para $\displaystyle\lim_{n \to \infty}\frac{P(n)}{Q(n)}$ con $P$ y $Q$ polinomios, se **amplifica por $\tfrac{1}{n^p}$**, donde $p$ es el grado de $Q$. Cada término de la forma $\tfrac{c}{n^k}$ con $k \ge 1$ tiende a $0$ y quedan los coeficientes principales.

**Ejemplos.**
- $\dfrac{n}{n + 1} = \dfrac{1}{1 + 1/n} \to 1$.
- $\dfrac{n^3 + 2n^2 - 4}{n^4 + 2}$: se divide arriba y abajo por $n^4$: $\dfrac{1/n + 2/n^2 - 4/n^4}{1 + 2/n^4} \to \dfrac{0}{1} = 0$.
- $\dfrac{n + n^2}{n^3} = \dfrac{1}{n^2} + \dfrac{1}{n} \to 0$ (Guía 10).
- $\dfrac{3n^3 + 2n^2 + n}{5n^3 + 8} = \dfrac{3 + 2/n + 1/n^2}{5 + 8/n^3} \to \dfrac{3}{5}$ (I3, 2025-2).

La regla resume tres casos: si el grado del numerador es **menor** que el del denominador el límite es $0$; si es **igual**, el cociente de coeficientes principales; si es **mayor**, la sucesión no converge (diverge a $\pm\infty$, que se estudia en el tema siguiente).

## Raíces: multiplicar por el conjugado

Cuando aparece una diferencia de raíces (forma $\infty - \infty$), el álgebra de límites no sirve directamente. Se multiplica y divide por el **conjugado** para llegar a un cociente.

**$\lim\left(\sqrt{n^2 + 5n + 6} - n\right)$ (I6, 2025-1).**
$$\sqrt{n^2 + 5n + 6} - n = \frac{(n^2 + 5n + 6) - n^2}{\sqrt{n^2 + 5n + 6} + n} = \frac{5n + 6}{\sqrt{n^2 + 5n + 6} + n} = \frac{5 + 6/n}{\sqrt{1 + 5/n + 6/n^2} + 1} \to \frac{5}{2}.$$

Del mismo modo: $\sqrt{n^2 - n + 1} - n \to -\tfrac{1}{2}$ (I6, 2026-1), $\sqrt{n^2 + 3n + 5} - n \to \tfrac{3}{2}$ (I10, 2020-1) y $\sqrt{n^2 + 1} - n = \dfrac{1}{\sqrt{n^2 + 1} + n} \to 0$.

**$\lim\sqrt{n}\left(\sqrt{n + 1} - \sqrt{n}\right)$ (I8, 2022-1).** Con el conjugado: $\sqrt{n}\cdot\dfrac{1}{\sqrt{n + 1} + \sqrt{n}} = \dfrac{1}{\sqrt{1 + 1/n} + 1} \to \dfrac{1}{2}$. Y $\sqrt{n + 1} - \sqrt{n} = \dfrac{1}{\sqrt{n + 1} + \sqrt{n}} \to 0$ (Guía 10).

**Una raíz cúbica (I6, 2025-1): $\lim\dfrac{\sqrt[3]{n^2 + 1}}{n + 1}$.** Se amplifica por $\tfrac{1}{n}$ y se entra $n$ en la raíz: $\dfrac{\sqrt[3]{(n^2 + 1)/n^3}}{1 + 1/n} = \dfrac{\sqrt[3]{1/n + 1/n^3}}{1 + 1/n} \to \dfrac{0}{1} = 0$.

**Con una raíz y un cociente (clase 24): $\lim\dfrac{\sqrt{2n^2 + 1}}{3n - 5}$.** Se divide por $n$: $\dfrac{\sqrt{2 + 1/n^2}}{3 - 5/n} \to \dfrac{\sqrt{2}}{3}$.

## Cocientes de exponenciales

Se divide por la **potencia dominante** y se usa que $x^n \to 0$ si $|x| < 1$.

- $\dfrac{3^{n+1} + 2^{n+1}}{3^n + 2^n} = \dfrac{3 + 2(2/3)^n}{1 + (2/3)^n} \to 3$ (I8, 2022-1).
- $\dfrac{a^{n+1} + b^{n+1}}{a^n + b^n} \to a$ si $a > b > 0$: se divide por $a^n$ y $\left(\tfrac{b}{a}\right)^n \to 0$ (I7, 2026-1).
- $\dfrac{3^n + 2^n}{5^n + 2^n} = \dfrac{(3/5)^n + (2/5)^n}{1 + (2/5)^n} \to 0$ (I7, 2025-1).

> [!warning] Dos errores frecuentes
> - Aplicar la regla del cociente cuando $M = 0$ o cuando los dos límites son infinitos (forma $\tfrac{\infty}{\infty}$): primero hay que dividir por $n^p$ para que los límites sean finitos.
> - Escribir $\lim(\sqrt{n^2 + 5n + 6} - n) = \infty - \infty = 0$. La diferencia de dos sucesiones que tienden a $\infty$ es una forma **indeterminada**: puede ser cualquier valor (aquí $\tfrac{5}{2}$).

## Preguntas de repaso

> [!question]- ¿Cómo se calcula $\lim\frac{2n^2 + 3n}{5n^2 - 1}$?
> Se divide por $n^2$: $\frac{2 + 3/n}{5 - 1/n^2} \to \frac{2}{5}$.

> [!question]- ¿Por qué hay que multiplicar por el conjugado en $\sqrt{n^2 + n} - n$?
> Porque ambos términos tienden a $\infty$ y la resta es indeterminada; el conjugado la convierte en $\frac{n}{\sqrt{n^2 + n} + n}$, un cociente al que sí se aplica el álgebra de límites (límite $\frac{1}{2}$).

> [!question]- ¿Qué hace falta para escribir $\lim\frac{a_n}{b_n} = \frac{L}{M}$?
> Que $\lim a_n = L$ y $\lim b_n = M$ existan como números reales y que $M \neq 0$.

> [!question]- ¿Cuál es el límite de $\frac{2^n}{3^n + 1}$?
> Se divide por $3^n$: $\frac{(2/3)^n}{1 + 3^{-n}} \to \frac{0}{1} = 0$.
