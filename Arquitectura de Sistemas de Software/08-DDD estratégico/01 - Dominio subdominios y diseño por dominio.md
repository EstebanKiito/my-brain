---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD estratégico"
tags:
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[03 - Tradeoffs y conocimiento de dominio]]"
---

# Dominio subdominios y diseño por dominio

Imagine que quiere competir con Shopify. ¿Cómo construiría una app de e-commerce común? La respuesta típica es técnica: "un frontend en React, un backend con su base de datos, un broker para los bancos". Pero ¿consideró los **carritos**, las **promociones**, el **inventario**, los **envíos**, la **conexión al ERP** (para emitir boletas), la **cadena de suministro**, los **precios** y las **notificaciones**? El **Domain-Driven Design estratégico** parte del negocio, no de la tecnología, para decidir cómo dividir el sistema.

## Diseño técnico frente a diseño por dominio

| Diseño técnico | Diseño por dominio |
|---|---|
| La **tecnología define las fronteras** | El **negocio define los dominios** |
| Las cosas se nombran por el stack (`frontend`, `backend`, `broker-bancos`, `replicas`) | El **dominio define los nombres** (`Catálogo`, `Envíos`, `Facturación`) |
| Pensamiento centrado en el desarrollador | **Bounded contexts** alineados con áreas del negocio |

El diseño por dominio exige conocer las **reglas del negocio** y orientar el sistema en base a ellas.

## Dominio

> [!tip] Dominio
> **Área de conocimiento que el software modela**: el problema de negocio que se busca resolver. Los problemas complejos se vuelven manejables con una modelación orientada al negocio.

Al construir algo hay que preguntarse qué queremos del negocio: ¿cuál es su funcionalidad central? ¿Qué le da más valor? En el ejemplo, el dominio es un **sistema de compra y venta en línea**.

## Subdominios

Los dominios son complejos, así que se **dividen en subdominios**: áreas donde se puede trabajar por separado.

| Tipo | Qué es | Cómo se construye |
|---|---|---|
| **Core** | **Lo que hace vivir al negocio**, su principal factor diferenciador | Desarrollo propio, con el mejor equipo |
| **Support** (soporte) | **Habilitan al core** y son de desarrollo interno | Desarrollo propio, más simple |
| **Genérico** | También habilitan, pero son **externalizables** | Se compran o se integran: frameworks, software COTS, SaaS |

**Clasificación del e-commerce:**
- **Core:** catálogo de productos y manejo de órdenes (ventas). Es donde la tienda compite.
- **Support:** envíos y atención al cliente.
- **Genéricos:** pagos (una pasarela externa), correo (un proveedor SaaS) y usuarios o autenticación (un proveedor de identidad).
- **Facturación** es un subdominio contable que puede ser support o genérico (si se integra un ERP).

> [!warning] Lo que NO es un subdominio
> Los componentes técnicos **no son subdominios**: "broker-bancos", "réplicas", la API Gateway, la base de datos o "un módulo de eventos genérico" son decisiones de implementación, no áreas del negocio. Es el error clásico que descuenta la pauta. Un subdominio se puede explicar a alguien del negocio sin hablar de tecnología.

> [!example]- Respuesta modelo: subdominios de FreeHelp (plataforma de ayuda ante catástrofes)
> **Core:** gestión de incidentes (declarar incidentes y actualizar sus demandas) y asignación de activos (encontrar los activos más cercanos y adecuados para cada demanda).
> **Otros subdominios:** ingesta de alertas, registro de organizaciones, integración y reservas con las organizaciones, y activos.
> **Errores clásicos:** marcar como dominio el broker, la API Gateway o la base de datos, o declarar un "módulo de eventos" genérico como dominio en sí mismo.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre el diseño técnico y el diseño por dominio?
> En el técnico, la tecnología define las fronteras y los nombres (frontend, backend, broker). En el diseño por dominio, el negocio define los dominios y sus nombres, y las fronteras del sistema siguen las áreas del negocio (bounded contexts).

> [!question]- Defina subdominio core, support y genérico, con un ejemplo de cada uno para un e-commerce.
> Core: lo que hace vivir al negocio y lo diferencia, como el catálogo y el manejo de órdenes. Support: habilita al core y se desarrolla internamente, como envíos o atención al cliente. Genérico: habilita pero es externalizable, como pagos con una pasarela o autenticación con un proveedor de identidad.

> [!question]- ¿Por qué el core domain merece el mejor equipo y desarrollo propio?
> Porque es donde el negocio compite y genera valor. Si se compra hecho, no hay diferenciación; si se descuida, se pierde la ventaja. Los genéricos, en cambio, conviene comprarlos para concentrar el esfuerzo en el core.

> [!question]- V o F: "El broker de mensajería que conecta los servicios es un subdominio de soporte".
> Falso. Es un componente técnico, no un área del negocio. Los subdominios se definen por el conocimiento del negocio que modelan (ventas, envíos, pagos), no por piezas de infraestructura.

> [!question]- En un sistema de reservas de hoteles, identifique el dominio y clasifique tres subdominios.
> Dominio: la reserva de alojamiento. Core: la gestión de disponibilidad y reservas (lo que diferencia al negocio). Support: gestión de huéspedes y check-in. Genérico: pagos (pasarela externa) y notificaciones (proveedor de correo o SMS).

> [!question]- ¿Qué subdominios olvida el enfoque técnico al diseñar un "Shopify"?
> Carritos, promociones, inventario, envíos, conexión con el ERP para la facturación, cadena de suministro, precios y notificaciones. Pensar solo en frontend, backend y base de datos deja fuera las áreas del negocio que el sistema debe modelar.

> [!question]- ¿Cuándo un subdominio de soporte debería pasar a ser genérico?
> Cuando existe una solución externa madura que cubre la necesidad y no aporta diferenciación desarrollarla internamente. Por ejemplo, reemplazar un sistema propio de envío de correos por un proveedor SaaS.
