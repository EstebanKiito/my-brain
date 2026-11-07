---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos operacionales"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[01 - Performance y escalabilidad como requisitos operacionales]]"
  - "[[01 - Confiabilidad y sus propiedades]]"
---

# Confiabilidad

Un sistema que está arriba pero que pierde transacciones o devuelve resultados incorrectos no sirve. La **confiabilidad** mide si el sistema **hace lo que tiene que hacer**: protege su funcionamiento y sus datos. Es distinta de la disponibilidad (estar arriba), y en las pruebas se pide no confundirlas.

## Definición

> [!tip] Confiabilidad (*reliability*)
> Una aplicación confiable **protege su funcionamiento y sus datos y mantiene la operación**. Hace lo que tiene que hacer, de forma correcta.

- **Los sistemas son inherentemente inestables**: la red falla, los discos fallan, los procesos se caen.
- Un sistema confiable **tiene previsiones y estrategias para las fallas**.
- Usa **QoS** (*quality of service*) en las comunicaciones: ¿cómo se quieren recibir los mensajes? ¿Al menos una vez? ¿Exactamente una vez?
- **Promete SLAs** de diversos tipos: durabilidad de los datos, transmisión, resistencia a caídas, del orden de 99,99x%. Son compromisos que quedan en los contratos.
- **Cobra cada vez más importancia con la IA.**

**Ejemplo:** un banco poco confiable acepta una transferencia y no la ejecuta, o la ejecuta dos veces. Puede estar disponible el 100% del tiempo y aun así no ser confiable.

**Escenario:** el broker (fuente) sigue publicando eventos mientras el listener sufre una **desconexión transitoria** (estímulo) en operación normal (entorno); el listener (artefacto) **se reconecta y repone los eventos desde el último offset** (respuesta), con **0 eventos perdidos en el mes** (medición).

## Factores

| Fomentan la confiabilidad | La dificultan |
|---|---|
| **Simplicidad y monitoreo**: menos piezas que fallen y fallas que se detectan | **Agilidad**: cambiar rápido introduce errores |
| **Estándares y SLAs**: compromisos medibles | **Visibilidad del valor**: cuesta justificar inversión en algo que "no se ve" mientras funciona |
| | **Seguridad**: más controles pueden agregar puntos de falla |

## Dos casos de falta de confiabilidad

> [!example]- Desert Storm: el error de reloj del misil Patriot
> En la Guerra del Golfo (1991), el sistema antimisiles Patriot de Dhahran acumulaba un pequeño error de redondeo en su reloj interno. Después de unas 100 horas encendido, el desfase era de aproximadamente un tercio de segundo, suficiente para calcular mal la posición de un misil Scud. El Patriot no lo interceptó y murieron 28 soldados.
> El sistema estaba **disponible** (encendido y operando), pero **no era confiable**: hacía mal su trabajo. La solución conocida era reiniciarlo periódicamente.

> [!example]- Alucinaciones de la IA
> Un modelo de lenguaje siempre responde (alta disponibilidad), pero a veces responde con seguridad algo incorrecto, como "la raíz cuadrada de 144 es 11". Integrar componentes de IA exige estrategias de confiabilidad: validar sus salidas, tener un fallback y supervisión humana.

> [!warning] Confiabilidad no es disponibilidad
> - **Disponibilidad:** ¿el sistema **responde**?
> - **Confiabilidad:** ¿responde **correctamente** y sin perder datos?
> Un sistema puede estar disponible y no ser confiable (el Patriot, una IA que alucina), o ser confiable pero tener baja disponibilidad (un sistema que se apaga cada noche, pero nunca pierde una transacción).

## Preguntas de repaso

> [!question]- Defina confiabilidad y diferénciela de disponibilidad con un ejemplo.
> La confiabilidad es que el sistema proteja su funcionamiento y sus datos y haga correctamente su trabajo. La disponibilidad es que esté operativo y responda. El misil Patriot estaba disponible (encendido), pero no era confiable, porque su error de reloj acumulado lo hacía fallar la intercepción.

> [!question]- ¿Qué rol juegan QoS y SLAs en la confiabilidad?
> QoS define garantías de las comunicaciones, como que un mensaje llegue al menos una vez. Los SLAs comprometen niveles medibles (durabilidad de datos, resistencia a caídas) en los contratos. Ambos convierten la confiabilidad en promesas verificables.

> [!question]- Escriba un escenario de confiabilidad para un sistema de pagos.
> Fuente: el proveedor de pagos. Estímulo: confirma un cobro y luego se cae antes de responder. Entorno: operación normal. Artefacto: el servicio de pagos. Respuesta: reconcilia el estado consultando al proveedor y no cobra dos veces. Medición: 0 cobros duplicados o perdidos por mes.

> [!question]- ¿Por qué la agilidad dificulta la confiabilidad?
> Porque cambiar rápido y seguido aumenta la probabilidad de introducir errores. Mantener la confiabilidad con mucha agilidad exige más tests, monitoreo y despliegues graduales.

> [!question]- ¿Qué lección deja el caso Desert Storm para la arquitectura?
> Que pequeños errores acumulados en la ejecución pueden producir fallas catastróficas aunque el sistema esté operativo. Hay que prever fallas (reinicios, sincronización de relojes, monitoreo de la deriva) y no confundir "funcionando" con "funcionando bien".

> [!question]- ¿Por qué la IA hace más importante la confiabilidad?
> Porque los modelos tienen salidas no deterministas que pueden ser incorrectas con apariencia de correctas (alucinaciones). Hay que validar sus salidas, tener un fallback y supervisión humana para que el sistema siga siendo confiable.

> [!question]- V o F: "Un sistema con 99,999% de disponibilidad es necesariamente confiable".
> Falso. Puede estar casi siempre arriba y aun así perder datos o entregar resultados incorrectos. Disponibilidad y confiabilidad son atributos distintos.
