---
ramo: Ingeniería de Software
tema: Patrones creacionales
tags: [ingsoft/patrones, patron/creacional, origen/apuntes]
prerrequisitos: ["[[03 - Patrón Builder|Patrón Builder]]"]
---
# Builder: implementación en Ruby

Implementación de referencia de [[03 - Patrón Builder|Builder]]: un producto con partes A, B y C; un builder concreto; un director con dos recetas; y un cliente que también arma un producto personalizado.

```ruby
# 1. Definir el Producto Complejo

class Producto
  attr_accessor :parte_a, :parte_b, :parte_c

  def mostrar_partes
    puts "Partes del Producto: #{[parte_a, parte_b, parte_c].compact.join(', ')}"
  end
end

# 2. Crear el Builder Abstracto

class BuilderAbstracto
  def construir_parte_a; raise NotImplementedError; end
  def construir_parte_b; raise NotImplementedError; end
  def construir_parte_c; raise NotImplementedError; end
  def obtener_producto; raise NotImplementedError; end
end

# 3. Crear el Builder Concreto

class BuilderConcreto < BuilderAbstracto
  def initialize
    reiniciar
  end

  def reiniciar
    @producto = Producto.new
  end

  def construir_parte_a
    @producto.parte_a = 'Parte A'
  end

  def construir_parte_b
    @producto.parte_b = 'Parte B'
  end

  def construir_parte_c
    @producto.parte_c = 'Parte C'
  end

  def obtener_producto
    producto = @producto
    reiniciar
    producto
  end
end

# 4. Crear el Director

class Director
  def initialize(builder)
    @builder = builder
  end

  def construir_producto_minimo
    @builder.construir_parte_a
  end

  def construir_producto_completo
    @builder.construir_parte_a
    @builder.construir_parte_b
    @builder.construir_parte_c
  end
end

# 5. Codigo del Cliente

def codigo_cliente(director)
  puts 'Producto mínimo estándar:'
  director.construir_producto_minimo
  producto = director.builder.obtener_producto
  producto.mostrar_partes

  puts 'Producto completo estándar:'
  director.construir_producto_completo
  producto = director.builder.obtener_producto
  producto.mostrar_partes

  puts 'Producto personalizado:'
  director.builder.construir_parte_a
  director.builder.construir_parte_c
  producto = director.builder.obtener_producto
  producto.mostrar_partes
end

builder = BuilderConcreto.new
director = Director.new(builder)
codigo_cliente(director)
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> `codigo_cliente` usa `director.builder`, pero `Director` no define ese método: lanza `NoMethodError`. Falta agregar `attr_reader :builder` en `Director`. Otra opción es que el cliente use directamente la variable `builder`.
> ```ruby
> class Director
>   attr_reader :builder
>   # ...
> end
> ```

> [!tip] Complemento — salida esperada (con el arreglo)
> ```
> Producto mínimo estándar:
> Partes del Producto: Parte A
> Producto completo estándar:
> Partes del Producto: Parte A, Parte B, Parte C
> Producto personalizado:
> Partes del Producto: Parte A, Parte C
> ```
> - `obtener_producto` **reinicia** el builder (`reiniciar`), así el siguiente producto parte de cero.
> - `.compact` quita las partes `nil` antes de unirlas con comas.

## Preguntas de repaso

1. ¿Por qué falla el código tal como está y cómo se arregla?
> [!question]- Respuesta
> `director.builder` no existe porque `Director` no expone `@builder`. Se arregla con `attr_reader :builder` en `Director`.

2. ¿Por qué `obtener_producto` llama a `reiniciar`?
> [!question]- Respuesta
> Para que el builder quede listo para construir un producto nuevo; si no, el siguiente producto acumularía las partes del anterior.

3. ¿Qué imprime el "producto personalizado"?
> [!question]- Respuesta
> "Partes del Producto: Parte A, Parte C".
