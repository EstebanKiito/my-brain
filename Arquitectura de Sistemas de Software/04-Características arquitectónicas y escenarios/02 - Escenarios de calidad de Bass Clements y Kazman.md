---
ramo: "Arquitectura de Sistemas de Software"
tema: "Características arquitectónicas y escenarios"
tags:
  - arquisis/atributos
  - arquisis/escenarios
  - origen/complemento
prerrequisitos:
  - "[[01 - Stakeholders y características arquitectónicas]]"
---

# Escenarios de calidad de Bass Clements y Kazman

"El sistema debe ser escalable" no dice nada: ¿escalable a cuántos usuarios, en cuánto tiempo, con qué latencia? Un **escenario** convierte un atributo en una promesa verificable. Es la herramienta que usa el curso para justificar decisiones y evitar que alguien pregunte "¿por qué?" sin respuesta.

> [!tip] "Un atributo sin escenario es una opinión al aire"
> Los escenarios (Bass, Clements y Kazman, *Software Architecture in Practice*, 4.ª ed., cap. 4) dan el **contexto** donde hablar de una característica tiene sentido. Aíslan problemas de **vocabulario**, **testeabilidad** y responsabilidad, y ayudan a **diferenciar un atributo de otro** a partir de un aspecto preciso.

## Las seis partes

![Diagrama de las seis partes de un escenario](adjuntos/Seis%20partes%20de%20un%20escenario%20de%20calidad.png)

> [!example]- Transcripción de la imagen
> - (1) **Source**, una mano que actúa, envía (2) un **Stimulus** al (3) **Artifact**, que está dentro de un (4) **Environment**.
> - El artefacto produce una (5) **Response**, que se evalúa con un (6) **Response Measure** (un medidor).

| Parte | Qué es | Ejemplos |
|---|---|---|
| **Fuente** | Quién o qué genera el estímulo | Un usuario, otro sistema, un operador, un atacante |
| **Estímulo** | La condición que llega al sistema | Una carga, un cambio, una falla, un intento de acceso |
| **Entorno** | En qué condiciones ocurre | Operación normal, horario peak, modo degradado |
| **Artefacto** | Qué parte del sistema recibe el estímulo | Un servicio, la base de datos, el sistema completo |
| **Respuesta** | Qué debe hacer el sistema | Escalar, reconectarse, registrar, rechazar |
| **Medición de la respuesta** | El número que decide si la promesa se cumplió | p95 < 500 ms, 0 eventos perdidos, ≤ 3 días-persona |

![Escenario de disponibilidad con un servidor que falla](adjuntos/Escenario%20de%20disponibilidad%20de%20ejemplo.png)

> [!example]- Transcripción de la imagen
> - **Source:** un servidor de una granja de servidores. **Stimulus:** el servidor falla.
> - **Artifact:** el servidor. **Environment:** operación normal.
> - **Response:** el sistema informa al operador y sigue operando. **Response Measure:** sin tiempo de inactividad (*no downtime*).

## Un escenario por atributo

| Atributo | Escenario |
|---|---|
| **Escalabilidad** | Un sistema disponibiliza un **feed** (artefacto) para **usuarios** (fuente) cuando **10.000 abren el home de forma concurrente** (estímulo) en **horario peak** (entorno); debe tener **p95 < 500 ms y errores < 0,1%** (medición) **escalando automáticamente en 5 minutos** (respuesta) |
| **Mantenibilidad** | Un **desarrollador** debe **agregar un medio de pago** durante el **desarrollo normal** en el **servicio de pagos**; el cambio queda implementado y probado **tocando un solo módulo, sin efectos colaterales**, en **≤ 3 días-persona** |
| **Flexibilidad** | El **negocio** exige **cambiar el proveedor de notificaciones** con el **sistema en producción**; **solo se modifica el adaptador** del proveedor, sin tocar la lógica de negocio, en **≤ 2 días-persona** |
| **Performance** | **Usuarios del SII** generan la **carga peak de M req/s** en **horario peak** contra el **servicio principal**; responde con **p95 < 500 ms y errores < 0,1%** |
| **Confiabilidad** | El **broker** sigue publicando mientras el **listener sufre una desconexión transitoria** en **operación normal**; el listener **se reconecta y repone los eventos desde el último offset**, con **0 eventos perdidos en el mes** |

