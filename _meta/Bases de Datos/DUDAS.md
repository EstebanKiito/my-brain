# Dudas y posibles errores en los apuntes originales — Bases de Datos (IIC2413)

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Modelo relacional
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[04 - Álgebra relacional\|Álgebra relacional]] | "Join (⨝): … combina tuplas de dos relaciones basándose en una condición de igualdad. Hay varios tipos de Join, incluyendo Inner Join, Left Outer Join…" | La igualdad describe el *equi-join*. En la clase el join admite cualquier condición: $R_1 \bowtie_{cond} R_2 = \sigma_{cond}(R_1 \times R_2)$. Los outer joins son una extensión de SQL, no del álgebra vista en clase. Corregido en el texto de la nota. |
| ✅ | [[03 - Superllaves, claves candidatas y clave primaria\|Superllaves, claves candidatas y clave primaria]] | "Superllave: Cualquier combinación de atributos que incluya una clave candidata. Por lo tanto." | La frase quedó cortada. Se propone completarla con la cita siguiente: toda clave candidata es superllave, pero no al revés. Corregido en el texto de la nota. |
| ℹ️ | [[05 - Join en álgebra relacional\|Join en álgebra relacional]] | Resultado con una sola columna B | Con la condición explícita `R1.B = R2.B` el resultado tendría `R1.B` y `R2.B`. Una sola columna B corresponde al *natural join*. Se explicó en un complemento; no es un error grave. |

## Definición de datos en SQL
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[05 - INSERT e integridad referencial\|INSERT e integridad referencial]] | `CREATE TABLE S(a int, c int, FOREIGN KEY(a) REFERENCES R, ...);` | El `...` viene de la slide y no es SQL válido. Se aclaró en una nota: `REFERENCES R` sin columnas apunta a la llave primaria de R. |

## Consultas SQL
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[06 - ORDER BY\|ORDER BY]] | "(Order by resuelve un empate por el ultimo atributo entregado)" | Se resuelve con el **siguiente** atributo de la lista. Slide: "El i-ésimo atributo del ORDER BY resuelve un empate en el atributo i-1". Con dos atributos coincide con el último. Corregido en el texto de la nota. |
| ✅ | [[08 - LIKE y NOT LIKE\|LIKE y NOT LIKE]] | `WHERE name LIKE ‘%Potter%'`, `# BUSCA TODAS…` | Comillas tipográficas (‘ ’) y comentario con `#`: no corren en PostgreSQL. Corregido en el texto de la nota. |
| ✅ | [[08 - LIKE y NOT LIKE\|LIKE y NOT LIKE]] | "  : No otro caracter → ( correo Like ‘%@gmail.com’ )" | Ambiguo. Se interpretó así: un patrón que no termina en `%` no admite más caracteres después (el correo **termina** en @gmail.com). Corregido en el texto de la nota. |
| ℹ️ | [[05 - Alias y expresiones en SELECT\|Alias y expresiones en SELECT]] | "Interestellar" | Errata de "Interstellar"; se dejó tal cual en la tabla de ejemplo. |

## Agregación y subconsultas
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[02 - COUNT y DISTINCT\|COUNT y DISTINCT]] | "SELECT DISTINCT COUNT(cantidad): … si hay filas con el mismo valor de cantidad, se cuentan solo una vez." | Falso: `COUNT(cantidad)` cuenta los repetidos (6, 1, 1 → 3) y el `DISTINCT` se aplica a la única fila del resultado. Solo `COUNT(DISTINCT …)` cuenta una vez los valores repetidos. Corregido en el texto de la nota. |
| ✅ | [[03 - GROUP BY\|GROUP BY]] | `WHERE fecha > '10/01'` | Si `fecha` es texto, `'07/02' > '10/01'` es falso (comparación de strings) y el filtro no hace lo esperado. Viene de la slide. Hace falta un tipo `date`. Corregido en el texto de la nota. |
| ✅ | [[09 - Subconsulta en el FROM - primera película de cada actor\|Subconsulta en el FROM: primera película de cada actor]] | Tabla intermedia `id/año`: 2 → 2014, 3 → 2001 | Con `Actuo_en` (2→1, 3→2) los años serían 2 → 1997 (Titanic) y 3 → 2014 (Interstellar). O los datos de `Actuo_en` son otros, o el resultado está mal. También cambia el nombre de columna: `pelicula_id` vs `id_pelicula`. Corregido en el texto de la nota. |
| ℹ️ | [[04 - HAVING\|HAVING]] | `HAVING SUM(cantidad) > 100` | Con los datos del ejemplo el resultado es vacío (tomates suma 10, zapallo 3). No es error: el ejemplo muestra la sintaxis. |
| ℹ️ | [[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)\|Consultas anidadas]] | `‘Lollapalooza’`, `‘Austral Calafate’`, `‘Toyota’` | Comillas tipográficas de la slide; en PostgreSQL van comillas simples rectas. |

