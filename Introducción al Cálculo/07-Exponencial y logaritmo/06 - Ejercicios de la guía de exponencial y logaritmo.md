---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Ecuaciones exponenciales y logarítmicas]]"
---

# Ejercicios de la guía de exponencial y logaritmo

Los siete ejercicios de la Guía 8: un gráfico, un dominio, una composición, expandir, combinar y dos ecuaciones.

## Ejercicios

### 1. Gráfico
Grafique $f(x) = 2^x - 5$.

> [!example]- Solución
> Es $2^x$ trasladada $5$ unidades hacia abajo. Asíntota horizontal $y = -5$; corte con el eje $y$ en $(0, -4)$; corte con el eje $x$ en $x = \log_2 5 \approx 2{,}32$; estrictamente creciente con recorrido $(-5, \infty)$.

### 2. Dominio
Determine el dominio de $f(x) = \ln(4 - x^2)$.

> [!example]- Solución
> $4 - x^2 > 0 \iff x^2 < 4 \iff -2 < x < 2$. $\operatorname{Dom}(f) = (-2, 2)$.

### 3. Composición
Sean $f(x) = 2^x$ y $g(x) = x^2 + 1$. Determine $f \circ g$.

> [!example]- Solución
> $(f \circ g)(x) = f(x^2 + 1) = 2^{x^2 + 1}$, con dominio $\mathbb{R}$.

### 4. Expandir
Expanda (a) $\log_5\sqrt{\dfrac{x - 1}{x + 1}}$, (b) $\log\sqrt{x\sqrt{y\sqrt{z}}}$ y (c) $\ln\!\left(\dfrac{x^2\sqrt{x^2 - 1}}{3x + 4}\right)$.

> [!example]- Solución
> (a) $\tfrac{1}{2}\big[\log_5(x - 1) - \log_5(x + 1)\big]$.
> (b) De afuera hacia adentro: $\tfrac{1}{2}\log\!\big(x\sqrt{y\sqrt{z}}\big) = \tfrac{1}{2}\log x + \tfrac{1}{4}\log y + \tfrac{1}{8}\log z$.
> (c) $2\ln x + \tfrac{1}{2}\ln(x^2 - 1) - \ln(3x + 4) = 2\ln x + \tfrac{1}{2}\ln(x - 1) + \tfrac{1}{2}\ln(x + 1) - \ln(3x + 4)$.

### 5. Combinar
Combine en un solo logaritmo: (a) $4\log x - \tfrac{1}{3}\log(x^2 + 1) + 2\log(x - 1)$; (b) $\ln 5 + 2\ln x + 3\ln(x^2 + 5)$; (c) $\log_a b + c\log_a d - r\log_a s$.

> [!example]- Solución
> (a) $\log\!\left(\dfrac{x^4(x - 1)^2}{\sqrt[3]{x^2 + 1}}\right)$.
> (b) $\ln\!\big(5x^2(x^2 + 5)^3\big)$.
> (c) $\log_a\!\left(\dfrac{b\,d^c}{s^r}\right)$.

### 6. Ecuación con $2^x$
Resuelva $x^2 2^x - 2^x = 0$.

> [!example]- Solución
> Se factoriza $2^x(x^2 - 1) = 0$. Como $2^x > 0$, queda $x^2 = 1$: $x = 1$ ó $x = -1$.

### 7. Ecuación con $e^x$
Resuelva $x^2 e^x + x e^x - e^x = 0$.

> [!example]- Solución
> $e^x(x^2 + x - 1) = 0$ y $e^x > 0$, luego $x^2 + x - 1 = 0$: $x = \dfrac{-1 \pm \sqrt{5}}{2}$.

## Preguntas de repaso

> [!question]- ¿Por qué se puede dividir por $2^x$ en el ejercicio 6?
> Porque $2^x > 0$ para todo $x$; nunca se anula y por eso no se pierden soluciones.

> [!question]- ¿Qué condición debe tener $x$ en el ejercicio 5(a) para que la expresión original exista?
> $x > 0$ y $x - 1 > 0$ (y $x^2 + 1 > 0$ siempre), es decir $x > 1$.

> [!question]- ¿Cómo se expande $\log\sqrt{x\sqrt{y\sqrt{z}}}$?
> Aplicando la raíz como potencia $\frac{1}{2}$ capa por capa: $\frac{1}{2}\log x + \frac{1}{4}\log y + \frac{1}{8}\log z$.
