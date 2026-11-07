---
ramo: "Arquitectura de Sistemas de Software"
tema: "Asincronía y control de demanda"
tags:
  - arquisis/performance
  - arquisis/casos
  - origen/complemento
prerrequisitos:
  - "[[03 - Tácticas de performance de Bass y Kazman]]"
  - "[[03 - Caso Amazon Prime Video de microservicios a monolito]]"
---

# Contenedores y el caso Twitter

Dos ideas del stack ayudan a entender cómo crecen los sistemas: los **contenedores**, que permiten aprovechar mejor las máquinas, y la historia de **Twitter**, que pasó de un monolito en Rails que se caía a cientos de servicios. El caso muestra la secuencia típica: primero se lanzan máquinas al problema, después se rediseña, y al final hay que pagar la complejidad que trae el rediseño.

## Contenedores y performance

- **Mejor utilización de recursos:** varias aplicaciones comparten una máquina o VM, así que se usa toda su capacidad en vez de dejar servidores medio vacíos.
- **La aislación permite *commoditizar* el hardware:** cualquier máquina sirve para correr cualquier contenedor.
- **Mejora la escalabilidad:** se levantan más contenedores de lo que necesita escalar, en segundos.

## Twitter en 2007: el monolito saturado

| 2007 | 2013-2015 |
|---|---|
| 600 peticiones por segundo | Récord de 143.199 tweets por segundo (2013) |
| 180 instancias de Rails | 500 millones de tweets al día |
| 1 base MySQL + 1 réplica (*slave*) | Más de 230 millones de usuarios activos |
| 30 procesos varios, 8 máquinas Sun X4100 | Más de 100 proyectos open source y más de 75 idiomas |

![Pageviews diarios de twitter.com entre mediados de 2006 y abril de 2007](adjuntos/Pageviews%20diarios%20de%20Twitter%20en%202006%20y%202007.png)

> [!example]- Transcripción de la imagen
> - Gráfico de Alexa: *Daily Pageviews (per million)* de twitter.com.
> - Casi plano en cero desde julio hasta octubre de 2006, con un crecimiento leve hasta enero de 2007.
> - Desde marzo de 2007 sube casi verticalmente y llega a unas 120 páginas por millón en abril.

**Estado inicial:** una gran aplicación en Rails.
- Se resolvía **lanzando más máquinas al problema** en vez de dar una solución de ingeniería.
- Había una tensión entre **optimizar el código** y mantener la **legibilidad y flexibilidad**.
- **Los recursos de las máquinas eran el cuello de botella**. Era la época de la "ballena", la página de error de Twitter caído.

## La transición

- **Cambio de la VM de Ruby a la JVM**, y luego a **Scala**: el buscador en Java con Lucene y FlockDB para el grafo social en Scala.
- La buena experiencia llevó a **migrar todo a servicios aislados**: Tweet, User, Timeline, DM y Social Graph.
- Cada servicio pudo escalar, optimizarse y desplegarse por separado según su carga. El timeline, por ejemplo, tiene un patrón de lectura muy distinto al de escribir tweets.

## Elevar la complejidad trae consecuencias

Años después, la arquitectura de servicios tenía otro problema: **puede que los recién llegados no la entiendan, o que se arrastre complejidad** que ya nadie justifica.

![Tweets sobre apagar microservicios y la latencia de la app en India](adjuntos/Tweets%20sobre%20microservicios%20y%20latencia%20en%20Twitter.png)

> [!example]- Transcripción de la imagen
> - Primer tweet (14 de noviembre de 2022): "Part of today will be turning off the 'microservices' bloatware. Less than 20% are actually needed for Twitter to work!"
> - Segundo tweet: "I was told ~1200 RPCs independently by several engineers at Twitter, which matches # of microservices." Luego: "Same app in US takes ~2 secs to refresh (too long), but ~20 secs in India, due to bad batching/verbose comms. Actually useful data transferred is low." El fragmento "~20 secs in India" está destacado en rojo.

El segundo tweet es un problema de performance clásico: **~1.200 llamadas RPC** para refrescar la app, con **mal batching y comunicación verbosa**. En Estados Unidos la latencia acumulada daba unos 2 s. En India, con más latencia de red, daba unos 20 s, porque **la latencia de cada salto se multiplica por la cantidad de saltos**. Son las falacias de la red otra vez.

> [!tip] Lo que enseñan Twitter y Prime Video juntos
> - Twitter **partió** el monolito porque los recursos y la escala lo exigían.
> - Prime Video **juntó** un subsistema porque la red y la orquestación costaban demasiado.
> No hay una arquitectura correcta en abstracto: hay que **medir** y poner las fronteras donde la cadencia, la escala o las fallas lo justifican, sin multiplicar los saltos de red.

## Preguntas de repaso

> [!question]- ¿Cómo mejoran los contenedores la utilización de recursos?
> Permiten que varias aplicaciones aisladas compartan una misma máquina o VM, aprovechando toda su capacidad. Como el contenedor aísla la aplicación, el hardware se vuelve intercambiable y se escala levantando más contenedores en segundos.

> [!question]- ¿Qué significa "lanzar máquinas al problema" y por qué no bastó en Twitter?
> Es escalar agregando servidores sin cambiar el diseño. No bastó porque el cuello de botella era estructural: un monolito en Rails sobre una sola base MySQL no escalaba al crecimiento explosivo, y más máquinas de aplicación solo trasladaban la presión a la base y al runtime.

> [!question]- ¿Qué cambios técnicos hizo Twitter en su transición?
> Pasó partes críticas de la VM de Ruby a la JVM y Scala (búsqueda con Lucene, FlockDB para el grafo social), y separó el sistema en servicios aislados: Tweet, User, Timeline, DM y Social Graph.

> [!question]- Explique, con las falacias de la red, por qué la app tardaba unos 2 s en Estados Unidos y unos 20 s en India.
> Refrescar implicaba cerca de 1.200 llamadas RPC con mal batching. Como la latencia no es cero, cada llamada suma su latencia, y con más latencia por salto (India está más lejos de los servidores) el total se multiplica. El problema no era el ancho de banda, porque se transfería poca información útil.

> [!question]- ¿Qué medidas habrían reducido el tiempo de refresco de 20 s?
> Agrupar llamadas (batching), un endpoint agregador o una API Gateway que componga la respuesta del lado del servidor, paralelizar las llamadas independientes y cachear o servir desde regiones cercanas. Así se reduce el número de viajes de ida y vuelta por la red.

> [!question]- V o F: "El caso Twitter demuestra que pasar a microservicios siempre mejora la performance".
> Falso. La separación resolvió problemas de escala y de recursos del monolito, pero años después la cantidad de servicios y llamadas generó problemas de latencia y de complejidad. Cada frontera tiene costo.

> [!question]- ¿Qué consecuencia organizacional tiene "elevar la complejidad"?
> Los recién llegados no entienden el sistema, se arrastra complejidad que ya nadie justifica y cuesta saber qué servicios son realmente necesarios. Eso frena el desarrollo y hace más difícil optimizar.
