---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, bd/sql, origen/apuntes]
prerrequisitos: ["[[03 - Llaves foráneas|Llaves foráneas]]", "[[05 - INSERT e integridad referencial|INSERT e integridad referencial]]"]
---
# Eliminación con llaves foráneas

Al borrar una fila referenciada por una llave foránea hay que decidir qué pasa con las filas que apuntan a ella: impedir el borrado (lo que SQL hace por defecto), borrarlas en cascada (`ON DELETE CASCADE`) o dejarlas en nulo (`ON DELETE SET NULL`).

## Eliminación con llaves foráneas (mis apuntes)
Supongamos que tenemos las siguientes tablas de 'Autores' y 'Libros':

```sql
CREATE TABLE Autores (
    id int,
    nombre varchar(255),
    edad int,
    PRIMARY KEY (id)
);

CREATE TABLE Libros (
    id int,
    titulo varchar(255),
    id_autor int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_autor) REFERENCES Autores(id)
);
```

| Autores | | | Libros | | |
|---|---|---|---|---|---|
| id | nombre | edad | id | titulo | id_autor |
| 1 | Gabriel Garcia Marquez | 87 | 1 | Cien años de soledad | 1 |
| 2 | Julio Cortázar | 69 | 2 | Rayuela | 2 |
| 3 | Carlos Ruiz Zafón | 55 | 3 | La sombra del viento | 3 |
| | | | 4 | El amor en los tiempos del cólera | 1 |

Si intentamos ejecutar la siguiente consulta para eliminar al autor 'Gabriel Garcia Marquez':

```sql
DELETE FROM Autores WHERE nombre = 'Gabriel Garcia Marquez';
```

Recibiríamos un error, ya que existen libros en la tabla 'Libros' que están haciendo referencia al 'id' del autor 'Gabriel Garcia Marquez' a través de la llave foránea 'id_autor'.

Para poder eliminar a este autor, primero tendríamos que eliminar todos los libros asociados a él en la tabla 'Libros'.

Existen varias opciones para manejar este problema:

1. **Propagar la eliminación (Cascada de eliminaciones):** En este caso, al eliminar una tupla en la tabla 'Autores', también se eliminarán todas las tuplas en la tabla 'Libros' que hacen referencia a ella. Esto se puede hacer añadiendo la cláusula ON DELETE CASCADE a la definición de la llave foránea en la tabla 'Libros'. De esta manera, si borramos un autor de la tabla 'Autores', todos sus libros correspondientes en la tabla 'Libros' también serán borrados automáticamente.

```sql
CREATE TABLE Autores (
    id int,
    nombre varchar(255),
    edad int,
    PRIMARY KEY (id)
);

CREATE TABLE Libros (
    id int,
    titulo varchar(255),
    id_autor int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_autor) REFERENCES Autores(id) ON DELETE CASCADE
);
```

2. **Dejar en nulo:** Otra opción es configurar la llave foránea en la tabla 'Libros' para que se establezca en NULL cuando se elimina la tupla correspondiente en la tabla 'Autores'. Esto se puede hacer añadiendo la cláusula ON DELETE SET NULL a la definición de la llave foránea en la tabla 'Libros'. De esta manera, si borramos un autor de la tabla 'Autores', el campo 'id_autor' de todos sus libros correspondientes en la tabla 'Libros' se establecerá en NULL.

```sql
CREATE TABLE Autores (
    id int,
    nombre varchar(255),
    edad int,
    PRIMARY KEY (id)
);

CREATE TABLE Libros (
    id int,
    titulo varchar(255),
    id_autor int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_autor) REFERENCES Autores(id) ON DELETE SET NULL
);
```

Es importante tener en cuenta que estas opciones deben usarse con cuidado, ya que pueden tener implicaciones significativas en la integridad de los datos en la base de datos.

> [!tip] Complemento — las tres opciones (slides "Clase 6") y qué pasa al borrar a García Márquez (id 1)
> | Opción | Cláusula | Resultado en `Libros` |
> |---|---|---|
> | **No permitir** (default en SQL) | *(nada)* o `ON DELETE NO ACTION` / `RESTRICT` | error; no se borra nada |
> | **Propagar** | `ON DELETE CASCADE` | se borran los libros 1 y 4 |
> | **Dejar en nulo** | `ON DELETE SET NULL` | los libros 1 y 4 quedan con `id_autor = NULL` |
>
> - `CASCADE` es típico en **entidades débiles**, que no existen sin su dueño. Por ejemplo, las evaluaciones de un curso borrado: `FOREIGN KEY(codigo) REFERENCES curso(codigo) ON DELETE CASCADE`.
> - `SET NULL` no funciona si la columna es `NOT NULL`.
> - Lo mismo existe para cambios de llave: `ON UPDATE CASCADE`, `ON UPDATE SET NULL`.

## Preguntas de repaso

1. ¿Por qué falla `DELETE FROM Autores WHERE nombre = 'Gabriel Garcia Marquez'` con la definición original?
> [!question]- Respuesta
> Porque hay libros cuya llave foránea `id_autor` apunta a ese autor, y por defecto SQL no permite dejar referencias a filas inexistentes.

2. ¿Qué hace `ON DELETE CASCADE`?
> [!question]- Respuesta
> Al borrar la fila referenciada, borra automáticamente todas las filas que la referencian; aquí, todos los libros del autor.

3. ¿Qué hace `ON DELETE SET NULL` y cuándo no se puede usar?
> [!question]- Respuesta
> Deja en `NULL` la llave foránea de las filas que apuntaban a la fila borrada. No se puede usar si la columna está declarada `NOT NULL`.

4. ¿Cuál es el comportamiento por defecto si no se indica ninguna cláusula?
> [!question]- Respuesta
> No permitir la eliminación: el `DELETE` da error mientras existan filas que referencien la tupla.
