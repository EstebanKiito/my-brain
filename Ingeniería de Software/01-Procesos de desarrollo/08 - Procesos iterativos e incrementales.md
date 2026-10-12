---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/apuntes]
prerrequisitos: ["[[03 - Procesos iterativos|Procesos iterativos]]", "[[07 - Procesos incrementales|Procesos incrementales]]"]
---
# Procesos iterativos e incrementales

Un proceso iterativo e incremental combina los dos enfoques: cada entrega **agrega funcionalidades nuevas** y **mejora las que ya existen**. Así el usuario recibe valor desde temprano y el producto se adapta al feedback.

## Características
- Con cada entrega **añadimos funcionalidades nuevas** (**INCREMENTAL**).
- Cada incremento incluye **mejoras sobre funcionalidades ya existentes** (**ITERATIVO**).

![Procesos iterativos e incrementales - analogía de la Mona Lisa](adjuntos/Procesos%20iterativos%20e%20incrementales%20-%20analogía%20de%20la%20Mona%20Lisa.png)

> [!note]- Qué muestra la imagen
> Se combinan los dos enfoques. En cada paso se agrega una parte nueva del cuadro (incremental) y se refinan las ya pintadas (iterativo), pasando por seis estados hasta la obra terminada.

## Ventajas
- **Adaptación**, evitando hacer cosas que no se deban hacer.
- **¡Entrega de valor al usuario antes de acabar el desarrollo!**

![Procesos iterativos e incrementales - del skate al auto](adjuntos/Procesos%20iterativos%20e%20incrementales%20-%20del%20skate%20al%20auto.png)

> [!note]- Qué muestra la imagen
> - **"Not like this":** se entrega una rueda, luego un eje, luego un chasis y recién al final un auto. El usuario está descontento hasta el último paso, porque nada le sirve antes.
> - **"Like this!":** skate → scooter → bicicleta → moto → auto. **Cada entrega ya le sirve al usuario para moverse** y su satisfacción crece en cada paso.

## Desventajas
- Pudiera ser que, en función del feedback recibido, tuviéramos que **deshacer algo ya construido**, con el consiguiente **sobrecoste**.
- Como queremos entregar incrementos de software frecuentemente, **o automatizamos también nuestro proceso** para poner el software funcionando a disposición de los usuarios, **o vamos a incurrir en otro importante sobrecoste** (no sólo en tiempo, sino también en errores provocados por las personas, que no somos tan buenos como las máquinas para hacer tareas repetitivas).

> [!tip] Complemento (libro del curso, cap. 2.4, y slides "Procesos de Desarrollo de Software")
> - Cada iteración genera un **aumento de valor tangible** para el cliente, con funcionalidades **listas para usar**. El producto está completo con el último incremento.
> - Los incrementos suelen corresponder a uno o más **relatos (historias) de usuario** nuevos.
> - Los procesos iterativos e incrementales suelen llamarse **ágiles**; ver [[09 - Metodologías ágiles y manifiesto ágil|Metodologías ágiles y manifiesto ágil]].
>
> ![Slide - enfoque iterativo e incremental](adjuntos/Slide%20-%20enfoque%20iterativo%20e%20incremental.png)
> *Analogía de las slides: la zanja se rellena con ladrillos (incrementos) y cada ladrillo se ajusta con el cincel (iteraciones).*

> [!tip] Complemento — cómo se mitiga la segunda desventaja
> La automatización que mencionan los apuntes corresponde, en la práctica, a la **integración continua** (compilar y correr las pruebas automáticamente en cada cambio) y al **despliegue continuo** (publicar automáticamente cada versión que pasa las pruebas). Por eso las pruebas automatizadas son tan importantes en los procesos ágiles. Ver también [[10 - Programación extrema (XP)|Programación extrema (XP)]].

## Preguntas de repaso

1. ¿Qué parte del proceso es "incremental" y qué parte es "iterativa"?
> [!question]- Respuesta
> Incremental: en cada entrega se agregan funcionalidades nuevas. Iterativa: cada incremento también mejora funcionalidades que ya existían.

2. ¿Cuál es la gran ventaja para el usuario?
> [!question]- Respuesta
> Recibe valor (software usable) antes de que termine el desarrollo, y el producto se adapta a su feedback evitando construir cosas innecesarias.

3. Explica la imagen del skate y el auto.
> [!question]- Respuesta
> Entregar piezas sueltas (rueda, eje, chasis) no le sirve al usuario hasta el final. Entregar algo usable en cada paso (skate, scooter, bicicleta, moto, auto) le da valor desde la primera entrega y permite ajustar el rumbo con su feedback.

4. ¿Qué dos sobrecostos pueden aparecer y cómo se mitiga el segundo?
> [!question]- Respuesta
> (1) Deshacer algo ya construido por el feedback. (2) El costo de entregar seguido, en tiempo y en errores humanos en tareas repetitivas. El segundo se mitiga automatizando: pruebas automáticas, integración y despliegue continuos.
