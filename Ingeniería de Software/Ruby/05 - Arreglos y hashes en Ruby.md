---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/complemento]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Arreglos y hashes en Ruby

> [!tip] Complemento — nota nueva (fuente: slides "Ruby" y libro del curso, cap. 10.7)
> **Qué es:** los arreglos (`Array`) guardan elementos por **índice**; los hashes (`Hash`) guardan pares **clave → valor**. Ambos son objetos con muchos métodos.
>
> ## Arreglos
> ```ruby
> days_of_week = Array.new           # []
> days_of_week.empty?                # true  (los métodos pueden terminar en ?)
> Array.new(7)                       # [nil, nil, nil, nil, nil, nil, nil]
> Array.new(7, "today")              # ["today", "today", ...] 7 veces
>
> days_of_week = Array[ "Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun" ]
> days_of_week.at(0)                 # devuelve "Mon"
> days_of_week.size                  # devuelve 7
> days_of_week.empty?                # devuelve false
>
> days_of_week = [ "Mon", "Tue", "Wed", "Thu", "Fri" ]   # forma literal
> days_of_week[0]                    # devuelve "Mon"
> days_of_week[1]                    # devuelve "Tue"
>
> days1 = ["Mon", "Tue", "Wed"]
> days2 = ["Thu", "Fri", "Sat", "Sun"]
> days = days1 + days2               # + concatena arreglos
>
> colors = ["red", "green", "blue"]
> colors[1] = "yellow"               # asigna "yellow"
> colors                             # ["red", "yellow", "blue"]
> ```
>
> ## Hashes
> ```ruby
> inst = { "a" => 1, "b" => 2 }
> inst["a"]          # devuelve 1
> inst["c"]          # devuelve nil (la clave no existe)
>
> inst = Hash.new(0) # valor por defecto 0 para claves inexistentes
> inst["a"]          # devuelve 0
> inst["a"] += 1
> inst["a"]          # devuelve 1
> ```

> [!warning] Error en las slides y el libro
> Ambos dicen que `inst["c"]` "devuelve 2". **Es un error:** `"c"` no está en el hash, así que devuelve `nil`. Solo con `Hash.new(valor)` se obtiene un valor por defecto. También están desordenados los comentarios del ejemplo de `Hash.new(0)`: primero devuelve 0 y, después del `+= 1`, devuelve 1. Registrado en `_meta/DUDAS.md`.

> [!example] Ejemplo extra — métodos muy usados
> ```ruby
> nums = [3, 1, 4, 1, 5]
> nums.sort            # [1, 1, 3, 4, 5]
> nums.map { |n| n * 2 }     # [6, 2, 8, 2, 10]
> nums.select(&:even?)       # [4]
> nums.include?(4)           # true
> nums.push(9)               # agrega al final (también nums << 9)
>
> edades = { ana: 20, beto: 25 }   # claves símbolo
> edades[:ana]                     # 20
> edades.each { |nombre, edad| puts "#{nombre}: #{edad}" }
> ```
> `Hash.new(0)` es ideal para contar ocurrencias: `conteo[palabra] += 1`.

## Preguntas de repaso

1. ¿Qué devuelve `{ "a" => 1 }["z"]` y qué devuelve `Hash.new(0)["z"]`?
> [!question]- Respuesta
> El primero devuelve `nil`, porque la clave no existe. El segundo devuelve `0`, el valor por defecto del constructor.

2. ¿Qué crea `Array.new(3, "x")`?
> [!question]- Respuesta
> `["x", "x", "x"]`.

3. ¿Cómo se concatenan dos arreglos?
> [!question]- Respuesta
> Con `+`: `[1, 2] + [3]` da `[1, 2, 3]`.
