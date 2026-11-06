---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos estructurales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[01 - Mantenibilidad y flexibilidad]]"
---

# Portabilidad e interoperabilidad

Los otros dos atributos estructurales miran hacia afuera del código. La **portabilidad** pregunta si el sistema puede correr en otro lugar. La **interoperabilidad** (o integrabilidad) pregunta si puede conversar con otros sistemas. Al final, un caso de capas muestra cómo leer qué atributos favorece una arquitectura.

## Portabilidad

> [!tip] Portabilidad
> Capacidad de **funcionar en variedad de sistemas y plataformas con modificaciones mínimas**. La pregunta guía es: ¿mi aplicación correrá siempre en el mismo tipo de servidor?

Distintos sistemas operativos funcionan distinto, así que hay que decidirlo explícitamente.
- Se apoya en la **cohesión de los componentes**: lo dependiente de la plataforma queda aislado.
- **Flutter y React Native:** con un mismo código se compilan aplicaciones para Android y para iOS (Flutter genera los binarios de cada plataforma).
- **Contenedores (Docker):** empaquetan la aplicación con sus dependencias y corren igual en cualquier máquina con un motor de contenedores, compartiendo el kernel del host. Son parecidos a las máquinas virtuales, pero más livianos. En el proyecto del curso, todos los sistemas se levantan contenerizados.

> [!warning] Portabilidad mal justificada
> "Es una app móvil, así que priorizo portabilidad" no basta. Vale si el caso exige correr en ambientes distintos (Android e iOS, varios sistemas operativos, distintos proveedores de nube) y se justifica con el enunciado.

## Interoperabilidad / integrabilidad

> [!tip] Interoperabilidad
> Capacidad de **interactuar con otros sistemas** e **intercambiar información**, usando **interfaces o contratos** claros y explícitos.

- **APIs:** un conjunto de funciones parametrizadas que controlan el acceso a los datos y garantizan la integridad de los datos y las reglas de negocio.
- Requiere un entendimiento **sintáctico** (cómo decirlo: el formato) y **semántico** (qué se dice: el significado).
- Se transfiere información relevante para la operación: sistemas de sistemas, plugins.
- Un sistema puede **ofrecer** datos, **recibirlos** o ambas cosas, por ejemplo como parte de una cadena de procesamiento.
- **Es especial en la industria:** B2B, SaaS, salud (la conexión entre Fonasa e Imed), gobiernos, domótica, ERPs.

### Dos casos opuestos

| | GitHub | Core bancario |
|---|---|---|
| Contrato | **Publicado en OpenAPI** | Especificación en un **contrato legal en papel** |
| Acceso | **Credenciales self-service** y límites de uso claros | **Ambiente de pruebas con cita previa** |
| Mecanismos | REST-like y webhooks | **Batches por SFTP** en ventana nocturna |
| Documentación | Pública y actualizada | **Muerta en un PDF**, o en la cabeza de quien ya se jubiló |
| Cambios | Versionados | Cada cambio de campo es un proyecto entre organizaciones |
| **Veredicto** | Un desconocido (o un agente) logra **su primera llamada exitosa en unas horas, sin hablar con nadie** | **Semanas** hasta la primera integración, la mayoría en reuniones |

Aunque parezca valioso solo hacia el exterior, es **igual de válido dentro de una organización**: los equipos internos también se integran entre sí.

### Preguntas clave

- ¿Conocemos los sistemas con los que queremos integrarnos? ¿Nos interesa hacerlo?
- ¿Podemos implementar una interfaz adecuada?
- ¿Podemos soportar la complejidad añadida?
- ¿Ofrecemos seguridad en nuestras interacciones?
- **¿Cuánto tiempo demora nuestro cliente en hacer su primera integración?** Esta es una buena métrica.

## Caso: arquitectura de capas

![Clientes, servidor web, servidor de aplicación y bases de datos en capas](adjuntos/Caso%20de%20arquitectura%20de%20capas.png)

