---
ramo: Bases de Datos
tema: Gestión del curso
tags: [bd/curso, origen/apuntes]
prerrequisitos: ["[[01 - Evaluación y calendario de IIC2413|Evaluación y calendario de IIC2413]]"]
---
# Preparación del examen de Bases de Datos

Mi plan de estudio para el examen y lo que dijo la clase de repaso sobre su formato y contenidos.

## Plan de estudio para el examen
- [x] 1 hora: SQL.
- [x] 1 hora: slides antiguas (de años anteriores).
- [x] 1 hora: slides que faltaban por repasar.
- [x] 1 hora: hoja resumen (2 páginas). Sugerencia: incluir las sentencias SQL más comunes (las usadas en clases, talleres y proyecto).

> [!tip] Complemento — clase de repaso del examen (PDF "clase_de_repaso")
> **Formato:**
> - 2 horas.
> - 18 preguntas breves de 10 puntos cada una. $Nota = \frac{puntaje\ total}{30} + 1$.
> - Solo se pueden usar las hojas del examen y un lápiz pasta.
> - El mismo tema puede aparecer en más de una pregunta.
> - Se entregan todas las preguntas, aunque no estén respondidas.
>
> **Objetivos:** principalmente **conocimientos teóricos**, con énfasis en la materia no evaluada. "Lo esencial del examen son los conocimientos teóricos y no la programación: decidir qué se usa, para qué sirve, cómo se usa, por qué es mejor o peor, y no programar SQL."
>
> | Tema del examen | Dónde está en el vault |
> |---|---|
> | Utilidad y características de los DBMS | [[01 - Sistemas de bases de datos y DBMS\|Sistemas de bases de datos y DBMS]] |
> | BD relacionales versus otras | [[01 - Bases de datos NoSQL\|Bases de datos NoSQL]] |
> | Dependencias, anomalías, formas normales | [[Bases de Datos/07-Normalización/_Índice\|Normalización]] |
> | Lenguajes de programación + SQL y vistas | [[01 - SQL desde Python con cursores\|SQL desde Python]], [[01 - Vistas\|Vistas]] |
> | Evaluación de consultas | [[Bases de Datos/12-Evaluación de consultas/_Índice\|Evaluación de consultas]] |
> | Storage, indexing | [[Bases de Datos/11-Almacenamiento e índices/_Índice\|Almacenamiento e índices]] |
> | Transacciones y recuperación ante fallas | [[Bases de Datos/09-Transacciones y concurrencia/_Índice\|Transacciones]], [[Bases de Datos/10-Recuperación de fallas/_Índice\|Recuperación]] |
> | Privacidad | [[Bases de Datos/15-Privacidad de datos/_Índice\|Privacidad de datos]] |
>
> **Repositorios con material de años anteriores** (sirven como las "slides antiguas"):
> - https://github.com/alanezz/Syllabus-2019-1
> - https://github.com/IIC2413/Syllabus-2020-1
> - https://github.com/IIC2413/Syllabus-2020-2
> - https://github.com/IIC2413/Syllabus-2021-1
> - https://github.com/IIC2413/Syllabus-2021-2
> - https://github.com/IIC2413/Syllabus-2022-1
> - https://github.com/IIC2413/Syllabus-2022-2
> - https://github.com/IIC2413/Syllabus-2023-1
> - https://github.com/IIC2413/Syllabus-2023-2
> - Libro del curso (Ramakrishnan y Gehrke, 3.ª ed.): https://github.com/Premiumlab/Database-Management-System-Ramakrishnan-Gehrke-3rd-Edition

> [!example] Ejemplo extra — qué poner en la hoja resumen de 2 páginas
> - Plantillas SQL: `CREATE TABLE` con PK/FK/`ON DELETE`, `SELECT-FROM-WHERE-GROUP BY-HAVING-ORDER BY`, joins (INNER/LEFT), `IN`/`EXISTS`/`ALL`/`ANY`, vista y vista materializada, trigger en PL/pgSQL, `START TRANSACTION`/`COMMIT`/`ROLLBACK`/`SAVEPOINT`.
> - Tablas: formas normales, niveles de aislamiento, undo vs redo, hash vs B+, costos de NLJ/BNLJ, k-anonimato vs ℓ-diversidad vs privacidad diferencial.

## Preguntas de repaso

1. ¿Qué tipo de preguntas tenía el examen según la clase de repaso?
> [!question]- Respuesta
> 18 preguntas breves, principalmente teóricas: decidir qué usar, para qué sirve, cómo se usa y por qué es mejor o peor, sin programar SQL.

2. ¿Cómo se calculaba la nota del examen?
> [!question]- Respuesta
> Nota = puntaje total / 30 + 1, con 18 preguntas de 10 puntos.

3. Nombra cuatro temas que entraban en el examen.
> [!question]- Respuesta
> Por ejemplo: utilidad de los DBMS, formas normales, evaluación de consultas, índices, transacciones y recuperación, privacidad.
