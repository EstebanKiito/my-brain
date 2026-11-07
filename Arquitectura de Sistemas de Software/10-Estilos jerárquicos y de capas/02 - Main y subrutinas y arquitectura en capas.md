---
ramo: "Arquitectura de Sistemas de Software"
tema: "Estilos jerárquicos y de capas"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[01 - Estilos patrones y el monolito]]"
  - "[[03 - Arquitectura en capas]]"
---

# Main y subrutinas y arquitectura en capas

Los dos estilos más antiguos organizan el sistema en una **jerarquía**. En **main y subrutinas**, un programa principal llama a funciones. En **capas**, cada nivel usa los servicios del inferior. Ambos son fáciles de entender, pero tienen límites claros que las pautas usan para descartarlos.

## Main y subrutinas

Es un estilo **influenciado por el lenguaje** e históricamente relevante:
- Hay **subrutinas** individuales y encapsuladas: funciones específicas que se ejecutan.
- El **main** "cede" el control a cada subrutina y **determina el orden**. Se conecta a cada una y la ejecuta cuando la necesita.
- Es de **alto acoplamiento** y **bloqueante**: mientras corre una subrutina, el resto espera (un solo hilo, un `while True`).

**Ejemplos:** Lunar Lander (solo se realiza una acción a la vez), Tetris (mientras la pieza gira, el resto se detiene), sistemas embebidos, MS-DOS y Pac-Man.

**Datos y topología:** los datos son los parámetros de las llamadas a función, y la topología está centralizada en el main, con ida y vuelta a cada subrutina.

| Cualidades | Advertencias |
|---|---|
| **Modularidad**: si se respeta la interfaz, se puede modificar la subrutina | **Pobre extensibilidad y escalabilidad**: más código significa más opciones de bloqueo |
| **Costo de comunicación nulo**: las llamadas son casi instantáneas | **Incompatible con estructuras de datos complejas** |
| Varios desarrolladores pueden trabajar en distintas partes (pero no muchos) | **Limitaciones de performance** y **posibilidad de bloqueo**: si una subrutina entra en un loop infinito, se pierde la aplicación |

> [!warning] Main y subrutinas casi nunca aplica en una prueba
> Las pautas lo marcan como **no válido** en sistemas distribuidos o con muchos usuarios, porque **es bloqueante**. Solo se justifica para un componente embebido, simple y secuencial.

## Arquitectura en capas

Organiza el sistema en **capas lógicas horizontales**, cada una con un **rol específico**, interconectadas para formar el sistema completo. Es un estilo muy común que suele salir de una **división técnica**. Cada capa encapsula funcionalidad.

- **Capas cerradas:** solo se interactúa con las capas **adyacentes**. Ejemplo: el modelo OSI, donde cada nivel solo habla con el de arriba y el de abajo.
- **Capas abiertas:** se puede saltar capas e interactuar con cualquiera.

![Capas apiladas con interfaces entre adyacentes y una conexión que salta capas](adjuntos/Capas%20abiertas%20y%20cerradas.png)

> [!example]- Transcripción de la imagen
> - Croquis titulado "CAPAS": tres rectángulos apilados. Cada uno se conecta con el de abajo mediante una interfaz.
> - A la izquierda, una línea conecta la capa superior directamente con la inferior, saltándose la del medio: es una capa abierta.

**Ejemplos:** Rails y MVC (servicios, helpers), máquinas virtuales, servicios web, e-commerce, y ciertos kernels (Linux, Windows NT). Una capa no es necesariamente un único bloque: puede ser muy potente según cómo se construya. También el protocolo MCP organiza su arquitectura en capas.

**Datos y topología:** parámetros y paquetes bien específicos y concisos, con una interfaz que exige una estructura determinada. La topología es **lineal**: los datos se mueven en direcciones predecibles.

