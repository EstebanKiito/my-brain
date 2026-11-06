---
ramo: "Arquitectura de Sistemas de Software"
tema: "Diagramación y UML de componentes"
tags:
  - arquisis/uml
  - origen/complemento
prerrequisitos:
  - "[[01 - Diagramación modelos y lenguajes de descripción]]"
  - "[[01 - Diagrama de clases UML]]"
---

# Vistas 4+1 modelo de zoom y variantes de UML

Tres estándares organizan la forma de diagramar. **4+1** dice **qué vistas** hay que mostrar. **C4** propone **niveles de zoom**. **UML** es el **lenguaje** con el que se dibuja cada diagrama. En el curso se usa sobre todo UML, y en particular el diagrama de componentes.

## El modelo de vistas 4+1

Es un estándar **fundamental**. Las decisiones arquitectónicas se basan en **casos de uso y escenarios** del sistema. No define cómo dibujar, sino **qué hay que mostrar** para que el sistema se entienda; en cada vista se pueden usar distintos diagramas.

| Vista | Qué muestra | Diagramas típicos |
|---|---|---|
| **Lógica** | La abstracción del sistema: clases, objetos y cómo funciona el código | Clases, secuencia, colaboración |
| **De desarrollo** | La estructura del software en módulos, archivos y paquetes | Paquetes, componentes |
| **De proceso** | Los procesos del sistema y su interacción en ejecución | Actividad |
| **Física** | Cómo se instala y se ejecuta el sistema en una red de computadores | Despliegue (*deployment*) |
| **+1: Escenarios** | Cómo los actores usan la aplicación; une las otras cuatro | Casos de uso |

## C4

Cuatro tipos de diagrama que **hacen zoom** progresivamente: dentro de cada sistema se ve otro más detallado.
1. **Contexto:** el sistema y su entorno (usuarios y sistemas externos).
2. **Contenedores:** las aplicaciones y almacenes que lo componen (web, API, base de datos).
3. **Componentes:** los componentes dentro de cada contenedor.
4. **Código:** clases e implementación.

- Es **sencillo de aprender y fácil de usar**, y se usa mucho en la industria.
- Es **menos formal y estructurado** que UML.
- **Tradeoff:** es más fácil de iterar, a cambio de menos rigurosidad. En el curso no se usa en las pruebas.

## UML

- Creado por el **OMG** (Object Management Group): versión 1.1 en 1997 y 2.0 en 2005.
- Es un **modelo enorme**, con diagramas para casi todo, pero usable en varios contextos y **comprensible por varias audiencias**. Sus fundamentos son bastante complejos.
- **Infraestructura de UML:** define los elementos usados por el metamodelo y la superestructura.
- **Superestructura de UML:** define el metamodelo, es decir, el lenguaje (su especificación 2.2 tiene unas 740 páginas).

![Árbol de tipos de diagramas UML con componentes y secuencia destacados](adjuntos/Variantes%20de%20diagramas%20UML.png)

> [!example]- Transcripción de la imagen
> - Raíz **Diagram**, dividida en **Structure Diagram** y **Behavior Diagram**.
> - Estructura: Class, **Component** (destacado con un círculo rojo), Object, Profile, Composite Structure, Deployment y Package.
> - Comportamiento: Activity, Use Case, State Machine e **Interaction**, que se divide en **Sequence** (destacado con un círculo rojo), Communication, Interaction Overview y Timing.

Se puede elegir qué diagramas usar y mezclarlos con las otras vistas. **El curso se enfoca en dos:**
- **Componentes** (estructura): qué piezas hay y qué interfaces se exponen y consumen. Es el diagrama de las pruebas.
- **Secuencia** (comportamiento): el orden de los mensajes entre participantes.

**¿Por qué UML?**
- Es un **estándar en la industria**.
- Es bueno para **visualizar y mostrar soluciones rápidamente**.
- **Refleja las ideas más fielmente.**
- Permite **mayor detalle** sobre la implementación.

> [!warning] Componentes no es un diagrama de flujo
> Hay que desligarse de los diagramas de secuencia y de flujo: el diagrama de componentes muestra **un todo** (los elementos de software y sus interacciones), no dónde empieza y dónde termina un proceso. El orden en que se dibujan las interfaces **no implica flujo**: eso lo determinan el protocolo y el funcionamiento del sistema.

## Preguntas de repaso

> [!question]- ¿Qué muestra cada vista del modelo 4+1?
> Lógica: la abstracción del sistema (clases, objetos). Desarrollo: la organización del software en módulos y paquetes. Proceso: los procesos en ejecución y su interacción. Física: el despliegue en máquinas y red. +1 escenarios: los casos de uso que unen y validan las otras cuatro.

> [!question]- ¿Qué diagrama UML corresponde a la vista física y cuál a la de escenarios?
> A la vista física, el diagrama de despliegue (deployment). A la de escenarios, el diagrama de casos de uso.

> [!question]- ¿Cuál es el tradeoff de C4 frente a UML?
> C4 es más fácil de aprender e iterar, con niveles de zoom intuitivos, pero es menos formal y riguroso. UML es más preciso y estandarizado, pero más complejo.

> [!question]- Nombre los cuatro niveles de C4.
> Contexto, contenedores, componentes y código.

> [!question]- ¿En qué dos diagramas UML se enfoca el curso y a qué categoría pertenece cada uno?
> El de componentes, que es un diagrama de estructura, y el de secuencia, que es un diagrama de comportamiento (de interacción).

> [!question]- V o F: "En un diagrama de componentes, el orden de izquierda a derecha de las interfaces indica el flujo de los datos".
> Falso. El diagrama de componentes muestra estructura y dependencias, no flujo. El flujo depende del protocolo y del funcionamiento del sistema. Para el orden de los mensajes se usa un diagrama de secuencia.

> [!question]- ¿Qué diferencia hay entre la infraestructura y la superestructura de UML?
> La infraestructura define los elementos base que usan el metamodelo y la superestructura. La superestructura define el metamodelo de UML, es decir, el lenguaje con sus diagramas y su significado.
