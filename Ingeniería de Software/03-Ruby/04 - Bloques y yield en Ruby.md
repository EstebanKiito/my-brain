---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/complemento]
prerrequisitos: ["[[03 - Métodos y retorno implícito en Ruby|Métodos y retorno implícito en Ruby]]"]
---
# Bloques y yield en Ruby

> [!tip] Complemento — nota nueva (fuente: slides "Ruby" y libro del curso, cap. 10.4)
> **Qué es:** un **bloque** es una "función anónima" que se pasa a un método, entre `{ }` o `do … end`. Dentro del método, **`yield`** ejecuta ese bloque y le pasa argumentos.
>
> ```ruby
> def call_block
>   yield("hello", 2)          # ejecuta el bloque con "hello" y 2
> end
>
> call_block { |s, n| puts s * n, "\n" }   # imprime hellohello
> ```
>
> - `|s, n|` son los parámetros que recibe el bloque.
> - `s * n` con un string lo repite: `"hello" * 2` da `"hellohello"`.
> - Los **iteradores** como `each` y `times` son justamente métodos que reciben un bloque (ver [[06 - Estructuras de control e iteradores en Ruby|Estructuras de control e iteradores]]).

> [!example] Ejemplo extra — `{ }` vs `do … end` y `block_given?`
> ```ruby
> [1, 2, 3].each { |x| puts x }   # una línea: llaves
>
> [1, 2, 3].each do |x|           # varias líneas: do ... end
>   doble = x * 2
>   puts doble
> end
>
> def saludar
>   return "sin bloque" unless block_given?
>   yield("Ana")
> end
> saludar { |nombre| "Hola #{nombre}" }   # => "Hola Ana"
> saludar                                 # => "sin bloque"
> ```

## Preguntas de repaso

1. ¿Qué hace `yield` dentro de un método?
> [!question]- Respuesta
> Ejecuta el bloque que se le pasó al método, entregándole los argumentos que se pongan en `yield(...)`.

2. ¿Qué imprime `call_block { |s, n| puts s * n }` si `call_block` hace `yield("hello", 2)`?
> [!question]- Respuesta
> `hellohello`.

3. ¿Qué relación hay entre bloques e iteradores como `each`?
> [!question]- Respuesta
> Los iteradores son métodos que reciben un bloque y lo ejecutan (con `yield`) una vez por cada elemento.