## Valores nulos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[01 - NULL en SQL\|NULL en SQL]] | "(Que no sea ni 3 ni distinto a 3 NO ES NULO!!!)" | Redacción confusa. La idea de la slide: si `b` **es** nulo, ni `b = 3` ni `b <> 3` son verdaderos, así que esas filas se pierden y hay que agregar `IS NULL`. Corregido en el texto de la nota. |
| ✅ | [[02 - Lógica de tres valores\|Lógica de tres valores]] | Encabezado "R.A + R.S" y "UNKWNOWN" | Erratas: debería decir R.A + S.B y UNKNOWN. Los valores están correctos. |
| ℹ️ | [[03 - NOT IN con nulos\|NOT IN con nulos]] | "La comparación NULL NOT IN (...) se comporta como si la condición fuera desconocida…" | Precisión: el NULL problemático está **dentro** de la subconsulta (R), no en S.A. Cada `x = null` da UNKNOWN. Se aclaró en un complemento. |

## Diseño entidad-relación
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[06 - Principios de diseño de bases de datos\|Principios de diseño de bases de datos]] | *(slide 6)* `email nombre varchar(30) UNIQUE NOT NULL` | Errata de la slide: son dos columnas. En la nota se dejó `email varchar(30) UNIQUE NOT NULL`. |

## Normalización
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[06 - Forma normal de Boyce-Codd\|Forma normal de Boyce-Codd]] | Tabla 1 de la descomposición: "CS102 \| Dr. Brown" | La original dice CS101 \| Dr. Brown. La proyección debe tener (CS101, Dr. Smith) y (CS101, Dr. Brown). Corregido en el texto de la nota. |
| ✅ | [[06 - Forma normal de Boyce-Codd\|Forma normal de Boyce-Codd]] | "para toda dependencia funcional X→Y, X es una SUPERLLAVE" | Falta "no trivial" (A,B → A se cumple siempre). Además, el ejemplo Curso/Profesor/Aula tampoco está en 2NF, así que no muestra la diferencia entre 3NF y BCNF. Corregido en el texto de la nota. |
| ✅ | [[05 - Tercera forma normal\|Tercera forma normal]] | Ejemplo "NO en 3NF" con (Fabricante, Modelo, País, Continente) | Con llave (Fabricante, Modelo), Fabricante → País es parcial: la tabla no está ni en 2NF. Se propuso un ejemplo con llave simple. Corregido en el texto de la nota. |

## Lógica en la base de datos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[03 - Triggers\|Triggers]] | "Ej: BEFORE CREATE", `AFTER CREATE ON Evaluaciones` | CREATE no es un evento de trigger: son INSERT, UPDATE, DELETE (y TRUNCATE). El error viene de la slide 8. Corregido en el texto de la nota. |
| ✅ | [[03 - Triggers\|Triggers]] | `CREATE TRIGGER … BEGIN … END` | Sintaxis genérica o MySQL ("más o menos así", dice la slide). En PostgreSQL el trigger ejecuta una función (`EXECUTE FUNCTION`), y falta el `;` tras `REFRESH`. Corregido en el texto de la nota. |
| ℹ️ | [[05 - Stored procedures\|Stored procedures]] | `SELECT insertar_persona(‘11.111.111-1’, …)` | Comillas tipográficas de la slide; van comillas simples rectas. |

