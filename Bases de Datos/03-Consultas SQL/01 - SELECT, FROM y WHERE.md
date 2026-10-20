---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[02 - CREATE TABLE y llave primaria|CREATE TABLE y llave primaria]]", "[[04 - Álgebra relacional|Álgebra relacional]]"]
---
# SELECT, FROM y WHERE

La forma básica de toda consulta SQL: `SELECT` elige las columnas, `FROM` indica las tablas y `WHERE` filtra las filas que cumplen una condición.

## Cláusulas básicas
1. **SELECT:** Selecciona datos de una base de datos. Los datos devueltos se almacenan en una tabla de resultados, llamada conjunto de resultados. Por ejemplo, `SELECT nombre FROM Personas;` seleccionará todos los nombres de la tabla Personas.
2. **FROM:** Se utiliza para especificar la tabla de la que se obtendrán los datos. Por ejemplo, en la consulta anterior, Personas es la tabla especificada con FROM.
3. **WHERE:** Filtra registros. Extrae solo aquellos registros que cumplen una condición especificada. Por ejemplo, `SELECT * FROM Personas WHERE edad > 20;`
    - WHERE en SQL permite el uso de los siguientes operadores:
        - `=`: Igual que.
        - `<>` o `!=`: Diferente que.
        - `<` y `>`: Menor que y mayor que.
        - `<=`: Menor o igual que.
        - `>=`: Mayor o igual que.
        - **AND:** Operador lógico AND. Selecciona registros donde dos o más condiciones deben ser verdaderas.
        - **OR:** Operador lógico OR. Selecciona registros donde al menos una de las condiciones debe ser verdadera.
        - **NOT:** Operador lógico NOT. Selecciona registros donde una condición debe ser falsa.
        - **IN:** Permite especificar múltiples valores en una cláusula WHERE.
        - **BETWEEN:** Selecciona valores dentro de un rango. Los valores pueden ser números, texto o fechas.

Los comandos UPDATE y DELETE están en [[02 - UPDATE y DELETE|UPDATE y DELETE]].

### Ejemplos sobre `Personas`
- **SELECT:**

```sql
SELECT nombre FROM Personas;
```

Esto seleccionaría todos los nombres de la tabla Personas y los mostraría como sigue:

| Nombre |
|---|
| Esteban |
| Monse |
| Mateo |

- **FROM:**

```sql
SELECT nombre, edad FROM Personas;
```

Esta consulta seleccionaría los nombres y las edades de la tabla Personas y los mostraría así:

| Nombre | Edad |
|---|---|
| Esteban | 21 |
| Monse | 22 |
| Mateo | 19 |

- **WHERE:**

```sql
SELECT * FROM Personas WHERE edad > 20;
```

Esta consulta seleccionaría todos los registros de la tabla Personas donde la edad sea mayor a 20 y los mostraría de esta forma:

| ID | Nombre | Edad |
|---|---|---|
| 1 | Esteban | 21 |
| 2 | Monse | 22 |

> [!tip] Complemento — forma general y traducción al álgebra (slides "Clase 3")
> ```sql
> SELECT a_1, …, a_n
> FROM T_1, …, T_m
> WHERE <condicion>
> ```
> equivale a $\pi_{a_1,\dots,a_n}(\sigma_{condicion}(T_1 \times \dots \times T_m))$. `SELECT *` deja todas las columnas.
>
> Ejemplos de la clase:
> ```sql
> SELECT nombre, calificacion FROM Peliculas WHERE director = 'C. Nolan';
> SELECT * FROM Peliculas WHERE año >= 2010;
> SELECT * FROM Peliculas WHERE año BETWEEN 1971 AND 1978;   -- extremos incluidos
> SELECT * FROM Peliculas WHERE año IN (1971, 1973, 2001);
> ```
> Los strings van entre comillas **simples** rectas (`'C. Nolan'`). Las comillas dobles son para nombres de columnas o tablas.

> [!tip] Complemento — orden lógico de evaluación
> Aunque se escribe `SELECT … FROM … WHERE`, el DBMS lo evalúa así: **FROM** (arma el producto de las tablas) → **WHERE** (filtra filas) → **SELECT** (proyecta columnas). Por eso en el `WHERE` no se puede usar un alias definido en el `SELECT`.

## Preguntas de repaso

1. ¿Qué hace cada cláusula en `SELECT nombre FROM Personas WHERE edad > 20`?
> [!question]- Respuesta
> `FROM` indica la tabla (Personas), `WHERE` deja solo las filas con edad mayor que 20 y `SELECT` muestra solo la columna nombre.

2. Traduce `SELECT a FROM T WHERE c` al álgebra relacional.
> [!question]- Respuesta
> $\pi_a(\sigma_c(T))$.

3. ¿Qué diferencia hay entre `BETWEEN 1971 AND 1978` e `IN (1971, 1978)`?
> [!question]- Respuesta
> `BETWEEN` acepta cualquier valor del rango, extremos incluidos. `IN` acepta solo los valores de la lista, en este caso 1971 y 1978.

4. ¿Qué devuelve `SELECT * FROM Personas WHERE edad > 20` en el ejemplo?
> [!question]- Respuesta
> Las filas de Esteban (21) y Monse (22), con todas sus columnas.
