---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/complemento]
prerrequisitos: []
---
# Proceso de desarrollo de software

> [!tip] Complemento — nota nueva (fuente: slides "Procesos de Desarrollo de Software" y libro del curso, cap. 2)
> **Qué es:** un proceso de desarrollo es un conjunto de actividades que se realizan en secuencia para crear un software. Es *"la creación y traducción de una necesidad de las personas en requerimientos, de requerimientos en diseño, del diseño en código, pruebas, instalación, etc."*
>
> **Por qué hace falta uno**
> - Escribir código es relativamente simple. Lo difícil es desarrollar software **de calidad**:
>   - trabajar con personas (clientes, desarrolladores, managers) puede ser un problema;
>   - los programas grandes toman mucho tiempo;
>   - en cuanto participan más de dos personas aparecen complicaciones, y eso incluye al cliente.
> - Por eso **seguir un proceso (cualquier proceso) es de suma importancia**.
> - Las organizaciones quieren procesos **bien definidos, entendibles y repetibles** para:
>   - encontrar y repetir buenas prácticas;
>   - administrar el proyecto: ¿qué hacemos después?, ¿en qué tarea vamos?, ¿vamos atrasados?, ¿cómo medimos el progreso?, ¿cuánto falta en tiempo o costo?;
>   - que los miembros nuevos sepan qué hacer.
> - Desarrollar sin proceso (*"hacking"*) puede funcionar con personas muy talentosas, pero **no es repetible**: repetir lo mismo no garantiza el mismo éxito.
>
> **Etapas que todo proceso considera en alguna medida** (según las slides):
> 1. Recopilación de requerimientos
> 2. Especificación de requerimientos
> 3. Diseño
> 4. Desarrollo (diseño, implementación, pruebas)
> 5. Validación
> 6. Evolución (mantenimiento)
>
> La diferencia entre un proceso y otro está en **cuál de estas etapas enfatiza y en qué orden o con qué repetición las ejecuta**.
>
> El libro da una lista más detallada: estudio de factibilidad, ingeniería de requisitos, diseño de la interfaz de usuario, diseño de la arquitectura, diseño detallado (módulos), programación, integración, verificación (pruebas unitarias y de sistema), validación (pruebas de aceptación), puesta en producción, mantenimiento, documentación y gestión del proyecto.

> [!example] Ejemplo extra — analogía del libro
> Preparar una torta no consiste solo en tener los ingredientes; hay que seguir un procedimiento (mezclar, hornear, decorar) para que el resultado sea consistente. Lo mismo pasa con un auto o un neumático. Si el software es potencialmente más complejo que un auto, también necesita un proceso bien definido.

> [!tip] Complemento — mapa de los modelos de proceso del curso
> ```mermaid
> flowchart TD
>   P[Procesos de desarrollo] --> C[Secuencial: Cascada]
>   P --> I[Iterativos]
>   I --> E[Espiral]
>   I --> PR[Prototipos]
>   I --> U[Proceso Unificado]
>   P --> INC[Incrementales]
>   P --> II[Iterativos e incrementales]
>   II --> AG[Ágiles: XP, Scrum, Kanban]
> ```
> - [[02 - Modelo en cascada|Modelo en cascada]]
> - [[03 - Procesos iterativos|Procesos iterativos]]: [[04 - Modelo en espiral|Modelo en espiral]], [[05 - Modelo de prototipos|Modelo de prototipos]], [[06 - Proceso unificado (RUP)|Proceso unificado (RUP)]]
> - [[07 - Procesos incrementales|Procesos incrementales]]
> - [[08 - Procesos iterativos e incrementales|Procesos iterativos e incrementales]] → [[09 - Metodologías ágiles y manifiesto ágil|Metodologías ágiles y manifiesto ágil]], [[10 - Programación extrema (XP)|Programación extrema (XP)]]
> - Para elegir entre ellos: [[11 - Cómo elegir un proceso de desarrollo|Cómo elegir un proceso de desarrollo]] y [[12 - Comparación de modelos de proceso|Comparación de modelos de proceso]].

## Preguntas de repaso

1. ¿Qué es un proceso de desarrollo de software?
> [!question]- Respuesta
> Un conjunto de actividades que se realizan en secuencia para crear software: traducir una necesidad en requerimientos, los requerimientos en diseño, el diseño en código, y luego probar, instalar, etc.

2. ¿Por qué una empresa quiere un proceso bien definido y repetible?
> [!question]- Respuesta
> Para repetir buenas prácticas y poder administrar el proyecto: saber qué sigue, medir el progreso, detectar atrasos, estimar tiempo y costo, e incorporar miembros nuevos.

3. ¿Qué etapas considera, en alguna medida, todo proceso?
> [!question]- Respuesta
> Recopilación y especificación de requerimientos, diseño, desarrollo (implementación y pruebas), validación y evolución (mantenimiento). Los procesos se diferencian en cuál etapa enfatizan y en cómo las ordenan o repiten.

4. ¿Cuál es la principal desventaja de desarrollar sin proceso ("hacking")?
> [!question]- Respuesta
> No es repetible: aunque funcione con personas muy talentosas, repetir lo mismo no garantiza el mismo resultado.
