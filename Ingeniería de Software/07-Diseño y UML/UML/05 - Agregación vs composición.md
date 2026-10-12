---
ramo: Ingeniería de Software
tema: UML
tags: [ingsoft/uml, origen/complemento]
prerrequisitos: ["[[04 - Relaciones entre clases en UML|Relaciones entre clases en UML]]"]
---
# Agregación vs. composición

> [!tip] Complemento — nota nueva (comparación basada en las slides "UML" y el libro del curso, cap. 8.10)
> **Qué es:** las dos son relaciones "todo–parte". La diferencia está en **quién crea las partes y si estas pueden existir sin el todo**.
>
> | | Agregación ◇ | Composición ◆ |
> |---|---|---|
> | Símbolo | rombo **vacío** en el todo | rombo **lleno** en el todo |
> | ¿Quién crea las partes? | se crean **fuera** y se le pasan al todo | el todo las crea **dentro** de sí |
> | ¿La parte existe sin el todo? | **sí** | **no** (muere con el todo) |
> | Dependencia | débil | fuerte |
> | Ejemplo del libro | un autor tiene referencias a una o más cuentas | una entrada de blog compuesta de introducción y cuerpo |
>
> ```ruby
> # Agregación: los jugadores existen antes y fuera del equipo
> class Equipo
>   def initialize(jugadores)
>     @jugadores = jugadores          # recibidos desde afuera
>   end
> end
>
> # Composición: las habitaciones se crean dentro de la casa
> class Casa
>   def initialize
>     @habitaciones = [Habitacion.new, Habitacion.new]   # creadas aquí
>   end
> end
> ```
>
> ```mermaid
> classDiagram
>   Equipo o-- Jugador : agregación
>   Casa *-- Habitacion : composición
> ```
>
> **Regla práctica para la prueba:** busca dónde está el `.new` de la parte. Si está **dentro** de la clase contenedora → composición. Si la parte llega por **parámetro** → agregación.

## Preguntas de repaso

1. ¿Cuál es la diferencia clave entre agregación y composición?
> [!question]- Respuesta
> En la composición el todo crea y posee las partes, que no existen sin él. En la agregación las partes se crean afuera y pueden existir independientemente.

2. `class Auto; def initialize; @motor = Motor.new; end; end`: ¿agregación o composición?
> [!question]- Respuesta
> Composición: el motor se crea dentro del auto.

3. `class Curso; def initialize(alumnos); @alumnos = alumnos; end; end`: ¿agregación o composición?
> [!question]- Respuesta
> Agregación: los alumnos se crean fuera y se pasan al curso; existen sin él.
