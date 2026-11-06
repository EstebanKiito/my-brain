---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos transversales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[01 - Performance y escalabilidad como requisitos operacionales]]"
---

# Elasticidad frente a escalabilidad

Los **requisitos transversales** involucran varias partes del sistema a varios niveles: afectan tanto la parte estructural como la operacional, son más difíciles de categorizar e incorporan más elementos del dominio. El primero es la **elasticidad**, que el curso insiste en no confundir con escalabilidad. Es una pregunta de prueba clásica.

## Definición

> [!tip] Elasticidad
> Capacidad de **soportar aumentos "instantáneos" de demanda operacional**, obteniendo recursos en función de las necesidades. Requiere una **estructura orientada** a ello, **capacidad operacional** y un **entorno compatible**. Suele estar disponible en los proveedores de nube.

| | Escalabilidad | Elasticidad |
|---|---|---|
| Naturaleza | **Preventiva**: se diseña para soportar una demanda mayor | **Reactiva**: detecta el aumento de carga y levanta capacidad |
| Horizonte | Crecimiento sostenido en el tiempo | Picos repentinos, y bajadas |
| Pregunta | ¿Hasta cuántos usuarios llego? | ¿Qué tan rápido me adapto a un pico y vuelvo a bajar? |
| Ejemplo | Pasar de 10.000 a 1.000.000 usuarios en un año | El Cyber a medianoche, o una noticia viral |

![Gráficos de usuarios en el tiempo para escalabilidad y elasticidad](adjuntos/Escalabilidad%20frente%20a%20elasticidad%20en%20el%20tiempo.png)

> [!example]- Transcripción de la imagen
> - Dos gráficos de cantidad de usuarios en el tiempo, titulados **Escalabilidad** y **Elasticidad**.
> - **Escalabilidad:** una línea horizontal marca la capacidad. La demanda la supera en un punto (marcado con una estrella), y el área entre la capacidad y la demanda está achurada con la anotación "se está perdiendo ese dinero" (capacidad pagada que no se usa).
> - **Elasticidad:** la capacidad sigue a la demanda, subiendo y bajando junto a ella, con poca diferencia entre ambas.

Con escalabilidad, la capacidad se fija para un máximo esperado: si la demanda lo supera, el sistema puede caerse, y mientras no lo supera, se paga capacidad ociosa. Con elasticidad, la capacidad acompaña a la demanda.

## Elástico no implica escalable

> [!warning] Pregunta de prueba: "no todo sistema elástico es escalable"
> La escalabilidad es **funcional** (que el sistema completo soporte más carga). Un componente puede ser perfectamente elástico y aun así el sistema no escalar.

**Ejemplo 1: un componente limitado aguas abajo.**

![A envía a B, que es elástico, y B envía a C, que es limitado](adjuntos/Componente%20elástico%20que%20satura%20a%20uno%20limitado.png)

> [!example]- Transcripción de la imagen
> - Tres componentes en fila: **A** se conecta a **B** (dibujado como varias cajas apiladas, porque se replica) y B se conecta a **C**, uno solo.
> - Muchas flechas salen de B hacia C: B multiplica el tráfico que le llega a C.

A envía peticiones a B, que es totalmente elástico y se replica según la carga. Pero B, al terminar, envía todo a C, que tiene una capacidad limitada. Ante más carga, B aguanta y **C colapsa**. El sistema no escaló.

**Ejemplo 2: una página que comprime videos.**

![Cliente, broker con cola y workers que crecen según demanda](adjuntos/Broker%20con%20workers%20que%20crecen%20según%20demanda.png)

> [!example]- Transcripción de la imagen
> - Croquis: "e) Página web que comprime videos". Un cliente **C** envía a un **Broker** (con una cola), y el broker reparte a varios **Workers** apilados, con la anotación "crece según demanda" y "replicación con autoescaler".
> - Muchas flechas entran al broker.

El broker y los workers crecen con la demanda, así que el sistema es elástico. Pero cada worker tarda en procesar, y si en un mismo minuto llegan más peticiones de las que los workers alcanzan a procesar, la cola crece sin límite y el sistema empieza a colapsar. **Los sistemas elásticos también tienen un límite.**

## Estructural y operacional a la vez

La elasticidad es transversal:
- **Estructural:** hay que **programarla** para que el sistema pueda levantarse según la demanda (servicios sin estado, autoescalado configurado). Un monolito con estado no puede ser elástico.
- **Operacional:** se **mide** con el sistema funcionando (tiempo de reacción ante el pico).

## Los costos

- **Problema de la escalabilidad:** si se puede crecer mucho, hay que pagarlo, y la capacidad preparada para el máximo se paga aunque no se use.
- **Problema de la elasticidad:** si un atacante hace muchas peticiones por minuto, el sistema crece y **hay que pagarle a la nube por esa capacidad**. **Hay que limitar el crecimiento** con un máximo de instancias y rate limiting.

## Preguntas de repaso

> [!question]- Diferencie escalabilidad y elasticidad.
> La escalabilidad es preventiva: el sistema está diseñado para soportar una demanda mayor y sostenida. La elasticidad es reactiva: detecta un aumento repentino de carga y obtiene recursos en el momento, para luego liberarlos.

> [!question]- V o F: "Todo sistema elástico es escalable".
> Falso. Un componente puede ser elástico pero el sistema no escalar si otro componente es limitado (B elástico que satura a C), o si la carga supera lo que los recursos elásticos alcanzan a procesar en el tiempo disponible.

> [!question]- Según el gráfico de escalabilidad, ¿qué problema tiene fijar la capacidad para el máximo esperado?
> Mientras la demanda está bajo la capacidad, se paga capacidad ociosa (dinero perdido), y si la demanda supera la capacidad prevista, el sistema puede caerse.

> [!question]- ¿Por qué la elasticidad es a la vez estructural y operacional?
> Estructural, porque el sistema debe estar construido para replicarse según la demanda (sin estado, con autoescalado). Operacional, porque solo se puede medir con el sistema funcionando, observando cómo reacciona ante los picos.

> [!question]- ¿Qué riesgo de costo trae la elasticidad y cómo se mitiga?
> Que un ataque o un error genere tráfico masivo y el sistema escale automáticamente, generando una factura enorme en la nube. Se mitiga limitando el crecimiento (máximo de instancias), con rate limiting y con alertas de presupuesto.

> [!question]- Mini caso: una tienda tiene tráfico estable salvo en el Cyber, cuando sube 30 veces durante 6 horas. ¿Qué atributo prioriza?
> Elasticidad: el pico es repentino y temporal, así que conviene obtener recursos solo durante esas horas y liberarlos después, en vez de pagar todo el año una capacidad 30 veces mayor. Hay que asegurarse de que los componentes aguas abajo (base de datos, pagos) también soporten el pico.

> [!question]- ¿Qué requiere un sistema para ser elástico según el curso?
> Una estructura orientada a ello (componentes que se puedan replicar), capacidad operacional (monitoreo y autoescalado) y un entorno compatible (normalmente un proveedor de nube).
