---
ramo: "Arquitectura de Sistemas de Software"
tema: "Componentes quanta y documentación"
tags:
  - arquisis/fundamentos
  - arquisis/documentacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Componentes y quanta arquitectónica]]"
---

# Documentación vistas y ADR

Parte del rol de comunicador del arquitecto es **documentar**: no mostrar solo código, sino las **decisiones** y el **porqué** de cada una. Hoy la documentación vale más que nunca: los agentes de IA la necesitan para trabajar, evita cargar contexto innecesario o llamar a expertos innecesarios, y hace posible que nuevos ingenieros entren a sistemas cada vez más complejos.

## Niveles de documentación

- **Código**: nombres claros y estructura legible.
- **Comentarios**: llenar el código de comentarios es mala documentación.
- **Informes.**
- **Vistas**: representaciones gráficas.
- **ADRs**: registros de decisiones.

Lo ideal es tener una **vista gráfica**: alguien que la ve entiende el sistema mucho más rápido que leyendo el código.

## Vistas

> [!tip] Vista
> **Colección de decisiones y hechos sobre un sistema, representados en un formato gráfico.** **Ninguna vista posee toda la verdad**: se requieren varios tipos.

![Vistas: un diagrama de componentes y un diagrama de flujo de un mismo sistema](adjuntos/Vistas%20como%20colecciones%20de%20decisiones.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, el título **Vistas** y la definición: colecciones de decisiones y hechos sobre un sistema en formato gráfico; ninguna vista posee toda la verdad, se requieren varios tipos.
> - A la derecha, dos diagramas del mismo sistema: arriba, uno de **componentes** (PostgreSQL, ActiveRecord, controladores, un router); abajo, uno de **flujo** con tareas en paralelo (OSINT, análisis de documentación, footprinting) entre un inicio y un fin.

Es como en medicina, donde un cráneo se estudia con radiografía, escáner y resonancia: cada examen muestra algo que los otros no. Un diagrama de componentes no muestra el orden de las llamadas; uno de secuencia no muestra el despliegue.

**Vistas importantes:**
- **4+1**: es general, pero declara qué cosas importantes hay que ver.
- **UML**: diagramas de **componentes** y de **secuencia**.
- **C4**: más moderna, pero no absoluta.

## Architecture Decision Record (ADR)

> [!tip] Decisión arquitectónica (adr.github.io)
> "Una decisión arquitectónica es una **elección de diseño justificada** que atiende un requisito funcional o no funcional **arquitectónicamente significativo**."

Un **ADR** es un documento corto que registra una decisión. Ganó mucha relevancia con la IA (*spec-driven design*) y es parte de la base de conocimiento de la empresa.

| Sección | Contenido |
|---|---|
| **Título** | La decisión, en pocas palabras |
| **Status** | Propuesta, aceptada, rechazada o reemplazada (*superseded*) |
| **Contexto** | El problema, las fuerzas y las restricciones que llevaron a decidir |
| **Decisión** | Qué se eligió |
| **Consecuencias** | Qué se gana, qué se pierde y qué queda pendiente (los tradeoffs) |

> [!example]- Ejemplo de ADR
> **ADR-007: Usar una cola de mensajes entre Checkout y Pagos**
> **Status:** aceptada.
> **Contexto:** el proveedor de pagos tiene caídas de varios minutos en horarios peak, y hoy Checkout lo llama de forma síncrona: si Pagos cae, Checkout devuelve errores y se pierden ventas.
> **Decisión:** Checkout publica `CobroSolicitado` en una cola persistente, y un worker de Pagos consume y reintenta con backoff.
> **Consecuencias:** (+) Checkout no se cae con el proveedor (desacople temporal); (+) Checkout y Pagos pasan a ser quantas separadas. (−) El usuario ve "pago en proceso" en vez de una confirmación inmediata; (−) hay que operar la cola y manejar duplicados (consumidores idempotentes).

> [!warning] Documentar el cómo sin el porqué
> Un diagrama o un README que solo describe la tecnología ("usamos RabbitMQ") no le sirve a quien llega después. Lo valioso es el **porqué**: qué problema se resolvió, qué alternativas se descartaron y qué se sacrificó. Eso es lo que captura un ADR.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que "ninguna vista posee toda la verdad"?
> Porque cada vista representa ciertos aspectos del sistema y omite otros: la de componentes muestra la estructura y las interfaces, pero no el orden de las llamadas ni el despliegue. Para entender el sistema completo se necesitan varias vistas complementarias.

> [!question]- ¿Qué secciones tiene un ADR y cuál es la más importante para quien llega después?
> Título, status, contexto, decisión y consecuencias. El contexto y las consecuencias son las más valiosas: explican por qué se decidió así y qué tradeoffs se aceptaron, información que no está en el código.

> [!question]- ¿Por qué la documentación ganó valor con la IA?
> Porque los agentes la necesitan como contexto para trabajar correctamente sobre el sistema, y porque documentar evita cargar contexto innecesario o depender de expertos. Además, el desarrollo guiado por especificaciones convierte los documentos en el insumo principal.

> [!question]- ¿Por qué llenar el código de comentarios se considera mala documentación?
> Porque los comentarios entre líneas explican detalles locales, se desactualizan con facilidad y no comunican las decisiones de alto nivel. La documentación arquitectónica debe registrar estructura y decisiones en vistas y ADRs.

> [!question]- Escriba el contexto y las consecuencias de un ADR que decide usar una CDN para los archivos estáticos.
> Contexto: los usuarios de otros países sufren tiempos de carga altos y el servidor de origen se satura con imágenes. Consecuencias: (+) menor latencia y menos carga en el origen; (−) costo de la CDN y riesgo de servir contenido viejo si la invalidación está mal configurada.

> [!question]- Nombre tres vistas que el curso considera importantes.
> 4+1 (general, define qué vistas hay que mostrar), UML (componentes y secuencia) y C4 (zoom de contexto a código).

> [!question]- V o F: "Un diagrama de componentes bien hecho reemplaza la necesidad de documentar decisiones".
> Falso. El diagrama muestra el resultado (qué componentes e interfaces hay), pero no por qué se eligió esa estructura ni qué alternativas se descartaron. Para eso están los ADRs.