| Pros | Contras |
|---|---|
| Muy conocido: **fácil de diseñar y entender**, y suele reflejar la estructura del negocio | **Pobre desempeño en dominios complejos**: los problemas extensos generan una maraña de conexiones entre capas |
| Sube el nivel de abstracción: **dependencias muy claras**; un cambio en una capa solo afecta a las adyacentes | **Demasiadas capas reducen la performance** |
| **Interfaces precisas** | Algunos diseños se bloquean esperando respuestas |
| **Económico y rápido de crear** | No es universalmente aplicable, y es difícil de evolucionar por su rigidez |
| | **Poco tolerante a fallos**, y pueden aparecer capas anémicas (que solo pasan datos) |

## Ejemplo: la arquitectura de la E1 leída como capas

![Arquitectura de la E1: front en S3, API Gateway, EC2 con nginx y API, y broker](adjuntos/Arquitectura%20de%20la%20E1%20con%20API%20Gateway.png)

> [!example]- Transcripción de la imagen
> - Croquis "E1": el usuario entra por **CloudFront**, que sirve el **Front** alojado en **S3**. El front usa un servicio **Auth0**.
> - El front llama a una **API Gateway**, que valida con un **Custom Authz**.
> - La API Gateway llama a una **EC2** que contiene **nginx** y la **API**, y la EC2 se conecta al **Broker**.

![La misma arquitectura anotada como estilo en capas](adjuntos/Arquitectura%20de%20la%20E1%20leída%20como%20capas.png)

> [!example]- Transcripción de la imagen
> - El mismo diagrama, anotado debajo de cada parte: **CDN**, **FRONT**, **GATEWAY** y **API**.
> - Texto: "Estilo en capas (4)" y "App web, que se subdivide en capas funcionales".

La API de la EC2 **no se expone directamente a internet**. Se pone delante un servicio *serverless*, la **API Gateway**: es lo que queda expuesto, y en cada petición verifica con un **custom authorizer**. Así se evita que la colapsen con peticiones al azar y solo pasan las válidas. Leído con estilos, son **4 capas funcionales**: CDN, front, gateway y API.

## Preguntas de repaso

> [!question]- ¿Por qué main y subrutinas se describe como de alto acoplamiento y bloqueante?
> Porque el main controla el orden y cede el control a cada subrutina, y mientras una se ejecuta, el resto espera en el mismo hilo. Si una subrutina se cuelga, se cuelga toda la aplicación.

> [!question]- Diferencie capas cerradas y abiertas.
> En capas cerradas, cada capa solo se comunica con las adyacentes (como en el modelo OSI). En capas abiertas, una capa puede saltarse otras y hablar con cualquiera, lo que gana performance a cambio de más acoplamiento.

> [!question]- Nombre tres pros y tres contras del estilo en capas.
> Pros: fácil de diseñar y entender, dependencias claras e interfaces precisas, y económico de crear. Contras: bajo desempeño con muchas capas o dominios complejos, rigidez para evolucionar y poca tolerancia a fallos.

> [!question]- ¿Por qué en la E1 se pone una API Gateway delante de la EC2?
> Para no exponer directamente la API a internet. La gateway serverless recibe las peticiones, las valida con un custom authorizer y solo deja pasar las válidas, protegiendo a la EC2 de peticiones al azar o maliciosas.

> [!question]- ¿Qué es una "capa anémica" y por qué es un problema?
> Una capa que no agrega lógica y solo pasa datos de la de arriba a la de abajo. Suma latencia y código sin valor, y suele indicar capas forzadas por convención.

> [!question]- V o F: "Main y subrutinas es una buena opción para un backend con miles de usuarios concurrentes".
> Falso. Es bloqueante y de un solo hilo: no puede atender peticiones concurrentes y escala mal. Las pautas lo marcan como no válido en esos casos.

> [!question]- Mini caso: una web de noticias con frontend, servidor web, lógica y base de datos. ¿Qué estilo y qué riesgo de performance hay?
> Estilo en capas: presentación, servidor web, lógica de negocio y datos. El riesgo es que cada petición atraviesa todas las capas, y con muchas capas o llamadas entre ellas se acumula latencia. Se mitiga minimizando las llamadas entre capas y cacheando.
