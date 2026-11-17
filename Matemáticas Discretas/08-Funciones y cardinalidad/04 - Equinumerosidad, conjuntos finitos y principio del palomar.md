---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/cardinalidad
  - origen/complemento
prerrequisitos:
  - "[[03 - Composición e inversa de funciones]]"
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Equinumerosidad, conjuntos finitos y principio del palomar

Contar los elementos de $\{a, b, c, d, e, f\}$ es poner una etiqueta $1, 2, \dots, 6$ a cada uno sin repetir ni dejar ninguno. Contar es entonces construir una biyección con un conjunto de números. Esa idea, que no usa números sino funciones, sirve también para comparar conjuntos infinitos, donde no se puede "terminar de contar".

## Equinumerosidad

Dos conjuntos $A$ y $B$ son **equinumerosos** si existe una función biyectiva $f : A \to B$; se escribe $A \approx B$ y se dice que tienen el mismo tamaño.

> [!tip] La relación $\approx$ es de equivalencia
> Es refleja (la identidad $A \to A$ es biyectiva), simétrica (si $f : A \to B$ es biyectiva, $f^{-1}$ lo es de $B$ en $A$) y transitiva (si $f : A \to B$ y $g : B \to C$ son biyectivas, $g \circ f$ lo es de $A$ en $C$).

La **cardinalidad** de $A$ es su clase de equivalencia: $\lvert A \rvert = [A]_\approx$. Dos conjuntos tienen la misma cardinalidad exactamente cuando son equinumerosos. Las clases son bloques de conjuntos "del mismo tamaño"; todo conjunto con seis elementos cae en la misma clase.

## Conjuntos finitos

Un conjunto $A$ es **finito** si $A \approx n = \{0, 1, \dots, n-1\}$ para algún $n \in \mathbb{N}$. Entonces se escribe $\lvert A \rvert = n$ y se dice que tiene $n$ elementos. El caso $n = 0$ corresponde a $A = \emptyset$. Un conjunto que no es finito es **infinito**.

Ejemplo: $A = \{a, b, c, d, e, f\}$ es equinumeroso con $\{0, \dots, 5\}$ mediante $a \mapsto 0, b \mapsto 1, \dots, f \mapsto 5$, así que $\lvert A \rvert = 6$.

**Unión disjunta.** Si $A$ y $B$ son finitos y disjuntos, $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$. Si $f : A \to \{0, \dots, n-1\}$ y $g : B \to \{0, \dots, m-1\}$ son biyecciones, la función $h(x) = f(x)$ si $x \in A$ y $h(x) = n + g(x)$ si $x \in B$ es una biyección sobre $\{0, \dots, n+m-1\}$: bien definida porque $A \cap B = \emptyset$, inyectiva porque $f$ y $g$ lo son y sus rangos $[0, n)$ y $[n, n+m)$ no se tocan, y sobreyectiva porque cada $k$ cae en uno de esos dos rangos.

**Conjunto potencia.** Si $A$ es finito, $\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}$. Por inducción sobre $n = \lvert A \rvert$:
- **Base** $n = 0$: $\mathcal{P}(\emptyset) = \{\emptyset\}$ tiene $1 = 2^0$ elementos.
- **Paso.** Sea $\lvert A \rvert = n + 1$, con $a \in A$ y $B = A \setminus \{a\}$. Los subconjuntos de $A$ son los que no contienen a $a$ (es decir, $\mathcal{P}(B)$, con $2^n$ elementos por HI) y los que sí lo contienen. La función $X \mapsto X \cup \{a\}$ es una biyección entre los primeros y los segundos, así que también hay $2^n$ de estos. Por la unión disjunta, $\lvert \mathcal{P}(A) \rvert = 2^n + 2^n = 2^{n+1}$.

En particular, para todo conjunto finito, $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$. El teorema de Cantor extiende esto a todos los conjuntos.

## Principio del palomar

> [!tip] Principio del palomar (o de los cajones)
> Si $m > n$ y $f : \mathbb{N}_m \to \mathbb{N}_n$, entonces $f$ **no** es inyectiva: existen $x \ne y$ con $f(x) = f(y)$. Si $m < n$, $f$ **no** es sobreyectiva. Por lo tanto, una biyección $\mathbb{N}_m \to \mathbb{N}_n$ solo existe si $m = n$.

Se llama así porque repartir $m$ palomas en $n$ palomares con $m > n$ obliga a que algún palomar tenga dos. Ejemplo: en una sala con 8 personas, la función que a cada persona le asigna el día de la semana de su cumpleaños va de un conjunto de 8 a uno de 7, luego no es inyectiva y dos personas celebran el mismo día de la semana. Su utilidad es que prueba existencia sin exhibir quiénes son.

> [!warning] Solo vale para conjuntos finitos
> En $\mathbb{N}$ la función $n \mapsto 2n$ lleva $\mathbb{N}$ en una parte propia y es inyectiva. El palomar descansa en que $\mathbb{N}_n$ es finito, y por eso la cardinalidad de infinitos exige otras ideas (ver [[05 - Conjuntos enumerables y listas infinitas]]).

## Preguntas de repaso

> [!question]- ¿Por qué se define el tamaño mediante una biyección y no contando?
> Porque "contar" no tiene sentido para conjuntos infinitos, mientras que la existencia de una biyección sí. Además coincide con contar en el caso finito.

> [!question]- ¿Qué se usa en la prueba de $\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}$ para pasar de $n$ a $n+1$?
> Se separa $\mathcal{P}(A)$ en los subconjuntos sin $a$ y con $a$; la función $X \mapsto X \cup \{a\}$ muestra que ambos grupos tienen igual tamaño, y la suma de uniones disjuntas da $2^n + 2^n$.

> [!question]- ¿Cuántas personas hacen falta en una sala para asegurar que dos cumplan años el mismo mes?
> Trece: con doce personas cada una puede tener un mes distinto, y con trece la función persona $\mapsto$ mes va de 13 a 12 elementos y no es inyectiva.
