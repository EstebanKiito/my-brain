---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - origen/complemento
prerrequisitos: []
---

# Los números reales como cuerpo

El curso no construye los números reales: los **describe** mediante una lista corta de propiedades, los axiomas. Todo lo que se demuestra después (reglas de signos, cancelación, desigualdades) sale únicamente de esa lista, de modo que cada paso de una demostración puede justificarse citando un axioma o un teorema ya probado. Los axiomas de cuerpo recogen lo que se usa al manipular álgebra: sumar, restar, multiplicar y dividir.

## Los seis axiomas de cuerpo

Se supone que $\mathbb{R}$ tiene dos operaciones, suma $+$ y producto $\cdot$ (que se escribe $ab$), que cumplen:

| Axioma | Enunciado |
|---|---|
| **A0. Cierre** | Si $a, b \in \mathbb{R}$, entonces $a + b \in \mathbb{R}$ y $ab \in \mathbb{R}$ |
| **A1. Conmutatividad** | $a + b = b + a$ y $ab = ba$ |
| **A2. Asociatividad** | $(a + b) + c = a + (b + c)$ y $(ab)c = a(bc)$ |
| **A3. Neutros** | Existe un único $0$ con $a + 0 = a$ y un único $1$ con $a \cdot 1 = a$ |
| **A4. Distributividad** | $a(b + c) = ab + ac$ |
| **A5. Inversos** | Para todo $a$ existe $-a$ con $a + (-a) = 0$; si $a \neq 0$, existe $a^{-1}$ con $a \cdot a^{-1} = 1$ |

> [!tip] Qué se está usando realmente
> Cuando se "pasa restando" un término al otro lado o se factoriza, lo que se aplica son estos axiomas. Un conjunto con dos operaciones que los cumple se llama **cuerpo**; $\mathbb{Q}$ y $\mathbb{R}$ son cuerpos, $\mathbb{Z}$ no (el $2$ no tiene inverso multiplicativo en $\mathbb{Z}$).

## Resta y división

Las dos operaciones "que faltan" no son nuevas: se definen con los inversos del axioma A5.

> [!tip] Definición
> - **Diferencia:** $a - b := a + (-b)$.
> - **Cociente:** si $b \neq 0$, $\dfrac{a}{b} := a\, b^{-1}$.

Por eso dividir por $0$ no tiene sentido: $0^{-1}$ no existe. El axioma A5 solo garantiza inverso para $a \neq 0$, y la nota siguiente prueba que ningún valor podría hacer de $0^{-1}$ sin romper el resto del sistema (porque $a \cdot 0 = 0 \neq 1$).

## Un ejemplo de lectura de axiomas

Para despejar $x$ en $x + 5 = 8$ se escribe $x = 3$. Cada paso tiene su axioma:

1. Se suma $-5$ a ambos lados: $(x + 5) + (-5) = 8 + (-5)$.
2. Asociatividad (A2): $x + (5 + (-5)) = 3$.
3. Inverso (A5): $x + 0 = 3$.
4. Neutro (A3): $x = 3$.

> [!warning] Los axiomas no dicen "mayor" ni "menor"
> La lista de esta nota habla solo de operaciones. Que $2 < 3$, o que un cuadrado sea siempre positivo, **no** se deduce de ellos: hace falta una estructura adicional, los [[03 - Axiomas de orden y números positivos|axiomas de orden]].

## Preguntas de repaso

> [!question]- ¿Por qué $\mathbb{Z}$ no es un cuerpo aunque sea cerrado para suma y producto?
> Porque falla el axioma de inversos multiplicativos: por ejemplo $2 \in \mathbb{Z}$ pero $2^{-1} = \tfrac{1}{2} \notin \mathbb{Z}$.

> [!question]- ¿Qué axioma impide definir $0^{-1}$?
> El A5 solo exige inverso multiplicativo a los $a \neq 0$. Si existiera $0^{-1}$ se tendría $0 \cdot 0^{-1} = 1$, pero se demuestra que $a \cdot 0 = 0$ para todo $a$, lo que obligaría a $0 = 1$.

> [!question]- ¿Cómo se define $a - b$ y por qué no hace falta un axioma aparte para la resta?
> Se define como $a + (-b)$. Basta el inverso aditivo $-b$ del axioma A5: la resta es un nombre corto para una suma.

> [!question]- ¿En qué axiomas se apoya el paso $2(x + 3) = 2x + 6$?
> En la distributividad (A4): $2(x + 3) = 2x + 2 \cdot 3$, y luego se calcula $2 \cdot 3 = 6$.
