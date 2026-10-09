---
ramo: Ingeniería de Software
tema: Patrones creacionales
tags: [ingsoft/patrones, patron/creacional, origen/apuntes]
prerrequisitos: ["[[05 - Patrón Factory Method|Patrón Factory Method]]"]
---
# Factory Method: implementación en Ruby

Implementación de referencia de [[05 - Patrón Factory Method|Factory Method]]: un `Creador` abstracto cuya `alguna_operacion` usa el producto que devuelve `factory_method`, definido por cada creador concreto.

## Ejemplo
```ruby
# 1. Definir el Producto Abstracto

class Producto
  def operacion
    raise NotImplementedError, "#{self.class} no ha implementado el método '#{__method__}'"
  end
end

# 2. Definir Productos Concretos

class ProductoConcreto1 < Producto
  def operacion
    'Resultado del Producto Concreto 1'
  end
end

class ProductoConcreto2 < Producto
  def operacion
    'Resultado del Producto Concreto 2'
  end
end

# 3. Definir el Creador Abstracto

class Creador
  def factory_method
    raise NotImplementedError, "#{self.class} no ha implementado el método '#{__method__}'"
  end

  def alguna_operacion
    producto = factory_method
    "Creador: El mismo código del creador acaba de trabajar con #{producto.operacion}"
  end
end

# 4. Definir Creadores Concretos

class CreadorConcreto1 < Creador
  def factory_method
    ProductoConcreto1.new
  end
end

class CreadorConcreto2 < Creador
  def factory_method
    ProductoConcreto2.new
  end
end

# 5. Codigo del Cliente

def codigo_cliente(creador)
  puts "Cliente: No conozco la clase del creador, pero aún funciona.\n#{creador.alguna_operacion}"
end

puts 'App: Lanzado con el CreadorConcreto1.'
codigo_cliente(CreadorConcreto1.new)

puts "\nApp: Lanzado con el CreadorConcreto2."
codigo_cliente(CreadorConcreto2.new)
```

> [!tip] Complemento — salida
> ```
> App: Lanzado con el CreadorConcreto1.
> Cliente: No conozco la clase del creador, pero aún funciona.
> Creador: El mismo código del creador acaba de trabajar con Resultado del Producto Concreto 1
>
> App: Lanzado con el CreadorConcreto2.
> Cliente: No conozco la clase del creador, pero aún funciona.
> Creador: El mismo código del creador acaba de trabajar con Resultado del Producto Concreto 2
> ```
> `alguna_operacion` está escrita **una sola vez** en `Creador`. Lo único que cambia entre subclases es qué producto crea `factory_method`.

## Preguntas de repaso

1. ¿Dónde está definida `alguna_operacion` y por qué funciona con ambos creadores?
> [!question]- Respuesta
> En `Creador`. Llama a `factory_method`, que cada subclase sobrescribe, y trabaja con el producto a través de su interfaz común (`operacion`).

2. ¿Qué pasa si se llama `Creador.new.alguna_operacion`?
> [!question]- Respuesta
> `factory_method` lanza `NotImplementedError`, porque `Creador` es abstracto.

3. ¿Cuál es el "método fábrica" en este código?
> [!question]- Respuesta
> `factory_method`, que en los creadores concretos devuelve `ProductoConcreto1.new` o `ProductoConcreto2.new`.
