---
ramo: "Arquitectura de Sistemas de Software"
tema: "Cohesión acoplamiento y connascence"
tags:
  - arquisis/fundamentos
  - arquisis/connascence
  - origen/complemento
prerrequisitos:
  - "[[02 - Connascence estática]]"
---

# Connascence dinámica y reglas de grado y localidad

La connascence **dinámica** solo es **observable al ejecutar el sistema**. Es más fuerte y más difícil de trabajar que la estática, porque el compilador no la detecta: aparece como un error intermitente en producción. En arquitectura es la más importante, porque los componentes distribuidos se coordinan en tiempo de ejecución.

## Los cuatro tipos dinámicos

**Execution (ejecución).** El **orden de ejecución** del código importa. Un lock en threads es connascence de ejecución.

![Diagrama de secuencia con lecturas y escrituras de A y B](adjuntos/Connascence%20de%20ejecución%20en%20lecturas%20y%20escrituras.png)

> [!example]- Transcripción de la imagen
> - Croquis de secuencia con una base de datos a la izquierda y dos sistemas, **A** y **B**.
> - A hace `Get 1` y recibe el dato. Luego hace `Write 1` con información nueva y recibe confirmación. Al hacer otro `Get`, debe recibir el valor nuevo.
> - B intenta también un `Write` entre medio (marcado con una X): si el orden no se respeta, A lee un valor que no esperaba.

Si A lee, modifica y escribe, y B escribe entre medio, el resultado depende del orden. Hay que **mantener el orden de ejecución**, con transacciones o locks.

**Timing (tiempo).** El **momento** en que se ejecutan varios componentes importa. Ejemplo: un servicio asume que el otro responde en menos de 2 s, o dos procesos deben terminar antes de que empiece un tercero (las *race conditions*).

**Value (valor).** **Varios valores deben cambiar en conjunto** durante la ejecución.

![Rectángulo cuyas cuatro esquinas deben moverse juntas](adjuntos/Connascence%20de%20valor%20en%20las%20esquinas%20de%20un%20rectángulo.png)

> [!example]- Transcripción de la imagen
> - Un rectángulo con sus cuatro esquinas marcadas, y líneas punteadas que salen de cada esquina hacia afuera.
> - Si se mueve una esquina, las demás deben moverse también para que siga siendo un rectángulo.

Ejemplo en sistemas: el stock en Inventario y la reserva en Checkout. Si cambia uno y el otro no, el sistema queda inconsistente. Varios sistemas se ponen de acuerdo en un valor, y si uno cambia, los demás deben ajustarse.

**Identity (identidad).** Varios componentes deben **referirse a la misma instancia** de una entidad.

![Dos sistemas que comparten un broker o una base de datos](adjuntos/Connascence%20de%20identidad%20con%20broker%20o%20base%20compartida.png)

> [!example]- Transcripción de la imagen
> - Izquierda: los componentes **A** y **B** conectados al mismo **Broker**, con la anotación "E0".
> - Derecha: **A** y **B** conectados a la misma **base de datos**.

A y B deben usar **la misma instancia** del broker o de la base para compartir los mismos datos. Si uno apunta a otra instancia, todo "funciona", pero ven datos distintos. Es la connascence más fuerte.

## El ejemplo de recetas e ingredientes

![Componentes Recipes e Ingredients con interfaces en ambas direcciones](adjuntos/Ejemplo%20de%20connascence%20entre%20recetas%20e%20ingredientes.png)

> [!example]- Transcripción de la imagen
> - Dos componentes, **Recipes** e **Ingredients**, unidos por dos interfaces, una en cada sentido.
> - Texto: "Una receta se ejecuta llamando a sus ingredientes, mientras que los ingredientes pueden llamar a su receta al momento de ejecutarse." Pregunta: "¿De qué tipo es su connascence?"

La dependencia es **circular**: cada lado conoce y llama al otro. Además de la connascence estática de nombre y tipo, hay connascence dinámica de **ejecución**, porque importa quién llama primero y la ejecución de uno depende de la del otro. Si se modifica algo en Ingredientes, hay que modificar Recetas, y viceversa.

