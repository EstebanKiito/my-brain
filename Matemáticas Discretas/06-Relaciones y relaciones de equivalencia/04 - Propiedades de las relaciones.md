---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Relación inversa y composición de relaciones]]"
---

# Propiedades de las relaciones

Las relaciones que importan (equivalencias, órdenes) se reconocen por un puñado de propiedades. Cada una es una condición universal sobre los pares de la relación, así que se demuestra con un elemento arbitrario y se refuta con un contraejemplo concreto.

## Las siete propiedades

Sea $R$ una relación sobre $A$. Es:

| Propiedad | Condición | Se ve en el grafo como |
|---|---|---|
| **Refleja** | $\forall a\; R(a, a)$ | bucle en cada punto |
| **Irrefleja** | $\forall a\; \neg R(a, a)$ | ningún bucle |
| **Simétrica** | $R(a, b) \Rightarrow R(b, a)$ | toda flecha tiene su vuelta |
| **Asimétrica** | $R(a, b) \Rightarrow \neg R(b, a)$ | ninguna flecha de ida y vuelta (ni bucles) |
| **Antisimétrica** | $R(a, b) \wedge R(b, a) \Rightarrow a = b$ | ida y vuelta solo en bucles |
| **Transitiva** | $R(a, b) \wedge R(b, c) \Rightarrow R(a, c)$ | cada atajo de dos pasos existe |
| **Conexa** | $R(a, b) \vee R(b, a)$ para todo par | todo par está unido en algún sentido |

> [!warning] Irrefleja no es «no refleja»
> «No refleja» significa que falta algún bucle; «irrefleja» que faltan todos. Del mismo modo, asimétrica es más fuerte que antisimétrica (prohíbe también los bucles) y simétrica no es lo opuesto de antisimétrica: la relación $=$ es ambas cosas.

Ejemplos sobre $\mathbb{N}$: $\leq$ es refleja, antisimétrica, transitiva y conexa; $<$ es irrefleja, asimétrica y transitiva; $=$ y $\equiv_n$ son reflejas, simétricas y transitivas; $\mid$ es refleja, antisimétrica y transitiva, pero no conexa ($2 \nmid 3$ y $3 \nmid 2$).

## Leer propiedades en un grafo

Sea $A = \{0, 1, 2, 3\}$ y $R = \{(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)\}$.

![Grafo dirigido de una relación refleja y simétrica no transitiva](adjuntos/Grafo%20dirigido%20de%20una%20relaci%C3%B3n%20refleja%20y%20sim%C3%A9trica%20no%20transitiva.png)

> [!example]- Transcripción de la imagen
> Cuatro puntos rotulados $0, 1, 2, 3$. Cada uno tiene un bucle. Entre $0$ y $1$ hay flechas en ambos sentidos, y entre $0$ y $3$ también. El punto $2$ está aislado salvo su bucle. No hay flecha entre $1$ y $3$.

$R$ es **refleja** (cuatro bucles) y **simétrica** (cada flecha tiene su vuelta), pero **no transitiva**: $1\,R\,0$ y $0\,R\,3$, y sin embargo $(1, 3) \notin R$. Un solo trío de este tipo basta para refutar.

## Demostraciones típicas

**$\mid$ es refleja, antisimétrica y transitiva** (sobre $\mathbb{N}$ sin el 0). Refleja: $a = 1 \cdot a$. Antisimétrica: si $a \mid b$ y $b \mid a$, existen $k_1, k_2$ con $b = k_1 a$ y $a = k_2 b$; luego $b = k_1 k_2 b$ y, como $b \neq 0$, $k_1 k_2 = 1$, de modo que $k_1 = k_2 = 1$ y $a = b$. Transitiva: $b = k_1 a$ y $c = k_2 b$ dan $c = (k_2 k_1) a$.

**$\equiv_n$ es refleja, simétrica y transitiva.** Refleja: $\lvert x - x \rvert = 0 = 0 \cdot n$. Simétrica: $\lvert x - y \rvert = \lvert y - x \rvert$. Transitiva: si $x - y = \pm k_1 n$ y $y - z = \pm k_2 n$, al sumar se obtiene $x - z = (\pm k_1 \pm k_2)\, n$, un múltiplo de $n$ en valor absoluto.

## Caracterización con operaciones

Con $D = \{(a, a) \mid a \in A\}$ (la **relación diagonal** o identidad), las propiedades se vuelven igualdades o inclusiones entre conjuntos, válidas aunque $A$ sea infinito:

- $R$ es refleja $\iff D \subseteq R$.
- $R$ es simétrica $\iff R = R^{-1}$.
- $R$ es antisimétrica $\iff R \cap R^{-1} \subseteq D$.
- $R$ es transitiva $\iff R \circ R \subseteq R$.

Si $A$ es finito, equivalen a condiciones sobre la matriz: diagonal de unos, $M_R = M_R^{\top}$, $M_R \wedge M_R^{\top} \leq I$ y $M_R^2 \leq M_R$ (entrada a entrada).

Sobre un conjunto de 3 elementos hay $512$ relaciones; de ellas $64$ son reflejas, $64$ simétricas, $216$ antisimétricas, $27$ asimétricas y $171$ transitivas.

## Preguntas de repaso

> [!question]- ¿Por qué la relación vacía sobre un conjunto no vacío es simétrica y transitiva pero no refleja?
> Simetría y transitividad son implicaciones cuya premisa nunca se cumple (no hay pares), así que valen vacuamente; la reflexividad exige que existan los pares $(a, a)$, que no están.

> [!question]- ¿Cómo se refuta la transitividad?
> Se exhiben $a, b, c$ con $R(a, b)$ y $R(b, c)$ pero $\neg R(a, c)$. Un único trío concreto basta.

> [!question]- ¿Puede una relación ser simétrica y antisimétrica a la vez?
> Sí, pero solo si está contenida en la diagonal $D$: cualquier par $(a, b)$ con $a \neq b$ exigiría $(b, a)$ por simetría y $a = b$ por antisimetría.

> [!question]- ¿Por qué la demostración de antisimetría de $\mid$ se hace sobre los naturales sin el $0$?
> Porque cancela $b$ en $b = k_1 k_2 b$, y eso solo da $k_1 k_2 = 1$ si $b \neq 0$. El caso $b = 0$ habría que tratarlo aparte.
