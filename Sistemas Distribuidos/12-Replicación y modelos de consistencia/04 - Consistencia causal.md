---
ramo: "Sistemas Distribuidos"
tema: "Replicación y modelos de consistencia"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[02 - Consistencia secuencial]]"
  - "[[02 - Relojes vectoriales]]"
---

# Consistencia causal

¿Hace falta que todos vean **todas** las operaciones en el mismo orden? A menudo no: basta con que nadie vea una respuesta antes que la pregunta. La **consistencia causal** (Hutto y Ahamad, 1990) debilita la secuencial: solo exige el mismo orden para las operaciones **relacionadas causalmente**, y deja libres las concurrentes.

## Definición

> [!tip] Regla
> Si un evento B fue **causado** por un evento A (por ejemplo, B escribe después de leer lo que escribió A), todos los nodos deben ver **primero A y luego B**. Un evento C **concurrente**, sin relación causal, puede aparecer en distintas posiciones para distintos nodos.

Es la misma relación "sucedió antes" de los [[01 - Relojes lógicos de Lamport|relojes lógicos]], y los [[02 - Relojes vectoriales|relojes vectoriales]] son la forma natural de implementarla.

## Ejemplo: un foro

1. La persona 1 publica un post sobre **memes**.
2. La persona 2 **lee** ese post y lo **comenta**.
3. La persona 3 publica un post sobre **anime**.

Todos deben ver el post de memes **antes** que su comentario (el comentario fue causado por el post). El post de anime no tiene relación causal con ellos, así que cada usuario puede verlo antes o después.

## Causal pero no secuencial

![Ejecución causal pero no secuencial](adjuntos/Ejecuci%C3%B3n%20causal%20pero%20no%20secuencial.png)

> [!example]- Transcripción de la imagen
> A escribe $W_A(x)=2$ y luego $W_A(x)=5$. F lee $R_F(x)\rightarrow 2$ y luego escribe $W_F(x)=9$. H lee 2, 5 y 9; S lee 2, 9 y 5. "Nodos H y S ven los write en órdenes distintos → no es consistente secuencial. Nodo F leyó la escritura de A (x=2) antes de escribir él (x=9). Solo se exige que se respete que 2 viene antes de 9. Si algún nodo lee el 2 después del 9, se rompe la consistencia causal."

- $W_A(x)=2 \rightarrow W_F(x)=9$ (F leyó el 2 antes de escribir), y $W_A(x)=2 \rightarrow W_A(x)=5$ (mismo proceso).
- $W_A(x)=5$ y $W_F(x)=9$ son **concurrentes**: H y S pueden verlos en órdenes distintos.

## Qué valores son posibles

![Valores posibles bajo consistencia causal](adjuntos/Valores%20posibles%20bajo%20consistencia%20causal.png)

> [!example]- Transcripción de la imagen
> A escribe $z=1$, $z=2$, $XX=2$ y más tarde $z=9$. F escribe $z=4$, lee $XX\rightarrow 2$ y escribe $Y=9$. H lee $Y\rightarrow 9$ y luego $z$. ¿Qué valor puede tener $z$? 1: ❌; 2: ✅; 4: ✅; 9: ❓ (la consistencia no dice nada); NULL: ❌.

Como H leyó $Y=9$, y F escribió $Y$ después de leer $XX=2$, que A escribió después de $z=2$, la cadena causal obliga a H a haber visto $z=2$. Por eso:

- **NULL o 1:** imposibles, porque $z=2$ ya debe ser visible y es posterior a $z=1$.
- **2 o 4:** posibles. $z=4$ es concurrente con las escrituras de A.
- **9:** el modelo no lo exige ni lo prohíbe; depende de si $W_A(z)=9$ ya llegó.

Con un caso más simple: si A escribe $x=2$, F lee ese 2 y escribe $z=4$, y H lee $z=4$, entonces al leer $x$ puede obtener 2, pero **no** un valor sin definir.

> [!warning] Lo causal se hereda
> Una escritura arrastra a todas las que la causaron, aunque sean de otras variables. Leer $Y$ obligó a H a ver el $z=2$ de A.

## Preguntas de repaso

> [!question]- ¿Qué diferencia a la consistencia causal de la secuencial?
> La secuencial exige que todos vean todas las operaciones en el mismo orden. La causal solo lo exige para las relacionadas causalmente; las concurrentes pueden verse en órdenes distintos.

> [!question]- En el foro, ¿qué violaría la consistencia causal?
> Que un usuario viera el comentario de la persona 2 antes que el post de memes que comentó.

> [!question]- ¿Por qué $W_A(x)=5$ y $W_F(x)=9$ pueden verse en distinto orden?
> Porque son concurrentes: F escribió 9 después de leer el 2, no el 5, así que no hay relación causal entre ambas escrituras.
