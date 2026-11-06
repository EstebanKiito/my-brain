---
ramo: "Arquitectura de Sistemas de Software"
tema: "Características arquitectónicas y escenarios"
tags:
  - arquisis/atributos
  - arquisis/tacticas
  - origen/complemento
prerrequisitos:
  - "[[02 - Escenarios de calidad de Bass Clements y Kazman]]"
---

# Decisiones relevantes y tácticas arquitectónicas

Con los atributos priorizados y los escenarios escritos, falta decidir **cómo** cumplirlos. Bass y Kazman ordenan las decisiones arquitectónicas en seis categorías, y llaman **táctica** a cada decisión concreta que mueve la respuesta de un atributo. Las tácticas son lo que se evalúa al pedir "qué medida implementaría".

## Categorías de decisiones relevantes

| Categoría | Preguntas que responde |
|---|---|
| **Allocation of responsibilities** (asignación de responsabilidades) | ¿Qué debe hacer el sistema en cada nivel? ¿Quién se hace o puede hacerse cargo de qué? |
| **Coordination model** (modelo de coordinación) | ¿Qué debe coordinarse con qué? ¿Qué recursos se consumen? ¿Con qué concurrencia y a qué costo? |
| **Data model** (modelo de datos) | Tipos, propiedades, metadata, almacenamiento y organización de los datos |
| **Mapping** (mapeo) | Entre qué elementos, ¿sincrónico o asincrónico? Ley de Conway |
| **Binding time decisions** (momento de ligado) | ¿Cuándo se fija cada decisión: en diseño, en despliegue, en ejecución? Influyen el mercado, el tiempo, la coordinación y el manejo de recursos |
| **Elección de tecnología** | El stack, el soporte del equipo, el soporte operacional y los efectos secundarios |

**Ejemplo de *binding time*:** el proveedor de pagos puede fijarse en el código (diseño), en un archivo de configuración (despliegue) o elegirse por cliente en tiempo de ejecución. Mientras más tarde se fija, más flexible es el sistema, pero más complejo.

## Tácticas arquitectónicas

> [!tip] Táctica (Bass, Clements y Kazman)
> "**Decisión de diseño que afecta a la respuesta de un atributo de calidad.**"
> **El escenario fija la promesa; la táctica es cómo se cumple.**

**Toda táctica compra un atributo y cobra otro**, y el escenario dice si el precio es aceptable:

| Táctica | Compra | Cobra |
|---|---|---|
| **Caché** | Latencia (performance) | Frescura y consistencia: el navegador puede mostrar una versión vieja sin preguntar |
| **Redundancia** | Disponibilidad | Costo y complejidad |
| **Cola de mensajes** | Tolerancia a fallos, desacople | Consistencia inmediata y simplicidad |
| **Cifrado** | Seguridad | Performance (CPU, latencia) |
| **Inyección de dependencias** | Mantenibilidad y flexibilidad | Velocidad de desarrollo inicial |

> [!example]- Del escenario a la táctica
> **Escenario:** si cae una zona de disponibilidad en operación normal, el servicio se restablece en menos de 30 s.
> **Táctica:** redundancia multi-zona (≥ 3) con health checks y failover automático.
> **Tradeoff:** unas 3 veces la infraestructura, más coordinación y complejidad operacional.
> Sin la táctica, "restablecido en < 30 s" es solo una opinión al aire.

## En qué fijarse con los NFR

- **No son necesariamente excluyentes ni independientes**: mejorar uno puede ayudar o perjudicar a otro.
- **Algunos pueden ser vagos** ("usable"). Hay que asignarlos como responsabilidad del equipo y bajarlos a escenarios.
- **Cómo encontrarlos:** en el curso, relacionándolos con el enunciado. En el trabajo, preguntándose qué se prioriza.
- **Cada atributo es una promesa.**

## ¿Son valiosos los atributos?

Sí, pero con cuidado:
- Muestran las **"funcionalidades globales"** de la aplicación.
- Cumplir todos sería lo ideal, pero **no siempre es factible**.
- **Un atributo sin métrica pierde sustentabilidad.**
- **Demasiados atributos limitan la capacidad de acción; muy pocos limitan la utilidad.** Hay que saber cuándo elegirlos y cuáles priorizar.

> [!warning] Proponer una táctica sin su costo
> En las pautas, una táctica nombrada sin el atributo que sacrifica queda incompleta. Por ejemplo: "uso caché para mejorar la performance; a cambio, los datos pueden quedar desactualizados, así que defino un TTL de 60 s, aceptable porque los precios cambian una vez al día".

## Preguntas de repaso

> [!question]- Defina táctica arquitectónica y explique su relación con el escenario.
> Es una decisión de diseño que afecta la respuesta de un atributo de calidad. El escenario fija la promesa medible, y la táctica es el mecanismo que permite cumplirla. El escenario también dice si el costo de la táctica es aceptable.

> [!question]- ¿Qué compra y qué cobra la redundancia?
> Compra disponibilidad, porque si un nodo falla otro responde. Cobra costo (más infraestructura) y complejidad (sincronizar y coordinar réplicas, hacer failover).

> [!question]- Dé un ejemplo de decisión de "binding time".
> Elegir el proveedor de pagos en tiempo de diseño (en el código), en el despliegue (configuración) o en ejecución (por cliente). Ligarlo tarde da flexibilidad, pero agrega complejidad y más casos que probar.

> [!question]- ¿Qué pregunta responde la categoría "coordination model"?
> Qué componentes deben coordinarse entre sí, qué recursos consumen y con qué concurrencia y costo. Por ejemplo, si dos servicios se comunican de forma sincrónica por REST o asincrónica por una cola.

> [!question]- ¿Por qué tener demasiados atributos priorizados es un problema?
> Porque muchos se contraponen (seguridad contra performance, consistencia contra disponibilidad) y no se pueden cumplir todos a la vez. Se pierde capacidad de decidir y se diluye el foco del diseño.

> [!question]- Proponga una táctica para el escenario "p95 < 300 ms al consultar el catálogo en peak" e indique su costo.
> Cachear las consultas del catálogo (Redis o CDN) con un TTL corto. Baja la latencia y la carga sobre la base, a cambio de que un cambio de precio pueda tardar hasta el TTL en reflejarse y de operar la caché.

> [!question]- V o F: "Una buena táctica mejora un atributo sin perjudicar a ningún otro".
> Falso. Toda táctica compra un atributo y cobra otro: la caché sacrifica frescura, la redundancia costo y complejidad, el cifrado performance. Lo que se busca es que el precio sea aceptable para el escenario.
