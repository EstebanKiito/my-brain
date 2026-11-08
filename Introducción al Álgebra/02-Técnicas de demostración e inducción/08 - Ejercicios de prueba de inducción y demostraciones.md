---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Plantilla de inducción y cambio de caso base]]"
  - "[[06 - Contrarrecíproca y contradicción en la práctica]]"
---

# Ejercicios de prueba de inducción y demostraciones

Preguntas de interrogaciones y exámenes anteriores. La inducción aparece en casi todas las pruebas del curso, casi siempre en una de tres formas: divisibilidad, una suma con fórmula cerrada o una desigualdad. Las pautas reparten el puntaje entre **caso base**, **hipótesis de inducción escrita explícitamente**, **paso inductivo** y **conclusión**, así que conviene escribir las cuatro partes aunque parezcan obvias.

## Ejercicios

### 1. Recurrencia con fórmula cerrada
Sea $a_0 = 4$ y $a_{n+1} = 2a_n + 1$ para $n \ge 0$. Pruebe que $a_n = 5 \cdot 2^n - 1$ para todo $n \ge 0$.

> [!example]- Solución
> **Caso base** ($n = 0$): $a_0 = 4$ y $5 \cdot 2^0 - 1 = 4$.
> **HI:** para un $k \ge 0$, $a_k = 5 \cdot 2^k - 1$.
> **Paso:** $a_{k+1} = 2a_k + 1 = 2(5 \cdot 2^k - 1) + 1 = 5 \cdot 2^{k+1} - 2 + 1 = 5 \cdot 2^{k+1} - 1$.
> **Conclusión:** por inducción (desde $n_0 = 0$), la fórmula vale para todo $n \ge 0$.

### 2. Divisibilidad separando el coeficiente
Demuestre que $4^{n+1} + 5^{2n-1}$ es divisible por $21$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base:** $4^2 + 5^1 = 21$.
> **HI:** $4^{k+1} + 5^{2k-1} = 21c$ para algún entero $c$.
> **Paso:** el término siguiente multiplica la primera potencia por $4$ y la segunda por $25$. Se separa $25 = 4 + 21$:
> $$4^{k+2} + 5^{2k+1} = 4 \cdot 4^{k+1} + 25 \cdot 5^{2k-1} = 4\left(4^{k+1} + 5^{2k-1}\right) + 21 \cdot 5^{2k-1} = 21\left(4c + 5^{2k-1}\right).$$
> **Conclusión:** es divisible por $21$ para todo $n$.
>
> La misma maniobra resuelve "$2^{n+1} + 3^{2n-1}$ es divisible por $7$" ($9 = 2 + 7$) y "$6^n - 1$ es divisible por $5$" ($6 = 1 + 5$).

### 3. Divisibilidad de un polinomio
Demuestre que $4n^3 + 5n$ es divisible por $3$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base:** $4 + 5 = 9 = 3 \cdot 3$.
> **HI:** $4k^3 + 5k = 3m$ para algún entero $m$.
> **Paso:** se expande y se agrupa la expresión en $k$:
> $$4(k+1)^3 + 5(k+1) = (4k^3 + 5k) + 12k^2 + 12k + 9 = 3m + 3(4k^2 + 4k + 3) = 3(m + 4k^2 + 4k + 3).$$
> **Conclusión:** es divisible por $3$ para todo $n$.

### 4. Una suma con fórmula cerrada
Demuestre que para todo $n \in \mathbb{N}$:
$$\frac{1}{1\cdot 2\cdot 3} + \frac{1}{2\cdot 3\cdot 4} + \dots + \frac{1}{n(n+1)(n+2)} = \frac{n(n+3)}{4(n+1)(n+2)}.$$

> [!example]- Solución
> **Caso base:** a la izquierda $\frac{1}{6}$; a la derecha $\frac{1 \cdot 4}{4 \cdot 2 \cdot 3} = \frac{1}{6}$.
> **HI:** la suma hasta $k$ vale $\frac{k(k+3)}{4(k+1)(k+2)}$.
> **Paso:** la suma hasta $k+1$ es la de $k$ más el término $\frac{1}{(k+1)(k+2)(k+3)}$:
> $$\frac{k(k+3)}{4(k+1)(k+2)} + \frac{1}{(k+1)(k+2)(k+3)} = \frac{k(k+3)^2 + 4}{4(k+1)(k+2)(k+3)} = \frac{(k+1)^2(k+4)}{4(k+1)(k+2)(k+3)} = \frac{(k+1)(k+4)}{4(k+2)(k+3)},$$
> que es la fórmula con $n = k+1$. La factorización $k^3 + 6k^2 + 9k + 4 = (k+1)^2(k+4)$ sale probando $k = -1$ como raíz.
> **Conclusión:** vale para todo $n \in \mathbb{N}$.

