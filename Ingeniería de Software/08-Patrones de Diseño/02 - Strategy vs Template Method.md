---
ramo: Ingeniería de Software
tema: Patrones de Diseño
tags: [ingsoft/patrones, patron/comportamiento, origen/complemento]
prerrequisitos: ["[[01 - Patrón Strategy|Patrón Strategy]]", "[[03 - Patrón Template Method|Patrón Template Method]]"]
---
# Strategy vs Template Method

> [!tip] Complemento — nota nueva (comparación a partir de las notas de cada patrón)
> **Qué es:** los dos patrones permiten variar un algoritmo y suelen confundirse en la prueba. Esta tabla muestra sus diferencias.
>
> | | [[01 - Patrón Strategy\|Strategy]] | [[03 - Patrón Template Method\|Template Method]] |
> |---|---|---|
> | Qué varía | el **algoritmo completo** | **algunos pasos** de un algoritmo fijo |
> | Mecanismo | **composición**: el contexto *tiene* una estrategia | **herencia**: la subclase *es* una variante |
> | ¿Cuándo se elige la variante? | en **tiempo de ejecución** (se puede cambiar) | al **crear el objeto** (según la subclase) |
> | Dónde queda el esqueleto | cada estrategia tiene el suyo | en el **método plantilla** de la superclase |
> | Ejemplo del curso | filtros de libros, rutas del navegador, pagos | bebidas con cafeína, data miners |
>
> **Cómo decidir:**
> - ¿Las variantes comparten la mayor parte de los pasos y solo cambian algunos? → **Template Method**.
> - ¿Son algoritmos distintos e intercambiables, y quieres cambiarlos en tiempo de ejecución? → **Strategy**.
>
> ```ruby
> # Strategy: el procesador TIENE una estrategia
> PaymentProcessor.new("Ana", 100, PayPal.new).process_payment
>
> # Template Method: Coffee ES una CaffeineBeberage
> Coffee.new.prepareRecipe
> ```

## Preguntas de repaso

1. ¿Qué mecanismo de POO usa cada patrón?
> [!question]- Respuesta
> Strategy usa composición (el contexto contiene un objeto estrategia). Template Method usa herencia (las subclases sobrescriben pasos).

2. Si necesitas cambiar el comportamiento de un objeto mientras el programa corre, ¿cuál usas?
> [!question]- Respuesta
> Strategy, porque basta con asignarle otra estrategia al contexto (`context.strategy = ...`).

3. Tienes tres exportadores (CSV, JSON, XML) que abren el archivo, escriben un encabezado, escriben filas en distinto formato y cierran. ¿Cuál conviene?
> [!question]- Respuesta
> Template Method: el esqueleto (abrir → encabezado → filas → cerrar) es fijo y solo cambia cómo se escriben las filas.
