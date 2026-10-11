---
ramo: Bases de Datos
tema: Diseño entidad-relación
tags: [bd/diseño, origen/complemento]
prerrequisitos: ["[[05 - Del modelo E-R al relacional|Del modelo E/R al relacional]]"]
---
# Principios de diseño de bases de datos

Reglas prácticas para un buen esquema: ser fiel al problema, evitar la redundancia (que causa anomalías), elegir bien entidades y relaciones, no complicar de más y escoger la llave primaria con criterio.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 6: Diseño de Bases de Datos II")
> 1. **Fidelidad al problema:** el diagrama debe reflejar la realidad. Ejemplos de la slide: un `Producto —compra— Persona` mal dirigido, o `País —Presidente— Persona` con multiplicidades que permiten varios presidentes por país.
> 2. **Evitar redundancia:** guardar el mismo dato en varios lugares genera **anomalías** de actualización, inserción y borrado (se ven en [[01 - Dependencias funcionales|Dependencias funcionales]]).
> 3. **Elegir entidades y relaciones correctamente:** por ejemplo, ¿la compañía es un atributo del producto o una entidad?
> 4. **No complicar más de lo necesario:** no agregar entidades o relaciones que no aportan.
> 5. **Elección de llave primaria:**
>    - Primero se identifican los atributos candidatos a llave, las **natural keys**. En `Usuario(email, rut, username, nombre, tipo, fecha_de_inscripcion)` lo son `rut`, `email` y `username`.
>    - "…pero en la práctica el 99% de las veces es mejor usar una columna inventada, sin significado, autogenerada por el RDBMS": la **surrogate key**. "Bueno, en realidad es algo medio opinionado…", pero los frameworks web modernos esperan una surrogate key `id` como llave primaria, e incluso la generan por defecto.
>    ```sql
>    CREATE TABLE usuario(
>      id SERIAL,
>      email varchar(30) UNIQUE NOT NULL,
>      rut varchar(30) UNIQUE NOT NULL,
>      fecha date,
>      PRIMARY KEY (id)
>    );
>    ```
>    (En la slide aparece `email nombre varchar(30)`, que es una errata: falta separar las columnas.)

## Ejemplo completo: vinos y cervezas

> [!example] Ejemplo extra — modelado paso a paso (slides "Clase 5")
> **Requisitos:** vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y ciudad-origen; cada cerveza tiene ciudad-origen, tipo y grados. Ambos tienen un precio unitario y una cantidad "en stock" cada día.
>
> Iteraciones de la clase y el problema que resolvió cada una:
> 1. Primer diagrama → **no hay llaves**.
> 2. Se agregan llaves → **repetición de atributos** entre Vino y Cerveza.
> 3. Jerarquía de clases `Bebida` → **¿cuál es la llave del stock?**
> 4. Se agregan multiplicidades → ¿qué pasa si cada bebida debe tener stock?, ¿y si solo se guarda el stock actual?
> 5. Con solo el stock actual, precio unitario y cantidad pasan a ser atributos de `Bebida`:
>
> ![Slide - modelo ER de vinos y cervezas](adjuntos/Slide%20-%20modelo%20ER%20de%20vinos%20y%20cervezas.png)

> [!note]- Transcripción de la imagen
> "Modelando vinos y cervezas con solo stock actual": Bebida (nombre subrayado, tipo, ciudad-origen, grados, precio-unitario, cantidad) con dos `IsA` hacia Vino (año) y Cerveza.

## Preguntas de repaso

1. ¿Qué problema trae la redundancia en un esquema?
> [!question]- Respuesta
> Anomalías: al actualizar un dato repetido hay que cambiarlo en todos lados (o queda inconsistente); además puede ser imposible insertar o borrar un hecho sin afectar a otro.

2. ¿Qué es una natural key y qué es una surrogate key?
> [!question]- Respuesta
> Una natural key es un atributo que naturalmente identifica, como rut o email. Una surrogate key es una columna inventada, sin significado, autogenerada (`id SERIAL`).

3. Si usas una surrogate key, ¿qué haces con las natural keys?
> [!question]- Respuesta
> Las mantienes con `UNIQUE NOT NULL`, para no perder la restricción de que son únicas.

4. En el ejemplo de vinos y cervezas, ¿qué problema resolvió la jerarquía de clases?
> [!question]- Respuesta
> La repetición de atributos comunes (tipo, grados, ciudad-origen) en Vino y Cerveza, que pasaron a la superclase Bebida.
