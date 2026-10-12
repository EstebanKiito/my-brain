---
ramo: Ingeniería de Software
tema: Patrones de Diseño
tags: [ingsoft/patrones, patron/creacional, origen/complemento]
prerrequisitos: ["[[05 - Patrón Factory Method|Patrón Factory Method]]", "[[01 - Patrón Abstract Factory|Patrón Abstract Factory]]"]
---
# Factory Method vs Abstract Factory

> [!tip] Complemento — nota nueva (comparación a partir de las notas de cada patrón)
> **Qué es:** los dos esconden el `new` de las clases concretas, pero a distinta escala.
>
> | | [[05 - Patrón Factory Method\|Factory Method]] | [[01 - Patrón Abstract Factory\|Abstract Factory]] |
> |---|---|---|
> | Qué crea | **un** producto | una **familia** de productos relacionados |
> | Mecanismo | **herencia**: la subclase sobrescribe el método fábrica | **composición**: el cliente recibe un objeto fábrica |
> | Número de métodos de creación | uno (`factory_method`) | uno por producto (`crear_producto_a`, `crear_producto_b`, …) |
> | Quién usa el producto | la propia superclase (`alguna_operacion`) | el cliente que recibió la fábrica |
> | Ejemplo | logística: camión o barco | muebles: victorianos o modernos (silla + sofá + mesa) |
>
> - Una Abstract Factory suele **implementarse con varios Factory Methods**: cada `crear_…` es un método fábrica.
> - Para **un solo** producto que varía, Factory Method. Para **varios** productos que deben ser **consistentes entre sí**, Abstract Factory.
> - Los otros creacionales: [[03 - Patrón Builder|Builder]] arma **un objeto complejo paso a paso**; [[07 - Patrón Singleton|Singleton]] controla que haya **una sola instancia**.

## Preguntas de repaso

1. ¿Qué patrón usa herencia y cuál composición?
> [!question]- Respuesta
> Factory Method usa herencia (las subclases sobrescriben el método fábrica). Abstract Factory usa composición (el cliente recibe un objeto fábrica).

2. Necesitas crear botones, checkboxes y menús que combinen entre sí para Windows o macOS. ¿Cuál usas?
> [!question]- Respuesta
> Abstract Factory: es una familia de productos relacionados con una variante por sistema operativo.

3. ¿Qué patrón creacional usarías para construir un pedido con muchas partes opcionales?
> [!question]- Respuesta
> Builder, porque construye un objeto complejo paso a paso con partes opcionales.
