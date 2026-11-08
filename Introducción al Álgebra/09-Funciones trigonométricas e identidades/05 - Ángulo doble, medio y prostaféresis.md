---
ramo: "Introducción al Álgebra"
tema: "Funciones trigonométricas e identidades"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[04 - Identidades de suma y resta]]"
---

# Ángulo doble, medio y prostaféresis

De las fórmulas de suma salen tres familias más: el **ángulo doble**, el **argumento medio** y las de **prostaféresis** (que convierten sumas en productos). Son las herramientas para simplificar y para demostrar identidades.

## Ángulo doble

Poniendo $\alpha = \beta$ en las fórmulas de suma:

$$
\sin(2\alpha) = 2\sin\alpha\cos\alpha, \qquad
\cos(2\alpha) = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha, \qquad
\tan(2\alpha) = \frac{2\tan\alpha}{1 - \tan^2\alpha}.
$$

## Argumento medio

Despejando de $\cos(2\alpha) = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1$:

$$
\sin\!\left(\tfrac\alpha2\right) = \pm\sqrt{\tfrac{1 - \cos\alpha}{2}}, \qquad
\cos\!\left(\tfrac\alpha2\right) = \pm\sqrt{\tfrac{1 + \cos\alpha}{2}}.
$$

El signo se elige según el cuadrante de $\alpha/2$.

## Prostaféresis (suma a producto)

$$
\sin\alpha + \sin\beta = 2\sin\!\left(\tfrac{\alpha+\beta}{2}\right)\cos\!\left(\tfrac{\alpha-\beta}{2}\right),
$$

$$
\sin\alpha - \sin\beta = 2\cos\!\left(\tfrac{\alpha+\beta}{2}\right)\sin\!\left(\tfrac{\alpha-\beta}{2}\right),
$$

$$
\cos\alpha + \cos\beta = 2\cos\!\left(\tfrac{\alpha+\beta}{2}\right)\cos\!\left(\tfrac{\alpha-\beta}{2}\right),
$$

$$
\cos\alpha - \cos\beta = -2\sin\!\left(\tfrac{\alpha+\beta}{2}\right)\sin\!\left(\tfrac{\alpha-\beta}{2}\right).
$$

> [!tip] Para qué sirven
> El ángulo doble y el medio reducen un argumento a la mitad; las de prostaféresis convierten una **suma** de senos/cosenos en un **producto**, que es la forma que permite cancelar factores y demostrar identidades.

**De dónde salen.** Sumando y restando las fórmulas de $\sin(x \pm y)$ y $\cos(x \pm y)$ se cancelan términos y quedan las fórmulas de **producto a suma**:
$$\cos x\cos y = \tfrac{1}{2}[\cos(x+y) + \cos(x-y)], \qquad \sin y\cos x = \tfrac{1}{2}[\sin(x+y) - \sin(x-y)],$$
$$\sin x\sin y = \tfrac{1}{2}[\cos(x-y) - \cos(x+y)].$$
Con el cambio $x = \frac{\alpha+\beta}{2}$, $y = \frac{\alpha-\beta}{2}$ (de modo que $x + y = \alpha$ y $x - y = \beta$) se obtienen las de prostaféresis. Las pruebas piden a veces demostrar una de ellas antes de usarla, y este es el camino corto.

## Cómo demostrar una identidad

1. Partir del lado **más complicado** y llegar al otro; no trabajar con los dos a la vez "pasando términos", porque eso supone lo que se quiere probar.
2. Si hay secantes, cosecantes, tangentes o cotangentes, escribirlas en senos y cosenos, o usar $\sec^2 = 1 + \tan^2$ y $\csc^2 = 1 + \cot^2$ si el otro lado las tiene.
3. Si hay ángulos distintos ($3x$, $2x$, $x$), llevarlos todos al mismo con suma de ángulos o ángulo doble.
4. Buscar $\sin^2 + \cos^2 = 1$ escondido después de expandir.

**Ejemplo.** $\sin 3x = \sin(2x + x) = \sin 2x\cos x + \cos 2x\sin x = 2\sin x\cos^2 x + (\cos^2 x - \sin^2 x)\sin x = 3\sin x\cos^2 x - \sin^3 x$.

## Fórmulas de reducción

Estas trasladan un ángulo al complementario ($\pi/2 - t$):

$$
\sin t = \cos\!\left(\tfrac{\pi}{2} - t\right), \qquad \cos t = \sin\!\left(\tfrac{\pi}{2} - t\right), \qquad \tan t = \cot\!\left(\tfrac{\pi}{2} - t\right).
$$

> [!warning] El signo del argumento medio
> Las fórmulas de ángulo medio llevan un $\pm$ que se decide con el cuadrante. Olvidarlo da un valor que puede tener el signo incorrecto.

## Preguntas de repaso

> [!question]- Escriba $\cos(2\alpha)$ de dos formas.
> $\cos^2\alpha - \sin^2\alpha$ y $1 - 2\sin^2\alpha$ (también $2\cos^2\alpha - 1$). Son la misma por la identidad fundamental.

> [!question]- ¿Qué hace la prostaféresis y por qué es útil?
> Convierte una suma (o resta) de senos/cosenos en un producto. El producto permite cancelar términos y simplificar, que es lo que piden las demostraciones de identidades.

> [!question]- ¿Cómo se elige el signo en $\sin(\alpha/2)$?
> Según el cuadrante en el que esté el ángulo $\alpha/2$: si su seno es positivo ahí, se toma $+$; si es negativo, $-$.

> [!question]- Simplifique $\sin(2\alpha)$ cuando $\sin\alpha = \tfrac35$ y $\cos\alpha = \tfrac45$.
> $\sin(2\alpha) = 2\sin\alpha\cos\alpha = 2\cdot\tfrac35\cdot\tfrac45 = \tfrac{24}{25}$.
