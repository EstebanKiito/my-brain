---
ramo: "Sistemas Distribuidos"
tema: "Gestión del curso"
tags:
  - sd/gestion
  - origen/complemento
prerrequisitos: []
---

# Evaluación y organización del curso

Cómo se organizó el ramo Sistemas Distribuidos (IIC2523, segundo semestre de 2025): metodología, evaluaciones escritas y prácticas, fórmulas de nota y condiciones de aprobación. Sirve como referencia de la estructura del curso; las fechas corresponden a ese semestre.

## Metodología

- Clases expositivas y de discusión, con actividades tipo Kahoot o Menti.
- La presentación está disponible al inicio de cada clase y el PDF se sube después al Syllabus del curso en GitHub.
- Avisos semanales con lo que viene; no hay ayudantías salvo aviso previo.
- Dudas de contenido y evaluaciones en las *discussions* del Syllabus o en clases; avisos oficiales por Canvas.
- Está permitido usar IA como herramienta de apoyo, pero el estudiante debe ser autor de su solución y **referenciar** el uso (prompt y cómo se aprovechó la respuesta); no hacerlo es una falta a la integridad académica.

## Evaluaciones escritas

- **Controles:** periódicos en Canvas, de corrección automática, sobre las clases ya vistas. La mayoría de las preguntas salen directamente de las slides, algunas exigen conectar contenidos. Dos intentos (vale el mejor); se publican a las 13:30 y cierran a las 20:00 del mismo día de la semana siguiente. La nota de controles (NC) es el promedio **sin el peor control**.
- **Interrogaciones y examen:** presenciales y de selección múltiple. I1: sábado 13 de septiembre; I2: jueves 30 de octubre; examen: lunes 1 de diciembre. Ausentarse sin justificación es un 1,0; si se faltó justificadamente a ambas interrogaciones, se recupera en el periodo de examen.

![Fórmula de evaluaciones escritas](adjuntos/F%C3%B3rmula%20de%20evaluaciones%20escritas.png)

> [!example]- Transcripción de la imagen
> Sea NC la nota final de los controles y EC la nota final de las evaluaciones escritas: $EC = 25\% \cdot NC + 35\% \cdot \max(I1, I2) + 40\% \cdot Examen$. EC debe ser mayor o igual a 3,75 o se reprueba el curso.

$$EC = 0{,}25 \cdot NC + 0{,}35 \cdot \max(I1, I2) + 0{,}40 \cdot \text{Examen}$$

Solo cuenta la **mejor** de las dos interrogaciones.

## Evaluaciones prácticas

- **Tareas (3):** en parejas o individuales, de 7 a 10 días hábiles, se entregan a las 20:00, corrección 100 % automatizada con algunos tests públicos (los casos borde son responsabilidad del estudiante). Hasta 2 días de atraso, con un descuento de 1 punto por día aplicado a la **nota máxima**: con 2 días de atraso el máximo es 5,0. La nota de tareas (NT) es su promedio. Los temas fueron servidores TCP con sockets, RPC y relojes lógicos (T1), simulación de algoritmos de coordinación (T2) y transacciones distribuidas con 2PC y control de concurrencia (T3).
- **Presentación (investigación):** en el último mes, grupos de hasta 4 investigan un tema o paper (por ejemplo, Cassandra, Apolo o Valorant), entregan un video y el PDF, y evalúan la presentación de otro grupo. No se usan clases para presentar.

$$NTP = 0{,}7 \cdot NT + 0{,}3 \cdot PR \qquad (NTP \geq 3{,}95)$$

## Nota final

![Condiciones de aprobación](adjuntos/Condiciones%20de%20aprobaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Sea NTP la nota de tareas y presentación, EC la de evaluaciones escritas y NP la nota de presentación al curso: $NP = 0{,}5 \cdot NTP + 0{,}5 \cdot EC$. Se deben cumplir tres condiciones para que la nota final sea NP: $NTP \geq 3{,}95$, $EC \geq 3{,}75$ y $NP \geq 3{,}95$. Si no se cumple alguna, la nota final es $\min(NP, 3{,}9)$.

> [!warning] Las tres condiciones
> Basta fallar una para reprobar, aunque el promedio dé sobre 4: por ejemplo, $EC = 3{,}7$ con $NTP = 6{,}5$ da $NP = 5{,}1$, pero la nota final queda en 3,9.

## Preguntas de repaso

> [!question]- ¿Cuál interrogación cuenta en la nota de evaluaciones escritas?
> Solo la mejor de las dos, que pondera un 35 %.

> [!question]- Con 2 días de atraso en una tarea y una nota de 5,6, ¿qué nota queda?
> 5,0: el descuento se aplica a la nota máxima posible, que con 2 días de atraso es 5,0.

> [!question]- ¿Qué pasa si NP es 4,5 pero EC es 3,6?
> Se reprueba: EC debe ser al menos 3,75, así que la nota final es $\min(4{,}5;\ 3{,}9) = 3{,}9$.
