---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[07 - Herencia en Ruby|Herencia en Ruby]]", "[[04 - Constructor initialize en Ruby|Constructor initialize en Ruby]]"]
---
# super en Ruby

`super` llama al **método con el mismo nombre en la clase padre**. Se usa sobre todo para reutilizar el constructor del padre y para extender un método sobrescrito.

## Super
```ruby
class Padre
	def initialize
		"Soy el padre"
	end

class Hijo
	def initialize
		super         # -> super: ejecutara el Constructor (initialize) del Padre
	end
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> `class Hijo` no hereda de `Padre`: falta `< Padre`. Sin eso, `super` buscaría el `initialize` de `Object`. También faltan los `end` de las clases.
> ```ruby
> class Padre
>   def initialize
>     puts "Soy el padre"
>   end
> end
>
> class Hijo < Padre
>   def initialize
>     super          # ejecuta el initialize de Padre
>   end
> end
>
> Hijo.new   # imprime "Soy el padre"
> ```

## Herencia y constructor
```ruby
# Este ejemplo: ejecuta el constructor padre mandando atributos necesarios
class Figure
	attr_accesor: :stroke, :fill
	#---------------------------
	def initialize(stroke, fill)
		@stroke = stroke
		@fill = fill
	end
	#---------------------------
end

class Circle < Figure
	attr_accesor: :radius

	def initialize(stroke, fill, radius)
		super(stroke, fill) # -> Constructor del padre con sus respectivos attr
		@radius = radius
	end
end
```
*(`attr_accesor:` debe ser `attr_accessor`; ver [[05 - Atributos y accesores en Ruby|Atributos y accesores]].)*

## Super y override
- Con **"super"** podemos llamar al método de la clase padre con el mismo nombre.

```ruby
class Empleado
	def calcular_salario
		...
	end

class Manager < Empleado
	def calcular_salario
		base_salario = super
		base_salario + @bonus
	end
```

> [!tip] Complemento — `super` vs `super()` (slides "Ruby": Song y KaraokeSong)
> | Forma | Argumentos que pasa al padre |
> |---|---|
> | `super` (sin paréntesis) | **Los mismos** que recibió el método actual |
> | `super()` | **Ninguno** |
> | `super(a, b)` | Exactamente `a` y `b` |
>
> ```ruby
> class KaraokeSong < Song
>   def initialize(name, artist, duration, lyrics)
>     super(name, artist, duration)   # el padre no recibe lyrics
>     @lyrics = lyrics
>   end
>
>   def to_s
>     super + " [#{@lyrics}]"         # extiende el to_s del padre
>   end
> end
> # "Song: My Way--Sinatra (225) [And now, the...]"
> ```
> Aquí se usa `super(name, artist, duration)` explícito porque, con un `super` "pelado", se le pasarían los 4 argumentos al `initialize` de `Song`, que solo acepta 3, y daría `ArgumentError`.

## Preguntas de repaso

1. ¿Qué hace `super` dentro de un método?
> [!question]- Respuesta
> Busca y ejecuta el método del mismo nombre empezando por la clase padre de donde está escrito, y devuelve su resultado.

2. ¿Qué diferencia hay entre `super` y `super()`?
> [!question]- Respuesta
> `super` reenvía los mismos argumentos que recibió el método; `super()` llama al método del padre sin argumentos.

3. En `Manager#calcular_salario`, ¿qué valor tiene `base_salario`?
> [!question]- Respuesta
> El resultado de `Empleado#calcular_salario`, el salario base, al que luego se suma `@bonus`.