Un escenario más complejo: un **contador de automóviles** en un sector concurrido usa las patentes de los vehículos. Debe procesar los datos **en 5 segundos para el 70% de los casos** en **horario valle**, con un error del **0,0001%**, y el escalamiento debe estar listo **en 5 minutos para la zona norte y en 20 minutos para la zona sur**.

## Del deseo al atributo

El mismo sistema cambia de atributo según el escenario:
- "En un **Cyber** todos entran a las 00:00 y el sistema debe soportarlo" → **escalabilidad**.
- "Los usuarios bajan a menos de la mitad y el sistema debe seguir funcionando **usando menos recursos**" → **elasticidad**, y también eficiencia.
- "**Si se cae un servidor**, el sistema debe seguir funcionando" → **disponibilidad**.

> [!warning] El error típico: escenario sin medida o sin entorno
> "El sistema debe responder rápido cuando hay muchos usuarios" no es un escenario: le falta la **medición** (¿cuánto es rápido?) y precisar el **entorno** (¿peak? ¿degradado?). Sin medida no se puede verificar, y sin entorno no se sabe cuándo aplica.

## Preguntas de repaso

> [!question]- Nombre las seis partes de un escenario y dé un ejemplo de cada una para un ataque de fuerza bruta.
> Fuente: un atacante. Estímulo: 1.000 intentos de login por minuto. Entorno: operación normal. Artefacto: el servicio de autenticación. Respuesta: bloquear la cuenta y la IP y alertar. Medición: el bloqueo ocurre en menos de 10 intentos fallidos y se alerta en menos de 1 minuto.

> [!question]- ¿Por qué "un atributo sin escenario es una opinión al aire"?
> Porque sin contexto ni medida no se puede verificar si se cumple ni comparar alternativas. El escenario convierte el atributo en una promesa medible y justificable.

> [!question]- ¿Qué parte del escenario distingue uno de escalabilidad de uno de performance?
> La respuesta: en el de escalabilidad, el sistema debe adaptarse (escalar automáticamente en cierto tiempo) ante un aumento de carga. En el de performance basta con cumplir la medida bajo la carga dada.

> [!question]- Escriba un escenario de mantenibilidad para agregar un nuevo tipo de reporte.
> Fuente: un desarrollador. Estímulo: debe agregar un reporte de ventas por región. Entorno: desarrollo normal. Artefacto: el módulo de reportes. Respuesta: el reporte queda implementado y probado tocando solo ese módulo, sin efectos colaterales. Medición: ≤ 2 días-persona.

> [!question]- ¿Qué tiene de malo "el sistema debe estar siempre disponible"?
> No tiene una medida realista (ningún sistema está disponible el 100% del tiempo), ni fuente, estímulo ni entorno. Debería ser algo como "ante la caída de un servidor, en operación normal, el sistema sigue respondiendo con downtime < 30 s, cumpliendo 99,95% mensual".

> [!question]- Identifique las partes del escenario del contador de automóviles.
> Fuente: los vehículos y las cámaras que leen patentes. Estímulo: las lecturas que llegan. Entorno: horario valle. Artefacto: el sistema de procesamiento. Respuesta: procesar y escalar. Medición: 5 s para el 70% de los casos, error del 0,0001%, y escalamiento en 5 min (norte) o 20 min (sur).

> [!question]- V o F: "Un escenario de flexibilidad debe medir la latencia del sistema".
> Falso. La flexibilidad se mide en esfuerzo de cambio (días-persona, módulos tocados), no en latencia. La medida debe corresponder al atributo.
