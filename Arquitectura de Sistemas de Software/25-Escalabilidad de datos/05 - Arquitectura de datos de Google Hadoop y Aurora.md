---
ramo: "Arquitectura de Sistemas de Software"
tema: "Escalabilidad de datos"
tags:
  - arquisis/escalabilidad
  - arquisis/datos
  - arquisis/casos
  - origen/complemento
prerrequisitos:
  - "[[04 - Caché y leader-follower para escalar lecturas]]"
---

# Arquitectura de datos de Google Hadoop y Aurora

Cuando los datos se miden en petabytes, las bases de datos comerciales no escalan. Google construyó su propia infraestructura sobre **hardware barato** (*commodity*), y sus ideas dieron origen a **Hadoop**. Hoy los proveedores de nube ofrecen bases distribuidas administradas, como **Aurora**. Las tres ilustran las técnicas del tema llevadas al extremo: particionar, replicar y aceptar que las fallas son normales.

## La escala de Google

- **La tarea (2010): ordenar 1 PB** (1.000 TB, un millón de GB), es decir, 10 billones de registros de 100 bytes: **6 horas y 2 minutos** con **4.000 computadores**, con los datos **replicados 3 veces en 48.000 discos**.
- Hoy procesa unos **2,5 EB por día** (1 EB = 1.000 PB).
- **Stack de datos:** Linux; Python, Java y C++; más de 200 clusters GFS (cada uno de 1.000 a 5.000 máquinas dual core con GB Ethernet y 4-8 GB de RAM, con lectura y escritura a 40 GB/s); 6.000 aplicaciones MapReduce. BigTable guarda miles de millones de URLs, cientos de TB de imágenes satelitales y las preferencias de cientos de millones de usuarios.
- **Stack de servicios:** los productos (búsqueda, publicidad, correo, mapas, video, chat, Blogger) corren sobre la infraestructura distribuida (GFS, MapReduce, BigTable), que corre sobre **máquinas baratas en distintos data centers**.

## Google File System (GFS)

Un sistema de archivos **masivo, estructurado y distribuido**: alta confiabilidad entre data centers, miles de nodos, alto ancho de banda de lectura y escritura, y bloques de datos grandes. Sus operaciones son `create`, `delete`, `open`, `close`, `read`, `write`, `snapshot` y `append`.

![Un archivo de GFS dividido en chunks replicados en varios chunkservers, con un master](adjuntos/Archivos%20de%20GFS%20divididos%20en%20chunks%20replicados.png)

> [!example]- Transcripción de la imagen
> - Un **file** se divide en **chunks de 64 MB**, y cada chunk se **replica** para tolerar fallas (tres filas de bloques de colores).
> - Las réplicas se reparten entre varios **chunkservers**.
> - El **master** guarda la *in-memory FS metadata*, un *checkpoint image* y un *operation log*: "the master manages the file system namespace".

- **Relación asimétrica:** un **master** con la metadata y **chunkservers** con los datos, cada chunk replicado 3 veces.
- No tiene interfaz de usuario: se invoca mediante una **API** desde las aplicaciones. No tiene links ni directorios, solo paths.
- **Limitaciones:** mala performance con **archivos pequeños**, manejo de inconsistencias, y la **metadata en memoria** del master (mucha metadata significa mucha memoria).

## Bigtable

Diseñada para un escenario con **más lecturas que escrituras**, donde **las fallas de componentes son comunes** y los discos son baratos.
- Es un **mapa hash distribuido**, construido sobre GFS (hoy Colossus). **No soporta SQL**: solo búsquedas por llave **(fila, columna, timestamp)**, sin operadores relacionales, con número de columnas variable y tipos distintos por columna.
- Cada fila se guarda en una o más **tablets**. Una tablet es una secuencia de bloques de 64 KB en formato **SSTable**.
- **Servidores:**
  - el **master** asigna tablets a los tablet servers, sigue su ubicación y las redistribuye;
  - los **tablet servers** procesan lecturas y escrituras y dividen las tablets grandes (100-200 MB);
  - **Chubby** es el servicio de locks para la exclusión mutua (abrir una tablet para escritura, elegir al master, controlar el acceso).
- Las tablets se cachean en RAM siempre que es posible, y si un servidor falla, sus tablets se reparten entre muchos otros.

![Tablets de Bigtable sobre chunkservers de GFS](adjuntos/Tablets%20de%20Bigtable%20sobre%20chunkservers%20de%20GFS.png)

