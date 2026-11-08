---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/complejos
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Producto, potencias y raíces de complejos]]"
  - "[[04 - Ecuaciones trigonométricas]]"
---

# Ejercicios de la guía de complejos e inversas

Preguntas de la guía y de las clases sobre Moivre, raíces de complejos y ecuaciones trigonométricas. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Potencia por Moivre
Calcule $(1 + i)^{10}$.

> [!example]- Solución
> $1 + i = \sqrt2\operatorname{cis}(\pi/4)$, así que $(1+i)^{10} = (\sqrt2)^{10}\operatorname{cis}(10\pi/4) = 32\operatorname{cis}(5\pi/2) = 32\operatorname{cis}(\pi/2) = 32i$.

### 2. Raíces de una ecuación
Resuelva $z^3 + 27 = 0$.

> [!example]- Solución
> $z^3 = -27 = 27\operatorname{cis}(\pi)$. Las raíces son $z_k = 3\operatorname{cis}\!\left(\frac{\pi + 2k\pi}{3}\right)$ con $k = 0, 1, 2$: $3\operatorname{cis}(\pi/3) = \tfrac32 + \tfrac{3\sqrt3}{2}i$, $3\operatorname{cis}(\pi) = -3$ y $3\operatorname{cis}(5\pi/3) = \tfrac32 - \tfrac{3\sqrt3}{2}i$.

### 3. Raíces octavas de 16
Encuentre todas las soluciones complejas de $x^8 - 16 = 0$ en la forma $a + bi$.

> [!example]- Solución
> $x^8 = 16 = 16\operatorname{cis}(0)$. Las raíces octavas son $\sqrt2\operatorname{cis}(k\pi/4)$, $k = 0, \dots, 7$: $\sqrt2$, $1 + i$, $\sqrt2 i$, $-1 + i$, $-\sqrt2$, $-1 - i$, $-\sqrt2 i$, $1 - i$.

### 4. Ecuación con senos
Encuentre todos los $x \in [0, \pi]$ que satisfacen $\sin(3x) - \sin(5x) = 0$.

> [!example]- Solución
> $\sin3x = \sin5x$ da $5x = 3x + 2k\pi$ (o sea $x = k\pi$) o $5x = \pi - 3x + 2k\pi$ (o sea $x = (2k+1)\pi/8$). En $[0,\pi]$: $0$, $\pi$, $\pi/8$, $3\pi/8$, $5\pi/8$ y $7\pi/8$.

### 5. Ecuación con tangente
Resuelva $3\tan^2 x + 5 = \dfrac{7}{\cos x}$.

> [!example]- Solución
> Con $\tan^2 x = \frac{1}{\cos^2 x} - 1$: $3\left(\frac{1}{\cos^2 x} - 1\right) + 5 = \frac{7}{\cos x}$, o sea $\frac{3}{\cos^2 x} + 2 = \frac{7}{\cos x}$. Multiplicando por $\cos^2 x$: $2\cos^2 x - 7\cos x + 3 = 0$, de donde $\cos x = 1/2$ (la otra raíz $3$ es imposible). Soluciones: $x = \pm\pi/3 + 2k\pi$.

## Preguntas de repaso

> [!question]- ¿Qué teorema convierte una potencia compleja en un problema de ángulos?
> El teorema de Moivre: $(r\operatorname{cis}\theta)^n = r^n\operatorname{cis}(n\theta)$, que eleva el módulo y multiplica el ángulo.

> [!question]- En el ejercicio 4, ¿por qué hay dos familias de soluciones?
> Porque $\sin u = \sin v$ tiene dos ramas: $u = v + 2k\pi$ o $u = \pi - v + 2k\pi$ (ángulos con el mismo seno en la circunferencia unitaria).

> [!question]- ¿Cuántas raíces octavas tiene $16$ y cómo se distribuyen?
> Ocho, todas de módulo $\sqrt2$ y con ángulos separados $2\pi/8 = \pi/4$, formando un octógono regular centrado en el origen.
