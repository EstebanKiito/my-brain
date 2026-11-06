---
ramo: "Arquitectura de Sistemas de Software"
tema: "Métodos de escalabilidad"
tags:
  - arquisis/escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[02 - Modelación de sistemas para escalar]]"
---

# Distribución serverless frontend y nube

La modelación de sistemas tiene cuatro frentes más: **distribuir** el sistema por dominio, usar **serverless**, optimizar el **frontend** y apoyarse en la **nube**. Cada uno escala algo distinto y cada uno tiene una trampa.

## Distribución por dominio

Dividir el sistema por **dominio** en servicios: SOA o microservicios. Cada servicio escala según su propia carga.

![API Gateway frente a servicios con distintos tipos de bases de datos](adjuntos/API%20Gateway%20frente%20a%20servicios%20con%20distintas%20bases%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, clientes (tablet, laptop, celular y una web) que llaman por **HTTP** a una **API GATEWAY**.
> - La gateway se comunica con varios servicios (hexágonos de colores): uno por **AMQP** (mensajería) y los otros por **HTTP**.
> - Cada servicio tiene su propio almacenamiento: uno una **Relational DB** y otros un **Key / Value Store**.

**Consideraciones:**
- **Complejidad de coordinación** entre servicios.
- **Latencia** y la necesidad de implementar intermediarios (gateway, broker).
- **El glorioso monolito** sigue siendo una opción válida: hay que partir solo donde se justifique.

## Serverless

Útil para **pruebas de concepto (PoC)** y **scripts puntuales**. El proveedor escala automáticamente y se paga por uso.

| Rol | Servicios de AWS |
|---|---|
| Cómputo | Lambda, Fargate |
| Almacenamiento | S3 |
| Base de datos | RDS |
| Coordinación | SNS, SQS |
| Datos | Aurora, DynamoDB |

> [!warning] Ojo con serverless
> - Recordar el **caso Amazon Prime Video**: su flujo distribuido en serverless movía demasiados datos y salía caro.
> - **Arranque en frío** (*cold start*): las funciones que no se han usado tardan en arrancar, lo que es malo para casos que exigen baja latencia desde el primer request.

## Frontend

Un frontend pesado multiplica la carga sobre el backend y la red. Buenas prácticas (reglas de Yahoo, actualizadas):
- Reducir las peticiones: sprites, combinar scripts e imágenes, comprimir (gzip), usar cachés del servidor, manejar la caché con **ETags**.
- Stylesheets al principio. Scripts al final, hoy reemplazado por `async`/`defer` y priorización.
- No usar expresiones CSS. JavaScript y CSS en archivos **externos** (paquetes cacheables).
- **Hacer cacheable el Ajax** (HTTP, CDN, cachés incorporadas). Minimizar iframes y cookies.
- Uso inteligente de **preload, prefetch** y carga especulativa.
- Evitar bundles innecesarios con **chunking** y **tree shaking**.
- Usar **HTTP/2 y HTTP/3**.

**Herramientas:**
- **Modernizr** detecta las capacidades HTML5 y CSS3 del navegador y adapta o degrada la página.
- **HTML5 Boilerplate** es una plantilla del front optimizada.
- **Lighthouse y Core Web Vitals** analizan el rendimiento de carga: LCP (cuánto tarda en verse el contenido principal), INP (cuánto tarda en responder a la interacción) y CLS (cuánto se mueve el contenido al cargar).

**Mejorar la carga y no traer datos innecesarios también mejora la escalabilidad**: cada byte que el frontend no pide es carga que el backend no atiende.

## Nube

- **Elasticidad de alto nivel**: crecer y decrecer según la demanda.
- **OPEX en vez de CAPEX**: se paga por uso en vez de comprar servidores, lo que da **escalabilidad financiera**.
- **Sistemas de autoescalado** (*autoscaling groups*).

**Consideraciones:**
- Es una **bala de oro**, no de plata: resuelve mucho, pero cuesta mucho ("¿quieres disparar oro?").
- **Vendor lock-in**: depender de servicios propietarios dificulta cambiar de proveedor.
- **Descontrol sobre la infraestructura subyacente.**

## Preguntas de repaso

> [!question]- ¿Qué gana y qué cuesta distribuir un sistema por dominio en servicios?
> Gana que cada servicio escala, se despliega y elige su base de datos según su propia necesidad. Cuesta complejidad de coordinación, latencia por los saltos de red e intermediarios (gateway, broker) que hay que operar.

> [!question]- ¿Para qué casos recomienda el curso serverless y cuál es su riesgo principal?
> Para pruebas de concepto y scripts puntuales o eventuales. Los riesgos son el costo y la latencia cuando el flujo mueve muchos datos entre funciones (caso Prime Video), y el arranque en frío en servicios que necesitan baja latencia desde la primera petición.

> [!question]- ¿Por qué optimizar el frontend mejora la escalabilidad del backend?
> Porque reduce la cantidad y el tamaño de las peticiones que llegan al servidor: cachear recursos estáticos, combinar archivos, evitar bundles innecesarios y no pedir datos de más. Menos peticiones por usuario significa más usuarios con la misma infraestructura.

> [!question]- ¿Qué son los Core Web Vitals?
> Métricas de experiencia de carga: LCP (cuánto tarda en verse el contenido principal), INP (cuánto tarda la página en responder a una interacción) y CLS (cuánto se mueve el contenido mientras carga). Lighthouse las mide.

> [!question]- ¿Qué significa que la nube dé "escalabilidad financiera"?
> Que el gasto pasa de inversión fija (CAPEX: comprar servidores para el peak) a gasto operacional por uso (OPEX). Se paga más cuando hay más demanda y menos cuando baja, y el costo sigue a la carga.

> [!question]- Nombre dos desventajas de depender de la nube para escalar.
> El vendor lock-in, porque los servicios propietarios dificultan migrar, y la pérdida de control sobre la infraestructura subyacente. Además el costo puede ser alto: es una bala de oro.

> [!question]- V o F: "Serverless es siempre más barato porque solo se paga por uso".
> Falso. Para cargas constantes y altas, o flujos que mueven muchos datos entre funciones, puede ser más caro que servidores dedicados. El caso Prime Video redujo su costo un 90% al sacar un flujo de la arquitectura distribuida.