### 5. Una desigualdad que necesita cuidado en $k = 1$
Demuestre que $3^n > 2n^2$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base:** $3 > 2$.
> **HI:** $3^k > 2k^2$.
> **Paso:** $3^{k+1} = 3 \cdot 3^k > 6k^2$. Falta $6k^2 \ge 2(k+1)^2 = 2k^2 + 4k + 2$. Para $k \ge 2$: $6k^2 = 2k^2 + 4k^2 \ge 2k^2 + 8k > 2k^2 + 4k + 2$. Para $k = 1$ la cadena falla ($6 < 8$), así que ese paso se verifica a mano: $3^2 = 9 > 8 = 2 \cdot 2^2$.
> **Conclusión:** con el paso de $1$ a $2$ hecho aparte y el paso general para $k \ge 2$, vale para todo $n$.

### 6. Escribir $P(k)$ y $P(k+1)$
Sea $P(n)$: $1 + \frac{1}{\sqrt 2} + \frac{1}{\sqrt 3} + \dots + \frac{1}{\sqrt n} > \sqrt n$. (a) Muestre que $P(2)$ es verdadera. (b) Escriba $P(k)$ y $P(k+1)$. (c) Si $P(2)$ y $P(k) \Rightarrow P(k+1)$ son verdaderas, ¿qué se concluye?

> [!example]- Solución
> (a) Como $\sqrt 2 > 1$, se tiene $1 > \frac{1}{\sqrt 2} = \frac{\sqrt 2}{2}$, así que $1 + \frac{1}{\sqrt 2} > \frac{\sqrt 2}{2} + \frac{\sqrt 2}{2} = \sqrt 2$.
> (b) $P(k)$: $1 + \frac{1}{\sqrt 2} + \dots + \frac{1}{\sqrt k} > \sqrt k$. $P(k+1)$: $1 + \frac{1}{\sqrt 2} + \dots + \frac{1}{\sqrt k} + \frac{1}{\sqrt{k+1}} > \sqrt{k+1}$.
> (c) Que $P(n)$ es verdadera para todo natural $n \ge 2$ (no para $n = 1$, donde hay igualdad).
>
> El paso inductivo, aunque no se pedía: por HI basta $\sqrt k + \frac{1}{\sqrt{k+1}} > \sqrt{k+1}$; multiplicando por $\sqrt{k+1}$ queda $\sqrt{k(k+1)} + 1 > k + 1$, es decir, $\sqrt{k(k+1)} > k$, cierto porque $k(k+1) > k^2$.

### 7. Contrarrecíproca con una disyunción
Pruebe que si $a \in \mathbb{R}$ cumple $a^2 \ge 3a$, entonces $a \le 0$ o $a \ge 3$.

> [!example]- Solución
> Por contrarrecíproca: suponer $0 < a < 3$ y probar $a^2 < 3a$. Como $a > 0$, multiplicar $a < 3$ por $a$ conserva el sentido y da $a^2 < 3a$. Las pautas dan puntaje a declarar la técnica, a decir que $a > 0$ al multiplicar y a concluir.

### 8. Irracionales
Sean $a, b \in \mathbb{R}$. (a) Si $a \in \mathbb{Q}$ y $b \notin \mathbb{Q}$, demuestre que $a + b \notin \mathbb{Q}$. (b) Si $a + b \notin \mathbb{Q}$, demuestre que $a \notin \mathbb{Q}$ o $b \notin \mathbb{Q}$.

> [!example]- Solución
> (a) Por contradicción: si $a + b = \frac{m}{n}$ y $a = \frac{p}{q}$, entonces $b = \frac{mq - np}{nq} \in \mathbb{Q}$, contra la hipótesis.
> (b) Por contrarrecíproca: la negación de "$a \notin \mathbb{Q}$ o $b \notin \mathbb{Q}$" es, por De Morgan, "$a \in \mathbb{Q}$ y $b \in \mathbb{Q}$", y la suma de racionales es racional, así que $a + b \in \mathbb{Q}$.

## Preguntas de repaso

> [!question]- En una divisibilidad por inducción, ¿cómo se escribe la hipótesis para poder usarla?
> Como igualdad con un entero: "expresión en $k$ $= d \cdot c$". Así se puede sustituir dentro de la expresión en $k+1$; la frase "es divisible por $d$" por sí sola no se deja manipular.

> [!question]- En el ejercicio 5, ¿por qué no basta el caso base $n = 1$ y el paso general?
> Porque el paso general solo vale para $k \ge 2$; sin verificar el paso de $1$ a $2$ la cadena de dominós tiene un hueco.

> [!question]- ¿Qué técnica conviene para probar "$p \Rightarrow (q_1 \vee q_2)$"?
> La contrarrecíproca: $\neg(q_1 \vee q_2) \equiv \neg q_1 \wedge \neg q_2$ entrega dos condiciones para usar a la vez.
