---
ramo: "Arquitectura de Sistemas de Software"
tema: "Arquitecturas orientadas a servicios"
tags:
  - arquisis/estilos
  - arquisis/servicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Topologías mediator y broker y el estilo pub sub]]"
  - "[[05 - Arquitectura orientada a servicios (SOA)]]"
---

# SOA historia y el bus de servicios

Antes había monolitos que lo hacían todo: controladores, vistas y modelos (un patrón), y dentro, la lógica de inventario, registros, envíos y pagos. Cuando muchos usuarios se autentican mientras otros pagan y otros procesan envíos, **cada área necesita escalar por separado**. Así se empezó a separar por servicios. La **arquitectura orientada a servicios (SOA)** es la primera respuesta a gran escala, y su historia explica por qué hoy se habla de microservicios.

## Qué es

> [!tip] SOA
> Paradigma que usa el **servicio como idea básica**, para construir aplicaciones **interoperables**, **masivamente distribuidas** y **evolucionables** de forma rápida y a bajo costo. Los servicios son de **grano grueso**: cada uno captura muchos conceptos, típicamente un subdominio (pagos, envíos, logística, inventario).

**Lo que SOA dejó instalado:** el **servicio como unidad con contrato propio**. El bus (ESB) fue una decisión de implementación **opcional**, y la que más costó.

![SOA: consumidores, bus de servicios e implementaciones](adjuntos/SOA%20con%20bus%20de%20servicios.png)

> [!example]- Transcripción de la imagen
> - Arriba, **Service Consumers**, que intercambian **Messages** con el **Service Bus**.
> - El bus está rodeado de **Configuration & Rules** a la izquierda y **Management & Reporting** a la derecha.
> - Abajo, **Service Interfaces and Service Implementations** (los servicios).

## La línea de tiempo de las decisiones

| Época | Decisión | Consecuencia |
|---|---|---|
| **1990s** | Objetos distribuidos (CORBA, DCOM, RPC) | Llamar a un objeto remoto como si fuera local, y descubrir que la red no es transparente |
| **2000** | El servicio con contrato (SOAP, WSDL, UDDI, WS-*) | Interoperabilidad por estándar y no por acoplamiento a un lenguaje, pero estándares ilegibles |
| **2002-2006** | El bus (ESB); el modelo de referencia de OASIS (2006) define SOA **sin** bus | Se centraliza la integración, y se centraliza también la lógica |
| **2009** | "SOA is dead; long live services" (Manes) y el Manifiesto SOA | Valores sobre productos |
| **2011-2014** | Microservicios (Netflix, Amazon; Fowler y Lewis, 2014) | Mantener el servicio, cambiar la unidad de despliegue y botar el bus: *smart endpoints, dumb pipes* |
| **2020s** | El tamaño correcto (monolito modular, *service-based*) | Pagar solo la distribución que un requisito exige |

## Las variantes de SOA

![Servicios conectados a un bus de servicios](adjuntos/Servicios%20conectados%20a%20un%20bus%20de%20servicios.png)

> [!example]- Transcripción de la imagen
> - Croquis "SOA": **Servicio 1**, **Serv 2** y **Serv 3** conectados por interfaces a un **EBS** (bus de eventos o de servicios).
> - Anotaciones: "EBS → API Gateway = E1".

- **Primera variante:** todos los servicios conectados al mismo bus. Los servicios 2 y 3 pueden tener **su propia base de datos**. El sistema tiene **N quantas**: el bus es opcional, y si se cae, cada servicio puede seguir funcionando por su cuenta.
- **Equivalencia con el proyecto:** el rol del bus lo cumple la API Gateway de la E1.

### El servicio compartido

![SOA con servicio de autenticación compartido y microservicios](adjuntos/Servicio%20de%20autenticación%20compartido%20y%20microservicios.png)

> [!example]- Transcripción de la imagen
> - Arriba, el mismo SOA con el EBS. Abajo, "SOA 2": un servicio **Auth** del que dependen **S1** y **S2**, con la anotación "Alto acoplamiento".
> - A la derecha, "Micro servicios": **MS1**, **MS2** y **MS3**, cada uno con su base, anotados con "monolito para ver desde DD" y "deben conectarse por orquest y coreografía".

Si se agrega un **servicio de autenticación** que usan S1 y S2:
- Como **servicio**, genera connascence de **identidad**: ambos dependen de la misma instancia. Si Auth se cae, se caen los dos.
- Como **librería**, sería connascence de **algoritmo**, más débil: cada servicio la ejecuta por su cuenta.
- **Un servicio compartido es un acoplamiento compartido.** Lo que eran N quantas pasa a comportarse como menos, porque todos dependen de Auth.

## La promesa del reuso extremo, y cómo se aplicó mal

- **La apuesta de SOA:** construir una vez y reutilizar en toda la empresa ("servicios compartidos sobre implementaciones de propósito específico").
- **En la práctica:** un servicio compartido es un acoplamiento compartido. Todos dependen de su calendario de releases, de su modelo y de su disponibilidad.
- **El servicio "genérico" no sirve bien a nadie:** cada consumidor necesita una variante, y las variantes terminan viviendo en el bus.
- **El ESB llevado al extremo** fue un intermediario que sabía demasiado (ruteo, transformación, reglas de negocio), y el **modelo canónico** fue un shared kernel forzado a toda la empresa.

> [!warning] SOA "se empezó a hacer de mala manera"
> El problema no fue la idea de servicio, sino servicios demasiado grandes y un bus con demasiada lógica. De esa reacción nacen los microservicios: servicios pequeños, contratos explícitos y sin bus inteligente.

## Preguntas de repaso

> [!question]- ¿Qué problema del monolito motivó SOA?
> Que las distintas áreas (autenticación, pagos, envíos) tienen cargas y ritmos distintos y necesitan escalar por separado. En un monolito todo escala junto.

> [!question]- ¿Qué dejó instalado SOA y qué fue lo que más costó?
> Dejó el servicio como unidad con contrato propio. Lo que más costó fue el ESB: un bus central que terminó concentrando la integración y la lógica.

> [!question]- ¿Por qué se dice que "un servicio compartido es un acoplamiento compartido"?
> Porque todos sus consumidores dependen de su disponibilidad, de su modelo y de su calendario de cambios. Si cambia o se cae, afecta a todos, que es connascence de identidad entre servicios lejanos.

> [!question]- Un servicio de autenticación compartido frente a una librería de autenticación: ¿qué connascence genera cada uno?
> El servicio genera connascence de identidad (todos dependen de la misma instancia, que si cae los tumba). La librería genera connascence de algoritmo (cada servicio ejecuta la misma lógica localmente), más débil y sin un punto único de falla.

> [!question]- ¿Cuántas quantas tiene un SOA con bus y bases propias, y qué lo cambia?
> Puede tener N quantas si el bus es opcional y cada servicio funciona solo. Lo cambia agregar dependencias compartidas obligatorias (un auth central, un bus imprescindible), que hacen que la caída de una pieza arrastre a varias.

> [!question]- Ordene cronológicamente: microservicios, ESB, objetos distribuidos, servicios con contrato SOAP.
> Objetos distribuidos (1990s), servicios con contrato SOAP/WSDL (2000), ESB (2002-2006) y microservicios (2011-2014).

> [!question]- V o F: "SOA requiere obligatoriamente un Enterprise Service Bus".
> Falso. El modelo de referencia de OASIS (2006) define SOA sin bus. El ESB fue una decisión de implementación opcional, y la más costosa.
