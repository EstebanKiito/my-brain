---
ramo: "Arquitectura de Sistemas de Software"
tema: "Fundamentos de la arquitectura de software"
tags:
  - arquisis/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es la arquitectura de software]]"
---

# El rol del arquitecto

Toda arquitectura tiene detrás a alguien que la decide y responde por ella: el **ente arquitectónico**. Puede ser una persona, un equipo pequeño o una responsabilidad repartida, pero siempre tiene que haber un responsable. Esta nota describe qué hace, qué debe saber y cómo debe comportarse. Aunque uno no sea arquitecto mañana, esas habilidades (análisis, decisiones, modelación) son las que más se valoran hoy.

## El arquitecto

- Es el **elemento central** y el **responsable directo**.
- Es **multifacético, con enfoque técnico**.
- Puede estar apoyado por un sub-equipo, normalmente de implementadores.

> [!tip] "An architect sells options" (*The Architect Elevator*)
> El arquitecto no impone una solución: **presenta opciones** con sus costos y beneficios, y ayuda a elegir. Vender opciones también significa diseñar para dejar decisiones abiertas cuando todavía no hay información suficiente.

### Clásico frente a distribuido

| Concepción clásica | Ente arquitectónico distribuido |
|---|---|
| Las mejores arquitecturas son producto de **"una sola mente"** o de un equipo pequeño y estructurado (Rechtin, 1991) | Aparece cuando hay **horizontalidad**, equipos vagamente definidos o pequeños y multifacéticos, y baja el costo de implementar |
| Todo proyecto debe tener **exactamente un arquitecto identificable**; en proyectos grandes, apoyado por un arquitecto por sub-equipo (Booch, 1996) | La responsabilidad arquitectónica **se reparte**: ojo con la *accountability* (quién responde) |
| Hoy, la "mente" queda impresa en la **documentación** y en hechos centralizados | **Demanda mejores procesos** y puede convertirse en un **rol móvil** |

## Qué hace

- Toma **decisiones de grano grueso**: "decisiones arquitectónicamente significativas, que afectan la estructura, los requisitos no funcionales, las dependencias, las interfaces o las técnicas de construcción" (Michael Nygard, *Release It!*).
- **Liga los requerimientos con propuestas arquitectónicas.**
- **Piensa en tradeoffs.**
- Mantiene a **todos los involucrados en su línea de visión**.
- **También programa: no vive en una torre de marfil.** Tiene que saber cómo se programa y se maneja el sistema.

## Qué debe saber

- Conoce una **variedad de sistemas y posibilidades**.
- Tiene **conocimiento de dominio**.
- Es capaz de **modelar y amoldar soluciones** para que escalen y evolucionen.
- **Entiende el problema subyacente** que se quiere resolver.
- Está al día con el mundo tech y **no tiene remordimientos por cambiar a un paradigma superior**, siempre que esté bien justificado.
- **Demuestra su expertise** con pruebas de concepto, y tiene una o más áreas de conocimiento profundo.

![Pirámides del saber técnico de un desarrollador y de un arquitecto](adjuntos/Saber%20técnico%20de%20un%20desarrollador%20frente%20a%20un%20arquitecto.png)

> [!example]- Transcripción de la imagen
> - Dos pirámides de tres niveles: arriba *stuff you know* (lo que sé), al medio *stuff you know you don't know* (lo que sé que no sé) y abajo *stuff you don't know you don't know* (lo que no sé que no sé). Sobre ambas se marca el ancho técnico (*technical breadth*).
> - **Developer:** el nivel superior es grande y con mucha *technical depth* (profundidad).
> - **Arquitecto:** el nivel superior es pequeño, con varias puntas delgadas de profundidad, y el nivel del medio es más ancho.
> - Leyenda: "Queremos expandir lo que nosotros sabemos que no sabemos" (Mark Richards).

El desarrollador profundiza en pocas tecnologías. El arquitecto necesita **amplitud**: no dominar todo, pero saber que existe, para poder considerarlo como opción.

## Cómo debe actuar

![El arquitecto debe hablar: conversar, coordinar y explicar](adjuntos/El%20arquitecto%20debe%20hablar.png)

> [!example]- Transcripción de la imagen
> "El arquitecto debe hablar…": conversa con todas las partes (escuchar, negociar, explicar, convencer, vender), coordina requisitos y capacidades, y explica problemas con calma y respeto (por qué pasa esto o aquello).

| Debe… | Qué implica |
|---|---|
| **Decidir a largo plazo** | Conoce el costo de cada decisión, no solo el monetario; observa a todos los stakeholders, propone y decide; entiende el negocio y mira a la competencia |
| **Hablar** | Escucha, negocia, explica, **convence y vende**; coordina requisitos con capacidades |
| **Liderar** | Tiene un pie técnico que lo respalda frente a desarrolladores y otros líderes, y un pie de negocio frente a presupuestos, product owners y usuarios. **No impone: convence y guía.** Lidia con la política empresarial |
| **Estimar** | Observa costos: software ya hecho (COTS) frente a desarrollo propio, integrabilidad, FinOps. **No siempre se puede usar todo lo que se desea** |

El arquitecto debe ser maduro y **debe convencer**, y para eso necesita un nivel alto de conocimiento. También **debe saber de dinero**, porque hay decisiones que cuestan.

## Preguntas de repaso

> [!question]- ¿Qué significa que "un arquitecto vende opciones"?
> Que su rol no es imponer una solución única, sino presentar alternativas con sus costos, beneficios y riesgos para que se tome una decisión informada, y diseñar de modo que algunas decisiones puedan postergarse o cambiarse.

> [!question]- Compare la concepción clásica del arquitecto con el ente arquitectónico distribuido.
> La clásica plantea una sola mente o un arquitecto identificable responsable de todo. La distribuida reparte la responsabilidad entre equipos horizontales y multifacéticos: es más ágil, pero exige mejores procesos y cuidar quién responde por cada decisión.

> [!question]- ¿Por qué se dice que el arquitecto "no vive en una torre de marfil"?
> Porque también programa y conoce el sistema por dentro. Si no, sus decisiones se desconectan de la realidad técnica y pierde credibilidad frente al equipo que implementa.

> [!question]- Según la figura del saber técnico, ¿en qué se diferencia el conocimiento de un arquitecto del de un desarrollador?
> El desarrollador tiene mucha profundidad en pocas tecnologías. El arquitecto prioriza la amplitud: ampliar lo que sabe que no sabe, para conocer más opciones posibles, aunque no domine cada una en detalle.

> [!question]- ¿Por qué el arquitecto debe saber de dinero?
> Porque las decisiones tienen costos de desarrollo, de operación (OPEX), de licencias y de integración. Debe estimar si conviene construir o comprar (COTS) y reconocer que no siempre se puede usar todo lo que se desea.

> [!question]- Nombre tres cosas que hace el arquitecto según Nygard y el curso.
> Toma decisiones de grano grueso que afectan la estructura, los requisitos no funcionales, las dependencias o las interfaces. Liga requerimientos con propuestas arquitectónicas. Evalúa tradeoffs manteniendo a todos los involucrados en su línea de visión.

> [!question]- V o F: "Un buen arquitecto impone sus decisiones técnicas al equipo para mantener la coherencia".
> Falso. El arquitecto convence y guía: justifica sus decisiones con un respaldo técnico y de negocio, de modo que el equipo las siga por convicción y no por imposición.
