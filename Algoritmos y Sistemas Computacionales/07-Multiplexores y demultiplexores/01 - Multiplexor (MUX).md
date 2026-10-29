---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Multiplexores y demultiplexores"
tags:
  - algoritmos/multiplexores
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[03 - Comparadores y enabler|Comparadores y enabler]]"
---

# Multiplexor (MUX)

Un **multiplexor** es un circuito que tiene varias entradas de datos y una sola salida, y permite elegir cuál de las entradas se lee. La elección se controla con una o más **líneas de selección**. Es uno de los componentes que permiten que un computador decida qué dato usar en cada momento.

## La idea

Imagina una mesa con varios papeles y una sola ventana de salida. Un multiplexor es como un brazo que, según una señal, toma uno de los papeles y lo pone en la ventana. Las entradas no se mezclan: en cada momento pasa exactamente una.

Un MUX con $2^n$ entradas necesita $n$ líneas de selección, porque con $n$ bits se pueden formar $2^n$ combinaciones distintas.

## Multiplexor de 2 entradas

El caso más simple tiene dos entradas de 1 bit, $A_0$ y $B_0$, una señal de selección $S$ y una salida $M_0$:

- Si $S = 0$, la salida es $A_0$.
- Si $S = 1$, la salida es $B_0$.

| $S$ | $M_0$ |
|---:|---|
| 0 | $A_0$ |
| 1 | $B_0$ |

El circuito se construye con dos compuertas AND y una OR: una AND deja pasar $A_0$ cuando $S = 0$ (usando $\neg S$), la otra deja pasar $B_0$ cuando $S = 1$, y la OR junta las dos salidas.

![Multiplexor de 2 entradas de 1 bit: dos AND, una OR y la señal de selección S](adjuntos/Multiplexor%20de%202%20entradas.png)

> [!example]- Transcripción de la imagen
> - Entradas $A_0$ y $B_0$; señal de selección $S$; salida $M_0$.
> - La señal $S$ entra directa a una AND y negada (con un NOT) a la otra.
> - Las salidas de las dos AND se unen con una OR.
> - El bloque se rotula "1-bit Mux".

## Multiplexor de 4 entradas

Con cuatro entradas $I_0, I_1, I_2, I_3$ hacen falta dos líneas de selección, $S_1$ y $S_0$:

| $S_1$ | $S_0$ | Salida $Y$ |
|---:|---:|---|
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

> [!tip] La regla de las líneas de selección
> Para elegir entre $N$ entradas se necesitan $\log_2 N$ líneas de selección. Con 2 entradas, 1 línea; con 4, 2 líneas; con 8, 3 líneas; con 16, 4 líneas.

## Multiplexores de varios bits

Un MUX no está limitado a datos de 1 bit. Un multiplexor de 4 entradas de 4 bits elige uno de cuatro buses de 4 bits y lo envía a la salida. En los diagramas, cada línea se anota con el número de bits que transporta: el selector tiene 2 bits porque hay 4 entradas, y los datos tienen 4 bits.

> [!warning] No confundir el ancho de los datos con las líneas de selección
> En un MUX de 4 entradas de 4 bits, el selector tiene 2 bits (para elegir entre 4) y cada entrada tiene 4 bits (el dato). Son dos cantidades distintas.

## Preguntas de repaso

> [!question]- ¿Cuántas líneas de selección necesita un MUX de 8 entradas?
> Tres, porque $2^3 = 8$. Con tres bits se forman ocho combinaciones.

> [!question]- ¿Qué salida entrega un MUX de 2 entradas cuando $S = 0$?
> La entrada $A_0$. Cuando $S = 1$, entrega $B_0$.

> [!question]- ¿Por qué un MUX no mezcla las entradas?
> Porque las compuertas AND dejan pasar solo una entrada a la vez, según la señal de selección. Las demás quedan bloqueadas.

> [!question]- ¿Para qué sirve un multiplexor en un computador?
> Para elegir entre varios datos o registros: por ejemplo, decidir qué valor entra a la ALU o qué operación se ejecuta.
