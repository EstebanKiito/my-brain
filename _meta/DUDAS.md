# Dudas y posibles errores en los apuntes originales

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta.

## Procesos de desarrollo
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[06 - Proceso unificado (RUP)\|Proceso unificado (RUP)]] | "Tiene su propio Lenguaje!!! → (UML)" | UML no es exclusivo de RUP: es un lenguaje de modelado general estandarizado por el OMG. Lo crearon los mismos autores (Rational), por eso aparecen juntos. Se agregó la precisión. |
| 🟡 | [[07 - Procesos incrementales\|Procesos incrementales]] | "No Feedback hasta terminar!" | Es discutible: cada pieza terminada puede mostrarse al usuario. Lo distintivo del incremental "puro" es que las piezas no se reelaboran con el feedback. Se agregó el matiz. |
| ✅ | [[05 - Modelo de prototipos\|Modelo de prototipos]] | "Reduce Improvistos → Menor tiempo de desarrollo" | Lo había marcado como dudoso, pero el libro del curso lo afirma ("menor tiempo de desarrollo porque no hay grandes sorpresas al final"). Sin cambios, solo se corrigió la errata "Improvistos" → "imprevistos". |

## Scrum
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - Product Owner\|Product Owner]] | "Asume Responsabilidad total del proyecto" | El libro dice "del **producto**". El PO responde por el valor del producto, pero no gestiona el proyecto ni decide cuánto trabajo entra en cada sprint. Se agregó la precisión. |
| 🟡 | [[08 - Sprint Backlog\|Sprint Backlog]] | *(contradicción entre fuentes, no en tus apuntes)* | El libro dice que una vez iniciado el sprint no se agregan ni quitan tareas; las slides dicen que cualquier miembro puede agregar, borrar o cambiar el sprint backlog. Según la Scrum Guide 2020, lo fijo es el **objetivo del sprint**; las tareas se ajustan. Se muestran ambas versiones. |
| ✅ | [[04 - Equipo de desarrollo Scrum\|Equipo de desarrollo Scrum]] | "Son autónomos, 5-8 personas" | Coincide con el libro. Las slides dicen 4–8 y la Scrum Guide 2020, 10 o menos (equipo completo). Se muestran las tres fuentes en una tabla. |
| ✅ | [[06 - Sprint\|Sprint]] | Imagen: "Sprint 1-4 weeks" | Las slides y el libro dicen 2–4 semanas y la Scrum Guide, un mes o menos. Se muestran todas. |
| ℹ️ | [[01 - Scrum\|Scrum]] | *(libro)* "desarrollado a fines de los años 90 por Ken Schwaber" | Scrum se presentó formalmente en 1995 por Schwaber y Sutherland. Se aclaró en un complemento; no afecta tus apuntes. |

## Historias de usuario
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[02 - Estructura de una historia de usuario\|Estructura de una historia de usuario]] | "Yo, como (type_usuario) neceisto (tarea) para (onjetivo)" | Solo erratas ("neceisto", "onjetivo"); se corrigieron sin cambiar el sentido. |
| ℹ️ | [[02 - Estructura de una historia de usuario\|Estructura de una historia de usuario]] | Ejemplo "Como usuario necesito recuperar mi contraseña…" | No es un error, pero el libro recomienda evitar el genérico "como usuario". Se agregó una nota aclarando cuándo es aceptable. |

## Planificación y estimación
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ | [[07 - Estimación de software\|Estimación de software]] | "8. Estimaciones:" (solo el título) | Se completó con las slides y el libro; todas las notas del tema son complemento. |

## Ruby
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - Convenciones de estilo en Ruby\|Convenciones de estilo en Ruby]] | "lista.reverse → !Cambia definitivamente" | `reverse` no modifica la lista; `reverse!` sí. Se agregó el ejemplo con ambas. |
| 🟡 | [[02 - Convenciones de estilo en Ruby\|Convenciones de estilo en Ruby]] | "lista = [1,2] → is_even? → true/false" | El método es `even?` y es de Integer, no de Array. La idea correcta: los métodos con `?` devuelven booleanos. |
| 🟡 | [[02 - Convenciones de estilo en Ruby\|Convenciones de estilo en Ruby]] | "Convenciones → snake_case →PascalCase" | Falta decir a qué se aplica cada una: `snake_case` para variables, métodos y archivos; `PascalCase` para clases y módulos. Se agregó la tabla del libro. |
| ℹ️ | [[05 - Arreglos y hashes en Ruby\|Arreglos y hashes en Ruby]] | *(slides y libro)* `inst["c"] # devuelve 2` | Error de las fuentes, no tuyo: una clave inexistente devuelve `nil`. |

## Programación orientada a objetos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[05 - Atributos y accesores en Ruby\|Atributos y accesores]] | "Por default los metodos son PRIVADOS…" | La slide dice que son los **atributos** los privados por defecto; en Ruby los métodos son públicos por defecto. |
| 🟡 | [[03 - Visibilidad de métodos en Ruby\|Visibilidad de métodos]] | "Public: - - -", "Protected: - - -" | Incompletos; se completaron en un complemento. |
| 🟡 | [[04 - Constructor initialize en Ruby\|Constructor initialize]] | `class Persona … Person.new` | El nombre de la clase no coincide (NameError). Se agregó la versión corregida. |
| 🟡 | [[05 - Atributos y accesores en Ruby\|Atributos y accesores]] | `attr_accesor :name, :gender # Crea los metodos name= y gender=` | Es `attr_accessor`, y crea además los getters `name` y `gender`. Falta `end`. |
| 🟡 | [[06 - Variables de clase en Ruby\|Variables de clase]] | `ass Person` | Debe ser `class Person`. |
| 🟡 | [[07 - Herencia en Ruby\|Herencia]] | `attr_accessor: :stroke :fill`, `attr_accesor: :radius`, `:lenght` | Sintaxis: `attr_accessor :stroke, :fill`; faltan los `end`. |
| 🟡 | [[08 - super en Ruby\|super]] | `class Hijo` (sin `< Padre`) | Sin herencia, `super` no llama a `Padre#initialize`. Faltan los `end`. |
| 🟡 | [[11 - Polimorfismo y duck typing\|Polimorfismo]] | `attr_accessor :base :altura`, sin `end` | Falta la coma y los `end`; la idea es correcta. |
| ℹ️ | [[06 - Variables de clase en Ruby\|Variables de clase]] | *(slides)* `Song.new` sin argumentos | El `initialize` pide 3 argumentos; en el complemento se agregaron. |

## Detectadas para temas pendientes
Se resolverán, con su callout en la nota, cuando se migre cada tema:
- **Rails:**
  - `post “/pokemon”, to: “pokemons#create”)`: paréntesis sobrante y `/pokemon` vs `/pokemons`.
  - `create_table: pokemons` debería ser `create_table :pokemons`.
  - "generate migration … (tiene que ser en singular)": lo singular es el nombre del modelo.
  - `<& end %>` y `pokemon_tupe` en la vista ERB.
  - Link roto de Notion `https://app.notion.comundefined` junto a la imagen de Formularios Rails (no se migra).
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
