---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[02 - Acoplamiento|Acoplamiento]]", "[[05 - Atributos y accesores en Ruby|Atributos y accesores en Ruby]]"]
---
# Encapsulamiento

El encapsulamiento consiste en **ocultar los datos internos de un objeto** y exponer solo los métodos necesarios. Así otras clases no dependen de cómo está hecho por dentro.

## Mis apuntes (del ejemplo del carrito)
- Romper el encapsulamiento: los **datos de los objetos deben estar lo más ocultos posible** para evitar dependencias innecesarias.
- En el código mejorado, **`Item` tiene sus datos privados** y el método `totalCost` también es **privado**.

> [!tip] Complemento (slides "Diseño Orientado al Objeto")
> - *"Encapsulamiento se refiere a que los datos de los objetos deben estar lo más ocultos posibles para evitar dependencias innecesarias."*
> - **Tell, don't ask:** en vez de pedirle sus datos a un objeto para hacer algo con ellos afuera, **pedirle al objeto que lo haga**. Es lo que pasa en el carrito: antes `ShoppingCar` leía `item.name`, `item.quantity` y `item.totalCost`; después solo le dice `item.print`.
> - Reduce el [[02 - Acoplamiento|acoplamiento]] y mejora la [[03 - Cohesión|cohesión]]: la lógica de un `Item` queda dentro de `Item`.
> - En Ruby: atributos `@x` (siempre ocultos), getters solo si hacen falta (`attr_reader`) y métodos auxiliares bajo `private`.

## Preguntas de repaso

1. ¿Qué es el encapsulamiento?
> [!question]- Respuesta
> Ocultar los datos internos de un objeto y exponer solo el comportamiento necesario mediante métodos, para evitar dependencias innecesarias.

2. ¿Qué significa "tell, don't ask"?
> [!question]- Respuesta
> Pedirle al objeto que haga la tarea con sus propios datos (`item.print`) en vez de sacarle los datos para procesarlos afuera.

3. ¿Cómo mejoró el encapsulamiento el ejemplo del carrito?
> [!question]- Respuesta
> `Item` dejó sus datos privados (sin getters de `name` y `quantity`) e hizo privado `totalCost`; `ShoppingCar` solo llama a `item.print`.
