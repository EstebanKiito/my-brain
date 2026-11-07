---
ramo: "Arquitectura de Sistemas de Software"
tema: "Hardware red y performance"
tags:
  - arquisis/performance
  - arquisis/red
  - origen/complemento
prerrequisitos:
  - "[[01 - Hardware y performance]]"
  - "[[03 - Desafíos de los sistemas distribuidos]]"
---

# Las falacias de la red y la performance

Cuando un sistema sale del monolito, cada llamada entre componentes pasa por la red. La red tiene **ancho de banda** y **latencia** limitados, tanto entre servidores como hacia los usuarios, y además sufre **congestión** y **pérdida de paquetes**, incluso dentro de la misma nube. Las **falacias de la computación distribuida** son los supuestos falsos que los diseñadores hacen sin darse cuenta.

## Las falacias (FOSA)

| Falacia | La realidad | Consecuencia en performance |
|---|---|---|
| **La red es confiable** | Se pierden paquetes incluso en la nube; las instancias caen de repente; las respuestas se pierden | Reintentos, timeouts y duplicados que agregan latencia y carga |
| **La latencia es cero** | Cada salto cuesta milisegundos | Encadenar peticiones suma latencias; aparecen problemas de concurrencia. Una SAGA o un mediator mal configurados pueden multiplicar los viajes |
| **El ancho de banda es infinito** | Es limitado, sobre todo al salir del monolito | Mover archivos pesados entre servicios satura la red |
| **La red es segura** | No todos los actores son confiables, menos en internet | Firewalls, TLS y autenticación agregan overhead |
| **La topología no cambia** | El movimiento de datos y el ruteo cambian y son impredecibles | Latencias variables (jitter) y rutas más largas |
| **El costo de transporte es cero** | Serializar y transferir cuesta; en la nube se cobra explícitamente | La salida de datos (*egress*) entre regiones o servicios tiene un costo directo |
| **La red es homogénea** | Los dispositivos varían en tipo, rendimiento y fabricante | Clientes lentos o con protocolos distintos degradan el conjunto |

En la nube, la **replicación y la redundancia** también consumen red, y hay escenarios de **consumo excesivo de red** que no se ven hasta que llega la factura.

## Cómo se combinan: el caso típico de prueba

Las falacias rara vez fallan solas. Ejemplo:

**Escenario:** el checkout llama en cadena a Usuarios → Inventario → Precios → Pagos, todos en servicios distintos.
- **Latencia ≠ 0:** cuatro saltos de 80 ms cada uno ya suman unos 320 ms antes de procesar nada.
- **Red no confiable:** si Precios pierde una respuesta, el cliente espera hasta su timeout (por ejemplo 2 s) y reintenta, así que la petición completa pasa a tardar más de 2,3 s.
- **Combinación:** con reintentos en cada salto, una falla parcial se **amplifica**. Además, los reintentos agregan carga a un servicio que ya está lento, lo que puede provocar una caída en cascada.

**Medidas:**
- **Paralelizar** las llamadas independientes (Usuarios y Precios a la vez) en vez de encadenarlas.
- **Timeouts cortos** con **circuit breaker** y **reintentos con *backoff* y *jitter***, para no amplificar la falla.
- **Cachear** los precios, que cambian poco, para eliminar un salto.
- Si los servicios conversan demasiado, **agruparlos** (menos distancia modular), como hizo Amazon Prime Video.

> [!tip] Estructura de la respuesta esperada
> Nombrar **2 falacias** concretas, explicar **cómo se combinan** en un sistema distribuido y proponer **una medida acorde** al caso. La pauta asigna puntaje por cada falacia, por la combinación y por la medida.

## Medidas por falacia

| Falacia | Medidas |
|---|---|
| Red no confiable | Reintentos idempotentes, timeouts, circuit breakers, colas persistentes (MOM) |
| Latencia ≠ 0 | Cachés, CDN, llamadas en paralelo, menos saltos, protocolos binarios (gRPC) |
| Ancho de banda finito | Compresión, no mover archivos pesados entre servicios, procesar donde están los datos |
| Red insegura | TLS, firewalls, WAF, autenticación entre servicios |
| Topología cambiante | Service discovery, DNS, balanceadores |
| Costo de transporte > 0 | Agrupar y comprimir mensajes, evitar transferencias entre regiones |
| Red heterogénea | Estándares (HTTP, JSON, protobuf), adaptadores, degradar contenido según el cliente |

## Preguntas de repaso

> [!question]- Explique la falacia "la latencia es cero" y por qué empeora con llamadas encadenadas.
> Es suponer que una llamada remota cuesta lo mismo que una local. En realidad cada salto agrega milisegundos, y si las llamadas son secuenciales, sus latencias se suman. Una cadena de 5 servicios a 50 ms cada uno agrega unos 250 ms antes de hacer trabajo útil.

> [!question]- ¿Cómo se combinan "la red no es confiable" y "la latencia no es cero" para producir una falla en cascada?
> Una respuesta perdida obliga a esperar el timeout y reintentar, lo que suma latencia. Si cada servicio de la cadena reintenta, la carga sobre el servicio lento se multiplica, lo hace todavía más lento y los timeouts se propagan hacia arriba hasta tumbar el flujo completo.

> [!question]- ¿Qué medidas mitigan esa combinación?
> Timeouts cortos, circuit breakers que dejen de llamar a un servicio caído, reintentos con backoff exponencial y jitter, llamadas en paralelo cuando son independientes, y caché o asincronía (MOM) para sacar saltos del camino crítico.

> [!question]- ¿Por qué el costo de transporte "es más explícito en la nube"?
> Porque los proveedores cobran por la transferencia de datos, sobre todo la salida entre regiones o hacia internet. Un diseño que mueve mucho volumen entre servicios se ve directamente en la factura, como pasó con Amazon Prime Video.

> [!question]- V o F: "Dentro de una misma nube la red es confiable, así que no hace falta manejar fallas de red entre servicios".
> Falso. Incluso dentro de la nube se pierden paquetes, las instancias caen repentinamente y las respuestas se pierden. Hay que diseñar con timeouts, reintentos idempotentes y tolerancia a fallos.

> [!question]- Mini caso: unas sondas espaciales se alejan y la latencia crece. ¿Qué medida de performance propone?
> Es el problema de la red sin cables. Se pueden usar intermediarios de comunicación que funcionen como caché o relé, o una red P2P entre sondas para retransmitir. Así los datos viajan por el camino disponible sin perder información, y la sonda trabaja de forma asíncrona sin esperar respuestas inmediatas.

> [!question]- ¿Qué falacia ignora un diseño que envía videos completos entre microservicios para procesarlos?
> Que el ancho de banda es infinito y que el costo de transporte es cero. Mover archivos pesados por la red satura el ancho de banda, agrega latencia y cuesta dinero. Conviene procesar donde están los datos.
