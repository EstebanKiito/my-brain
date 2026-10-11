# Dudas y posibles errores en los apuntes originales — Bases de Datos (IIC2413)

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Modelo relacional
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[04 - Álgebra relacional\|Álgebra relacional]] | "Join (⨝): … combina tuplas de dos relaciones basándose en una condición de igualdad. Hay varios tipos de Join, incluyendo Inner Join, Left Outer Join…" | La igualdad describe el *equi-join*. En la clase el join admite cualquier condición: $R_1 \bowtie_{cond} R_2 = \sigma_{cond}(R_1 \times R_2)$. Los outer joins son una extensión de SQL, no del álgebra vista en clase. |
| 🟡 | [[03 - Superllaves, claves candidatas y clave primaria\|Superllaves, claves candidatas y clave primaria]] | "Superllave: Cualquier combinación de atributos que incluya una clave candidata. Por lo tanto." | La frase quedó cortada. Se propone completarla con la cita siguiente: toda clave candidata es superllave, pero no al revés. |
| ℹ️ | [[05 - Join en álgebra relacional\|Join en álgebra relacional]] | Resultado con una sola columna B | Con la condición explícita `R1.B = R2.B` el resultado tendría `R1.B` y `R2.B`. Una sola columna B corresponde al *natural join*. Se explicó en un complemento; no es un error grave. |

## Definición de datos en SQL
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[05 - INSERT e integridad referencial\|INSERT e integridad referencial]] | `CREATE TABLE S(a int, c int, FOREIGN KEY(a) REFERENCES R, ...);` | El `...` viene de la slide y no es SQL válido. Se aclaró en una nota: `REFERENCES R` sin columnas apunta a la llave primaria de R. |

## Consultas SQL
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[06 - ORDER BY\|ORDER BY]] | "(Order by resuelve un empate por el ultimo atributo entregado)" | Se resuelve con el **siguiente** atributo de la lista. Slide: "El i-ésimo atributo del ORDER BY resuelve un empate en el atributo i-1". Con dos atributos coincide con el último. |
| 🟡 | [[08 - LIKE y NOT LIKE\|LIKE y NOT LIKE]] | `WHERE name LIKE ‘%Potter%'`, `# BUSCA TODAS…` | Comillas tipográficas (‘ ’) y comentario con `#`: no corren en PostgreSQL. Se agregó la versión con `'…'` y `--`. |
| 🟡 | [[08 - LIKE y NOT LIKE\|LIKE y NOT LIKE]] | "  : No otro caracter → ( correo Like ‘%@gmail.com’ )" | Ambiguo. Se interpretó así: un patrón que no termina en `%` no admite más caracteres después (el correo **termina** en @gmail.com). |
| ℹ️ | [[05 - Alias y expresiones en SELECT\|Alias y expresiones en SELECT]] | "Interestellar" | Errata de "Interstellar"; se dejó tal cual en la tabla de ejemplo. |

## Agregación y subconsultas
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - COUNT y DISTINCT\|COUNT y DISTINCT]] | "SELECT DISTINCT COUNT(cantidad): … si hay filas con el mismo valor de cantidad, se cuentan solo una vez." | Falso: `COUNT(cantidad)` cuenta los repetidos (6, 1, 1 → 3) y el `DISTINCT` se aplica a la única fila del resultado. Solo `COUNT(DISTINCT …)` cuenta una vez los valores repetidos. |
| 🟡 | [[03 - GROUP BY\|GROUP BY]] | `WHERE fecha > '10/01'` | Si `fecha` es texto, `'07/02' > '10/01'` es falso (comparación de strings) y el filtro no hace lo esperado. Viene de la slide. Hace falta un tipo `date`. |
| 🟡 | [[09 - Subconsulta en el FROM - primera película de cada actor\|Subconsulta en el FROM: primera película de cada actor]] | Tabla intermedia `id/año`: 2 → 2014, 3 → 2001 | Con `Actuo_en` (2→1, 3→2) los años serían 2 → 1997 (Titanic) y 3 → 2014 (Interstellar). O los datos de `Actuo_en` son otros, o el resultado está mal. También cambia el nombre de columna: `pelicula_id` vs `id_pelicula`. |
| ℹ️ | [[04 - HAVING\|HAVING]] | `HAVING SUM(cantidad) > 100` | Con los datos del ejemplo el resultado es vacío (tomates suma 10, zapallo 3). No es error: el ejemplo muestra la sintaxis. |
| ℹ️ | [[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)\|Consultas anidadas]] | `‘Lollapalooza’`, `‘Austral Calafate’`, `‘Toyota’` | Comillas tipográficas de la slide; en PostgreSQL van comillas simples rectas. |