> [!example]- Transcripción de la imagen
> - **Client Tier:** tres *Web Client*. **Web Server Tier:** un *Web Server*. **Business Logic Tier:** un *Application Server*. **Data Management Tier:** *Databases*. Flechas dobles conectan cada capa con la siguiente.
> - Características: **modularidad** (separación de temas), **comunicación sincrónica** entre capas (request, wait, answer), **implantación flexible** (capas independientes, distribuidas y heterogéneas) y un gran número de clientes con solicitudes concurrentes que requieren poco tiempo de proceso.

![Tabla con los atributos que favorece la arquitectura de capas](adjuntos/Atributos%20que%20favorece%20la%20arquitectura%20de%20capas.png)

> [!example]- Transcripción de la imagen
> | Atributo | Ventajas |
> |---|---|
> | Disponibilidad | Réplica de servidores en cada capa: si uno falla, los otros responden. La QoS disminuye hasta restaurar el servidor caído |
> | Manejo de fallas | Los servidores web y de aplicación implementan recuperación transparente: el cliente se redirige a un servidor replicado |
> | Flexibilidad | La modularidad facilita el cambio por la encapsulación; el impacto de un cambio en una capa debería ser mínimo en las otras |
> | Desempeño | Alto desempeño con replicación (threads concurrentes); se recomienda minimizar las llamadas entre capas |
> | Escalabilidad | Escala bien porque los servidores pueden replicarse; en la práctica, la gestión de datos se vuelve el cuello de botella |

**Lectura con los atributos estructurales:**
- **Mantenibilidad: sí.** Si hay un error en una capa, se va solo a esa capa.
- **Flexibilidad: sí, en parte.** Se pueden agregar capas intermedias que hagan otras cosas.
- **Interoperabilidad: no se prioriza.** La arquitectura no muestra contratos hacia otros sistemas.
- **Portabilidad: no se prioriza.** No hay nada que permita ejecutar en varias plataformas (salvo que se agreguen contenedores).

## Preguntas de repaso

> [!question]- ¿Qué tecnologías favorecen la portabilidad según el curso y por qué?
> Flutter y React Native, que generan apps para Android e iOS desde un mismo código, y los contenedores, que empaquetan la aplicación con sus dependencias para que corra igual en cualquier máquina con un motor de contenedores.

> [!question]- ¿Qué diferencia el entendimiento sintáctico del semántico en interoperabilidad?
> El sintáctico es acordar el formato (cómo se dice: JSON, campos, tipos). El semántico es acordar el significado (qué se dice: qué representa "estado = 2"). Sin ambos, los sistemas se conectan pero se malinterpretan.

> [!question]- Compare la interoperabilidad de GitHub con la de un core bancario tradicional.
> GitHub publica su contrato en OpenAPI, entrega credenciales self-service, tiene límites claros y webhooks: un desconocido se integra en horas sin hablar con nadie. El core bancario usa batches nocturnos por SFTP, documentación muerta y contratos en papel: la integración tarda semanas, en su mayoría en reuniones.

> [!question]- ¿Qué buena métrica propone el curso para la interoperabilidad?
> El tiempo que tarda un cliente nuevo en lograr su primera integración exitosa.

> [!question]- En la arquitectura de capas, ¿qué atributos estructurales se favorecen y cuáles no?
> Se favorecen la mantenibilidad (un error se localiza en una capa) y la flexibilidad (se pueden agregar capas intermedias). No se priorizan la interoperabilidad ni la portabilidad, porque nada en la arquitectura apunta a ellas.

> [!question]- Según la tabla del caso de capas, ¿dónde suele estar el cuello de botella al escalar?
> En la gestión de datos: las capas web y de aplicación se replican fácilmente, pero todas terminan consultando la misma capa de bases de datos.

> [!question]- V o F: "La interoperabilidad solo importa cuando el sistema se integra con empresas externas".
> Falso. Es igual de válida dentro de una organización: los equipos y sistemas internos también se integran, y contratos claros ahorran tiempo y reuniones.
