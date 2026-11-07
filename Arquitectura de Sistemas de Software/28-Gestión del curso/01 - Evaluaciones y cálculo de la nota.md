---
ramo: "Arquitectura de Sistemas de Software"
tema: "Gestión del curso"
tags:
  - arquisis/gestion
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es la arquitectura de software]]"
---

# Evaluaciones y cálculo de la nota

Arquisis (IIC2173) evalúa con tres tipos de instancias, cada una con un foco distinto: **actividades** (pensar rápido y defender soluciones), **pruebas** (justificar decisiones) y **proyecto** (descubrir tecnologías e investigar). Esta nota resume los pesos, las fechas del semestre 2026-2 y cómo se calcula la nota final, con ejemplos. Los valores pueden ajustarse en el programa oficial del curso.

## Plan del curso

![Plan del curso entre proyecto y cátedra](adjuntos/Plan%20del%20curso%20entre%20proyecto%20y%20cátedra.png)

> [!example]- Transcripción de la imagen
> - **Proyecto:** *Lenguaje común* (definiciones base, conceptos esenciales, NFR) → *Estrategias* (diagramación, estilos, patrones, interfaces) → *Aplicaciones* (performance, seguridad, DevOps, patrones avanzados).
> - **Cátedra:** *Cloud computing* → *Modelación* → *Software COTS e integrabilidad*.

Al principio suele no entenderse el hilo, pero después se va dirigiendo. El curso **tiende a ser más demandante que complicado**: no debería ser difícil, solo toma tiempo.

**Principios del curso:** exploración complementaria autónoma, flexibilidad evaluativa sin *free-riders* (no se acepta no hacer nada en los trabajos grupales) y acompañamiento en el aprendizaje.

## Actividades (30% de la nota final)

| Instancia | Tipo | Peso | Regla |
|---|---|---|---|
| **Quiz** (los martes, de alternativas) | Individual | 33% | Se elimina el 30% de los quizzes |
| **Modelaciones** (los jueves, en clase, 15-20 min) | Grupal ad hoc | 33% | Se elimina la peor |
| **Debate** | Grupal ad hoc | 34% | Uno por grupo |

En una modelación se forman grupos que responden preguntas y arman un diagrama. La primera es formativa y entrega décimas.

## Pruebas (40%)

- **2 interrogaciones + examen**, estrictamente individuales.
- **I1:** del 30/09/26 al 03/10/26, **online**, con 72 horas para realizarla.
- **I2:** **11/11/26**, **presencial**. Se permite un **torpedo de 3 hojas (6 planas)**.
- **Examen:** **03/12/26**, presencial y **eximible**. **Elimina la peor nota.**

$$NIE = \frac{I1 + I2 + 2 \cdot Ex - \min(I1, I2, Ex)}{3}$$

El examen pesa doble, pero se resta la peor de las tres notas, así que en la práctica **reemplaza a la peor interrogación** si es mejor que ella.

## Proyecto (30%)

| Entrega | Tipo | Peso |
|---|---|---|
| E0 | Individual | 20% |
| E1 | Grupal | 25% |
| E2 | Grupal | 25% |
| E3 | Grupal | 30% |

- Las entregas son **acumulativas** y **no hay instancias recuperativas**.
- Las grupales están sujetas a **evaluación de pares**: $N_i = 1 + N_{ig} \cdot (F_i - 1)$, donde $N_{ig}$ es el factor de pares del integrante y $F_i$ la nota del grupo.

## Nota final y aprobación

$$NF = 0{,}3 \cdot NP + 0{,}3 \cdot NA + 0{,}4 \cdot NIE$$

**Requisitos (todos):** $NIE \geq 3{,}95$; examen $\geq 3{,}00$ (si se rinde); $NA \geq 3{,}95$; $NP \geq 4{,}00$; promedio de evaluación de pares $\geq 0{,}7$; $NF \geq 3{,}95$; y responder un formulario de conocimientos. El curso adscribe a la política de integridad académica del DCC y al código de honor.

> [!example]- Ejemplos de cálculo
> **Ejemplo 1:** I1 = 5,0, I2 = 4,5, Ex = 5,5.
> $NIE = (5{,}0 + 4{,}5 + 11{,}0 - 4{,}5)/3 = 16{,}0/3 \approx 5{,}33$.
> **Ejemplo 2:** I1 = 3,5, I2 = 5,0, Ex = 5,5. Se descarta el 3,5:
> $NIE = (3{,}5 + 5{,}0 + 11{,}0 - 3{,}5)/3 \approx 5{,}33$. El examen "borró" la mala I1.
> **Nota final:** NP = 5,5, NA = 6,0, NIE = 5,33 → $NF = 1{,}65 + 1{,}80 + 2{,}13 \approx 5{,}58$.
> **Factor de pares:** grupo con F = 6,0 y factor 0,9 → $N_i = 1 + 0{,}9 \cdot 5{,}0 = 5{,}5$.

> [!warning] Las notas de corte se cumplen por separado
> Aunque la NF supere 3,95, se reprueba si alguna componente queda bajo su mínimo: por ejemplo, un proyecto con NP = 3,9 o un promedio de pares bajo 0,7.

## Preguntas de repaso

> [!question]- ¿Qué foco tiene cada tipo de evaluación?
> Las actividades evalúan pensar rápido y defender soluciones. Las pruebas evalúan justificar decisiones. El proyecto evalúa descubrir tecnologías nuevas y la capacidad de investigar.

> [!question]- Calcule la NIE con I1 = 4,0, I2 = 6,0 y Ex = 5,0.
> $(4{,}0 + 6{,}0 + 10{,}0 - 4{,}0)/3 = 16{,}0/3 \approx 5{,}33$. Se descarta la I1, la peor.

> [!question]- ¿Por qué se dice que el examen "elimina la peor nota"?
> Porque cuenta doble y luego se resta la mínima entre I1, I2 y examen. Si la peor es una interrogación, el examen la reemplaza. Si la peor es el examen, se resta una de sus dos copias y queda el promedio simple de las tres.

> [!question]- ¿Cuánto pesa cada componente en la nota final?
> 30% el proyecto, 30% las actividades y 40% las pruebas (NIE).

> [!question]- ¿Qué reglas de eliminación tienen los quizzes y las modelaciones?
> Se elimina el 30% de los quizzes (los peores) y la peor modelación.

> [!question]- V o F: "Con NF = 5,0 se aprueba siempre".
> Falso. Además hay que cumplir cada mínimo por separado: NIE ≥ 3,95, NA ≥ 3,95, NP ≥ 4,00, examen ≥ 3,00 si se rinde y promedio de pares ≥ 0,7, y responder el formulario de conocimientos.
