---
ramo: "Sistemas Distribuidos"
tema: "Tolerancia a fallos"
tags:
  - sd/tolerancia-a-fallos
  - origen/complemento
prerrequisitos:
  - "[[04 - Objetivos de un sistema distribuido]]"
---

# Confiabilidad y sus propiedades

Un sistema distribuido **tolerante a fallos** es, ante todo, un sistema **confiable**: uno que se puede usar de la forma esperada aunque algunas de sus partes fallen. "Confiable" agrupa varias propiedades distintas, y un mismo sistema puede destacar en una y fallar en otra. Distinguirlas permite decir qué exige cada aplicación.

## Confiabilidad

La **confiabilidad** (*dependability*) es el grado en que un sistema informático puede ser utilizado de la forma esperada. Para lograrla se busca cumplir cuatro propiedades:

| Propiedad | Pregunta que responde | Idea |
|---|---|---|
| **Disponibilidad** (*availability*) | ¿Está funcionando **ahora**? | Probabilidad de que el sistema esté operando correctamente en un momento dado, listo para usarse de inmediato |
| **Fiabilidad** (*reliability*) | ¿Cuánto tiempo funciona **sin interrupción**? | Capacidad de funcionar continuamente sin fallas durante un periodo considerable |
| **Seguridad** (*safety*) | ¿Qué pasa **si falla**? | Si el sistema falla, no se producen consecuencias catastróficas |
| **Mantenibilidad** | ¿Qué tan **fácil es repararlo**? | Facilidad con que un sistema fallido se repara después de una falla |

> [!tip] Disponibilidad no es fiabilidad
> La disponibilidad mira un **instante**; la fiabilidad, un **intervalo**. Un sistema que se cae un milisegundo cada hora tiene altísima disponibilidad, pero baja fiabilidad: nunca funciona una hora seguida.

## Disponibilidad con réplicas

Si un servidor tiene un 5 % de probabilidad de estar fallando y se replica en dos servidores independientes, el servicio solo cae si **ambos** fallan:

$$\text{Disponibilidad} = 1 - 0{,}05^2 = 99{,}75\,\%$$

Con tres servidores sube a $1 - 0{,}05^3 = 99{,}9875\,\%$ (calculado en Python). Replicar es la forma más directa de ganar disponibilidad.

## Ejemplos

![Ejemplos de propiedades de confiabilidad](adjuntos/Ejemplos%20de%20propiedades%20de%20confiabilidad.png)

> [!example]- Transcripción de la imagen
> - Un sistema que administra una central nuclear exige una alta **seguridad**.
> - Un código que ocupa varias librerías, pero todo modularizado para poder cambiar una librería si falla, garantiza una alta **mantenibilidad**.
> - Un sistema que funciona perfecto durante el día, pero que de 2 a 6 de la madrugada entra en mantención y nadie puede acceder, tiene una alta **fiabilidad**.
> - Una aplicación para ver el clima debería tener una alta **disponibilidad**.
> - Una plataforma para rendir una prueba, con una semana de plazo, debería tener una alta **fiabilidad**.

En la plataforma de pruebas lo grave no es que no esté arriba en un instante dado (hay una semana de plazo), sino que se caiga **mientras** alguien rinde la prueba. En la app del clima, en cambio, basta con que responda cuando se consulta. Lo ideal es que un sistema cumpla la mayor cantidad posible de estas propiedades.

## Métricas

| Métrica | Significado |
|---|---|
| **MTTF** (*Mean Time To Failure*) | Tiempo promedio hasta que un componente, proceso o nodo falla |
| **MTTR** (*Mean Time To Repair*) | Tiempo promedio para reparar el elemento fallado |
| **MTBF** (*Mean Time Between Failures*) | Tiempo promedio entre fallas: $MTBF = MTTF + MTTR$ |

Un MTTF alto indica buena **fiabilidad** y un MTTR bajo, buena **mantenibilidad**. Con ambos se suele estimar la disponibilidad como $\frac{MTTF}{MTTF + MTTR}$: la fracción del tiempo en que el sistema está operativo.

> [!warning] Tolerar fallos no es evitarlos
> Un sistema tolerante a fallos **no** asegura que no ocurra ninguna falla. Acepta que ocurrirán y busca seguir entregando el servicio a pesar de ellas.

## Preguntas de repaso

> [!question]- ¿Por qué un sistema con mantenimiento diario de 2 a 6 de la madrugada puede tener alta fiabilidad?
> Porque fuera de esa ventana funciona continuamente sin fallar. La ventana programada reduce la disponibilidad (no está operativo en esas horas), pero no implica que el sistema falle mientras se usa.

> [!question]- Si MTTF = 99 horas y MTTR = 1 hora, ¿cuánto vale MTBF y qué disponibilidad aproximada tiene?
> $MTBF = 99 + 1 = 100$ horas, y la disponibilidad es $\frac{99}{100} = 99\,\%$.

> [!question]- ¿Qué propiedad prioriza el software de control de un avión y por qué?
> La seguridad: una falla puede tener consecuencias catastróficas, así que el sistema debe fallar de forma segura antes que seguir funcionando de forma incorrecta.
