---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[01 - Patrón Strategy|Patrón Strategy]]"]
---
# Strategy: implementación en Ruby

Implementación de referencia del patrón [[01 - Patrón Strategy|Strategy]]: un `Context` que ordena datos con una estrategia intercambiable (orden normal o inverso).

## Implementación en código
```ruby
class Context
  # The Context maintains a reference to one of the Strategy objects
  attr_writer :strategy

  def initialize(strategy)
    @strategy = strategy
  end

	# provides a setter to change it at runtime.
  def strategy=(strategy)
    @strategy = strategy
  end

  def do_some_business_logic
    # ...

    puts 'Context: Sorting data using the strategy (not sure how it\'ll do it)'
    result = @strategy.do_algorithm(%w[a b c d e])
    print result.join(',')

    # ...
  end
end

class Strategy
  # @abstract
  # @param [Array] data
  def do_algorithm(_data)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end

# Concrete Strategies implement the algorithm while following the base Strategy
# interface. The interface makes them interchangeable in the Context.

class ConcreteStrategyA < Strategy
  # @param [Array] data
  #
  # @return [Array]
  def do_algorithm(data)
    data.sort
  end
end

class ConcreteStrategyB < Strategy
  # @param [Array] data
  #
  # @return [Array]
  def do_algorithm(data)
    data.sort.reverse
  end
end

# The client code picks a concrete strategy and passes it to the context

context = Context.new(ConcreteStrategyA.new)
puts 'Client: Strategy is set to normal sorting.'
context.do_some_business_logic
puts 'Client: Strategy is set to reverse sorting.'
context.strategy = ConcreteStrategyB.new
context.do_some_business_logic
```

```
# OUTPUT
Client: Strategy is set to normal sorting.
Context: Sorting data using the strategy (not sure how it'll do it)
a,b,c,d,e
Client: Strategy is set to reverse sorting.
Context: Sorting data using the strategy (not sure how it'll do it)
e,d,c,b,a
```

> [!tip] Complemento — lectura del código
> | Rol del patrón | En el código |
> |---|---|
> | Contexto | `Context`: guarda `@strategy` y en `do_some_business_logic` llama a `@strategy.do_algorithm(...)` |
> | Estrategia (abstracta) | `Strategy#do_algorithm` lanza `NotImplementedError` |
> | Estrategias concretas | `ConcreteStrategyA` (ordena) y `ConcreteStrategyB` (ordena y luego invierte) |
> | Cliente | crea `Context.new(ConcreteStrategyA.new)` y después cambia con `context.strategy = ...` |
>
> - `attr_writer :strategy` y el método `strategy=` hacen lo mismo; basta con uno de los dos.
> - `%w[a b c d e]` es un arreglo de strings: `["a", "b", "c", "d", "e"]`.
> - `print` (sin salto de línea) junta la salida con la siguiente línea; en la salida mostrada aparecen en líneas separadas por formato.

## Preguntas de repaso

1. ¿Qué imprime el contexto con `ConcreteStrategyB`?
> [!question]- Respuesta
> `e,d,c,b,a`: ordena y luego invierte el arreglo.

2. ¿Qué línea cambia la estrategia en tiempo de ejecución?
> [!question]- Respuesta
> `context.strategy = ConcreteStrategyB.new`, que usa el setter `strategy=`.

3. ¿Qué pasa si se crea una estrategia nueva que no implementa `do_algorithm`?
> [!question]- Respuesta
> Hereda el método de `Strategy`, que lanza `NotImplementedError` cuando el contexto lo llama.
