# Progreso de la migración — Programación en C (material de IIC2133)

Rama: `migrar/estructuras-de-datos` (compartida por Estructuras de Datos y Programación en C). Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Programación en C" --tema "<Tema>"` revisando el código de salida; al cerrar cada bloque de temas, la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Programación en C/`, cobertura reescrita en `verificar.py`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos del lenguaje | `01-Fundamentos del lenguaje/` | pendiente | – | – |
| 2 | Punteros, arreglos y strings | `02-Punteros, arreglos y strings/` | pendiente | – | – |
| 3 | Memoria dinámica y Valgrind | `03-Memoria dinámica y Valgrind/` | pendiente | – | – |
| 4 | Structs | `04-Structs/` | pendiente | – | – |
| 5 | Módulos, compilación y depuración | `05-Módulos, compilación y depuración/` | pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): prosa reescrita, sin marcas de procedencia ni citas literales, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables.
- Prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador da advertencias y no errores, porque ya no se copia literal. Las pruebas [1], [2], [4] y [5] siguen siendo errores.
- **Slides:** ningún PDF entra al repo. Las útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` dentro de un callout que cita la clase y se registran con `tipo: "slide"` y `original: …pdf#page=N`.
- **Imágenes HEIC:** se convierten a PNG con `sips` y se registran con `tipo: "convertida"`.
- **Fuentes:** Cápsulas de C (apuntes propios), las 11 páginas del CheatSheet C y el Taller introductorio (material del curso), más las guías `.md` de setup y depuración como complemento.
- **Código:** todo snippet C compila con `gcc -Wall -Wextra` en macOS y se ejecuta antes del commit.
- Las notas de `Estructuras de Datos/` enlazan a estas como prerrequisito.

## Registro
