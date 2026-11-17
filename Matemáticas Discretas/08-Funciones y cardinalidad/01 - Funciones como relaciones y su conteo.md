---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/funciones
  - origen/complemento
prerrequisitos: []
---

# Funciones como relaciones y su conteo

Una **función** es la forma más estricta de asociar elementos de un conjunto con elementos de otro: cada entrada tiene a lo más una salida. Todo el tema de cardinalidad se apoya en funciones, porque comparar tamaños de conjuntos (incluso infinitos) se reduce a ver qué funciones existen entre ellos.

## Definición: una relación que no se bifurca

Una relación binaria de $A$ en $B$ es un subconjunto $f \subseteq A \times B$, un conjunto de pares $(a, b)$. Se dice que $f$ es una **función** de $A$ en $B$, y se escribe $f : A \to B$, si ningún elemento de $A$ queda asociado a dos elementos distintos:

$$a\,f\,b \;\wedge\; a\,f\,c \;\Rightarrow\; b = c.$$

Cuando $(a, b) \in f$ se escribe $b = f(a)$: $b$ es la **imagen** de $a$ y $a$ es una **preimagen** de $b$. Como una función es un conjunto de pares, hereda las operaciones de conjuntos (unión, intersección, inclusión) y dos operaciones propias de relaciones que se verán en [[03 - Composición e inversa de funciones]].

> [!tip] Función total
> Una función es **total** si todo $a \in A$ tiene imagen; si algún elemento queda sin imagen es **parcial**. En el ramo "función" significa total salvo que se avise lo contrario.

El conjunto $A$ es el **dominio** y $B$ el **codominio**. Hay que distinguir el codominio del **conjunto imagen** $f(A) = \{f(a) \mid a \in A\}$, que es el subconjunto de $B$ que realmente se alcanza. Para $X \subseteq A$ se escribe $f(X) = \{b \in B \mid \exists a \in X,\ f(a) = b\}$. Esa diferencia es la que luego separa funciones sobreyectivas de las que no lo son.

## Ejemplos que sí y que no son funciones

Sea $\mathbb{N}_4 = \{0, 1, 2, 3\}$. Estas tres relaciones son funciones de $\mathbb{N}_4$ en $\mathbb{N}_4$:

| Función | Pares | Qué hace |
|---|---|---|
| $f_1$ | $\{(0,0),(1,1),(2,2),(3,3)\}$ | identidad |
| $f_2$ | $\{(0,1),(1,1),(2,1),(3,1)\}$ | constante $1$ |
| $f_3$ | $\{(0,3),(1,2),(2,1),(3,0)\}$ | $n \mapsto 3 - n$ |

En cambio $\{(0,1),(0,2),(1,0)\}$ no es función, porque $0$ se asocia a $1$ y a $2$. Que dos elementos distintos compartan imagen (como en $f_2$) sí está permitido; lo que no se permite es que un mismo elemento tenga dos imágenes.

También se definen funciones con fórmulas. Algunas de $\mathbb{R}$ en $\mathbb{R}$: $f(x) = x^2 + 1$, o $f(x) = 1$ si $x \ge 0$ y $f(x) = -1$ si $x < 0$. Y de un conjunto $A$ en su conjunto potencia $\mathcal{P}(A)$: $a \mapsto \{a\}$, $a \mapsto A \setminus \{a\}$ o $a \mapsto \emptyset$. Esta última familia reaparece en el teorema de Cantor.

## Cuántas funciones hay

Una función $f : A \to B$ con $\lvert A \rvert = m$ y $\lvert B \rvert = n$ se construye eligiendo, para cada uno de los $m$ elementos de $A$, una imagen entre los $n$ de $B$. Las elecciones son independientes, así que hay

$$n^m = \lvert B \rvert^{\lvert A \rvert}$$

funciones de $A$ en $B$. Para $\mathbb{N}_4 \to \mathbb{N}_4$ son $4^4 = 256$. Es el mismo número que los subconjuntos de $A$ cuando $B = \{0, 1\}$: cada subconjunto corresponde a su función característica, y por eso $\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}$.

> [!warning] Dominio y codominio importan
> La regla $f(n) = n + 1$ define funciones distintas según el conjunto de llegada: de $\mathbb{N}$ en $\mathbb{N}$ es una función, pero de $\mathbb{N}$ en $\{0, 1, 2\}$ no lo es (la regla se sale del codominio). Una función queda determinada por el dominio, el codominio y la regla.

## Preguntas de repaso

> [!question]- ¿Por qué $\{(0,1),(0,2),(1,0)\}$ no es función de $\mathbb{N}_3$ en $\mathbb{N}_3$ aunque sea una relación?
> Porque $0$ tiene dos imágenes distintas, lo que viola $a f b \wedge a f c \Rightarrow b = c$. Además, $2$ no tiene imagen, así que tampoco sería total.

> [!question]- ¿Cuántas funciones hay de un conjunto de 3 elementos en uno de 5 y por qué esa fórmula?
> Hay $5^3 = 125$: cada uno de los 3 elementos del dominio elige libremente una de las 5 imágenes posibles.

> [!question]- ¿Qué diferencia hay entre codominio e imagen de una función?
> El codominio es el conjunto de llegada declarado; la imagen es el subconjunto de él que efectivamente se alcanza. Son iguales exactamente cuando la función es sobreyectiva.
