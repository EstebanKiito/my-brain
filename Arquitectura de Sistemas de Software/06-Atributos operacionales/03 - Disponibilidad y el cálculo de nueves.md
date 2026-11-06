---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos operacionales"
tags:
  - arquisis/atributos
  - arquisis/calculos
  - origen/complemento
prerrequisitos:
  - "[[02 - Confiabilidad]]"
---

# Disponibilidad y el cálculo de nueves

La **disponibilidad** es el atributo que más se mide en contratos: "99,9% de uptime". Cada nueve extra suena a poco, pero cuesta muchísimo. Esta nota explica qué significa cada nueve, cómo lo logra AWS, las tácticas para conseguirlo y cómo calcular la disponibilidad de un sistema con componentes en serie o en paralelo.

## Definición

> [!tip] Disponibilidad
> Capacidad de **mantener la operación el mayor tiempo posible** (99,99x%). Viene con un **SLA de tiempo asociado**, se relaciona con la confiabilidad y se deriva de otros requisitos. **Puede implicar un costo muy elevado.** Un sistema disponible **puede levantarse de caídas en sus componentes**.

El sistema nunca va a estar disponible el 100% del tiempo. Lo que se busca es acercarse al nivel que el negocio necesita, con todas las medidas de resiliencia razonables.

## Los nueves

![Tabla de porcentajes de disponibilidad y tiempo de caída permitido](adjuntos/Tabla%20de%20nueves%20de%20disponibilidad.png)

> [!example]- Transcripción de la imagen
> | Disponibilidad | Caída por año | Por mes | Por semana |
> |---|---|---|---|
> | 90% (un nueve) | 36,5 días | 72 horas | 16,8 horas |
> | 99% (dos nueves) | 3,65 días | 7,2 horas | 1,68 horas |
> | 99,5% | 1,83 días | 3,6 horas | 50,4 minutos |
> | 99,9% (tres nueves) | 8,76 horas | 43,8 minutos | 10,1 minutos |
> | 99,95% | 4,38 horas | 21,56 minutos | 5,04 minutos |
> | 99,99% (cuatro nueves) | 52,56 minutos | 4,32 minutos | 1,01 minutos |
> | 99,999% (cinco nueves) | 5,26 minutos | 25,9 segundos | 6,05 segundos |
> | 99,9999% (seis nueves) | 31,5 segundos | 2,59 segundos | 0,605 segundos |
> | 99,99999% (siete nueves) | 3,15 segundos | 0,259 segundos | 0,0605 segundos |

**Cálculo:** tiempo de caída permitido = $(1 - A) \times$ período. Para 99,9% en un año: $0{,}001 \times 8.760\text{ h} = 8{,}76$ h. Pasar de tres a cuatro nueves significa bajar de 8,76 horas a menos de 53 minutos de caída al año.

### Componentes en serie y en paralelo

- **En serie** (la petición pasa por todos): $A = A_1 \cdot A_2 \cdots A_n$. **Cada componente baja la disponibilidad total.**
- **En paralelo** (réplicas: basta que una funcione): $A = 1 - (1-A_1)(1-A_2)\cdots$. **La redundancia sube la disponibilidad.**

**Ejemplos:**
- Gateway (99,9%) → API (99,9%) → base de datos (99,5%) en serie: $0{,}999 \cdot 0{,}999 \cdot 0{,}995 \approx 0{,}993$, es decir, **99,3%**, menos que cualquiera de las partes.
- Dos réplicas de una API al 99% en paralelo: $1 - 0{,}01^2 = 0{,}9999$, es decir, **99,99%**. Con tres réplicas, 99,9999%.
- Esas dos réplicas (99,99%) detrás de un balanceador al 99,9% en serie: $0{,}9999 \cdot 0{,}999 \approx 0{,}9989$. **El balanceador pasa a ser el límite**, así que también hay que replicarlo.

## Cómo lo logra AWS

![Región de AWS con tres zonas de disponibilidad unidas por fibra](adjuntos/Región%20de%20AWS%20con%20tres%20zonas%20de%20disponibilidad.png)

