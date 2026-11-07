---
ramo: "Arquitectura de Sistemas de Software"
tema: "Estilos jerárquicos y de capas"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[03 - Máquinas virtuales y cliente-servidor]]"
---

# Microkernel

VS Code tiene miles de extensiones y su núcleo casi no cambia. Canvas permite agregar funcionalidades a través de su API sin tocar su core. Ese es el estilo **microkernel**: un **núcleo mínimo** que se extiende con **plugins**. Es la respuesta típica cuando un enunciado pide personalización o extensiones de terceros.

## Descripción

- La **funcionalidad core se mantiene al mínimo posible.**
- Los demás sistemas se **agregan como plugins** mediante **interfaces estandarizadas** que extienden el sistema.
- La comunicación es generalmente **punto a punto**.
- Se asocia con los kernels de sistemas operativos, pero hoy se acerca a muchas arquitecturas.

**Ejemplos:** kernels (apreciados por su extensibilidad), **IDEs** como VS Code, **navegadores** con sus extensiones, sistemas multi-entorno y plataformas como Canvas.

## Microkernel frente a main y subrutinas

![Microkernel con plugins frente a main y subrutinas](adjuntos/Microkernel%20con%20plugins%20frente%20a%20main%20y%20subrutinas.png)

> [!example]- Transcripción de la imagen
> - Arriba, un **Core** que **provee** interfaces a las que se conectan dos plugins **P**, con la anotación "pluggin".
> - Abajo, **MAIN** que **requiere** la interfaz de una **Subrutina**.
> - Entre ambos, "v/s" y una flecha tachada: la dirección de la dependencia es opuesta.

Se dibujan parecido (una entidad central y piezas alrededor), pero la **dependencia va al revés**:
- En **main y subrutinas**, el main **se conecta a** las subrutinas, las conoce y las controla.
- En **microkernel**, los **plugins se conectan al core**: el core publica una interfaz y no conoce a los plugins. Por eso es **extensible**: se pueden crear funcionalidades nuevas y enchufarlas sin tocar el core. Si un plugin se cae, los demás siguen funcionando.

## Variantes y topologías

- Los enlaces no tienen que ser llamadas a funciones: pueden ser **REST** o **colas**.
- Se pueden agregar **almacenes de datos**: uno común, uno por plugin o uno en el core.
- Puede haber un **registro de plugins** para encontrarlos fácilmente, como un marketplace.

| Pros | Contras |
|---|---|
| **Fácil de evolucionar**: miles de extensiones en marketplaces | **Punto único de falla**: el core |
| **Fácil de implementar**: simple y económico | **Quanta única** |
| **Incorpora particionado de dominio**: cada plugin puede reflejar un área del problema | **Mala escalabilidad**: limitada por el core, y puede responder mal ante la demanda |

> [!example]- Cuándo proponerlo en una prueba
> - "Cada cliente necesita personalizar el sistema con módulos propios." Si el sistema requiere customización por usuario, sirve un microkernel.
> - "Terceros desarrollarán integraciones para la plataforma." Plugins sobre interfaces estandarizadas.
> - "El core debe ser estable y las extensiones cambian seguido." Integrabilidad y flexibilidad, sin tocar el núcleo.
> No conviene si el requisito principal es la escalabilidad masiva o la alta disponibilidad, porque todo depende de un core único.

## Quantas de los estilos jerárquicos

| Estilo | Quantas | Por qué |
|---|---|---|
| Monolito | 1 | Un bloque y una base |
| Main y subrutinas | 1 | Todo depende del main |
| Cliente-servidor | 1 | El servidor es un SPOF |
| Microkernel | 1 | Todo depende del core |
| Máquinas virtuales | N | Cada VM o contenedor independiente es una quanta |

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia clave entre microkernel y main y subrutinas?
> La dirección de la dependencia. En main y subrutinas, el main conoce y llama a las subrutinas. En microkernel, los plugins se conectan a la interfaz del core, que no los conoce. Por eso se pueden agregar plugins sin modificar el núcleo.

> [!question]- Nombre tres ejemplos de microkernel.
> VS Code y sus extensiones, los navegadores con sus extensiones y Canvas con su API para agregar funcionalidades. También los kernels de sistemas operativos.

> [!question]- ¿Por qué el microkernel tiene mala escalabilidad?
> Porque toda la funcionalidad pasa por el core, que es único: ante más demanda, el core se vuelve el cuello de botella, y además es un punto único de falla.

> [!question]- ¿Qué variantes de comunicación y almacenamiento admite un microkernel?
> Los enlaces pueden ser llamadas a funciones, REST o colas. El almacenamiento puede ser común, por plugin o del core. Además puede tener un registro de plugins.

> [!question]- Mini caso: un ERP debe permitir que cada empresa cliente agregue módulos propios sin afectar a las demás. ¿Qué estilo propone y qué riesgo menciona?
> Microkernel: un core estable con interfaces estandarizadas y módulos como plugins por cliente. El riesgo es que el core es un punto único de falla y un posible cuello de botella, que se mitiga con réplicas del core o aislando la ejecución de los plugins.

> [!question]- V o F: "En un microkernel, si un plugin falla, cae todo el sistema".
> Falso en general. Los plugins son independientes entre sí y del core, así que la falla de uno no tumba a los demás. Lo que sí tumba al sistema es la falla del core.

> [!question]- ¿Cuántas quantas tienen cliente-servidor y microkernel, y por qué?
> Una cada uno: en cliente-servidor todo depende del servidor, y en microkernel todo depende del core. Si ese componente central cae, cae el sistema.
