---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[03 - Límites con el número e]]"
  - "[[02 - Límites infinitos]]"
---

# Cómo elegir la técnica para calcular un límite

Ante un límite de sucesión, lo difícil no es aplicar una técnica sino **reconocer** cuál corresponde. Esta nota las junta en una tabla de decisión, con los límites de los exámenes que mezclan raíces, factoriales, logaritmos y exponenciales.

## Tabla de decisión

| La expresión es... | Técnica | Ejemplo |
|---|---|---|
| Cociente de polinomios en $n$ | Dividir por la mayor potencia del denominador | $\dfrac{3n^3 + 2n^2 + n}{5n^3 + 8} \to \tfrac{3}{5}$ |
| Diferencia de raíces ($\infty - \infty$) | Multiplicar y dividir por el **conjugado** | $\sqrt{n^2 + 5n + 6} - n \to \tfrac{5}{2}$ |
| Cociente de exponenciales ($a^n$, $b^n$) | Dividir por la **base mayor** | $\dfrac{3^{n+1} + 2^{n+1}}{3^n + 2^n} \to 3$ |
| $(1 + \text{pequeño})^{\text{grande}}$ | Reconocer **$e$** | $\left(\tfrac{n + 2}{n + 1}\right)^{3n} \to e^3$ |
| Seno o coseno dividido por algo que crece | **Sándwich** con $\pm 1$ | $\tfrac{\cos(n^3 + 1)}{n} \to 0$ |
| Factoriales y potencias | **Cociente de términos consecutivos** o acotación | $\tfrac{n!}{n^n} \to 0$ |
| Logaritmo contra potencia | $\ln x \le x - 1$ y sándwich | $\tfrac{\ln n}{n} \to 0$ |
| Raíz $n$-ésima de una suma de potencias | Acotar por el **mayor término** | $\sqrt[n]{a^n + b^n + c^n} \to c$ |
| Algo que crece sin cota | Comparar con $\sqrt{n}$, $n$... (límites infinitos) | $\ln\tfrac{3n}{e^{2n}} \to -\infty$ |

## Ejemplos de exámenes

**Raíz anidada (Examen, 2025-1): $\lim\left(\sqrt{n + \sqrt{n}} - \sqrt{n - \sqrt{n}}\right)$.** Se multiplica por el conjugado:
$$\frac{(n + \sqrt{n}) - (n - \sqrt{n})}{\sqrt{n + \sqrt{n}} + \sqrt{n - \sqrt{n}}} = \frac{2\sqrt{n}}{\sqrt{n + \sqrt{n}} + \sqrt{n - \sqrt{n}}}.$$
Dividiendo numerador y denominador por $\sqrt{n}$: $\dfrac{2}{\sqrt{1 + 1/\sqrt{n}} + \sqrt{1 - 1/\sqrt{n}}} \to \dfrac{2}{1 + 1} = 1$.

**Con un coseno (Examen, 2025-1): $\lim\dfrac{3}{\sqrt{n}}\cos\!\left(\dfrac{n}{n!}\right)$.** Como $-1 \le \cos\!\left(\tfrac{n}{n!}\right) \le 1$, queda $-\tfrac{3}{\sqrt{n}} \le \tfrac{3}{\sqrt{n}}\cos\!\left(\tfrac{n}{n!}\right) \le \tfrac{3}{\sqrt{n}}$, y ambos extremos tienden a $0$. Por el sándwich, el límite es $0$.

**Con factoriales (I8, 2026-1): $\lim\dfrac{n! + 3^n}{(n + 1)!}$.** Se separa: $\dfrac{n!}{(n + 1)!} + \dfrac{3^n}{(n + 1)!} = \dfrac{1}{n + 1} + \dfrac{3^n}{(n + 1)!}$. El primero tiende a $0$. Para el segundo, $\tfrac{3^n}{(n + 1)!} \le \tfrac{3^{n+1}}{(n + 1)!} \to 0$ (porque $\tfrac{a^k}{k!} \to 0$). El límite es $0$.

**Con un conjugado y un cociente (Examen, 2026-1): $\lim\dfrac{\sqrt{n^2 - n + 1} - 2n}{n + 1}$.** Aquí **no** se necesita el conjugado para la diferencia (la raíz crece como $n$): se divide por $n$: $\dfrac{\sqrt{1 - 1/n + 1/n^2} - 2}{1 + 1/n} \to \dfrac{1 - 2}{1} = -1$. (La pauta racionaliza y llega al mismo valor.)

**Una raíz $n$-ésima (I10, 2020-1): $\lim\sqrt[n]{a^n + b^n + c^n}$ con $1 < a < b < c$.** Se acota: $c = \sqrt[n]{c^n} \le \sqrt[n]{a^n + b^n + c^n} \le \sqrt[n]{3c^n} = \sqrt[n]{3}\,c$, y como $\sqrt[n]{3} \to 1$, el sándwich da límite $c$.

**Un cociente de logaritmos (Examen, 2022-2): $\lim\dfrac{\ln(n + 1)}{\ln n}$.** $\dfrac{\ln(n + 1)}{\ln n} = 1 + \dfrac{\ln\!\left(\tfrac{n + 1}{n}\right)}{\ln n} = 1 + \dfrac{\ln(1 + 1/n)}{\ln n}$. El numerador tiende a $\ln 1 = 0$ y $\ln n \to +\infty$ (regla 4 de límites infinitos): el segundo término tiende a $0$ y el límite es $1$.

## Antes de empezar: ¿qué forma tiene?

1. **Sustituir** $n \to \infty$ mentalmente: ¿sale $\tfrac{\infty}{\infty}$, $\infty - \infty$, $1^\infty$, un factor acotado?
2. Si hay una **forma determinada**, aplicar el álgebra de límites o las reglas de infinitos.
3. Si es **indeterminada**, elegir la técnica de la tabla.
4. **Verificar** el resultado numéricamente con un $n$ grande ($n = 1000$) para detectar errores de álgebra.

> [!warning] Errores frecuentes
> - **Aplicar el álgebra de límites a formas indeterminadas** (restar dos infinitos, dividir dos infinitos).
> - **Olvidar justificar el sándwich**: hay que escribir ambas cotas y decir que sus límites coinciden.
> - **Usar $\infty$ como número** en una cuenta de cierre: se debe citar el teorema de límites infinitos, no operar con el símbolo.

## Preguntas de repaso

> [!question]- ¿Qué técnica sirve para $\frac{2^n + 5}{3^n - 1}$?
> Dividir por la base mayor ($3^n$): $\frac{(2/3)^n + 5/3^n}{1 - 1/3^n} \to 0$.

> [!question]- ¿Cómo se calcula $\lim\sqrt[n]{2^n + 5^n}$?
> Acotando por el mayor término: $5 \le \sqrt[n]{2^n + 5^n} \le \sqrt[n]{2}\cdot 5 \to 5$; el límite es $5$.

> [!question]- ¿Por qué la técnica del conjugado no hace falta en $\frac{\sqrt{n^2 - n + 1} - 2n}{n + 1}$?
> Porque la resta $\sqrt{n^2 - n + 1} - 2n$ no es indeterminada: la raíz crece como $n$ y $2n$ domina; dividiendo por $n$ el límite es directamente $-1$.

> [!question]- ¿Cuál es el primer paso ante un límite desconocido?
> Evaluar mentalmente la forma de la expresión (con $n$ muy grande) para saber si es determinada o indeterminada y cuál técnica corresponde.
