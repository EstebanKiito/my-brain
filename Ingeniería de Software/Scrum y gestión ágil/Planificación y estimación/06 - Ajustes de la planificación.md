---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[05 - Planificación de un release|Planificación de un release]]"]
---
# Ajustes de la planificación

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.5)
> **Qué es:** cuando el proyecto va atrasado respecto del plan, hay tres formas de ajustar: **tiempo, alcance o calidad**. Solo las dos primeras son aceptables.
>
> **La necesidad de ajustar (slides):**
> - La agilidad implica **abrazar el cambio**.
> - Las estimaciones tempranas (siempre necesarias) suelen no ser muy certeras.
> - A medida que el proyecto avanza hay más elementos para mejorar las estimaciones iniciales, y puede ser necesario ajustar.
> - **El plan del sprint NO SE AJUSTA.** El ajuste ocurre una vez terminado el sprint, sobre todo después de la Sprint Review y de la retrospectiva.
>
> **Tipos de ajuste**
> | Ajuste | Qué se negocia | Recepción |
> |---|---|---|
> | **Por tiempo** | Más plazo ("ir avergonzadamente a negociar más tiempo") | Suele recibirse mal: "no se cumple lo prometido" |
> | **Por alcance** | Se entrega en la fecha pactada, pero con menos funcionalidades en el release | Generalmente bien recibido, si se priorizó bien |
> | **Por calidad** | Nada: se "apura" quitando tests, revisiones, pares, etc. | **NO RECOMENDABLE.** La calidad no se negocia: termina costando más caro |
>
> **Ejemplo del libro:** se planificaron 8 sprints de 2 semanas para 40 historias, y al cerrar el sprint 4 hay 16 terminadas.
> - **Por tiempo:** a ese ritmo, las 24 restantes toman 6 sprints y no 4 → se pide un mes más.
> - **Por alcance:** en la fecha se alcanzan 32 de 40. Como se priorizó lo más importante, esas 32 deberían tener el 90% o más de lo que le importa al cliente → se entrega en la fecha y el resto va a un release futuro.
> - **Por calidad:** se cumple fecha y alcance, pero con calidad comprometida y un equipo desgastado y frustrado.

> [!tip] Complemento — deuda técnica (libro)
> Ajustar por calidad genera **deuda técnica**: igual que una deuda financiera, se paga después **con intereses**. Un diseño apresurado ahorra tiempo hoy, pero cuesta más cuando hay que corregirlo; un bug no detectado puede costar después muchas horas de *debugging*.

## Preguntas de repaso

1. ¿Cuáles son los tres tipos de ajuste y cuál no se debe hacer?
> [!question]- Respuesta
> Por tiempo, por alcance y por calidad. Nunca se debe ajustar por calidad: la calidad no se negocia.

2. ¿Por qué el ajuste por alcance suele ser mejor recibido que el ajuste por tiempo?
> [!question]- Respuesta
> Porque se cumple la fecha comprometida y, si se priorizó por valor, lo que queda fuera es lo menos importante para el cliente.

3. ¿Se puede ajustar el plan en medio de un sprint?
> [!question]- Respuesta
> No. El plan del sprint no se ajusta; el ajuste se hace al terminarlo, sobre todo después de la Sprint Review y la retrospectiva.

4. ¿Qué es la deuda técnica?
> [!question]- Respuesta
> El costo futuro de atajos tomados hoy (menos pruebas, diseño apresurado). Como una deuda, se paga después con intereses: más bugs, más tiempo de corrección y más dificultad para cambiar el sistema.
