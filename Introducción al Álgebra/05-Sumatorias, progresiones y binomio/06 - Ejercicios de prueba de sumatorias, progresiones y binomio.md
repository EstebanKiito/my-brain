---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Progresiones aritméticas y geométricas]]"
  - "[[05 - Teorema del binomio]]"
---

# Ejercicios de prueba de sumatorias, progresiones y binomio

Preguntas de interrogaciones y exámenes anteriores. Los tipos que se repiten: calcular una suma con propiedades (traslación de índice, sumas conocidas, geométrica), una telescópica disfrazada, recuperar una progresión desde sus sumas, y encontrar el término independiente en un desarrollo binomial.

## Ejercicios

### 1. Calcular con traslación y sumas conocidas
Determine el valor de $\displaystyle\sum_{k=23}^{111} \left[(k-2)^2 - \frac{2^{2k}}{5^k}\right]$.

> [!example]- Solución
> Se separa en dos sumas y se nota que $\frac{2^{2k}}{5^k} = \left(\frac{4}{5}\right)^k$.
> - Con $j = k - 2$: $\sum_{k=23}^{111} (k-2)^2 = \sum_{j=21}^{109} j^2 = \frac{109 \cdot 110 \cdot 219}{6} - \frac{20 \cdot 21 \cdot 41}{6} = 437635 - 2870 = 434765$.
> - Geométrica desde $k = 23$: $\sum_{k=23}^{111} \left(\frac{4}{5}\right)^k = \frac{(4/5)^{23} - (4/5)^{112}}{1 - 4/5} = 5\left[\left(\frac{4}{5}\right)^{23} - \left(\frac{4}{5}\right)^{112}\right]$.
>
> Resultado: $434765 - 5\left[\left(\frac{4}{5}\right)^{23} - \left(\frac{4}{5}\right)^{112}\right]$. No se exige simplificar más.

### 2. Una progresión a partir de sus sumas
Sea $(a_k)$ una sucesión con $\sum_{k=1}^{n} a_k = \frac{n(13 - 3n)}{2}$ para todo $n \ge 1$. Sin usar inducción, demuestre que es aritmética y encuentre su término general.

> [!example]- Solución
> Con $n = 1$: $a_1 = \frac{1 \cdot 10}{2} = 5$. Para $n \ge 2$, $a_n = S_n - S_{n-1} = \frac{n(13-3n) - (n-1)(16-3n)}{2} = \frac{16 - 6n}{2} = 8 - 3n$, que en $n = 1$ también da $5$. Entonces $a_{n+1} - a_n = -3$ para todo $n$: es aritmética de diferencia $-3$ y $a_n = 5 - 3(n-1) = 8 - 3n$.

### 3. Telescópica con raíces de una PA
Sea $(a_k)$ aritmética de diferencia $d \neq 0$ y términos positivos. (a) Verifique que $\frac{1}{\sqrt{a_k} + \sqrt{a_{k+1}}} = \frac{\sqrt{a_{k+1}} - \sqrt{a_k}}{d}$. (b) Demuestre que $\displaystyle\sum_{k=1}^{n} \frac{1}{\sqrt{a_k} + \sqrt{a_{k+1}}} = \frac{n}{\sqrt{a_1} + \sqrt{a_{n+1}}}$.

> [!example]- Solución
> (a) Racionalizando: $\frac{\sqrt{a_{k+1}} - \sqrt{a_k}}{a_{k+1} - a_k} = \frac{\sqrt{a_{k+1}} - \sqrt{a_k}}{d}$.
> (b) Por (a) y la propiedad telescópica,
> $$\sum_{k=1}^{n} \frac{\sqrt{a_{k+1}} - \sqrt{a_k}}{d} = \frac{\sqrt{a_{n+1}} - \sqrt{a_1}}{d} = \frac{a_{n+1} - a_1}{d\left(\sqrt{a_{n+1}} + \sqrt{a_1}\right)} = \frac{nd}{d\left(\sqrt{a_{n+1}} + \sqrt{a_1}\right)},$$
> amplificando por el conjugado y usando $a_{n+1} - a_1 = nd$. Al cancelar $d$ queda la fórmula pedida.

### 4. Término independiente con un factor extra
Encuentre el término independiente de $x$ en $(2x + 1)\left(1 + \frac{2}{x}\right)^{15}$.

> [!example]- Solución
> El término general de $\left(1 + \frac{2}{x}\right)^{15}$ es $\binom{15}{k} 2^k x^{-k}$. Al multiplicar:
> - por $2x$: queda $\binom{15}{k} 2^{k+1} x^{1-k}$; independiente si $k = 1$: $\binom{15}{1} 2^2 = 60$.
> - por $1$: queda $\binom{15}{k} 2^k x^{-k}$; independiente si $k = 0$: $1$.
>
> Término independiente: $60 + 1 = 61$.

### 5. Término independiente con un parámetro
Sea $a \in \mathbb{R}$. (a) Calcule el término independiente de $x$ en $(x^3 + 1)\left(x + \frac{a}{x^2}\right)^9$. (b) ¿Para qué valores de $a$ el desarrollo no tiene término independiente?

