---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Clases y objetos en Ruby|Clases y objetos en Ruby]]"]
---
# Constructor initialize en Ruby

En Ruby el constructor es el método `initialize`. `Clase.new(...)` crea el objeto y luego llama automáticamente a `initialize` con esos argumentos.

## Constructor 👷🏻‍♂️
- El `new` es un **método de clase** que se ejecuta sobre la clase `Person`.
- Crea una **instancia** de la clase.
- Posteriormente llama al método **`initialize`** sobre el objeto recién creado.

```ruby
class Persona

	def initialize
		puts "Creando Persona Nueva"
	end
end
Person.new # Imprimira lo del metodo -> "Creando Persona Nueva"
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> La clase se llama `Persona`, pero se instancia `Person.new`. Así daría `NameError: uninitialized constant Person`. Versión corregida:
> ```ruby
> class Persona
>   def initialize
>     puts "Creando Persona Nueva"
>   end
> end
> Persona.new # imprime "Creando Persona Nueva"
> ```

> [!tip] Complemento — constructor con parámetros
> ```ruby
> class Persona
>   def initialize(name, edad = 18)   # parámetro con valor por defecto
>     @name = name
>     @edad = edad
>   end
> end
>
> Persona.new("Ana")       # edad = 18
> Persona.new("Beto", 30)
> ```
> - `initialize` siempre es **privado**: no se puede llamar como `obj.initialize`.
> - Lo que devuelve `initialize` se ignora: `new` siempre devuelve el objeto creado.
> - En herencia, el constructor del padre se llama con `super` (ver [[08 - super en Ruby|super en Ruby]]).

## Preguntas de repaso

1. ¿Qué hace `Persona.new("Ana")` paso a paso?
> [!question]- Respuesta
> `new` (método de clase) crea una instancia vacía de `Persona` y luego llama a `initialize("Ana")` sobre esa instancia. Finalmente devuelve el objeto.

2. ¿Qué devuelve `new` si `initialize` termina con `"hola"`?
> [!question]- Respuesta
> Devuelve el objeto creado; el valor de retorno de `initialize` se ignora.

3. ¿Por qué falla el ejemplo `class Persona … end; Person.new`?
> [!question]- Respuesta
> Porque la constante `Person` no está definida: la clase se llama `Persona`.
