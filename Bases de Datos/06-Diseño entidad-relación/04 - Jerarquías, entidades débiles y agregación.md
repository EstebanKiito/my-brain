---
ramo: Bases de Datos
tema: Diseño entidad-relación
tags: [bd/diseño, bd/er, origen/complemento]
prerrequisitos: ["[[03 - Multiplicidad y restricciones en E-R|Multiplicidad y restricciones en E/R]]"]
---
# Jerarquías, entidades débiles y agregación

Tres construcciones avanzadas del modelo E/R: **jerarquías de clases** (IsA, como la herencia), **entidades débiles** (su llave depende de otra entidad) y **agregación** (tratar una relación como entidad).

## Jerarquía de clases (IsA)

> [!tip] Complemento — nota nueva (fuente: slides "Clase 5" y "Clase 6")
> Algunas entidades son casos especiales de otra, como la herencia en orientación a objetos: todo estudiante es también una persona.
>
> ![Slide - jerarquía de clases Bebida](adjuntos/Slide%20-%20jerarquía%20de%20clases%20Bebida.png)
>
> - Los atributos de la superclase (`Bebida`: nombre, origen, tipo) **se heredan** a las subclases (`Vino`, `Cerveza`).
> - **Las subclases no pueden tener llaves:** usan la de la superclase. `Vino` agrega `año`.
> - **Solapamiento:** una bebida puede ser vino y cerveza a la vez; **no solapamiento:** no puede.
> - **Cobertura:** toda bebida es vino o cerveza; **sin cobertura:** existen otras (whisky, pisco…).

> [!note]- Transcripción de la imagen
> Superclase Bebida (origen, nombre, tipo) con dos `isA` hacia las subclases Vino (año) y Cerveza. Globos: "Los atributos de bebida se heredan por vino y cerveza", "Las subclases no pueden tener llaves".

## Entidades débiles

> [!tip] Complemento (slides "Clase 5")
> Son entidades **cuya llave depende de la llave de otra entidad**. Una evaluación ("I1") no se identifica sola: hay una "I1" en cada curso.
>
> ![Slide - entidad débil Evaluación de Curso](adjuntos/Slide%20-%20entidad%20débil%20Evaluación%20de%20Curso.png)
>
> - Se dibujan con **borde grueso**, igual que su relación identificadora (`de`), que tiene **participación total n a 1**.
> - `nombre` es una **llave parcial** (subrayado punteado). La llave de Evaluación es el par **(código, nombre)**.
> - Se pueden encadenar: `Nota` es débil respecto de `Evaluación`, con llave (código, nombre, pregunta, rut).
> - No hay que repetir datos de otra entidad dentro de la débil (por ejemplo, el nombre del alumno en cada nota): eso es redundante con el rut. Mejor se relaciona `Nota` con `Alumno`.

> [!note]- Transcripción de la imagen
> Evaluación (fecha, nombre = llave parcial) con borde grueso → `de` → Curso (código, nombre). "Participación total (n a 1)". "La llave de Evaluación es el par (código, nombre)". "¿Y las notas?…"

## Agregación

> [!tip] Complemento (slides "Clase 5")
> Queremos registrar las películas que tiene un local de videos y su **precio por noche**, y que una persona alquile **películas de un local que efectivamente las tiene**. Pero las relaciones son entre entidades: Persona no puede relacionarse con la relación `tiene`.
>
> **Solución:** encapsular la relación y sus entidades en una **entidad virtual** (agregación) y relacionar Persona con ella mediante `alquila`.
>
> ![Slide - agregación de la relación tiene](adjuntos/Slide%20-%20agregación%20de%20la%20relación%20tiene.png)

> [!note]- Transcripción de la imagen
> Recuadro punteado que encierra Película (código, nombre) — `tiene` (precio_por_noche) — Local de Videos (código, nombre). Desde el recuadro sale `alquila` (hasta) hacia Persona (rut, nombre). "Encapsulamos la relación y sus correspondientes entidades en una entidad virtual."

El paso de cada construcción a tablas está en [[05 - Del modelo E-R al relacional|Del modelo E/R al relacional]].

## Preguntas de repaso

1. ¿Qué heredan las subclases de una jerarquía IsA y qué no pueden tener?
> [!question]- Respuesta
> Heredan todos los atributos de la superclase, incluida su llave. No pueden tener una llave propia.

2. ¿Qué diferencia hay entre cobertura y solapamiento?
> [!question]- Respuesta
> La cobertura indica si toda entidad de la superclase pertenece a alguna subclase. El solapamiento indica si una entidad puede pertenecer a varias subclases a la vez.

3. ¿Qué es una entidad débil y cuál es la llave de Evaluación?
> [!question]- Respuesta
> Una entidad cuya llave depende de la llave de otra entidad, con la que tiene participación total n a 1. La llave de Evaluación es (código del curso, nombre), donde nombre es la llave parcial.

4. ¿Cuándo hace falta una agregación?
> [!question]- Respuesta
> Cuando se quiere relacionar una entidad con una relación, por ejemplo Persona alquila la "película que tiene un local". Se encapsula la relación como entidad virtual.
