# Progreso de la migración — Bases de Datos (IIC2413)

Rama: `migrar/bases-de-datos`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Bases de Datos"` (y la verificación de Ingeniería de Software, porque el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura multi-ramo (`verificar.py --ramo`, `_meta/<Ramo>/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Modelo relacional | `Modelo relacional/` | ✅ hecho | 6 + índice | 0 + 3 |
| 2 | Definición de datos en SQL | `Definición de datos en SQL/` | ✅ hecho | 7 + índice | 0 |
| 3 | Consultas SQL | `Consultas SQL/` | ✅ hecho | 11 + índice | 0 |
| 4 | Agregación y subconsultas | `Agregación y subconsultas/` | ✅ hecho | 9 + índice | 0 |
| 5 | Valores nulos | `Valores nulos/` | ✅ hecho | 4 + índice | 0 |
| 6 | Diseño entidad-relación | `Diseño entidad-relación/` | ✅ hecho | 6 + índice | 0 + 9 |
| 7 | Normalización | `Normalización/` | ✅ hecho | 8 + índice | 0 |
| 8 | Lógica en la base de datos | `Lógica en la base de datos/` | ✅ hecho | 5 + índice | 0 |

## Convenciones
- Las mismas de Ingeniería de Software: prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- Tags `bd/<tema>` + `origen/apuntes` u `origen/complemento`.
- **Slides:** ningún PDF ni PPTX de las clases entra al repo, porque no declaran licencia. Las slides útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` dentro de un callout que cita la clase y se registran en `imagenes.json` con `tipo: "slide"` y `original: …pdf#page=N`.
- **Datos personales** del proyecto (teléfono, nombres de compañeros) no se migran; quedan en `aceptados` con su motivo.

## Registro
- **2026-10-11 — Infraestructura.** La configuración de IngSoft pasó a `_meta/Ingeniería de Software/`. `verificar.py` es multi-ramo (`--ramo`, `--raw` o `RAW_DIR`) y revisa autocontención y grafo sobre el vault completo. IngSoft: 0 errores, 0 advertencias.
- **2026-10-11 — Modelo relacional.**
  - Fuentes: Apuntes I1, «ALGEBRA RELACIONAL» (álgebra y el ejemplo de join), y Apuntes I2, «EXPLICACION LLAVES» (superllaves, candidatas, primaria). Complementos de las slides de las clases 1 (Motivación), 2 (Álgebra Relacional) y 3 (Repaso de llaves + SQL).
  - Notas de complemento puro: 01 DBMS, 02 Modelo relacional y 06 Consultas en álgebra relacional.
- **2026-10-11 — Definición de datos en SQL.**
  - Fuentes: Apuntes I1, «SQL 1» (crear tabla, llaves foráneas, modificar tabla, insertar datos), «Eliminación con llaves foráneas» y «RESTRICCION DE NULOS». Complementos de las slides de las clases 3 y 6.
  - Nota de complemento puro: 01 SQL y PostgreSQL. Enlaces cruzados a Active Record, Migraciones y Asociaciones de Ingeniería de Software.
- **2026-10-11 — Consultas SQL.**
  - Fuentes: Apuntes I1, «4. Consultas Sql (Query) + CRUD» y de «PRODUCTO CRUZ» a «DISTINCT»; Apuntes I2, «1. SQL Avanzado» (INNER, LEFT, RIGHT y FULL JOIN). Complementos de las slides de las clases 3 y 4.
  - El ítem vacío «Producto Cruz:» de la sección 4 quedó como aviso en la nota 03.
- **2026-10-11 — Agregación y subconsultas.**
  - Fuente: Apuntes I1, «SQL 2» hasta «NULL» (agregación, COUNT, GROUP BY, HAVING, anidadas, ALL/ANY, monótonas, correlacionadas, join anidado). Complementos de las slides de la clase 4.
  - El join anidado se dividió en dos notas (08 y 09) para no pasar de 150 líneas. Se detectó una inconsistencia de datos en el Ejemplo 2 (DUDAS).
- **2026-10-11 — Valores nulos.**
  - Fuente: Apuntes I1, «NULL» hasta «RESTRICCION DE NULOS» (esta última está en Definición de datos/07). Complementos de las slides de la clase 4: las tablas de verdad de AND, OR y NOT se transcribieron en Markdown.
- **2026-10-11 — Diseño entidad-relación.**
  - Sin contenido en mis apuntes: 6 notas de complemento puro basadas en las slides de las clases 5 y 6, con 9 diagramas en PNG (todos transcritos).
  - Se marcó la errata de la slide `email nombre varchar(30)`.
- **2026-10-11 — Normalización.**
  - Fuente: Apuntes I2, «2. Formas Normales y Dependencias» hasta «EXPLICACION LLAVES» (las llaves se migraron con Modelo relacional). Complementos de las slides de la clase 7.
  - Notas de complemento puro: 02 Reglas de inferencia y 08 Descomposición en BCNF y 3NF. Se agregó el link pendiente desde Diseño E/R/06.
- **2026-10-11 — Lógica en la base de datos.**
  - Fuente: Apuntes I2, «3. Lógica en Base de Datos» completa. Complementos de las slides de la clase 8 (vistas y su reescritura, vista vs vista materializada vs tabla, sintaxis de PL/pgSQL, loops, `RETURN QUERY EXECUTE`, conclusiones).
  - Se agregaron versiones PostgreSQL de los triggers con `CREATE`/`BEGIN…END`.
