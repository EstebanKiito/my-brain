---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[01 - Método directo]]"
---

# Contraejemplos

No toda afirmación universal es cierta, y para mostrarlo no hace falta un gran argumento: basta exhibir **un solo caso** en que falla. Ese caso es un contraejemplo, y refuta la afirmación "para todo" de inmediato.

## Refutar con un contraejemplo

Una afirmación universal dice "para todo $n$, se cumple $P(n)$". Su negación es "existe un $n$ para el que $P(n)$ es falsa". Por eso, para demostrar que la afirmación universal es falsa alcanza con **un** ejemplo donde no se cumpla: un contraejemplo.

> [!tip] Contraejemplo
> Para refutar "todo $n$ cumple $P(n)$" basta encontrar **un** $n$ con $\neg P(n)$. Encontrar el contraejemplo demuestra la falsedad; no probar nada más.

## Ejemplo: un polinomio "casi primo"

¿Es cierto que $f(n) = n^2 - n + 17$ es primo para todo entero positivo $n$?

**Respuesta:** No. Evaluando en $n = 17$,

$$
f(17) = 17^2 - 17 + 17 = 289 = 17^2,
$$

que no es primo. Un solo valor que falla basta para refutar la afirmación.

> [!warning] Muchos casos no demuestran nada
> Que $f(1), f(2), \dots, f(16)$ sean todos primos no prueba que siempre lo sean. La verificación de casos concretos da evidencia, pero no una demostración: el contraejemplo puede aparecer más adelante (aquí, en $n = 17$).

## Ejemplo: irracionales que se portan mal

¿Es cierto que el producto de dos números irracionales es siempre irracional?

**Respuesta:** No. Tómese $a = b = \sqrt{2}$, ambos irracionales. Su producto es $\sqrt{2} \cdot \sqrt{2} = 2$, que es racional.

Este ejemplo ilustra la técnica complementaria: ante una conjetura universal que no se ataca fácilmente, conviene buscar antes un contraejemplo; si aparece, se acabó el problema.

## Preguntas de repaso

> [!question]- ¿Cuántos contraejemplos se necesitan para refutar una afirmación universal?
> Uno solo. La afirmación "para todo $n$, $P(n)$" cae con un único $n$ donde $P(n)$ sea falsa.

> [!question]- ¿Qué se concluye si no se encuentra ningún contraejemplo?
> Nada definitivo: puede que la afirmación sea cierta, o que el contraejemplo no se haya encontrado todavía. La ausencia de contraejemplo no es una demostración.

> [!question]- Refute "todo número impar es primo" con un contraejemplo.
> $n = 9$ es impar y no es primo (es $3 \times 3$). Basta este valor.

> [!question]- ¿Por qué $f(n) = n^2 - n + 17$ falla justo en $n = 17$?
> Porque $f(17) = 17(17 - 1) + 17 = 17 \cdot 16 + 17 = 17 \cdot 17 = 17^2$. En general, $f(n) = n^2 - n + 17$ se anula el término $-n + 17$ cuando $n = 17$, dejando $17^2$.