> [!example]- Transcripción de la imagen
> - Arriba, un **Head node** conectado a un **Chubby Server**.
> - Debajo, dos **Tablet server**, cada uno con tres **Tablet** (vista lógica).
> - Más abajo, **GFS Chunkserver** con **SSTable** de colores (disposición física), algunas con su **(replica) SSTable** en otro servidor.

## Apache Hadoop

Framework open source (Apache License 2.0) para **almacenar y procesar grandes cantidades de datos en clusters de computadores baratos**, inspirado en los papers de Google.
- **Componentes:** HDFS (sistema de archivos distribuido, inspirado en GFS: Master → NameNode, Chunkserver → DataNode, chunk → block), YARN (gestión de recursos) y MapReduce. Ecosistema: Pig, Hive, HBase y Spark.
- **Usos:** big data, creación de índices de búsqueda, procesamiento de logs, text mining, sistemas de recomendación, modelos predictivos y análisis de video y de grafos. Lo usan industrias que procesan muchos datos en paralelo (riesgo, churn, publicidad, fraude). Casos: el seguimiento de billones de canciones y likes (un cluster de 40 nodos con 10 TB) y Twitter, que analizó 100.000 millones de tweets con Hadoop y Pig.
- **Contras:** **no sirve en línea** (latencia mínima de un minuto, porque es procesamiento por lotes), es muy malo con datos de grafo, HBase tiene problemas de recolección de basura, y hoy hay soluciones más rápidas que trabajan en RAM (Spark).

## AWS Aurora

**Base de datos SQL distribuida en la nube, compatible con PostgreSQL y MySQL.**
- **Pros:** escalabilidad bajo demanda, réplicas autogestionadas y compatibilidad con los motores conocidos.
- **Contras:** más cara que otras soluciones y poco personalizable.

> [!tip] El patrón común
> GFS, Bigtable y HDFS comparten la misma estructura: **un coordinador con la metadata** (master o NameNode) y **muchos nodos baratos con los datos particionados y replicados 3 veces**. Asumen que las fallas son normales, y la replicación las hace irrelevantes.

## Preguntas de repaso

> [!question]- Describa la arquitectura de GFS y por qué replica cada chunk 3 veces.
> Un master guarda la metadata (namespace y ubicación de los chunks) en memoria, y muchos chunkservers guardan los datos en chunks de 64 MB. Cada chunk se replica 3 veces en servidores distintos porque, con miles de máquinas baratas, las fallas son constantes: la replicación permite seguir leyendo aunque caiga un servidor.

> [!question]- ¿Cuáles son las limitaciones de GFS?
> Mala performance con archivos pequeños (está pensado para archivos grandes), manejo de inconsistencias, y que el master guarda toda la metadata en memoria: con muchos archivos, la memoria del master se vuelve el límite.

> [!question]- ¿Por qué Bigtable no soporta SQL y qué ofrece a cambio?
> Porque las bases relacionales no escalaban a miles de máquinas y petabytes. Ofrece un mapa distribuido con acceso por (fila, columna, timestamp), columnas variables y particionado automático en tablets, que escala horizontalmente a costa de no tener joins ni operadores relacionales.

> [!question]- ¿Qué rol cumple Chubby en Bigtable?
> Es el servicio de locks distribuidos: da exclusión mutua para operaciones como abrir una tablet para escritura y elegir al master, y controla el acceso. Evita que dos servidores crean ser dueños de lo mismo.

> [!question]- ¿Para qué casos sirve Hadoop y para cuáles no?
> Sirve para procesamiento por lotes de grandes volúmenes en paralelo: índices de búsqueda, análisis de logs, recomendaciones, modelos predictivos. No sirve para consultas en línea (su latencia mínima es de un minuto) ni para datos de grafo, y hoy hay alternativas más rápidas que trabajan en RAM.

> [!question]- Relacione GFS con HDFS.
> HDFS está inspirado en GFS: el master pasa a llamarse NameNode, los chunkservers son DataNodes, los chunks son blocks, la checkpoint image es FsImage y el operation log es EditLog.

> [!question]- V o F: "Aurora es una base NoSQL distribuida de Amazon".
> Falso. Aurora es una base SQL distribuida y compatible con PostgreSQL y MySQL, con réplicas autogestionadas y escalabilidad bajo demanda. Su costo es mayor y es poco personalizable.
