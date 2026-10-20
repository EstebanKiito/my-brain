---
ramo: "Sistemas Distribuidos"
tema: "Teoremas CAP y PACELC"
tags:
  - sd/cap
  - origen/complemento
prerrequisitos:
  - "[[01 - Teorema CAP]]"
  - "[[03 - Replicación primaria y replicación activa]]"
---

# Teorema PACELC

CAP solo dice qué pasa cuando la red se parte. Pero la mayor parte del tiempo la red funciona, y aun así hay que elegir: esperar a que todas las réplicas confirmen (más consistencia) o responder rápido (menos latencia). **PACELC** (Daniel J. Abadi, 2010) agrega ese segundo compromiso y sirve mejor para diseñar sistemas reales.

## Enunciado

> [!tip] PACELC
> **Si** hay partición (**P**), el sistema elige entre disponibilidad (**A**) y consistencia (**C**); **si no** (*else*, **E**), cuando funciona normalmente, elige entre latencia (**L**) y consistencia (**C**).

La **latencia** es el tiempo que tardan los datos en viajar por la red; alta latencia significa mucho retraso en la comunicación.

![Árbol de decisión de PACELC](adjuntos/%C3%81rbol%20de%20decisi%C3%B3n%20de%20PACELC.png)

> [!example]- Transcripción de la imagen
> Un rombo "Partition": si la respuesta es *Yes*, se elige entre *Availability* y *Consistency* (la parte que cubre el teorema CAP); si es *No*, se elige entre *Latency* y *Consistency*. Todo el árbol es el teorema PACELC.

Cada sistema se clasifica con dos letras de cada rama: **PA** o **PC**, y **EL** o **EC**.

## Por qué agregar la latencia

Si compras una entrada y la confirmación llega **4 horas** después, para CAP el sistema es disponible y consistente, y ahí termina el análisis. Para PACELC esa demora es una propiedad clave: el sistema priorizó la consistencia por sobre la latencia, a un costo inaceptable.

## Cómo se ubican los protocolos

| Protocolo | Prioriza | Por qué |
|---|---|---|
| [[03 - Replicación primaria y replicación activa\|Basado en primario]] | Consistencia sobre latencia | El primario ordena las peticiones y las réplicas aplican en el mismo orden; cuesta tiempo de secuenciamiento, desacople y la distancia al primario |
| [[02 - Replicación basada en quórum\|Quórum]] | Consistencia sobre latencia | Cada operación espera un quórum: el nodo más lento del quórum domina, y pesa la distancia geográfica |
| [[01 - Protocolos de replicación y gossip\|Gossip]] | Latencia sobre consistencia | Responde de inmediato; los nodos lejanos tardan en enterarse y distintos usuarios ven datos distintos |
| **Replicación sincrónica** | Según la operación | El primario espera que **todas** las réplicas confirmen cada escritura (consistencia), y las lecturas van a los secundarios (latencia), aunque pueden ver datos atrasados |
| **Replicación asincrónica (híbrida)** | Punto medio | Sincrónica hacia un subconjunto de réplicas "relacionadas" con el dato y asíncrona hacia el resto |

## Casos reales

| Sistema | En partición | Sin partición | Resultado |
|---|---|---|---|
| **Amazon Dynamo** | Disponibilidad | Latencia (consistencia eventual) | PA/EL |
| **Google Spanner** | Consistencia | Consistencia: usa el reloj **TrueTime** y ralentiza operaciones para garantizar el orden global | PC/EC |
| **Git** | Disponibilidad: se sigue haciendo commit y creando ramas | Latencia: cada usuario puede ver algo distinto hasta el merge | PA/EL |

## Pregunta de aplicación

Un banco global replica sus bases por sucursal. Las consultas de saldo se atienden desde la réplica local, que se sincroniza **periódicamente** con un servidor central, así que en condiciones normales puede mostrar saldos con demora. Si una sucursal pierde conexión con el servidor central, muestra un error y bloquea el acceso hasta reconectar.

- **En partición:** bloquea el acceso antes que mostrar datos posiblemente inconsistentes, así que es **PC**.
- **Sin partición:** responde desde la réplica local aunque el saldo esté atrasado: prioriza la **latencia**, es decir, **EL**.

Las slides marcan PC/EC como respuesta; con la descripción del enunciado, la lectura más coherente es **PC/EL** (ver `DUDAS.md`).

> [!warning] Las dos mitades son independientes
> Un sistema puede ser PC y a la vez EL: estricto cuando hay partición y rápido cuando no. Hay que analizar cada rama por separado.

## Preguntas de repaso

> [!question]- ¿Qué pregunta responde PACELC que CAP no responde?
> Qué sacrifica el sistema cuando **no** hay partición: si espera la coordinación entre réplicas (consistencia) o responde rápido con lo que tiene (latencia).

> [!question]- ¿Por qué Google Spanner es EC?
> Porque, aun sin particiones, ralentiza sus operaciones (con el reloj TrueTime) para garantizar un orden global y consistencia fuerte, aceptando más latencia.

> [!question]- ¿Por qué un sistema basado en quórum tiene alta latencia incluso sin fallas?
> Porque cada operación debe esperar las respuestas de varias réplicas, y el tiempo lo marca la más lenta (o la más lejana) del quórum.
