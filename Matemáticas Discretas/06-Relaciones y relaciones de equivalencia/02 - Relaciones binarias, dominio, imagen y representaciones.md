---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Pares ordenados, producto cartesiano y relaciones n-arias]]"
---

# Relaciones binarias, dominio, imagen y representaciones

De las relaciones $n$-arias, el caso más usado es el binario: dos elementos están o no están relacionados. Así se formalizan ideas como «es menor que», «divide a» o «tiene el mismo resto que». Elegir bien la representación (conjunto de pares, flechas, grafo o matriz) hace que ciertas propiedades se vean a simple vista.

## Definición y notación

Una **relación binaria de $A$ en $B$** es un subconjunto $R \subseteq A \times B$. Si $A = B$ se dice **relación sobre $A$**, $R \subseteq A \times A = A^2$. Para indicar que $a$ y $b$ están relacionados valen tres escrituras equivalentes: $(a, b) \in R$, $R(a, b)$ y $a\,R\,b$; la tercera se llama **notación infija** y su negación se escribe $a \mathrel{\not R} b$.

Con $A = \{2, 3, 4\}$, $B = \{2, 6, 8\}$ y $x\,R\,y \iff x \mid y$ resulta

$$R = \{(2,2), (2,6), (2,8), (3,6), (4,8)\}.$$

El **dominio** es el conjunto de elementos de $A$ que aparecen como primera componente, $\mathrm{dom}(R) = \{a \mid \exists b\ (a, b) \in R\}$, y la **imagen** es el de las segundas componentes, $\mathrm{img}(R) = \{b \mid \exists a\ (a, b) \in R\}$. Aquí $\mathrm{dom}(R) = \{2, 3, 4\}$ e $\mathrm{img}(R) = \{2, 6, 8\}$. A diferencia de una función, un elemento puede estar relacionado con varios o con ninguno: el $2$ tiene tres imágenes.

## Tres relaciones sobre los naturales

- **Menor que**, $<$: $(1, 3) \in {<}$, pero $(10, 4) \notin {<}$ y $(7, 7) \notin {<}$.
- **Divide a**, $\mid$, sobre $\mathbb{N}$ sin el 0: $a \mid b$ si existe $k \in \mathbb{N}$ con $b = ka$. Así $3 \mid 9$ y $18 \mid 72$, pero $7 \nmid 9$.
- **Congruencia módulo $n$**, $\equiv_n$: $a \equiv_n b$ si $\lvert a - b \rvert$ es múltiplo de $n$. Con $n = 7$, $2 \equiv_7 23$ (diferencia $21$) y $8 \equiv_7 1$ (diferencia $7$), pero $19 \not\equiv_7 4$ (diferencia $15$).

En esta nota el símbolo $=$ dentro de $n_1 + n_2 = n_3$ es parte de la notación infija de la relación $+_{\mathbb{N}}$; no es la igualdad de conjuntos.

## Representaciones

Para $R$ de $A$ en $B$, el **diagrama de flechas** dibuja los dos conjuntos como óvalos y una flecha por cada par.

![Relación divide de A en B en diagrama de flechas](adjuntos/Relaci%C3%B3n%20divide%20de%20A%20en%20B%20en%20diagrama%20de%20flechas.png)

> [!example]- Transcripción de la imagen
> Dos óvalos: $A$ con los puntos $2, 3, 4$ y $B$ con los puntos $2, 6, 8$. Hay flechas de $2$ a $2$, de $2$ a $6$ y de $2$ a $8$; de $3$ a $6$; y de $4$ a $8$. Es la relación «divide a», con cinco pares.

Cuando $R$ es una relación **sobre un conjunto**, el diagrama se reemplaza por un **grafo dirigido**: cada elemento se dibuja una sola vez, una flecha $a \to b$ indica $a\,R\,b$ y un par $(a, a)$ se dibuja como un **bucle**. Si el conjunto es finito, también sirve la **matriz de la relación** $M_R$: se ordenan los elementos y $[M_R]_{ij} = 1$ si el $i$-ésimo está relacionado con el $j$-ésimo, y $0$ si no. Para $A = \{a, b, c, d, e\}$ y

$$R = \{(a,b), (b,b), (b,c), (c,b), (c,d), (d,a), (d,b), (d,c), (d,d), (d,e)\}$$

se obtiene, con filas y columnas en orden alfabético,

$$M_R = \begin{pmatrix} 0&1&0&0&0 \\ 0&1&1&0&0 \\ 0&1&0&1&0 \\ 1&1&1&1&1 \\ 0&0&0&0&0 \end{pmatrix}.$$

Cada representación destaca algo distinto: en el grafo se leen bucles y ciclos, y en la matriz se detecta una diagonal de unos (relación refleja) o una matriz igual a su traspuesta (relación simétrica). Solo la matriz exige que $A$ sea finito.

> [!warning] Una relación no es una función
> Una función exige exactamente una flecha de salida por cada elemento del dominio; una relación admite cero, una o varias. Por eso la inversa de una relación siempre existe, mientras que la inversa de una función no siempre es función.

## Preguntas de repaso

> [!question]- ¿Cuántas relaciones binarias hay sobre un conjunto de $n$ elementos y por qué?
> Hay $2^{n^2}$: cada relación es un subconjunto de $A^2$, que tiene $n^2$ pares, y cada par está o no está. Sobre 3 elementos son $512$.

> [!question]- ¿Qué se ve en la matriz de la relación $R$ del ejemplo sobre $\{a, \dots, e\}$ y qué no es?
> La fila de $e$ es toda ceros, así que $e$ no se relaciona con nada; y la diagonal no es toda unos ($a$ no está relacionado con $a$), luego $R$ no es refleja.

> [!question]- ¿Por qué se dibujan bucles en el grafo dirigido?
> Porque una flecha de $a$ a $b$ representa el par $(a, b)$, y si $a = b$ el par $(a, a)$ debe salir y llegar al mismo punto.

> [!question]- ¿Es $\equiv_n$ una relación sobre $\mathbb{N}$ aunque se defina con la resta?
> Sí: solo es un subconjunto de $\mathbb{N}^2$ con pares $(a, b)$ que cumplen que $\lvert a - b \rvert = kn$; la resta se usa únicamente para decidir qué pares pertenecen.