## Transacciones y concurrencia
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[04 - Lecturas sucias, no repetibles y actualización perdida\|Lecturas sucias, no repetibles y actualización perdida]] | Bloque "Ejemplos": `READ(A,x) WRITE(A,x)` repetido para sucia y no repetible | No indica qué transacción hace cada operación y los dos primeros quedan iguales. Corregido en el texto de la nota. |
| ✅ | [[05 - Schedules serial y serializable\|Schedules serial y serializable]] | Código de "Schedule Serial" y "Schedule No Serializable" | El serial muestra solo T1, y al no serializable le faltan las operaciones de T2 sobre A. Se reconstruyeron desde las imágenes. Corregido en el texto de la nota. |
| ✅ | [[12 - Niveles de aislamiento\|Niveles de aislamiento]] | "Por defecto: SET TRANSACTION ISOLATION LEVEL SERIALIZABLE READ WRITE" | Es el default del estándar SQL. En PostgreSQL el default es READ COMMITTED (en MySQL, REPEATABLE READ). Además, READ WRITE es el modo de acceso, no un nivel. Corregido en el texto de la nota. |
| ℹ️ | [[10 - COMMIT, ROLLBACK y SAVEPOINT\|COMMIT, ROLLBACK y SAVEPOINT]] | "Al ejecutar ROLLBACK TO SAVEPOINT se borra el SAVEPOINT" | Lo dice la slide. En PostgreSQL el savepoint sigue vivo después de `ROLLBACK TO` (se elimina con `RELEASE`); los que se crearon después de él sí se borran. |
| ✅ | [[02 - Propiedades ACID\|Propiedades ACID]] | "Sin Atomoicidad", "transiciones en serie", "Aislamineto (Granulidad)" | Erratas: atomicidad, transacciones, aislamiento (granularidad). Se corrigieron en los títulos sin cambiar el sentido. |

## Almacenamiento e índices
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[08 - Tablas de hash\|Tablas de hash]] | "Una función de hash no necesariamente es inyectiva," + ítem vacío | La sección quedó inconclusa. Se completó en un complemento: colisiones y cómo se resuelven, con el ejemplo de la clase (aid mod 5). Corregido en el texto de la nota. |
| ℹ️ | [[02 - Disco duro y páginas\|Disco duro y páginas]] | "Página: … que el sistema operativo gestiona, generalmente de 4 KB" | Precisión: la slide dice que la página la define el SO **o el DBMS**. En PostgreSQL mide 8 KB. |
| ✅ | [[06 - Arreglos y listas ligadas\|Arreglos y listas ligadas]] | "alteatoria", "utlizando", "lecutras" | Erratas; se dejaron en el texto original y se anotaron. |

## Gestión del curso
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Proyecto de Bases de Datos\|Proyecto de Bases de Datos]] | Query 8: `SELECT platos.nombre, plato.nombre_restaurant FROM platos` | Inconsistente con la query 1 (`platos`, `nombre_restaurante`) e incompleta (sin WHERE). Se propuso `SELECT platos.nombre, platos.nombre_restaurante FROM platos;`. |
| 🟡 | [[03 - Proyecto de Bases de Datos\|Proyecto de Bases de Datos]] | Query 2: "Input: email y gasto mensual" | Solo el enunciado; falta el SQL. |
| 🟡 | [[03 - Proyecto de Bases de Datos\|Proyecto de Bases de Datos]] | "Al hacer cdeldes sobrescribir clientes" | Ilegible: ¿"deletes"?, ¿"CSV"? Se dejó tal cual. |
| ℹ️ | [[01 - Evaluación y calendario de IIC2413\|Evaluación y calendario de IIC2413]] | Calendario 2024-1 vs slides 2023-2 | Las slides dicen 3 controles + examen y 3 entregas; el calendario tiene I1, I2, examen, E1, E2 y 4 talleres. Se muestran ambas versiones. |
| ℹ️ | [[03 - Proyecto de Bases de Datos\|Proyecto de Bases de Datos]] | Teléfono y "Revisar al fukin Pablo O / Ryan" | Omitidos por privacidad (repo público), por decisión tuya; quedan en `aceptados` del mapeo. |