![Servicio RecipeIngredient entre recetas e ingredientes](adjuntos/Servicio%20RecipeIngredient%20que%20reduce%20la%20connascence.png)

> [!example]- Transcripción de la imagen
> - Un nuevo componente **«service» RecipeIngredient** arriba, con dos interfaces provistas.
> - **«component» Recipes** e **«component» Ingredients** dependen cada uno de RecipeIngredient y ya no se llaman entre sí.

**Mejora:** extraer un componente externo (`RecipeIngredient`) que coordina la relación. Recipes e Ingredients dependen de él, pero no entre sí. ¿En verdad queríamos hacerlo? **Pro:** un cambio ya no destruye todo. **Contra:** más código que mantener.

## Reglas para manejar la connascence (Jim Weirich)

> [!tip] Rule of degree
> **Convertir formas fuertes de connascence en formas más débiles.** Por ejemplo, la de significado en la de nombre con enums, la de posición en la de nombre con argumentos con nombre, y la de identidad en la de valor con eventos.

> [!tip] Rule of locality
> **Mientras más distantes estén los elementos, más débil debe ser su connascence.** Dentro de una clase se tolera connascence fuerte. Entre servicios de equipos distintos, solo la más débil posible (nombre o tipo, vía un contrato).

Si dos componentes muy alejados comparten una connascence fuerte, un cambio en uno desencadena una larga cadena de cambios intermedios. Se busca siempre la connascence más **"deseable"**: la de menor grado y lo más simple posible.

## Preguntas de repaso

> [!question]- ¿Por qué la connascence dinámica es más difícil de manejar que la estática?
> Porque solo aparece al ejecutar el sistema: el compilador o el IDE no la detectan, y suele manifestarse como errores intermitentes que dependen del orden, el tiempo o el estado compartido.

> [!question]- Dos servicios deben apuntar a la misma base de datos para ver los mismos pedidos. ¿Qué connascence tienen?
> Connascence de identidad: deben referirse a la misma instancia. Es la más fuerte, porque si uno apunta a otra instancia el sistema funciona pero con datos distintos, sin errores visibles.

> [!question]- Diferencie la connascence de timing y la de ejecución.
> La de ejecución exige un orden (A antes que B). La de timing exige que las cosas ocurran dentro de cierto tiempo o al mismo tiempo: un timeout que asume que el otro responde en menos de 2 s, o una carrera entre dos procesos.

> [!question]- Explique la rule of degree y la rule of locality.
> Rule of degree: convertir las formas fuertes de connascence en formas más débiles. Rule of locality: mientras más lejanos estén los componentes, más débil debe ser su connascence, porque los cambios entre componentes lejanos se propagan por largas cadenas y son más caros.

> [!question]- ¿Qué tipo de connascence hay entre Recipes e Ingredients y cómo se mejora?
> Hay una dependencia circular: connascence estática de nombre y tipo, y dinámica de ejecución, porque cada uno llama al otro y el orden importa. Se mejora extrayendo un servicio RecipeIngredient del que ambos dependen sin llamarse entre sí. A cambio, hay más código que mantener.

> [!question]- Dé un ejemplo de connascence de valor entre dos servicios de un e-commerce y cómo mitigarla.
> El stock de Inventario y las reservas de Checkout deben cambiar juntos: si se confirma un pedido, el stock debe bajar. Se mitiga con un evento `PedidoConfirmado` que Inventario procesa, o protegiendo ambos valores en un mismo agregado o transacción si deben ser ciertos a la vez.

> [!question]- V o F: "Según la rule of locality, dos microservicios de equipos distintos pueden compartir tranquilamente la misma base de datos".
> Falso. Compartir la base es connascence de identidad, la más fuerte, entre componentes lejanos. La rule of locality pide que entre componentes distantes haya solo connascence débil, como un contrato de API o eventos con esquema.
