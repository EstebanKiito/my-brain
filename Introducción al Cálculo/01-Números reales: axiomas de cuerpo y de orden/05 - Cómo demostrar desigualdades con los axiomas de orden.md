---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - origen/complemento
prerrequisitos:
  - "[[03 - Axiomas de orden y números positivos]]"
  - "[[04 - Cuadrados, inversos y signos del producto]]"
---

# Cómo demostrar desigualdades con los axiomas de orden

Las interrogaciones piden una y otra vez "demuestre que ..." una desigualdad, y exigen justificar cada paso con los axiomas. Casi todas se resuelven con un mismo método: pasar todo a un lado, factorizar o completar cuadrados hasta ver una expresión de signo conocido, y concluir con la cerradura de $\mathbb{R}^+$.

## El método

> [!tip] Receta
> Para probar $A \le B$ (o $A < B$):
> 1. Estudiar $B - A$ y simplificar: expandir, agrupar, factorizar.
> 2. Reescribirlo como suma o producto de términos de signo conocido: cuadrados ($\ge 0$) y números positivos por hipótesis.
> 3. Concluir con "suma y producto de positivos son positivos" o con $a^2 \ge 0$.

Hay dos formas de presentarlo: partir de la desigualdad pedida y encadenar **equivalencias** hasta llegar a una verdad evidente, o partir de la verdad evidente y llegar a la desigualdad. Lo primero es válido solo si cada flecha es $\iff$; si alguna es solo $\Rightarrow$, se está probando al revés de lo debido.

## Ejemplo 1: un cuadrado oculto

Probar que $x + \dfrac{1}{x} \ge 2$ para $x > 0$. Se calcula
$$x + \frac{1}{x} - 2 = \frac{x^2 - 2x + 1}{x} = \frac{(x - 1)^2}{x} = (x - 1)^2\, x^{-1}.$$
Es un cuadrado ($\ge 0$) por un positivo ($x^{-1} > 0$), así que es $\ge 0$. La igualdad ocurre solo si $x = 1$. El mismo truco prueba $x + \tfrac{9}{x} \ge 6$, con diferencia $\tfrac{(x - 3)^2}{x}$.

## Ejemplo 2: tres variables

Si $a, b, c > 0$ no son todos iguales, entonces $(a + b + c)(bc + ca + ab) > 9abc$. Al expandir la diferencia con $9abc$ queda
$$(a + b + c)(bc + ca + ab) - 9abc = c(a - b)^2 + b(a - c)^2 + a(b - c)^2.$$
Cada término es un positivo por un cuadrado, así que la suma es $\ge 0$; y es **estrictamente** positiva porque al menos un par es distinto, lo que hace positivo al menos un cuadrado.

## Ejemplo 3: media aritmética y geométrica

Para $a, b > 0$ vale $\sqrt{ab} \le \dfrac{a + b}{2}$. Por contradicción, si $\tfrac{a+b}{2} < \sqrt{ab}$, ambos lados son positivos y elevar al cuadrado conserva el orden: $\tfrac{(a+b)^2}{4} < ab$. Eso equivale a $a^2 - 2ab + b^2 < 0$, es decir $(a - b)^2 < 0$, absurdo por el teorema de los cuadrados. Sin raíces, la forma útil es $(a + b)^2 \ge 4ab$.

## Ejemplo 4: separar en casos con la tricotomía

Probar que $n^2 \ge n$ para $n \in \mathbb{N}$. Si $n = 1$, $1^2 = 1 \ge 1$. Si $n \neq 1$, entonces $n > 1$, luego $n - 1 > 0$ y $n > 0$; por cerradura $(n - 1)n > 0$, es decir $n^2 > n$. Los dos casos dan $n^2 \ge n$.

> [!warning] Cuando falta el signo
> Cuando una hipótesis no fija el signo (por ejemplo, "$a < b$" sin $a > 0$), no se puede multiplicar a ciegas. Se separa con la tricotomía en $a > 0$, $a = 0$ y $a < 0$, o se busca una factorización cuyo signo sí sea conocido.

> [!tip] Idea para reconocer el cuadrado
> Una diferencia que parece "no tener signo" muchas veces es $(\text{algo})^2 + (\text{algo})^2$ o un cuadrado por un positivo. Probar con $(x - y)^2 \ge 0$, que expandido es $x^2 + y^2 \ge 2xy$, resuelve desigualdades como $a^2 + b^2 + c^2 \ge ab + bc + ca$ (sumando la desigualdad para cada par).

## Preguntas de repaso

> [!question]- ¿Qué se gana pasando todo a un lado y estudiando $B - A$?
> Convierte un problema de comparación en un problema de signo: basta factorizar la diferencia hasta ver que es producto o suma de términos positivos o cuadrados.

> [!question]- ¿Cómo se sabe que la desigualdad $(a + b + c)(bc + ca + ab) > 9abc$ es estricta si no todos son iguales?
> Si al menos dos de los números difieren, uno de los cuadrados $(a-b)^2$, $(a-c)^2$ o $(b-c)^2$ es positivo, y multiplicado por su coeficiente positivo ($c$, $b$ o $a$) da un término positivo. La suma de términos no negativos con alguno positivo es positiva.

> [!question]- ¿Por qué en la demostración por contradicción de la media aritmética-geométrica se puede elevar al cuadrado?
> Porque ambos lados son positivos ($a + b > 0$ y $\sqrt{ab} > 0$) y entre positivos elevar al cuadrado conserva el orden.

> [!question]- ¿Cuándo vale la igualdad en $x + 1/x \ge 2$?
> Solo si $(x - 1)^2 x^{-1} = 0$. Como $x^{-1} > 0$, esto exige $(x - 1)^2 = 0$, o sea $x = 1$.
