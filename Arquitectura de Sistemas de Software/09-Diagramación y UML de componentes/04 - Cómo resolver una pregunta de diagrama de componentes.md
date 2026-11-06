---
ramo: "Arquitectura de Sistemas de Software"
tema: "Diagramación y UML de componentes"
tags:
  - arquisis/uml
  - arquisis/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Notación del diagrama de componentes UML]]"
  - "[[01 - Stakeholders y características arquitectónicas]]"
---

# Cómo resolver una pregunta de diagrama de componentes

En cada prueba hay una pregunta de unos 13 puntos que pide un diagrama de componentes UML que resuelva un caso, más las preguntas previas de atributos y estilos y una de "falencias". **No hay solución única**, así que la corrección es por **descuentos**. Esta nota reúne el método, los formatos típicos de cada estilo y la checklist de lo que se descuenta.

## El orden de la respuesta

1. **Atributos de calidad priorizados**, justificados con el enunciado.
2. **Estilos y patrones**, diciendo qué responsabilidad del problema ataca cada uno y qué atributo apoya.
3. **El diagrama**: debe **priorizar las decisiones anteriores**. Si se declaró pub/sub, el pub/sub tiene que estar en el diagrama.
4. **Falencias**: dos debilidades de la propia solución, cómo se solucionarían y qué implican.

> [!tip] Lo que se espera como mínimo
> **Todos los servicios o funcionalidades que pide el enunciado.** Después se revisa que esté bien diagramado: conexiones con interfaces, orden y el formato lollipop.

## Métodos para manejar un problema

![Tabla de los métodos inductivo, deductivo y por referencia](adjuntos/Métodos%20inductivo%20deductivo%20y%20por%20referencia.png)

> [!example]- Transcripción de la imagen
> | Inductivo: del detalle a lo general | Deductivo: de lo general al detalle | Referencia |
> |---|---|---|
> | "Tengo que armar un chat en tiempo real": debo aplicar invocación implícita | "Debo cubrir 1.000 usuarios por minuto": debo usar un balanceador de carga y manejar concurrencia | "He visto esto en otro lado…" |
> | "Tengo que almacenar fotos": hay que introducir un tipo de almacenamiento de objetos | "Mi sistema es complejo en dominios": debo tener una arquitectura orientada a servicios (SOA) | Hay componentes reusables que se pueden usar en nuestros sistemas |

A veces el problema viene con un diagrama pequeño que hay que completar: ahí se usa el método **por referencia**. **Aprenderse los diagramas de las ayudantías** sirve, porque se pueden reutilizar.

**Premisas:** no hay un solo tipo de diagrama, ni un sistema que resuelva todo. Hay que buscar un **relato** (describir cada funcionalidad como una historia), **sin asumir antes de tiempo ni saltarse información**, y partir del alto nivel hacia piezas específicas.

**Qué buscar en el enunciado:** contextualización, **core**, especificaciones, detalles, **supuestos** (anotarlos en el diagrama) y limitaciones.

## Formatos típicos de cada estilo

![Formato de pipe and filter y de peer to peer](adjuntos/Diagramas%20de%20pipe%20and%20filter%20y%20peer%20to%20peer.png)

> [!example]- Transcripción de la imagen
> - **Pipe & Filter:** un componente contenedor "Pipe & Filter" con *Filter N* … *Filter 1* encadenados por interfaces, y una interfaz de entrada y otra de salida en los bordes.
> - **Peer To Peer:** tres componentes *Peer 1*, *Peer 2* y *Peer 3*, cada uno proveyendo y requiriendo interfaces de los otros dos.

![Formato de pub/sub y de un sistema basado en eventos](adjuntos/Diagramas%20de%20pub%20sub%20y%20basado%20en%20eventos.png)

> [!example]- Transcripción de la imagen
> - **PubSub:** un *Broker* al centro, un *Publisher* que se le conecta y dos *Subscriber* que requieren interfaces del broker.
> - **Basado en eventos:** un *Event Bus* central con *Service 0* arriba y *Service 1*, *2* y *3* abajo, todos conectados al bus por interfaces.

Cliente-servidor y capas se dibujan con un componente cliente y uno servidor, o con capas apiladas (presentación, lógica y datos) conectadas por interfaces entre capas adyacentes. Dentro de cada uno hay más componentes.

## Ejemplo: plataforma de telemedicina

**Enunciado:** agendar horas, conectarse a videoconsultas (provistas por un externo) y centralizar fichas de pacientes de distintos centros. Se espera un aumento de centros conectados. El frontend y el backend están separados y deben integrarse con distintos sistemas médicos.

