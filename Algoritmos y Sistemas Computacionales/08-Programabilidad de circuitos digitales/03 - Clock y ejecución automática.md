---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Programabilidad de circuitos digitales"
tags:
  - algoritmos/arquitectura
  - algoritmos/clock
  - origen/complemento
prerrequisitos:
  - "[[02 - Memoria de instrucciones y PC|Memoria de instrucciones y PC]]"
---

# Clock y ejecución automática

Para que el computador ejecute un programa sin que una persona avance las instrucciones, necesita un **clock** (reloj): una señal que pulsa a intervalos regulares y marca el ritmo de los ciclos. Cada pulso hace que se ejecute una instrucción.

## Qué es el clock

El **clock** es una señal cuadrada que alterna entre 0 y 1. Cada transición marca un **ciclo**. Los componentes del computador sincronizan sus cambios con ese ritmo: los registros se actualizan al inicio o al final de cada pulso, y así todos trabajan coordinados.

Sin clock, cada parte del circuito cambiaría en un momento distinto y los datos podrían leerse antes de estar listos.

> [!tip] La idea central
> El clock es el metrónomo del computador. Un pulso, un ciclo; un ciclo, una instrucción (en el modelo simplificado del curso).

## Frecuencia

La **frecuencia** del clock se mide en hertz (Hz): la cantidad de pulsos por segundo.

- 1 Hz = 1 pulso por segundo.
- 1 kHz = $10^3$ pulsos por segundo.
- 1 MHz = $10^6$ pulsos por segundo.
- 1 GHz = $10^9$ pulsos por segundo.

El **período** es el tiempo entre dos pulsos: $T = 1/f$. A 1 GHz, cada ciclo dura $10^{-9}$ segundos, es decir, 1 nanosegundo.

Si en cada ciclo se ejecuta una instrucción, un procesador de 1 GHz podría ejecutar hasta $10^9$ instrucciones por segundo. Es una cota ideal: en la práctica hay instrucciones que tardan más de un ciclo, accesos a memoria y otras demoras.

## Qué significa realmente 1 GHz

Que el procesador tenga un clock de 1 GHz significa que puede completar del orden de mil millones de ciclos por segundo. No significa que todos los programas vayan a esa velocidad: depende de cuántos ciclos necesita cada instrucción y de cuánto tiempo espera el procesador a la memoria o al disco.

> [!warning] Más núcleos no siempre es más rápido
> Un procesador con 4 núcleos puede ejecutar hasta 4 tareas en paralelo, pero un programa que no está preparado para repartir su trabajo no se acelera 4 veces. La velocidad de un solo programa depende de su propio paralelismo y de los cuellos de botella.

## Preguntas de repaso

> [!question]- ¿Para qué sirve el clock en un computador?
> Para sincronizar los componentes y marcar el ritmo de los ciclos. Cada pulso permite que los registros y la memoria se actualicen de forma coordinada.

> [!question]- ¿Qué significa que un procesador funcione a 1 GHz?
> Que su clock produce $10^9$ pulsos por segundo, es decir, mil millones de ciclos por segundo.

> [!question]- ¿Un procesador de 1 GHz ejecuta siempre mil millones de instrucciones por segundo?
> No necesariamente. Es una cota ideal: algunas instrucciones requieren más de un ciclo y hay esperas por memoria o por otros recursos.

> [!question]- ¿Por qué cuatro núcleos no hacen que un programa cualquiera sea cuatro veces más rápido?
> Porque el programa debe poder dividirse en tareas paralelas. Si es secuencial, los núcleos extra no ayudan.

> [!question]- ¿Cuál es el período de un clock de 1 GHz?
> $T = 1/f = 1/10^9$ segundos, es decir, 1 nanosegundo por ciclo.
