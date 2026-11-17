---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos: []
---

# Conjunto cuociente y particiones

Una relación de equivalencia agrupa los elementos que se consideran "lo mismo" bajo algún criterio. Si en lugar de mirar elemento por elemento se mira **grupo por grupo**, aparece un conjunto nuevo y más pequeño: el conjunto cuociente. Es la herramienta que permite pasar de "muchos objetos equivalentes" a "un representante por clase".

## Clases y conjunto cuociente

Sea $\sim$ una relación de equivalencia (refleja, simétrica y transitiva) sobre $A$. La **clase de equivalencia** de $x$ es $[x] = \{y \in A \mid x \sim y\}$. Se cumple siempre que $x \in [x]$, que $x \sim y \iff [x] = [y]$ y que dos clases distintas son disjuntas.

> [!tip] Conjunto cuociente
> El **conjunto cuociente** de $A$ respecto a $\sim$ es el conjunto de todas sus clases: $A/{\sim} \;=\; \{[x] \mid x \in A\}$. Sus elementos son conjuntos, no elementos de $A$.

**Ejemplo.** En $\mathbb{Z}$, la congruencia módulo $4$ ($a \equiv_4 b$ si $4$ divide a $a-b$) tiene cuatro clases, según el resto de dividir por $4$:

$$\mathbb{Z}/{\equiv_4} = \{[0],[1],[2],[3]\}, \qquad [1] = \{\dots,-7,-3,1,5,9,\dots\}.$$

![Los enteros pintados según su clase módulo 4](adjuntos/Clases%20de%20equivalencia%20de%20congruencia%20módulo%204.png)

> [!example]- Transcripción de la imagen
> Una fila de círculos con los enteros desde $-4$ hasta $8$, cada uno con uno de cuatro tonos: $-4, 0, 4, 8$ comparten color (clase $[0]$), igual que $-3, 1, 5$ ($[1]$), $-2, 2, 6$ ($[2]$) y $-1, 3, 7$ ($[3]$). Los colores se repiten cada cuatro posiciones. Debajo figura $\mathbb{N}/{\equiv_4} = \{[0],[1],[2],[3]\}$.

El **índice** de la relación es la cantidad de clases, es decir, $\lvert A/{\sim}\rvert$. El de $\equiv_4$ es $4$.

## Particiones

Una **partición** de $A$ es una colección $S \subseteq \mathcal{P}(A)$ que cumple tres cosas: ningún bloque es vacío, la unión de los bloques es todo $A$, y dos bloques distintos son disjuntos. Por ejemplo, $\{\text{pares}, \text{impares}\}$ y $\{\{n\} \mid n \in \mathbb{N}\}$ son particiones de $\mathbb{N}$; en cambio $\{\{1,2\},\{2,3\}\}$ no lo es sobre $\{1,2,3\}$ porque los bloques se solapan.

> [!tip] Equivalencia y partición son lo mismo visto de dos lados
> Si $\sim$ es de equivalencia, entonces $A/{\sim}$ es una partición de $A$. Recíprocamente, toda partición $S$ de $A$ define una relación de equivalencia con $x \sim y \iff \exists X \in S\ (\{x,y\} \subseteq X)$, y su conjunto cuociente es $S$.

**Por qué $A/{\sim}$ es partición.** (1) Cada clase es no vacía porque $x \in [x]$. (2) La unión de las clases es $A$: cada clase está contenida en $A$ y cada $x$ está en su propia clase $[x]$. (3) Clases distintas son disjuntas por la propiedad ya citada.

**Por qué una partición da una equivalencia.** Refleja: cada $x$ está en algún bloque $X$, luego $\{x,x\} \subseteq X$. Simétrica: $\{x,y\} = \{y,x\}$. Transitiva: si $\{x,y\} \subseteq X_1$ y $\{y,z\} \subseteq X_2$, entonces $y \in X_1 \cap X_2$; como bloques distintos son disjuntos, $X_1 = X_2$ y por tanto $\{x,z\} \subseteq X_1$.

> [!warning] Los elementos del cuociente son conjuntos
> $[1]$ y $[5]$ son el **mismo** elemento de $\mathbb{Z}/{\equiv_4}$ (porque $1 \sim 5$). Contar clases no es contar números: el índice de $\equiv_4$ es $4$, aunque cada clase tenga infinitos enteros.

## Preguntas de repaso

> [!question]- ¿Por qué dos clases de equivalencia nunca se solapan sin ser iguales?
> Si $z \in [x] \cap [y]$, entonces $z \sim x$ y $z \sim y$; por simetría y transitividad $x \sim y$, y de ahí $[x] = [y]$. Un solapamiento obliga a que sean la misma clase.

> [!question]- ¿Cuál es el índice de la relación "tienen el mismo resto al dividir por $7$" y qué ocurre con su cuociente?
> El índice es $7$ y el cuociente es $\{[0],\dots,[6]\}$, una partición de $\mathbb{Z}$ en siete bloques infinitos.

> [!question]- ¿Es $\{\{x \in \mathbb{N} \mid x < 5\}, \{x \in \mathbb{N} \mid x \ge 5\}\}$ una partición de $\mathbb{N}$? ¿Qué equivalencia induce?
> Sí: bloques no vacíos, disjuntos y de unión $\mathbb{N}$. Induce "ambos son menores que $5$ o ambos son al menos $5$", con índice $2$.

> [!question]- ¿Por qué no sirve $\{\{1,2\},\{2,3\}\}$ como partición de $\{1,2,3\}$?
> Los bloques comparten el $2$, así que la relación inducida sería $1 \sim 2$ y $2 \sim 3$ pero no $1 \sim 3$: no sería transitiva.
