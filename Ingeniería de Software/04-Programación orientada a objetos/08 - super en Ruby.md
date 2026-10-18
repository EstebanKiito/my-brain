---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[07 - Herencia en Ruby|Herencia en Ruby]]", "[[04 - Constructor initialize en Ruby|Constructor initialize en Ruby]]"]
---
# super en Ruby

`super` llama al **método con el mismo nombre en la clase padre**. Se usa sobre todo para reutilizar el constructor del padre y para extender un método sobrescrito.

## Super
Dentro de un método, `super` ejecuta el método del **mismo nombre en la clase padre**. En un constructor, ejecuta el `initialize` del padre:

```ruby
class Padre
  def initialize
    puts "Soy el padre"
  end
end

class Hijo < Padre
  def initialize
    super          # ejecuta el initialize de Padre
  end
end

Hijo.new   # imprime "Soy el padre"
```

Sin el `< Padre`, `Hijo` no heredaría de `Padre` y `super` buscaría el `initialize` de `Object`.

## Herencia y constructor
Si el constructor del padre recibe argumentos, la hija se los pasa con `super(...)` y luego inicializa lo propio:

```ruby
class Figure
  attr_accessor :stroke, :fill

  def initialize(stroke, fill)
    @stroke = stroke
    @fill = fill
  end
end

class Circle < Figure
  attr_accessor :radius

  def initialize(stroke, fill, radius)
    super(stroke, fill)  # constructor del padre con sus atributos
    @radius = radius
  end
end
```

## Super y override
Al sobrescribir un método, `super` permite **reutilizar** la versión del padre y extenderla:

```ruby
class Empleado
  def calcular_salario
    # ...
  end
end

class Manager < Empleado
  def calcular_salario
    base_salario = super   # resultado del método de Empleado
    base_salario + @bonus
  end
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
