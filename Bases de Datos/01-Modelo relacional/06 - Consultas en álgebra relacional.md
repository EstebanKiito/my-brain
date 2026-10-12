---
ramo: Bases de Datos
tema: Modelo relacional
tags: [bd/modelo-relacional, bd/algebra, origen/complemento]
prerrequisitos: ["[[04 - Álgebra relacional|Álgebra relacional]]", "[[05 - Join en álgebra relacional|Join en álgebra relacional]]"]
---
# Consultas en álgebra relacional

Cómo se resuelven preguntas concretas combinando σ, π, ×, ⨝, ∪, −, ∩ y ρ sobre la base de películas del curso, y por qué algunas consultas necesitan la diferencia.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 1" y "Clase 2: Álgebra Relacional")
> **La instancia de la clase**
>
> `actores(id, nombre, edad)`: 1 Leonardo DiCaprio 41 · 2 Matthew McConaughey 46 · 3 Daniel Radcliffe 27 · 4 Jessica Chastain 39
>
> `actuo_en(id_actor, id_pelicula)`: (1,2) · (2,1) · (4,1) · (3,3) · (1,5)
>
> | id | nombre | año | categoria | calificacion | director |
> |---|---|---|---|---|---|
> | 1 | Interstellar | 2014 | SciFi | 8.6 | C. Nolan |
> | 2 | The Revenant | 2015 | Drama | 8.1 | A. Iñárritu |
> | 3 | Harry Potter | 2011 | Fantasía | 8.1 | D. Yates |
> | 4 | The Theory of Everything | 2014 | Biografía | 7.7 | J. Marsh |
> | 5 | Inception | 2010 | Adventure | 8.8 | C. Nolan |

> [!example] Ejemplo extra — consultas resueltas en clase
> | Pregunta | Álgebra relacional | Resultado |
> |---|---|---|
> | Nombre de todos los actores | $\pi_{nombre}(actores)$ | DiCaprio, McConaughey, Radcliffe, Chastain |
> | Películas de C. Nolan | $\sigma_{director = 'C. Nolan'}(peliculas)$ | Interstellar, Inception |
> | Calificación < 8.5 y de J. Marsh | $\sigma_{calificacion < 8.5 \wedge director = 'J. Marsh'}(peliculas)$ | The Theory of Everything |
> | Nombre y calificación con calificación < 8.5 | $\pi_{nombre,calificacion}(\sigma_{calificacion<8.5}(peliculas))$ | The Revenant, Harry Potter, The Theory of Everything |
> | Nombres de actores y directores | $\pi_{nombre}(actores) \cup \pi_{director}(peliculas)$ | los 4 actores + 4 directores |
> | id de los actores de "Interstellar" | $\pi_{id\_actor}(\sigma_{nombre='Interstellar'}(\sigma_{peliculas.id = actuo\_en.id\_pelicula}(peliculas \times actuo\_en)))$ | 2, 4 |
>
> En la unión, en rigor habría que renombrar `director` a `nombre` con ρ para que los atributos coincidan.

> [!tip] Complemento — renombrar (slides "Clase 2")
> - **Atributos:** $\rho(nombre \to name,\ año \to year,\ categoria \to category,\ calificacion \to rating,\ peliculas)$
> - **Relaciones**, para reutilizar un resultado: $\rho(actores\_jovenes, \sigma_{edad<30}(actores))$ y luego $\pi_{nombre}(actores\_jovenes)$.

## Intersección: actores dirigidos por Nolan **y** por Iñárritu
Primero se guardan resultados intermedios con ρ y luego se intersectan.

> [!tip] Complemento (slides "Clase 2")
> ![Slide - intersección de actores de Nolan e Iñárritu](adjuntos/Slide%20-%20intersección%20de%20actores%20de%20Nolan%20e%20Iñárritu.png)

> [!note]- Transcripción de la imagen
> $\rho(peliculas\_join,\ actuo\_en \bowtie_{peliculas.id=actuo\_en.id\_pelicula} peliculas \bowtie_{actores.id=actuo\_en.id\_actor} actores)$
>
> $\rho(peliculas\_nolan,\ \pi_{actores.id,actores.nombre}(\sigma_{pelicula.director="C.Nolan"}(peliculas\_join)))$
>
> $\rho(peliculas\_inarritu,\ \pi_{actores.id,actores.nombre}(\sigma_{pelicula.director="A.Iñarritu"}(peliculas\_join)))$
>
> $\pi_{nombre}(peliculas\_nolan \cap peliculas\_inarritu)$

Hacerlo con una sola selección, `director = 'C. Nolan' AND director = 'A. Iñárritu'`, **no funciona**: ninguna tupla tiene dos directores a la vez. Por eso se calculan los dos conjuntos por separado y se intersectan. Resultado: Leonardo DiCaprio.

## Diferencia: dirigidos por Nolan y **no** por Iñárritu

> [!tip] Complemento — consultas monótonas (slides "Clase 2")
> Sea $E$ una expresión de álgebra relacional sobre un esquema $S$. $E$ es **monótona** si para toda instancia $I, J$ sobre $S$, si $I \subseteq J$ entonces $E(I) \subseteq E(J)$: **si aumenta el tamaño de mi instancia, el resultado de mi consulta no disminuye**.
>
> **Teorema:** toda consulta que usa solo $\rho, \times, \sigma, \pi, \cup$ es monótona.
>
> "Dirigidos por Nolan y **no** por Iñárritu" **no es monótona**: si agrego una película de Iñárritu con un actor, ese actor desaparece del resultado. Entonces no se puede escribir sin la **diferencia** $R_1 - R_2$, que no es monótona.
>
> ![Slide - diferencia de actores de Nolan y no de Iñárritu](adjuntos/Slide%20-%20diferencia%20de%20actores%20de%20Nolan%20y%20no%20de%20Iñárritu.png)

> [!note]- Transcripción de la imagen
> Las mismas definiciones de $peliculas\_join$, $peliculas\_nolan$ y $peliculas\_inarritu$ que en la intersección, y al final: $\pi_{nombre}(peliculas\_nolan - peliculas\_inarritu)$.

## Preguntas de repaso

1. Escribe en álgebra relacional: "nombre y calificación de las películas con calificación inferior a 8.5".
> [!question]- Respuesta
> $\pi_{nombre,calificacion}(\sigma_{calificacion<8.5}(peliculas))$.

2. ¿Por qué no sirve $\sigma_{director='C. Nolan' \wedge director='A. Iñárritu'}$ para encontrar los actores dirigidos por ambos?
> [!question]- Respuesta
> Porque cada tupla tiene un solo director, así que ninguna cumple ambas condiciones. Hay que calcular por separado los actores de cada director y luego intersectar.

3. ¿Qué es una consulta monótona? Da un ejemplo de una que no lo sea.
> [!question]- Respuesta
> Una cuyo resultado nunca disminuye al agregar datos. "Actores dirigidos por Nolan y no por Iñárritu" no es monótona: al agregar una película de Iñárritu, un actor puede salir del resultado.

4. ¿Qué operadores garantizan que una consulta sea monótona y cuál rompe esa propiedad?
> [!question]- Respuesta
> ρ, ×, σ, π y ∪ dan siempre consultas monótonas. La diferencia − no es monótona.
