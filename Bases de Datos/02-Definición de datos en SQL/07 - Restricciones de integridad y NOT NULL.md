---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, bd/sql, origen/apuntes]
prerrequisitos: ["[[02 - CREATE TABLE y llave primaria|CREATE TABLE y llave primaria]]", "[[03 - Llaves foráneas|Llaves foráneas]]"]
---
# Restricciones de integridad y NOT NULL

Las restricciones de integridad son condiciones que el esquema impone y que **toda instancia** debe cumplir: no nulos, unicidad, llave, referencia y dominio. En SQL se declaran en el `CREATE TABLE`.

## Restricción de nulos

```sql
CREATE TABLE <Nombre> (
    id int NOT NULL
);
```

> [!tip] Complemento — tipos de restricciones (slides "Clase 6: Diseño de Bases de Datos II")
> | Restricción | Qué exige | En SQL |
> |---|---|---|
> | **De valores nulos** | el valor puede o no ser nulo | `NOT NULL` |
> | **Unicidad** | no puede haber dos tuplas con el mismo valor del atributo | `UNIQUE` |
> | **De llave** | el valor es único y no puede ser null | `PRIMARY KEY` |
> | **De referencia** | si alguien trabaja en una compañía, esta debe existir | `FOREIGN KEY … REFERENCES` |
> | **De dominio** | la edad de una persona debe estar entre 0 y 150 años | tipo de dato, `CHECK` |
>
> Además, `DEFAULT` da el valor cuando no se entrega uno.

> [!example] Ejemplo extra — todas juntas (slides "Clase 6")
> ```sql
> CREATE TABLE Profesor(
>   id int PRIMARY KEY,
>   nombre varchar(30) NOT NULL,
>   apellidos varchar(30) NOT NULL,
>   telefono varchar(30) NOT NULL,
>   id_universidad int NOT NULL,          -- participación total: todo profesor trabaja en una
>   nivel varchar(20) DEFAULT 'Pregrado',
>   FOREIGN KEY(id_universidad) REFERENCES Universidad(id)
> );
>
> CREATE TABLE Festival(
>   id int PRIMARY KEY,
>   nombre varchar(30) NOT NULL,
>   fecha_inicio date NOT NULL,
>   fecha_fin date NOT NULL,
>   precio int NOT NULL,
>   CHECK( precio BETWEEN 10000 AND 1000000 ),
>   CHECK( fecha_fin > fecha_inicio )
> );
> ```
> - **Participación:** si `id_universidad` admite `NULL`, un profesor puede estar sin trabajo. Con `NOT NULL`, todo profesor trabaja necesariamente en una única universidad.
> - **Entidad débil** (un equipo no existe sin su universidad): `id_universidad int NOT NULL` + `ON DELETE CASCADE`.
> - Cualquier `INSERT` o `UPDATE` que viole una restricción se rechaza completo.

> [!tip] Complemento — conexión con los nulos
> `NOT NULL` evita los problemas de la lógica de tres valores (`UNKNOWN`) en las columnas donde el dato siempre debe existir.

## Preguntas de repaso

1. ¿Qué hace `NOT NULL` en `id int NOT NULL`?
> [!question]- Respuesta
> Impide insertar o actualizar una fila dejando `id` sin valor. Todo `INSERT` debe darle un valor no nulo.

2. ¿Qué diferencia hay entre `UNIQUE` y `PRIMARY KEY`?
> [!question]- Respuesta
> Ambos impiden valores repetidos, pero `PRIMARY KEY` además prohíbe los nulos y solo puede haber una por tabla. `UNIQUE` puede haber varias y admite nulos.

3. ¿Cómo se restringe que el precio de un festival esté entre 10.000 y 1.000.000?
> [!question]- Respuesta
> Con una restricción de dominio: `CHECK( precio BETWEEN 10000 AND 1000000 )`.

4. ¿Cómo se expresa en SQL que todo profesor trabaja necesariamente en una universidad?
> [!question]- Respuesta
> Con una llave foránea `id_universidad` declarada `NOT NULL`, que referencia `Universidad(id)`.
