---
ramo: "Arquitectura de Sistemas de Software"
tema: "Resolución de casos de diseño"
tags:
  - arquisis/casos
  - origen/complemento
prerrequisitos:
  - "[[01 - Método para resolver un caso de prueba]]"
  - "[[05 - Cómo elegir el mecanismo de integración]]"
  - "[[04 - Microkernel]]"
---

# Caso de integración bancaria LegitBank

Caso de la I1 2026-1, muy relevante para la I2 porque combina en un mismo sistema **tres mecanismos de integración distintos**: notificaciones por MOM, **GraphQL** y **gRPC**, sobre un core **microkernel** con plugins. Es el ejemplo perfecto de "elegir el mecanismo según el flujo".

## El enunciado, resumido

Por normativas de OpenBanking, LegitBank tiene un core **microkernel** al que se le agregan tres plugins:
1. **Transferencias:** el usuario envía su transferencia y el plugin inicia el flujo con el core por la interfaz `iTransfer`. El banco envía **notificaciones** de los estados por `iNotify`. Los estados se guardan en una base para informar al usuario.
2. **Cuentas bancarias:** un **cliente GraphQL**. El usuario elige campos y fechas. Si la respuesta no llega dentro del plazo de la petición, el core deja el registro y la envía después por `iSubscription`. Solo se guarda lo necesario para ese paso.
3. **Inversiones:** una API para los usuarios (ver inversiones y carteras, agregar fondos) con un **cliente gRPC** que consume las funciones del core, por velocidad, con una función por caso. Se guarda un registro local de las solicitudes **para auditoría**.

## Preguntas y respuestas de la pauta

**a) ¿Cómo validar que el usuario es quien dice ser usando el token del login del banco?** Sí es válido usar el token. La validación esperada es **conectar todo a través de una API Gateway con un custom authorizer**, como en la E1. También valen validadores internos o un authorizer por plugin.

**b) El banco envía notificaciones de estado de las transferencias: ¿qué mecanismo usar?** Un mecanismo que permita **múltiples notificaciones**:
- un **MOM** con el core como publicador; o
- **REST con webhook** (el core hace `POST` a un endpoint del plugin).
No se necesita la alta performance de RPC (que además es difícil de implementar), ni es una conexión directa con un cliente donde se aproveche GraphQL.

**c) Características válidas:**
- **performance**, por el plugin de inversiones con gRPC;
- **usabilidad**, por el plugin de cuentas, donde el usuario elige campos;
- **seguridad**, por la pregunta a;
- **confiabilidad**, por ser una aplicación bancaria.

**No válidas:** integrabilidad (es un requisito del core, no de los plugins), soporte, flexibilidad (no se piden funcionalidades futuras), elasticidad (no hay picos) y portabilidad.

**d) Estilos válidos:** EDA (si usan MOM), pub/sub, capas, cliente-servidor (solo dentro de un plugin) y SOA. **No válidos:** main y subrutinas, pizarra, máquinas virtuales y **microkernel**, salvo que lo usen internamente en un plugin y lo justifiquen, porque el microkernel **ya existe** en el core.

## El diagrama de referencia

![Diagrama de referencia con los plugins de transferencias, cuentas e inversiones](adjuntos/Diagrama%20de%20referencia%20de%20integración%20bancaria%20con%20plugins.png)

> [!example]- Transcripción de la imagen
> - **LegitBank Core** al centro, con *Transfer Plugin Connector*, *Bank Account Plugin Connector* e *Investments Plugin Connector*.
> - **Transfer Plugin** (izquierda): *Transfer Input Receiver* → *Transfer Input Parser* → *Plugin Connector* (`iTransfer` hacia el core). Una *Transfers DB* y un **MoM** con un *MoM Transfer States Subscriber*, que recibe `iNotify` del core.
> - **Bank Account Plugin** (derecha): *Bank Account Input Receiver* → *Input Parser* → *Request Manager* → **GraphQL Client** (`iGraphConnect` al core). Un **GraphQL Subscriber** recibe `iSubscription`, con una *Requests DB*, una *GraphQL SchemaDB* y *Show Schema*.
> - **Investments Plugin** (abajo): un **gRPC Client** (`iGRPCConnect` al core) y funciones *gRPC Invest Money*, *gRPC Get Wallets* y *gRPC Get Investments Info*, cada una detrás de su endpoint (*Invest Money*, *Get Wallets*, *Get Investments Info*), con una *Records DB* para auditoría.
> - Abajo, una **API Gateway** expone todos los endpoints, y una **«Lambda Function» Custom Bank Token Authorizer** valida el token (`iCheckToken`).

**Lo que hay que notar:**
- Cada plugin **elige el mecanismo de integración según su flujo**: MOM para notificaciones múltiples y asíncronas, GraphQL para que el cliente elija campos y reciba la respuesta diferida por suscripción, y gRPC para la velocidad entre el plugin de inversiones y el core.
- **La API Gateway con un authorizer** concentra la seguridad.
- Cada plugin tiene **su propia base**, con solo lo que necesita (estados, requests, registros de auditoría).

## Preguntas de repaso

> [!question]- ¿Por qué un MOM o un webhook para las notificaciones de transferencias, y no gRPC ni GraphQL?
> Porque se necesitan múltiples notificaciones asíncronas de estado, sin requisitos de latencia extrema: un MOM con el core como publicador o un webhook REST es simple y suficiente. gRPC agrega complejidad sin necesidad, y GraphQL está pensado para que un cliente elija los campos que consulta.

> [!question]- ¿Qué aporta GraphQL al plugin de cuentas bancarias?
> Que el usuario elija exactamente los campos y fechas que quiere, en una sola consulta. Además, con las suscripciones (`iSubscription`) se puede recibir la respuesta más tarde si la consulta tarda más que el plazo de la petición.

> [!question]- ¿Por qué el plugin de inversiones usa gRPC?
> Para comunicarse rápido con las funciones del core: binario, tipado y sobre conexiones persistentes, con una función por operación. Justifica la performance como atributo.

> [!question]- ¿Por qué microkernel no suma como estilo en este caso?
> Porque el core ya es microkernel: es parte del enunciado, no una decisión de la solución. Solo sumaría si se usara internamente en un plugin y se justificara.

> [!question]- ¿Cómo se valida el token según la respuesta esperada?
> Pasando todas las peticiones por una API Gateway con un custom authorizer (una función Lambda) que valida el token del login del banco antes de llegar a los plugins, como en la E1.

> [!question]- ¿Por qué integrabilidad no es válida aunque el caso trate de integración?
> Según la pauta, la integrabilidad es un requisito del core microkernel, que ya está construido, y no de los plugins que se diseñan. Los atributos se justifican por lo que pide la solución, no por el tema del enunciado.
