---
ramo: "Arquitectura de Sistemas de Software"
tema: "Fundamentos de la arquitectura de software"
tags:
  - arquisis/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Arquitectura de software]]"
---

# Qué es la arquitectura de software

El software enfrenta muchos frentes de presión al mismo tiempo: complejidad, calidad, tiempo, dinero, esfuerzo, personal, mercado. Un diseño inicial que funciona hoy tiene que sobrevivir a preguntas como "¿qué pasa si…?". La **arquitectura de software** es la disciplina que se adelanta a esas preguntas. El enfoque del curso es **aprender a tomar decisiones**: qué agregar a un sistema, por qué y a qué costo.

## Las preguntas que la arquitectura anticipa

¿Qué pasa si…
- agregamos muchos más clientes?
- se caen los servidores?
- aparece un bug en producción?
- hay que agregar una funcionalidad en el futuro?
- cambia el presupuesto?
- compramos otra empresa, o nos compran?
- agentes de IA trabajan sobre el código?
- se suma un colaborador, o cien?

Además, en un sistema intervienen muchas personas: **clientes** (usuarios, dueños, terceros), **tecnología** (desarrolladores, QA, DevOps) y **gestión** (ventas, project managers, C-level, RR.HH.). En el software open source se suman colaboradores, auditores, integradores y empresas del rubro. Cada uno ve una parte del problema.

## Definiciones

> [!tip] Definición de Bass y Kazman (2013)
> "Es un **set de estructuras requeridas para razonar acerca de un sistema**, y comprende elementos de software, relaciones entre ellos y propiedades de ambos."

**¿Qué estructuras?**
- **Componentes + conectores:** interacciones entre componentes y estilos de conexión (divisiones, concurrencia).
- **Estructuras modulares:** composición de servicios, capas (*layering*) y dependencias de uso.
- **Estructuras de ocupación (*allocation*):** despliegues, asignación de recursos a tareas, grupos humanos y hardware.

**¿Razonar sobre qué?**
- **Características arquitectónicas:** dónde aplican y qué las dirige.
- **Tradeoffs:** de dónde salen y qué impacto tienen.
- **Organizaciones:** cómo se aplica la solución y cómo beneficia al dominio central (*core domain*).

Otras definiciones apuntan a lo mismo desde otro ángulo:

| Autor | Definición |
|---|---|
| Ralph Johnson (coautor de GoF) | "La arquitectura de software es sobre lo **importante**, sea lo que sea" |
| Martin Fowler | Dos elementos comunes: la **división de más alto nivel** del sistema en partes, y las **decisiones difíciles de cambiar** |
| Neal Ford | "Es lo que es **difícil de cambiar más adelante**" |
| ANSI/IEEE 1471-2000 | La organización fundamental de un sistema: sus componentes, sus relaciones, el ambiente y los principios que gobiernan su diseño y evolución |
| Grady Booch (2006) | "Toda arquitectura es diseño, pero no todo diseño es arquitectura." La arquitectura son las decisiones **significativas**, y lo significativo se mide por el **costo del cambio** |

Dos ideas se repiten. La arquitectura **representa la organización del sistema y del negocio**. Y **no es solo diseñar: es tomar decisiones difíciles**, sabiendo qué cambios tomar y cómo adaptarse.

## La analogía con la construcción

Una puerta tiene cierta estructura por algo: alguien la diseñó así. El arquitecto **guía el proyecto desde un punto de vista holístico**, para que el edificio se mantenga de pie. En software: que el sistema no colapse al pasar a producción, o que la tienda no se caiga el día del Cyber.

![Tabla que compara la arquitectura en construcción y en software](adjuntos/Comparación%20entre%20arquitectura%20de%20construcción%20y%20de%20software.png)

> [!example]- Transcripción de la imagen
> | Construcción | Software |
> |---|---|
> | No basta con saber construir: requiere conocimiento y experiencia | No basta con saber programar: requiere conocimiento adicional |
> | Se comunica con un equipo amplio (ingenieros, constructores, administradores, dueños) | Se comunica con ingenieros, PM, PO, QA, cliente, usuarios, dueños, C-level |
> | Hace mock-ups | Hace pruebas de concepto (PoC) y planificaciones |
> | Usa patrones de construcción | Usa patrones y estilos de software ampliamente probados |
> Filas compartidas: guía el proyecto con visión holística, reconoce antipatrones y tiene puntos de revisión, y se enfoca en las necesidades del futuro usuario.

