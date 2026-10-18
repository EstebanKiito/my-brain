---
ramo: Bases de Datos
tema: Recuperación de fallas
tags: [bd/recuperacion, origen/apuntes]
prerrequisitos: ["[[02 - Propiedades ACID|Propiedades ACID]]"]
---
# Tipos de fallas

Una base de datos puede fallar por datos erróneos, por daño del almacenamiento, por catástrofes o por caídas del sistema. Cada falla tiene su solución; las caídas del sistema se resuelven con el **log** y el Recovery Manager.

## Tipos de fallas en transacciones y soluciones
### Fallas en la ejecución de transacciones
- **Datos erróneos:**
    - Problema: se ingresan datos incorrectos por errores humanos o problemas de integración.
    - Soluciones: validaciones estrictas, controles de integridad y procesos periódicos de limpieza de datos.
- **Fallas en el almacenamiento:**
    - Problema: fallos físicos en los dispositivos de almacenamiento.
    - Soluciones: configuraciones RAID (*Redundant Array of Independent Disks*) para tener redundancia, y copias de seguridad regulares.
- **Catástrofes:**
    - Problema: eventos graves como incendios, inundaciones o ciberataques.
    - Soluciones: estrategias de recuperación ante desastres, copias de seguridad distribuidas geográficamente y planes de continuidad del negocio.
- **Fallas del sistema:**
    - Problema: interrupciones en el funcionamiento del sistema de base de datos, como fallos de software o de hardware.
    - Solución: técnicas de recuperación con logs, *checkpointing* y reinicio del sistema, para volver a un estado consistente de la base de datos. Se explican desde [[02 - Log manager y registros de log|Log manager y registros de log]].

> [!tip] Complemento (slides "Clase 11: Transacciones y Recuperación de Fallas")
> | Falla | Solución según la slide |
> |---|---|
> | Datos erróneos | restricciones de integridad, *data cleaning* |
> | Fallas en el disco duro | RAID, copias redundantes |
> | Catástrofes | copias distribuidas |
> | **Fallas del sistema** | **Log y Recovery Manager** |
>
> El Log Manager y el Recovery Manager se encargan de asegurar la **atomicidad** y la **durabilidad** ([[02 - Propiedades ACID|ACID]]). El problema central: si el sistema se cae, en disco pueden haber quedado cambios de transacciones **no confirmadas** (hay que deshacerlos, *undo*) y pueden faltar cambios de transacciones **confirmadas** que estaban solo en RAM (hay que rehacerlos, *redo*).

## Preguntas de repaso

1. Nombra los cuatro tipos de fallas y una solución para cada uno.
> [!question]- Respuesta
> Datos erróneos: validaciones e integridad. Fallas del almacenamiento: RAID y respaldos. Catástrofes: respaldos distribuidos geográficamente y planes de continuidad. Fallas del sistema: recuperación con logs y checkpoints.

2. ¿Qué componentes se encargan de las fallas del sistema y qué propiedades ACID aseguran?
> [!question]- Respuesta
> El Log Manager y el Recovery Manager, que aseguran la atomicidad y la durabilidad.

3. ¿Qué dos problemas puede dejar una caída del sistema en el disco?
> [!question]- Respuesta
> Cambios de transacciones sin commit ya escritos en disco (hay que deshacerlos) y cambios de transacciones con commit que no alcanzaron a escribirse (hay que rehacerlos).
