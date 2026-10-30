---
ramo: "Testing"
tema: "Gestión del curso"
tags:
  - testing/gestion-del-curso
  - origen/apuntes
prerrequisitos: []
---

# Programa metodología y reglas de evaluación de Testing

## Información general y objetivos del curso

- **Curso**: IIC3745 / IIC2143 — *Testing* (Departamento de Ciencia de la Computación, Pontificia Universidad Católica de Chile).
- **Profesor**: Juan Pablo Sandoval (`juanpablo.sandoval@uc.cl`).
- **Ayudantes coordinadores**: Javiera Azócar (Actividades) y José Tapia (Tareas).
- **Requisito**: IIC2143 (*Ingeniería de Software*).

El objetivo central del curso es formar desarrolladores e ingenieros capaces de asegurar la calidad del software de manera sistemática y automatizada: desde pruebas unitarias, dobles de prueba, cobertura e instrumentación dinámica, hasta generación automática mediante fuzzing (aleatorio, mutacional, basado en búsqueda, simbólico y concólico), análisis de mutación, diseño de caja negra, análisis estático y transformación de AST, *taint analysis* y *profiling* de rendimiento.

---

## Sistema de evaluación y fórmulas de calificación

La calificación del curso se divide en tres componentes principales: **Nota de Cátedra ($NC$, $60\%$)**, **Nota de Tareas ($NT$, $30\%$)** y **Nota de Actividades ($NA$, $10\%$)**.

$$\text{NF} = 0.60 \cdot \text{NC} + 0.30 \cdot \text{NT} + 0.10 \cdot \text{NA}$$

### 1. Nota de Actividades ($NA$ — $10\%$)
Promedio simple de **5 actividades individuales** prácticas destinadas a aplicar directamente las técnicas vistas en clases (cobertura, mutación, transformación AST, ejecución simbólica, etc.):

$$\text{NA} = \frac{A_1 + A_2 + A_3 + A_4 + A_5}{5}$$

### 2. Nota de Tareas ($NT$ — $30\%$)
Promedio simple de **3 tareas en parejas** ($10\%$ cada una), inspiradas en desafíos reales de ingeniería de software asistida por herramientas modernas:
1. **Tarea 1**: Generación automática de pruebas unitarias utilizando Modelos de Lenguaje (*LLMs*) e ingeniería de prompts para lograr que los tests compilen, pasen y alcancen alta cobertura.
2. **Tarea 2**: Localización de fallas (*Fault Localization*) y reparación sobre suites con tests que fallan utilizando un LLM con presupuesto acotado hasta hacer pasar la suite.
3. **Tarea 3**: Diseño y ejecución de pruebas manuales y automatizadas sobre una API real y análisis crítico de herramientas.

$$\text{NT} = \frac{T_1 + T_2 + T_3}{3}$$

### 3. Nota de Cátedra ($NC$ — $60\%$) y condición de eximición
Se evalúa mediante dos interrogaciones escritas individuales ($I_1$ e $I_2$) y un examen acumulativo ($E$). Las décimas de participación obtenidas en ejercicios de clase se suman directamente a la interrogación correspondiente ($I_1$ o $I_2$) y cuentan tanto para aprobación como para eximición:
- **Con eximición del examen** (si el promedio $\frac{I_1 + I_2}{2} \ge 5.5$ y además $I_1 \ge 3.95$ e $I_2 \ge 3.95$):
  $$\text{NC} = \frac{I_1 + I_2}{2}$$
- **Sin eximición** (rindiendo el examen $E$):
  $$\text{NC} = 0.60 \cdot \left(\frac{I_1 + I_2}{2}\right) + 0.40 \cdot E = 0.30 \cdot I_1 + 0.30 \cdot I_2 + 0.40 \cdot E$$

---

## Condiciones de aprobación, plazos e integridad académica

- **Aprobación por separado**: para aprobar el curso se exige simultáneamente $\text{NC} \ge 3.95$ y $\text{NT} \ge 3.95$ (no es requisito aprobar $NA$ por separado). Si no se cumple, $\text{NF} = \min(3.9, \text{NF})$.
- **Política de atrasos**:
  - *Actividades*: hasta 2 días de retraso con descuento de $1\text{ punto}$ el primer día y $2\text{ puntos}$ el segundo día.
  - *Tareas*: cada estudiante dispone de **1 cupón** en el semestre que permite entregar una tarea con hasta 2 días de retraso sin penalización; sin cupón, el retraso se califica con nota mínima.
- **Uso de IA e Integridad Académica**: se permite usar herramientas de IA en actividades y tareas siempre que el estudiante comprenda y pueda explicar cada línea de su entrega; las interrogaciones y el examen se rinden de forma individual sin apoyo de IA.

---

## Bibliografía de referencia

