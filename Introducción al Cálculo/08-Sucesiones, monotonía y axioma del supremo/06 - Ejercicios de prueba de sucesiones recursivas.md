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

# Ejercicios de prueba de sucesiones recursivas

Preguntas de las interrogaciones 6 a 8 de 2023 a 2026 sobre sucesiones definidas por recurrencia: demostrar por **inducción** una cota y la monotonía. El límite se pide muchas veces en la misma pregunta y se resuelve con el teorema de la sucesión monótona y la ecuación del punto fijo (tema de cálculo de límites); aquí se resuelven las dos primeras partes, que son las que se prueban por inducción.

## Ejercicios

### 1. Cota y crecimiento con una raíz (I8, 2026-1)
Sea $s_1 = 1$, $s_{n+1} = \sqrt{\dfrac{9 + s_n^2}{2}}$. (a) Demuestre que $\{s_n\}$ es acotada superiormente. (b) Demuestre que es creciente.

> [!example]- Solución
> (a) Se prueba $s_n \le 3$ por inducción. Caso base: $s_1 = 1 \le 3$. Paso: si $s_n \le 3$, entonces $s_{n+1} = \sqrt{\tfrac{9 + s_n^2}{2}} \le \sqrt{\tfrac{9 + 9}{2}} = 3$.
> (b) Se prueba $s_{n+1} \ge s_n$ por inducción. Caso base: $s_2 = \sqrt{5} \ge 1 = s_1$. Paso: si $s_{n+1} \ge s_n$, como $s_k \ge 0$ resulta $s_{n+1}^2 \ge s_n^2$, luego $\tfrac{9 + s_{n+1}^2}{2} \ge \tfrac{9 + s_n^2}{2}$ y, al tomar raíz, $s_{n+2} \ge s_{n+1}$.
> Como es creciente y acotada por $3$, converge, y su límite cumple $L = \sqrt{\tfrac{9 + L^2}{2}}$, o sea $L^2 = 9$, $L = 3$.

### 2. Una cota que se verifica con una raíz (I8, 2023-1)
Sea $s_1 = 1$, $s_{n+1} = \sqrt{72 + s_n}$. (a) Demuestre por inducción que $s_n < 9$. (b) Pruebe que $s_{n+1} - s_n > 0$.

> [!example]- Solución
> (a) $s_1 = 1 < 9$. Si $s_n < 9$, entonces $72 + s_n < 81$ y $s_{n+1} = \sqrt{72 + s_n} < 9$.
> (b) Racionalizando, $s_{n+1} - s_n = \sqrt{72 + s_n} - s_n = \dfrac{72 + s_n - s_n^2}{\sqrt{72 + s_n} + s_n} = \dfrac{(9 - s_n)(8 + s_n)}{\sqrt{72 + s_n} + s_n} > 0$, porque $0 < s_n < 9$. La sucesión es estrictamente creciente y acotada por $9$: converge, con $L^2 = 72 + L$, o sea $L = 9$ (la raíz $L = -8$ se descarta porque $s_n > 0$).

### 3. Una recurrencia con un cociente (I7, 2025-1)
Sea $a_1 = 1$, $a_{n+1} = 3 - \dfrac{1}{a_n}$. (a) Demuestre por inducción que es monótona creciente. (b) Demuestre que $a_n \le 3$.

> [!example]- Solución
> (a) $a_1 = 1 < 2 = a_2$. Si $a_n < a_{n+1}$ (ambos positivos), $\tfrac{1}{a_{n+1}} < \tfrac{1}{a_n}$, luego $-\tfrac{1}{a_n} < -\tfrac{1}{a_{n+1}}$ y sumando $3$: $a_{n+1} < a_{n+2}$.
> (b) $a_1 \le 3$. Si $a_n \le 3$, entonces $\tfrac{1}{a_n} \ge \tfrac{1}{3}$ y $a_{n+1} = 3 - \tfrac{1}{a_n} \le 3 - \tfrac{1}{3} \le 3$.
> Es creciente y acotada: converge a $L$ con $L = 3 - \tfrac{1}{L}$, o sea $L^2 - 3L + 1 = 0$ y, como $L \ge 1$, $L = \dfrac{3 + \sqrt{5}}{2}$.

