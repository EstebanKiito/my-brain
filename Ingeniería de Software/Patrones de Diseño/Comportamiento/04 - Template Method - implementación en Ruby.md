---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[03 - Patrón Template Method|Patrón Template Method]]"]
---
# Template Method: implementación en Ruby

Implementación de referencia de [[03 - Patrón Template Method|Template Method]]: una clase abstracta con el método plantilla, operaciones base, operaciones requeridas (abstractas) y hooks opcionales.

## Ejemplo de código
```ruby
# The Abstract Class defines a template method that contains a skeleton of some
# algorithm, composed of calls to (usually) abstract primitive operations.

class AbstractClass
  # The template method defines the skeleton of an algorithm.
  def template_method
    base_operation1
    required_operations1
    base_operation2
    hook1
    required_operations2
    base_operation3
    hook2
  end

  def base_operation1
    puts 'AbstractClass says: I am doing the bulk of the work'
  end

  def base_operation2
    puts 'AbstractClass says: But I let subclasses override some operations'
  end

  def base_operation3
    puts 'AbstractClass says: But I am doing the bulk of the work anyway'
  end

  # These operations have to be implemented in subclasses. -> (Abstractas)
  def required_operations1
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def required_operations2
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  # Subclasses may override them, but it's not mandatory
  def hook1; end

  def hook2; end
end

# -----------------------------------------------------------
# Concrete classes have to implement all abstract operations of the base class.
# They can also override some operations with a default implementation.
class ConcreteClass1 < AbstractClass
  def required_operations1
    puts 'ConcreteClass1 says: Implemented Operation1'
  end

  def required_operations2
    puts 'ConcreteClass1 says: Implemented Operation2'
  end
end

class ConcreteClass2 < AbstractClass
  def required_operations1
    puts 'ConcreteClass2 says: Implemented Operation1'
  end

  def required_operations2
    puts 'ConcreteClass2 says: Implemented Operation2'
  end

  def hook1
    puts 'ConcreteClass2 says: Overridden Hook1'
  end
end

#-------------------------------------------------------------
# The client code calls the template method to execute the algorithm.
def client_code(abstract_class)
  # ...
  abstract_class.template_method
  # ...
end

puts 'Same client code can work with different subclasses:'
client_code(ConcreteClass1.new)
puts "\n"

puts 'Same client code can work with different subclasses:'
client_code(ConcreteClass2.new)
```

> [!tip] Complemento — salida y lectura del código
> `client_code(ConcreteClass2.new)` imprime, en orden:
> ```
> AbstractClass says: I am doing the bulk of the work
> ConcreteClass2 says: Implemented Operation1
> AbstractClass says: But I let subclasses override some operations
> ConcreteClass2 says: Overridden Hook1
> ConcreteClass2 says: Implemented Operation2
> AbstractClass says: But I am doing the bulk of the work anyway
> ```
> Con `ConcreteClass1` la salida es igual, pero sin la línea del hook, porque no lo sobrescribe y el `hook1` por defecto no hace nada.
>
> | Tipo de método | Ejemplo | ¿La hija debe implementarlo? |
> |---|---|---|
> | Método plantilla | `template_method` | No (no se toca) |
> | Operación base | `base_operation1..3` | No (ya tiene implementación) |
> | Operación requerida | `required_operations1..2` | **Sí** (lanza `NotImplementedError`) |
> | Hook | `hook1`, `hook2` | Opcional (vacío por defecto) |

## Preguntas de repaso

1. ¿Qué imprime `client_code(ConcreteClass1.new)`?
> [!question]- Respuesta
> Las tres operaciones base intercaladas con "ConcreteClass1 says: Implemented Operation1/2". Los hooks no imprimen nada porque ConcreteClass1 no los sobrescribe.

2. ¿Qué pasa si una subclase no implementa `required_operations2`?
> [!question]- Respuesta
> Al ejecutar `template_method` se lanza `NotImplementedError` cuando se llega a ese paso.

3. ¿Para qué sirven `hook1` y `hook2`?
> [!question]- Respuesta
> Son puntos de extensión opcionales: por defecto no hacen nada, y una subclase puede sobrescribirlos para agregar comportamiento en ese punto del algoritmo.
