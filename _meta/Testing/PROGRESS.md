# Progreso de la migración — Testing (IIC3745)

Rama: `migrar/testing`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Testing" --tema "<Tema>"` revisando el código de salida, y en las pausas y al cierre se verifican todos los ramos del vault.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Testing/`) | `_meta/Testing/` | ✅ hecho | – | – |
| 1 | Fundamentos del testing de software | `01-Fundamentos del testing de software/` | ✅ hecho | 4 + `_Índice` | 2 + 0 |
| 2 | Pruebas unitarias dobles de prueba y test smells | `02-Pruebas unitarias dobles de prueba y test smells/` | ✅ hecho | 5 + `_Índice` | 3 + 0 |
| 3 | Cobertura de código e instrumentación con settrace | `03-Cobertura de código e instrumentación con settrace/` | ✅ hecho | 4 + `_Índice` | 7 + 0 |
| 4 | Fuzzing aleatorio y fuzzing basado en mutación | `04-Fuzzing aleatorio y fuzzing basado en mutación/` | ⏳ pendiente | – | – |
| 5 | Fuzzing basado en búsqueda | `05-Fuzzing basado en búsqueda/` | ⏳ pendiente | – | – |
| 6 | Análisis de mutación y diseño de pruebas de caja negra | `06-Análisis de mutación y diseño de pruebas de caja negra/` | ⏳ pendiente | – | – |
| 7 | Análisis estático y árboles de sintaxis abstracta | `07-Análisis estático y árboles de sintaxis abstracta/` | ⏳ pendiente | – | – |
| 8 | Reglas de código automáticas y linters | `08-Reglas de código automáticas y linters/` | ⏳ pendiente | – | – |
| 9 | Transformaciones de código con AST | `09-Transformaciones de código con AST/` | ⏳ pendiente | – | – |
| 10 | Análisis de flujo de información y taint analysis | `10-Análisis de flujo de información y taint analysis/` | ⏳ pendiente | – | – |
| 11 | Ejecución simbólica y fuzzing concólico | `11-Ejecución simbólica y fuzzing concólico/` | ⏳ pendiente | – | – |
| 12 | Análisis dinámico y perfilado de ejecución | `12-Análisis dinámico y perfilado de ejecución/` | ⏳ pendiente | – | – |
| 13 | Gestión del curso | `13-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md) y [`_meta/Testing/NIVEL-DETALLE.md`](NIVEL-DETALLE.md): prosa explicativa para un estudiante de **2° año de Ciencia de la Computación**, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables (`[!question]-`).
- Sin comas en nombres de carpetas ni de notas; nombres únicos en todo el vault; sin marcas de procedencia («clase N», «décima», «actividad», «I1/I2») en los nombres ni en el texto de las notas.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador entrega advertencias informativas.
- **Énfasis en los apuntes del profesor y preparación I2:** Los capítulos del libro del profesor (`C0`–`C14`), los notebooks de Colab (`.ipynb`), los módulos de `instrumentor/` y `sampler/`, las actividades semanales (`Ac-1` a `Ac-4`) y las pautas de ejercicios (`10_EjerciciosI1.pdf` y `17-EjerciciosI2.pdf`) se integran directamente en los temas correspondientes.
- **Imágenes:** Las `.png` de Notion se copian con su SHA-256 intacto (`tipo: "apuntes"`), las fotos `.heic` se convierten a `.png` (`tipo: "convertida"`), y los diagramas útiles de slides o libros entran como `.png` (`tipo: "slide"`).

## Registro
- **2026-10-29 · Infraestructura.** Se crea la rama `migrar/testing` y `_meta/Testing/` (`mapeo.json` con los 13 temas, `imagenes.json` vacío, `PROGRESS.md`, `DUDAS.md` y `NIVEL-DETALLE.md`). Se verifican los 4 archivos HTML de Notion, los 12 capítulos del libro del profesor (`C0`–`C11`, `C14`), los 14 PDFs de slides y ejercicios (`00`–`17`), los notebooks `.ipynb` y los proyectos `instrumentor/` y `sampler/`. Temario aprobado por el usuario.
