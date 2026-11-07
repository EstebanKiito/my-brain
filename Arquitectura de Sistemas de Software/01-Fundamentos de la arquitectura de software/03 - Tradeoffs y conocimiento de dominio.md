---
ramo: "Arquitectura de Sistemas de Software"
tema: "Fundamentos de la arquitectura de software"
tags:
  - arquisis/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[02 - El rol del arquitecto]]"
---

# Tradeoffs y conocimiento de dominio

Dos ideas atraviesan todo el curso y aparecen en todas las preguntas de diseño. La primera es que **todo es un tradeoff**: no existe la opción perfecta, solo la más adecuada al caso, y en las pautas se pide explícitamente identificar tradeoffs. La segunda es que **sin conocimiento del dominio no se puede decidir bien**: saber de tecnologías no basta si no se entiende el negocio.

## Los facts clave de la arquitectura

| Frase | Qué significa |
|---|---|
| *"Everything in software architecture is a trade-off"* | Cada decisión compra algo y cobra otra cosa; muchas decisiones terminan siendo subóptimas en algún aspecto |
| *"Why is more important than how"* | No se toman decisiones solo porque son más fáciles. Si el porqué es convincente, los medios para hacerlo se encuentran |
| *"Architecture is the stuff you can't Google"* (Mark Richards) | Los problemas reales de arquitectura dependen del contexto y no tienen respuesta lista en internet |
| **Ley de Conway** | "Toda organización que diseña un sistema producirá un diseño cuya estructura es una copia de la estructura de comunicación de la organización" |

La **ley de Conway** explica, por ejemplo, por qué una empresa con un solo equipo tiende a construir un monolito, y una con muchos equipos autónomos, servicios separados. La arquitectura y la organización se influyen mutuamente: **todo software se construye en equipo**.

## Dónde pone el ojo el arquitecto

- **Pensar en tradeoffs**: ventajas y desventajas de cada opción.
- **Mirar más allá de las clases y las líneas de código.**
- **Encontrar lo mejor para el caso**, no necesariamente lo perfecto.
- **Agregar y desagregar el sistema**: saber cuándo juntar y cuándo separar.
- **Vender opciones.**

> [!example]- Ejemplo de tradeoff: caché
> Una caché **compra latencia**: la segunda carga de la página es mucho más rápida. Pero **cobra frescura y consistencia**: si la página cambió, el navegador puede seguir mostrando la versión vieja sin preguntar. El escenario del negocio dice si ese precio es aceptable: para un catálogo de productos sí, para el saldo de una cuenta no.

## Conocimiento de dominio

> [!tip] Conocimiento de dominio
> **Capacidad de hablar y reconocer problemas de forma general en un campo de conocimiento específico.** Es un requisito para lograr un diseño exitoso. No tiene que ser extremadamente profundo, y no implica que nadie vaya a explicar nada, pero sin él no se puede conversar con el negocio.

No queremos saber solo de tecnologías (conocimiento técnico): también necesitamos el campo del negocio. En otros ramos se pide "implementar algo de tal forma usando tal tecnología", y eso deja muy pocas decisiones. En la industria, el contexto donde funcionará la aplicación define qué priorizar.

**Ejemplo del hedge fund:** se pide desarrollar un sistema de manejo de cartera capaz de administrar y ejercer opciones, y de mostrar a los clientes sus carteras de acciones. Antes de diseñar hay que saber:
- ¿Qué es un *stock*? En finanzas son acciones de una empresa; en un inventario, unidades disponibles. La misma palabra significa cosas distintas según el área.
- ¿Qué significa una *call*? ¿Cómo se ejercen las opciones? ¿Qué es un futuro? ¿Qué es un contrato aleatorio?

**Conocer todo esto es clave para comunicarse con todas las áreas y ofrecer un diseño apropiado.** Un sistema de inventario, por ejemplo, no es "un CRUD": necesita control, logística, la parte comercial y la de inventario, cada una con sus reglas. La arquitectura necesita reflejarlas.

> [!warning] Conocimiento de dominio no es conocimiento técnico
> En un sistema de reserva de salas:
> - "Una sala no puede reservarse dos veces al mismo tiempo" es **dominio**: una regla del negocio.
> - "Qué departamentos pueden reservar salas VIP" es **dominio**: una política de la organización.
> - "Los lenguajes y frameworks que conozco" es **conocimiento técnico**, no de dominio.

## Preguntas de repaso

> [!question]- Explique "why is more important than how" con un ejemplo.
> Elegir microservicios "porque es lo moderno" es un cómo sin porqué. Si el porqué es que tres equipos necesitan desplegar a ritmos distintos y una parte recibe 100 veces más carga, la decisión está justificada y los medios para implementarla se encuentran.

> [!question]- ¿Qué dice la ley de Conway y qué implicancia tiene para el diseño?
> Que la estructura del sistema tiende a copiar la estructura de comunicación de la organización que lo construye. Al diseñar hay que considerar cómo están organizados los equipos: fronteras de sistema que no calzan con los equipos generan fricción constante.

> [!question]- Alternativas: en un sistema de reserva de salas, ¿qué es conocimiento de dominio? I. "Una sala no puede reservarse dos veces al mismo tiempo" · II. Lenguajes y frameworks que conozco · III. Qué departamentos pueden reservar salas VIP. a) Solo II · b) II y III · c) I y III · d) Todas
> c) I y III. Ambas son reglas y políticas del negocio. II es conocimiento técnico.

> [!question]- ¿Por qué el conocimiento de dominio es un requisito y no un "plus" para el arquitecto?
> Porque las prioridades del sistema (qué atributo importa más, qué datos deben ser consistentes, qué conceptos significan qué) salen del negocio. Sin entender el dominio, el diseño puede ser técnicamente correcto y aun así resolver el problema equivocado.

> [!question]- Dé un ejemplo de un concepto que cambia de significado según el área del negocio.
> "Stock": acciones de una empresa en finanzas, o unidades disponibles en inventario. "Producto" es otro: para el catálogo tiene imagen y precio, para envíos tamaño y peso, y para facturación precio e IVA.

> [!question]- ¿Qué significa "encontrar lo mejor para el caso, no lo perfecto"?
> Que no existe una arquitectura óptima en todo: cada opción gana en algunos atributos y pierde en otros. El arquitecto elige la que mejor sirve a las prioridades del caso concreto, aceptando conscientemente lo que sacrifica.

> [!question]- V o F: "Architecture is the stuff you can't Google" significa que no hay que investigar soluciones existentes.
> Falso. Significa que los problemas arquitectónicos dependen de un contexto particular (negocio, equipo, restricciones) y no tienen una respuesta única en internet. Investigar estilos y patrones probados sigue siendo parte del trabajo.
