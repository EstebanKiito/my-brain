---
ramo: "Sistemas Distribuidos"
tema: "Sincronización de relojes físicos"
tags:
  - sd/relojes
  - origen/complemento
prerrequisitos:
  - "[[02 - Relojes físicos y desincronización]]"
---

# Método de Cristian

La forma más directa de corregir un reloj es preguntarle la hora a alguien que la sepa mejor. El problema es que la respuesta tarda en llegar: cuando el cliente la recibe, ya pasó tiempo. El **método de Cristian** corrige ese retraso con una estimación simple, y es la base de los otros algoritmos de relojes físicos. Su fórmula hay que saberla de memoria.

## Supuestos

- Un servidor P ajusta su reloj a lo que diga otro servidor S.
- S tiene un **mejor reloj**: sincronizado con **UTC** (tiempo universal coordinado) o con un reloj atómico.
- Existe un **retraso de comunicación**, y se asume que es **igual de ida que de vuelta**.
- S **responde de inmediato** al recibir la consulta.

Con la respuesta de S y el retraso medido, P estima la hora que tendría S **en el momento de recibir la respuesta** y sobrescribe su propio reloj con ella.

## La fórmula

![Método de Cristian](adjuntos/M%C3%A9todo%20de%20Cristian.png)

> [!example]- Transcripción de la imagen
> El servidor P envía "¿Qué hora es?" en su tiempo $t_0$. El servidor S responde "Son las $T_s$", y la respuesta llega a P en su tiempo $t_1$. Abajo, la fórmula: $T_{servidor\ p} = T_s + \frac{t_1 - t_0}{2}$.

$$T_P = T_s + \frac{t_1 - t_0}{2}$$

- $t_1 - t_0$ es el tiempo total de ida y vuelta (*round trip*), medido con el reloj de P. Como es una diferencia, no importa que el reloj de P esté desfasado.
- Si ida y vuelta tardan lo mismo, la respuesta viajó durante $\frac{t_1 - t_0}{2}$. Mientras viajaba, el reloj de S siguió avanzando: por eso se suma esa mitad a $T_s$.

## Ejemplo

![Ejemplo del método de Cristian](adjuntos/Ejemplo%20del%20m%C3%A9todo%20de%20Cristian.png)

> [!example]- Transcripción de la imagen
> P pregunta a las 2:00 (su reloj). S responde "Son las 3:00". La respuesta llega a P a las 2:30. Cálculo: $T_{servidor\ p} = 3{:}00 + \frac{2{:}30 - 2{:}00}{2} = 3{:}15$.

El viaje completo tardó 30 minutos según P, así que la respuesta tardó unos 15 minutos en volver. Cuando llegó, S ya marcaba aproximadamente $3{:}00 + 0{:}15 = 3{:}15$, y P ajusta su reloj a esa hora.

```python
def cristian(ts, t0, t1):
    return ts + (t1 - t0) / 2
# cristian(3:00, 2:00, 2:30) → 3:15 (verificado en segundos)
```

> [!warning] Los supuestos casi nunca se cumplen
> El retraso de ida rara vez es igual al de vuelta, y S tampoco responde en tiempo cero. El error de la estimación puede llegar hasta la mitad del *round trip*. Por eso conviene medir con viajes cortos: cuanto menor es $t_1 - t_0$, menor es el error posible.

> [!tip] ¿Y si S no tiene una mejor hora?
> Cristian necesita un servidor confiable. Si ningún nodo tiene una referencia UTC, se usa [[04 - Algoritmo de Berkeley|Berkeley]], que aplica Cristian a todos los nodos y promedia.

## Preguntas de repaso

> [!question]- ¿Por qué se suma solo la mitad de $t_1 - t_0$ y no el total?
> Porque $t_1 - t_0$ incluye la ida de la pregunta y la vuelta de la respuesta. A la hora $T_s$ solo hay que sumarle lo que tardó la respuesta en volver, que bajo el supuesto de simetría es la mitad.

> [!question]- ¿Importa que el reloj de P esté muy desfasado para medir $t_1 - t_0$?
> No, porque solo se usa la diferencia entre dos lecturas del mismo reloj. Un desfase constante se cancela. Lo que sí afecta es que el reloj de P avance a otra velocidad, aunque en un viaje corto ese efecto es despreciable.

> [!question]- P pregunta a las 10:00:00, S responde 10:05:00 y la respuesta llega a las 10:00:04. ¿A qué hora ajusta P su reloj?
> $10{:}05{:}00 + \frac{4}{2}\text{ s} = 10{:}05{:}02$.
