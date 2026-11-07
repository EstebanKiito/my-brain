---
ramo: "Arquitectura de Sistemas de Software"
tema: "Estilos jerárquicos y de capas"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[03 - Decisiones relevantes y tácticas arquitectónicas]]"
  - "[[01 - Qué es un patrón de diseño]]"
---

# Estilos patrones y el monolito

En cada prueba se pide "indique los estilos o patrones arquitectónicos que va a emplear y qué aspecto del problema ataca cada uno". Para responder bien hay que saber qué es un estilo, en qué se diferencia de un patrón y cuál es el punto de partida contra el que se comparan todos: el **monolito**.

## Estilo arquitectónico

> [!tip] Estilo arquitectónico (Taylor, Medvidović y Dashofy, 2009)
> **Colección nombrada de decisiones de diseño arquitectónico** que:
> - aplican a un **contexto de desarrollo** dado;
> - **restringen** las decisiones de diseño específicas de un sistema dentro de ese contexto;
> - **promueven ciertos atributos de calidad**.
> Gobierna el código, los componentes, los requisitos y las decisiones.

No es lo mismo decir que un sistema es un monolito, que es cliente-servidor, que es en capas o que es pub/sub con un broker: cada nombre ya dice mucho de cómo se ve. Además, **no todo el sistema tiene que seguir un solo estilo**: partes distintas pueden usar estilos distintos. Hay estilos que priorizan el desarrollo veloz y otros la escalabilidad.

## Patrón arquitectónico

> [!tip] Patrón arquitectónico
> **Colección nombrada de decisiones de diseño** que aplica a un **problema de diseño recurrente** y se **parametriza** según el contexto en que aparece.

**Ejemplo:** MVC (modelo, vista, controlador) es un patrón que ayuda a organizar un monolito. Por eso un monolito en Rails es más fácil de trabajar. Ojo: un **patrón de arquitectura** no es lo mismo que un **patrón de diseño** (Strategy, Observer), que opera a nivel de clases.

| | Estilo | Patrón |
|---|---|---|
| **Alcance** | Un **contexto de desarrollo** | Un **problema de diseño** específico |
| **Abstracción** | Requiere **interpretación humana** | **Fragmentos arquitectónicos parametrizados** |
| **Relación** | Un sistema que sigue un estilo puede usar varios patrones | Un patrón puede aplicarse en sistemas de varios estilos |

![Patrones de diseño, estilos, patrones arquitectónicos y DSSA según alcance y conocimiento de dominio](adjuntos/Estilos%20y%20patrones%20según%20alcance%20y%20conocimiento%20de%20dominio.png)

> [!example]- Transcripción de la imagen
> - Eje horizontal, **alcance**: programación (lenguaje), aplicación (componentes y conectores) y sistema.
> - Eje vertical, **conocimiento del dominio de la aplicación**: de superficial a profundo.
> - Abajo a la izquierda, **patrones de diseño**: alcance de lenguaje y poco conocimiento de dominio.
> - Al centro, **estilos arquitectónicos**: alcance de aplicación o sistema y conocimiento moderado.
> - Más arriba, **patrones arquitectónicos**, y arriba a la derecha, **arquitecturas específicas de dominio (DSSA)**: alcance amplio y mucho conocimiento del dominio.

## Por qué usar estilos y patrones

- **Reuso de diseños probados:** soluciones bien entendidas aplicadas a problemas nuevos, que producen soluciones más maduras.
- **Lenguaje compartido:** decir "cliente-servidor" ya explica cómo es el sistema.
- **DRY:** se apoyan en convenciones, sin reinventar la rueda.
- **Interoperabilidad:** la estandarización hace los sistemas más comprensibles y fáciles de componer.
- **Análisis específico al estilo:** restringir el espacio de diseño hace más fácil justificar decisiones.
- **Visualizaciones:** cada estilo tiene figuras propias que calzan con el modelo mental "ingenieril".

