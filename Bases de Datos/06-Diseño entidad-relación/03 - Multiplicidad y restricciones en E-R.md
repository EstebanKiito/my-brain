---
ramo: Bases de Datos
tema: Diseño entidad-relación
tags: [bd/diseño, bd/er, origen/complemento]
prerrequisitos: ["[[02 - Diagramas entidad-relación|Diagramas entidad-relación]]"]
---
# Multiplicidad y restricciones en E/R

La multiplicidad indica con **cuántas** entidades de un lado se puede relacionar cada entidad del otro (n a n, n a 1, 1 a 1). La **participación total** exige que toda entidad participe al menos una vez.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 5: Diseño de Bases de Datos")
> **Multiplicidades** de `Producto —fabrica— Compañía`:
> | Multiplicidad | Lectura |
> |---|---|
> | n a n | una compañía puede fabricar varios productos y un producto, ser fabricado por varias compañías |
> | n a 0 o 1 | un producto se fabrica **a lo más** por una compañía |
> | 0 o 1 a n | una compañía fabrica a lo más un producto (raro :S) |
> | 0 o 1 a 0 o 1 | a lo más uno de cada lado |
>
> Existen muchas convenciones distintas; **en el curso se usa la de la flecha**:
>
> ![Slide - convención de la flecha en ER](adjuntos/Slide%20-%20convención%20de%20la%20flecha%20en%20ER.png)
>
> - **Con la flecha** de Producto a `fabrica` ("esa es mi compañía"): la llave de `fabrica` es (la llave de) Producto, es decir, cada producto tiene **a lo más una** compañía.
> - La multiplicidad de los atributos es siempre a 1.

> [!note]- Transcripción de la imagen
> Producto (nombre, precio, categoría) → `fabrica` (atributo desde) — Compañía (nombre, valor-acción). Con la flecha: llave de la *fabrica* es (llave de) *Producto*. Multiplicidad de atributos es siempre a 1.

> [!tip] Complemento — participación (slides "Clase 5")
> ![Slide - participación y participación total](adjuntos/Slide%20-%20participación%20y%20participación%20total.png)
>
> | Notación | Significado |
> |---|---|
> | flecha delgada (n a 0 o 1) | un producto se fabrica **a lo más** por una compañía |
> | línea gruesa (n a 1 a n) | **participación total**: un producto se fabrica **al menos** en una compañía |
> | flecha gruesa (n a 1) | un producto se fabrica en **exactamente 1** compañía |
>
> **Equivalencia con la notación min-max** (Ramakrishnan): se anota `(mín, máx)` en cada lado.
>
> ![Slide - equivalencia de multiplicidades min-max](adjuntos/Slide%20-%20equivalencia%20de%20multiplicidades%20min-max.png)

> [!note]- Transcripción de las imágenes
> **Participación:** "n a 0 o 1: un producto se fabrica a lo más por una compañía"; "n a 1 a n: un producto se fabrica al menos en una compañía"; "n a 1: un producto se fabrica en exactamente 1 (sola) compañía".
>
> **Equivalencia** (Producto — compra — Persona, convención del curso → min-max):
> | Curso | Producto | Persona |
> |---|---|---|
> | línea simple | (0,n) | (0,n) |
> | flecha | (0,1) | (0,n) |
> | línea gruesa | (1,n) | (0,n) |
> | flecha gruesa | (1,1) | (0,n) |

> [!example] Ejemplo extra — cómo se traduce a SQL
> - **A lo más una** (flecha): llave foránea en Producto que admite `NULL`.
> - **Exactamente una** (flecha gruesa): llave foránea `NOT NULL`. Es la participación del profesor en [[07 - Restricciones de integridad y NOT NULL|Restricciones de integridad y NOT NULL]].
> - **n a n:** tabla intermedia (ver [[05 - Del modelo E-R al relacional|Del modelo E/R al relacional]]).

## Preguntas de repaso

1. ¿Qué significa una flecha de Producto hacia la relación `fabrica`?
> [!question]- Respuesta
> Que cada producto se relaciona con a lo más una compañía: la llave de `fabrica` es la llave de Producto.

2. ¿Qué es la participación total y cómo se dibuja?
> [!question]- Respuesta
> Que toda entidad del conjunto debe participar al menos una vez en la relación. Se dibuja con línea gruesa; con flecha gruesa significa "exactamente una".

3. Traduce "flecha gruesa" a notación min-max.
> [!question]- Respuesta
> (1,1) del lado de la entidad: cada producto participa exactamente una vez.

4. ¿Cómo implementas en SQL que un producto se fabrique en exactamente una compañía?
> [!question]- Respuesta
> Con una llave foránea hacia Compañía en la tabla Producto, declarada `NOT NULL`.
