---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[06 - Relaciones de equivalencia y clases de equivalencia]]"
---

# Particiones, cuociente e índice y relación inducida

Las clases de una equivalencia cortan el conjunto en trozos que no se pisan. Ese «cortar en trozos» tiene un nombre, **partición**, y la correspondencia es total: toda equivalencia produce una partición y toda partición produce una equivalencia. Dos maneras de ver la misma estructura.

## Partición

Una colección $S \subseteq \mathcal{P}(A)$ es una **partición** de $A$ si:
1. todo $X \in S$ es no vacío,
2. $\bigcup S = A$ (los trozos cubren todo),
3. si $X \neq Y$ en $S$, entonces $X \cap Y = \emptyset$ (no se pisan).

![Partición de un conjunto](adjuntos/Partici%C3%B3n%20de%20un%20conjunto.png)

> [!example]- Transcripción de la imagen
> Una elipse dividida en seis regiones rotuladas $A_1, \dots, A_6$, sin superposiciones. A la derecha se leen las dos condiciones: $A_i \cap A_j = \emptyset$ siempre que $i \neq j$ y $A_1 \cup A_2 \cup \cdots \cup A_6 = A$.

Ejemplos sobre $\mathbb{N}$: los pares y los impares; o las cuatro clases de restos módulo $4$. En cambio $\{\{0, 1\}, \{1, 2\}\}$ no es partición de $\{0, 1, 2\}$ porque los trozos se solapan en $1$.

## Conjunto cuociente e índice

El **conjunto cuociente** de $A$ por $\sim$ es el conjunto de todas las clases, $A/{\sim} = \{[x] \mid x \in A\}$. Sus elementos son conjuntos, no números. El **índice** de $\sim$ es la cantidad de clases, $\lvert A/{\sim} \rvert$. Por ejemplo, $\mathbb{N}/{\equiv_4} = \{[0], [1], [2], [3]\}$ y el índice de $\equiv_4$ es $4$.

## Equivalencia $\Rightarrow$ partición

> [!tip] Teorema
> Si $\sim$ es de equivalencia sobre $A$, entonces $A/{\sim}$ es una partición de $A$.

Las clases son no vacías porque $x \in [x]$. Su unión es $A$: cada clase está contenida en $A$ y cada $x \in A$ está en $[x] \in A/{\sim}$. Y dos clases distintas son disjuntas por el teorema de las clases. Es decir, las tres condiciones de partición salen de las tres propiedades vistas.

## Partición $\Rightarrow$ equivalencia

> [!tip] Teorema recíproco
> Si $S$ es una partición de $A$, entonces $x \sim y \iff \exists X \in S\ \{x, y\} \subseteq X$ es de equivalencia (dos elementos se relacionan si caen en el mismo trozo).

**Refleja:** $x$ está en algún $X \in S$ porque $\bigcup S = A$, luego $\{x, x\} \subseteq X$. **Simétrica:** $\{x, y\} = \{y, x\}$. **Transitiva:** si $\{x, y\} \subseteq X_1$ y $\{y, z\} \subseteq X_2$, entonces $y \in X_1 \cap X_2$; como los trozos distintos son disjuntos, $X_1 = X_2$, y así $\{x, z\} \subseteq X_2$.

Con $A = \{0, 1, 2, 3, 4\}$ y la partición $\{\{0, 3, 4\}, \{1\}, \{2\}\}$, la relación inducida tiene $3^2 + 1 + 1 = 11$ pares: los nueve pares dentro de $\{0, 3, 4\}$, más $(1, 1)$ y $(2, 2)$. Aplicar los dos teoremas en cadena devuelve lo mismo que se tenía: partir de una partición, tomar su equivalencia y calcular su cuociente da la partición original.

Como equivalencias y particiones se corresponden una a una, sobre un conjunto de 3 elementos hay tantas equivalencias como particiones: $5$ (todo junto, todo separado y las tres formas de agrupar un par aparte). Para $n = 0, 1, \dots, 6$ elementos son $1, 1, 2, 5, 15, 52, 203$ (números de Bell).

## Un cuociente que construye los racionales

Sobre $Q = \mathbb{Z} \times (\mathbb{Z} \setminus \{0\})$ se define $(a, b) \uparrow (c, d) \iff a d = b c$, que es de equivalencia y agrupa los pares que representan la misma fracción: $(1, 2) \uparrow (3, 6)$. El cuociente $Q/{\uparrow}$ **es** el conjunto de los racionales, con la clase $[(a, b)]$ en el papel de la fracción $a/b$. Las operaciones se definen con representantes, $[(a,b)] + [(c,d)] = [(ad + bc,\, bd)]$, y no dependen del representante escogido.

## Preguntas de repaso

> [!question]- ¿Por qué cualquier elemento puede ser representante de su clase?
> Porque si $y \in [x]$ entonces $x \sim y$, y por el teorema de las clases $[x] = [y]$: ambos generan el mismo conjunto.

> [!question]- ¿Qué le ocurriría a la relación inducida si la partición tuviera trozos que se solapan?
> Dejaría de ser transitiva: en $\{\{0, 1\}, \{1, 2\}\}$ se tendría $0 \sim 1$ y $1 \sim 2$ pero $0 \not\sim 2$.

> [!question]- ¿Qué índice tiene la equivalencia «mismo resto módulo $n$»?
> Índice $n$: las clases son $[0], \dots, [n-1]$, ya que todo natural tiene exactamente un resto entre $0$ y $n-1$.

> [!question]- ¿Por qué la condición de «no vacío» es necesaria en la definición de partición?
> Porque cada trozo debe provenir de una clase, y toda clase contiene a su representante. Un trozo vacío no podría ser clase de ningún elemento.
