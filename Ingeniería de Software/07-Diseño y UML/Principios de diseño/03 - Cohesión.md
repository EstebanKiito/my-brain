---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[01 - Buen diseño de software|Buen diseño de software]]"]
---
# Cohesión

La cohesión mide **qué tan enfocada está una unidad de código** (clase, método o módulo) en una sola tarea o entidad. Un buen diseño busca **alta cohesión**.

## Cohesión
- Se refiere a **qué tan BIEN un código MAPEA a una ENTIDAD**.
- **+ Diseño → + Cohesión**
- **Alta cohesión** → cada clase, método o módulo es **responsable de una tarea**.
- **Buenas clases** → **alto nivel de cohesión**.

> [!tip] Complemento (slides "Diseño Orientado al Objeto" y libro del curso, cap. 8.6)
> - En un sistema con alta cohesión, **cada unidad de código es responsable de una tarea bien definida**. Es el **Principio de Responsabilidad Única** (SRP): una clase debería tener una sola razón para cambiar.
> - **Visualización de las slides:** las clases son cubos y los puntos dentro son sus atributos y métodos; hay una línea entre dos elementos si uno depende del otro (un método llama a otro, o accede a un atributo). Una clase cohesiva tiene sus elementos muy conectados **entre sí** y pocas líneas hacia afuera.
> - **Tipos de cohesión** (libro), de menor (malo) a mayor (deseable): coincidencial → lógica → temporal → procedural → comunicacional → secuencial → **funcional**.
> - Una clase enfocada en una sola cosa es más fácil de entender, mantener y extender.

> [!example] Ejemplo extra — baja vs. alta cohesión
> ```ruby
> # Baja cohesión: una clase que hace de todo
> class Reporte
>   def calcular_totales; end
>   def generar_pdf; end
>   def enviar_por_email; end
>   def guardar_en_bd; end
> end
>
> # Alta cohesión: cada clase con una responsabilidad
> class CalculadoraTotales; end
> class GeneradorPDF; end
> class Mailer; end
> class RepositorioReportes; end
> ```

## Preguntas de repaso

1. ¿Qué es la cohesión y qué nivel se busca?
> [!question]- Respuesta
> Qué tan bien una unidad de código se mapea a una sola entidad o tarea. Se busca alta cohesión: cada clase, método o módulo responsable de una tarea bien definida.

2. ¿Qué principio está ligado a la alta cohesión?
> [!question]- Respuesta
> El Principio de Responsabilidad Única (Single Responsibility).

3. ¿Por qué no basta con minimizar el acoplamiento?
> [!question]- Respuesta
> Porque se podría poner todo en una sola clase (sin acoplamiento) y quedaría con pésima cohesión. Hay que buscar bajo acoplamiento **y** alta cohesión al mismo tiempo.
