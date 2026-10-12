---
ramo: Ingeniería de Software
tema: Patrones creacionales
tags: [ingsoft/patrones, patron/creacional, origen/apuntes]
prerrequisitos: ["[[01 - Patrón Abstract Factory|Patrón Abstract Factory]]"]
---
# Abstract Factory: implementación en Ruby

Implementación de referencia de [[01 - Patrón Abstract Factory|Abstract Factory]] en 5 pasos: fábrica abstracta, fábrica concreta, productos abstractos, productos concretos y cliente.

```ruby
# 1. Crear Fabrica Abstracta

class FabricaAbstracta
  def crear_producto_a
    raise NotImplementedError
  end

  def crear_producto_b
    raise NotImplementedError
  end
end

# 2. Crear Fabrica Concreta

class FabricaConcreta < FabricaAbstracta
  def crear_producto_a
    ProductoConcretoA.new
  end

  def crear_producto_b
    ProductoConcretoB.new
  end
end

# 3. Definir Productos Abstractos

class ProductoAbstractoA
  def funcion_util_a
    raise NotImplementedError
  end
end

class ProductoAbstractoB
  def funcion_util_b
    raise NotImplementedError
  end

  def otra_funcion_util_b(_colaborador)
    raise NotImplementedError
  end
end

# 4. Definir Productos Concretos

class ProductoConcretoA < ProductoAbstractoA
  def funcion_util_a
    'Resultado del producto A.'
  end
end

class ProductoConcretoB < ProductoAbstractoB
  def funcion_util_b
    'Resultado del producto B.'
  end

  def otra_funcion_util_b(colaborador)
    resultado = colaborador.funcion_util_a
    "Resultado del B colaborando con el (#{resultado})"
  end
end

# 5. Codigo del Cliente -> Usa fabricas abstractas para crear productos
def codigo_cliente(fabrica)
  producto_a = fabrica.crear_producto_a
  producto_b = fabrica.crear_producto_b

  puts producto_b.funcion_util_b
  puts producto_b.otra_funcion_util_b(producto_a)
end

# Ejecutar codigo del cliente con una fabrica concreta
puts 'Cliente: Probando el código del cliente con una fábrica concreta:'
codigo_cliente(FabricaConcreta.new)
```

> [!tip] Complemento — salida y lectura
> ```
> Cliente: Probando el código del cliente con una fábrica concreta:
> Resultado del producto B.
> Resultado del B colaborando con el (Resultado del producto A.)
> ```
> - `codigo_cliente` **no nombra ninguna clase concreta**: solo usa `crear_producto_a` y `crear_producto_b`. Si mañana existiera `FabricaConcreta2` (otra familia), el cliente funcionaría igual.
> - `otra_funcion_util_b(producto_a)` muestra por qué importa la "familia": los productos de una misma fábrica **colaboran entre sí**.
> - En el ejemplo de los muebles: `FabricaAbstracta` = `FurnitureFactory`, `crear_producto_a` = `createChair` y `FabricaConcreta` = `VictorianFurnitureFactory`.

## Preguntas de repaso

1. ¿Qué imprime el programa?
> [!question]- Respuesta
> "Resultado del producto B." y "Resultado del B colaborando con el (Resultado del producto A.)".

2. ¿Qué habría que crear para agregar una segunda familia de productos?
> [!question]- Respuesta
> `FabricaConcreta2 < FabricaAbstracta` y sus productos `ProductoConcretoA2 < ProductoAbstractoA` y `ProductoConcretoB2 < ProductoAbstractoB`. El cliente no cambia.

3. ¿Qué rol cumple `FabricaAbstracta`?
> [!question]- Respuesta
> Es la interfaz de creación de la familia: declara un método por producto, que las fábricas concretas implementan devolviendo su variante.
