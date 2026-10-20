---
ramo: Bases de Datos
tema: Lógica en la base de datos
tags: [bd/logica, bd/sql, origen/apuntes]
prerrequisitos: ["[[02 - Vistas materializadas|Vistas materializadas]]", "[[02 - UPDATE y DELETE|UPDATE y DELETE]]"]
---
# Triggers

Un trigger es un procedimiento que la base de datos ejecuta **automáticamente** cuando ocurre un evento (`INSERT`, `UPDATE` o `DELETE`) en una tabla: antes, después o en lugar de la operación.

## Triggers
**Definición y funcionamiento**
- Los triggers son procedimientos que se ejecutan automáticamente en respuesta a ciertos eventos en la base de datos.
- Se pueden ejecutar antes o después de eventos como `INSERT`, `UPDATE` o `DELETE`.

**Tipos de triggers**
- **BEFORE:** Antes de la operación.
- **AFTER:** Después de la operación.
- **INSTEAD OF:** En lugar de la operación.
- Ejemplo: `BEFORE INSERT`, `AFTER UPDATE`. (`CREATE` no es un evento de trigger.)

**Observación:** el trigger se ejecuta:
1. una vez por cada **fila** afectada por el evento: `FOR EACH ROW`;
2. una sola vez por evento: `FOR EACH STATEMENT`.

**Ejemplo de Trigger**
Reducir el stock de un producto cada vez que se crea una venta. Esta es la sintaxis genérica de la slide; en PostgreSQL el trigger llama a una función (ver [[04 - Trigger para descontar stock en PLpgSQL|la versión completa]]).

```sql
CREATE TRIGGER reducir_stock
AFTER INSERT ON Ventas
FOR EACH ROW
BEGIN
  UPDATE Productos
  SET stock = Productos.stock - 1
  WHERE NEW.id_producto = Productos.id;
END;
```

### Ejemplo de actualizar vistas materializadas

En PostgreSQL, el trigger llama a una función que hace el refresco. El evento es cualquier cambio en `Evaluaciones`:

```sql
CREATE OR REPLACE FUNCTION refrescar_peleval() RETURNS TRIGGER AS $$
BEGIN
  REFRESH MATERIALIZED VIEW PelEval;
  RETURN NULL;   -- en triggers FOR EACH STATEMENT el valor de retorno se ignora
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER refresh_eval
AFTER INSERT OR UPDATE OR DELETE ON Evaluaciones
FOR EACH STATEMENT
EXECUTE FUNCTION refrescar_peleval();
```

> [!tip] Complemento (slides "Clase 8" y documentación de PostgreSQL)
> - Los triggers ayudan a **forzar restricciones más complejas** que un `CHECK` y a mantener la consistencia de la BD (como stock o vistas materializadas al día).
> - Dentro de un trigger `FOR EACH ROW`, **`NEW`** es la fila nueva (en INSERT y UPDATE) y **`OLD`** la anterior (en UPDATE y DELETE).
> - Un trigger `BEFORE … FOR EACH ROW` puede modificar `NEW` antes de que se guarde, o cancelar la operación devolviendo `NULL`.
> - `INSTEAD OF` se usa sobre **vistas**, para que se puedan "actualizar".
> - El ejemplo completo en PostgreSQL está en [[04 - Trigger para descontar stock en PLpgSQL|Trigger para descontar stock en PL/pgSQL]].

## Preguntas de repaso

1. ¿Qué es un trigger y qué eventos lo pueden gatillar?
> [!question]- Respuesta
> Un procedimiento que se ejecuta automáticamente ante un evento en una tabla: INSERT, UPDATE o DELETE.

2. ¿Qué diferencia hay entre `FOR EACH ROW` y `FOR EACH STATEMENT`?
> [!question]- Respuesta
> `FOR EACH ROW` ejecuta el trigger una vez por cada fila afectada. `FOR EACH STATEMENT` lo ejecuta una sola vez por sentencia, aunque afecte muchas filas.

3. ¿Qué representan `NEW` y `OLD`?
> [!question]- Respuesta
> `NEW` es la fila nueva (INSERT y UPDATE) y `OLD` la fila anterior (UPDATE y DELETE), dentro de un trigger por fila.

4. ¿Por qué `AFTER CREATE ON Evaluaciones` es incorrecto?
> [!question]- Respuesta
> Porque CREATE no es un evento de trigger. Insertar filas es `INSERT`, así que debería ser `AFTER INSERT ON Evaluaciones`.
