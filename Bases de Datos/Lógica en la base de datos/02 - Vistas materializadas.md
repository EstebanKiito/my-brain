---
ramo: Bases de Datos
tema: Lógica en la base de datos
tags: [bd/logica, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - Vistas|Vistas]]"]
---
# Vistas materializadas

Una vista materializada **guarda físicamente** el resultado de su consulta. Es tan rápida como una tabla, pero puede quedar desactualizada: hay que refrescarla con `REFRESH MATERIALIZED VIEW`.

## Vistas materializadas (mis apuntes)
- A diferencia de las vistas estándar, las vistas materializadas almacenan datos físicamente.
- Requieren espacio adicional y deben mantenerse actualizadas con comandos como REFRESH MATERIALIZED VIEW.

**Ejemplo de vistas materializadas**

```sql
CREATE MATERIALIZED VIEW PelEval AS
SELECT pelicula, director, AVG(eval) AS promedio
FROM Evaluaciones
GROUP BY pelicula, director;
```

**Actualizar vistas materializadas**

```sql
REFRESH MATERIALIZED VIEW PelEval;
```

- Podemos automatizar el esto en la DB? → Si, con TRIGGERS

> [!tip] Complemento (slides "Clase 8: Lógica en la BDD")
> | | Vista | Vista materializada | Tabla (`CREATE TABLE … AS SELECT`) |
> |---|---|---|---|
> | Guarda datos | no | **sí** | sí |
> | Velocidad de consulta | lenta (recalcula) | rápida | rápida |
> | Al cambiar los datos base | siempre al día | **desactualizada** hasta un `REFRESH` | desactualizada para siempre |
> | Se actualiza con | — | `REFRESH MATERIALIZED VIEW` | hay que recrearla a mano |
>
> - Las vistas materializadas dan **la misma abstracción** que las normales, pero son más rápidas.
> - En cambio, requieren espacio adicional e **introducen redundancia** que hay que mantener consistente; por ejemplo, ejecutando `REFRESH MATERIALIZED VIEW` cuando sea necesario.
> - ¿Se puede automatizar en la misma base de datos? Sí, con [[03 - Triggers|triggers]].
>
> Ejemplo: se inserta una evaluación nueva de Interstellar. `PelEval` sigue mostrando el promedio anterior hasta que se ejecuta el `REFRESH`.

## Preguntas de repaso

1. ¿En qué se diferencia una vista materializada de una vista normal?
> [!question]- Respuesta
> La materializada guarda físicamente el resultado: es más rápida, pero ocupa espacio y puede quedar desactualizada. La normal no guarda nada y recalcula en cada consulta.

2. ¿Qué hay que hacer cuando cambian las tablas base de una vista materializada?
> [!question]- Respuesta
> Ejecutar `REFRESH MATERIALIZED VIEW nombre;` para recalcular su contenido.

3. ¿Cómo se puede automatizar el refresco?
> [!question]- Respuesta
> Con un trigger que ejecute el `REFRESH` después de los cambios en la tabla base.
