---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, origen/complemento]
prerrequisitos: ["[[01 - Sistemas de bases de datos y DBMS|Sistemas de bases de datos y DBMS]]", "[[02 - Propiedades ACID|Propiedades ACID]]"]
---
# Arquitectura de un DBMS

Por dentro, un DBMS se divide en módulos: el procesador de consultas (parser, reescritura, optimizador, ejecutor), las transacciones, el **storage manager** (disco, buffer, métodos de acceso) y utilidades compartidas. Esta nota abre la parte de cómo se ejecuta realmente una consulta.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> Hasta ahora usamos el DBMS como una **caja negra**: hacemos una consulta y el sistema se encarga. Pero ¿cómo funciona realmente? ¿Cómo se evalúa una consulta?
>
> ![Slide - arquitectura de un DBMS](adjuntos/Slide%20-%20arquitectura%20de%20un%20DBMS.png)

> [!note]- Transcripción de la imagen
> Database Management System (DBMS) sobre la Database:
> | Módulo | Componentes |
> |---|---|
> | **Process Manager** | Admission Control, Scheduler |
> | **Query Processor** | Parser, Query Rewrite, Optimizer, Executor |
> | **Shared Utilities** | Catalog Manager, Memory Manager, Administration, Replication Services, Batch Utilities |
> | **Transactions** | Transaction Manager, Log Manager, Recovery Manager |
> | **Storage Manager** | Access Methods, Buffer Manager, Disk Manager |

## Ciclo de vida de una consulta

> [!tip] Complemento (slides "Clase 9")
> ```mermaid
> flowchart LR
>   SQL[Consulta SQL] -->|1| AR[Álgebra relacional]
>   AR -->|"2. reescritura"| PL[Plan lógico]
>   PL -->|"3. ¿qué algoritmos uso?"| PF[Plan físico]
>   PF -->|4| EJ[Ejecución]
>   EJ <-->|páginas| D[(Disco)]
> ```
> Para ejecutar la consulta hay que **acceder a los datos en disco**. De eso se encarga el **Storage Manager**:
> - **Disk Manager:** el almacenamiento secundario.
> - **Buffer Manager:** el uso de datos en memoria; optimiza la cantidad de I/O al disco duro (ver [[03 - Disco, RAM y buffer pool|Disco, RAM y buffer pool]]).
> - **Access Methods:** la organización eficiente de los datos, como los índices ([[09 - Índices en bases de datos|Índices en bases de datos]]).
>
> El módulo de **Transactions** es el de [[02 - Propiedades ACID|Propiedades ACID]]. Los algoritmos del paso 3 están en «Evaluación de consultas».

## Preguntas de repaso

1. ¿Cuáles son los cuatro pasos del ciclo de vida de una consulta?
> [!question]- Respuesta
> (1) SQL → álgebra relacional; (2) reescritura → plan lógico; (3) elegir algoritmos → plan físico; (4) ejecución, accediendo a los datos en disco.

2. ¿Qué hacen el Disk Manager, el Buffer Manager y los Access Methods?
> [!question]- Respuesta
> El Disk Manager maneja el almacenamiento secundario. El Buffer Manager maneja las páginas en memoria y minimiza los I/O. Los Access Methods organizan los datos para encontrarlos eficientemente (índices).

3. ¿En qué módulo están el Log Manager y el Recovery Manager?
> [!question]- Respuesta
> En Transactions, junto al Transaction Manager.