**Lo que se quiere evitar:**
- **Big ball of mud:** sin estilo ni plan, todo conectado con todo, sin querer una sola quanta gigante. Si algo se cae, muere todo.
- **"Vibes on prod":** decisiones sin fundamento, como desplegar lo que "se siente bien" sin justificar.

## El monolito: la primera arquitectura

![Croquis de un monolito y de main y subrutinas](adjuntos/Monolito%20frente%20a%20main%20y%20subrutinas.png)

> [!example]- Transcripción de la imagen
> - Izquierda, **Monolito**: un único bloque con una interfaz provista arriba y una sola base de datos abajo.
> - Derecha, **Main-Subrutina**: un componente **Main** que se conecta mediante interfaces requeridas con **SR1**, **SR2** y **SR3**.

- Sistema contenido en **una sola quanta**: un bloque de software y una base de datos (tener otra base sería innecesario, porque el mismo sistema es el que se conecta).
- **Alta cohesión** y **acoplamiento estático**: todo está entrelazado en el mismo código y comparte memoria. Aun así, valora la modularidad.
- **Ventaja: la velocidad de desarrollo.** Es ideal para un MVP.
- **Problemas al crecer:** el build se vuelve más pesado porque todo está concentrado, impide escalar partes por separado y aparecen problemas de performance al añadir más y más código. Por eso Rails adoptó MVC, para ponerle orden.
- **No es inherentemente malo** (es debatible): sus implicancias dependen de cómo se use.

**Estilos comunes del curso** (Taylor): influenciados por el lenguaje (main y subrutinas, orientado a objetos), en capas (máquinas virtuales, cliente-servidor), microkernel, flujo de datos (por lotes, pipe and filter), memoria compartida (pizarra, basado en reglas), intérprete (intérprete, código móvil), invocación implícita (eventos, pub/sub) y P2P.

## Preguntas de repaso

> [!question]- Defina estilo arquitectónico según Taylor y nombre qué gobierna.
> Es una colección nombrada de decisiones de diseño que aplican a un contexto de desarrollo, restringen las decisiones específicas del sistema y promueven ciertos atributos de calidad. Gobierna el código, los componentes, los requisitos y las decisiones.

> [!question]- Diferencie estilo y patrón arquitectónico en alcance y abstracción.
> El estilo aplica a un contexto de desarrollo completo y requiere interpretación humana. El patrón resuelve un problema de diseño recurrente y es un fragmento parametrizado. Un sistema de un estilo puede usar varios patrones, y un patrón puede aparecer en sistemas de distintos estilos.

> [!question]- ¿MVC es un estilo o un patrón? ¿Y un patrón de diseño?
> Es un patrón arquitectónico: resuelve el problema recurrente de separar datos, presentación y control, por ejemplo dentro de un monolito en Rails. No es un patrón de diseño como Strategy u Observer, que operan a nivel de clases.

> [!question]- ¿Qué es el big ball of mud y por qué los estilos ayudan a evitarlo?
> Es un sistema sin estructura clara, todo conectado con todo, que termina siendo una sola quanta frágil. Los estilos imponen restricciones (quién se comunica con quién y cómo) que mantienen el orden y la cohesión.

> [!question]- ¿Cuáles son la ventaja principal y los problemas de un monolito al crecer?
> Ventaja: la velocidad de desarrollo, ideal para un MVP. Problemas: build cada vez más pesado, imposibilidad de escalar partes por separado, problemas de performance al agregar código y una sola quanta (si falla, falla todo).

> [!question]- Nombre cuatro ventajas de usar estilos y patrones.
> Reuso de diseños probados, lenguaje compartido que mejora la comunicación, mejor interoperabilidad por estandarización y un espacio de diseño acotado que facilita justificar las decisiones. También DRY y visualizaciones típicas.

> [!question]- V o F: "Un sistema debe seguir un único estilo arquitectónico".
> Falso. Partes distintas del sistema pueden seguir estilos distintos: un backend en capas, pub/sub para las notificaciones y pipe and filter para procesar datos. Por eso en las pruebas se pide indicar qué responsabilidad ataca cada estilo.
