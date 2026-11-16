---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades del valor absoluto y desigualdad triangular]]"
  - "[[05 - Raíces cuadradas y valor absoluto]]"
---

# Ejercicios de la guía de valor absoluto y raíces

Los cuatro ejercicios de la Guía 2. Son demostraciones: cada una se apoya en $|t|^2 = t^2$, en la desigualdad triangular o en la definición por casos.

## Ejercicios

### 1. El valor absoluto de un producto
Demuestre que $|xy| = |x|\,|y|$ para todo $x, y \in \mathbb{R}$.

> [!example]- Solución
> Ambos lados son $\ge 0$ y sus cuadrados coinciden: $|xy|^2 = (xy)^2 = x^2y^2 = |x|^2|y|^2 = (|x||y|)^2$. Dos números no negativos con el mismo cuadrado son iguales, así que $|xy| = |x||y|$.
> (También se puede separar en los cuatro casos de signo de $x$ e $y$.)

### 2. Cadena de desigualdades
Demuestre que $|x| - |y| \le \big||x| - |y|\big| \le |x - y|$.

> [!example]- Solución
> La primera desigualdad es $t \le |t|$ aplicada a $t = |x| - |y|$. La segunda es la desigualdad triangular inversa: de $|x| = |(x - y) + y| \le |x - y| + |y|$ sale $|x| - |y| \le |x - y|$, y de $|y| \le |y - x| + |x|$ sale $|y| - |x| \le |x - y|$; ambas juntas dan $\big||x| - |y|\big| \le |x - y|$.

### 3. Triangular con tres puntos
Demuestre que $|x - z| \le |x - y| + |y - z|$.

> [!example]- Solución
> Se escribe $x - z = (x - y) + (y - z)$ y se aplica la desigualdad triangular con los sumandos $x - y$ e $y - z$: $|x - z| \le |x - y| + |y - z|$. Es la desigualdad triangular de la distancia $d(x, z) \le d(x, y) + d(y, z)$.

### 4. Valor absoluto de un cuadrado
Demuestre que $|x^2| = |x|^2$.

> [!example]- Solución
> Como $x^2 \ge 0$ para todo real, $|x^2| = x^2$. Por otro lado, $|x|^2 = x^2$. Luego $|x^2| = |x|^2$.

## Preguntas de repaso

> [!question]- ¿Por qué basta comparar cuadrados para probar $|xy| = |x||y|$?
> Porque ambos lados son no negativos, y dos números no negativos son iguales cuando sus cuadrados lo son (la raíz cuadrada es una función de $\mathbb{R}_{\ge 0}$).

> [!question]- ¿Qué truco convierte $|x - z|$ en algo a lo que aplicar la triangular?
> Sumar y restar $y$: $x - z = (x - y) + (y - z)$.

> [!question]- ¿Qué relación hay entre el ejercicio 3 y la distancia?
> Es la cuarta propiedad de la distancia: ir de $x$ a $z$ directamente no es más largo que pasar por $y$.
