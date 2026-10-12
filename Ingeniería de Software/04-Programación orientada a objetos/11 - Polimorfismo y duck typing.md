---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[09 - Sobrescritura de métodos (override)|Sobrescritura de métodos (override)]]"]
---
# Polimorfismo y duck typing

El polimorfismo es la capacidad de **tratar objetos distintos de la misma forma**, porque todos responden al mismo mensaje. En Ruby se basa en el **duck typing**: no importa la clase, sino que el objeto tenga el método.

## Polimorfismo 🦆
Capacidad de un objeto de **tomar otras formas**.

→ **Duck typing** ("Si camina como pato y hace quack, entonces debe ser un pato") 🦆

```ruby
def pintar(figura, x, y)
	set_cordenadas(x, y)
	figura.draw

class Circle
	attr_accessor :radius
	def draw
		...
	end

class Triangulo
	attr_accessor :base :altura
	def draw
		...
	end

# Basicamente puedo llamar a pintar
# Le entrego cualquier clase (que tenga el metodo draw)
# pintar va a hacer draw del objeto entregado
```

> [!warning] Posible error de sintaxis (registrado en `_meta/DUDAS.md`)
> Faltan los `end` del método y de las clases, y `attr_accessor :base :altura` necesita coma: `attr_accessor :base, :altura`. La idea es correcta.

> [!example] Ejemplo extra — versión ejecutable
> ```ruby
> class Circle
>   def draw = "dibujo un círculo"
> end
>
> class Triangulo
>   def draw = "dibujo un triángulo"
> end
>
> class Pato            # no es una figura, pero responde a draw
>   def draw = "dibujo un pato 🦆"
> end
>
> def pintar(figura)
>   puts figura.draw    # no pregunta la clase: solo envía el mensaje
> end
>
> [Circle.new, Triangulo.new, Pato.new].each { |f| pintar(f) }
> ```
> - **Polimorfismo por herencia:** las subclases sobrescriben un método del padre (por ejemplo, `Figure#draw`).
> - **Duck typing:** basta con que el objeto responda al método, sin relación de herencia.
> - Así se puede agregar una figura nueva **sin modificar `pintar`**: es el principio abierto/cerrado que se ve en Diseño.

## Preguntas de repaso

1. ¿Qué es el duck typing?
> [!question]- Respuesta
> Tratar a un objeto según los métodos a los que responde y no según su clase: "si camina como pato y hace quack, es un pato".

2. ¿Qué necesita un objeto para poder pasarse a `pintar`?
> [!question]- Respuesta
> Solo responder al método `draw`.

3. ¿Qué ventaja de diseño da el polimorfismo en `pintar`?
> [!question]- Respuesta
> Se pueden agregar nuevos tipos de figura sin modificar `pintar` (abierto a extensión, cerrado a modificación) y se evitan cadenas de `if` por tipo.
