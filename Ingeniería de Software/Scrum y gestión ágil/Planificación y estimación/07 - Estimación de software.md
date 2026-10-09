---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, origen/complemento]
prerrequisitos: ["[[01 - Story points|Story points]]"]
---
# Estimación de software

*En mis apuntes, la sección "8. Estimaciones" quedó solo con el título; esta nota y las siguientes se arman con las slides y el libro del curso.*

> [!tip] Complemento — qué queremos estimar (slides "Estimaciones" y libro del curso, cap. 7.1–7.2)
> | Magnitud | Unidad | Por qué importa |
> |---|---|---|
> | **Esfuerzo** | meses-hombre, semanas-hombre | Primera aproximación del **costo** |
> | **Tiempo** (duración) | meses, semanas, días | Es lo que más interesa antes de empezar: se firman compromisos y puede haber multas |
> | **Tamaño** | puntos de función, requerimientos, story points, líneas de código | Es lo **primero** que se estima, porque de él dependen el esfuerzo y el tiempo |
>
> - **Esfuerzo = tiempo × personas.** Por ejemplo, 5 personas durante 4 meses son 20 meses-hombre.
> - **Ley de Brooks** (*El mítico hombre-mes*): en software, **personas y tiempo no son intercambiables**. Que 5 personas tarden 4 meses no significa que 10 personas tarden 2.
> - Se estima **durante todo el proyecto**, no solo al inicio: las estimaciones se corrigen al terminar el primer sprint, al cambiar el equipo, etc.

> [!tip] Complemento — objetivos del negocio vs. compromisos (slides)
> Muchas "estimaciones" en realidad son **objetivos** del negocio: "necesitamos la versión 2.1 para una demo en mayo", "solo tenemos 2 millones de dólares".
>
> **Diálogo poco productivo:**
> - *Ejecutivo:* lo necesitamos en 3 meses.
> - *Líder:* estimamos 5 meses.
> - *Ejecutivo:* ¿5 meses? ¡No me escuchaste!
>
> **Diálogo productivo:** el líder pregunta qué es lo más importante para la demo y negocia el alcance: "entregaremos todas las funcionalidades que podamos en los siguientes 3 meses".
>
> Es mejor preguntar si el número es **un estimado o un objetivo**.

> [!tip] Complemento — toda estimación es una probabilidad (slides y libro)
> - Suponer un 100% de probabilidad de que el resultado real sea exactamente el estimado es poco realista.
> - Es incorrecto suponer que la estimación sigue una **curva normal**: hay un límite a qué tan rápido puede terminar un equipo, pero no a cuánto puede atrasarse. La curva real es **asimétrica, con cola hacia el atraso**: hay un 50% de probabilidad de terminar antes o en la fecha y un 50% de terminar después.
> - *"La predicción más optimista que tiene una probabilidad distinta de cero de ser verdad"* (Tom DeMarco). Si tienes una estimación, su probabilidad no es 100%: **hay que preguntar cuál es**.
> - **Una buena estimación** es la que da una vista suficientemente clara de la realidad del proyecto como para que el gestor tome buenas decisiones para lograr sus objetivos (Steve McConnell, *Software Estimation*, 2006).
> - Sobre el "90% de confianza": en un experimento de 10 preguntas el promedio de aciertos fue 2,8 y solo el 2% acertó 8 o más. Solemos estar demasiado seguros.
>
> ![Slide - distribución de probabilidad de una estimación](../adjuntos/Slide%20-%20distribución%20de%20probabilidad%20de%20una%20estimación.png)

> [!tip] Complemento — ¿es mejor sobreestimar o subestimar? (slides y libro, cap. 7.5)
> ![Slide - penalización por subestimar y sobreestimar](../adjuntos/Slide%20-%20penalización%20por%20subestimar%20y%20sobreestimar.png)
>
> - **Sobreestimar** tiene una penalización **lineal** por dos leyes:
>   - **Ley de Parkinson:** el trabajo se expande hasta llenar el tiempo disponible.
>   - **Ley de Goldratt** ("síndrome del estudiante"): si sobra tiempo, se malgasta al comienzo.
> - **Subestimar** tiene una penalización **no lineal**, que puede crecer exponencialmente: estrés, errores de planificación, defectos, recortes en análisis y diseño, y un efecto dominó de más atrasos.
> - Conclusión: **es mucho peor subestimar.**

> [!tip] Complemento — fuentes de error y buenas prácticas (slides y libro, cap. 7.4, 7.7 y 7.8)
> **Las cuatro fuentes de error:**
> 1. **Información imprecisa sobre el proyecto:** "era una página simple" y resultó ser un e-commerce completo.
> 2. **Información imprecisa sobre las capacidades del equipo.**
> 3. **Imprecisiones del proceso de estimación:** datos de la industria y no del equipo, modelos aproximados, etc.
> 4. **Cambios frecuentes en los requerimientos:** el proyecto "blanco móvil".
>
> **Buenas prácticas:**
> - **Evitar la respuesta improvisada.** No "imagino que una semana", sino "lo estudio y te contesto en un rato". Incluso un análisis superficial, hecho con calma, se acerca mucho más a la realidad.
> - **Precisión ≠ exactitud.** π = 5,123233341 es preciso pero no exacto. La unidad comunica precisión: decir "90 días" hace que 7 días de atraso sean un problema; decir "3 meses" tolera incluso 2 semanas.
>
> El error de una estimación se reduce con el tiempo: ver [[08 - Cono de la incertidumbre|Cono de la incertidumbre]].

## Preguntas de repaso

1. ¿Qué tres magnitudes se estiman y cuál se estima primero?
> [!question]- Respuesta
> Esfuerzo (costo, en meses-hombre), tiempo (duración) y tamaño. Primero se estima el tamaño, porque de él dependen las otras dos.

2. ¿Por qué es peor subestimar que sobreestimar?
> [!question]- Respuesta
> Sobreestimar tiene una penalización lineal (ley de Parkinson y de Goldratt). Subestimar tiene una penalización no lineal: estrés, defectos, recortes en diseño y un efecto dominó de atrasos.

3. ¿Por qué la curva de probabilidad de una estimación no es normal?
> [!question]- Respuesta
> Porque hay un límite a qué tan rápido puede completarse un trabajo, pero no a cuánto puede atrasarse. La curva es asimétrica, con cola hacia el atraso.

4. ¿Qué dice la ley de Brooks sobre el esfuerzo?
> [!question]- Respuesta
> Que en software personas y tiempo no son intercambiables: duplicar las personas no reduce el tiempo a la mitad, por el costo de comunicación y coordinación.

5. Nombra las cuatro fuentes de error en las estimaciones.
> [!question]- Respuesta
> Información imprecisa sobre el proyecto, información imprecisa sobre las capacidades del equipo, imprecisiones del proceso de estimación y cambios frecuentes en los requerimientos.
