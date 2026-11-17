---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Cotas elementos minimales y mínimos]]"
  - "[[06 - Supremo e ínfimo de un conjunto]]"
---

# Ejercicios de ayudantías de cuocientes y órdenes

Cinco ejercicios de ayudantía sobre relaciones de orden: demostrar que una relación es un orden total, decidir verdadero o falso con contraejemplos, combinar equivalencias con órdenes, y calcular elementos extremos de un conjunto concreto. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Monarquías
Sea $K$ el conjunto de los monarcas ingleses y $M$ la relación "$a\,M\,b$ si $a$ reinó después o al mismo tiempo que $b$". Demuestre que $M$ y su inversa $M^{-1}$ ("antes o al mismo tiempo") son órdenes totales.

> [!example]- Solución
> **Refleja:** todo monarca reina al mismo tiempo que sí mismo. **Antisimétrica:** si $a\,M\,b$ y $b\,M\,a$, $a$ reinó después de $b$ y $b$ después de $a$, lo que sólo es posible si son el mismo monarca (en cada momento hay uno solo y nadie reina dos veces separadas). **Transitiva:** si $a$ reinó después que $b$ y $b$ después que $c$, por linealidad del tiempo $a$ reinó después que $c$. **Conexa:** dados $a,b$, o reinaron en el orden $a$ después de $b$, o $b$ después de $a$, o son el mismo. Para $M^{-1}$ valen las mismas propiedades con el orden temporal invertido; la inversa de un orden total es un orden total.

### 2. Verdadero o falso sobre mínimos
Sea $(A,\preceq)$ un orden parcial con $A \ne \emptyset$. Decida: (1) si todo $S \subseteq A$ no vacío tiene mínimo, entonces $\preceq$ es total; (2) si $\preceq$ es total, todo $S \subseteq A$ no vacío tiene mínimo; (3) si $x$ es minimal y maximal de $S$, entonces $S$ tiene un solo elemento.

> [!example]- Solución
> 1. **Verdadero.** Dados $a,b \in A$, el conjunto $\{a,b\}$ tiene mínimo, que es $a$ o $b$; luego $a \preceq b$ o $b \preceq a$, es decir, el orden es conexo.
> 2. **Falso.** $(\mathbb{Z},\le)$ es total y $\mathbb{Z}$ no tiene mínimo. (Es verdad para conjuntos finitos.)
> 3. **Falso.** En $(\mathbb{N}\setminus\{0\},\mid)$, $S = \{2,3\}$ tiene $2$ y $3$ minimales y maximales a la vez. Otro contraejemplo: $\{\{1,2\},\{3,4\}\}$ con $\subseteq$.

### 3. La mezcla: orden sobre el cuociente
Sean $\simeq$ una equivalencia y $\preceq$ un orden parcial sobre $A$. En $A/{\simeq}$ se define $S_1 \ll S_2$ si existe $a \in S_1$ tal que $a \preceq b$ para todo $b \in S_2$. Sea $\ll^r$ su clausura refleja. Demuestre que $\ll^r$ es un orden parcial.

> [!example]- Solución
> **Refleja** por ser clausura refleja. **Antisimétrica:** si $S_1 \ll^r S_2$ y $S_2 \ll^r S_1$ con $S_1 \ne S_2$, existen $a \in S_1$ con $a \preceq b$ para todo $b \in S_2$ y $c \in S_2$ con $c \preceq d$ para todo $d \in S_1$. En particular $a \preceq c$ y $c \preceq a$, así que $a = c$; como $a \in S_1$ y $c \in S_2$ son el mismo elemento, las clases coinciden, contradicción. **Transitiva:** si $S_1 \ll S_2$ (con $a \in S_1$) y $S_2 \ll S_3$ (con $c \in S_2$), entonces $a \preceq c$ por ser $c \in S_2$, y $c \preceq d$ para todo $d \in S_3$; por transitividad $a \preceq d$ y $S_1 \ll S_3$. Los casos con igualdad son triviales. Una comprobación por fuerza bruta en cientos de órdenes y equivalencias aleatorias de hasta seis elementos confirma el resultado.

### 4. ¿Elemento minimal arriba y abajo?
Con la misma notación, ¿es cierto que $A$ tiene un elemento minimal según $\preceq$ si y sólo si $A/{\simeq}$ tiene un minimal según $\ll^r$?

> [!example]- Solución
> **Falso**; la ida es cierta pero la vuelta no. Contraejemplo: $A = \mathbb{Z}$ con $\le$, y $a \simeq b$ si $a,b$ son ambos negativos o ambos no negativos. El cuociente es $\{N, P\}$ con $N$ los negativos y $P$ los no negativos. Como todo negativo es menor que cualquier elemento de $P$, $N \ll P$: $N$ es minimal en el cuociente. Pero $(\mathbb{Z},\le)$ no tiene ningún elemento minimal.

### 5. Elementos extremos de un conjunto concreto
En $(\mathcal{P}(\{1,2,3\}),\subseteq)$ sea $S = \{\{1\},\{2\},\{1,2\},\{1,3\}\}$. Determine cotas, minimales, maximales, mínimo, máximo, ínfimo y supremo.

> [!example]- Solución
> - **Cotas inferiores:** sólo $\emptyset$ (nada no vacío está en $\{1\}$ y en $\{2\}$ a la vez). Por tanto $\inf S = \emptyset$, que no pertenece a $S$.
> - **Cotas superiores:** sólo $\{1,2,3\}$, así que $\sup S = \{1,2,3\}$, tampoco en $S$.
> - **Minimales:** $\{1\}$ y $\{2\}$ (nada de $S$ está debajo). **Maximales:** $\{1,2\}$ y $\{1,3\}$ (nada de $S$ está encima).
> - **Mínimo y máximo:** no hay, porque ni $\emptyset$ ni $\{1,2,3\}$ están en $S$.
>
> Los resultados se comprobaron enumerando todos los subconjuntos de $\{1,2,3\}$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 4 el orden sobre el cuociente crea un elemento minimal que no existía?
> Porque agrupar elementos en clases oculta que hay una cadena descendente infinita: $N$ se comporta como un único elemento aunque dentro de él no haya un menor.

> [!question]- ¿Qué técnica común usan los contraejemplos del ejercicio 2?
> Usar dos elementos incomparables (para el 3) o un conjunto infinito sin primer elemento (para el 2), que son las dos formas típicas de romper propiedades de un orden total.

> [!question]- ¿Por qué en el ejercicio 3 basta el elemento $a$ y no todos los elementos de $S_1$?
> La definición de $\ll$ es existencial en $S_1$ y universal en $S_2$: un representante de $S_1$ debajo de toda $S_2$ ya sitúa la clase completa antes.
