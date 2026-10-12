---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[07 - Herencia en Ruby|Herencia en Ruby]]"]
---
# Sobrescritura de métodos (override)

Sobrescribir es **redefinir en la clase hija un método que ya existe en el padre**, con el mismo nombre y argumentos, para cambiar su comportamiento.

## Override
- La sobreescritura es escribir un método existente en la clase padre en la clase hija.
- Tiene **mismo nombre y argumentos** que el método del padre.
- Ej: **"to_s"**: método de `Object` (propio de Ruby).

```ruby
class Circle < Figure

	def initialize(radius)
		@radius = radius
	end

	def to_s
		"Es un circulo de radio #{@radius}"
	end

c = Circle.new(5)
puts c.to_s
```
*(Falta el `end` de la clase antes de `c = Circle.new(5)`.)*

> [!tip] Complemento (slides "Object Oriented Programming" y "Ruby")
> - En Ruby **todas las clases heredan de `Object`**, y `to_s` está definido en `Object`. Sin sobrescribirlo, `Song.new(...).to_s` devuelve algo como `#<Song:0xe6c>`.
> - Al sobrescribirlo se obtiene una representación útil:
> ```ruby
> class Song
>   def initialize(name, artist, duration)
>     @name, @artist, @duration = name, artist, duration
>   end
>
>   def to_s   # sobre-escritura
>     "Song: #{@name}--#{@artist} (#{@duration})"
>   end
> end
> Song.new("Bicylops", "Fleck", 260).to_s   # "Song: Bicylops--Fleck (260)"
> ```
> - `puts objeto` llama a `to_s` automáticamente.
> - Para **extender** en vez de reemplazar, se usa [[08 - super en Ruby|super]] dentro del método sobrescrito.
> - La sobrescritura es la base del [[11 - Polimorfismo y duck typing|polimorfismo]] y de patrones como Template Method.

> [!warning] Error común: override ≠ overload
> **Sobrescribir** (override) = la hija redefine un método del padre. **Sobrecargar** (overload) = varios métodos con el mismo nombre y distintos parámetros en la misma clase. Ruby **no** tiene sobrecarga: si defines dos veces el mismo método, el segundo reemplaza al primero.

## Preguntas de repaso

1. ¿Qué es sobrescribir un método?
> [!question]- Respuesta
> Definir en la clase hija un método con el mismo nombre (y argumentos) que uno del padre, para reemplazar su comportamiento.

2. ¿Por qué cualquier objeto de Ruby tiene `to_s` aunque no lo definas?
> [!question]- Respuesta
> Porque todas las clases heredan de `Object`, que define `to_s`.

3. ¿Cómo sobrescribes un método pero reutilizando lo que hacía el padre?
> [!question]- Respuesta
> Llamando a `super` dentro del método sobrescrito y agregando el comportamiento nuevo.
