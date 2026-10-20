---
ramo: "Sistemas Distribuidos"
tema: "Consistencia centrada en el cliente"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[05 - Consistencia eventual]]"
---

# Consistencia centrada en el cliente

Los modelos de consistencia vistos antes (fuerte, secuencial, causal, eventual) son **centrados en los datos**: buscan una vista coherente del sistema completo para todos los procesos a la vez, y eso exige sincronización costosa y alta latencia. Pero a un usuario no le importa lo que ven los demás, sino que **su propia** experiencia tenga sentido. Los modelos **centrados en el cliente** garantizan justo eso, de forma barata.

## Idea

- No buscan una vista global perfecta, sino la experiencia de **un cliente individual**.
- Ocultan inconsistencias de forma eficiente y económica.
- Aceptan una consistencia más relajada, pero aceptable para el usuario.

Son clave cuando un usuario accede a **réplicas distintas** a lo largo del tiempo, por ejemplo al viajar o al usar el celular y el computador. Aunque la consistencia global sea débil (eventual), la réplica con que interactúa el cliente debe estar al día con **los datos que ese cliente ya manipuló**.

## Garantías de sesión

Las **garantías de sesión** (Terry et al., 1994) definen expectativas razonables para un cliente que interactúa con el sistema en el tiempo. Son cuatro, y **no** tienen que cumplirse todas a la vez: se eligen según el caso de uso.

![Las cuatro garantías de sesión](adjuntos/Las%20cuatro%20garant%C3%ADas%20de%20sesi%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Se centran en la experiencia consistente de un cliente individual, no en una vista global del sistema. Incluyen cuatro propiedades: *Monotonic Reads*, *Read Your Writes*, *Monotonic Writes* y *Writes Follow Reads*.

| Garantía | Intuición |
|---|---|
| **Monotonic reads** | Una vez que viste algo, no verás una versión anterior |
| **Read your writes** | Si escribiste algo, puedes leerlo de inmediato |
| **Monotonic writes** | Tus escrituras siguen una progresión lógica |
| **Writes follow reads** | Si modificas lo que leíste, tu cambio se basa en esa versión |

## Notación

- $X_z$: versión $z$ del dato $X$.
- $W_q(X_1 \rightarrow X_2)$: el nodo $q$ escribe la versión $X_2$ **sabiendo** que existe $X_1$.
- $W_q(X_1 \mid X_n)$: el nodo $q$ escribe $X_n$ **concurrentemente** con $X_1$, sin conocerla, lo que puede generar un conflicto de versiones.

## Por qué importa

- La sensación de confiabilidad depende de que las acciones del usuario tengan efecto **visible y coherente**: "lo que hice se guardó" y "lo que veo tiene sentido".
- La consistencia eventual sola **no basta** para una buena experiencia.
- Compromiso práctico: no siempre se puede ofrecer consistencia fuerte global, pero sí una experiencia consistente para cada cliente.

> [!warning] Fallas típicas
> - **Read your writes:** publicas un comentario, recargas y no aparece; piensas que debes escribirlo de nuevo.
> - **Monotonic reads:** ves un correo nuevo en el celular, abres la versión web y el correo no está.
> - **Monotonic writes:** envías un mensaje desde el PC, lo editas en el celular, y al editar de nuevo en el PC la edición se basa en la versión original.
> - **Writes follow reads:** ves una reunión el martes y propones moverla al miércoles, sin saber que alguien ya la había movido.

## Preguntas de repaso

> [!question]- ¿En qué se diferencian los modelos centrados en datos de los centrados en el cliente?
> Los primeros garantizan una vista coherente del sistema para todos los procesos a la vez; los segundos solo garantizan que la experiencia de cada cliente individual sea coherente, lo que es mucho más barato.

> [!question]- ¿Por qué estas garantías son relevantes con consistencia eventual?
> Porque la consistencia eventual permite que un cliente que cambia de réplica vea datos más viejos o pierda sus propios cambios. Las garantías de sesión ocultan esas inconsistencias para ese cliente.

> [!question]- ¿Qué significa $W_B(X_1 \mid X_2)$?
> Que B escribió la versión $X_2$ sin conocer $X_1$, de forma concurrente con ella.
