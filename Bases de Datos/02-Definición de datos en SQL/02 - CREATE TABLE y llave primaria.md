---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SQL y PostgreSQL|SQL y PostgreSQL]]", "[[03 - Superllaves, claves candidatas y clave primaria|Superllaves, claves candidatas y clave primaria]]"]
---
# CREATE TABLE y llave primaria

`CREATE TABLE` define una relación: su nombre, sus atributos con su tipo y sus restricciones, entre ellas la **llave primaria** (`PRIMARY KEY`).

## Crear una tabla

```sql
CREATE TABLE Personas (
    id int,
    nombre varchar(255),
    edad int,
    PRIMARY KEY (id)
);
```

| ID | Nombre | Edad |
|---|---|---|
| 1 | Esteban | 21 |
| 2 | Monse | 22 |
| 3 | Mateo | 19 |

> [!tip] Complemento — formas de declarar la llave (slides "Clase 3")
> El esquema del curso: `Peliculas(id, nombre, año, categoria, calificacion, director)`, `Actores(id, nombre, edad)`, `Actuo_en(id_actor, id_pelicula)`.
> ```sql
> -- llave de un atributo: en la misma línea
> CREATE TABLE Peliculas(
>   id int PRIMARY KEY,
>   nombre varchar(30),
>   año int,
>   categoria varchar(30),
>   calificacion float,
>   director varchar(30)
> );
>
> -- llave compuesta: al final, con todos sus atributos
> CREATE TABLE Actuo_en(
>   id_actor int,
>   id_pelicula int,
>   PRIMARY KEY (id_pelicula, id_actor)
> );
> ```
> La llave primaria es una restricción de llave: sus valores son **únicos** y **no pueden ser nulos**.

> [!tip] Complemento — valores por defecto (slides "Clase 3")
> Sintaxis general: `CREATE TABLE <Nombre> (...<atr> tipo DEFAULT <valor>...)`
> ```sql
> CREATE TABLE Peliculas(
>   id int PRIMARY KEY,
>   nombre varchar(30),
>   año int,
>   categoria varchar(30) DEFAULT 'Acción',
>   calificacion float DEFAULT 0,
>   director varchar(30)
> );
> ```
> Si un `INSERT` no entrega `categoria`, queda `'Acción'`.

> [!tip] Complemento — surrogate key autogenerada (slides "Clase 6")
> En la práctica, casi siempre conviene una **surrogate key** autogenerada por el RDBMS. Los frameworks web modernos esperan una llave primaria llamada `id`, igual que [[04 - Modelos y Active Record|Active Record]] en Rails, que la crea en cada [[05 - Migraciones en Rails|migración]]:
> ```sql
> CREATE TABLE usuario(
>   id SERIAL,
>   email varchar(30) UNIQUE NOT NULL,
>   rut varchar(30) UNIQUE NOT NULL,
>   fecha date,
>   PRIMARY KEY (id)
> );
> ```
> `rut`, `email` o `username` serían *natural keys*: se mantienen con `UNIQUE NOT NULL` para no perder la restricción.

## Preguntas de repaso

1. Escribe el `CREATE TABLE` de `Personas(id, nombre, edad)` con `id` como llave primaria.
> [!question]- Respuesta
> `CREATE TABLE Personas (id int, nombre varchar(255), edad int, PRIMARY KEY (id));`

2. ¿Cómo se declara una llave primaria compuesta?
> [!question]- Respuesta
> Al final de la definición, con todos sus atributos: `PRIMARY KEY (id_pelicula, id_actor)`.

3. ¿Qué garantiza `PRIMARY KEY` sobre los valores de la columna?
> [!question]- Respuesta
> Que son únicos y que no pueden ser nulos.

4. ¿Para qué sirve `DEFAULT`?
> [!question]- Respuesta
> Para dar el valor que toma un atributo cuando un `INSERT` no lo especifica, por ejemplo `categoria varchar(30) DEFAULT 'Acción'`.
