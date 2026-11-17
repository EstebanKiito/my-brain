---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Relaciones binarias, dominio, imagen y representaciones]]"
---

# Relación inversa y composición de relaciones

Dos operaciones permiten construir relaciones nuevas a partir de otras: dar vuelta las flechas (**inversa**) y encadenarlas (**composición**). Son la base de las clausuras y de las caracterizaciones algebraicas de las propiedades de una relación.

## Relación inversa

Si $R \subseteq A \times B$, su **inversa** es $R^{-1} \subseteq B \times A$ con los pares invertidos:

$$R^{-1} = \{(b, a) \in B \times A \mid (a, b) \in R\}.$$

Con $R$ la relación «divide a» entre $A = \{2, 3, 4\}$ y $B = \{2, 6, 8\}$, se tiene $R = \{(2,2), (2,6), (2,8), (3,6), (4,8)\}$ y $R^{-1} = \{(2,2), (6,2), (8,2), (6,3), (8,4)\}$, que se lee «$y$ es múltiplo de $x$». En el diagrama de flechas basta copiar el de $R$ con las flechas al revés.

![Relación inversa de divide en diagrama de flechas](adjuntos/Relaci%C3%B3n%20inversa%20de%20divide%20en%20diagrama%20de%20flechas.png)

> [!example]- Transcripción de la imagen
> El óvalo de la izquierda es $A = \{2, 3, 4\}$ y el de la derecha $B = \{2, 6, 8\}$; una flecha curva rotulada $R^{-1}$ apunta de derecha a izquierda. Las flechas van de $2 \in B$ a $2 \in A$; de $6$ a $2$ y a $3$; y de $8$ a $2$ y a $4$. Son las mismas cinco flechas de la relación original, pero con la dirección invertida.

Siempre ocurre que $(R^{-1})^{-1} = R$. Además, la inversa permite expresar la simetría: $R$ es simétrica si y solo si $R = R^{-1}$.

## Composición

Dadas $R \subseteq A \times B$ y $S \subseteq B \times C$, la **composición** conecta lo que se alcanza pasando por un intermedio:

$$R \circ S = \{(a, c) \in A \times C \mid \exists b \in B\ \ (a, b) \in R \wedge (b, c) \in S\}.$$

Por ejemplo, si $R = \{(1,a), (1,b), (2,b), (3,c)\}$ y $S = \{(a,10), (b,20), (b,30), (d,40)\}$, entonces $R \circ S = \{(1,10), (1,20), (1,30), (2,20), (2,30)\}$: el $1$ llega a $10$ por $a$ y a $20, 30$ por $b$; el $2$ llega a $20, 30$ por $b$; el $3$ se pierde porque $c$ no sale en $S$, y $(d, 40)$ no se usa porque nadie llega a $d$. Sobre un solo conjunto se define la potencia $R^1 = R$ y $R^{i+1} = R^i \circ R$: el par $(x, y)$ está en $R^k$ cuando hay un camino de exactamente $k$ flechas de $x$ a $y$.

> [!warning] Orden de la composición
> En estas notas $R \circ S$ aplica primero $R$ y luego $S$. Algunas fuentes (y las funciones) lo escriben al revés, con $S$ primero. Conviene fijar la convención al leer un enunciado; en las afirmaciones simétricas (como $R_1 \circ R_2 = R_1 \cup R_2$ con $R_1, R_2$ de equivalencia) el resultado no cambia.

## Propiedades y matrices

Para relaciones cualesquiera valen:
- **Asociatividad:** $(R \circ S) \circ T = R \circ (S \circ T)$, así que $R^k$ no necesita paréntesis.
- **Inversa de una composición:** $(R \circ S)^{-1} = S^{-1} \circ R^{-1}$, igual que con funciones: se deshacen los pasos en orden inverso.
- **No conmutatividad:** con $R = \{(1,2)\}$ y $S = \{(2,3)\}$ sobre $\{1, 2, 3\}$ se tiene $R \circ S = \{(1,3)\}$ pero $S \circ R = \emptyset$.

Sobre un conjunto finito, con matrices de ceros y unos, la inversa corresponde a la **traspuesta**, $M_{R^{-1}} = M_R^{\top}$, y la composición al **producto de matrices con suma booleana** ($1 + 1 = 1$): $M_{R \circ S} = M_R \cdot M_S$. Con $R = \{(1,2), (2,3)\}$ sobre $\{1,2,3\}$,

$$M_R = \begin{pmatrix} 0&1&0 \\ 0&0&1 \\ 0&0&0 \end{pmatrix}, \qquad M_R^2 = \begin{pmatrix} 0&0&1 \\ 0&0&0 \\ 0&0&0 \end{pmatrix},$$

que corresponde a $R \circ R = \{(1, 3)\}$: un salto de dos pasos de $1$ a $3$.

## Preguntas de repaso

> [!question]- ¿Por qué $R^{-1}$ existe siempre, aunque $R$ no sea una función?
> Porque invertir pares no exige nada: $(a, b) \in R$ pasa a $(b, a) \in R^{-1}$. Una función solo es invertible como función si es biyectiva, pero como relación su inversa siempre existe.

> [!question]- ¿Qué significa que $(x, y)$ esté en $R^3$?
> Que existen $z_1, z_2$ con $(x, z_1), (z_1, z_2), (z_2, y) \in R$: hay un camino de exactamente tres flechas de $x$ a $y$.

> [!question]- ¿Por qué $(R \circ S)^{-1} = S^{-1} \circ R^{-1}$ y no $R^{-1} \circ S^{-1}$?
> Porque un camino $a \to b \to c$ invertido es $c \to b \to a$: primero se deshace $S$ y después $R$.

> [!question]- ¿Cómo se calcula $R \circ R$ con matrices y cuál es el riesgo?
> Se multiplica $M_R$ por sí misma con suma booleana. El riesgo es usar la suma usual: aparecerían entradas mayores que $1$ que cuentan caminos, no solo indican su existencia.
