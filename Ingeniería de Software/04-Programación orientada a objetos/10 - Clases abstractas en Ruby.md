---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[09 - Sobrescritura de métodos (override)|Sobrescritura de métodos (override)]]"]
---
# Clases abstractas en Ruby

Una clase abstracta es una **clase incompleta**: deja uno o más métodos sin implementar para que las hijas los definan. En Ruby se simula con `raise NotImplementedError`.

## Clases abstractas
- Es una **clase incompleta**, que se busca **implementar en la hija**.

```ruby
class Figure
	def print
		raise NotImplementedError
	end

class Square < Figure
end

f = Figure.new
f.print # -> Error (No se usa la clase abstracta!)
```

> [!tip] Complemento (slides "Object Oriented Programming")
> - Una clase abstracta es una clase incompleta: le falta la implementación de uno o más métodos. **Las clases hijas tienen que implementarlos; si no, Ruby lanza error** al llamarlos.
> - Ruby **no tiene** la palabra clave `abstract`: la convención es lanzar `NotImplementedError`. Por eso `Figure.new` sí funciona; el error aparece recién al llamar `print`.
> - En el ejemplo, `Square` tampoco implementa `print`, así que `Square.new.print` también lanza el error. Para que funcione:
> ```ruby
> class Figure
>   def print
>     raise NotImplementedError, "#{self.class} debe implementar print"
>   end
> end
>
> class Square < Figure
>   def print
>     puts "Soy un cuadrado"
>   end
> end
>
> Square.new.print   # "Soy un cuadrado"
> Figure.new.print   # NotImplementedError
> ```
> - Las clases abstractas son la base de patrones como Strategy, Template Method y Observer, donde la clase padre define la **interfaz** común.

## Preguntas de repaso

1. ¿Qué es una clase abstracta?
> [!question]- Respuesta
> Una clase incompleta que define métodos sin implementar (en Ruby, que lanzan `NotImplementedError`) para que sus subclases los implementen.

2. En Ruby, ¿se puede hacer `Figure.new` si `Figure` es "abstracta"?
> [!question]- Respuesta
> Sí, Ruby no lo impide. El error ocurre recién al llamar el método no implementado.

3. ¿Qué pasa si una subclase no implementa el método abstracto?
> [!question]- Respuesta
> Hereda el método del padre, que lanza `NotImplementedError` al ser llamado.
