---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de grafo y tipos de aristas]]"
---

# Isomorfismo y complemento de grafos

Dos dibujos distintos pueden representar el mismo grafo con otros nombres en los vértices. Esta nota formaliza cuándo dos grafos son "el mismo" (isomorfismo) y define las relaciones más usadas entre un grafo y otros derivados de él: subgrafos, cliques, conjuntos independientes y complemento.

## Isomorfismo

Dos grafos $G_1 = (V_1, E_1)$ y $G_2 = (V_2, E_2)$ son **isomorfos**, $G_1 \cong G_2$, si existe una **biyección** $f : V_1 \to V_2$ tal que $(x, y) \in E_1 \iff (f(x), f(y)) \in E_2$. La función $f$ es un **isomorfismo**: renombra vértices sin cambiar quién es adyacente con quién.

![Tres grafos isomorfos de cuatro vértices](adjuntos/Tres%20grafos%20isomorfos%20de%20cuatro%20vértices.png)

> [!example]- Transcripción de la imagen
> Tres grafos de cuatro vértices. El primero (vértices $a, b, c, d$) y el segundo ($1, 2, 3, 4$) son cuadrados con aristas $a$–$b$, $b$–$c$, $c$–$d$, $d$–$a$ (y análogas con números). El tercero tiene las mismas letras pero dibujado con una "equis": $a$–$b$, $d$–$c$ y las dos diagonales que se cruzan; también es un ciclo de cuatro vértices ($a$–$b$–$d$–$c$–$a$).

Los tres son $C_4$. Entre el primero y el segundo basta $f(a) = 1$, $f(b) = 2$, $f(c) = 3$, $f(d) = 4$; entre el primero y el tercero sirve $f(a) = a$, $f(b) = b$, $f(c) = d$, $f(d) = c$, que lleva las aristas del cuadrado $\{a,b\},\{b,c\},\{c,d\},\{d,a\}$ a $\{a,b\},\{b,d\},\{d,c\},\{c,a\}$, las del tercer dibujo.

> [!tip] Isomorfismo es una relación de equivalencia
> $\cong$ es refleja (la identidad), simétrica (la inversa $f^{-1}$ de una biyección que preserva aristas también las preserva) y transitiva (la composición $g \circ f$). Por eso las familias $P_n$, $C_n$, $K_n$ son clases de equivalencia. Dos grafos isomorfos comparten número de vértices, de aristas y la lista de grados, de modo que basta que una de estas difiera para probar que **no** son isomorfos.

Hay $1, 2, 4, 11, 34$ grafos no isomorfos con $1, 2, 3, 4, 5$ vértices respectivamente.

## Subgrafos

$H = (V_H, E_H)$ es **subgrafo** de $G$, $H \subseteq G$, si $V_H \subseteq V_G$, $E_H \subseteq E_G$ y $E_H$ solo contiene aristas entre vértices de $V_H$. Se obtiene borrando vértices (con sus aristas) y/o aristas.

![Subgrafo de un grafo](adjuntos/Subgrafo%20de%20un%20grafo.png)

> [!example]- Transcripción de la imagen
> A la izquierda $G$ con vértices $1, 2, 3, 4$ y aristas $\{1,2\}, \{2,3\}, \{1,3\}, \{1,4\}, \{3,4\}$. A la derecha $H \subseteq G$ con solo los vértices $1$, $2$ y $4$ y la arista $\{1,2\}$; el vértice $4$ queda aislado y el $3$ fue borrado con sus aristas.

## Cliques y conjuntos independientes

Un **clique** en $G$ es un conjunto de vértices $K \subseteq V$ en que todo par es adyacente; un **conjunto independiente** es uno en que ningún par es adyacente.

![Clique y conjunto independiente](adjuntos/Clique%20y%20conjunto%20independiente.png)

> [!example]- Transcripción de la imagen
> Grafo $G$ con aristas $\{1,2\}, \{2,3\}, \{1,3\}, \{1,4\}, \{3,4\}$. Se indica que $K = \{1,2,3\}$ es clique en $G$ y que $K' = \{2,4\}$ es un conjunto independiente en $G$.

## Complemento y autocomplementarios

El **complemento** $\overline{G} = (V, \overline{E})$ tiene los mismos vértices y $(u, v) \in \overline{E} \iff (u, v) \notin E$ (para $u \neq v$): une exactamente lo que $G$ deja sin unir. Un grafo es **autocomplementario** si $G \cong \overline{G}$; $P_4$ y $C_5$ lo son.

> [!tip] Cliques e independientes se intercambian
> $V' \subseteq V$ es un clique en $G$ si y solo si es un conjunto independiente en $\overline{G}$. Es inmediato de la definición: todos los pares de $V'$ están en $E$ si y solo si ninguno está en $\overline{E}$.

**Aplicación (seis personas).** En cualquier grupo de $6$ personas hay $3$ que se conocen entre sí o $3$ que no se conocen. Modelo: vértices = personas, aristas = "se conocen". Hay que probar que $G$ o $\overline{G}$ tiene un clique de tamaño $3$. Se toma un vértice $v$ y se mira sus $5$ posibles vecinos: o tiene al menos $3$ vecinos en $G$, o es no adyacente a al menos $3$ en $G$ (es decir, tiene $\geq 3$ vecinos en $\overline{G}$). Basta tratar el primer caso (el otro es simétrico intercambiando $G$ y $\overline{G}$): si entre esos tres vecinos $x, y, z$ hay una arista, con $v$ forma un triángulo en $G$; si no, $\{x, y, z\}$ es independiente en $G$, o sea un clique en $\overline{G}$. Con $5$ personas la afirmación es falsa: $C_5$ no tiene triángulo ni conjunto independiente de tamaño $3$.

## Preguntas de repaso

> [!question]- ¿Cómo se prueba que dos grafos con el mismo número de vértices y aristas no son isomorfos?
> Se busca un invariante que difiera, por ejemplo la lista de grados ordenada: un isomorfismo lleva cada vértice a otro del mismo grado. Si las listas de grados son distintas, no puede existir $f$.

> [!question]- ¿Por qué un subgrafo no puede tener una arista cuyo extremo no esté en $V_H$?
> Porque una arista es un par de vértices del propio grafo; si falta uno de sus extremos, la "arista" no sería un objeto de $H$. Por eso al borrar un vértice se borran sus aristas incidentes.

> [!question]- ¿Cuál es el complemento de $K_n$?
> El grafo sin aristas sobre $n$ vértices: como en $K_n$ todos los pares están unidos, en el complemento no queda ninguno.
