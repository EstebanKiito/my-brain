---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[01 - Buen diseño de software|Buen diseño de software]]"]
---
# Acoplamiento

El acoplamiento mide **cuánto dependen unas clases de otras**. Un buen diseño busca **bajo acoplamiento**: clases independientes que se comunican por pocos métodos bien definidos.

## Acoplamiento
- Se refiere a la **INTERACCIÓN ENTRE CLASES** → qué tanto están **CONECTADAS**.
- **+ Diseño → − Acoplamiento**
- Buscamos tener **clases muy independientes** que se comuniquen a través de **pocos métodos bien definidos**.

> [!tip] Complemento (slides "Diseño Orientado al Objeto" y libro del curso, cap. 8.6)
> - Es la **interconectividad entre clases**. Para un buen diseño hay que **reducir el acoplamiento** del sistema.
> - Bajo acoplamiento hace el sistema más fácil de **entender, modificar, extender y testear**: un cambio en una clase no obliga a cambiar las demás.
> - **Es imposible no tener acoplamiento**, pero hay tipos mejores y peores (de peor a mejor):
>   1. **por contenido:** acceder a los datos internos de otra clase;
>   2. **por variables globales;**
>   3. **de control:** una unidad influye en el flujo de control de otra (por ejemplo, pasarle un flag);
>   4. **de datos:** pasar solo los parámetros necesarios (**el deseable**).
> - **Analogía del tren** (libro): los carros se conectan en un solo punto (bajo acoplamiento) y cada uno lleva carga de un mismo tipo (cohesión). Así es fácil agregar o cambiar un carro.
> - Ojo: hay que mirar acoplamiento y [[03 - Cohesión|cohesión]] **a la vez**. Poner todo en una sola clase da acoplamiento nulo pero pésima cohesión; clases diminutas dan alta cohesión pero muchísimo acoplamiento.
>
> **Ejemplo:** en el [[07 - Ejemplo de diseño - Carrito de compras|carrito de compras]], `ShoppingCar` dependía de dos atributos y un método de `Item`. Al rediseñarlo, depende solo de `item.print`.

## Preguntas de repaso

1. ¿Qué es el acoplamiento y qué nivel se busca?
> [!question]- Respuesta
> El grado de interconexión o dependencia entre clases. Se busca bajo acoplamiento: clases independientes que se comunican por pocos métodos bien definidos.

2. Ordena de peor a mejor: acoplamiento de datos, por contenido, de control y por variables globales.
> [!question]- Respuesta
> Por contenido → por variables globales → de control → de datos.

3. ¿Por qué el bajo acoplamiento facilita el cambio?
> [!question]- Respuesta
> Porque si una clase depende poco de otra, modificar una no obliga a modificar la otra, y cada una se puede probar y entender por separado.
