---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, ingsoft/agil, origen/complemento]
prerrequisitos: ["[[09 - Metodologías ágiles y manifiesto ágil|Metodologías ágiles y manifiesto ágil]]"]
---
# Programación extrema (XP)

> [!tip] Complemento — nota nueva (fuente: slides "Procesos de Desarrollo de Software" y libro del curso, cap. 2.4)
> **Qué es:** Extreme Programming (XP) es uno de los primeros modelos ágiles. Más que un modelo de proceso, es una **colección de buenas prácticas** alineadas con el [[09 - Metodologías ágiles y manifiesto ágil|Manifiesto Ágil]], llevadas a niveles "extremos".
>
> **Origen (slides):** Kent Beck, 1999. Se desarrolló durante el proyecto C3 junto a Ron Jeffries.
>
> **Prácticas destacadas en las slides:**
> - **Test first:** pruebas de aceptación y unitarias escritas antes del código.
> - **Integración continua.**
> - **Programación en pares** (*pair programming*).
> - **Refactorización repetida.**
>
> **Pilares según el libro:**
> - El cliente es parte integral del equipo de desarrollo.
> - Casos de uso concisos (tres frases).
> - El cliente especifica los casos de prueba.
> - Máxima simplicidad en el software.
> - Programación en pares.
> - Propiedad compartida del código.
> - Pruebas continuas.

> [!tip] Complemento — programación en pares
> Dos desarrolladores trabajan en el mismo código con un solo teclado y mouse: uno **conduce** (escribe) y el otro **revisa**, y van alternando.
>
> **Ventajas (libro):**
> - la revisión en pares detecta errores temprano;
> - al menos dos personas entienden a fondo el código;
> - el código suele ser más legible y de mejor calidad;
> - facilita aplicar estándares de codificación.
>
> **Costo a considerar:** dos personas en una tarea. Se justifica cuando el código es crítico o complejo, o para traspasar conocimiento.

> [!example] Ejemplo extra — "test first" en una línea
> Antes de implementar `calcular_descuento`, se escribe la prueba `assert_equal 90, calcular_descuento(100, 10)`. Primero falla; luego se implementa lo mínimo para que pase y finalmente se refactoriza. Las pruebas en Rails se ven en el tema Testing.

## Preguntas de repaso

1. ¿Por qué se dice que XP no es tanto un modelo de proceso?
> [!question]- Respuesta
> Porque es principalmente una colección de buenas prácticas de ingeniería (pruebas primero, integración continua, pares, refactorización) alineadas con el Manifiesto Ágil, más que un ciclo de fases definido.

2. Nombra cuatro prácticas de XP.
> [!question]- Respuesta
> Test first (pruebas de aceptación y unitarias), integración continua, programación en pares y refactorización repetida. También: cliente en el equipo, propiedad compartida del código y simplicidad.

3. ¿Qué ventajas tiene la programación en pares?
> [!question]- Respuesta
> Detecta errores temprano, al menos dos personas conocen el código, mejora la legibilidad y la calidad, y facilita seguir estándares de codificación.

4. Verdadero o falso: XP es un modelo altamente estructurado y rígido.
> [!question]- Respuesta
> Falso. Es un enfoque ágil basado en prácticas y en adaptarse al cambio.
