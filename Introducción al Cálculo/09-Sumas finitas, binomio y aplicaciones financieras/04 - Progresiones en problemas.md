---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - origen/complemento
prerrequisitos:
  - "[[01 - Sucesiones y formas de definirlas]]"
  - "[[02 - Sumas telescópicas y geométricas en la práctica]]"
---

# Progresiones en problemas

Las progresiones aritméticas y geométricas aparecen en problemas donde se dan **dos datos** (por ejemplo, dos términos) y se pide un tercero, o la suma de varios. Todo se resuelve con dos fórmulas de término general y dos de suma. Esta nota las junta con la forma de plantear el sistema de ecuaciones.

## Fórmulas

> [!tip] Progresión aritmética (primer término $c$, diferencia $d$)
> - Término general: $a_n = c + (n - 1)d$.
> - Suma de los $n$ primeros: $S_n = \dfrac{n}{2}\,(a_1 + a_n) = \dfrac{n}{2}\big(2c + (n - 1)d\big)$.

> [!tip] Progresión geométrica (primer término $c$, razón $r$)
> - Término general: $a_n = c\,r^{n-1}$.
> - Suma de los $n$ primeros: $S_n = c\,\dfrac{1 - r^n}{1 - r}$ (para $r \neq 1$).

La suma aritmética es la de Gauss: se pareja el primero con el último, el segundo con el penúltimo, etc., y cada pareja suma lo mismo. La geométrica es la suma de potencias de la nota anterior.

> [!tip] Cómo atacar un problema
> 1. Identificar si es aritmética o geométrica.
> 2. Escribir cada dato como una ecuación con $c$ y $d$ (o $c$ y $r$).
> 3. Resolver el sistema y responder lo que se pide.

## Problemas de la Guía 9

**Dos términos (aritmética).** El décimo término es $\tfrac{55}{2}$ y el segundo $\tfrac{7}{2}$. Restando, $8d = 24$, $d = 3$, y $a_1 = a_2 - d = \tfrac{7}{2} - 3 = \tfrac{1}{2}$.

**Suma de una aritmética.** $-3, -\tfrac{3}{2}, 0, \tfrac{3}{2}, 3, \ldots, 30$ tiene $d = \tfrac{3}{2}$. Para el último término: $-3 + (n - 1)\tfrac{3}{2} = 30 \Rightarrow n = 23$. La suma es $\tfrac{23}{2}(-3 + 30) = \tfrac{621}{2}$.

**Cuántos términos para una suma.** Con $c = 5$ y $d = 2$: $\tfrac{n}{2}(10 + 2(n - 1)) = n(n + 4) = 2700 \Rightarrow n^2 + 4n - 2700 = 0 \Rightarrow n = 50$ (la raíz negativa se descarta).

**Una geométrica por sus términos.** $a_1 = 8$ y $a_3 = 4$ dan $r^2 = \tfrac{1}{2}$, y $a_5 = 8r^4 = 2$. Con razón $\tfrac{3}{2}$ y $a_5 = 1$: $a_3 = \dfrac{a_5}{r^2} = \tfrac{4}{9}$ (porque $a_5 = a_3 r^2$).

**Suma de una geométrica.** $c = 5$, $r = 2$, seis términos: $5\cdot\dfrac{1 - 2^6}{1 - 2} = 315$. Y el término $118\,098$ de $2, 6, 18, \ldots$: con $r = 3$, $2\cdot 3^{n-1} = 118\,098 \Rightarrow 3^{n-1} = 59\,049 = 3^{10} \Rightarrow n = 11$.

**Un término general que hay que descubrir.** $\sqrt{2},\ \sqrt{2\sqrt{2}},\ \sqrt{2\sqrt{2\sqrt{2}}},\ \ldots$ Como $a_1 = 2^{1/2}$, $a_2 = 2^{3/4}$, $a_3 = 2^{7/8}$, se conjetura $a_n = 2^{(2^n - 1)/2^n} = 2^{1 - 2^{-n}}$. Es una **recurrencia**: $a_{n+1} = \sqrt{2\,a_n}$; el exponente $e_n$ de $2$ cumple $e_{n+1} = \tfrac{1 + e_n}{2}$ con $e_1 = \tfrac{1}{2}$, que se prueba por inducción: $\tfrac{1 + 1 - 2^{-n}}{2} = 1 - 2^{-(n+1)}$.

## Problemas de pruebas

**Una aritmética y una geométrica enlazadas (I7, 2023-1).** $\{a_n\}$ geométrica con $a_1 = a$, $a_2 = 10$, $a_3 = c$, y $\{b_n\}$ aritmética con $b_1 = a - 1$, $b_2 = 8$, $b_3 = c - 8$. La geométrica da $\tfrac{10}{a} = \tfrac{c}{10}$, es decir $ac = 100$. La aritmética da $8 - (a - 1) = (c - 8) - 8$, es decir $a + c = 25$. Sustituyendo, $a^2 - 25a + 100 = 0$, con $a = 20$ y $c = 5$, o bien $a = 5$ y $c = 20$ (la pauta escribe "$b = 20$" en el segundo caso, pero es $c = 20$).

**Contar términos (I3, 2023-2).** El primer, segundo y último término de una aritmética son $5$, $9$ y $101$. La diferencia es $4$ y $5 + (m - 1)4 = 101$ da $m = 25$.

> [!warning] Errores frecuentes
> - Confundir el término $a_n$ con la suma $S_n$.
> - Usar la fórmula geométrica con $r = 1$ (da $0/0$; la suma es $nc$).
> - Olvidar que una cantidad entera de términos exige $n \in \mathbb{N}$: descartar las raíces negativas o no enteras.

## Preguntas de repaso

> [!question]- ¿Cuál es la suma de $5 + 8 + 11 + \dots + 50$?
> Es aritmética con $d = 3$: $50 = 5 + 3(n - 1)$ da $n = 16$ y $S = \frac{16}{2}(5 + 50) = 440$.

> [!question]- ¿Cómo se halla el quinto término de una geométrica con $a_1 = 8$ y $a_3 = 4$?
> $r^2 = \frac{a_3}{a_1} = \frac{1}{2}$ y $a_5 = a_1 r^4 = 8 \cdot \frac{1}{4} = 2$.

> [!question]- ¿Por qué se emparejan primero con último en la suma aritmética?
> Porque $a_1 + a_n = a_2 + a_{n-1} = \dots$: todas las parejas suman lo mismo, así que hay $\frac{n}{2}$ parejas de valor $a_1 + a_n$.
