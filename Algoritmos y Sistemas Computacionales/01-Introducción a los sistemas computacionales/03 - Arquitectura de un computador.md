---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Introducción a los sistemas computacionales"
tags:
  - algoritmos/arquitectura
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un programa|Qué es un programa]]"
---

# Arquitectura de un computador

Un programa necesita dónde ejecutarse y dónde guardar sus datos. La **arquitectura** del computador describe las piezas que lo forman y cómo se comunican. Esta nota presenta el modelo simplificado que usa el curso: una CPU, una memoria principal y los dispositivos de entrada/salida, unidos por buses.

## Las tres piezas principales

| Componente | Qué hace | Ejemplos |
|---|---|---|
| **CPU** (*Central Processing Unit*) | Ejecuta las instrucciones | Procesador del computador |
| **Memoria principal** | Guarda instrucciones y datos mientras el programa corre | RAM |
| **Entrada/salida (I/O)** | Comunica al computador con el mundo | Teclado, mouse, pantalla, disco |

> [!tip] La idea central
> La CPU no guarda los programas: los lee desde la memoria, los ejecuta y escribe los resultados. La memoria es el espacio de trabajo; el disco es el almacenamiento permanente.

## La CPU por dentro

La CPU contiene tres elementos que aparecen en el diagrama:

- **PC** (*Program Counter*): registro que guarda la dirección de la próxima instrucción a ejecutar.
- **Registros**: espacios muy pequeños y rápidos donde la CPU guarda los datos con los que trabaja en este momento.
- **ALU** (*Arithmetic Logic Unit*): circuito que hace las operaciones aritméticas y lógicas (sumar, restar, comparar, AND, OR…).

El ciclo básico se repite sin parar: el PC indica una dirección, la CPU **busca** la instrucción en memoria, la **decodifica** para saber qué hacer, la **ejecuta** en la ALU (si corresponde) y **escribe** el resultado. Al final, el PC avanza a la instrucción siguiente.

```mermaid
flowchart LR
    PC["PC<br/>dirección"] --> M["Memoria"]
    M --> D["Decodificar"]
    D --> A["ALU / ejecutar"]
    A --> R["Registros"]
    R --> PC
```

## Memoria y buses

La **memoria principal** (RAM) es un gran arreglo de bytes, cada uno con su propia **dirección**. Allí viven tanto las instrucciones del programa como sus datos.

Las piezas no están sueltas: se comunican por **buses**, que son conjuntos de líneas por donde viajan datos, direcciones y señales de control. El diagrama muestra tres niveles:
- **Bus de sistema:** conecta la CPU con el resto.
- **Bus de memoria:** conecta la memoria principal con el puente de I/O.
- **Bus de I/O:** conecta los controladores de dispositivos.

El **I/O bridge** (puente) traduce y conecta esos mundos. Los **controladores** (USB, gráfico, disco) manejan cada dispositivo y lo hacen aparecer ante la CPU de forma uniforme.

![Arquitectura de un computador: CPU, memoria principal, buses y dispositivos de entrada/salida](adjuntos/Arquitectura%20de%20un%20computador.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, la **CPU** con el **PC**, los **registros** y la **ALU**.
> - A la derecha, la **memoria principal (RAM)**.
> - Entre ambos, el **bus de sistema** y el **I/O bridge**; abajo, el **bus de I/O**.
> - Colgando del bus de I/O: controlador USB (teclado y mouse), adaptador gráfico (pantalla), controlador de disco (disco) y otros adaptadores.

> [!warning] Jerarquía de velocidades
> La CPU es muchísimo más rápida que la memoria y el disco. Por eso existen cachés y por eso un programa que lee mucho disco se siente lento aunque el procesador esté ocioso. Esa diferencia es la razón de ser de los sistemas operativos, que administran quién usa cada recurso.

## Preguntas de repaso

> [!question]- ¿Cuáles son los tres componentes principales de un computador según este modelo?
> La CPU, la memoria principal y los dispositivos de entrada/salida, conectados por buses.

> [!question]- ¿Para qué sirve el PC y qué pasa con él después de ejecutar una instrucción?
> Guarda la dirección de la próxima instrucción. Después de ejecutarla, avanza a la siguiente dirección, salvo que la instrucción sea un salto.

> [!question]- ¿Por qué la CPU no puede ejecutar un programa que está solo en el disco?
> Porque la CPU lee las instrucciones desde la memoria principal. El sistema operativo debe cargar primero el programa desde el disco a la RAM.

> [!question]- ¿Qué diferencia hay entre un registro y la memoria principal?
> Un registro es un espacio muy pequeño y rapidísimo dentro de la CPU; la memoria principal es grande y más lenta. La CPU trae datos desde memoria a registros para operar con ellos.
