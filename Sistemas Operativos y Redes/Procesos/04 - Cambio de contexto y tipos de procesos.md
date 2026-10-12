---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/apuntes]
prerrequisitos: ["[[02 - Bloque de control de procesos y tabla de procesos|Bloque de control de procesos y tabla de procesos]]", "[[03 - Estados de un proceso y ciclo de vida|Estados de un proceso y ciclo de vida]]"]
---
# Cambio de contexto y tipos de procesos

El cambio de contexto (*context switch*) es el mecanismo que permite a la CPU alternar la ejecución entre procesos guardando y restaurando sus estados en el PCB, cuyo costo e impacto depende del perfil de carga del proceso (CPU-bound vs I/O-bound).

## Cambio de contexto y perfiles de carga (mis apuntes)
### Context Switch
- Cambio de Proceso Corriendo
- Siempre tiene un poco de OVERHEAD → Tenemos que posicionar todo para correr de nuevo
- Se usa mucho en computacion → Cambio de Contexto
- Cargar datos y variables que habian antes
- Se realiza con un tiempo extra para realizarlo

### Tipos de Procesos
- Es altamente computacional
- Ej: Calculos matematicos → caja obscura
- Codigo que corre solo y no requiere interaccion Humana
- CPU Burst → Alto encomputo → Necesita muchos recursos
- Ej: Recien entrenar una Machine Learning
- Ej: Whatsapp → si no hay input , no hay mensaje
- EJ: Un Juego → Alto de input output → Constantemente esta esperando recibir y entregar
- Necesita de Input Output
- CPU I/O → Recibe Input/ Output
Pregunta prueba: Verdadero falso
Un proceso de input/output es alto en señales de entrada y salida
Este proceso es alto en input/output

CONTEXT SWITCH EJEMPLO

![Secuencia temporal del cambio de contexto](adjuntos/Secuencia%20temporal%20del%20cambio%20de%20contexto.png)

> [!example]- Transcripción de la imagen
> Secuencia temporal de un cambio de contexto en multitasking:
> 1. El proceso **P1** ejecuta en *User space*.
> 2. Ocurre una **INTERRUPCIÓN** (timer, syscall o evento de I/O) que salta a *Kernel space*.
> 3. La CPU en modo kernel almacena el estado completo de registros de P1 en su **PCB1**. P1 queda "en pausa" (en estado *Ready* o *Waiting*).
> 4. El kernel restaura el estado guardado de registros desde **PCB2**.
> 5. El proceso **P2** toma la CPU y continúa su ejecución en *User space*.
> 6. Posteriormente, otra interrupción almacena PCB2 y restituye el contexto de P1.

En la pcb se esta guardando todo el estado de un Juego por ejemplo
El SO por detras guarda la info que minimizaste y probablemente lo cierra
Cuando tenga que abirlo denuevo, probablemente va a recargar toda la info

> [!tip] Complemento (slides "Contenido 2: Costo del Context Switch")
> Durante un cambio de contexto, el procesador no realiza trabajo útil para ningún programa de usuario: es puro *overhead* del sistema operativo (habitualmente toma entre unos pocos microsegundos y decenas de microsegundos).
>
> **Factores de costo directo e indirecto:**
> - **Costo directo:** Guardar y recuperar registros de la arquitectura (registros enteros, punteros de pila, registros de coma flotante / SIMD) y cambiar el espacio de direcciones de memoria virtual (registro `CR3` en x86).
> - **Costo indirecto (*Cache Pollution*):** Al cambiar de proceso, las memorias caché (L1, L2, L3) y el búfer de traducción de direcciones (TLB) quedan con datos del proceso anterior. El nuevo proceso sufrirá una ráfaga inicial de fallos de caché hasta volver a calentar la memoria.

## Preguntas de repaso

1. ¿Qué es un cambio de contexto (*context switch*) y por qué representa puro *overhead*?
> [!question]- Respuesta
> Es el procedimiento mediante el cual el kernel guarda el estado de la CPU del proceso en ejecución y carga el estado guardado de otro proceso. Es overhead porque consume tiempo y ciclos de máquina sin avanzar en el cómputo de ninguna aplicación de usuario.

2. ¿Qué diferencia a un proceso *CPU-bound* de uno *I/O-bound*?
> [!question]- Respuesta
> Un proceso *CPU-bound* realiza cómputo intensivo con ráfagas de CPU largas y escasa interacción externa; un proceso *I/O-bound* pasa la mayor parte del tiempo esperando operaciones de entrada/salida (disco, red o usuario) con ráfagas de CPU muy breves.

3. ¿Por qué el cambio de contexto entre procesos diferentes invalida parcialmente las cachés de CPU?
> [!question]- Respuesta
> Porque cada proceso posee su propio espacio de memoria virtual con datos e instrucciones distintas; al conmutar, las líneas de caché L1/L2 cargadas con código del proceso previo ya no corresponden al nuevo proceso.

4. ¿Qué información almacena el sistema operativo al pausar un proceso interactivo en segundo plano?
> [!question]- Respuesta
> El Program Counter, los registros de propósito general, punteros de stack, estado de archivos abiertos y descriptores de memoria en su PCB correspondiente.

