---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos estructurales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[03 - Decisiones relevantes y tácticas arquitectónicas]]"
---

# Mantenibilidad y flexibilidad

Los **requisitos estructurales** son inquietudes sobre la estructura y el desarrollo del código: se notan al programar, no al ejecutar. Tienen un **alto grado de recompensa, pero requieren un pago inicial** de dinero y tiempo, y la **deuda técnica** puede afectarlos mucho a futuro. En el curso solo se consideran los atributos vistos en clases, no los que pueda listar una IA o internet.

## Mantenibilidad

> [!tip] Mantenibilidad
> Capacidad de **solventar y reparar la operación** de un sistema: qué tan fácil es encontrar un error y corregirlo. Incluye **operabilidad**, **simplicidad** (del código y la estructura) y **evolución** (*evolvability*): upgrades, mejoras y fixes.

Es técnica y práctica a la vez, porque se ve en el código. **Ejemplo: APT en Linux.** Está muy bien pensado para mantenerse: las librerías se actualizan con un comando, los errores se identifican rápido y se ofrecen soluciones.

**Escenario:** un desarrollador (fuente) debe agregar un nuevo medio de pago (estímulo) durante el desarrollo normal (entorno) en el servicio de pagos (artefacto); el cambio queda implementado y probado **tocando un solo módulo, sin efectos colaterales** (respuesta), en **≤ 3 días-persona** (medición). Lo que se exige es que el cambio sea rápido y localizado.

**Cómo se logra:** alta cohesión y bajo acoplamiento (el cambio queda en un módulo), tests automatizados (el cambio se prueba sin miedo), monitoreo y logs claros (el error se encuentra rápido), y código simple.

## Flexibilidad / extensibilidad

> [!tip] Flexibilidad o extensibilidad
> Capacidad de **extender un sistema y agregarle funcionalidad**: ¿cuánto esfuerzo se necesita para agregar algo nuevo?

La diferencia con la mantenibilidad es el foco. La mantenibilidad piensa en **reparar y evolucionar** (errores incluidos); la flexibilidad piensa en **agregar** funcionalidades.
- Requiere **identificar los escenarios de cambio probables**: no se puede ser flexible en todo.
- La **alta cohesión** dentro de los componentes y los **subsistemas débilmente acoplados** facilitan el cambio.
- **Ejemplos:** VS Code con sus extensiones (el editor se extiende sin tocar su núcleo) y la inyección de dependencias.

**Escenario:** el negocio (fuente) exige **cambiar el proveedor de notificaciones** (estímulo) con el sistema en producción (entorno); **solo se modifica el adaptador** del proveedor (artefacto y respuesta), sin tocar la lógica de negocio, en **≤ 2 días-persona** (medición).

## Caso: el inyector de dependencias

Un **inyector de dependencias** es un sistema para incorporar módulos de código y hacerlos **reemplazables**. Aplica la **inversión de control** (el framework crea y entrega las dependencias) y prefiere la **composición a la instanciación** (la clase recibe sus colaboradores en vez de crearlos con `new`).

```python
class Notificador:                     # puerto
    def enviar(self, destino, mensaje): ...

class NotificadorSendgrid(Notificador): ...
class NotificadorTwilio(Notificador): ...

class ServicioPedidos:
    def __init__(self, notificador: Notificador):   # se inyecta, no se crea adentro
        self.notificador = notificador

servicio = ServicioPedidos(NotificadorTwilio())      # cambiar de proveedor = cambiar esta línea
```

- **Promueve:** mantenibilidad y flexibilidad. El escenario de "cambiar el proveedor de notificaciones en ≤ 2 días" se cumple tocando solo el adaptador.
- **Degrada:** la **velocidad de desarrollo**, porque hay más interfaces, más configuración y más indirección para entender el flujo.

> [!warning] Flexibilidad en todo es sobreingeniería
> Hacer configurable y reemplazable cada pieza "por si acaso" multiplica las abstracciones y frena el desarrollo. La flexibilidad se invierte donde hay **escenarios de cambio probables** (proveedores externos, medios de pago, reglas de negocio volátiles), no en todas partes.

## Preguntas de repaso

> [!question]- ¿Qué caracteriza a los requisitos estructurales?
> Se refieren a la estructura y al desarrollo del código, se notan al programar y no al ejecutar. Dan mucha recompensa a largo plazo, pero exigen una inversión inicial, y la deuda técnica los degrada con el tiempo.

> [!question]- Diferencie mantenibilidad y flexibilidad.
> La mantenibilidad mide qué tan fácil es reparar, corregir y evolucionar el sistema (encontrar y arreglar errores, aplicar upgrades). La flexibilidad mide cuánto esfuerzo cuesta agregar funcionalidades nuevas.

> [!question]- ¿Qué promueve y qué degrada un inyector de dependencias?
> Promueve mantenibilidad y flexibilidad, porque los módulos se reemplazan sin tocar a quienes los usan. Degrada la velocidad de desarrollo, por la indirección, las interfaces extra y la configuración adicional.

> [!question]- Escriba un escenario de flexibilidad para agregar un nuevo idioma a una aplicación.
> Fuente: el negocio. Estímulo: pide agregar portugués. Entorno: sistema en producción. Artefacto: el módulo de internacionalización. Respuesta: se agregan archivos de traducción sin modificar código de negocio. Medición: ≤ 1 día-persona.

> [!question]- ¿Por qué APT es un ejemplo de mantenibilidad?
> Porque está diseñado para que actualizar y reparar sea simple: un comando actualiza paquetes y dependencias, los errores se identifican rápido y se ofrecen soluciones. La operación y la evolución del sistema son fáciles.

> [!question]- V o F: "Para maximizar la flexibilidad conviene abstraer y hacer reemplazable cada componente del sistema".
> Falso. La flexibilidad se invierte donde hay escenarios de cambio probables. Abstraer todo es sobreingeniería: agrega complejidad y frena el desarrollo sin beneficio.

> [!question]- ¿Qué principios de diseño facilitan la flexibilidad según el curso?
> Alta cohesión dentro de los componentes y bajo acoplamiento entre subsistemas, de modo que un cambio quede contenido en un lugar y no se propague.
