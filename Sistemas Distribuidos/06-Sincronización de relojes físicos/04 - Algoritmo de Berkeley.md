---
ramo: "Sistemas Distribuidos"
tema: "Sincronización de relojes físicos"
tags:
  - sd/relojes
  - origen/complemento
prerrequisitos:
  - "[[03 - Método de Cristian]]"
---

# Algoritmo de Berkeley

Cristian supone que alguien tiene la hora correcta. ¿Qué pasa en una red sin acceso a UTC, donde ningún nodo es más confiable que otro? El **algoritmo de Berkeley** no busca la hora "real", sino que todos los nodos **coincidan entre sí**: un líder estima la hora de cada uno con Cristian, calcula el **promedio** y le dice a cada nodo cuánto ajustar. No hace falta memorizar sus cálculos, pero sí entender qué hace.

## Idea

- Se creó para entornos **sin receptores de tiempo UTC**.
- Entre los nodos se elige un **líder**; los demás son **seguidores**. En parte de la literatura se los llama "maestro" y "esclavos".
- El líder define una hora común, que él y los seguidores adoptan.

## Funcionamiento

1. El líder aplica **Cristian** para estimar la hora actual de cada seguidor, considerando el retraso de comunicación.
2. Calcula el **promedio** de las horas de todos los nodos, **incluida la suya**.
3. Ajusta su propio reloj a ese promedio.
4. Envía a cada nodo la **diferencia** entre su hora estimada y el promedio (no la hora promedio).
5. Cada nodo ajusta su reloj según la diferencia recibida.

![Berkeley estima la hora de cada seguidor](adjuntos/Berkeley%20estima%20la%20hora%20de%20cada%20seguidor.png)

> [!example]- Transcripción de la imagen
> El líder envía consultas en $t_{L0}$ a los nodos K y T. K responde con su hora $t_{K1}$, que llega al líder en $t_{L1}$; T responde con $t_{T1}$, que llega en $t_{L2}$. Fórmulas: $T_K = t_{K1} + \frac{t_{L1} - t_{L0}}{2}$ y $T_T = t_{T1} + \frac{t_{L2} - t_{L0}}{2}$.

![Berkeley envía la diferencia a cada nodo](adjuntos/Berkeley%20env%C3%ADa%20la%20diferencia%20a%20cada%20nodo.png)

> [!example]- Transcripción de la imagen
> Como las respuestas llegan en momentos distintos, el líder lleva todas las estimaciones al instante $t_{L2}$: la de K pasa a $T_K + (t_{L2} - t_{L1})$. Calcula el promedio $T_{prom}$ y envía a K la diferencia $d_{LK}$ y a T la diferencia $d_{LT}$, es decir, la diferencia entre el tiempo estimado en $t_{L2}$ y $T_{prom}$ para cada nodo.

> [!tip] Por qué se envía la diferencia y no la hora
> La hora promedio tardaría en llegar y ya estaría desactualizada al recibirse. Una diferencia ("atrásate 7 segundos") sigue siendo válida sin importar cuánto tarde el mensaje.

## Ejemplo numérico

Tiempos en segundos tras el inicio. El líder pregunta en 0:00; K responde con su hora 0:20 y la respuesta llega al líder en 0:30; T responde con 0:10 y la respuesta llega en 0:40.

![Ejemplo numérico de Berkeley](adjuntos/Ejemplo%20num%C3%A9rico%20de%20Berkeley.png)

> [!example]- Transcripción de la imagen
> Nodo K marca 00:20, 0:35 y 0:45; el líder marca 00:00, 0:30 y 0:40 (que pasa a 0:38); nodo T marca 0:10 y 0:30. Entre K y el líder hay 15 s de retraso y entre T y el líder, 20 s. El líder envía −7 s a K y +8 s a T. Texto: "Se envía diferencia de tiempo para que todos calcen con el tiempo promedio. K: 0:45 − 0:38 = 7s [7 segundos adelantado]. T: 0:30 − 0:38 = −8s [8 segundos atrasado]".

| Paso | K | Líder | T |
|---|---|---|---|
| Retraso estimado (mitad del viaje) | $\frac{30-0}{2} = 15$ s | – | $\frac{40-0}{2} = 20$ s |
| Hora estimada al recibir | $20 + 15 = 0{:}35$ | – | $10 + 20 = 0{:}30$ |
| Llevada al instante 0:40 | $35 + (40 - 30) = 0{:}45$ | 0:40 | 0:30 |
| Promedio | | $\frac{45 + 40 + 30}{3} \approx 0{:}38$ | |
| Diferencia enviada | −7 s (adelantado) | se ajusta a 0:38 | +8 s (atrasado) |

**Comprobación:** el mensaje "−7" tarda 15 s en llegar a K. Cuando K marca 1:00, lo aplica y queda en 0:53; el líder, que partió de 0:38, también marca $0{:}38 + 15 = 0{:}53$. El "+8" tarda 20 s en llegar a T: T marca 0:50, se ajusta a 0:58, y el líder marca $0{:}38 + 20 = 0{:}58$. Los tres coinciden.

> [!warning] Sincronizados entre sí, no con UTC
> Berkeley logra que los nodos coincidan, pero la hora acordada es un promedio, no la hora real. Si todos los relojes derivan en la misma dirección, el grupo entero se aleja de UTC.

## Preguntas de repaso

> [!question]- ¿Por qué el líder lleva todas las estimaciones a un mismo instante antes de promediar?
> Porque las respuestas llegan en momentos distintos. Promediar una hora estimada en 0:30 con otra estimada en 0:40 mezclaría instantes diferentes; hay que sumar a cada estimación el tiempo transcurrido hasta el instante común.

> [!question]- ¿Qué tiene en común Berkeley con Cristian y en qué se diferencia?
> Usa Cristian para estimar la hora de cada nodo. Se diferencia en que no confía en un reloj de referencia: promedia las horas de todos, incluida la del líder, y distribuye diferencias de ajuste.

> [!question]- ¿Por qué Berkeley requiere elegir un líder?
> Porque alguien debe recolectar las horas, calcular el promedio y enviar los ajustes. Es un ejemplo de un algoritmo que combina dos mecanismos de coordinación: elección de líder y sincronización de relojes.
