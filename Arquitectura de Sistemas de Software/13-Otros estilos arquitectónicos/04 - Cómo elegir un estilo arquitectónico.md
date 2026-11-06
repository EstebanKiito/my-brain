---
ramo: "Arquitectura de Sistemas de Software"
tema: "Otros estilos arquitectónicos"
tags:
  - arquisis/estilos
  - arquisis/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Peer to peer]]"
  - "[[04 - Microkernel]]"
  - "[[03 - Topologías mediator y broker y el estilo pub sub]]"
---

# Cómo elegir un estilo arquitectónico

¿Cuál es el estilo más apropiado? **Depende**: todos tienen sus tradeoffs. Esta nota reúne en tablas **cuándo sí, cuándo no y qué atributo favorece** cada estilo del curso, los consejos para elegir y la lista de estilos que las pautas suelen aceptar o rechazar. Sirve como resumen para repasar antes de la prueba.

## Tabla resumen de estilos

| Estilo | Cómo procesa | Cuándo sí | Cuándo no | Impacto en calidad |
|---|---|---|---|---|
| **Main y subrutinas** | Un problema que se descompone en problemas pequeños; el orden lo fija el main | Aplicación pequeña y simple | Estructuras de datos complejas; se modificará mucho | Performance (+), reusabilidad (+) |
| **Orientado a objetos** | Entidades que interactúan | Mapeo claro entre entidades del problema y objetos | Sistemas distribuidos en redes heterogéneas que exigen alto performance | Flexibilidad (+), integridad (+) |
| **Máquina virtual** | La data trae información de control que indica cómo procesarla | Una capa sirve de base para otras aplicaciones y su interfaz es estable | Se requieren varias capas y los datos se acceden desde varias | Portabilidad (+) |
| **Cliente-servidor** | El servidor centraliza y ejecuta procesos para varios clientes, que esperan la respuesta | Se pueden centralizar tareas; el cliente tiene procesamiento limitado | La centralización es un punto único de falla; ancho de banda limitado; muchos clientes compiten | Escalabilidad (+), flexibilidad (+) |
| **Por lotes, secuencial** | Un lote completo se procesa en una serie de transformaciones | Problema divisible en una secuencia de pasos | Se requiere interactividad, concurrencia o acceso aleatorio | Reusabilidad (+), modificabilidad (+), performance (no importa) |
| **Pipe and filter** | Transformaciones incrementales sobre un flujo continuo; pueden ser concurrentes | Filtros reusables; datos serializables | Se requiere interacción entre componentes | Escalabilidad (+), performance (+) |
| **Pizarra** | Programas independientes que se comunican solo a través de un repositorio global | Cálculos sobre datos compartidos que cambian; orden definido en ejecución | Partes independientes de los datos; la interfaz de datos puede cambiar | Escalabilidad (+), modificabilidad (+) |
| **Basado en reglas** | Hechos y reglas de una base de conocimiento para responder consultas | Problema expresable como reglas de inferencia simples | Muchísimas reglas con mucha interacción; se requiere gran performance | Escalabilidad (+), modificabilidad (+), performance (−) |
| **Intérprete** | Parsea y ejecuta un flujo de entrada y actualiza su estado | Conducta dinámica y mucha personalización | Se requiere alto performance | Portabilidad (+), modificabilidad (+), performance (−) |
| **Código móvil** | El código se mueve al host que lo ejecuta | Es más eficiente mover el proceso cerca de los datos; código local personalizado | No se puede garantizar la seguridad del código; se requiere un fuerte control de versiones | Modificabilidad (+), extensibilidad (+), performance (+) |
| **Pub/sub** | Un publicador difunde mensajes a suscriptores | Componentes débilmente acoplados; suscripciones pequeñas y fáciles de transportar | No hay middleware para muchos datos | Escalabilidad (+), flexibilidad (+), performance (+) |
| **Basado en eventos** | Componentes que emiten y reciben eventos de forma asíncrona | Componentes concurrentes, independientes y heterogéneos, distribuidos en red | Se requieren garantías de procesamiento de eventos en tiempo real | Escalabilidad (+), flexibilidad (+), performance (+) |
| **P2P** | Los peers guardan estado y actúan como clientes y servidores | Peers heterogéneos e independientes; robustez ante fallas; alta escalabilidad | No se puede garantizar la confiabilidad de los peers; hay nodos designados para descubrir recursos que pueden no estar disponibles | Escalabilidad (+), flexibilidad (+), performance (+) |

