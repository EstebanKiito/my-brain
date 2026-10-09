---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[04 - Constructor initialize en Ruby|Constructor initialize en Ruby]]"]
---
# Atributos y accesores en Ruby

Los atributos (variables de instancia) empiezan con `@` y **no se pueden leer ni modificar desde fuera del objeto**. Para eso se definen **accesores** (getters y setters), a mano o con `attr_accessor` y `attr_reader`.

## Atributos
- Los atributos en Ruby empiezan con **"@"**.

```ruby
class Persona
	def initialize(name)
		@name = name
	end

	def saludo(otra_persona)
		puts "Hola #{otra_persona}, me llamo #{@name}"
  end
end
pedro = Persona.new("Pedro")
pedro.saludo("Juan") # "Hola Juan, me llamo pedro"
```

## Visibilidad de atributos
- Por default los métodos son **PRIVADOS**, solo pueden ser accedidos desde la misma clase.
- Para acceder a ellos se necesitan hacer **"ACCESORES"**.

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> Lo que es privado por defecto son los **atributos** (variables de instancia), no los métodos. Los métodos son **públicos** por defecto (ver [[03 - Visibilidad de métodos en Ruby|Visibilidad de métodos]]). La slide dice: *"Por defecto los atributos en ruby son privados…"*.

```ruby
class Persona
	def initialize(name)
		@name = name
	end

	# Este metodo permite leer el atributo
	def name
		@name
	end

	# Este metodo permite modificar el atributo
	def name=(name)
		@name = name
	end
end

pedro = Persona.new("Pedro")
pedro.name= ("Esteban")
puts pedro.name
```

```ruby
class Person
	attr_accesor :name, :gender # Crea los metodos name= y gender=
	attr_reader :age    # No crea el metodo age=
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> - Se escribe `attr_accessor` (con dos "s"); `attr_accesor` da `NoMethodError`.
> - `attr_accessor :name, :gender` crea **cuatro** métodos: los getters `name` y `gender` y los setters `name=` y `gender=`.
> - `attr_reader :age` crea solo el getter `age`.
> - Falta el `end` de la clase.
>
> ```ruby
> class Person
>   attr_accessor :name, :gender   # name, name=, gender, gender=
>   attr_reader :age               # solo age (no crea age=)
> end
> ```

> [!tip] Complemento — los tres macros
> | Macro | Crea |
> |---|---|
> | `attr_reader :x` | getter `x` |
> | `attr_writer :x` | setter `x=` |
> | `attr_accessor :x` | ambos |
>
> `pedro.name = "Esteban"` (con espacios) es lo mismo que `pedro.name=("Esteban")`: Ruby lo traduce a una llamada al método `name=`. Detalle menor: el comentario del primer ejemplo dice "me llamo pedro", pero imprimiría "Pedro", con mayúscula.

## Preguntas de repaso

1. ¿Por qué `pedro.@name` o `pedro.name` (sin accesor) no funcionan desde fuera?
> [!question]- Respuesta
> Porque las variables de instancia no son accesibles desde fuera del objeto. Hay que definir un método getter (`def name; @name; end`) o usar `attr_reader`/`attr_accessor`.

2. ¿Qué métodos crea `attr_accessor :name`?
> [!question]- Respuesta
> `name` (getter) y `name=` (setter).

3. ¿Qué diferencia hay entre `attr_reader` y `attr_accessor`?
> [!question]- Respuesta
> `attr_reader` solo crea el getter (lectura). `attr_accessor` crea el getter y el setter (lectura y escritura).
