---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/complemento]
prerrequisitos: ["[[04 - Bloques y yield en Ruby|Bloques y yield en Ruby]]"]
---
# Estructuras de control e iteradores en Ruby

> [!tip] Complemento — nota nueva (fuente: slides "Ruby" y libro del curso, cap. 10.8)
> **Qué es:** cómo tomar decisiones (`if`) y repetir (`while`, iteradores) en Ruby.
>
> ## if / elsif / else
> ```ruby
> if count > 10
>   puts "Try again"
> elsif tries == 3
>   puts "You lose"
> else
>   puts "Enter a number"
> end
> ```
>
> ## while
> ```ruby
> while weight < 100 and num_pallets <= 30
>   pallet = next_pallet()
>   weight += pallet.weight
>   num_pallets += 1
> end
> ```
>
> ## Iteradores
> Son **métodos que reciben un bloque** (ver [[04 - Bloques y yield en Ruby|Bloques y yield]]). `each` llama al bloque una vez por cada elemento.
> ```ruby
> animals = ["ant", "bee", "cat", "dog", "elk"]
> animals.each { |animal| puts animal }      # forma 1 (idiomática)
> for animal in animals do                   # forma 2
>   puts animal
> end
>
> 3.times { print "X " }                     # X X X
> 1.upto(5) { |i| print i, " " }             # 1 2 3 4 5
> 99.downto(95) { |i| print i, " " }         # 99 98 97 96 95
> 50.step(80, 5) { |i| print i, " " }        # 50 55 60 65 70 75 80
> ```

> [!example] Ejemplo extra — modificadores y `unless`
> ```ruby
> puts "mayor de edad" if edad >= 18        # if al final de la línea
> puts "sin stock" unless stock > 0         # unless = if not
>
> case nota
> when 6.0..7.0 then "excelente"
> when 4.0...6.0 then "aprobado"
> else "reprobado"
> end
> ```

## Preguntas de repaso

1. ¿Qué imprime `50.step(80, 5) { |i| print i, " " }`?
> [!question]- Respuesta
> `50 55 60 65 70 75 80`.

2. ¿Qué es un iterador en Ruby?
> [!question]- Respuesta
> Un método que recibe un bloque y lo ejecuta repetidamente, por ejemplo una vez por cada elemento (`each`) o n veces (`times`).

3. ¿Cómo se escribe "si no" en Ruby sin usar `!`?
> [!question]- Respuesta
> Con `unless`: `puts "vacío" unless lista.any?`.