- **Atributos:** seguridad (fichas médicas), integrabilidad (centros y videollamadas externos) y escalabilidad ("se espera un incremento").
- **Estilos:** cliente-servidor (pacientes y profesionales usan un frontend separado del backend) y capas (presentación, lógica de negocio y datos en el backend).

![Diagrama de componentes de la plataforma de telemedicina](adjuntos/Diagrama%20de%20componentes%20de%20una%20plataforma%20de%20telemedicina.png)

> [!example]- Transcripción de la imagen
> - Actores **Pacientes** y **Doctor** usan el **Frontend** (Dashboard, Request Handler y Auth Handler), que se conecta a un **Auth Service** por `iAuthService`.
> - El frontend se conecta con el **Backend** por `iClientConnection`. Dentro del backend: **Capa de Presentación**, **Capa de Lógica** y **DB**, conectadas en capas.
> - El backend requiere `iVideoCallSystem` de un **«Sistema de Videollamadas»** externo, y se conecta por `iCenterConnection` con los **Centros de atención 1…N**.

Los atributos de calidad van ligados a ciertos estilos: hay estilos que priorizan más la seguridad y otros que priorizan la escalabilidad.

## Lo que descuenta la pauta

| Descuento | Error |
|---|---|
| **−6** | No hay interfaces en el diagrama |
| **−3 c/u** | No se usan los estilos que se justificaron antes |
| **−1 c/u** | Falta un requisito funcional |
| **−1 c/u** | Interfaces mal implementadas |
| **−1 c/u** | Componentes desagregados (sin conectores) sin justificación |

Otros errores clásicos:
- **Diagrama incompleto:** detallar una parte y dejar otra sin diagramar.
- **Conexiones inútiles:** ¿por qué están conectados esos componentes?
- No justificar los estilos con los atributos declarados.
- Si no es un diagrama de componentes UML, no se corrige.

> [!example]- Pregunta de falencias: cómo responder
> "Identifique 2 falencias o tradeoffs de su solución, cómo los solucionaría y sus implicancias." No cuentan las falencias de **formato** ("me faltó explotar un componente").
> Ejemplo: "El broker es un punto único de falla: lo replicaría en un cluster con quorum queues, lo que aumenta el costo y la complejidad operacional. La base de datos de lecturas puede quedar desactualizada por la consistencia eventual: agregaría invalidación por eventos, lo que agrega mensajes y lógica."

## Preguntas de repaso

> [!question]- ¿En qué orden se responde una pregunta de diseño completa y por qué ese orden?
> Primero los atributos de calidad, luego los estilos que los apoyan, luego el diagrama y al final las falencias. El diagrama debe reflejar las decisiones anteriores: si los estilos declarados no aparecen en él, se descuenta.

> [!question]- Diferencie el método inductivo del deductivo con un ejemplo de cada uno.
> El inductivo va del detalle a lo general: "hay que guardar fotos, así que agrego un almacenamiento de objetos". El deductivo va de lo general al detalle: "hay que atender 1.000 usuarios por minuto, así que necesito un balanceador y concurrencia".

> [!question]- ¿Cuánto descuenta no poner interfaces y cuánto no usar un estilo declarado?
> No poner interfaces descuenta 6 puntos. Cada estilo justificado que no aparece en el diagrama descuenta 3.

> [!question]- ¿Qué es un "componente desagregado" y cuándo se acepta?
> Un componente sin conexiones con el resto. Se descuenta salvo que haya una justificación aparente (por ejemplo, un job independiente anotado como tal).

> [!question]- ¿Qué tipo de falencias no se aceptan en la pregunta de falencias?
> Las de formato del diagrama o del tipo "me faltó explotar un componente". Se esperan falencias de la solución: puntos únicos de falla, cuellos de botella, problemas de consistencia o seguridad, con su solución y sus implicancias.

> [!question]- ¿Cómo se dibuja un pub/sub en un diagrama de componentes?
> Con un broker al centro que provee interfaces de publicación y de suscripción: el publisher requiere `iPublish` del broker y cada subscriber requiere `iSubscribe`. Publisher y subscribers no se conectan entre sí.

> [!question]- En el caso de telemedicina, ¿qué atributos y estilos se eligen y por qué?
> Seguridad (fichas médicas sensibles), integrabilidad (centros médicos y un proveedor de videollamadas externo) y escalabilidad (se espera que crezcan los centros). Estilos: cliente-servidor, por el frontend y el backend separados para pacientes y profesionales, y capas en el backend, para separar presentación, lógica y datos.