1. Andreas Zeller, Rahul Gopinath, Marcel Böhme, Gordon Fraser, Christian Holler (2024). *The Fuzzing Book: Tools and Techniques for Generating Software Tests*. CISPA Helmholtz Center for Information Security.
2. Dorothy Graham, Erik van Veenendaal, Isabel Evans, Rex Black (2018). *Foundations of Software Testing: ISTQB Certification* (4th ed.). Cengage Learning.
3. Paul Ammann & Jeff Offutt (2016). *Introduction to Software Testing* (2nd ed.). Cambridge University Press.
4. Stéphane Ducasse, Guillermo Polito, Juan Pablo Sandoval (2020). *Testing in Pharo*.

---

---

## Ejemplo práctico: calcular la nota final en tres escenarios

Fórmulas: $\text{NF} = 0.6\,\text{NC} + 0.3\,\text{NT} + 0.1\,\text{NA}$, con $\text{NC}$ dependiendo de la eximición.

**Escenario A: eximición del examen.** $I_1 = 5.8$, $I_2 = 5.6$, $\text{NT} = 5.0$, $\text{NA} = 6.0$.

* Promedio de interrogaciones: $\frac{5.8 + 5.6}{2} = 5.7 \ge 5.5$ y ambas $\ge 3.95$ → **eximido**, $\text{NC} = 5.7$.
* $\text{NF} = 0.6 \cdot 5.7 + 0.3 \cdot 5.0 + 0.1 \cdot 6.0 = 3.42 + 1.50 + 0.60 = \mathbf{5.52}$.

**Escenario B: no se exime y rinde el examen.** $I_1 = 6.5$, $I_2 = 4.0$, $E = 5.0$, $\text{NT} = 4.5$, $\text{NA} = 5.0$.

* Promedio: $\frac{6.5 + 4.0}{2} = 5.25 < 5.5$ → **no se exime**.
* $\text{NC} = 0.3 \cdot 6.5 + 0.3 \cdot 4.0 + 0.4 \cdot 5.0 = 1.95 + 1.20 + 2.00 = 5.15$.
* $\text{NF} = 0.6 \cdot 5.15 + 0.3 \cdot 4.5 + 0.1 \cdot 5.0 = 3.09 + 1.35 + 0.50 = \mathbf{4.94}$ (aprueba: $\text{NC} \ge 3.95$ y $\text{NT} \ge 3.95$).

**Escenario C: el promedio alcanza, pero una interrogación no.** $I_1 = 3.9$, $I_2 = 7.1$, $E = 4.0$.

* Promedio: $\frac{3.9 + 7.1}{2} = 5.5$ cumple el umbral, pero $I_1 = 3.9 < 3.95$ → **no se exime**.
* $\text{NC} = 0.3 \cdot 3.9 + 0.3 \cdot 7.1 + 0.4 \cdot 4.0 = 1.17 + 2.13 + 1.60 = \mathbf{4.90}$.

La condición de eximición exige **las tres cosas a la vez** (promedio y cada interrogación sobre el mínimo), y por eso un promedio alto no basta si una nota queda bajo $3.95$.

---

## Preguntas de repaso

> [!question]- ¿Qué requisitos deben cumplirse simultáneamente para eximirse del examen final del curso?
> Obtener un promedio entre ambas interrogaciones (incluyendo las décimas de participación sumadas a cada una) mayor o igual a $5.5$, y además tener una nota mayor o igual a $3.95$ en cada interrogación por separado ($I_1 \ge 3.95$ e $I_2 \ge 3.95$).

> [!question]- Si un estudiante obtiene promedio $6.0$ en Actividades ($NA$), $5.2$ en Tareas ($NT$), pero su Nota de Cátedra ($NC$) tras el examen es $3.8$, ¿cuál es su situación final en el curso?
> Reprueba el curso con nota final ajustada a $\min(3.9, \text{NF})$, porque para aprobar se exige aprobar por separado tanto la Nota de Cátedra ($\text{NC} \ge 3.95$) como la Nota de Tareas ($\text{NT} \ge 3.95$).

> [!question]- ¿Cómo funcionan las reglas de entrega tardía para las Actividades en comparación con las Tareas?
> En las Actividades se permiten hasta 2 días de atraso con descuento directo de 1 punto por el primer día y 2 puntos por el segundo; en las Tareas no hay descuento gradual, sino que cada estudiante cuenta con un único cupón semestral para entregar una tarea hasta 2 días tarde sin penalización.

> [!question]- Un estudiante tiene $\text{NC} = 5.0$, $\text{NT} = 3.8$ y $\text{NA} = 7.0$. ¿Aprueba? ¿Cuál sería su promedio ponderado?
> No aprueba: la nota de tareas está bajo $3.95$ y se exige aprobar $\text{NC}$ y $\text{NT}$ por separado, sin que $\text{NA}$ lo compense. El promedio ponderado sería $0.6 \cdot 5.0 + 0.3 \cdot 3.8 + 0.1 \cdot 7.0 = 3.0 + 1.14 + 0.7 = 4.84$, pero la regla de aprobación por separado prima sobre ese número.

> [!question]- Un equipo entrega la Tarea 2 con $1$ día de atraso y no ha usado su cupón. ¿Qué ocurre?
> Puede usar su cupón (uno por semestre), que permite entregar una tarea con hasta $2$ días de atraso sin penalización. Si ya lo hubiera usado, se aplicaría la política de atrasos sin cupón.
