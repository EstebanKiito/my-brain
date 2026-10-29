---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Multiplexores y demultiplexores"
tags:
  - algoritmos/demultiplexores
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[01 - Multiplexor (MUX)|Multiplexor (MUX)]]"
---

# Demultiplexor (DEMUX)

El **demultiplexor** hace lo contrario del multiplexor: recibe una sola entrada y la dirige hacia una de varias salidas. La salida elegida se controla con líneas de selección. Es el componente que permite escribir un dato en uno de varios registros o posiciones de memoria.

## La idea

Si el multiplexor es un brazo que toma un papel de varios y lo pone en una ventana, el demultiplexor es un brazo que toma un papel de la ventana y lo deja en uno de varios casilleros. En cada momento, el dato llega a una sola salida; las demás quedan en 0.

Un DEMUX con $2^n$ salidas necesita $n$ líneas de selección.

## Demultiplexor de 1 a 4

Con una entrada $I$, dos líneas de selección $S_1$ y $S_0$, y cuatro salidas $Y_0, Y_1, Y_2, Y_3$:

| $S_1$ | $S_0$ | Salida activa |
|---:|---:|---|
| 0 | 0 | $Y_0 = I$ |
| 0 | 1 | $Y_1 = I$ |
| 1 | 0 | $Y_2 = I$ |
| 1 | 1 | $Y_3 = I$ |

Las salidas que no están seleccionadas valen 0.

![Demultiplexor de 1 a 4: una entrada I se dirige a una de las cuatro salidas según s1 y s0](adjuntos/Demultiplexor%201%20a%204.png)

> [!example]- Transcripción de la imagen
> - Una entrada $I$ a la izquierda.
> - Un bloque "1 x 4 De-Multiplexer".
> - Cuatro salidas $Y_3, Y_2, Y_1, Y_0$ a la derecha.
> - Dos líneas de selección, $s_1$ y $s_0$, en la parte inferior.

## MUX y DEMUX son complementarios

| Componente | Entradas | Salidas | Función |
|---|---:|---:|---|
| **MUX** | $N$ | 1 | Elige una entrada y la envía a la salida |
| **DEMUX** | 1 | $N$ | Envía la entrada a una de las salidas |

> [!tip] La idea central
> El MUX es de $N$ a 1; el DEMUX es de 1 a $N$. Juntos permiten seleccionar y distribuir datos en un circuito.

> [!warning] Las salidas no seleccionadas no desaparecen
> En un DEMUX, las salidas que no se eligen quedan en 0 (o desconectadas, según el diseño). El dato no se copia a todas: solo llega a la salida seleccionada.

## Preguntas de repaso

> [!question]- ¿Cuántas líneas de selección necesita un DEMUX de 1 a 8?
> Tres, porque $2^3 = 8$ salidas posibles.

> [!question]- ¿Qué diferencia hay entre un MUX y un DEMUX?
> El MUX elige una de varias entradas y la lleva a una salida. El DEMUX toma una entrada y la lleva a una de varias salidas.

> [!question]- Si un DEMUX de 1 a 4 tiene $S_1 = 1$ y $S_0 = 0$, ¿qué salida recibe el dato?
> La salida $Y_2$, porque la combinación 10 corresponde a la tercera salida (índice 2).

> [!question]- ¿Para qué sirve un DEMUX en un computador?
> Para escribir un dato en uno de varios registros o posiciones de memoria, seleccionando el destino.
