---
ramo: "Arquitectura de Sistemas de Software"
tema: "Medición de escalabilidad"
tags:
  - arquisis/escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Performance como atributo y sus métricas]]"
---

# Escalabilidad escenarios y cuellos de botella

La performance pregunta si el sistema responde bien **hoy**. La escalabilidad pregunta si **seguirá** respondiendo bien cuando la carga crezca 10 o 100 veces. Mike Krieger, cofundador de Instagram, lo describió como **"reemplazar todos los componentes de un auto mientras se conduce a 100 mph"**: Instagram tuvo 25.000 registros el primer día, y en el peak de carga Django empezó a responder errores sin que fuera obvio quién era el culpable.

## Definición

> [!tip] Escalabilidad
> **Capacidad del software de adaptarse para alcanzar nuevos requisitos de tamaño y alcance manteniendo un performance objetivo.** Permite dar servicio a multitud de usuarios con una experiencia fluida mientras se eleva la demanda.

La clave es "**manteniendo un performance objetivo**". Un sistema que atiende 10 veces más usuarios pero con una latencia 10 veces peor no escaló.

**Por qué se escala:** alta demanda, crecimiento de la base de usuarios (usuarios activos mensuales, MAU), funcionalidades que exigen más recursos, y el balance entre costo y performance, que incluye **optimizar el costo**: escalar también es reducir recursos cuando sobran.

**Preguntas que hay que responder:** ¿qué replicar? ¿qué minimizar? ¿qué optimizar? ¿cómo medir?

**Atributos relacionados:**
- **Heterogeneidad:** que el software pueda estar formado por múltiples partes o funciones en ambientes computacionales múltiples y dispares.
- **Portabilidad:** que se ejecute en varias plataformas (hardware y software) con modificaciones mínimas y sin degradar sus características funcionales ni no funcionales.

## Escenarios de escalabilidad

Se definen con **fuente, estímulo, entorno, artefacto, respuesta y medición de respuesta**.

| Parte | Ejemplo 1: feed | Ejemplo 2: contador de autos |
|---|---|---|
| Fuente | Usuarios | Cámaras que leen patentes en un sector concurrido |
| Estímulo | 10.000 usuarios abren el feed de forma concurrente | Llegan las lecturas de patentes |
| Entorno | Horario peak | Horario valle |
| Artefacto | El feed | El sistema de procesamiento |
| Respuesta | Escalar automáticamente en 5 minutos | Escalar en 5 min en la zona norte y en 20 min en la zona sur |
| Medida | p95 < 500 ms y tasa de errores < 0,1% | Procesar en 5 s el 70% de los casos, con un error del 0,0001% |

> [!warning] Un escenario de escalabilidad incluye cuánto tarda en escalar
> A diferencia de uno de performance, aquí la respuesta incluye **cuánto tarda el sistema en adaptarse** ("escalar en 5 minutos"), no solo qué latencia mantiene. Un escenario sin el tiempo de escalamiento queda incompleto.

## Fuentes de cuellos de botella

- **Recursos básicos** de las máquinas: CPU, RAM, disco y red.
- **Recursos asignados**: bases de datos, redes, servicios SaaS o IaaS con cuotas.
- **Locks**: bloqueos sobre filas, tablas o recursos compartidos que serializan el trabajo.
- **Dependencias externas**: APIs de terceros con sus propios límites.

## Métricas clave

| Grupo | Métricas |
|---|---|
| **Latencia** | p50, p95, p99, jitter |
| **Tráfico** | Peticiones por segundo (RPS), usuarios concurrentes, profundidad de la cola, distribución de prioridades en la cola |
| **Saturación** | % de CPU, % de RAM, número de conexiones, threads |
| **Eficiencia** | Costo por petición |
| **Datos** | Lag de replicación, tasa de aciertos de la caché (*cache hit*) |

Estas métricas hay que medirlas porque **no necesariamente escalan linealmente**: duplicar la carga puede triplicar la latencia. Sirven para identificar **dónde** está el cuello de botella.

**Cuidados al medir:**
- El stack es complejo.
- Las herramientas no solo no miden lo mismo: también **pueden introducir retardos**.
- **La optimización del código, en general, no es lo más significativo.** Los grandes saltos vienen de la arquitectura: caché, réplicas, particionar los datos, asincronía.

## Preguntas de repaso

> [!question]- ¿Por qué la definición de escalabilidad incluye "manteniendo un performance objetivo"?
> Porque atender más carga con peor servicio no es escalar. Un sistema escala si, al crecer la demanda, sigue cumpliendo sus objetivos de latencia y errores, agregando recursos de forma razonable.

> [!question]- Escriba un escenario de escalabilidad para la venta de entradas de un concierto.
> Fuente: compradores. Estímulo: 50.000 usuarios entran en el minuto en que se abre la venta. Entorno: apertura de la venta (peak). Artefacto: el servicio de compra. Respuesta: escalar automáticamente las instancias de compra en menos de 2 minutos. Medida: p95 < 1 s y menos del 0,5% de errores.

> [!question]- ¿Qué diferencia un escenario de escalabilidad de uno de performance?
> El de escalabilidad describe un aumento de la carga y exige que el sistema se adapte (incluido cuánto tarda en escalar) manteniendo la medida. El de performance mide la respuesta bajo una carga dada, sin pedir que el sistema cambie su capacidad.

> [!question]- Nombre cuatro fuentes de cuellos de botella y un ejemplo de cada una.
> Recursos básicos: la CPU de un servidor al 100%. Recursos asignados: el límite de conexiones de la base de datos. Locks: muchas transacciones actualizando la misma fila de stock. Dependencias externas: una API de pagos limitada a 100 req/s.

> [!question]- ¿Por qué el lag de replicación y la tasa de aciertos de la caché son métricas de escalabilidad?
> Porque las técnicas de escalabilidad de datos (réplicas y cachés) dependen de ellas. Un lag alto significa que las réplicas sirven datos viejos y no absorben lecturas consistentes. Una tasa de aciertos baja significa que la caché no está quitando carga al origen.

> [!question]- V o F: "La forma principal de escalar un sistema es optimizar el código".
> Falso. La optimización de código en general no es lo más significativo para escalar. Los grandes saltos vienen de decisiones de arquitectura: replicar, cachear, particionar datos y desacoplar con asincronía.

> [!question]- ¿Qué quiere decir que las métricas "no escalan linealmente"?
> Que duplicar la carga no duplica proporcionalmente la latencia o el uso de recursos: cerca de la saturación, la latencia crece mucho más rápido (como en la teoría de colas). Por eso hay que medir a distintos niveles de carga y no extrapolar.
