---
ramo: "Arquitectura de Sistemas de Software"
tema: "Escalabilidad de datos"
tags:
  - arquisis/datos
  - indice
---

# Índice — Escalabilidad de datos

Cómo escalar la capa de datos: primero **índices y query tuning**, luego una base por servicio, el **teorema CAP** y BASE frente a ACID, **sharding frente a partitioning**, **caché y leader-follower** para las lecturas (y por qué no sirven para las escrituras), y los casos de **Google (GFS y Bigtable), Hadoop y Aurora**.

## Contenido

1. [[01 - Índices query tuning y datos por servicio]] — Índices y su costo en escrituras, EXPLAIN, datos por servicio en EDA, SOA y microservicios, y qué base usar por sección.
2. [[02 - Teorema CAP y BASE en el diseño de datos]] — CAP con la figura de dos nodos, por qué P no se elige, la revisión de Brewer en 2012, ACID frente a BASE y dos respuestas modelo.
3. [[03 - Sharding y partitioning]] — Sharding horizontal y vertical, ventajas y riesgos, partitioning por rango, tabla comparativa y la confusión típica de prueba.
4. [[04 - Caché y leader-follower para escalar lecturas]] — Caché en datos, leader-follower y su lag, qué técnica usar para cada problema, costos de los métodos y chaos engineering.
5. [[05 - Arquitectura de datos de Google Hadoop y Aurora]] — Ordenar un petabyte, GFS con master y chunks replicados, Bigtable con tablets y Chubby, Hadoop y HDFS, y Aurora.
