---
ramo: "Arquitectura de Sistemas de Software"
tema: "Resolución de casos de diseño"
tags:
  - arquisis/casos
  - arquisis/uml
  - origen/complemento
prerrequisitos:
  - "[[01 - Método para resolver un caso de prueba]]"
  - "[[03 - Notación del diagrama de componentes UML]]"
---

# Diagramas de referencia MichiGuardian y Fundación SCP

La mejor forma de aprender a diagramar es leer diagramas de referencia de las pautas. Esta nota analiza dos: **MichiGuardian** (pub/sub, serverless y Bluetooth) y **Fundación SCP** (pipe & filter con notificaciones). Ambos muestran cómo se ven en UML las decisiones de las preguntas d y e.

## Caso MichiGuardian (I1 2021-2)

**Resumen:** un collar con **BLE** (Bluetooth de bajo consumo) emite constantemente una identificación. Si la mascota está marcada como perdida y un celular con la app la detecta, se avisa al dueño discretamente con la posición aproximada, y si varios la detectan, se **triangula**. La beta tiene unos **10.000 usuarios**. Hay que notificar, hacer seguimiento, conectarse con los servicios de notificaciones de **Google y Apple**, usar **serverless** donde convenga y ser agnóstico al proveedor de nube.

- **Atributos:** escalabilidad (10.000 usuarios), performance (velocidad de las notificaciones), disponibilidad, confiabilidad, usabilidad (muchas interfaces). Integrabilidad, poca. **Inválidos:** reusabilidad, portabilidad, mantenibilidad, testeabilidad.
- **Estilos:** **pub/sub** para las notificaciones (código basado en eventos) y **cliente-servidor** para lo básico. Pizarra no aplica.

![Diagrama de referencia de MichiGuardian](adjuntos/Diagrama%20de%20referencia%20de%20MichiGuardian.png)

> [!example]- Transcripción de la imagen
> - **Cloud:** una *App principal* con un *Servicio de triangulación*, los componentes *Mascotas* y *Collares*, el sistema *Usuarios* y una *DB*, expuesta por un *WSGI + webserver* (HTTPS). Un bloque **Serverless** con *Emisor de correos* y *Emisor de notificaciones*, conectados a un **Broker de notificaciones** (`Ipublish`, `Isubscribe`).
> - Externos: **Apple Notification System** y **Firebase Cloud Messaging**, que publican y se suscriben.
> - **Usuario:** una *App móvil* con *Suscriptor de notificaciones*, *Handler requests*, *Controlador de estado*, *Motor gráfico*, *Almacén de sesión*, *Polling de dispositivos*, *BLE stack* y una *caché de IDs en búsqueda*, más un *Receptor de notificaciones propietario*.
> - **Mascota:** el *Collar* con *BLE stack*, *Sistema de pareo*, *Beacon publisher* y *Almacén de ID propio*, conectado a la app por **Bluetooth**.

**Qué enseña:**
- Las **fronteras** (Cloud, Usuario, Mascota) se dibujan como paquetes, y los sistemas externos quedan fuera.
- El **broker de notificaciones** es el centro del pub/sub: publican el backend y los servicios externos, y se suscriben las apps.
- El **serverless** se usa para tareas puntuales (correos, notificaciones), que escalan sin servidores dedicados.
- **Variante:** si Apple ofrece notificar a un endpoint propio cada hallazgo, se agrega un **adaptador** hacia el pub/sub, idealmente un **worker asíncrono** que procese esas peticiones.

## Caso Fundación SCP (I1 2021-2)

**Resumen:** una IA peligrosa (SCP-079) recibe un acceso limitado a internet. Hay que diseñar un sistema que **revise la correctitud de las peticiones**, **autorice** las conexiones a fuentes de datos, **transforme en inocuos** los intercambios dañinos y **notifique** a varios investigadores.

- **Estilo esperado:** **pipe & filter**, con varios filtros que limitan el acceso, impiden excepciones y filtran las entradas y salidas, más un **sistema de notificaciones** asociado a los filtros cruciales, y ojalá una abstracción de varios filtros secuenciales.

![Diagrama de referencia de Fundación SCP con pipe and filter](adjuntos/Diagrama%20de%20referencia%20de%20Fundación%20SCP%20con%20pipe%20and%20filter.png)

> [!example]- Transcripción de la imagen
> - **Site-15:** la entidad **SCP-079** (con su *Network requests adaptor* y la *AI*) se conecta a un **Sistema supervisor de conexión**.
> - Dentro, un subsistema **Sistema de filtros** con *Filtro 1 … Filtro n* encadenados hacia una *Cola requests* y un *Autorizador*, y en la vuelta un *Filtro formato* y un *Filtro contenido*. Un *Requests handler* sale por HTTP a las **Fuentes de datos** externas.
> - Arriba, un *Sistema supervisor de registro* con *DB logs*, un **Broker de notificaciones** y un *Manager de autorizaciones* con su *DB de autorizaciones pendientes*, conectados a la **Consola del supervisor**.
> - Nota: hay autorizaciones automáticas en el manager para ciertas fuentes predeterminadas.

**Qué enseña:**
- Pipe & filter **filtra** (formato, contenido, autorización): es exactamente el uso que aceptan las pautas.
- Los filtros se encapsulan en un **subsistema** con interfaces de entrada y salida, en ambas direcciones (petición y respuesta).
- **¿Serverless?** Sí es posible: las reglas y chequeos pueden ser funciones atómicas que consultan bases de reglas y escalan ante demandas arbitrarias. Pero hay que **limitar las peticiones y monitorear**, porque el ente contenido podría abusar.

## Preguntas de repaso

> [!question]- En MichiGuardian, ¿qué estilos se esperan y qué responsabilidad cubre cada uno?
> Pub/sub para las notificaciones a los dueños y la integración con los servicios de Apple y Google, y cliente-servidor para las funciones básicas de la app con el backend.

> [!question]- ¿Cómo se incorpora el endpoint de Apple para hallazgos en el diagrama?
> Con un adaptador que reciba las notificaciones de Apple y las publique en el sistema pub/sub, idealmente mediante un worker asíncrono que procese esas peticiones sin bloquear al resto.

> [!question]- ¿Por qué pipe & filter es el estilo correcto para Fundación SCP?
> Porque el problema es filtrar: revisar, autorizar y sanear peticiones y respuestas en etapas sucesivas. Cada filtro tiene una responsabilidad simple y encadenable, que es el uso que las pautas aceptan para pipe & filter.

> [!question]- ¿Por qué el diagrama de MichiGuardian separa Cloud, Usuario y Mascota?
> Para mostrar dónde se despliega cada componente (en la nube, en el celular, en el collar) y qué conexiones cruzan esas fronteras (HTTPS, Bluetooth, pub/sub). Así quedan claros los límites y los protocolos entre los entornos.

> [!question]- ¿Es posible usar serverless en Fundación SCP? ¿Con qué precaución?
> Sí: los chequeos y las reglas pueden ser funciones que escalan según la demanda de los investigadores. Pero hay que limitar las peticiones y monitorear constantemente, porque el agente contenido podría abusar del sistema y generar costos o accesos indebidos.

> [!question]- ¿Qué atributos no son válidos en MichiGuardian según la pauta?
> Reusabilidad, portabilidad, mantenibilidad y testeabilidad, porque el enunciado no da razones para priorizarlos frente a la escalabilidad, la performance y la disponibilidad de las notificaciones.
