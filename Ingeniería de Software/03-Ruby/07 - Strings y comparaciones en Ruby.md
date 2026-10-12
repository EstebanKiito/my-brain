---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/complemento]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Strings y comparaciones en Ruby

*En mis apuntes solo quedó "Comparaciones / Strings / otros de clase"; el contenido viene de las slides y del conocimiento general de Ruby.*

> [!tip] Complemento — strings (slides "Ruby")
> ```ruby
> puts "texto"              # imprime texto
> puts 'texto'              # imprime texto
> puts "texto\n"            # imprime texto y un salto de línea
> puts "suma :#{1+2}"       # imprime "suma :3"      (comillas dobles: interpolan)
> puts 'suma :#{1+2}'       # imprime "suma :#{1+2}" (comillas simples: literal)
> ```
> - **Comillas dobles** permiten **interpolación** `#{…}` y secuencias como `\n`.
> - **Comillas simples** dejan el texto tal cual.
>
> ```ruby
> s = "Hola"
> s.length          # 4
> s.upcase          # "HOLA"
> s + " mundo"      # "Hola mundo" (nuevo string)
> s << "!"          # modifica s: "Hola!"
> s * 2             # "Hola!Hola!"
> s.include?("ol")  # true
> ```

> [!tip] Complemento — comparaciones
> | Operador | Compara | Ejemplo |
> |---|---|---|
> | `==` | igualdad de **valor** | `"a" == "a"` → `true` |
> | `!=` | distinto | `1 != 2` → `true` |
> | `<`, `>`, `<=`, `>=` | orden | `"a" < "b"` → `true` |
> | `<=>` | "nave espacial": -1, 0 o 1 (lo usa `sort`) | `1 <=> 2` → `-1` |
> | `equal?` | **mismo objeto** (identidad) | `"a".equal?("a")` → `false` |
> | `eql?` | valor **y** tipo | `1.eql?(1.0)` → `false`; `1 == 1.0` → `true` |
>
> Los operadores lógicos son `&&`, `||` y `!` (también `and`, `or` y `not`, con menor precedencia). En Ruby **solo `false` y `nil` son falsos**: `0` y `""` son verdaderos.

## Preguntas de repaso

1. ¿Qué imprime `puts 'suma :#{1+2}'`?
> [!question]- Respuesta
> `suma :#{1+2}` literal, porque con comillas simples no hay interpolación.

2. ¿Qué diferencia hay entre `==` y `equal?`?
> [!question]- Respuesta
> `==` compara valores (dos strings con el mismo texto son iguales). `equal?` compara identidad: solo es `true` si es exactamente el mismo objeto.

3. ¿El número `0` es verdadero o falso en un `if` de Ruby?
> [!question]- Respuesta
> Verdadero. En Ruby solo `false` y `nil` son falsos.
