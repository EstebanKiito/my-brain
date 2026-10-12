---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Métodos y retorno implícito en Ruby

Los métodos se definen con `def … end`. **Devuelven automáticamente el valor de la última expresión evaluada** (retorno implícito); `return` sale del método en ese mismo momento.

## Retorno de métodos (mis apuntes)
Con `return` explícito, el método **sale en esa línea** y lo que viene después nunca se ejecuta:
```ruby
def nivel
	return pokemon.nivel
	pokemon.nivel = 4
	pokemon.nivel
end

nivel -> pokemon.nivel
```

Sin `return`, se devuelve **la última expresión**. Una asignación también es una expresión: vale lo asignado.
```ruby
def nivel
	variable = 5
end

nivel -> retorna 5 xd
```

> [!tip] Complemento — definir y llamar métodos (slides "Ruby" y libro del curso, cap. 10.4)
> ```ruby
> def sum(n1, n2)
>   n1 + n2              # retorno implícito
> end
> sum(3, 4)              # devuelve 7
> sum("cat", "dog")      # devuelve "catdog" (duck typing: + funciona con strings)
>
> def multiply(val1, val2)
>   result = val1 * val2
>   return result        # retorno explícito (equivalente)
> end
> puts multiply(10, 20)  # imprime 200
>
> def say_goodnight(name)
>   "Good night, #{name}"
> end
> puts say_goodnight('Ma')   # imprime Good night, Ma
> puts say_goodnight 'Ma'    # los paréntesis son opcionales
> ```

> [!example] Ejemplo extra — `return` anticipado (guard clause)
> ```ruby
> def dividir(a, b)
>   return "no se puede dividir por cero" if b == 0
>   a / b
> end
> dividir(10, 2)  # => 5
> dividir(1, 0)   # => "no se puede dividir por cero"
> ```
> El estilo idiomático de Ruby usa `return` solo para salir antes; al final del método se omite.

## Preguntas de repaso

1. ¿Qué devuelve un método de Ruby si no tiene `return`?
> [!question]- Respuesta
> El valor de la última expresión evaluada. Si es una asignación como `variable = 5`, devuelve 5.

2. En el primer ejemplo de los apuntes, ¿se ejecuta `pokemon.nivel = 4`?
> [!question]- Respuesta
> No. `return pokemon.nivel` sale del método inmediatamente, así que las líneas siguientes nunca se ejecutan.

3. ¿Qué devuelve `sum("cat", "dog")` si `sum` hace `n1 + n2`?
> [!question]- Respuesta
> `"catdog"`, porque `+` concatena strings. El método funciona con cualquier objeto que responda a `+`.
