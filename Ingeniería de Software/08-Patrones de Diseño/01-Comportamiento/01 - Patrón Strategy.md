---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[01 - Qué es un patrón de diseño|Qué es un patrón de diseño]]", "[[08 - Ejemplo de diseño - Filtros de libros|Ejemplo de diseño - Filtros de libros]]"]
---
# Patrón Strategy 🧠

Strategy es un patrón de comportamiento que **encapsula cada algoritmo en su propia clase** para poder intercambiarlos. El objeto que los usa (el contexto) no sabe cuál está usando.

## Definición
Es un patrón de comportamiento que:
- define una **familia de algoritmos**,
- coloca cada uno en una **clase separada** (una **estrategia**),
- y hace que sus objetos sean **intercambiables** dentro de un **contexto**.

## Problemas
Una app de viajes con un mapa va sumando formas de calcular rutas en cada versión:
- V1: rutas en auto por carretera;
- V2: rutas a pie;
- V3: rutas en tren;
- V4: …

Si todo vive en la clase **`Navegador`**, esta acumula mucha lógica y cada cambio se vuelve insostenible: agregar un tipo de ruta obliga a modificar la misma clase, con riesgo de romper las demás.

## Solución
1. Se extrae cada algoritmo de la clase original y se coloca en una **clase separada**: cada una es una **estrategia**.
2. La clase original pasa a ser el **contexto**, que guarda una referencia a una estrategia.
3. El cliente le entrega al contexto la estrategia que quiere usar.
4. El contexto llama a un **método común** que todas las estrategias implementan, sin saber cuál de ellas tiene.

## Ventajas
- Los algoritmos se pueden **intercambiar en tiempo de ejecución**.
- Cumple el **principio abierto/cerrado**: se agregan estrategias nuevas sin modificar el contexto.
- **Sustituye la herencia por composición**: el contexto *tiene* una estrategia en vez de *ser* una variante.

## Diagrama
![Strategy - rutas del navegador](../adjuntos/Strategy%20-%20rutas%20del%20navegador.png)

![Strategy - estructura](../adjuntos/Strategy%20-%20estructura.png)

> [!note]- Transcripción de las imágenes
> - **Rutas:** `Navigator` (`-routeStrategy`, `+buildRoute(A, B)`, que hace `route = routeStrategy.buildRoute(A, B)`) agrega (rombo vacío) la interfaz `«interface» RouteStrategy` (`+buildRoute(A, B)`), implementada por `RoadStrategy`, `PublicTransportStrategy` y `WalkingStrategy`.
> - **Estructura general:**
>   1. El **Contexto** mantiene una referencia a una estrategia concreta y se comunica con ella solo a través de la interfaz.
>   2. La interfaz **Estrategia** es común a todas las estrategias concretas y declara el método que usa el contexto (`execute(data)`).
>   3. Las **Estrategias Concretas** implementan variaciones del algoritmo.
>   4. El contexto llama a `strategy.execute()` sin saber qué estrategia es.
>   5. El **Cliente** crea la estrategia y la pasa al contexto con `setStrategy`; puede cambiarla en tiempo de ejecución.

```mermaid
classDiagram
  class Context { -strategy +setStrategy(strategy) +doSomething() }
  class Strategy { <<interface>> +execute(data) }
  Context o--> Strategy
  Strategy <|.. ConcreteStrategyA
  Strategy <|.. ConcreteStrategyB
```

La implementación completa está en [[02 - Strategy - implementación en Ruby|Strategy: implementación en Ruby]] y un ejercicio resuelto en [[01 - Ejercicio - Strategy para procesador de pagos|Ejercicio: procesador de pagos]].

> [!tip] Complemento (slides "Patrones de Diseño: Comportamiento")
> - Cada algoritmo está en una clase separada, pero todas tienen **uno o más métodos públicos con la misma firma** (nombre y número de argumentos). La clase que usa las estrategias interactúa con ellas mediante esos métodos, sin saber cuál está usando.
> - Esos métodos comunes se definen en la **clase padre como "abstractos"** (en Ruby, con `raise NotImplementedError`) para obligar a las hijas a sobrescribirlos.
> - Ejemplo ya visto: [[08 - Ejemplo de diseño - Filtros de libros|filtros de libros]] (`BookStore` + `FilterStrategy`). Ejercicio de las slides: `Course` con `ImproveStrategy` (`ImproveMin`, `ImproveMax`) para subir las notas de distintas formas.
> - **Cuándo usarlo:** cuando hay varias variantes de un algoritmo y se elige entre ellas con `if` o `case`. Cada `when` pasa a ser una estrategia.

## Preguntas de repaso

1. ¿Qué problema resuelve Strategy?
> [!question]- Respuesta
> El de una clase con muchas variantes de un algoritmo (normalmente un `if`/`case` que crece), difícil de mantener y que hay que modificar para cada variante nueva.

2. ¿Cuáles son los participantes del patrón?
> [!question]- Respuesta
> El Contexto (tiene una referencia a una estrategia y llama a su método común), la interfaz Estrategia, las Estrategias Concretas y el Cliente, que elige la estrategia y se la pasa al contexto.

3. ¿Por qué se dice que "sustituye herencia por composición"?
> [!question]- Respuesta
> Porque en vez de crear subclases del contexto para cada variante, el contexto **contiene** un objeto estrategia y le delega el algoritmo; ese objeto se puede cambiar en tiempo de ejecución.

4. ¿Cómo cumple el principio abierto/cerrado?
> [!question]- Respuesta
> Agregar un algoritmo nuevo significa crear una nueva clase de estrategia, sin modificar el contexto ni las demás estrategias.