![Tabla con las diferencias entre construcción y software](adjuntos/Diferencias%20entre%20construcción%20y%20software%20fuera%20de%20la%20analogía.png)

> [!example]- Transcripción de la imagen
> | Construcción | Software |
> |---|---|
> | Cambiar después de construir es realmente difícil | Hay un costo menor y se pueden hacer grandes migraciones; tiene un aspecto temporal |
> | Costo basado en **CAPEX** (lo que se comprará) | Costo basado en **OPEX** (lo que se gastará) |
> | Despliegue difícilmente escalable | Más fácil de escalar, sobre todo si se intenciona |
> | Industria antigua y estructurada, con muchos estándares | Industria joven y menos estructurada |
> | Es fácil medir la calidad a simple vista | Medir la calidad es un desafío y no es aparente |
> | Mano de obra con distintos niveles de calificación | Colaboradores especializados |

**CAPEX** es lo que se invierte para empezar (comprar). **OPEX** es lo que se gasta en operar (por ejemplo, la factura mensual de la nube).

## La arquitectura en la era de la IA

- El **costo de las implementaciones sencillas baja**: un agente escribe un CRUD en minutos.
- El **costo de las decisiones irreversibles aumenta**.
- El **criterio importa más que la ejecución**.
- Los modelos de solución resilientes resisten ciclos de entrega agresivos, errores de agentes y personas más inexpertas metiéndose al desarrollo.

Lo que diferencia a un ingeniero de un servicio hecho con IA es su capacidad de tomar decisiones sobre sistemas complejos. Las decisiones son nuestras, aunque no siempre sean las mejores.

## Preguntas de repaso

> [!question]- Explique la definición de Bass y Kazman y nombre los tres tipos de estructuras.
> La arquitectura es el conjunto de estructuras necesarias para razonar sobre un sistema: sus elementos, sus relaciones y las propiedades de ambos. Las estructuras son de componentes y conectores (cómo interactúan en ejecución), modulares (cómo se divide el código y sus dependencias) y de ocupación (dónde se despliega, con qué recursos y qué equipos).

> [!question]- ¿Qué tienen en común las definiciones de Fowler, Ford y Booch?
> Las tres apuntan a las decisiones difíciles o costosas de cambiar. Para Booch, lo que hace arquitectónica a una decisión es su costo de cambio. Por eso la arquitectura se centra en decisiones tempranas y significativas, no en cualquier detalle de diseño.

> [!question]- V o F: "Todo diseño de software es arquitectura".
> Falso. Según Booch, toda arquitectura es diseño, pero no todo diseño es arquitectura. Solo son arquitectónicas las decisiones significativas: aquellas cuyo cambio sería caro, como el estilo, las fronteras entre componentes o la base de datos.

> [!question]- ¿Qué diferencia de costos plantea la comparación entre construcción y software?
> La construcción se basa en CAPEX: una gran inversión inicial en lo que se compra. El software se basa en OPEX: lo que se gasta al operar, como servidores en la nube por uso. Por eso en software importa tanto el costo operacional de cada decisión.

> [!question]- ¿Por qué la analogía con la construcción falla en cuanto a cambiar después?
> En construcción, cambiar un edificio terminado es casi imposible. En software los cambios son más baratos y se pueden hacer grandes migraciones, aunque las decisiones arquitectónicas siguen siendo las más caras de cambiar.

> [!question]- ¿Cómo cambia la IA el valor del trabajo arquitectónico?
> Abarata las implementaciones simples, pero encarece las decisiones irreversibles, porque se construye más rápido sobre ellas. El valor se desplaza del código al criterio: decidir bien la estructura, los tradeoffs y la resiliencia frente a errores, también los de agentes.

> [!question]- Nombre tres preguntas del tipo "¿qué pasa si…?" que una buena arquitectura debería anticipar.
> Por ejemplo: qué pasa si los clientes se multiplican por 10 (escalabilidad), si se cae un servidor (disponibilidad) o si hay que agregar un medio de pago nuevo (flexibilidad). Cada pregunta apunta a una característica arquitectónica.
