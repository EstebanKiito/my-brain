---
ramo: "Arquitectura de Sistemas de Software"
tema: "Componentes quanta y documentación"
tags:
  - arquisis/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[03 - Connascence dinámica y reglas de grado y localidad]]"
---

# Componentes y quanta arquitectónica

Para representar un diseño se necesitan unidades. El **componente** es la unidad lógica con la que se dibuja la arquitectura. La **quanta** es la **medida** de cuántas partes del sistema se despliegan y fallan de forma independiente. En casi todas las preguntas de estilos aparece "¿cuántas quantas tiene?", así que hay que manejar este concepto con precisión.

## Componente

> [!tip] Componente
> **Encapsula un subconjunto de funcionalidad y/o estado** de un sistema, **expone contratos o interfaces explícitos** y es **altamente cohesionado**, aunque por dentro puede tener connascence de diversos grados.

Un componente es una **agrupación lógica de software**: una librería, un módulo, un subsistema o un sistema completo. ¿Cuánto hay que desglosar? Todo lo necesario para que se entienda el sistema. En el diagrama es una caja; el círculo (*lollipop*) es la interfaz que expone, y el semicírculo (*socket*), la interfaz que requiere.

![Componente E0 que contiene una API, un conector y una base de datos](adjuntos/Componente%20E0%20con%20API%20conector%20y%20base%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - Croquis titulado "Componente:". Un rectángulo grande **E0** contiene una **API** y un **Connector** unidos por una interfaz, y la API está conectada a una **base de datos**.
> - Arriba, E0 expone una interfaz hacia afuera (un círculo sobre un palo).
> - A la derecha, el símbolo de la interfaz (círculo y semicírculo) con la anotación "interfaz expuesta".

## Quanta arquitectónica

> [!tip] Quantum arquitectónico (Ford, Parsons y Kua)
> *"An architectural quantum is an independently deployable component with high functional cohesion."* Es un **componente desplegable de forma independiente**, con alta cohesión funcional.

- Es una **medida o unidad**, no la descripción de un componente ni un set de reglas: sirve para mirar un sistema y contar cuántas quantas tiene.
- Idealmente, cada quantum corresponde a un **bounded context**.
- **Si es independientemente desplegable, también es independientemente "caíble".** Con 2 quantas, si se cae una, la otra sigue funcionando.
- **Más quantas, más resiliencia ante caídas**: identificar las quantas ayuda a ver los **puntos vulnerables** a nivel de despliegue (*allocation*).

### Cómo se cuentan

![Una sola quanta: la API y el conector dependen de la misma base](adjuntos/Una%20sola%20quanta%20cuando%20todo%20depende%20de%20la%20base.png)

> [!example]- Transcripción de la imagen
> - Croquis titulado "1 Quanta". Un rectángulo contiene una **API** y un **Conn** (conector); la conexión directa entre ellos está tachada.
> - Ambos se conectan a la misma **base de datos**, abajo.
> - Debajo dice: "Ambas dependen de la BDD".

- **La base de datos sola no es una quanta**: una base sin la aplicación no permite ver ni hacer nada.
- **API + BD = 1 quanta.** Si el conector (por ejemplo, el que recibe mensajes de un broker) solo depende de la API, puede ser otra quanta: si la API se cae, el conector sigue recibiendo.
- Pero si **el conector se conecta directo a la base** en vez de a la API, y **ambos dependen de la misma base**, todo es **1 sola quanta**: si se cae la base, se cae todo.
- En el proyecto: si se cae la app propia, el broker del curso sigue funcionando, y viceversa. Son quantas distintas.

| Arquitectura | Quantas típicas |
|---|---|
| Monolito con una base de datos | 1 |
| Cliente-servidor | 1 (el servidor es un punto único de falla) |
| Microkernel | 1 (depende del core) |
| Memoria compartida (reglas, pizarra) | 1 (depende del motor) |
| Microservicios con base propia | N |
| EDA con broker (fire and forget) | N |

> [!warning] Microservicios no implica N quantas
> Si todos los servicios se llaman de forma síncrona entre sí, o comparten una misma base de datos, la caída de uno arrastra a los demás: en la práctica son **una sola quanta** distribuida (*big ball of distributed mud*). Las quantas se cuentan por **dependencias de despliegue y de falla**, no por cantidad de cajas.

## Preguntas de repaso

> [!question]- ¿Qué características tiene un componente según el curso?
> Encapsula un subconjunto de funcionalidad o estado, expone interfaces o contratos explícitos y es altamente cohesionado (aunque tenga connascence interna). Puede ser una librería, un módulo, un subsistema o un sistema.

> [!question]- Defina quanta arquitectónica y explique por qué es una medida.
> Es un componente desplegable de forma independiente y con alta cohesión funcional. Es una medida porque sirve para contar cuántas partes del sistema pueden desplegarse y fallar por separado, no para describir cómo es un componente por dentro.

> [!question]- ¿Por qué una base de datos sola no cuenta como quanta?
> Porque por sí sola no entrega funcionalidad: sin la aplicación que la usa no se puede ver ni hacer nada. Se cuenta junto con la aplicación que depende de ella.

> [!question]- Una API y un worker son procesos distintos, pero ambos leen y escriben la misma base de datos. ¿Cuántas quantas son?
> Una sola: ambos dependen de la misma base, así que si la base cae, caen los dos. Para que fueran dos quantas independientes, el worker tendría que tener su propio almacenamiento o comunicarse de forma asíncrona sin depender de la misma instancia.

> [!question]- ¿Qué relación hay entre la cantidad de quantas y la resiliencia?
> Más quantas significa que las fallas quedan contenidas: si cae una, las demás siguen funcionando. Por eso contar quantas ayuda a encontrar puntos únicos de falla.

> [!question]- V o F: "Un sistema con 12 microservicios tiene necesariamente 12 quantas".
> Falso. Si los servicios dependen de forma síncrona unos de otros o comparten la misma base de datos, la caída de uno arrastra a los demás y en la práctica son menos quantas, incluso una sola.

> [!question]- ¿Cuántas quantas tiene un estilo cliente-servidor y por qué?
> Una: todos los clientes dependen del mismo servidor, que es un punto único de falla (SPOF). Si cae el servidor, el sistema completo deja de funcionar.
