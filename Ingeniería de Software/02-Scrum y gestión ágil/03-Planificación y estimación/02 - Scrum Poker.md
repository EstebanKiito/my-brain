---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[01 - Story points|Story points]]"]
---
# Scrum Poker (Planning Poker)

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.2 y 7.9)
> **Qué es:** una técnica de **estimación colaborativa** en la que el equipo asigna [[01 - Story points|story points]] a una historia usando cartas, para llegar a un **consenso**.
>
> **Pasos (slides):**
> 1. Se selecciona una historia. Cada participante elige una carta del mazo; el valor de la carta son los puntos que cree que tiene la historia.
> 2. Las cartas se muestran **en paralelo** (todas a la vez) **para evitar el sesgo**.
> 3. Si los valores son muy distintos, se abre una discusión, normalmente entre quien puso el valor **más alto** y quien puso el **más bajo**.
> 4. Después de la discusión se vuelve al paso 1.
> 5. Termina cuando hay **consenso** sobre los puntos de la historia.
>
> ![Slide - cartas de Scrum Poker](../adjuntos/Slide%20-%20cartas%20de%20Scrum%20Poker.png)
>
> **El mazo típico:** ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, **?** (no sé), **∞** (demasiado grande, hay que dividirla) y **☕** (necesito una pausa).
>
> **Por qué funciona** (libro): quien puso 1 puede no haber visto una complejidad que sí vio quien puso 5. Al conversar, el equipo comparte información y converge, a veces en varias rondas. Participan los desarrolladores y el Product Owner, que aclara dudas sobre la historia.

> [!example] Ejemplo extra
> Historia "exportar reporte a PDF". Primera ronda: 2, 3, 3, 13. Habla quien puso 13: "la librería de PDF no soporta tablas, hay que hacerlo a mano". Habla quien puso 2: "pensé que era un botón". Segunda ronda: 8, 8, 5, 8 → acuerdan **8**.

## Preguntas de repaso

1. ¿Por qué las cartas se muestran al mismo tiempo?
> [!question]- Respuesta
> Para evitar el sesgo de anclaje: que la opinión del primero (o del más experimentado) influya en los demás.

2. Si las estimaciones difieren mucho, ¿quiénes discuten primero?
> [!question]- Respuesta
> Quien asignó el valor más alto y quien asignó el más bajo, porque probablemente vieron cosas distintas de la historia.

3. ¿Qué significan las cartas "?" e "∞"?
> [!question]- Respuesta
> "?" = no tengo suficiente información para estimar. "∞" = la historia es demasiado grande para estimarla; hay que dividirla.
