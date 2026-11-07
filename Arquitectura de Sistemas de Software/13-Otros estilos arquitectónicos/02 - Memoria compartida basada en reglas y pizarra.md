---
ramo: "Arquitectura de Sistemas de Software"
tema: "Otros estilos arquitectónicos"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[01 - Intérprete y código móvil]]"
---

# Memoria compartida basada en reglas y pizarra

Los estilos de **memoria compartida** giran en torno a un almacén central de conocimiento que varios componentes consultan y modifican. Se usaron mucho históricamente (sistemas expertos, reconocimiento de voz) y hoy reaparecen con los agentes de IA. Tienen dos variantes: **basado en reglas** y **pizarra**. Ambas son **1 sola quanta**: si se cae el motor central, se cae todo.

## La idea común

Un **motor de inferencia** parsea las entradas del usuario y decide si cada una es:
- un **hecho**, que se agrega a la base de conocimiento;
- una **regla**, que también se agrega a la base de conocimiento;
- una **consulta**, que se resuelve ejecutándola sobre la base de conocimiento para evaluar qué reglas aplican.

## Basado en reglas

> [!tip] Las reglas son datos, no código
> Las reglas son pares **condición → acción** guardados en una **base de conocimiento**. El **motor de inferencia decide cuáles se disparan y en qué orden**: el programa no tiene el flujo de control. Un árbol de `if/else` es lo contrario, porque ahí el orden lo fijó el programador.

![Memoria compartida basada en reglas](adjuntos/Memoria%20compartida%20basada%20en%20reglas.png)

> [!example]- Transcripción de la imagen
> - Croquis "Memoria compartida": **UI** → **Motor inferencia**, que se conecta con una **DB Rules** (base de reglas) y con una **DB** (base de datos de hechos).

- **Componentes:** interfaz de usuario, motor de inferencia y base de conocimiento.
- **Conectores:** componentes fuertemente interconectados por llamadas a procedimientos o memoria compartida.
- **Datos:** hechos y consultas.
- **Ejemplo de motor:** Jess (Java Expert System Shell).

**Ejemplo:** llega un usuario y hay que saber si es mayor de edad: el motor busca las reglas aplicables (`edad >= 18 → permitir`) y las evalúa con los hechos (su fecha de nacimiento).

**Este estilo escala en cantidad de reglas:**
- **Sistemas de autenticación o fraude** que necesitan actualizar sus reglas sin redesplegar código.
- **Antivirus:** "la base de datos de virus ha sido actualizada". Al prender el computador llegan reglas nuevas sin cambiar el programa.

> [!warning] El riesgo de las reglas
> Al aumentar el número de reglas, se vuelve **muy difícil entender cómo interactúan** entre sí: una regla nueva puede anular o disparar otras de forma inesperada.

## Pizarra (*blackboard*)

> [!tip] Pizarra
> Un **espacio de datos central** consultado y modificado por **fuentes de conocimiento** independientes. Cada fuente aporta una solución a una parte del problema. La **blackboard** organiza los datos para que sean accesibles, y un **control** supervisa el resultado y decide quién escribe.

Es como un grupo de científicos que modifica una pizarra: cada uno aporta lo que sabe y el problema se va resolviendo por partes.

**Diferencia con el estilo basado en reglas:** las reglas tienen **una** base de conocimiento y **un** motor. La pizarra tiene **muchas fuentes de conocimiento independientes** y un control que decide quién escribe. Debe ser capaz de buscar dentro de muchas fuentes distintas.

![Pizarra con un motor de inferencia y varias fuentes](adjuntos/Pizarra%20con%20fuentes%20de%20conocimiento.png)

> [!example]- Transcripción de la imagen
> - Croquis: un **Motor inf** (motor de inferencia, el blackboard) arriba, conectado a varias fuentes: una **DB**, un **S3 (Bucket)** y otros almacenes.

**Aplicaciones:**
- **Reconocimiento de voz:** HEARSAY-II (CMU, años 70), el ejemplo original.
- **Fusión de sensores y planificación:** varias fuentes aportan hipótesis parciales.
- Problemas complejos evolutivos y control emergente.
- **Programación agéntica:** varios agentes de IA trabajan en porciones del problema, la pizarra es el repositorio de trabajo y el espacio de comunicación, se agregan proveedores fácilmente (MCP, skills), el orden de ejecución no está predefinido y el resultado no es determinista.

| Pros | Contras |
|---|---|
| Permite trabajar **problemas complejos** | **Complejo de implementar** correctamente |
| Se puede **dividir el problema y reensamblarlo** | Puede complicar las búsquedas si no se controla |
| **Arquitectura colaborativa** | El proveedor de la pizarra puede volverse un **cuello de botella** |
| | **1 quanta**: si cae el motor, cae todo |

> [!warning] Pizarra casi nunca aplica en una prueba
> Las pautas la marcan como **no válida** cuando "no se espera un motor de procesos de muchas fuentes de datos". Solo se justifica si hay varias fuentes independientes que aportan conocimiento parcial a un problema común.

## Preguntas de repaso

> [!question]- ¿Qué significa que en el estilo basado en reglas "las reglas son datos, no código"?
> Que las reglas se guardan como pares condición → acción en una base de conocimiento, y el motor de inferencia decide cuáles se aplican y en qué orden. Se pueden agregar o cambiar reglas sin modificar el programa, a diferencia de un `if/else` fijo.

> [!question]- Nombre los componentes del estilo basado en reglas.
> La interfaz de usuario, el motor de inferencia y la base de conocimiento (reglas y hechos). Los datos son los hechos y las consultas.

> [!question]- ¿Por qué un antivirus es un buen ejemplo del estilo basado en reglas?
> Porque detecta amenazas evaluando firmas o reglas guardadas en una base que se actualiza constantemente, sin reinstalar el programa: el comportamiento cambia actualizando datos.

> [!question]- Diferencie el estilo basado en reglas y la pizarra.
> El de reglas tiene una base de conocimiento y un motor que la evalúa. La pizarra tiene muchas fuentes de conocimiento independientes que escriben en un espacio central, coordinadas por un control que decide quién escribe.

> [!question]- ¿Cuántas quantas tienen los estilos de memoria compartida y por qué?
> Una: todo depende del motor de inferencia o del blackboard central. Si cae, el sistema completo deja de funcionar.

> [!question]- ¿Por qué la programación agéntica se parece a una pizarra?
> Porque varios agentes trabajan en porciones del problema y comparten un espacio de trabajo común donde leen y escriben resultados parciales, sin un orden de ejecución predefinido. Es la misma idea de fuentes independientes sobre un blackboard.

> [!question]- V o F: "Agregar reglas a un sistema basado en reglas siempre lo hace más fácil de entender".
> Falso. Al crecer el número de reglas, sus interacciones se vuelven difíciles de prever y depurar: es el principal riesgo del estilo.
