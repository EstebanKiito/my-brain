---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - origen/complemento
prerrequisitos:
  - "[[03 - Órdenes parciales y totales]]"
---

# Diagramas de Hasse y retículos

Un orden parcial sobre un conjunto finito se puede dibujar como un grafo dirigido, pero el dibujo se llena de flechas redundantes: los lazos de la reflexividad y las flechas que la transitividad ya deduce. El **diagrama de Hasse** conserva sólo la información esencial y deja ver de un vistazo qué va debajo de qué.

## Cómo se construye

Dado $(A,\preceq)$ finito, el diagrama de Hasse sigue tres reglas:
1. Cada elemento es un punto del dibujo.
2. Si $x \prec y$ ($x \preceq y$ y $x \ne y$), $x$ se dibuja **más abajo** que $y$.
3. Se une $x$ con $y$ con una línea sólo si $y$ **cubre** a $x$: no hay un $z$ distinto de ambos con $x \preceq z \preceq y$.

Las líneas no llevan flecha porque el "hacia arriba" ya indica el sentido. Para $(\mathcal{P}(\{1,2,3\}),\subseteq)$ el grafo completo tiene lazos y flechas redundantes (como la que va de $\emptyset$ a $\{1,2,3\}$):

![Grafo dirigido completo del orden de inclusión](adjuntos/Grafo%20dirigido%20del%20orden%20de%20inclusión%20con%20lazos%20y%20flechas%20redundantes.png)

> [!example]- Transcripción de la imagen
> Los ocho subconjuntos de $\{1,2,3\}$ en cuatro niveles: $\emptyset$ abajo, luego $\{1\},\{2\},\{3\}$, luego $\{1,2\},\{1,3\},\{2,3\}$ y $\{1,2,3\}$ arriba. Cada nodo tiene un lazo y hay flechas hacia arriba entre todo par comparable, incluidas curvas grandes de $\emptyset$ a $\{1,2,3\}$ y de $\{1\}$ y $\{3\}$ a $\{1,2,3\}$.

Quitando lazos y flechas deducibles queda el diagrama de Hasse:

![Diagrama de Hasse de las partes de un conjunto de tres elementos](adjuntos/Diagrama%20de%20Hasse%20del%20conjunto%20potencia%20de%20tres%20elementos.png)

> [!example]- Transcripción de la imagen
> $\emptyset$ en la base, unida con $\{1\}$, $\{2\}$ y $\{3\}$; cada singleton unido con dos de los pares ($\{1\}$ con $\{1,2\}$ y $\{1,3\}$, $\{2\}$ con $\{1,2\}$ y $\{2,3\}$, $\{3\}$ con $\{1,3\}$ y $\{2,3\}$), con las líneas cruzándose en el medio; y los tres pares unidos con $\{1,2,3\}$ arriba. Son 12 líneas.

El cálculo confirma las 12 relaciones de cobertura: $3$ de $\emptyset$ a los singletons, $6$ de singletons a pares y $3$ de pares a $\{1,2,3\}$.

## Leer el diagrama

Los **minimales** son los puntos sin nada debajo y los **maximales** los que no tienen nada encima. En el diagrama de las tareas para vestirse, la relación es "$t_1 \mapsto t_2$ si $t_1$ debe terminar antes de comenzar $t_2$":

![Diagrama de Hasse de las tareas para vestirse](adjuntos/Diagrama%20de%20Hasse%20de%20las%20tareas%20para%20vestirse.png)

> [!example]- Transcripción de la imagen
> Nueve tareas. Calcetines (Calz) están bajo pantalones (Pant); Pant está bajo zapatos (Zap) y bajo cinturón (Cint); calzoncillos (Calc) están bajo Zap; Zap está bajo cordones (Cord). Camisa (Camis) está bajo Cint y bajo corbata (Corb), y Corb bajo chaleco (Chal).

Aquí los minimales son Calc, Calz y Camis (lo primero que se puede hacer) y los maximales son Cord, Cint y Chal (lo último). Dos tareas incomparables, como Calc y Camis, se pueden hacer en cualquier orden.

## Retículos

Un orden es un **retículo** (*lattice*) si todo par $\{x,y\}$ tiene supremo e ínfimo (véase [[06 - Supremo e ínfimo de un conjunto]]). $(\mathcal{P}(U),\subseteq)$ lo es, con $\sup\{A,B\} = A\cup B$ e $\inf\{A,B\} = A\cap B$. $(\mathbb{N}\setminus\{0\},\mid)$ también: el supremo de $a,b$ es su mínimo común múltiplo y el ínfimo su máximo común divisor. El orden de las tareas **no** lo es: Calc y Camis no tienen ninguna cota superior común, así que su supremo no existe.

## Preguntas de repaso

> [!question]- ¿Por qué se pueden omitir los lazos y las flechas que van "dos niveles" arriba?
> Los lazos están garantizados por la reflexividad y las demás flechas se deducen por transitividad al seguir la cadena de líneas hacia arriba.

> [!question]- ¿Cómo se ve en un diagrama de Hasse que un elemento es mínimo y no sólo minimal?
> Un mínimo está bajo **todos** los demás: desde él se llega subiendo a cualquier punto. Un minimal sólo exige que nada quede debajo suyo.

> [!question]- ¿Cómo es el diagrama de Hasse de un orden total?
> Una sola cadena vertical: cada elemento cubre exactamente al anterior.

> [!question]- ¿Por qué las tareas con Calc y Camis dan un orden que no es retículo?
> Porque no existe ningún elemento mayor que ambos; sin cotas superiores comunes no hay supremo.