> [!example]- Transcripción de la imagen
> - Una **REGION** que contiene tres **Availability Zone**, cada una con dos o tres **Data Center**.
> - Las zonas están unidas entre sí por conexiones de fibra con baja latencia y resilientes (*low latency resilient fiber connectivity*).

- **1 región = múltiples zonas de disponibilidad (AZ)**, mínimo 3.
- **1 AZ = un clúster de data centers.**
- Tienen planes frente a desastres: **lugares distintos**, **energía redundante** y **conexiones redundantes**.

### Tácticas de disponibilidad (releyendo el caso AWS)

| Grupo | Tácticas |
|---|---|
| **Detectar fallas** | Health checks, heartbeats, timeouts |
| **Prepararse y reparar** | Redundancia (≥ 3 AZs), failover entre zonas, reintentos, reposición del estado |
| **Prevenir fallas** | Aislamiento de fallas por zona, planes de desastre, degradación controlada |

**La táctica es lo que hace cumplible el escenario:** sin redundancia multi-AZ, "restablecido en < 30 s" es solo una opinión al aire. **Tradeoff:** unas 3 veces la infraestructura, más coordinación y complejidad operacional.

## El efecto sandía

![El efecto sandía: verde por fuera y rojo por dentro](adjuntos/Efecto%20sandía%20en%20los%20indicadores.png)

> [!example]- Transcripción de la imagen
> - Título *The Watermelon Effect*: "Your outputs (activities) meet defined targets, but the outcome (result) is not achieved."
> - Un círculo verde, *Outputs: Your reports are green. Success!*; una sandía al centro; y un círculo naranja, *Outcome: Your customers aren't happy. Fail.*

Los indicadores están **verdes por fuera** (el SLA de 99,9% se cumple en el promedio), pero el negocio está **rojo por dentro**: los usuarios no pueden usar el sistema justo cuando lo necesitan (el día del Cyber, a fin de mes). La disponibilidad debe medirse **cuando y donde importa a los usuarios**, no solo como un promedio mensual.

## Preguntas de repaso

> [!question]- ¿Cuánto tiempo de caída al año permite un SLA de 99,95%?
> $(1 - 0{,}9995) \times 8.760 \text{ h} = 4{,}38$ horas al año, unos 21,9 minutos al mes.

> [!question]- Un flujo pasa por un gateway (99,9%), un servicio (99,9%) y una base de datos (99,9%). ¿Cuál es la disponibilidad total?
> En serie: $0{,}999^3 \approx 0{,}997$, es decir, 99,7%. Es menor que la de cada componente, porque basta que falle uno para que falle el flujo.

> [!question]- ¿Qué disponibilidad tienen tres réplicas independientes de un servicio al 99%?
> En paralelo: $1 - 0{,}01^3 = 0{,}999999$, es decir, 99,9999%, siempre que las fallas sean independientes (por ejemplo, en distintas zonas).

> [!question]- Clasifique como detectar, preparar/reparar o prevenir: health check, failover entre zonas, aislamiento de fallas por zona, timeout.
> Detectar: health check y timeout. Preparar o reparar: failover entre zonas. Prevenir: aislamiento de fallas por zona.

> [!question]- ¿Qué es el efecto sandía?
> Cuando los indicadores (outputs) se cumplen y se ven verdes, pero el resultado para el usuario (outcome) es malo. Por ejemplo, un 99,9% mensual que esconde que el sistema se cayó justo en el peak de ventas.

> [!question]- ¿Por qué replicar la API no basta si el balanceador no está replicado?
> Porque el balanceador queda en serie con las réplicas y es un punto único de falla: la disponibilidad total queda limitada por la suya. Hay que replicar cada componente del camino crítico.

> [!question]- V o F: "Pasar de 99,9% a 99,99% de disponibilidad es una mejora menor y de bajo costo".
> Falso. Significa pasar de 8,76 horas a unos 53 minutos de caída al año, y suele requerir redundancia multi-zona, failover automático y más operación: el costo crece mucho con cada nueve.
