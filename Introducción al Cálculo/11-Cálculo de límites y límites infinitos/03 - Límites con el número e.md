---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[01 - El número e y la función exponencial]]"
  - "[[04 - Álgebra de límites y cocientes de polinomios]]"
---

# Límites con el número e

Las expresiones del tipo $(1 + \text{algo pequeño})^{\text{algo grande}}$ son una forma indeterminada ($1^\infty$) que el álgebra de límites no resuelve. Se resuelven reconociendo la sucesión que **define** a $e$ y haciendo un cambio de variable que la deje a la vista.

## La base: la definición de e

> [!tip] Definición de $e$
> $\displaystyle\lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n = e$. Más en general, si $a_n \to +\infty$, entonces $\left(1 + \dfrac{1}{a_n}\right)^{a_n} \to e$ y, para una constante $c$, $\left(1 + \dfrac{c}{a_n}\right)^{a_n} \to e^{c}$.

La segunda forma es la que se usa en los ejercicios: la sucesión $a_n$ no tiene por qué ser $n$ (puede ser $3n - 4$, $n + 1$, $3 + n^2$...), y el resultado es el mismo con tal de que $a_n \to \infty$. (Es el límite de $\left(1 + \tfrac{1}{k}\right)^k$ evaluado a lo largo de una sucesión de índices que tiende a infinito.)

## Método

> [!tip] Cuatro pasos
> 1. Escribir la base como $1 + \dfrac{1}{a_n}$ para una sucesión $a_n \to \infty$ conveniente (se descompone el numerador: $\tfrac{n + 2}{n + 1} = 1 + \tfrac{1}{n + 1}$).
> 2. Reescribir el exponente como $a_n \cdot c_n$, con $c_n$ convergente.
> 3. Entonces $\left(1 + \tfrac{1}{a_n}\right)^{a_n c_n} = \left[\left(1 + \tfrac{1}{a_n}\right)^{a_n}\right]^{c_n} \to e^{\lim c_n}$.
> 4. Aplicar el álgebra de límites a la potencia.

## Ejemplos

**$\left(\dfrac{n + 2}{n + 1}\right)^{3n}$ (Examen, 2025-1).** $\dfrac{n + 2}{n + 1} = 1 + \dfrac{1}{n + 1}$. Con $a_n = n + 1$ y exponente $3n = 3(n + 1) - 3$:
$$\left(1 + \tfrac{1}{n + 1}\right)^{3(n + 1) - 3} = \left[\left(1 + \tfrac{1}{n + 1}\right)^{n + 1}\right]^3\left(1 + \tfrac{1}{n + 1}\right)^{-3} \to e^3\cdot 1 = e^3.$$

**$\left(\dfrac{n + 3}{n + 2}\right)^{5n}$ (I7, 2025-1).** $= \left(1 + \tfrac{1}{n + 2}\right)^{5n}$ con $a_n = n + 2$ y $\tfrac{5n}{n + 2} \to 5$: el límite es $e^5$.

**$\left(\dfrac{3n + 1}{3n - 4}\right)^{n - 2}$ (I8, 2026-1).** $\dfrac{3n + 1}{3n - 4} = 1 + \dfrac{5}{3n - 4} = 1 + \dfrac{1}{a_n}$ con $a_n = \tfrac{3n - 4}{5} \to \infty$. El exponente es $n - 2 = a_n\cdot\tfrac{5(n - 2)}{3n - 4}$, y $\tfrac{5(n - 2)}{3n - 4} \to \tfrac{5}{3}$. Por tanto el límite es $e^{5/3}$.

**$\left(\dfrac{n^2 + 1}{3 + n^2}\right)^{n^2}$ (Examen, 2026-1).** La base es $1 + \dfrac{-2}{3 + n^2}$. Con $a_n = 3 + n^2 \to \infty$: $\left(1 + \tfrac{-2}{a_n}\right)^{a_n} \to e^{-2}$, y el exponente es $n^2 = a_n\cdot\tfrac{n^2}{3 + n^2}$ con $\tfrac{n^2}{3 + n^2} \to 1$. Luego el límite es $\left(e^{-2}\right)^{1} = e^{-2}$.

**Con un cociente cuadrático (Guía 10, 13c).** $\left(\dfrac{n^2 + 2n + 3}{n^2 + 2n + 1}\right)^{(n+1)^2} = \left(1 + \dfrac{2}{(n + 1)^2}\right)^{(n+1)^2}$. Con $a_n = \tfrac{(n + 1)^2}{2}$ y exponente $2a_n$, el límite es $e^2$.

**$\left(1 + \dfrac{1}{2n}\right)^n$ y $\left(1 + \dfrac{1}{n + 1}\right)^{4n}$ (Guía 10, 13a y 13b).** El primero es $\left[\left(1 + \tfrac{1}{2n}\right)^{2n}\right]^{1/2} \to e^{1/2} = \sqrt{e}$. El segundo es $\left[\left(1 + \tfrac{1}{n + 1}\right)^{n + 1}\right]^{4n/(n + 1)} \to e^4$.

**La sucesión $\left(\dfrac{n + 1}{n}\right)^n$ (Guía 10, ejercicio 8).** Es exactamente $\left(1 + \tfrac{1}{n}\right)^n$: converge, y su límite es $e$.

## Un recordatorio sobre la forma indeterminada $1^\infty$

No se puede concluir que $1^\infty = 1$: si la base tiende a $1$ pero el exponente tiende a $\infty$, el resultado depende de **qué tan rápido** se acerca a $1$ la base. Con base $1 + \tfrac{1}{n}$ y exponente $n$ el límite es $e$; con base $1 + \tfrac{1}{n}$ y exponente $\sqrt{n}$ el límite es $1$; con exponente $n^2$ es $+\infty$.

> [!warning] Errores frecuentes
> - Reemplazar la base por su límite: $\left(\tfrac{n + 2}{n + 1}\right)^{3n} \neq 1^{3n} = 1$.
> - Olvidar que el exponente debe ser **exactamente** $a_n$ para aplicar la definición; la diferencia se arregla con una potencia ($\left[\cdots\right]^{c_n}$).
> - Escribir $e^{n}$ en lugar de $e^{\lim c_n}$: el exponente $c_n$ se evalúa en el límite.

## Preguntas de repaso

> [!question]- ¿Cuál es el límite de $\left(1 + \frac{3}{n}\right)^n$?
> Con $a_n = \frac{n}{3}$ y exponente $n = 3a_n$: $\left[\left(1 + \frac{1}{a_n}\right)^{a_n}\right]^3 \to e^3$.

> [!question]- ¿Por qué $\left(1 + \frac{1}{n}\right)^{\sqrt{n}}$ tiene límite $1$ y no $e$?
> Porque se puede escribir $\left[\left(1 + \frac{1}{n}\right)^n\right]^{1/\sqrt{n}} \to e^0 = 1$: el exponente efectivo $c_n = \frac{1}{\sqrt{n}}$ tiende a $0$.

> [!question]- ¿Cuál es la idea del paso "$a_n \to \infty$" en la definición ampliada?
> Que $\left(1 + \frac{1}{k}\right)^k \to e$ cuando $k \to \infty$ por cualquier camino; si $a_n$ tiende a infinito, los valores $\left(1 + \frac{1}{a_n}\right)^{a_n}$ tienden al mismo $e$.

> [!question]- Calcule $\lim\left(\frac{n}{n + 1}\right)^n$.
> $\left(1 - \frac{1}{n + 1}\right)^n \to e^{-1}$: es el inverso de $\left(\frac{n + 1}{n}\right)^n \to e$.
