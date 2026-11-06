---
ramo: "Arquitectura de Sistemas de Software"
tema: "Fundamentos de performance"
tags:
  - arquisis/performance
  - origen/complemento
prerrequisitos:
  - "[[05 - Cómo elegir el mecanismo de integración]]"
---

# Performance como atributo y sus métricas

Los productos digitales alcanzan millones de usuarios en meses, no en décadas. Un sistema que responde bien con 100 usuarios puede volverse inutilizable con 100.000. **Performance** es el atributo que mide si el sistema hace su trabajo **a tiempo** con la carga que recibe. Para razonar sobre él hacen falta una definición precisa y métricas concretas.

![Años que tardaron distintos productos en llegar a 50 millones de usuarios](adjuntos/Años%20que%20tardaron%20productos%20en%20llegar%20a%2050%20millones%20de%20usuarios.png)

> [!example]- Transcripción de la imagen
> - Título: *Number of years it took for each product to gain 50 million users*.
> - Fila superior: aerolíneas 68 años, automóviles 62, teléfono 50, electricidad 46, tarjeta de crédito 28, televisión 22, cajeros automáticos 18, computador 14, celular 12.
> - Fila inferior: tarjetas de débito 12 años, Internet 7, PayPal 5, iPods 4, YouTube 4, Facebook 3, Twitter 2, Instagram 17 meses y Pokémon Go 19 días.

## Definición

> [!tip] Performance
> Atributo de calidad **operacional**, observable cuando el sistema **está en ejecución**. Es la **carga de trabajo que una aplicación debe ejecutar en una unidad de tiempo** y/o los **plazos (*deadlines*) que debe cumplir** para operar correctamente.

Es la capacidad del software para dar una respuesta y ejecutar sus tareas, y **depende de la comunicación e interacción entre sus componentes**. Por eso es un tema de arquitectura y no solo de código: cada salto por la red, cada intermediario y cada capa suma tiempo.

## Estrategias de optimización

- **Determinar responsabilidades**, para saber a quién apuntar cuando algo es lento.
- **Modelos de coordinación**: cómo se sincronizan los componentes (timings, connascence de ejecución y de tiempo).
- **Tácticas** de Bass y Kazman: manejo de recursos y control de la demanda.
- **Interdependencias**: connascence y acoplamiento entre componentes.
- **Elección del stack**: cada tecnología apunta a problemas distintos. En lenguajes, Go, Rust, Node o Scala; en frameworks, NestJS, Spring o Ruby on Rails.

## Métricas clave (*fitness*)

| Métrica | Qué mide | Ejemplo |
|---|---|---|
| **Throughput** | Trabajo por unidad de tiempo: peticiones, respuestas o errores por segundo | 1.200 req/s |
| **Bandwidth** | Capacidad de transferencia de la red | 1 Gbps |
| **Latencia** | Tiempo de respuesta, en ms o s | p99 = 300 ms |
| **Jitter** | Variación de la latencia entre peticiones | ±40 ms |
| **Capacidad de conexiones** | Cuántas conexiones simultáneas soporta | 10.000 websockets |
| **Utilización de recursos** | CPU, RAM, accesos a la base de datos, uptime, pausas del recolector de basura | CPU al 85% |
| **Escalabilidad** | Cómo cambian las métricas al crecer la carga | Ver el tema de escalabilidad |

### Percentiles: por qué el promedio engaña

La latencia se reporta en **percentiles**: **p50** (la mediana), **p95** y **p99** (el 99% de las peticiones tarda menos que ese valor). Con 10 peticiones de 20, 22, 25, 25, 30, 31, 35, 40, 120 y 800 ms:
- el **promedio** es 114,8 ms, un valor que no describe a nadie;
- el **p50** es unos 30 ms, lo que vive el usuario típico;
- el **p99** queda cerca de 800 ms, lo que vive el peor caso.

Los usuarios más activos hacen muchas peticiones, así que casi seguro les toca alguna del extremo. Por eso los objetivos se fijan en p95 o p99.

## El escenario de performance

Un requisito de performance se escribe como un **escenario** medible:

| Parte | Ejemplo: dashboard de métricas en un satélite |
|---|---|
| **Fuente y estímulo** | Los 8 equipos de análisis publican métricas continuamente |
| **Ambiente** | Operación normal, con los 8 equipos escribiendo |
| **Respuesta** | La métrica procesada aparece en el dashboard |
| **Medida** | **p99 < 2 s** entre que se procesa la métrica y que se muestra |

Tácticas para cumplirlo, cada una con lo que sacrifica:
- **Push desde un event bus en vez de polling:** baja la latencia, a cambio de mantener conexiones abiertas y más complejidad.
- **Priorizar los eventos críticos:** a cambio, los de baja prioridad se atrasan.
- **Evitar lecturas separadas por cada panel:** agregar las métricas antes de enviarlas reduce viajes, a cambio de precalcular.

> [!warning] "El sistema debe ser rápido" no es un requisito
> Sin una **medida** (p99 < 2 s, 500 req/s con error < 0,1%) no se puede verificar ni diseñar. En la prueba, un escenario sin medida cuantitativa pierde puntos.

## Preguntas de repaso

> [!question]- ¿Por qué performance es un atributo operacional y no estructural?
> Porque solo se observa con el sistema en ejecución, bajo una carga concreta: depende de cómo interactúan los componentes en tiempo real. Uno estructural, como la mantenibilidad, se evalúa mirando el código y su organización.

> [!question]- Diferencie throughput y latencia con un ejemplo donde uno mejore y el otro empeore.
> El throughput es cuánto trabajo se hace por unidad de tiempo, y la latencia es cuánto tarda cada petición. Si se agrupan escrituras en lotes de 1.000, el throughput sube (menos viajes a la base de datos), pero cada escritura individual espera a que se llene el lote, así que su latencia empeora.

> [!question]- Con latencias de 20, 22, 25, 25, 30, 31, 35, 40, 120 y 800 ms, ¿por qué reportar el promedio es engañoso?
> El promedio da 114,8 ms, un valor que no corresponde a ninguna petición: la mayoría tarda unos 30 ms y una tarda 800 ms. Los percentiles separan la experiencia típica (p50 ≈ 30 ms) del peor caso (p99 ≈ 800 ms), que es el que se fija como objetivo.

> [!question]- ¿Qué es el jitter y en qué tipo de sistema importa más?
> Es la variación de la latencia entre peticiones. Importa sobre todo en streaming, videollamadas o juegos en línea, donde una latencia irregular produce cortes aunque el promedio sea bueno.

> [!question]- Escriba un escenario de performance completo para el pago en un e-commerce.
> Fuente y estímulo: un usuario confirma el pago. Ambiente: hora peak, con 2.000 usuarios simultáneos. Respuesta: el sistema confirma o rechaza la transacción. Medida: p95 < 1,5 s y menos del 0,1% de errores.

> [!question]- V o F: "Elegir el stack tecnológico no es una decisión de performance, porque todos los lenguajes modernos son igual de rápidos".
> Falso. Cada tecnología apunta a problemas distintos: Node es muy bueno con muchas conexiones de I/O pero malo con cálculo intensivo en CPU, y Go o Rust rinden mejor en servicios intensivos. El stack es una de las estrategias de optimización.

> [!question]- ¿Por qué se dice que la performance "depende de la comunicación entre componentes"?
> Porque en un sistema distribuido gran parte del tiempo de respuesta se va en llamadas entre componentes: red, serialización, intermediarios y esperas. Una arquitectura con muchos saltos puede ser lenta aunque cada componente sea rápido.
