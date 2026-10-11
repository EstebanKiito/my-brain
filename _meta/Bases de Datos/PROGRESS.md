# Progreso de la migración — Bases de Datos (IIC2413)

Rama: `migrar/bases-de-datos`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Bases de Datos"` (y la verificación de Ingeniería de Software, porque el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura multi-ramo (`verificar.py --ramo`, `_meta/<Ramo>/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Modelo relacional | `Modelo relacional/` | ✅ hecho | 6 + índice | 0 + 3 |
| 2 | Definición de datos en SQL | `Definición de datos en SQL/` | ✅ hecho | 7 + índice | 0 |

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
