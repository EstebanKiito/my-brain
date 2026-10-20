---
ramo: Bases de Datos
tema: Modelo relacional
tags: [bd/modelo-relacional, bd/algebra, origen/apuntes]
prerrequisitos: ["[[02 - Modelo relacional|Modelo relacional]]"]
---
# Álgebra relacional

El álgebra relacional es el **lenguaje teórico** del modelo relacional: un conjunto de operadores que reciben tablas y devuelven tablas. Sobre ella se construyen SQL y la forma en que el DBMS ejecuta las consultas.

## Operadores
1. **Select (σ):** El operador Select se utiliza para seleccionar tuplas de una relación que satisfacen una condición dada. La condición se puede especificar utilizando operadores de comparación como =, <>, <, <=, >, >=.
2. **Project (π):** El operador Project se utiliza para seleccionar ciertos atributos (columnas) de una relación.
3. **Union (∪):** El operador Union combina las tuplas de dos relaciones y elimina las duplicadas. Las dos relaciones deben ser compatibles con la unión, es decir, deben tener el mismo número de atributos y los atributos correspondientes deben tener el mismo dominio.
4. **Set Difference (-):** El operador Set Difference elimina las tuplas de una relación que también aparecen en otra.
5. **Cartesian Product (x):** El operador Cartesian Product combina tuplas de dos relaciones.
6. **Rename (ρ):** El operador Rename cambia los nombres de las relaciones o los atributos.
7. **Join (⨝):** El operador Join combina las tuplas de dos relaciones que cumplen una condición (θ-join): $R_1 \bowtie_{condición} R_2 = \sigma_{condición}(R_1 \times R_2)$. El caso más común es una condición de igualdad (*equi-join*). Los *outer joins* (LEFT, RIGHT, FULL) son una extensión que se usa sobre todo en SQL.

## Notación formal

> [!tip] Complemento — definiciones de la clase (slides "Clase 2: Álgebra Relacional")
> Es un lenguaje teórico con operadores que reciben tablas y devuelven tablas. **El resultado de una consulta siempre es otra relación**, por eso los operadores se pueden anidar.
>
> | Operador | Notación | Resultado |
> |---|---|---|
> | Selección | $\sigma_{condición}(R)$ | las tuplas de R que cumplen la condición. Condiciones: $<, \le, \ge, >, =, \ne$, combinables con $\wedge, \vee$ |
> | Proyección | $\pi_{a_1,\dots,a_n}(R)$ | R solo con los atributos $a_1,\dots,a_n$ |
> | Unión | $R_1 \cup R_2$ | tuplas de $R_1$ o $R_2$ (misma cantidad y tipo de atributos) |
> | Diferencia | $R_1 - R_2$ | tuplas de $R_1$ que no están en $R_2$ |
> | Producto cruz | $R_1 \times R_2$ | todas las combinaciones; $\lvert R_1 \times R_2\rvert = \lvert R_1\rvert \cdot \lvert R_2\rvert$ |
> | Renombrar | $\rho(nuevo, R)$ o $\rho(a \to b, R)$ | cambia el nombre de la relación o de sus atributos |
> | Join | $R_1 \bowtie_{cond} R_2 = \sigma_{cond}(R_1 \times R_2)$ | no es un operador nuevo: se define con selección y producto cruz |
> | Intersección | $R_1 \cap R_2$ | definible con los anteriores: $R_1 \cap R_2 = R_1 - (R_1 - R_2)$ |
>
> **Observación:** como una relación es un conjunto, la proyección y la unión **no dejan duplicados**. Por ejemplo, $\pi_{año}(peliculas)$ muestra 2014 una sola vez.
>
> **Natural join:** si los atributos comunes se llaman igual, se omite la condición. Con $R(a,b)$ y $S(b,c)$, $R \bowtie S$ une por $R.b = S.b$.
>
> ![Slide - producto cruz en álgebra relacional](adjuntos/Slide%20-%20producto%20cruz%20en%20álgebra%20relacional.png)

> [!note]- Transcripción de la imagen
> **Producto Cruz.** Necesitamos poder cruzar información entre tablas. El operador × permite hacer el producto cartesiano de dos relaciones. Ejemplo: $R_1(A,B)$ con filas $(a_1,b_1)$ y $(a_2,b_2)$, y $R_2(A,C,D)$ con filas $(a_1,c_1,d_1)$ y $(a_2,c_2,d_2)$. $R_1 \times R_2$ tiene 4 filas con columnas $R_1.A, R_1.B, R_2.A, R_2.C, R_2.D$: cada fila de $R_1$ combinada con cada fila de $R_2$. **Observación:** la cardinalidad está dada por $|R_1 \times R_2| = |R_1| \cdot |R_2|$.

> [!example] Ejemplo extra — mismo pedido en álgebra y en SQL
> "Nombre y calificación de las películas con calificación inferior a 8.5":
> - Álgebra: $\pi_{nombre,\ calificacion}(\sigma_{calificacion < 8.5}(peliculas))$
> - SQL: `SELECT nombre, calificacion FROM peliculas WHERE calificacion < 8.5`
>
> σ corresponde al `WHERE`, π al `SELECT` y × al `FROM` con varias tablas. Ojo con los nombres: el `SELECT` de SQL es la **proyección** π, no la "selección" σ.

## Preguntas de repaso

1. ¿Qué hace la selección σ y qué hace la proyección π?
> [!question]- Respuesta
> σ deja las tuplas (filas) que cumplen una condición; π deja solo algunos atributos (columnas).

2. ¿Qué condición deben cumplir dos relaciones para unirlas con ∪ o restarlas con −?
> [!question]- Respuesta
> Deben ser compatibles: el mismo número de atributos y, en cada posición, el mismo dominio.

3. ¿Por qué se dice que el join no es un operador nuevo?
> [!question]- Respuesta
> Porque se define con los anteriores: $R_1 \bowtie_{cond} R_2 = \sigma_{cond}(R_1 \times R_2)$, es decir, un producto cruz seguido de una selección.

4. Si $|R_1| = 4$ y $|R_2| = 5$, ¿cuántas tuplas tiene $R_1 \times R_2$?
> [!question]- Respuesta
> $4 \cdot 5 = 20$ tuplas.

5. ¿A qué operador del álgebra corresponde el `SELECT` de SQL?
> [!question]- Respuesta
> A la proyección π. La selección σ corresponde al `WHERE`.