## Consejos para elegir

- **Entender el estándar del momento en la industria**, pero verificar si aplica al contexto propio: no se agrega blockchain a todo solo porque se use.
- **Tener conocimiento de dominio**: cómo se usará la aplicación, y cómo se transformarán y enviarán los datos.
- **No descartar la estructura de la organización**: un estilo puede ser muy caro de mantener. ¿Se podrá contratar más personal?
- **Reconocer situaciones similares:**
  - si el sistema requiere personalización por usuario, conviene un **microkernel**;
  - si debe ser sumamente escalable y sin acoplamientos, conviene **EDA**.
- **Preguntas finales:**
  - Si una sola quanta funciona, ¿se acepta ese riesgo?
  - ¿Dónde se almacenan los datos? ¿Una sola base de datos?
  - En los puntos clave, ¿la comunicación será síncrona o asíncrona?
- **No abarcar todo**: elegir solo los estilos principales. **Hay más de una solución posible**; lo importante es **justificar y convencer**.

## Lo que aceptan y rechazan las pautas

| Estilo | Aceptado cuando… | Rechazado cuando… |
|---|---|---|
| Pub/sub | Hay notificaciones o subidas masivas | Se requiere un mediador que coordine |
| EDA / workers | Hay tareas pesadas o muchas peticiones que encolar | — |
| Pipe and filter | Se **filtran** datos (duplicados, formato) | Se usa para **procesamiento** pesado |
| Cliente-servidor | Tiene una responsabilidad específica (un servicio de IA dedicado, una API única para lectores) | Solo se justifica con "hay front y back" |
| En capas | Hay secciones separadas por tipo de usuario | Restringe flexibilidad o escalabilidad sin necesidad |
| Microservicios | Se justifica la división del backend en subsistemas | No hay razón para dividir |
| P2P | Hay nodos equivalentes o no hay servidor central | Todos los sistemas son distintos |
| Main y subrutinas | — | Casi siempre: es bloqueante |
| Pizarra | Muchas fuentes de conocimiento sobre un problema común | No hay un motor de procesos con muchas fuentes |
| Código móvil | Hay distribución o ejecución de código en varios ambientes | No hay inyección ni traspaso de código |

## Preguntas de repaso

> [!question]- ¿Qué estilo conviene si cada usuario necesita personalizar el sistema con extensiones propias?
> Microkernel: un core estable al que se le agregan plugins por interfaces estandarizadas. Favorece la flexibilidad y la extensibilidad, a cambio de que el core sea un punto único de falla.

> [!question]- ¿Qué tres preguntas finales propone el curso antes de cerrar la elección de estilos?
> Si se acepta el riesgo de tener una sola quanta, dónde se almacenarán los datos (y si basta una base) y si la comunicación en los puntos clave será síncrona o asíncrona.

> [!question]- Según la tabla, ¿cuándo NO conviene pipe and filter?
> Cuando se requiere interacción entre los componentes o con el usuario: es un flujo unidireccional de transformaciones.

> [!question]- ¿Qué estilos tienen impacto negativo en la performance según la tabla?
> El basado en reglas y el intérprete: la inferencia sobre muchas reglas y la interpretación en tiempo de ejecución agregan costo.

> [!question]- ¿Por qué "no agregar blockchain a todo" es un consejo de elección de estilos?
> Porque un estilo de moda no se justifica solo porque la industria lo use. Debe responder a una necesidad del dominio (por ejemplo, un registro sin confianza central). Si no, se pagan su complejidad y su costo sin beneficio.

> [!question]- Mini caso: un sistema con secciones para caza-noticias (subidas masivas), validadores (revisión con IA) y lectores (lectura rápida). Proponga estilos con su responsabilidad.
> Capas, para separar las secciones por tipo de usuario. Pub/sub o EDA con workers, para recibir las subidas masivas y encolar las revisiones con IA. Pipe and filter, para filtrar duplicados y validar el formato de las noticias al subirse. Cliente-servidor o caché para los lectores, que acceden por una API de lectura.

> [!question]- V o F: "Una buena respuesta de estilos incluye todos los estilos que podrían aplicar".
> Falso. Conviene elegir solo los principales y justificar qué responsabilidad cubre cada uno. Además, cada estilo declarado debe aparecer en el diagrama, o se descuenta.
