---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, origen/complemento]
prerrequisitos: ["[[07 - Estimación de software|Estimación de software]]"]
---
# Cono de la incertidumbre

> [!tip] Complemento — nota nueva (fuente: slides "Estimaciones" y libro del curso, cap. 7.6; Barry Boehm et al., *Software Cost Estimation with COCOMO II*, 2000)
> **Qué es:** un gráfico que muestra cómo el **error posible de una estimación disminuye a medida que avanza el proyecto**.
>
> ![Slide - cono de la incertidumbre](../adjuntos/Slide%20-%20cono%20de%20la%20incertidumbre.png)
>
> - Al inicio (concepto inicial), la estimación puede equivocarse hasta **4 veces hacia arriba o hacia abajo** (de 0,25× a 4×).
> - A medida que se completan hitos (definición del producto, requisitos, diseño de interfaz, diseño detallado), el cono se estrecha hasta llegar a 1× al terminar el software.
> - El gráfico muestra las etapas de un proceso en cascada, pero **vale igual para ágil**: en el eje X van el sprint 1, el sprint 2, etc.
>
> **Dos mecanismos para estrechar el cono (libro):**
> 1. El **desarrollo iterativo e incremental**: cada sprint entrega datos reales, como la velocidad.
> 2. La **descomposición en unidades pequeñas**: es más fácil estimar "implementar la autenticación de usuarios" que "construir un sitio web para una empresa de delivery". Aquí sirven las [[01 - Historias de usuario|historias de usuario]].
>
> ```mermaid
> flowchart LR
>   A["Concepto inicial: 0,25× a 4×"] --> B["Requisitos completos: ~0,67× a 1,5×"] --> C["Diseño detallado: ~0,8× a 1,25×"] --> D["Software completo: 1×"]
> ```
> *Los valores intermedios son los típicos del modelo de Boehm y McConnell; la slide muestra la forma general.*

## Preguntas de repaso

1. ¿Qué representa el cono de la incertidumbre?
> [!question]- Respuesta
> Que el margen de error de las estimaciones es muy grande al principio del proyecto (hasta 4× hacia arriba o abajo) y se reduce a medida que el proyecto avanza y se conoce mejor.

2. ¿Qué dos mecanismos ayudan a reducir el cono?
> [!question]- Respuesta
> El desarrollo iterativo e incremental (que da datos reales en cada iteración) y la descomposición del trabajo en unidades pequeñas, más fáciles de estimar.

3. ¿Aplica el cono a proyectos ágiles?
> [!question]- Respuesta
> Sí. En lugar de etapas de cascada, el eje X son los sprints, y la incertidumbre baja con cada sprint completado.
