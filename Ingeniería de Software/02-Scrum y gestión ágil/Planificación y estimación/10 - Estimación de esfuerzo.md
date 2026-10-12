---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, origen/complemento]
prerrequisitos: ["[[09 - Puntos de función y líneas de código|Puntos de función y líneas de código]]", "[[03 - Velocidad de desarrollo|Velocidad de desarrollo]]"]
---
# Estimación de esfuerzo (del tamaño al esfuerzo y la duración)

> [!tip] Complemento — nota nueva (fuente: slides "Estimaciones" y libro del curso, cap. 7.3 y 7.10)
> **Qué es:** una vez estimado el **tamaño**, se pasa al **esfuerzo** (meses-hombre) y a la **duración** usando datos de productividad.
>
> ## Regla de tres (relación lineal)
> - El esfuerzo **no crece linealmente** con el tamaño, pero para tamaños pequeños la regla de tres da una aproximación decente. La curva se aleja de la recta desde unas 250.000 LOC.
> - **De dónde sacar la productividad**, en orden de preferencia:
>   1. datos **del mismo proyecto** (sprints anteriores);
>   2. datos **de la organización** (proyectos similares);
>   3. solo en último término, datos **de la industria** (poco confiables, sobre todo si son de otro país).
> - Conviene recolectar los datos (LOC, tiempo, personas, defectos) de forma automática durante el proyecto; si no, se pierden.
>
> **Ejemplo con story points (libro):**
> - El proyecto tiene 60 historias, que suman **180 puntos** (Scrum Poker, escala exponencial).
> - En el sprint 1 (3 semanas, 4 personas) se entregaron **27 puntos**:
>   - esfuerzo = 3 × 4 = 12 semanas-hombre → **2,25 puntos por semana-hombre**;
>   - tiempo = 3 semanas → **9 puntos por semana**.
> - Estimaciones globales:
>   - **esfuerzo = 180 / 2,25 = 80 semanas-hombre**;
>   - **duración = 180 / 9 = 20 semanas**.
>
> ## Estimación por analogía (con LOC)
> **Etapas:**
> 1. obtener cifras de tamaño y esfuerzo de un proyecto similar;
> 2. expresar el nuevo proyecto en términos relativos al anterior;
> 3. construir la estimación de tamaño;
> 4. construir la estimación de esfuerzo comparando con el anterior;
> 5. verificar que sean de verdad comparables (envergadura, tecnología, equipo).
>
> **Ejemplo (slides y libro):** se estima la nueva app web **Triad** a partir de **AccSellerator**, que tomó **30 meses-hombre**.
> | Subsistema | LOC AccSellerator 1.0 | Factor | LOC estimadas Triad 1.0 |
> |---|---|---|---|
> | Database | 5.000 | 1,4 | 7.000 |
> | User interface | 14.000 | 1,4 | 19.600 |
> | Graphs and reports | 9.000 | 1,7 | 15.300 |
> | Foundation classes | 4.500 | 1,0 | 4.500 |
> | Business rules | 11.000 | 1,5 | 16.500 |
> | **Total** | **43.500** | – | **62.900** |
>
> Triad es 62.900 / 43.500 ≈ **1,45 veces** más grande → esfuerzo ≈ 30 × 1,45 ≈ **44 meses-hombre**.
>
> ## Modelos de la industria (puntos de función)
> ![Slide - modelos de duración y esfuerzo](../adjuntos/Slide%20-%20modelos%20de%20duración%20y%20esfuerzo.png)
>
> - **Duración:** D = Size^0,41 (D en meses, Size en PF)
> - **Esfuerzo:** D = 3 · E^(1/3) → E = (D/3)³ (E en meses-hombre)
>
> Con **S = 100 PF**:
> - D = 100^0,41 ≈ **6,6 meses**;
> - E = (6,6 / 3)³ ≈ **10,6 meses-hombre**.
>
> 10,6 meses-hombre en 6,6 meses ≈ **1,6 personas**, es decir, **dos personas** para el proyecto.

## Preguntas de repaso

1. En el primer sprint (2 semanas, 5 personas) se hicieron 20 puntos. Si el proyecto tiene 200 puntos, estima el esfuerzo y la duración.
> [!question]- Respuesta
> - Esfuerzo del sprint: 2 × 5 = 10 semanas-hombre → 20 / 10 = 2 puntos por semana-hombre → **200 / 2 = 100 semanas-hombre**.
> - Ritmo: 20 / 2 = 10 puntos por semana → **200 / 10 = 20 semanas**.

2. ¿De dónde conviene sacar los datos de productividad?
> [!question]- Respuesta
> Primero del mismo proyecto (sprints anteriores), luego de proyectos similares de la organización y solo al final de datos de la industria.

3. ¿Por qué la regla de tres es solo una aproximación?
> [!question]- Respuesta
> Porque el esfuerzo crece más que linealmente con el tamaño (deseconomía de escala). Para tamaños pequeños el error es aceptable.

4. Con el modelo de PF, ¿qué duración tendría un proyecto de 100 PF y cuántas personas sugiere?
> [!question]- Respuesta
> D = 100^0,41 ≈ 6,6 meses. E = (6,6/3)³ ≈ 10,6 meses-hombre. 10,6 / 6,6 ≈ 1,6 → unas 2 personas.
