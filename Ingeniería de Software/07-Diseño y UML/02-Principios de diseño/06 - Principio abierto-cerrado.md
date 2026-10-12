---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[05 - Código duplicado (code clones)|Código duplicado (code clones)]]", "[[11 - Polimorfismo y duck typing|Polimorfismo y duck typing]]"]
---
# Principio abierto-cerrado

El código debe estar **abierto para extensiones y cerrado para modificaciones**: se agregan funcionalidades creando código nuevo (por ejemplo, una clase nueva), sin modificar el código que ya funciona.

## Mis apuntes (ejemplo de filtros de libros)
- Ya **no tendremos que modificar `BookStore` ni `Book`** en caso de añadir más filtros.
- Solo se crea otra estrategia (clase nueva que hereda de `FilterStrategy`).
- Está **"Abierto para Extensiones, Cerrado para Modificaciones"**.

> [!tip] Complemento (slides "Diseño Orientado al Objeto")
> - Para agregar un nuevo tipo de filtro, por ejemplo `FilterByYear`, **no se modifica `Book` ni `BookStore`**: solo se crea un archivo nuevo con una clase que hereda de `FilterStrategy`.
> - En POO, el mecanismo que lo permite es la **herencia** junto con el **polimorfismo**: el código existente llama a un método común (`check`) sin saber qué clase concreta está usando.
> - Es la "O" de **SOLID** (*Open/Closed Principle*, Bertrand Meyer).
> - Muchos patrones de diseño existen para cumplirlo: Strategy, Template Method, Observer, Decorator…
>
> ```ruby
> class ByYear < FilterStrategy   # extensión: archivo nuevo
>   def initialize(year)
>     @year = year
>   end
>
>   def check(book)
>     book.year == @year
>   end
> end
> store.filter(ByYear.new(2022))  # BookStore no se tocó
> ```

## Preguntas de repaso

1. Enuncia el principio abierto-cerrado.
> [!question]- Respuesta
> El software debe estar abierto para extensión (se le puede agregar comportamiento) y cerrado para modificación (sin cambiar el código existente).

2. En el ejemplo de los libros, ¿qué hay que hacer para agregar un filtro por año?
> [!question]- Respuesta
> Crear una clase `ByYear < FilterStrategy` que implemente `check(book)`. No se modifica ni `BookStore` ni `Book`.

3. ¿Por qué un `case` sobre el tipo de pago viola este principio?
> [!question]- Respuesta
> Porque cada tipo nuevo obliga a modificar ese método para agregar otro `when`; no se puede extender sin modificar.