> [!example]- Solución
> (a) El término general del binomio es $\binom{9}{k} a^k x^{9-3k}$. Multiplicado por $x^3$ es independiente si $12 - 3k = 0$ ($k = 4$): $126a^4$. Multiplicado por $1$, si $9 - 3k = 0$ ($k = 3$): $84a^3$. Total: $126a^4 + 84a^3 = 42a^3(3a + 2)$.
> (b) Cuando ese coeficiente es $0$: $a = 0$ o $a = -\frac{2}{3}$.

### 6. Progresiones con datos sueltos
(a) Los dos primeros términos de una PA son $-7$ y $-3$. Calcule $a_{101}$. (b) Encuentre la PG con $a_2 = -24$ y $a_5 = 81$.

> [!example]- Solución
> (a) $d = 4$ y $a_{101} = -7 + 100 \cdot 4 = 393$.
> (b) $\frac{a_5}{a_2} = r^3 = -\frac{27}{8}$, así que $r = -\frac{3}{2}$ (única raíz cúbica real) y $a_1 = \frac{-24}{-3/2} = 16$. Luego $a_n = 16\left(-\frac{3}{2}\right)^{n-1}$.

### 7. Una recurrencia con dosis diarias
Un paciente recibe una dosis inicial de $X_0$ mg y luego $100$ mg cada día; el cuerpo elimina la mitad cada 24 horas, así que $X_n = \frac{X_{n-1}}{2} + 100$. (a) Pruebe que $X_n = \frac{X_0}{2^n} + \sum_{j=1}^{n} \frac{100}{2^{j-1}}$. (b) Sin inducción, concluya que $X_n = \frac{X_0 - 200}{2^n} + 200$. (c) ¿Qué $X_0$ hace que $X_n$ sea constante?

> [!example]- Solución
> (a) Por inducción. Caso $n = 1$: $\frac{X_0}{2} + 100$ en ambos lados. Paso: $X_{k+1} = \frac{X_k}{2} + 100 = \frac{X_0}{2^{k+1}} + \sum_{j=1}^{k} \frac{100}{2^{j}} + 100$; trasladando el índice ($j \to j + 1$), la suma es $\sum_{j=2}^{k+1} \frac{100}{2^{j-1}}$, y el $100$ suelto es el término $j = 1$.
> (b) La suma es geométrica con $a_1 = 100$, $r = \frac{1}{2}$ y $n$ términos: $100 \cdot \frac{1 - 2^{-n}}{1/2} = 200 - \frac{200}{2^n}$. Sumando $\frac{X_0}{2^n}$ queda lo pedido.
> (c) $X_n$ no depende de $n$ exactamente cuando $X_0 - 200 = 0$: $X_0 = 200$ mg (y entonces $X_n = 200$ siempre).

### 8. La suma de $k a^k$
Sea $a \neq 1$ y $S_n = \sum_{k=1}^{n} k a^k$. (a) Por inducción, pruebe que $(a - 1)S_n + \sum_{k=0}^{n-1} a^{k+1} = n a^{n+1}$. (b) Concluya que $S_n = \dfrac{a - (n+1)a^{n+1} + n a^{n+2}}{(1-a)^2}$.

> [!example]- Solución
> (a) Caso $n = 1$: $(a-1)a + a = a^2$. Paso: con $S_{n+1} = S_n + (n+1)a^{n+1}$ y separando el último término de la suma,
> $$(a-1)S_{n+1} + \sum_{k=0}^{n} a^{k+1} = \underbrace{(a-1)S_n + \sum_{k=0}^{n-1} a^{k+1}}_{n a^{n+1} \text{ (HI)}} + (n+1)(a-1)a^{n+1} + a^{n+1} = (n+1)a^{n+2}.$$
> (b) La suma es geométrica: $\sum_{k=0}^{n-1} a^{k+1} = \frac{a - a^{n+1}}{1 - a}$. Despejando $S_n$ de (a) y llevando a denominador común $(1-a)^2$ sale la fórmula. Con $a = 2$ da $\sum_{k=1}^{n} k\,2^k = (n-1)2^{n+1} + 2$, otra pregunta que también se ha tomado por inducción directa.

## Preguntas de repaso

> [!question]- En el ejercicio 1, ¿cuántos términos tiene cada suma y por qué importa?
> $111 - 23 + 1 = 89$. Importa al usar la fórmula geométrica: el exponente del numerador depende del número de términos ($112 = 111 + 1$).

> [!question]- Al buscar el término independiente de $P(x) \cdot (\dots)^n$, ¿por qué a veces aparecen dos aportes?
> Porque cada sumando de $P(x)$ desplaza las potencias de $x$ de una manera distinta, y cada uno puede combinarse con un término distinto del binomio para dar $x^0$.

> [!question]- ¿Cómo se obtiene $a_n$ si se conoce $S_n$ para todo $n$?
> $a_1 = S_1$ y $a_n = S_n - S_{n-1}$ para $n \ge 2$.
