---
ramo: "Sistemas Distribuidos"
tema: "Sincronización de relojes físicos"
tags:
  - sd/relojes
  - redes
  - origen/complemento
prerrequisitos:
  - "[[03 - Método de Cristian]]"
  - "[[03 - Protocolos de transporte TCP y UDP]]"
---

# Protocolo NTP

Cristian sirve entre dos máquinas, pero Internet necesita sincronizar millones de relojes con UTC sin que todos consulten al mismo reloj atómico. El **Protocolo de Tiempo de Red** (NTP, *Network Time Protocol*) lo resuelve con una jerarquía de servidores y una medición más fina que la de Cristian: separa el **retraso** de la red del **desfase** entre relojes. Es uno de los protocolos más usados y viaja sobre UDP.

## Estratos

![Estratos de NTP](adjuntos/Estratos%20de%20NTP.png)

> [!example]- Transcripción de la imagen
> En la cima, tres relojes de referencia. Debajo, el estrato 1 con tres servidores conectados directamente a ellos (flechas amarillas). El estrato 2 tiene cuatro servidores que se sincronizan con el estrato 1 y entre sí, y el estrato 3 tiene seis servidores que se sincronizan con el estrato 2 y entre ellos (flechas rojas).

- **Estrato 0:** los relojes más precisos (atómicos, GPS).
- **Estrato N:** servidores que se sincronizan **entre ellos y con el estrato anterior**.
- A mayor N, la sincronización es **menos precisa**, porque se acumulan errores en cada nivel.

La jerarquía reparte la carga: los relojes de referencia atienden a pocos servidores, que a su vez atienden a muchos.

## Retraso y desfase

![Retraso y desfase en NTP](adjuntos/Retraso%20y%20desfase%20en%20NTP.png)

> [!example]- Transcripción de la imagen
> El servidor P envía "Empezar NTP" en $t_{p0}$. S lo recibe en $t_{s1}$ y responde en $t_{s2}$ ("Tu mensaje llegó en $t_{s1}$, la respuesta te la mando en $t_{s2}$"). La respuesta llega a P en $t_{p3}$. Debajo, las fórmulas de retraso y desfase.

Con cuatro marcas de tiempo (dos de cada reloj) se calculan dos métricas:

$$\text{Retraso} = (T_{s1} - T_{p0}) + (T_{p3} - T_{s2}) = (T_{p3} - T_{p0}) - (T_{s2} - T_{s1})$$

$$\text{Desfase} = \frac{(T_{s1} - T_{p0}) + (T_{s2} - T_{p3})}{2}$$

- **Retraso:** el tiempo total de viaje de los dos mensajes. A diferencia de Cristian, descuenta el tiempo que S tardó en responder ($T_{s2} - T_{s1}$).
- **Desfase:** la estimación de cuánto está adelantado el reloj de S respecto al de P. Es el promedio de los dos desfases aparentes, de ida y de vuelta.

## Ejemplos

![Ejemplo de NTP con desfase de cinco minutos](adjuntos/Ejemplo%20de%20NTP%20con%20desfase%20de%20cinco%20minutos.png)

> [!example]- Transcripción de la imagen
> P envía a las 11:00:01; S recibe a las 11:05:06 y responde a las 11:05:08; P recibe a las 11:00:13. Retraso $= (05{:}06 - 00{:}01) + (00{:}13 - 05{:}08) = 5{:}05 - 4{:}55 = 10$ segundos. Desfase $= \frac{5{:}05 + (05{:}08 - 00{:}13)}{2} = \frac{5{:}05 + 4{:}55}{2} = \frac{10{:}00}{2} = 5$ minutos.

| Ejemplo | $T_{p0}$ | $T_{s1}$ | $T_{s2}$ | $T_{p3}$ | Retraso | Desfase |
|---|---|---|---|---|---|---|
| 1 | 11:00:01 | 11:05:06 | 11:05:08 | 11:00:13 | 10 s | 5 min |
| 2 | 11:00:01 | 11:05:06 | 11:05:08 | 11:00:03 | 0 s | 5 min 5 s |
| 3 | 11:05:00 | 11:05:30 | 11:05:32 | 11:06:02 | 1 min | 0 s |

- **Ejemplo 2:** sin retraso, el desfase es **exacto**: no hay incertidumbre sobre cuánto tardó cada mensaje.
- **Ejemplo 3:** la ida y la vuelta tardan lo mismo según los relojes ($T_{s1} - T_{p0} = T_{p3} - T_{s2}$), así que NTP concluye que **no hay desfase**, aunque el viaje sea lento.

Los tres resultados se verificaron con una implementación de ambas fórmulas en Python.

## Varias mediciones

NTP repite el proceso **varias veces** y elige la medición con **menor retraso** para aplicar su desfase, porque un retraso pequeño deja menos margen de error. También puede consultar a **varios servidores** para obtener más valores. En la práctica se logran diferencias muy pequeñas entre relojes.

> [!tip] Cuál deja más cerca de UTC
> De los mecanismos del curso, NTP es el más seguro para quedar cerca de UTC: se apoya en relojes de referencia, mide el retraso con precisión y repite mediciones. Berkeley solo hace coincidir a los nodos entre sí, Cristian depende de una sola medición, y los relojes lógicos de Lamport ni siquiera miden la hora real.

## Preguntas de repaso

> [!question]- ¿Qué mejora NTP respecto de Cristian al calcular el retraso?
> Descuenta el tiempo que el servidor tardó en responder ($T_{s2} - T_{s1}$). Cristian supone que la respuesta es instantánea y atribuye todo el tiempo a la red.

> [!question]- ¿Por qué NTP se queda con la medición de menor retraso?
> Porque el error del desfase depende de cuán asimétricos sean la ida y la vuelta, y ese error está acotado por el retraso. Con menos retraso hay menos margen de error.

> [!question]- ¿Por qué un servidor de estrato 3 es menos preciso que uno de estrato 1?
> Porque cada nivel se sincroniza con el anterior a través de la red, y cada sincronización agrega su propio error. El estrato 3 acumula los errores de dos saltos más que el estrato 1.
