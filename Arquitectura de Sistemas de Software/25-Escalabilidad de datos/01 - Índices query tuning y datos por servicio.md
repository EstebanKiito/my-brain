---
ramo: "Arquitectura de Sistemas de Software"
tema: "Escalabilidad de datos"
tags:
  - arquisis/escalabilidad
  - arquisis/datos
  - origen/complemento
prerrequisitos:
  - "[[01 - Escalamiento vertical y horizontal]]"
---

# Índices query tuning y datos por servicio

La base de datos suele ser el último cuello de botella: las réplicas de la aplicación se agregan fácil, pero todas terminan consultando los mismos datos. Los métodos en datos buscan principalmente **paralelizar el trabajo** manteniendo la **performance**, la **consistencia** y los **costos**. Las herramientas son modelos alternativos de bases de datos, distribución de los datos, NoSQL (*Not only SQL*) y modelos de datos avanzados. Antes de distribuir, conviene agotar lo barato: **índices** y **optimización de consultas**.

## Paso previo 1: indexado

Agregar **índices** sobre las columnas por las que se busca **acelera las lecturas**: el motor encuentra las filas sin recorrer la tabla completa. Muchas veces viene integrado (las llaves primarias y foráneas suelen indexarse).

| Pros | Contras |
|---|---|
| Sencillo de implementar | **Reconstruir los índices afecta las escrituras**: cada `INSERT` o `UPDATE` actualiza también el índice |
| Mejora enorme en lecturas selectivas | **No toda la data responde igual**: con columnas de pocos valores distintos (un booleano) el índice ayuda poco |

```sql
-- Antes: recorre la tabla completa de 10 millones de pedidos
SELECT * FROM pedidos WHERE cliente_id = 4821 AND estado = 'pendiente';

-- Índice compuesto para esa búsqueda frecuente
CREATE INDEX idx_pedidos_cliente_estado ON pedidos (cliente_id, estado);
```

## Paso previo 2: query tuning

Mejorar las consultas mediante optimización. En SQL, `EXPLAIN` (y sus variantes de cada motor) muestra el **plan de ejecución**: si usa un índice o recorre la tabla, en qué orden hace los joins y cuántas filas estima.

```sql
EXPLAIN ANALYZE
SELECT c.nombre, SUM(p.total)
FROM clientes c JOIN pedidos p ON p.cliente_id = c.id
WHERE p.fecha >= '2026-01-01'
GROUP BY c.nombre;
```

| Pros | Contras |
|---|---|
| Técnicas probadas | **Limitado a la data ya presente**: si el volumen sigue creciendo, una consulta optimizada vuelve a ser lenta |
| Amplio espacio de mejora | |

## Datos en arquitecturas distribuidas

EDA, SOA y microservicios intencionan **una fuente de datos por servicio**.

| Pros | Contras |
|---|---|
| Ayuda a la **separación de responsabilidades**: cada servicio es dueño de sus datos | **Añade complejidad**: consistencia entre servicios, sin joins entre bases |
| Permite **escalar cada fuente de datos según su necesidad** y elegir el modelo adecuado (relacional para pagos, llave-valor para sesiones, documentos para catálogos) | **Puede reducir la performance si se cruza mucha data**: armar una vista con datos de 5 servicios implica 5 llamadas |

> [!example]- Respuesta modelo: qué base de datos usar en cada sección
> Las preguntas de casos piden **el tipo de base de datos por sección, qué guarda y por qué**. Por ejemplo, en una app de noticias:
> - **Sección de caza-noticias:** guarda las noticias enviadas en JSON → **base de documentos**, porque el formato es JSON y su estructura varía.
> - **Sección de validadores:** guarda las noticias en revisión y los resultados de la IA → puede ser la misma base de documentos (o una relacional, si se justifica).
> - **Sección de lectores:** guarda las noticias aprobadas con su metadata para filtrar por zona → **relacional escalable**, como pedía el enunciado.
> Si hay que componer datos de varias bases en consultas más complejas, se explica cómo: un servicio que agrega, eventos que alimentan una vista de lectura o una base analítica aparte.

> [!warning] Una base compartida entre servicios
> Si todos los microservicios leen y escriben la misma base, no hay escalabilidad independiente y se vuelve al acoplamiento del Shared Kernel degenerado. Ojo también con el extremo contrario: separar bases donde los datos se cruzan constantemente degrada la performance.

## Preguntas de repaso

> [!question]- ¿Por qué un índice acelera las lecturas pero puede empeorar las escrituras?
> Porque permite encontrar las filas sin recorrer la tabla, pero cada inserción o actualización debe modificar también el índice. Con muchos índices o muchas escrituras, ese costo se nota.

> [!question]- ¿Qué muestra `EXPLAIN` y para qué sirve al escalar?
> Muestra el plan de ejecución: si usa índices o recorre tablas completas, el orden de los joins y las filas estimadas. Sirve para encontrar consultas ineficientes y corregirlas antes de invertir en más hardware o en distribuir los datos.

> [!question]- ¿Cuál es la limitación principal del query tuning?
> Que trabaja sobre los datos que ya existen. Si el volumen sigue creciendo, la consulta optimizada vuelve a ser lenta y hace falta distribuir los datos (particionar, shardear o replicar).

> [!question]- ¿Qué gana y qué pierde un sistema de microservicios con una base de datos por servicio?
> Gana responsabilidades separadas, escalabilidad independiente de cada fuente y libertad de elegir el modelo de datos adecuado. Pierde la posibilidad de hacer joins entre bases, suma complejidad de consistencia y puede ser lento si las vistas cruzan mucha información de varios servicios.

> [!question]- V o F: "Agregar un índice a cada columna de la tabla siempre mejora el rendimiento".
> Falso. Cada índice cuesta espacio y hace más lentas las escrituras. Además, en columnas con pocos valores distintos casi no ayuda. Se indexan las columnas que aparecen en búsquedas y joins frecuentes.

> [!question]- Mini caso: un sistema guarda documentos de contratos con formatos variables y además transacciones de pago. ¿Qué bases usaría?
> Una relacional transaccional para los pagos, que requieren consistencia y ACID, y una base de documentos o un almacenamiento de objetos tipo S3 para los contratos de formato variable. Si hay que cruzar ambos, un servicio compone las consultas o se mantiene una vista con los ids de los contratos en la base relacional.
