---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Convenciones de estilo en Ruby

Ruby tiene convenciones fuertes de nombres y formato: `snake_case`, `PascalCase`, indentación de 2 espacios y métodos terminados en `?` o `!`.

## Mis apuntes
- **Convenciones** → `snake_case` → `PascalCase`
- `lista = [1,2]` → `is_even?` → true/false
- `lista.reverse` → `!` cambia definitivamente
- **Indentación de 2 espacios**

> [!warning] Posible error / precisiones (registrado en `_meta/DUDAS.md`)
> - **`snake_case` y `PascalCase` se usan para cosas distintas:** `snake_case` para variables, métodos y archivos; `PascalCase` para clases y módulos (ver la tabla de abajo).
> - **`is_even?`:** en Ruby el método se llama `even?` y es de los **enteros**, no de las listas: `2.even? # => true`. Sobre una lista habría que hacer, por ejemplo, `lista.all?(&:even?)` o `lista.select(&:even?)`. La idea correcta del apunte es que **los métodos que terminan en `?` devuelven `true` o `false`**.
> - **`reverse` vs `reverse!`:** `lista.reverse` **no** modifica la lista; devuelve una nueva. La versión con `!`, `lista.reverse!`, es la que **cambia definitivamente** la lista. Por convención, el `!` marca la versión "peligrosa", la que modifica el objeto.
>
> ```ruby
> lista = [1, 2]
> lista.reverse    # => [2, 1]
> lista            # => [1, 2]   (no cambió)
> lista.reverse!   # => [2, 1]
> lista            # => [2, 1]   (cambió)
> ```

> [!tip] Complemento — tabla de convenciones (libro del curso, cap. 10.9)
> | Elemento | Convención | Ejemplo |
> |---|---|---|
> | Variables locales y métodos | minúscula, `snake_case` (o empiezan con `_`) | `name`, `fish_and_chips`, `_26` |
> | Variables globales | empiezan con `$` | `$debug` |
> | Variables de instancia | empiezan con `@` | `@name` |
> | Variables de clase | empiezan con `@@` | `@@total_plays` |
> | Constantes | todo en mayúsculas | `SINGLE`, `PI` |
> | Clases y módulos | mayúscula inicial en cada palabra (`PascalCase`) | `MyClass`, `FeedPerMile` |
> | Archivos | minúscula y `_` entre palabras | `hard_drive.rb` |
>
> En los nombres de métodos son válidos los caracteres `?`, `!` y `=`, como en `empty?`, `reverse!` y `name=` (setter).

## Preguntas de repaso

1. ¿Qué convención de nombre usan los métodos y cuál las clases?
> [!question]- Respuesta
> Los métodos y variables usan `snake_case` (por ejemplo, `calcular_total`). Las clases y módulos usan `PascalCase` (por ejemplo, `ShoppingCar`).

2. ¿Qué diferencia hay entre `lista.reverse` y `lista.reverse!`?
> [!question]- Respuesta
> `reverse` devuelve un arreglo nuevo invertido y deja el original igual. `reverse!` invierte el arreglo original, modificándolo.

3. ¿Qué indica por convención un método terminado en `?`?
> [!question]- Respuesta
> Que es un predicado: devuelve `true` o `false`, como `empty?` o `even?`.

4. ¿Cuántos espacios de indentación se usan en Ruby?
> [!question]- Respuesta
> Dos espacios.
