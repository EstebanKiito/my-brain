---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[05 - Atributos y accesores en Ruby|Atributos y accesores en Ruby]]"]
---
# Variables de clase en Ruby

Una **variable de clase** (`@@`) es **compartida por todas las instancias** de la clase, a diferencia de un atributo de instancia (`@`), que es propio de cada objeto.

## Atributos compartidos por instancias distintas
- `@` → atributo de **instancia**
- `@@` → atributo de **clase**

```ruby
ass Person
	@@contador_personas = 0

	def initialize
		@@contador_personas += 1
		end

	# Metodp para visuializar el atributo
	def self.contador_personas
		@@contador_personas
	end
end

puts Person.contador_personas # 0
Person.new
puts Person.contador_personas # 1
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> La primera línea dice `ass Person`; debe ser `class Person`. El resto del ejemplo está correcto (el `end` de `initialize` solo está mal indentado).

> [!tip] Complemento — ejemplo de las slides "Ruby"
> ```ruby
> class Song
>   @@total_plays = 0
>
>   def initialize(name, artist, duration)
>     @name = name
>     @artist = artist
>     @duration = duration
>     @plays = 0
>   end
>
>   def play
>     @plays += 1          # propio de cada canción
>     @@total_plays += 1   # compartido por todas
>   end
>
>   def printReport
>     puts "this song play #{@plays} times"
>   end
>
>   def self.printPlaysReport
>     puts "all songs play #{@@total_plays} times"
>   end
> end
>
> song1 = Song.new("A", "X", 100); song1.play
> song2 = Song.new("B", "Y", 200); song2.play
> song1.printReport        # this song play 1 times
> song2.printReport        # this song play 1 times
> Song.printPlaysReport    # all songs play 2 times
> ```
> En la slide se llama `Song.new` sin argumentos, lo que daría `ArgumentError` con ese `initialize`; aquí se agregaron argumentos.

## Preguntas de repaso

1. ¿Qué diferencia hay entre `@nombre` y `@@nombre`?
> [!question]- Respuesta
> `@nombre` es un atributo de instancia: cada objeto tiene el suyo. `@@nombre` es una variable de clase compartida por todas las instancias.

2. En el ejemplo de `Song`, después de que `song1` y `song2` llaman a `play` una vez cada uno, ¿cuánto valen `@plays` de cada una y `@@total_plays`?
> [!question]- Respuesta
> `@plays` vale 1 en cada canción y `@@total_plays` vale 2.

3. ¿Cómo se lee una variable de clase desde fuera?
> [!question]- Respuesta
> Con un método de clase que la devuelva, por ejemplo `def self.contador_personas; @@contador_personas; end`.
