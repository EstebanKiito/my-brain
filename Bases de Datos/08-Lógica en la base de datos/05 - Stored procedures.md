---
ramo: Bases de Datos
tema: Lógica en la base de datos
tags: [bd/logica, bd/sql, origen/apuntes]
prerrequisitos: ["[[04 - Trigger para descontar stock en PLpgSQL|Trigger para descontar stock en PL/pgSQL]]"]
---
# Stored procedures

Un stored procedure es una **función guardada en el DBMS** (en PostgreSQL, escrita en PL/pgSQL) que agrupa varias sentencias SQL, con variables, IFs y loops, y se ejecuta como una unidad.

## Stored procedures (mis apuntes)
**Definición y funcionamiento**
- Los stored procedures son conjuntos de comandos SQL que se almacenan en la base de datos y pueden ser ejecutados como una unidad.

**Ventajas de usar stored procedures**
- **Velocidad:** Optimizadas para ejecución rápida.
- **Seguridad:** Controlan el acceso a datos y lógica.
- **Reutilizabilidad:** Una vez definidos, pueden ser reutilizados múltiples veces.

**Desventaja principal:**
- Dificultad o imposibilidad de migrar a otra base de datos
- El testing sea mucho más difícil
- hace que sea más difícil mantener el código, porque SQL tiende a ser menos legible a medida que se vuelve más complejo.

**Ejemplo de Stored Procedure**
Insertar una nueva persona en la tabla personas.

```sql
CREATE OR REPLACE FUNCTION insertar_persona (rut varchar, nombre varchar, apellido varchar)
RETURNS void AS $$

--DECLARE
--  Aqui irian las declaracion de variables

BEGIN
  INSERT INTO personas VALUES (rut, nombre, apellido);
END;
$$ LANGUAGE plpgsql;
```

### Ahora para usarla:

```sql
SELECT insertar_persona(‘11.111.111-1’, ‘pepito’, ‘los palotes’)
```

> [!note] Comillas
> `‘…’` son comillas tipográficas copiadas de la slide. En PostgreSQL va `SELECT insertar_persona('11.111.111-1', 'pepito', 'los palotes');`

> [!tip] Complemento — sintaxis y más ejemplos (slides "Clase 8: Lógica en la BDD")
> ```sql
> CREATE OR REPLACE FUNCTION <nombre_funcion> (<argumentos>) RETURNS <tipo_retorno> AS $$
> DECLARE
>   <declaracion de variables>
> BEGIN
>   <sentencias SQL>
> END
> $$ LANGUAGE plpgsql;
> ```
> **Iterar sobre una consulta** e insertar en otra tabla:
> ```sql
> CREATE OR REPLACE FUNCTION transferencia_nombres() RETURNS void AS $$
> DECLARE
>   tupla RECORD;
>   concat varchar;
> BEGIN
>   FOR tupla IN SELECT * FROM Personas LOOP
>     concat = tupla.nombre || tupla.apellido;
>     INSERT INTO personascompleto VALUES (tupla.rut, concat);
>   END LOOP;
> END
> $$ LANGUAGE plpgsql;
> ```
> **Devolver una tabla** con una consulta parametrizada (`$1` es el primer argumento):
> ```sql
> CREATE OR REPLACE FUNCTION vuelos_desde (c_origen varchar)
> RETURNS TABLE (ciudad_destino varchar(50), horas integer) AS $$
> BEGIN
>   RETURN QUERY EXECUTE
>     'SELECT ciudad_destino, horas FROM Vuelo WHERE ciudad_origen = $1'
>   USING c_origen;
> END
> $$ LANGUAGE plpgsql;
> -- uso: SELECT * FROM vuelos_desde('Santiago');
> ```

> [!tip] Complemento — conclusión de la clase sobre la lógica en la BD
> - Escribir lógica compleja en SQL se puede volver **inmanejable muy rápido**. Además, para modificar triggers, vistas y procedimientos ya guardados hay que volver a ejecutar un `CREATE`.
> - Los frameworks web modernos, de manera opinionada, tienen **escaso soporte** para estas funcionalidades. Por eso views, procedures y triggers no se ven mucho en aplicaciones modernas; la lógica suele vivir en el código (por ejemplo, en los modelos de [[04 - Modelos y Active Record|Active Record]]).
> - Sí aparecen en **sistemas legados** y en **data engineering** (data warehouses, data lakes) y en ciertos servicios en la nube.

## Preguntas de repaso

1. ¿Qué es un stored procedure?
> [!question]- Respuesta
> Una función con varias sentencias SQL (y control de flujo) que se guarda en el DBMS y se ejecuta como una unidad, por ejemplo con `SELECT nombre_funcion(…)`.

2. Nombra tres ventajas y tres desventajas.
> [!question]- Respuesta
> Ventajas: velocidad, seguridad (control de acceso a datos y lógica) y reutilización. Desventajas: difícil migrar a otra base de datos, testing más difícil y código menos mantenible.

3. ¿Por qué se usan poco en aplicaciones web modernas?
> [!question]- Respuesta
> Porque la lógica compleja en SQL se vuelve difícil de mantener, cambiarla exige recrear los objetos y los frameworks web tienen poco soporte para ellos.

4. ¿Cómo se llama a `insertar_persona` en PostgreSQL?
> [!question]- Respuesta
> `SELECT insertar_persona('11.111.111-1', 'pepito', 'los palotes');`, con comillas simples rectas.