### 4. Decreciente y acotada inferiormente (I8, 2024-1)
Sea $a_1 = \tfrac{5}{3}$, $a_{n+1} = (a_n - 1)^2 + 1$. Demuestre que es acotada inferiormente y decreciente.

> [!example]- Solución
> **Cota:** $a_{n+1} = (a_n - 1)^2 + 1 \ge 1$ para todo $n$, y $a_1 = \tfrac{5}{3} \ge 1$. **Monotonía** por inducción: $a_2 = \left(\tfrac{2}{3}\right)^2 + 1 = \tfrac{13}{9} \le \tfrac{15}{9} = a_1$. Si $a_{k+1} \le a_k$, con $a_{k+1} \ge 1$ queda $0 \le a_{k+1} - 1 \le a_k - 1$, se eleva al cuadrado (ambos no negativos) y se suma $1$: $a_{k+2} \le a_{k+1}$.
> Converge, y $L = (L - 1)^2 + 1$ da $L^2 - 3L + 2 = 0$, es decir $L = 1$ ó $L = 2$. Como $a_1 < 2$ y la sucesión decrece, $L = 1$.
> **Otra vía:** por inducción $a_n = \left(\tfrac{2}{3}\right)^{2^{n-1}} + 1$, y como $\left(\tfrac{2}{3}\right)^{2^{n-1}}$ es una subsucesión de la geométrica de razón $\tfrac{2}{3}$, tiende a $0$: $L = 1$.

### 5. Los números de Fibonacci (I6, 2024-1)
Sea $F_1 = F_2 = 1$, $F_n = F_{n-1} + F_{n-2}$ para $n \ge 3$. Demuestre que (a) $\tfrac{F_n}{F_{n-1}} \le 2$ para $n \ge 2$ y (b) $\tfrac{3}{2} \le \tfrac{F_n}{F_{n-1}}$ para $n \ge 3$.

> [!example]- Solución
> Todos los términos son positivos (suma de positivos) y la sucesión es no decreciente: $F_n = F_{n-1} + F_{n-2} \ge F_{n-1}$.
> (a) Para $n = 2$ el cociente vale $1 \le 2$. Para $n \ge 3$: $\tfrac{F_n}{F_{n-1}} = 1 + \tfrac{F_{n-2}}{F_{n-1}} \le 1 + 1 = 2$, porque $F_{n-2} \le F_{n-1}$.
> (b) Para $n \ge 3$, (a) aplicada a $n - 1$ da $\tfrac{F_{n-1}}{F_{n-2}} \le 2$, es decir $\tfrac{F_{n-2}}{F_{n-1}} \ge \tfrac{1}{2}$. Entonces $\tfrac{F_n}{F_{n-1}} = 1 + \tfrac{F_{n-2}}{F_{n-1}} \ge 1 + \tfrac{1}{2} = \tfrac{3}{2}$.

## Preguntas de repaso

> [!question]- ¿Por qué se descarta una de las dos raíces de la ecuación del punto fijo?
> Porque el límite hereda las propiedades de la sucesión: en el ejercicio 2 los términos son positivos, así que $L \ge 0$ y $L = -8$ no puede ser; en el ejercicio 4 la sucesión decrece desde $\frac{5}{3}$, por lo que $L \le \frac{5}{3} < 2$.

> [!question]- ¿Qué hace falta en la inducción del ejercicio 1(b) para pasar de $s_{n+1} \ge s_n$ a la raíz?
> Que todos los términos sean no negativos, para poder elevar al cuadrado y tomar raíz sin perder el orden.

> [!question]- ¿Cómo se elige entre probar primero la cota o primero la monotonía?
> Se prueba primero lo que no depende de lo otro: normalmente la cota por inducción, que se usa después para decidir el signo de $a_{n+1} - a_n$.
