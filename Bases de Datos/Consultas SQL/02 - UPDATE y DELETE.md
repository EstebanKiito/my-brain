---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# UPDATE y DELETE

`UPDATE` modifica valores de filas existentes y `DELETE` borra filas. Ambos usan un `WHERE` para elegir qué filas afectar. Junto con `INSERT` y `SELECT`, completan el CRUD.

## Mis apuntes
4. **UPDATE:** Modifica los datos existentes en una tabla. Por ejemplo, `UPDATE Personas SET edad = 30 WHERE nombre = 'Esteban';` actualizará la edad de Esteban a 30 en la tabla Personas.
5. **DELETE:** Elimina registros existentes en una tabla. Por ejemplo, `DELETE FROM Personas WHERE nombre = 'Esteban';` eliminará todos los registros de la tabla Personas donde el nombre sea 'Esteban'.
    - Es importante tener cuidado al usar el comando DELETE, ya que si se omite la cláusula WHERE, se eliminarán todos los registros de la tabla.

- **UPDATE:**

```sql
UPDATE Personas SET edad = 30 WHERE nombre = 'Esteban';
```

Esta consulta actualizaría la edad de Esteban a 30 en la tabla Personas. La tabla se vería así:

| ID | Nombre | Edad |
|---|---|---|
| 1 | Esteban | 30 |
| 2 | Monse | 22 |
| 3 | Mateo | 19 |

- **DELETE:**

```sql
DELETE FROM Personas WHERE nombre = 'Esteban';
```

Esta consulta eliminaría todos los registros de la tabla Personas donde el nombre sea 'Esteban'. La tabla quedaría así:

| ID | Nombre | Edad |
|---|---|---|
| 2 | Monse | 22 |
| 3 | Mateo | 19 |

> [!tip] Complemento — forma general (slides "Clase 3")
> ```sql
> UPDATE R
> SET atributo1 = nuevoValor1, …, atributon = nuevoValorn
> WHERE <Condición sobre R>;
>
> DELETE FROM R
> WHERE <Condición sobre R>;
> ```
> Ejemplo de la clase: `UPDATE Peliculas SET calificacion = 0 WHERE name = 'Sharknado 6'`.

> [!warning] Complemento — el error clásico (slides "Clase 3")
> ¿Qué pasa si se nos olvida el `WHERE`, o si se nos pasa un `;` entre medio?
> ```sql
> UPDATE Users
> SET password = 'contraseña';          -- ← este ; termina la sentencia
> WHERE email = 'some@email.com'
>
> DELETE FROM Tweets;                   -- ← igual aquí
> WHERE user_name = 'realDonaldTrump'
> ```
> **¡Se borran o actualizan todas las filas!** La línea con el `WHERE` queda como una sentencia aparte, inválida. Para protegerse, se prueba antes con un `SELECT` usando el mismo `WHERE`, o se trabaja dentro de una transacción que se pueda deshacer con `ROLLBACK`.

> [!example] Ejemplo extra — UPDATE con expresión
> ```sql
> UPDATE Personas SET edad = edad + 1;               -- todos cumplen años
> UPDATE Productos SET precio = precio * 1.1 WHERE fabricante = 'Toyota';
> ```

## Preguntas de repaso

1. ¿Qué hace `UPDATE Personas SET edad = 30 WHERE nombre = 'Esteban'`?
> [!question]- Respuesta
> Cambia a 30 la edad de todas las filas cuyo nombre es 'Esteban'. Las demás filas no cambian.

2. ¿Qué pasa si ejecutas `DELETE FROM Personas;` sin `WHERE`?
> [!question]- Respuesta
> Se eliminan todos los registros de la tabla. La tabla sigue existiendo, pero queda vacía.

3. ¿Por qué es peligroso un `;` antes del `WHERE` en un `UPDATE`?
> [!question]- Respuesta
> Porque termina la sentencia antes de tiempo: el `UPDATE` se ejecuta sin condición sobre todas las filas, y el `WHERE` queda suelto como otra sentencia.

4. ¿Cómo te proteges antes de un `DELETE` grande?
> [!question]- Respuesta
> Corriendo primero un `SELECT` con el mismo `WHERE` para ver qué filas se afectarían, o haciéndolo dentro de una transacción para poder deshacerlo con `ROLLBACK`.
