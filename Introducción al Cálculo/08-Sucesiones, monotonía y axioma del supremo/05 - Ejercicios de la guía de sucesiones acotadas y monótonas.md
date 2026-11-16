---
ramo: "Introducción al Cálculo"
tema: "Sucesiones, monotonía y axioma del supremo"
tags:
  - intro-calculo/sucesiones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Sucesiones acotadas y monótonas]]"
---

# Ejercicios de la guía de sucesiones acotadas y monótonas

De los dieciséis ejercicios de la Guía 10, cuatro piden primero **probar monotonía y cota** (los ejercicios 1, 2, 6 y 12). Aquí se resuelve esa parte; el cálculo del límite se completa en los temas de límites, donde se dispone del teorema de la sucesión monótona. Los demás (ejercicios 3 a 5, 7 a 11 y 13 a 16) son de cálculo de límites.

## Ejercicios

### 1. Un producto de fracciones
Demuestre que $a_n = \dfrac{1\cdot 3\cdot 5\cdots(2n - 1)}{2\cdot 4\cdot 6\cdots 2n}$ es convergente y acote su límite.

> [!example]- Solución (monotonía y cota)
> Escrita como producto, $a_n = \prod_{k=1}^{n}\dfrac{2k - 1}{2k}$ y $a_{n+1} = a_n \cdot \dfrac{2n + 1}{2n + 2}$ con $\tfrac{2n + 1}{2n + 2} < 1$. Como $a_n > 0$, resulta $a_{n+1} < a_n$: **estrictamente decreciente**. Está acotada inferiormente por $0$. Por el teorema de la sucesión monótona, **converge**. Como $a_1 = \tfrac{1}{2}$ y decrece, el límite $L$ cumple $0 \le L \le \tfrac{1}{2}$.

### 2. Una recurrencia lineal
Demuestre que $a_1 = 2$, $a_{n+1} = \dfrac{a_n + 6}{2}$ es convergente.

> [!example]- Solución (monotonía y cota)
> **Cota:** $a_n < 6$ por inducción: $a_1 = 2 < 6$ y, si $a_n < 6$, $a_{n+1} = \tfrac{a_n + 6}{2} < \tfrac{12}{2} = 6$. **Monotonía:** $a_{n+1} - a_n = \tfrac{6 - a_n}{2} > 0$ por la cota. Luego es estrictamente creciente y acotada superiormente: converge. Los términos son $2, 4, 5, 5{,}5, \ldots$ y el límite $L$ cumple $L = \tfrac{L + 6}{2}$, es decir $L = 6$.

### 3. Raíces anidadas
Demuestre que $a_1 = \sqrt{2}$, $a_{n+1} = \sqrt{2 + a_n}$ es convergente.

> [!example]- Solución (monotonía y cota)
> **Cota:** $a_n < 2$ por inducción: $a_1 = \sqrt{2} < 2$ y si $a_n < 2$, entonces $a_{n+1} = \sqrt{2 + a_n} < \sqrt{4} = 2$. **Monotonía:** $a_{n+1} - a_n = \sqrt{2 + a_n} - a_n = \dfrac{(2 + a_n) - a_n^2}{\sqrt{2 + a_n} + a_n} = \dfrac{(2 - a_n)(1 + a_n)}{\sqrt{2 + a_n} + a_n} > 0$, porque $0 < a_n < 2$. Estrictamente creciente y acotada: converge. Su límite cumple $L = \sqrt{2 + L}$, o sea $L^2 - L - 2 = 0$ y, siendo $L > 0$, $L = 2$.

### 4. Una diferencia de raíces
Sea $a_n = \sqrt{n^2 + n} - n$. Demuestre que es monótona creciente y acotada; calcule su límite.

> [!example]- Solución (monotonía y cota)
> Multiplicando por el conjugado, $a_n = \dfrac{n}{\sqrt{n^2 + n} + n} = \dfrac{1}{\sqrt{1 + 1/n} + 1}$. Al crecer $n$, $\tfrac{1}{n}$ decrece, $\sqrt{1 + 1/n}$ decrece y el denominador decrece, luego $a_n$ **crece**. Como $\sqrt{1 + 1/n} > 1$, el denominador supera $2$ y $0 < a_n < \tfrac{1}{2}$: está **acotada**. Su límite es $\tfrac{1}{2}$ (cuando $\tfrac{1}{n} \to 0$ el denominador tiende a $2$).

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 2 se demuestra primero la cota?
> Porque la monotonía $a_{n+1} - a_n = \frac{6 - a_n}{2} > 0$ depende de que $a_n < 6$. La cota se prueba por inducción sin necesitar la monotonía.

> [!question]- ¿Qué característica de la recurrencia permite la inducción de la cota en el ejercicio 3?
> Que $x \mapsto \sqrt{2 + x}$ es creciente: si $a_n < 2$ entonces $\sqrt{2 + a_n} < \sqrt{4}$.

> [!question]- ¿Cómo se acota el límite del ejercicio 1 sin calcularlo?
> Como la sucesión es decreciente, su límite es menor o igual que $a_1 = \frac{1}{2}$, y como es positiva, es mayor o igual que $0$.
