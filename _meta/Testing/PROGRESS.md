# Progreso de la migración — Testing (IIC3745)

Rama: `migrar/testing`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Testing" --tema "<Tema>"` revisando el código de salida, y en las pausas y al cierre se verifican todos los ramos del vault.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Testing/`) | `_meta/Testing/` | ✅ hecho | – | – |
| 1 | Fundamentos del testing de software | `01-Fundamentos del testing de software/` | ✅ hecho | 4 + `_Índice` | 2 + 0 |
| 2 | Pruebas unitarias dobles de prueba y test smells | `02-Pruebas unitarias dobles de prueba y test smells/` | ✅ hecho | 5 + `_Índice` | 3 + 0 |
| 3 | Cobertura de código e instrumentación con settrace | `03-Cobertura de código e instrumentación con settrace/` | ✅ hecho | 4 + `_Índice` | 7 + 0 |
| 4 | Fuzzing aleatorio y fuzzing basado en mutación | `04-Fuzzing aleatorio y fuzzing basado en mutación/` | ✅ hecho | 3 + `_Índice` | 0 + 0 |
| 5 | Fuzzing basado en búsqueda | `05-Fuzzing basado en búsqueda/` | ✅ hecho | 3 + `_Índice` | 0 + 0 |
| 6 | Análisis de mutación y diseño de pruebas de caja negra | `06-Análisis de mutación y diseño de pruebas de caja negra/` | ✅ hecho | 5 + `_Índice` | 1 + 0 |
| 7 | Análisis estático y árboles de sintaxis abstracta | `07-Análisis estático y árboles de sintaxis abstracta/` | ✅ hecho | 5 + `_Índice` | 5 + 0 |
| 8 | Reglas de código automáticas y linters | `08-Reglas de código automáticas y linters/` | ✅ hecho | 4 + `_Índice` | 0 + 0 |
| 9 | Transformaciones de código con AST | `09-Transformaciones de código con AST/` | ✅ hecho | 5 + `_Índice` | 3 + 0 |
| 10 | Análisis de flujo de información y taint analysis | `10-Análisis de flujo de información y taint analysis/` | ✅ hecho | 3 + `_Índice` | 0 + 0 |
| 11 | Ejecución simbólica y fuzzing concólico | `11-Ejecución simbólica y fuzzing concólico/` | ✅ hecho | 5 + `_Índice` | 0 + 0 |
| 12 | Análisis dinámico y perfilado de ejecución | `12-Análisis dinámico y perfilado de ejecución/` | ✅ hecho | 4 + `_Índice` | 0 + 0 |
| 13 | Gestión del curso | `13-Gestión del curso/` | ✅ hecho | 2 + `_Índice` | 0 + 0 |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md) y [`_meta/Testing/NIVEL-DETALLE.md`](NIVEL-DETALLE.md): prosa explicativa para un estudiante de **2° año de Ciencia de la Computación**, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables (`[!question]-`).
- Sin comas en nombres de carpetas ni de notas; nombres únicos en todo el vault; sin marcas de procedencia («clase N», «décima», «actividad», «I1/I2») en los nombres ni en el texto de las notas.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador entrega advertencias informativas.
- **Énfasis en los apuntes del profesor y preparación I2:** Los capítulos del libro del profesor (`C0`–`C14`), los notebooks de Colab (`.ipynb`), los módulos de `instrumentor/` y `sampler/`, las actividades semanales (`Ac-1` a `Ac-4`) y las pautas de ejercicios (`10_EjerciciosI1.pdf` y `17-EjerciciosI2.pdf`) se integran directamente en los temas correspondientes.
- **Imágenes:** Las `.png` de Notion se copian con su SHA-256 intacto (`tipo: "apuntes"`), las fotos `.heic` se convierten a `.png` (`tipo: "convertida"`), y los diagramas útiles de slides o libros entran como `.png` (`tipo: "slide"`).

## Registro
- **2026-10-29 · Infraestructura.** Se crea la rama `migrar/testing` y `_meta/Testing/` (`mapeo.json` con los 13 temas, `imagenes.json` vacío, `PROGRESS.md`, `DUDAS.md` y `NIVEL-DETALLE.md`). Se verifican los 4 archivos HTML de Notion, los 12 capítulos del libro del profesor (`C0`–`C11`, `C14`), los 14 PDFs de slides y ejercicios (`00`–`17`), los notebooks `.ipynb` y los proyectos `instrumentor/` y `sampler/`. Temario aprobado por el usuario.
- **2026-10-29 · Temas 01 a 06 (Bloque I1).** Se migran los 6 temas del primer bloque (`01-Fundamentos del testing de software` a `06-Análisis de mutación y diseño de pruebas de caja negra`) con 24 notas de contenido, 6 índices y 13 imágenes de apuntes verificadas con SHA-256 / conversión `.heic`. Se integran `C0`–`C7`, slides `01`–`10`, notebooks `02`–`06.5`, décimas `D01`–`D06` y actividades `Ac-1` y `Ac-2`.
- **2026-10-29 · Temas 07 a 12 (Bloque I2).** Se migran exhaustivamente los 6 temas del segundo bloque (`07-Análisis estático y árboles de sintaxis abstracta` a `12-Análisis dinámico y perfilado de ejecución`) con 26 notas de contenido, 6 índices y 8 imágenes de apuntes verificadas. Se integran el 100% de los capítulos `C8`–`C14` del libro del profesor, todos los notebooks de `preparacion I2/`, `Clase-13/`, `Clase-15/`, los proyectos `instrumentor/` y `sampler/`, las actividades `Ac-3` y `Ac-4` y la totalidad de las preguntas y rúbricas de `17-EjerciciosI2.pdf`.
- **2026-10-29 · Tema 13 y cierre.** Se migra `13-Gestión del curso` (2 notas + `_Índice.md`), se completa `Testing/_Índice.md` y se verifica el ramo completo con `0 errores` y `0 advertencias de formato`.
