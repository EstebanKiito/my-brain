---
ramo: "Arquitectura de Sistemas de Software"
tema: "Otros estilos arquitectónicos"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[03 - Máquinas virtuales y cliente-servidor]]"
---

# Intérprete y código móvil

Cuando se escribe `SELECT * FROM pedidos`, la base de datos no ejecuta ese texto directamente: un **intérprete** lo traduce a operaciones. Cuando se abre una página web, el navegador descarga JavaScript y lo ejecuta localmente: eso es **código móvil**. Los dos estilos tratan **instrucciones como datos** que otro componente ejecuta.

## Intérprete

> [!tip] Intérprete
> El intérprete **parsea y ejecuta comandos de entrada** y **actualiza el estado** que mantiene. Componentes: el **intérprete de comandos**, el **programa** o estado que se interpreta y la **interfaz de usuario** por donde entran los comandos.

La gracia de este estilo es que el sistema tome mensajes (comandos) y los ejecute en algún programa: **el intérprete es el que traduce**.

**Ejemplos:**
- **SQL:** se envía un `SELECT` y el motor interpreta qué buscar, filtrar, agrupar y devolver.
- **Lenguajes de programación:** el código es la "interfaz" y el compilador o intérprete lo traduce. Python (CPython) y JavaScript se interpretan; en Java o C, el compilador transforma a binario lo necesario.
- **Bash:** una terminal que lee comandos, los traduce y hace las llamadas al sistema.

**Ventaja:** ofrece una interfaz mucho más fácil que manejar el sistema por debajo. Es fácil de usar, **flexible** y **portable** (Python corre en todos lados).

## Código móvil

> [!tip] Código móvil
> **Un elemento de datos se transforma dinámicamente en un componente que procesa datos**: software que puede **ejecutarse en múltiples nodos sin instalarlo ni compilarlo**, transmitido por la red. Lenguajes típicos: JavaScript, Java y Dart.

- **Datos:** el código como dato (bundles, archivos). **Topología:** vía red.
- **Variantes** (Fuggetta, Picco y Vigna, 1998):
  - **código bajo demanda**: el cliente descarga y ejecuta (JavaScript en el navegador);
  - **evaluación remota**: se envía código para que lo ejecute otro nodo;
  - **agentes móviles**: código que se mueve entre nodos, por ejemplo agentes de monitoreo.
- **Contenedores:** la **imagen es el código móvil** y el runtime es la máquina virtual.

**Ejemplo de la web:** los archivos estáticos (HTML, JS, CSS) se suben a un **S3**, que los distribuye por una **CDN** en todo el mundo. El navegador pide los archivos a la CDN, los recibe, los lee y **ejecuta el JavaScript** localmente. Otros ejemplos son Flutter, la JVM y **WebAssembly (WASM)**.

![Croquis de intérprete y de código móvil](adjuntos/Intérprete%20y%20código%20móvil.png)

> [!example]- Transcripción de la imagen
> - Izquierda, **Intérprete**: **UI** → **Intérprete** → **Programa**, conectados por interfaces.
> - Derecha, **Cod. Móvil**: **Code Senders** → **Motor ejec** (motor de ejecución) → **Estados de Sistem** (estados del sistema).

| Pros | Contras |
|---|---|
| **Portabilidad suprema** | **Riesgo de seguridad**: ¿de dónde viene ese código? (OWASP, *unsafe mobile code*) |
| **Contenido mejorado**: dinámico e interactivo | **Privacidad**: una página insegura puede ejecutar JS que robe cookies o lea el `localStorage` |
| **Reduce la carga de transmisión** en ciertos escenarios: se cachean los archivos estáticos en el navegador | **Compatibilidad**: hay que trabajar una base por plataforma |
| | **Performance**: más intermediarios |

**Máquinas virtuales y código móvil:** el código móvil puede correr sobre una máquina virtual (el sandbox del navegador, la JVM). Eso **ayuda a la seguridad**, porque aísla el código, y aún más a la **portabilidad**.

> [!warning] Cuándo no aplican en una prueba
> Las pautas marcan **código móvil como no válido** si el caso no tiene inyección ni traspaso de código ("no se pide ejecución en múltiples ambientes"), y el **intérprete como no válido** si no hay comandos que traducir. Sí aplica código móvil, por ejemplo, para distribuir una app a muchos dispositivos mediante un servidor de distribución (casi una CDN).

## Preguntas de repaso

> [!question]- ¿Qué hace un intérprete y qué componentes tiene?
> Parsea y ejecuta comandos de entrada y actualiza el estado que mantiene. Sus componentes son la interfaz por donde entran los comandos, el intérprete que los traduce y el programa o estado sobre el que actúan.

> [!question]- ¿Por qué SQL se considera un ejemplo del estilo intérprete?
> Porque el usuario envía instrucciones declarativas (`SELECT … WHERE …`) y el motor de la base las interpreta y las traduce a operaciones concretas: buscar, filtrar, agrupar y devolver.

> [!question]- Defina código móvil y nombre sus tres variantes.
> Es código que viaja por la red como dato y se ejecuta en otro nodo sin instalarse ni compilarse. Variantes: código bajo demanda, evaluación remota y agentes móviles.

> [!question]- Describa el flujo de código móvil en una aplicación web servida por CDN.
> Los archivos estáticos (HTML, CSS, JS) están en S3 y se distribuyen por una CDN. El navegador los pide a la CDN más cercana, los recibe y ejecuta el JavaScript localmente. Los archivos quedan cacheados para la próxima visita.

> [!question]- ¿Cuál es el principal riesgo del código móvil y cómo se mitiga?
> La seguridad: se ejecuta código cuyo origen puede no ser confiable, capaz de robar cookies o datos. Se mitiga ejecutándolo en un sandbox o máquina virtual (navegador, JVM), verificando su origen y firma, y con políticas como CSP.

> [!question]- ¿Por qué se dice que en contenedores "la imagen es el código móvil"?
> Porque la imagen es un paquete de código y dependencias que viaja por la red (desde un registry) y se ejecuta en cualquier nodo con el runtime, sin instalar ni compilar nada en ese nodo.

> [!question]- V o F: "El código móvil siempre mejora la performance porque ejecuta en el cliente".
> Falso. Puede reducir la carga de transmisión en algunos escenarios, pero agrega intermediarios y depende de la capacidad del dispositivo. Además, trae costos de seguridad y compatibilidad.
