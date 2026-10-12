---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[01 - Historias de usuario|Historias de usuario]]", "[[05 - Product Backlog|Product Backlog]]"]
---
# Story points (puntos de historia)

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.2 y 7.9)
> **Qué es:** un story point es una **unidad relativa** de medida del **esfuerzo** necesario para completar una historia de usuario.
>
> **Características:**
> - Los estiman **todos los miembros del equipo**.
> - Son un **valor relativo**: el número cambia de equipo a equipo. Un 5 de un equipo no equivale a un 5 de otro.
>
> **¿Qué significa "relativo"?**
> - Los puntos dan una visión del **tamaño** de una historia, como las tallas S, M y L de una polera.
> - Una historia de 3 puntos es más grande que una de 1 y más pequeña que una de 5: "lógica pura".
> - **¡Ojo!** Una historia de 2 puntos **no es necesariamente el doble** de una de 1.
>
> **¿Cómo se determinan?** Se consideran tres factores:
> - **Dificultad:** ¿cuánto esfuerzo requiere completar la historia, según la Definition of Done?
> - **Complejidad:** ¿es una tarea sencilla o un desafío?
> - **Incertidumbre:** ¿qué posibilidad hay de encontrar sorpresas que no habíamos previsto?
>
> **Procedimiento:**
> 1. Se elige una **historia de referencia** que todos entienden bien y se le asigna un número de puntos (puede ser cualquiera).
> 2. Las demás historias se puntúan **en comparación** con ella: ¿es más difícil?, ¿es más fácil?
>
> **Escalas típicas** (libro): **Fibonacci** (1, 2, 3, 5, 8, 13…) o **exponencial** (1, 2, 4, 8…). Los números crecen cada vez más porque, mientras más grande la historia, menos precisa puede ser la estimación.
>
> Ventaja compartida con los [[09 - Puntos de función y líneas de código|puntos de función]]: **no dependen del lenguaje** y sirven para estimar **temprano**.

> [!example] Ejemplo extra
> El equipo toma "iniciar sesión" como referencia y le asigna **3 puntos**.
> - "Cerrar sesión" es claramente más simple: **1 punto**.
> - "Pagar con tarjeta" tiene más pasos e integración externa con incertidumbre: **8 puntos**.
>
> Nadie dijo cuántas horas toma cada una; solo se compararon entre sí.

## Preguntas de repaso

1. ¿Qué mide un story point y por qué es relativo?
> [!question]- Respuesta
> Mide el esfuerzo (dificultad, complejidad e incertidumbre) de una historia, comparado con otras historias del mismo equipo. Es relativo porque no equivale a horas y su valor depende de la historia de referencia y del equipo.

2. Verdadero o falso: una historia de 2 puntos toma exactamente el doble que una de 1 punto.
> [!question]- Respuesta
> Falso. Solo se sabe que es más grande; los puntos no son proporcionales.

3. ¿Qué tres factores se consideran al asignar puntos?
> [!question]- Respuesta
> Dificultad (esfuerzo), complejidad e incertidumbre (posibles sorpresas).

4. ¿Por qué se usan escalas como Fibonacci?
> [!question]- Respuesta
> Porque a mayor tamaño hay más incertidumbre: los saltos crecientes evitan discutir diferencias falsamente precisas entre historias grandes (por ejemplo, 20 contra 21).