## Valores nulos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - NULL en SQL\|NULL en SQL]] | "(Que no sea ni 3 ni distinto a 3 NO ES NULO!!!)" | Redacción confusa. La idea de la slide: si `b` **es** nulo, ni `b = 3` ni `b <> 3` son verdaderos, así que esas filas se pierden y hay que agregar `IS NULL`. |
| ✅ | [[02 - Lógica de tres valores\|Lógica de tres valores]] | Encabezado "R.A + R.S" y "UNKWNOWN" | Erratas: debería decir R.A + S.B y UNKNOWN. Los valores están correctos. |
| ℹ️ | [[03 - NOT IN con nulos\|NOT IN con nulos]] | "La comparación NULL NOT IN (...) se comporta como si la condición fuera desconocida…" | Precisión: el NULL problemático está **dentro** de la subconsulta (R), no en S.A. Cada `x = null` da UNKNOWN. Se aclaró en un complemento. |

## Diseño entidad-relación
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[06 - Principios de diseño de bases de datos\|Principios de diseño de bases de datos]] | *(slide 6)* `email nombre varchar(30) UNIQUE NOT NULL` | Errata de la slide: son dos columnas. En la nota se dejó `email varchar(30) UNIQUE NOT NULL`. |

## Normalización
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[06 - Forma normal de Boyce-Codd\|Forma normal de Boyce-Codd]] | Tabla 1 de la descomposición: "CS102 \| Dr. Brown" | La original dice CS101 \| Dr. Brown. La proyección debe tener (CS101, Dr. Smith) y (CS101, Dr. Brown). |
| 🟡 | [[06 - Forma normal de Boyce-Codd\|Forma normal de Boyce-Codd]] | "para toda dependencia funcional X→Y, X es una SUPERLLAVE" | Falta "no trivial" (A,B → A se cumple siempre). Además, el ejemplo Curso/Profesor/Aula tampoco está en 2NF, así que no muestra la diferencia entre 3NF y BCNF. Se agregó el ejemplo de la slide. |
| 🟡 | [[05 - Tercera forma normal\|Tercera forma normal]] | Ejemplo "NO en 3NF" con (Fabricante, Modelo, País, Continente) | Con llave (Fabricante, Modelo), Fabricante → País es parcial: la tabla no está ni en 2NF. Se propuso un ejemplo con llave simple. |

## Lógica en la base de datos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Triggers\|Triggers]] | "Ej: BEFORE CREATE", `AFTER CREATE ON Evaluaciones` | CREATE no es un evento de trigger: son INSERT, UPDATE, DELETE (y TRUNCATE). El error viene de la slide 8. |
| 🟡 | [[03 - Triggers\|Triggers]] | `CREATE TRIGGER … BEGIN … END` | Sintaxis genérica o MySQL ("más o menos así", dice la slide). En PostgreSQL el trigger ejecuta una función (`EXECUTE FUNCTION`), y falta el `;` tras `REFRESH`. Se agregó la versión PostgreSQL. |
| ℹ️ | [[05 - Stored procedures\|Stored procedures]] | `SELECT insertar_persona(‘11.111.111-1’, …)` | Comillas tipográficas de la slide; van comillas simples rectas. |
