---
ramo: "Arquitectura de Sistemas de Software"
tema: "Estilos jerárquicos y de capas"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[02 - Main y subrutinas y arquitectura en capas]]"
  - "[[02 - Arquitectura cliente-servidor]]"
---

# Máquinas virtuales y cliente-servidor

Las capas tienen dos variantes muy usadas. La **máquina virtual** encapsula una capa completa para ofrecer un entorno de ejecución "hacia arriba", y es la base de la nube y de los contenedores. **Cliente-servidor** reduce las capas a dos y es probablemente el estilo más común hoy. Ambas se cuentan como pocas quantas, y eso es lo primero que hay que saber decir de ellas.

## Máquina virtual

Si una de las capas está **encapsulada** y ofrece recursos a las de arriba, se está describiendo una **máquina virtual**. Es la capacidad de **proveer recursos a múltiples sistemas o subsistemas completos en una máquina física**, como un servicio "hacia arriba". Es el gran sustento de la infraestructura actual, incluida la nube.

**Componentes:** los programas que se ejecutan, el motor de ejecución, el estado de los programas y el estado interno del motor. **Conectores:** llamadas a procedimientos. **Topología:** capas cerradas o un grafo acíclico dirigido.

| Tipo | Ejemplos |
|---|---|
| **Hipervisor tipo 1** (sobre el hardware) | Xen, Hyper-V |
| **Hipervisor tipo 2** (sobre un sistema operativo) | VMware, VirtualBox |
| **Contenedores** | Docker, runc |

![Máquinas virtuales sobre una capa de virtualización](adjuntos/Máquinas%20virtuales%20sobre%20una%20capa%20de%20virtualización.png)

> [!example]- Transcripción de la imagen
> - Croquis: tres columnas sobre una base **Virtualización**. La primera muestra sus capas internas (**API**, **Lib**, **OS**) y las otras dos son **VM**.
> - Cada columna se conecta a la capa de virtualización mediante una interfaz.

![Servidor con máquinas virtuales frente a servidor con contenedores Docker](adjuntos/Máquinas%20virtuales%20frente%20a%20contenedores.png)

> [!example]- Transcripción de la imagen
> - **Server with virtual machines:** Host OS → Hypervisor → dos VM, cada una con su **Guest OS**, sus binarios y librerías y la aplicación.
> - **Server with Docker containers:** Host OS → binarios y librerías compartidos → **Docker** → tres contenedores con su aplicación, sin sistema operativo invitado.

- Una **VM** virtualiza el hardware completo: cada una levanta todo un sistema operativo.
- Un **contenedor** comparte el **kernel** del sistema anfitrión: solo empaqueta binarios y librerías, y necesita un motor (Docker, Kubernetes). Es más liviano.
- **Ojo con la arquitectura del procesador:** código compilado para x86 puede no ejecutarse en ARM, y viceversa. Hay que pedirle a Docker que construya para la plataforma correcta.

| Pros | Contras |
|---|---|
| **Portabilidad**: funciona en más sistemas | **Overhead**: redundancia y menos performance |
| **Seguridad** (±): la máquina anfitriona queda protegida; la virtualizada asume el riesgo de su uso | Menor **eficiencia** y **costo** elevado |

## Cliente-servidor

**Dos capas: cliente y servidor.** Es la variante de capas más común hoy: el frontend y el backend.
- **Conocimiento asimétrico:** el servidor no conoce a los clientes a priori (después puede usar identificadores); los clientes sí conocen al servidor. Es una relación **1-N**.
- El servidor es **stateless** respecto de los clientes.

**Comunicación:**
- **REST.**
- **RPC** (*Remote Procedure Call*): el cliente invoca un método que se ejecuta remotamente **como si fuera local** y espera la respuesta. El servidor define funciones (`suma(a, b)`) y el cliente las llama (`servidorRPC.suma(a, b)`). Permite descargar procesamiento al servidor (*off-loading*) y tener clientes livianos (*thin client*).
- Para eso, el cliente **conoce la interfaz**, sabe **empaquetar y desempaquetar** los datos para la red (*marshalling* y *unmarshalling*) y **conoce la dirección del servidor**. El **stub** es el código del lado del cliente que hace todo eso y oculta la red.

**Ejemplos:** arquitectura web, SMTP, APIs web, servidores de juegos (Unity) y streaming de video.

| Pros | Contras |
|---|---|
| **Confiable**: apto para introducir mecanismos de confiabilidad | **Centralización**: en su forma básica es un **punto único de falla (SPOF)** |
| **Sencillo y probado** | **Muy pesado en términos de red** |
| **Altamente mantenible** | Puede crecer en tamaño fácilmente si no se controla |

> [!warning] "Cliente-servidor porque hay frontend y backend" no suma
> Las pautas lo consideran **demasiado general** si se justifica solo porque existe un front y un back: casi todo sistema lo tiene. Vale si se le asigna una **responsabilidad concreta**: por ejemplo, una IA en un servidor aparte que atiende inferencias, o la sección donde los lectores acceden a los datos por una única API.

**Quantas:** cliente-servidor es **1 quanta**: si cae el servidor, cae todo. En virtualización, el número de capas encapsuladas (VMs o contenedores independientes) puede dar **N quantas**.

## Preguntas de repaso

> [!question]- ¿Qué convierte a una capa en una máquina virtual?
> Que esté encapsulada y provea un entorno de ejecución completo "hacia arriba", de modo que varios sistemas corran sobre ella como si tuvieran su propia máquina. Ejemplos: hipervisores y motores de contenedores.

> [!question]- Diferencie una VM de un contenedor.
> La VM virtualiza el hardware y cada una levanta su propio sistema operativo, sobre un hipervisor. El contenedor comparte el kernel del anfitrión y solo empaqueta la aplicación con sus binarios y librerías, sobre un motor como Docker: es más liviano y arranca más rápido, pero aísla menos.

> [!question]- Dé un ejemplo de hipervisor tipo 1 y uno tipo 2.
> Tipo 1, que corre directo sobre el hardware: Xen o Hyper-V. Tipo 2, que corre sobre un sistema operativo: VMware Workstation o VirtualBox.

> [!question]- ¿Qué hace un stub en RPC?
> Es el código del lado del cliente que expone la función remota como si fuera local: empaqueta los argumentos (marshalling), los envía al servidor, espera la respuesta y la desempaqueta (unmarshalling).

> [!question]- ¿Cuál es el principal riesgo de cliente-servidor y cuántas quantas tiene?
> Que el servidor es un punto único de falla: si cae, todos los clientes quedan sin servicio. En su forma básica es una sola quanta.

> [!question]- V o F: "Cliente-servidor siempre es un estilo válido en una prueba porque todo sistema tiene frontend y backend".
> Falso. Las pautas lo consideran muy general con esa justificación. Hay que asignarle una responsabilidad concreta del problema (por ejemplo, un servicio de IA en un servidor dedicado).

> [!question]- ¿Por qué una imagen construida en x86 puede fallar en un servidor ARM?
> Porque el contenedor comparte el kernel y ejecuta binarios nativos del procesador: si fueron compilados para otra arquitectura, no corren. Hay que construir imágenes multiplataforma o para la arquitectura de destino.
