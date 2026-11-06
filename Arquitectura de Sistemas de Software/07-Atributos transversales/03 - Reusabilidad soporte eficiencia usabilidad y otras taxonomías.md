---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos transversales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[02 - Seguridad como atributo de calidad]]"
---

# Reusabilidad soporte eficiencia usabilidad y otras taxonomías

Los últimos atributos transversales del curso son más vagos o dependen mucho de los demás, y por eso es fácil invocarlos mal en una prueba. Esta nota los define, dice cuándo tienen sentido y cierra con otras taxonomías de calidad, como la de McCall, que ordenan los atributos según quién los pide.

## Reusabilidad

> [!tip] Reusabilidad
> Capacidad de un sistema o componente de **volver a usarse en otros sistemas más grandes**: funcionalidad compartida.

**Ejemplo:** un servicio de autenticación reutilizado por todas las aplicaciones de la empresa.

> [!warning] Precaución con el exceso de reuso
> **Un exceso de reusabilidad puede provocar un fracaso arquitectónico.** Un componente que todos comparten se vuelve un acoplamiento compartido: si cambia o se cae, arrastra a todos los que lo usan. Es la promesa del "reuso extremo" de SOA, que terminó en buses y modelos canónicos que nadie podía cambiar.

## Soporte

> [!tip] Soporte
> Capacidad de **responder a requerimientos de modificación, mantención y extensión puntual** del sistema.

- Se relaciona con la mantenibilidad, pero es **operado por humanos**: es el trabajo de atender tickets y casos puntuales.
- Requiere una **estructura sólida** y **capacidad operacional**.
- Se asocia a métricas como **tickets por hora** y **SLAs** de respuesta.

## Eficiencia

> [!tip] Eficiencia
> Capacidad de **cumplir las metas de negocio con el menor uso de recursos posible**.

- Depende mucho de otros NFR.
- Es **muy medible, pero con métricas muy contextualizadas**: ¿es bueno que una app use 1 GB de RAM? Depende de lo que haga. ¿Por qué mi aplicación sube tanto el uso de CPU del servidor? Hay que compararlo con el trabajo que realiza.
- **Ejemplo:** un sistema que con la mitad de los usuarios sigue funcionando y usa la mitad de los recursos es eficiente (y elástico).

## Usabilidad

> [!tip] Usabilidad (*Fundamentals of Software Architecture*)
> **Nivel de entrenamiento requerido por los usuarios** para lograr sus metas con la aplicación.

- Es bastante vaga y **más difícil de medir**, pero debe considerarse.
- Se puede pedir en prácticamente todas las aplicaciones con interacción: hay que saber **cuándo priorizarla**.
- Está fuertemente influenciada por muchos otros atributos (performance, disponibilidad).

> [!warning] Usabilidad en la prueba
> Solo suma si el enunciado la justifica de forma específica. Por ejemplo: "hay segmentos de la población con menor conocimiento tecnológico que suelen caer en estas estafas", o "el usuario interactúa con muchas interfaces". "Toda app debe ser fácil de usar" no basta.

## Otras taxonomías: McCall

![Atributos de calidad de McCall agrupados por usuario final, desarrollador y negocio](adjuntos/Taxonomía%20de%20McCall%20por%20perspectiva.png)

> [!example]- Transcripción de la imagen
> - **Usuario final:** performance, disponibilidad (*availability*), usabilidad, seguridad.
> - **Desarrollador:** mantenibilidad, portabilidad, reusabilidad, testeabilidad.
> - **Negocio y stakeholders:** time to market, costo y beneficios, vida útil proyectada, mercado objetivo, integración con sistemas legados, calendario de rollback.

El modelo de McCall también ordena los factores a **nivel de producto** en tres grupos:

| Grupo | Factores | Pregunta que responde |
|---|---|---|
| **Operación** | Correctness (exactitud), reliability (confiabilidad), usability, integrity (integridad), efficiency | ¿El producto hace lo esperado, con precisión, de forma segura y con buen uso de recursos? |
| **Revisión** | Maintainability, flexibility, testability | ¿Qué tan fácil es corregirlo, cambiarlo y probarlo? |
| **Transición** | Portability, reusability, interoperability | ¿Puede usarse en otro hardware, reusarse en otras aplicaciones o conectarse con otros sistemas? |

Cada factor se define como un **esfuerzo o grado**. Por ejemplo, la **mantenibilidad** es el esfuerzo requerido para localizar y corregir una falla. La **testeabilidad** es el esfuerzo para probar el programa y asegurar que hace lo que debe. La **integridad** es el grado en que se controla el acceso no autorizado a los datos.

**Métricas de operación:** además de los atributos, se monitorean métricas como uptime, tasa de errores o tickets, que muestran si las promesas se cumplen en la práctica.

## Preguntas de repaso

> [!question]- ¿Por qué un exceso de reusabilidad puede ser un fracaso arquitectónico?
> Porque el componente compartido se vuelve un punto de acoplamiento para todos: cambiarlo exige coordinar con todos sus usuarios, y si falla, arrastra a todos. Es lo que pasó con el reuso extremo en SOA.

> [!question]- Diferencie soporte y mantenibilidad.
> La mantenibilidad es una propiedad del código y la estructura: qué tan fácil es reparar y evolucionar. El soporte es la capacidad operacional, con personas, de atender requerimientos puntuales, y se mide con tickets por hora y SLAs.

> [!question]- ¿Por qué se dice que la eficiencia tiene "métricas muy contextualizadas"?
> Porque un número de recursos (1 GB de RAM, 60% de CPU) no dice nada sin saber cuánto trabajo hace el sistema y para qué. La eficiencia es la relación entre metas cumplidas y recursos usados.

> [!question]- ¿Cómo define usabilidad Fundamentals of Software Architecture y cuándo conviene priorizarla?
> Como el nivel de entrenamiento que necesitan los usuarios para lograr sus metas con la aplicación. Conviene priorizarla cuando el público objetivo tiene poca experiencia tecnológica o la interacción es compleja, y el enunciado lo respalda.

> [!question]- Según McCall, ¿qué atributos le importan al desarrollador y cuáles al negocio?
> Al desarrollador: mantenibilidad, portabilidad, reusabilidad y testeabilidad. Al negocio: time to market, costo y beneficios, vida útil proyectada, mercado objetivo, integración con sistemas legados y calendario de rollback.

> [!question]- Clasifique en operación, revisión o transición según McCall: portabilidad, confiabilidad, testeabilidad, interoperabilidad.
> Confiabilidad: operación. Testeabilidad: revisión. Portabilidad e interoperabilidad: transición.

> [!question]- V o F: "La reusabilidad siempre es deseable porque evita duplicar código".
> Falso. Reusar crea dependencias compartidas: si el componente reusado cambia o falla, afecta a todos. A veces duplicar algo pequeño (separate ways) es más barato que compartirlo.
