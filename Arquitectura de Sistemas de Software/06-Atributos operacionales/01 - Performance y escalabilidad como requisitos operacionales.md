---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos operacionales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[02 - Portabilidad e interoperabilidad]]"
---

# Performance y escalabilidad como requisitos operacionales

Los **requisitos operacionales** influyen en el **runtime**: se manifiestan con la operación del negocio, según cómo se comporta el sistema frente a distintas situaciones, y **requieren varias iteraciones de ajuste**. No se pueden verificar leyendo el código: hay que medir el sistema funcionando. Esta nota presenta performance y escalabilidad a nivel de atributo. Su tratamiento en profundidad (métricas, tácticas, leyes) está en [[01 - Performance como atributo y sus métricas]] y en [[01 - Escalabilidad escenarios y cuellos de botella]].

## Performance

> [!tip] Performance (desempeño)
> **Carga de trabajo** que una aplicación debe ejecutar **en una unidad de tiempo**, y/o **plazos** (*deadlines*) que debe cumplir para operar correctamente. En pocas palabras: la velocidad del sistema.

**Cargas de trabajo típicas:** transacciones, mensajes, lecturas a la base de datos, actualizaciones de una base distribuida con commit de dos fases. La performance no se puede medir solo con el código: la complejidad $O(n)$ o $O(n^2)$ es una pista, pero lo que cuenta es el sistema completo funcionando.

| Métrica | Qué mide |
|---|---|
| **Throughput (salida)** | Carga de trabajo por unidad de tiempo, por ejemplo transacciones por segundo (tps), en peak y en promedio |
| **Tiempo de respuesta** | Latencia al procesar una carga: garantizada (límite) y promedio |
| **Deadline (plazo)** | Ventana de tiempo para completar una carga; si no se cumple, el sistema falla |
| **Capacidad** | Cuánta carga soporta |

**Escenario:** usuarios del SII (fuente) generan la carga peak de M req/s (estímulo) en horario peak (entorno) contra el servicio principal (artefacto); el sistema responde (respuesta) con **p95 < 500 ms y errores < 0,1%** (medición).

> [!warning] "Suena demasiado bien": performance no siempre es crítica
> - **Sobrepriorizarla perjudica otros atributos.** Un sistema muy veloz puede estar sacrificando confiabilidad, por ejemplo con una base que prefiere responder rápido antes que consistente.
> - **Depende del contexto:** ¿quizás 10 segundos es aceptable para generar un reporte mensual?
> - **Sin métricas específicas tiene escaso valor**: "que sea rápido" es casi idílico.
> - Se prioriza cuando el caso lo justifica, por ejemplo cuando la competencia gana por velocidad o el enunciado pide tiempos explícitos.

## Escalabilidad

> [!tip] Escalabilidad
> **Enfrentar el aumento de demanda de forma funcional**: pasar a 1, 100, 1 millón o 1.000 millones de usuarios en el tiempo.

**Métodos posibles:** balanceadores de carga, brokers, asincronía, y estilos y patrones adecuados.

| Métrica | Qué mide |
|---|---|
| **Requests** (cantidad de solicitudes) | Multi-thread y balanceo de carga: repartir solicitudes entre servidores o CPUs |
| **Conexiones concurrentes** | Cuántas conexiones simultáneas soporta |
| **Tamaño de datos** | Cuántos datos procesa en cada transacción, a medida que crecen los paquetes |
| **Deployment** (implantación) | Esfuerzo para distribuir, actualizar y configurar la aplicación cuando crecen los usuarios. Desplegar réplicas a mano es poco escalable |

La carga no es solo de peticiones: también puede ser de **datos**. Si el enlace es de 1 Gb y alguien envía 10 GB, el ancho de banda se llena y nadie más puede enviar.

**Costos de escalar:** la complejidad sube, se requieren esfuerzos de **coordinación** y puede requerirse **asincronía**.

> [!example]- Asincronía en JavaScript y su efecto en la escalabilidad
> Una **promesa** permite iniciar una operación asíncrona (una consulta, una llamada HTTP) y seguir ejecutando otras cosas mientras se resuelve. `await` le dice al programa "espera a que esta promesa termine antes de seguir con las líneas siguientes", sin bloquear el hilo para otras peticiones.
> ```javascript
> async function verPedido(id) {
>   const pedido = await db.pedidos.findById(id);   // libera el hilo mientras espera
>   return pedido;
> }
> ```
> Manejar mal las promesas (no esperarlas, no capturar sus errores o encadenarlas en serie sin necesidad) produce errores silenciosos y cuellos de botella cuando la carga crece.

## Preguntas de repaso

> [!question]- ¿Qué caracteriza a los requisitos operacionales?
> Se observan en tiempo de ejecución, con la operación del negocio. Dependen del comportamiento del sistema bajo distintas situaciones (carga, fallas) y requieren varias iteraciones de medición y ajuste.

> [!question]- Diferencie throughput, tiempo de respuesta y deadline.
> El throughput es cuánto trabajo se completa por unidad de tiempo (tps). El tiempo de respuesta es cuánto tarda en procesarse una carga (latencia). El deadline es el plazo máximo para completar una carga, que si se supera significa que el sistema falló.

> [!question]- ¿Por qué no siempre conviene priorizar la performance?
> Porque optimizarla puede sacrificar otros atributos (confiabilidad, consistencia, mantenibilidad), y en muchos contextos una respuesta más lenta es aceptable. Sin una métrica concreta, priorizarla tiene poco valor.

> [!question]- Nombre cuatro métricas de escalabilidad del curso.
> Cantidad de solicitudes (requests), conexiones concurrentes, tamaño de los datos por transacción y esfuerzo de despliegue o implantación al crecer.

> [!question]- ¿Qué costos trae escalar un sistema?
> Más complejidad, esfuerzos de coordinación entre componentes (balanceadores, sincronización de datos) y muchas veces la necesidad de asincronía, con todo lo que implica manejarla.

> [!question]- V o F: "La performance de un sistema se puede determinar analizando la complejidad algorítmica de su código".
> Falso. La complejidad es una pista, pero la performance depende del sistema completo funcionando: red, base de datos, concurrencia, carga real. Se mide en ejecución.

> [!question]- Mini caso: un sistema debe soportar el Cyber, donde la carga sube 20 veces a medianoche. ¿Qué atributo prioriza y qué métodos propone?
> Escalabilidad, junto con elasticidad por la subida repentina. Métodos: balanceador de carga con réplicas que se agregan automáticamente, colas o brokers para absorber picos, y asincronía para no bloquear con las tareas pesadas.
