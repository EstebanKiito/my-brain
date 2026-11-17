---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[04 - Propiedades de las relaciones]]"
  - "[[05 - Clausuras de una relación]]"
---

# Relaciones de equivalencia y clases de equivalencia

Muchas veces dos objetos distintos se tratan como «el mismo» según algún criterio: dos fracciones que valen lo mismo, dos números con igual resto al dividir por 7, dos fórmulas con la misma tabla de verdad. Una **relación de equivalencia** formaliza ese criterio de identificación y las **clases de equivalencia** agrupan los objetos que el criterio no distingue.

## Definición

> [!tip] Relación de equivalencia
> Una relación $\sim$ sobre $A$ es de equivalencia si es **refleja, simétrica y transitiva**.

Los ejemplos más usados:
- $\equiv_n$ sobre $\mathbb{N}$ (mismo resto al dividir por $n$).
- La **equivalencia lógica** $\varphi \equiv \psi \iff \forall\sigma\ \sigma(\varphi) = \sigma(\psi)$ sobre las fórmulas proposicionales: es refleja y simétrica porque la igualdad lo es, y transitiva porque $\sigma(\varphi) = \sigma(\psi) = \sigma(\theta)$ da $\sigma(\varphi) = \sigma(\theta)$.
- Dada una función $f$, «$x \sim y \iff f(x) = f(y)$»: hereda las tres propiedades de la igualdad.

No lo son $\leq$ (no es simétrica), $<$ (no es refleja) ni «$\lvert x - y \rvert \leq 1$» sobre $\mathbb{Z}$ (no es transitiva: $0 \sim 1$ y $1 \sim 2$, pero $0 \not\sim 2$).

## Clase de equivalencia

Para $x \in A$, su **clase** es el conjunto de todo lo que es equivalente a él:

$$[x]_\sim = \{y \in A \mid x \sim y\}.$$

Un ejemplo con el grafo de la relación $x \sim y \iff 3 \mid (x - y)$ sobre $A = \{2, 3, 4, 6, 7, 9\}$:

![Grafo dirigido de la congruencia módulo 3](adjuntos/Grafo%20dirigido%20de%20la%20congruencia%20m%C3%B3dulo%203.png)

> [!example]- Transcripción de la imagen
> Un grafo dirigido con tres piezas separadas. El punto $2$ está solo, con un bucle. Los puntos $4$ y $7$ tienen un bucle cada uno y flechas en ambos sentidos entre ellos. Los puntos $3$, $6$ y $9$ forman un triángulo en el que cada par está unido por flechas de ida y vuelta, y cada uno tiene su bucle. No hay flechas entre piezas distintas.

Las clases son $[2] = \{2\}$, $[4] = [7] = \{4, 7\}$ y $[3] = [6] = [9] = \{3, 6, 9\}$. Se ve el patrón general: un grafo de equivalencia se descompone en «islas» completamente conectadas, y cada isla es una clase. En $\mathbb{N}$, $\equiv_4$ tiene las clases $[0] = \{0, 4, 8, \dots\}$, $[1]$, $[2]$ y $[3]$.

Bajo la equivalencia lógica, cada clase reúne todas las fórmulas con la misma tabla de verdad. Con $n$ variables hay $2^{2^n}$ tablas posibles (cada una de las $2^n$ filas vale 0 o 1), luego esa es la cantidad de clases.

## Teorema fundamental de las clases

> [!tip] Propiedades de las clases
> Sea $\sim$ de equivalencia sobre $A$. Entonces:
> 1. $x \in [x]$ para todo $x$.
> 2. $x \sim y \iff [x] = [y]$.
> 3. Si $[x] \neq [y]$, entonces $[x] \cap [y] = \emptyset$.

**(1)** Por reflexividad $x \sim x$, es decir $x \in [x]$.

**(2)** ($\Rightarrow$) Si $x \sim y$ y $z \in [x]$, entonces $x \sim z$; por simetría $y \sim x$ y por transitividad $y \sim z$, así que $z \in [y]$. Entonces $[x] \subseteq [y]$; el argumento simétrico da $[y] \subseteq [x]$. ($\Leftarrow$) Por (1), $y \in [y] = [x]$, o sea $x \sim y$.

**(3)** Por contrarrecíproco: si existe $z \in [x] \cap [y]$, entonces $x \sim z$ y $y \sim z$; por simetría y transitividad $x \sim y$, y por (2) $[x] = [y]$.

El sentido práctico es doble: cualquier elemento de una clase sirve como **representante** (por eso $[4] = [7]$), y dos clases son iguales o completamente disjuntas, nunca se solapan parcialmente.

## Preguntas de repaso

> [!question]- ¿Por qué la clase de un elemento nunca es vacía?
> Porque por reflexividad $x \sim x$, de modo que $x \in [x]$.

> [!question]- ¿Qué falla si una relación es refleja y simétrica pero no transitiva, al intentar definir clases?
> Las «clases» pueden solaparse sin coincidir. Con $0 \sim 1$ y $1 \sim 2$ pero $0 \not\sim 2$, el $1$ pertenece a las clases de $0$ y de $2$, que no son iguales ni disjuntas.

> [!question]- ¿Cuántas clases tiene la equivalencia lógica sobre fórmulas con 3 variables y qué representan?
> Tiene $2^{2^3} = 256$ clases; cada una corresponde a una de las posibles tablas de verdad de 8 filas.

> [!question]- Si $[a] \cap [b] \neq \emptyset$, ¿qué se concluye?
> Que $[a] = [b]$: el contrarrecíproco del punto 3 del teorema. Un elemento común $z$ da $a \sim z$ y $b \sim z$, y por tanto $a \sim b$.
