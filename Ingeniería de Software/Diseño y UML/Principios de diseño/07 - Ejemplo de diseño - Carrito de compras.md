---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, ingsoft/ejemplo, origen/apuntes]
prerrequisitos: ["[[02 - Acoplamiento|Acoplamiento]]", "[[04 - Encapsulamiento|Encapsulamiento]]"]
---
# Ejemplo de diseño: carrito de compras

Ejemplo de clase sobre **métodos y datos entrelazados**: `ShoppingCar` usaba los datos internos de `Item`. Al mover esa lógica a `Item`, baja el acoplamiento y mejora el encapsulamiento.

## Ejemplo 1 (métodos y datos entrelazados)
![Ejemplo carrito de compras - código original](../adjuntos/Ejemplo%20carrito%20de%20compras%20-%20código%20original.png)

> [!note]- Transcripción de la imagen
> ```ruby
> # ShoppingCar.rb
> require_relative 'item'
> class ShoppingCar
>   def initialize
>     @items = []
>   end
>   def add(item)
>     @items.push item
>   end
>   def print
>     @items.each do |item|
>       puts "name: #{item.name}"
>       puts "quantity: #{item.quantity}"
>       puts "cost: #{item.totalCost}"
>     end
>   end
> end
>
> # Item.rb
> class Item
>   def initialize(item_name,item_quantity,item_cost)
>     @name = item_name
>     @quantity = item_quantity
>     @cost = item_cost
>   end
>   def name
>     @name
>   end
>   def quantity
>     @quantity
>   end
>   def totalCost
>     return @cost * @quantity
>   end
> end
>
> # main.rb
> require_relative "shopping_car"
> require_relative "item"
> car = ShoppingCar.new
> car.add(Item.new("Pancito",5,200))
> car.print
> ```

**Problemas:**
- `ShoppingCar` depende de **2 atributos y un método** de otra clase (`Item`).
- Aumenta el **acoplamiento** entre clases.
- Rompe el **encapsulamiento** → los datos de los objetos deben estar lo más ocultos posible para evitar dependencias innecesarias.

## Código mejorado
![Ejemplo carrito de compras - código mejorado](../adjuntos/Ejemplo%20carrito%20de%20compras%20-%20código%20mejorado.png)

> [!note]- Transcripción de la imagen
> ```ruby
> # ShoppingCar.rb
> require_relative 'item'
> class ShoppingCar
>   def initialize
>     @items = []
>   end
>   def add(item)
>     @items.push item
>   end
>   def print
>     @items.each do |item|
>       item.print
>     end
>   end
> end
>
> # Item.rb
> class Item
>   def initialize(item_name,item_quantity,item_cost)
>     @name = item_name
>     @quantity = item_quantity
>     @cost = item_cost
>   end
>   def print
>     puts "name: #{@name}"
>     puts "quantity: #{@quantity}"
>     puts "cost: #{self.totalCost}"
>   end
>   private:
>     def totalCost
>       return @cost * @quantity
>     end
> end
> ```
> *(main.rb queda igual.)*

**Ventajas:**
- `ShoppingCar` solo depende del método `print` → **disminuyen las dependencias** (acoplamiento).
- `Item` tiene sus **datos privados** + el método `totalCost` es **privado**.

`require_relative` se usa para cargar los archivos: ver [[08 - require_relative en Ruby|require_relative en Ruby]].

> [!warning] Detalle de sintaxis en la imagen
> `private:` (con dos puntos) no es Ruby válido: se escribe `private`. Desde Ruby 2.7, `self.totalCost` sí puede llamar a un método privado (con `self` explícito).

> [!tip] Complemento — por qué mejora (slides "Diseño Orientado al Objeto")
> Es el principio **"tell, don't ask"**: el carrito le pide al ítem que se imprima en vez de pedirle sus datos. Mejora la [[03 - Cohesión|cohesión]] (la lógica de un ítem está en `Item`) y el [[04 - Encapsulamiento|encapsulamiento]].

## Preguntas de repaso

1. ¿Qué problema de diseño tenía el `ShoppingCar` original?
> [!question]- Respuesta
> Dependía de dos atributos (`name`, `quantity`) y un método (`totalCost`) de `Item`: alto acoplamiento y ruptura del encapsulamiento.

2. ¿Qué se cambió en el código mejorado?
> [!question]- Respuesta
> La impresión se movió a `Item#print`; `ShoppingCar#print` solo delega con `item.print`, e `Item` dejó privados sus datos y `totalCost`.

3. ¿Qué gana el diseño mejorado?
> [!question]- Respuesta
> Menor acoplamiento (el carrito depende solo de `print`), mejor encapsulamiento y mejor cohesión.
