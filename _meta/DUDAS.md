# Dudas y posibles errores en los apuntes originales

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta.

## Procesos de desarrollo
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[06 - Proceso unificado (RUP)\|Proceso unificado (RUP)]] | "Tiene su propio Lenguaje!!! → (UML)" | UML no es exclusivo de RUP: es un lenguaje de modelado general estandarizado por el OMG. Lo crearon los mismos autores (Rational), por eso aparecen juntos. Se agregó la precisión. |
| 🟡 | [[07 - Procesos incrementales\|Procesos incrementales]] | "No Feedback hasta terminar!" | Es discutible: cada pieza terminada puede mostrarse al usuario. Lo distintivo del incremental "puro" es que las piezas no se reelaboran con el feedback. Se agregó el matiz. |
| ✅ | [[05 - Modelo de prototipos\|Modelo de prototipos]] | "Reduce Improvistos → Menor tiempo de desarrollo" | Lo había marcado como dudoso, pero el libro del curso lo afirma ("menor tiempo de desarrollo porque no hay grandes sorpresas al final"). Sin cambios, solo se corrigió la errata "Improvistos" → "imprevistos". |

## Detectadas para temas pendientes
Se resolverán, con su callout en la nota, cuando se migre cada tema:
- **Scrum:**
  - Equipo de 5–8 personas (tus apuntes y el libro) vs. 4–8 (slides). No es un error: se mostrarán ambas fuentes.
- **Ruby:**
  - `lista.reverse → !Cambia definitivamente`: `reverse` no muta, `reverse!` sí.
  - `is_even?` sobre una lista: en Ruby `even?` es método de Integer.
  - Las convenciones "snake_case → PascalCase" no dicen a qué se aplica cada una.
- **Rails:**
  - `post “/pokemon”, to: “pokemons#create”)`: paréntesis sobrante y `/pokemon` vs `/pokemons`.
  - `create_table: pokemons` debería ser `create_table :pokemons`.
  - "generate migration … (tiene que ser en singular)": lo singular es el nombre del modelo.
  - `<& end %>` y `pokemon_tupe` en la vista ERB.
  - Link roto de Notion `https://app.notion.comundefined` junto a la imagen de Formularios Rails (no se migra).
- **POO:**
  - "Por default los métodos son PRIVADOS": en la slide son los *atributos*; en Ruby los métodos son públicos por defecto.
  - "Public: - - -" y "Protected: - - -" están incompletos.
  - `attr_accesor`, `attr_accessor: :stroke :fill`, `ass Person`.
  - `class Persona` con `Person.new`.
  - `class Hijo` sin `< Padre`.
- **UML:**
  - Composición: "Los objetos de B son creados dentro de B"; probablemente "dentro de A" (así dice la slide).
- **Patrones:**
  - Decorator, "Solución: Herencia y Dependencia": el patrón usa composición.
  - "Template Method — Ejemplo Diagrama (ya visto)": no queda claro a qué ejemplo se refiere.
  - Builder: `director.builder` sin `attr_reader :builder`, lo que da NoMethodError.
  - "SINGLETON (YO)": no queda claro qué significa "(YO)".
- **Gestión del curso:**
  - Fechas y ponderaciones de la página del ramo y del CSV (2024) no coinciden con el esquema del PDF 0 (I1/I2 de otra versión del curso).
  - La lista de contenidos de "Resumen Prueba Práctica" nombra DOCUMENTACIÓN y QUALITY ASSESSMENT, pero no tienen contenido en ninguna fuente.
  - "Resumen Software Pt 1", §8 "Estimaciones", solo tiene el título.
