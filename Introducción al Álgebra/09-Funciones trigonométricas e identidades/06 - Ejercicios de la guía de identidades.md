---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Identidades de suma y resta]]"
  - "[[05 - Ángulo doble, medio y prostaféresis]]"
---

# Ejercicios de la guía de identidades

Preguntas de la guía sobre valores exactos, fórmulas de suma, ángulo doble y prostaféresis. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Valores exactos
Calcule $\cos(15\pi/6)$, $\sin(-\pi/12)$ y $\tan(125\pi/12)$.

> [!example]- Solución
> - $\cos(15\pi/6) = \cos(5\pi/2) = \cos(2\pi + \pi/2) = \cos(\pi/2) = 0$.
> - $\sin(-\pi/12) = -\sin(\pi/12) = -\tfrac{\sqrt6 - \sqrt2}{4}$ (por imparidad y el valor de $\pi/12 = 15^\circ$).
> - $\tan(125\pi/12) = \tan(125\pi/12 - 10\pi) = \tan(5\pi/12) = 2 + \sqrt3$ (pues $\tan(5\pi/12) = \tan(45^\circ + 30^\circ)$).

### 2. Coseno del triple
Demuestre que $\cos(3\alpha) = 4\cos^3\alpha - 3\cos\alpha$.

> [!example]- Solución
> $\cos(3\alpha) = \cos(2\alpha + \alpha) = \cos2\alpha\cos\alpha - \sin2\alpha\sin\alpha = (2\cos^2\alpha - 1)\cos\alpha - (2\sin\alpha\cos\alpha)\sin\alpha = 2\cos^3\alpha - \cos\alpha - 2\sin^2\alpha\cos\alpha$. Con $\sin^2\alpha = 1 - \cos^2\alpha$: $2\cos^3\alpha - \cos\alpha - 2\cos\alpha + 2\cos^3\alpha = 4\cos^3\alpha - 3\cos\alpha$.

### 3. Producto de medio ángulo
Demuestre que $\sin(\alpha/2)\cos(\alpha/2) = \tfrac12\sin\alpha$.

> [!example]- Solución
> Es la fórmula del ángulo doble al revés: $\sin(2x) = 2\sin x\cos x$ con $x = \alpha/2$ da $\sin\alpha = 2\sin(\alpha/2)\cos(\alpha/2)$, de donde $\sin(\alpha/2)\cos(\alpha/2) = \tfrac12\sin\alpha$.

### 4. Cuadrado de una diferencia
Demuestre que $(\cos(\alpha/2) - \sin(\alpha/2))^2 = 1 - \sin\alpha$.

> [!example]- Solución
> Desarrollando: $\cos^2(\alpha/2) + \sin^2(\alpha/2) - 2\sin(\alpha/2)\cos(\alpha/2) = 1 - \sin\alpha$, usando la identidad fundamental y $\sin\alpha = 2\sin(\alpha/2)\cos(\alpha/2)$.

### 5. Prostaféresis
Verifique que $\dfrac{\sin\alpha - \sin\beta}{\cos\alpha + \cos\beta} = \tan\!\left(\dfrac{\alpha - \beta}{2}\right)$.

> [!example]- Solución
> Por prostaféresis, $\sin\alpha - \sin\beta = 2\cos\!\left(\tfrac{\alpha+\beta}{2}\right)\sin\!\left(\tfrac{\alpha-\beta}{2}\right)$ y $\cos\alpha + \cos\beta = 2\cos\!\left(\tfrac{\alpha+\beta}{2}\right)\cos\!\left(\tfrac{\alpha-\beta}{2}\right)$. El cociente es $\dfrac{\sin\!\left(\tfrac{\alpha-\beta}{2}\right)}{\cos\!\left(\tfrac{\alpha-\beta}{2}\right)} = \tan\!\left(\tfrac{\alpha-\beta}{2}\right)$.

## Preguntas de repaso

> [!question]- ¿Cómo se calcula un valor exacto como $\tan(5\pi/12)$?
> Escribiéndolo como suma de ángulos notables ($45^\circ + 30^\circ$) y aplicando la fórmula de la tangente de una suma.

> [!question]- ¿Qué técnica usa el ejercicio 5?
> Prostaféresis: convertir la diferencia de senos y la suma de cosenos en productos, que comparten un factor común que se cancela.

> [!question]- ¿Cómo se demuestra $\cos(3\alpha)$ sin conocer la fórmula?
> Escribiendo $3\alpha = 2\alpha + \alpha$ y aplicando la fórmula del coseno de una suma, junto con el ángulo doble y la identidad fundamental.
