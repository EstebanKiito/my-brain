---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - Transacciones|Transacciones]]"]
---
# COMMIT, ROLLBACK y SAVEPOINT

Los comandos SQL para controlar una transacción: `COMMIT` la confirma, `ROLLBACK` la deshace completa y `SAVEPOINT` marca un punto intermedio al que se puede volver con `ROLLBACK TO SAVEPOINT`.

## Transacciones en SQL
1. **Commit**

```sql
START TRANSACTION;
	SELECT a_nombre
	FROM Actores; 
COMMIT;

-- Fuera de un bloque de transacción, cada consulta
-- se confirma automáticamente (autocommit)
```

2. **Rollback**

```sql
START TRANSACTION; 
	UPDATE Actores
	SET bio = 'El mejor actor'
	WHERE nombre = 'Adrian Soto'; 
ROLLBACK;

-- ROLLBACK deshace toda la transacción
```

3. **SavePoints**

```sql
START TRANSACTION; 
	UPDATE Actores
	SET bio = 'El mejor actor' 
	WHERE nombre = 'Adrian Soto'; 
	SAVEPOINT MejorActor; 
		UPDATE Actores
		SET bio = 'El peor actor'
		WHERE nombre = 'Juan Reutter';
ROLLBACK TO SAVEPOINT MejorActor;

-- Se deshace solo lo posterior al SAVEPOINT (la bio de Juan Reutter);
-- el cambio a Adrian Soto sigue pendiente de COMMIT.
-- Útil para probar varios pasos y verificar condiciones.
```

> [!tip] Complemento (slides "Clase 11" y documentación de PostgreSQL)
> - **Autocommit:** si no se escribe `START TRANSACTION`, cada sentencia es su propia transacción y se confirma sola. Lo mismo ocurre al conectarse con un lenguaje de programación, según la librería.
> - **Tras `ROLLBACK TO SAVEPOINT MejorActor`:** se deshace solo el cambio a 'El peor actor'. La bio de Adrian Soto **sigue cambiada**, y la transacción sigue abierta: hay que terminarla con `COMMIT` (para guardar 'El mejor actor') o con `ROLLBACK`.
> - En PostgreSQL, el savepoint **no se borra** con `ROLLBACK TO` (sí con `RELEASE SAVEPOINT`), así que se puede volver a él varias veces. Los que sí se borran son los savepoints creados después de él.
> - Si una sentencia falla dentro de una transacción, PostgreSQL la marca como abortada y rechaza todo hasta el `ROLLBACK`.
>
> ```mermaid
> flowchart LR
>   S[START] --> U1["UPDATE Adrian = 'El mejor actor'"] --> SP((SAVEPOINT MejorActor)) --> U2["UPDATE Juan = 'El peor actor'"]
>   U2 -->|ROLLBACK TO SAVEPOINT| SP
>   SP --> C[COMMIT: queda solo el cambio de Adrian]
> ```

## Preguntas de repaso

1. ¿Qué diferencia hay entre `COMMIT` y `ROLLBACK`?
> [!question]- Respuesta
> `COMMIT` confirma y hace permanentes los cambios de la transacción. `ROLLBACK` los deshace todos.

2. Después de `ROLLBACK TO SAVEPOINT MejorActor`, ¿qué cambios quedan?
> [!question]- Respuesta
> Solo los anteriores al savepoint: la bio de Adrian Soto como 'El mejor actor'. El cambio a Juan Reutter se deshace y la transacción sigue abierta.

3. ¿Qué pasa si ejecutas un `UPDATE` sin `START TRANSACTION`?
> [!question]- Respuesta
> Con autocommit, el `UPDATE` es su propia transacción y se confirma automáticamente al terminar.

4. ¿Para qué sirven los savepoints?
> [!question]- Respuesta
> Para deshacer solo una parte de una transacción. Es útil cuando un programa hace varios pasos y verifica condiciones entre ellos.
