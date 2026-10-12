---
ramo: Bases de Datos
tema: Modelo relacional
tags: [bd/modelo-relacional, bd/algebra, origen/apuntes]
prerrequisitos: ["[[04 - Álgebra relacional|Álgebra relacional]]"]
---
# Join en álgebra relacional

El join ⨝ combina las tuplas de dos relaciones que cumplen una condición, por ejemplo que un atributo común sea igual. Es la operación para cruzar información entre tablas.

## Ejemplo (mis apuntes)
Si tenemos dos relaciones R1(A, B) y R2(B, C) con los siguientes datos:

| R1 | | R2 | |
|---|---|---|---|
| A | B | B | C |
| 1 | 2 | 2 | 20 |
| 3 | 4 | 4 | 40 |
| 5 | 6 | 6 | 60 |
| 7 | 8 | 8 | 80 |
| 9 | 10 | 10 | 100 |
| | | 12 | 120 |

Si queremos combinar las dos relaciones basándonos en una condición de igualdad en el atributo B, usaríamos el siguiente operador:

$$R1 \bowtie_{R1.B = R2.B} R2$$

`R1 ⨝{R1.B = R2.B} R2`

Esto nos devolvería la siguiente relación:

| A | B | C |
|---|---|---|
| 1 | 2 | 20 |
| 3 | 4 | 40 |
| 5 | 6 | 60 |
| 7 | 8 | 80 |
| 9 | 10 | 100 |

> [!tip] Complemento — cómo se calcula (slides "Clase 2: Álgebra Relacional")
> El join se define como **producto cruz + selección**: $R1 \bowtie_{R1.B = R2.B} R2 = \sigma_{R1.B = R2.B}(R1 \times R2)$.
>
> ```mermaid
> flowchart LR
>   X["R1 × R2<br/>5 · 6 = 30 tuplas"] -->|"σ R1.B = R2.B"| S["5 tuplas que calzan"] -->|"una sola columna B"| J["resultado A, B, C"]
> ```
>
> - Con un θ-join "puro" el resultado tiene las dos columnas `R1.B` y `R2.B`, con valores iguales. La tabla de mis apuntes muestra una sola columna B, que es lo que hace el **natural join** $R1 \bowtie R2$: como el atributo común se llama igual, se omite la condición y se deja una sola copia.
> - La tupla `(12, 120)` de R2 **no aparece**, porque ninguna tupla de R1 tiene B = 12. Si se quisiera conservarla con A nulo, haría falta un *right outer join*.

> [!example] Ejemplo extra — el join del curso
> En la clase el ejemplo es "liste cada actor junto a todas las películas en las que ha actuado":
> $$\pi_{actores.nombre,\ peliculas.nombre}(actuo\_en \bowtie_{peliculas.id = actuo\_en.id\_pelicula} peliculas \bowtie_{actores.id = actuo\_en.id\_actor} actores)$$
> Se encadenan dos joins porque la relación muchos a muchos `actuo_en` está entre `actores` y `peliculas`.

## Preguntas de repaso

1. ¿Qué tuplas devuelve `R1 ⨝{R1.B = R2.B} R2`?
> [!question]- Respuesta
> Las combinaciones de una tupla de R1 con una de R2 que tienen el mismo valor de B. En el ejemplo son 5: (1,2,20), (3,4,40), (5,6,60), (7,8,80) y (9,10,100).

2. ¿Por qué no aparece la tupla (12, 120) en el resultado?
> [!question]- Respuesta
> Porque no hay ninguna tupla en R1 con B = 12. El join interno solo deja las tuplas que tienen pareja en la otra relación.

3. Escribe el join usando solo producto cruz y selección.
> [!question]- Respuesta
> $\sigma_{R1.B = R2.B}(R1 \times R2)$.

4. ¿Qué diferencia hay entre este join y un natural join?
> [!question]- Respuesta
> El natural join iguala automáticamente los atributos con el mismo nombre y deja una sola copia de cada uno. El join con condición explícita conserva `R1.B` y `R2.B` como columnas separadas.
