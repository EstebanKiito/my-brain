---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/complemento]
prerrequisitos: ["[[Modelo en cascada]]", "[[Procesos iterativos]]", "[[Procesos incrementales]]", "[[Procesos iterativos e incrementales]]"]
---
# Comparación de modelos de proceso

> [!tip] Complemento — nota nueva (tabla armada a partir de las notas del tema)
> **Qué es:** una vista lado a lado de los modelos de proceso del curso, para repasar diferencias de un vistazo.
>
> | Modelo | Tipo | Feedback del usuario | Manejo del riesgo | Cambios | Punto fuerte | Punto débil |
> |---|---|---|---|---|---|---|
> | [[Modelo en cascada\|Cascada]] | Secuencial | Al final | Tardío | Muy difíciles | Simple y fácil de seguir | Rígido, riesgo alto hasta el final |
> | [[Modelo en espiral\|Espiral]] | Iterativo | En cada ciclo | **Explícito** en cada ciclo | Posibles | Manejo de riesgo | Difícil estimar tiempo; costoso |
> | [[Modelo de prototipos\|Prototipos]] | Iterativo | Muy temprano (sobre el prototipo) | Reduce imprevistos | Fáciles | Aclara requisitos | Proyecto sin fin, "casi listo" |
> | [[Proceso unificado (RUP)\|Proceso Unificado]] | Iterativo, 4 fases | Por iteración | Enfocado en riesgos críticos | Posibles, pero formal | Casos de uso y arquitectura | Mucha documentación y costo |
> | [[Procesos incrementales\|Incremental]] | Incremental | Limitado hasta terminar | Medio | Difíciles sobre lo ya hecho | Entrega por piezas | Supone requisitos claros |
> | [[Procesos iterativos e incrementales\|Iterativo e incremental]] / [[Metodologías ágiles y manifiesto ágil\|Ágil]] | Ambos | Continuo | Temprano y continuo | Bienvenidos | Valor temprano, adaptación | Puede haber que rehacer; requiere automatizar |
>
> **Cómo recordarlo:**
> - **Cascada** = una sola pasada.
> - **Iterativo** = repetir y refinar el todo.
> - **Incremental** = agregar piezas terminadas.
> - **Ágil** = las dos cosas en ciclos cortos, con el cliente.

## Preguntas de repaso

1. ¿Qué modelo introduce el análisis de riesgo explícito y cuál lo posterga hasta el final?
> [!question]- Respuesta
> El modelo en espiral lo hace explícito en cada ciclo. La cascada posterga la reducción del riesgo hasta las etapas avanzadas.

2. ¿En qué se parecen y en qué se diferencian el Proceso Unificado y los procesos ágiles?
> [!question]- Respuesta
> Ambos son iterativos. RUP es formal, pone mucho énfasis en la documentación y no siempre es incremental. Los ágiles entregan incrementos usables en cada ciclo y privilegian el software funcionando sobre la documentación.

3. Un cliente no tiene claro lo que quiere y el equipo necesita validar una interfaz rápido. ¿Qué modelo encaja mejor?
> [!question]- Respuesta
> El modelo de prototipos (por ejemplo, con un prototipo desechable), porque le da al usuario una vista temprana para aclarar los requisitos.
