---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[09 - Sobrescritura de métodos (override)|Sobrescritura de métodos (override)]]"]
---
# Polimorfismo y duck typing

El polimorfismo es la capacidad de **tratar objetos distintos de la misma forma**, porque todos responden al mismo mensaje. En Ruby se basa en el **duck typing**: no importa la clase, sino que el objeto tenga el método.

## Polimorfismo
Es la capacidad de un objeto de **tomar otras formas**: distintos objetos responden al mismo mensaje, cada uno a su manera.

En Ruby se apoya en el **duck typing**: *"si camina como pato y hace cuac, entonces es un pato"*. No importa la clase del objeto, sino que tenga el método que se necesita.

```ruby
def pintar(figura, x, y)
  set_coordenadas(x, y)
  figura.draw
end

class Circle
  attr_accessor :radius
  def draw
    # ...
  end
end

class Triangulo
  attr_accessor :base, :altura
  def draw
    # ...
  end
end
```

A `pintar` se le puede entregar **cualquier objeto que tenga el método `draw`**: un `Circle`, un `Triangulo` o una clase futura. `pintar` no necesita saber cuál es.

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
