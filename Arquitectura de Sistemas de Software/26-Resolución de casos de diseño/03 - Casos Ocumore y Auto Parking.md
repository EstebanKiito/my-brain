---
ramo: "Arquitectura de Sistemas de Software"
tema: "Resolución de casos de diseño"
tags:
  - arquisis/casos
  - origen/complemento
prerrequisitos:
  - "[[01 - Método para resolver un caso de prueba]]"
  - "[[03 - Tácticas de performance de Bass y Kazman]]"
---

# Casos Ocumore y Auto Parking

Dos casos donde las preguntas giran en torno a **delegar acceso**, **bases de datos**, **tácticas de performance y escalabilidad** y **seguridad**. Ocumore (I2 2024-2) muestra un caso donde pub/sub **no suma** porque hace falta un mediador. Auto Parking (I2 2025-2) es un caso de carga masiva de video.

## Caso Ocumore: micro cursos generados desde muchas fuentes

**Resumen:** el sistema arma micro cursos a partir de una solicitud. Un **enjambre de workers** con acceso a internet recoge material desde muchos protocolos (web, DAV, FTP, SFTP). Un sistema **gestiona y entrega bajo demanda** el acceso a los recursos. El solicitante trabaja en **modo manual** (entrega DOIs, URLs e ids y sube documentos) o en **modo IA** (conversa con una IA preconstruida que opera los sistemas). El curso se envía a un **LMS** (Canvas) por **LTI o SCORM**, y todo debe completarse **en menos de 10 minutos para 300 recursos**.

| Pregunta | Respuesta esperada |
|---|---|
| **a)** El operador debe delegar acceso a plataformas a las que solo él accede (seguridad y performance) | **OAuth2**: el operador autoriza y el sistema recibe un token con alcance limitado, sin compartir credenciales. Hay que describir una implementación adecuada |
| **b)** Bases de datos y cómo componer consultas complejas | Al menos una **relacional transaccional**, complementada con algo que guarde archivos: **documental** o almacenamiento tipo **S3**. Explicar cómo se cruzan, por ejemplo por ids |
| **c)** Al menos 4 tácticas de performance y escalabilidad | **Tácticas de Bass y Kazman**: múltiples copias de cómputo (workers), concurrencia, colas limitadas, caché de fuentes ya descargadas, priorización, timeouts, infraestructura elástica. Cada una con dónde y por qué |
| **d)** Características | **Confiabilidad** (mucha documentación y archivos), **escalabilidad** (muchos workers y fuentes), **integrabilidad** (literalmente se integra con LMS y fuentes). Elasticidad, bien justificada |
| **e)** Estilos | **Suman:** mediator (coordina el ensamblado), EDA con workers, cliente-servidor en la UI y los consumidores. **No suman:** capas (restringe flexibilidad y escalabilidad), **pub/sub** (aquí debe haber un mediador) y pipe & filter (complica sin necesidad). **No aplican:** pizarra, main y subrutinas |

> [!warning] Pub/sub no siempre suma
> En Ocumore hay un flujo con pasos que dependen entre sí (recoger fuentes → ensamblar → publicar en el LMS) con un plazo de 10 minutos: hace falta **coordinar**, es decir, un **mediator** u orquestador. Un pub/sub sin coordinación no garantiza el orden ni el plazo.

## Caso Auto Parking: cobro de estacionamientos con cámaras

**Resumen:** miles de cámaras envían **video en streaming** a una central. Una IA detecta cuándo se estaciona o sale un auto y lee la patente. Al salir, se calcula el tiempo y se obtiene el correo del dueño desde la API del registro de tránsito para cobrarle. Si no se detecta la patente, se genera un **ticket** de revisión manual. Los usuarios ven sus cobros en una web, pagan por varios medios o inscriben su tarjeta (convenio con VISA) para el pago automático.

| Pregunta | Respuesta esperada |
|---|---|
| **a)** 2 medidas de escalabilidad para la carga de video y la IA | **Escalado horizontal**: varias centrales y **réplicas de la IA**. **Asincronía con workers**: encolar los análisis para no bloquear. 2 puntos por medida bien justificada |
| **b)** Si los cobros tardan más de 2 s, los pagos exitosos bajan un 35%, y los usuarios recargan varias veces | Aprovechar el comportamiento: **caché** de los cobros pendientes (las recargas piden lo mismo) y **mejor hardware** o **bases separadas para las lecturas**. También valen mejores algoritmos de filtrado |
| **c)** Un vector de ataque y su solución | Por ejemplo, inyección o abuso de la API de pagos → validación de entradas, autenticación, WAF y rate limiting. 2 puntos por el vector y 2 por la solución |
| **d)** Características | Performance, escalabilidad, seguridad, **integrabilidad** (medios de pago, registro de tránsito), mantenibilidad, **soporte** (por los tickets), **usabilidad** (paga toda la población). **No:** portabilidad, flexibilidad |
| **e)** Estilos | **Suman:** cliente-servidor (solo con las cámaras), SOA, **lotes secuenciales** (proceso de pago), EDA, **pub/sub** (flujo de tickets), capas. **No:** código móvil, pizarra, main y subrutinas, **pipe & filter** |

> [!example]- Por qué pipe & filter no suma en Auto Parking
> El procesamiento del video con IA es **procesamiento pesado**, no filtrado simple. Las pautas reservan pipe & filter para filtrar datos (duplicados, formato). El análisis va en workers o réplicas de la IA.

## Preguntas de repaso

> [!question]- ¿Por qué OAuth2 es la respuesta para delegar acceso en Ocumore?
> Porque permite que el operador autorice al sistema a acceder a sus plataformas sin entregarle sus credenciales: el sistema recibe un token con alcance y vigencia limitados. Resuelve la seguridad y es eficiente, porque el token se valida sin pedir la contraseña en cada acceso.

> [!question]- ¿Qué combinación de bases de datos espera la pauta de Ocumore?
> Al menos una relacional transaccional para los cursos, solicitudes y relaciones, más un almacenamiento de archivos (documental o tipo S3) para los recursos recolectados, compuestos por ids en las consultas.

> [!question]- ¿Por qué capas y pub/sub no suman en Ocumore?
> Capas restringiría la flexibilidad y la escalabilidad sin aportar a un flujo distribuido de workers. Pub/sub no coordina pasos dependientes con un plazo: el ensamblado del curso necesita un mediador que orqueste.

> [!question]- Proponga 2 medidas de escalabilidad para Auto Parking y justifíquelas.
> Escalado horizontal de las centrales y réplicas de la IA, para repartir los miles de streams entre instancias. Asincronía con workers y colas, para que el análisis de cada evento no bloquee la recepción de video y la cola absorba los picos.

> [!question]- ¿Cómo aprovechar que los usuarios recargan varias veces la página de cobros?
> Con caché de los cobros pendientes por usuario: las recargas piden lo mismo y se responden desde la caché en milisegundos, con invalidación al registrarse un pago o un cobro nuevo.

> [!question]- ¿Por qué en Auto Parking sí valen soporte y usabilidad?
> Soporte, porque hay un sistema de tickets para gestionar errores de detección. Usabilidad, porque la usa toda la población, incluidas personas con poca experiencia tecnológica, para ver y pagar sus cobros.
